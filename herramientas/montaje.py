"""Monta un vídeo a partir de un guion de escenas (JSON) con FFmpeg.

Uso:
  python montaje.py escenas.json

Formato de escenas.json (las rutas son relativas al propio JSON):
{
  "salida": "output/FINAL_YOUTUBE_1080P.mp4",
  "formato": "horizontal",            # horizontal (1920x1080) | vertical (1080x1920)
  "voz": "audio/voz.mp3",
  "musica": "audio/musica.mp3",       # opcional
  "musica_db": -24,                   # volumen de la música respecto a la voz
  "subtitulos": "06_SUBTITULOS.srt",  # opcional
  "quemar_subtitulos": false,         # true en Shorts/Reels (subtítulos grandes dentro del vídeo)
  "escenas": [
    {"archivo": "images/IMAGE_001.png", "duracion": 5.5, "movimiento": "zoom_in",
     "texto": "3 € fabricarlo", "posicion_texto": "abajo", "fundido": false}
  ]
}
Movimientos: zoom_in, zoom_out, pan_izq, pan_der, pan_arriba, pan_abajo, estatico.
Los archivos pueden ser imágenes (png/jpg/webp) o vídeos (mp4/mov/webm).
Si la suma de duraciones no llega al final de la voz, la última escena se alarga.
"""
import json, os, subprocess, sys, tempfile, shutil
from comun import FFMPEG, FFPROBE, RAIZ

sys.stdout.reconfigure(encoding="utf-8")
FPS = 30
FUENTE = os.path.join(RAIZ, "herramientas", "fuentes", "ArchivoBlack-Regular.ttf")
FUENTE_RESERVA = r"C:\Windows\Fonts\arialbd.ttf"
VIDEO_EXT = (".mp4", ".mov", ".webm", ".mkv", ".m4v")


def run(args):
    r = subprocess.run([FFMPEG, "-y", "-loglevel", "error"] + args, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("FFmpeg falló:\n" + r.stderr[-2000:])


def duracion(ruta):
    out = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "json", ruta],
                         capture_output=True, text=True, check=True).stdout
    return float(json.loads(out)["format"]["duration"])


def ff_texto(s):
    return s.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\u2019").replace("%", "\\%")


def ff_ruta(p):
    return p.replace("\\", "/").replace(":", "\\:")


def filtro_movimiento(mov, n, W, H):
    # Se amplía la imagen antes del zoompan para que el movimiento sea suave (sin temblores)
    base = f"scale={W*4}:{H*4}:force_original_aspect_ratio=increase,crop={W*4}:{H*4},"
    z_in = f"zoompan=z='1+0.12*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
    z_out = f"zoompan=z='1.12-0.12*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
    pans = {
        "pan_der": f"zoompan=z=1.12:x='(iw-iw/zoom)*on/{n}':y='ih/2-(ih/zoom/2)'",
        "pan_izq": f"zoompan=z=1.12:x='(iw-iw/zoom)*(1-on/{n})':y='ih/2-(ih/zoom/2)'",
        "pan_abajo": f"zoompan=z=1.12:x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*on/{n}'",
        "pan_arriba": f"zoompan=z=1.12:x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*(1-on/{n})'",
    }
    if mov == "estatico":
        return f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}"
    zp = {"zoom_in": z_in, "zoom_out": z_out}.get(mov) or pans.get(mov, z_in)
    return base + zp + f":d={n}:s={W}x{H}:fps={FPS}"


