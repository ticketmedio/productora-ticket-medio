"""Genera la locución con Azure Speech y unos subtítulos sincronizados.

Uso:
  python voz.py GUION.txt CARPETA_SALIDA [--voz es-ES-AlvaroNeural] [--velocidad 0%]

- Lee la clave y la región de config/claves.txt.
- Divide el texto por párrafos (una petición por párrafo, respetando el límite del plan gratuito).
- Une los audios con FFmpeg y crea voz.mp3 y subtitulos.srt. Los tiempos del SRT
  salen de la duración real de cada párrafo, repartida por frases según su longitud.
"""
import argparse, json, os, re, subprocess, sys, time, urllib.request, urllib.error
from xml.sax.saxutils import escape
from comun import FFMPEG, FFPROBE

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAVES = os.path.join(RAIZ, "config", "claves.txt")


def leer_claves():
    datos = {}
    with open(CLAVES, encoding="utf-8") as f:
        for linea in f:
            if ":" in linea:
                k, v = linea.split(":", 1)
                datos[k.strip()] = v.strip()
    clave, region = datos.get("AZURE_VOZ_CLAVE", ""), datos.get("AZURE_VOZ_REGION", "").lower().replace(" ", "")
    if not clave or not region:
        sys.exit("Falta la clave o la región de Azure en config/claves.txt")
    return clave, region


def tts(texto, voz, velocidad, clave, region, destino, estilo=None):
    cuerpo = f'<prosody rate="{velocidad}">{escape(texto)}</prosody>'
    if estilo:  # estilos expresivos (solo algunas voces, p. ej. Marta)
        cuerpo = f'<mstts:express-as style="{estilo}">{cuerpo}</mstts:express-as>'
    ssml = (
        '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
        'xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="es-ES">'
        f'<voice name="{voz}">{cuerpo}</voice></speak>'
    )
    req = urllib.request.Request(
        f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1",
        data=ssml.encode("utf-8"),
        headers={
            "Ocp-Apim-Subscription-Key": clave,
            "Content-Type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
            "User-Agent": "ticketmedio",
        },
    )
    for intento in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                open(destino, "wb").write(r.read())
            return
        except urllib.error.HTTPError as e:
            if e.code == 429:  # límite del plan gratuito: esperar y reintentar
                time.sleep(15 * (intento + 1))
                continue
            sys.exit(f"Error de Azure {e.code}: {e.read()[:300]!r}")
    sys.exit("Azure sigue rechazando peticiones (límite de uso). Prueba más tarde.")


def duracion(ruta):
    out = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "json", ruta],
                         capture_output=True, text=True, check=True).stdout
    return float(json.loads(out)["format"]["duration"])


def frases(parrafo):
    partes = re.split(r"(?<=[.!?…])\s+", parrafo.strip())
    salida = []
    for p in partes:  # frases largas: cortar por comas para que el subtítulo quepa en pantalla
        while len(p) > 90 and "," in p[20:]:
            corte = p.find(",", 40 if len(p) > 60 else 20)
            if corte == -1:
                break
            salida.append(p[: corte + 1])
            p = p[corte + 1 :].strip()
        salida.append(p)
    return [s for s in salida if s]


def ts(seg):
    ms = int(round(seg * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("guion")
    ap.add_argument("salida")
    ap.add_argument("--voz", default="es-ES-Tristan:DragonHDLatestNeural")  # voz de Ticket Medio
    ap.add_argument("--velocidad", default="-12%")  # ≈160 palabras por minuto
    ap.add_argument("--estilo", default=None, help="estilo expresivo, p. ej. friendlycheerful")
    ap.add_argument("--pausa", type=float, default=0.35, help="silencio entre párrafos (s)")
    a = ap.parse_args()

    clave, region = leer_claves()
    os.makedirs(a.salida, exist_ok=True)
    tmp = os.path.join(a.salida, "_trozos")
    os.makedirs(tmp, exist_ok=True)

    texto = open(a.guion, encoding="utf-8").read()
    parrafos = [p.strip() for p in re.split(r"\n\s*\n", texto) if p.strip()]

    silencio = os.path.join(tmp, "silencio.wav")
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                    "-t", str(a.pausa), silencio], check=True)

    lista, srt, t, n = [], [], 0.0, 1
    for i, p in enumerate(parrafos, 1):
        ruta = os.path.join(tmp, f"p{i:03d}.wav")
        if not os.path.exists(ruta):
            print(f"Voz {i}/{len(parrafos)}…")
            tts(p, a.voz, a.velocidad, clave, region, ruta, a.estilo)
            time.sleep(3.2)  # plan gratuito: máx. 20 peticiones por minuto
        dur = duracion(ruta)
        fr = frases(p)
        total = sum(len(f) for f in fr) or 1
        inicio = t
        for f in fr:
            d = dur * len(f) / total
            srt.append(f"{n}\n{ts(inicio)} --> {ts(inicio + d)}\n{f}\n")
            inicio += d
            n += 1
        lista += [ruta, silencio]
        t += dur + a.pausa

    concat = os.path.join(tmp, "lista.txt")
    with open(concat, "w", encoding="utf-8") as f:
        for r in lista:
            f.write(f"file '{os.path.abspath(r)}'\n")
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", concat,
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "libmp3lame", "-b:a", "192k",
                    os.path.join(a.salida, "voz.mp3")], check=True)
    open(os.path.join(a.salida, "subtitulos.srt"), "w", encoding="utf-8").write("\n".join(srt))
    print(f"Listo: voz.mp3 ({t:.0f} s) y subtitulos.srt en {a.salida}")


if __name__ == "__main__":
    main()