def render_escena(esc, i, carpeta, tmp, W, H):
    ruta = os.path.join(carpeta, esc["archivo"])
    if not os.path.exists(ruta):
        sys.exit(f"Falta el archivo de la escena {i+1}: {esc['archivo']}")
    dur = float(esc["duracion"])
    n = max(1, round(dur * FPS))
    salida = os.path.join(tmp, f"e{i:04d}.mp4")
    es_video = ruta.lower().endswith(VIDEO_EXT)

    if es_video:
        entrada = ["-stream_loop", "-1", "-i", ruta]
        vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},trim=end_frame={n},setpts=PTS-STARTPTS"
    else:
        mov = esc.get("movimiento", "zoom_in")
        entrada = (["-loop", "1", "-framerate", str(FPS)] if mov == "estatico" else []) + ["-i", ruta]
        vf = filtro_movimiento(mov, n, W, H)

    if esc.get("texto"):
        fuente = ff_ruta(FUENTE if os.path.exists(FUENTE) else FUENTE_RESERVA)
        tam = int(H * (0.075 if W > H else 0.05))
        y = {"arriba": "h*0.08", "centro": "(h-text_h)/2"}.get(esc.get("posicion_texto", "abajo"), "h*0.80-text_h")
        vf += (f",drawtext=fontfile='{fuente}':text='{ff_texto(esc['texto'])}':fontsize={tam}:fontcolor=0xFBFAF6"
               f":box=1:boxcolor=0x12161C@0.82:boxborderw={int(tam*0.35)}:x=(w-text_w)/2:y={y}")
    if esc.get("fundido"):
        vf += f",fade=t=in:st=0:d=0.3,fade=t=out:st={max(0, dur-0.3):.2f}:d=0.3"
    vf += ",format=yuv420p,setsar=1"

    run(entrada + ["-vf", vf, "-frames:v", str(n), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",
                   "-r", str(FPS), salida])
    return salida


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    js = os.path.abspath(sys.argv[1])
    carpeta = os.path.dirname(js)
    cfg = json.load(open(js, encoding="utf-8"))
    W, H = (1080, 1920) if cfg.get("formato") == "vertical" else (1920, 1080)
    escenas = cfg["escenas"]

    voz = os.path.join(carpeta, cfg["voz"]) if cfg.get("voz") else None
    if voz:
        total_voz = duracion(voz) + 0.8
        suma = sum(float(e["duracion"]) for e in escenas)
        if suma < total_voz:
            escenas[-1]["duracion"] = float(escenas[-1]["duracion"]) + (total_voz - suma)

    tmp = tempfile.mkdtemp(prefix="montaje_")
    try:
        partes = []
        for i, e in enumerate(escenas):
            print(f"Escena {i+1}/{len(escenas)}…", flush=True)
            partes.append(render_escena(e, i, carpeta, tmp, W, H))
        lista = os.path.join(tmp, "lista.txt")
        with open(lista, "w", encoding="utf-8") as f:
            for p in partes:
                f.write(f"file '{p}'\n")
        solo_video = os.path.join(tmp, "video.mp4")
        run(["-f", "concat", "-safe", "0", "-i", lista, "-c", "copy", solo_video])

        salida = os.path.join(carpeta, cfg.get("salida", "output/FINAL.mp4"))
        os.makedirs(os.path.dirname(salida), exist_ok=True)
        entradas = ["-i", solo_video]
        filtros, mapa_audio = [], None
        if voz:
            entradas += ["-i", voz]
            mapa_audio = "1:a"
            if cfg.get("musica"):
                entradas += ["-stream_loop", "-1", "-i", os.path.join(carpeta, cfg["musica"])]
                db = cfg.get("musica_db", -24)
                # La música baja sola cuando habla la voz (ducking) y queda por debajo en todo momento
                filtros.append(f"[2:a]volume={db}dB,aformat=channel_layouts=stereo[m];"
                               f"[1:a]aformat=channel_layouts=stereo,asplit=2[v1][v2];"
                               f"[m][v1]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
                               f"[v2][md]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]")
                mapa_audio = "[a]"

        vf = None
        if cfg.get("subtitulos") and cfg.get("quemar_subtitulos"):
            srt = os.path.join(carpeta, cfg["subtitulos"])
            shutil.copy(srt, os.path.join(tmp, "subs.srt"))
            tam = 12 if W < H else 13
            vf = (f"subtitles=subs.srt:force_style='FontName=Arial,Bold=1,FontSize={tam},PrimaryColour=&H00F6FAFB,"
                  f"OutlineColour=&H001C1612,BorderStyle=1,Outline=3,Shadow=0,Alignment=2,MarginV={int(H*0.035)}'")

        args = entradas
        if filtros:
            args += ["-filter_complex", ";".join(filtros)]
        if vf:
            args += ["-vf", vf]
        args += ["-map", "0:v"] + (["-map", mapa_audio] if mapa_audio else [])
        args += ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS),
                 "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart", salida]
        cwd = os.getcwd()
        os.chdir(tmp)  # para que el filtro de subtítulos encuentre subs.srt sin problemas de rutas en Windows
        try:
            run(args)
        finally:
            os.chdir(cwd)
        print(f"Vídeo listo: {salida} ({duracion(salida):.1f} s)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
