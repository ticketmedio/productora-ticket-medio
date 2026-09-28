"""Anima un vídeo vertical de Pepa Pita (1080x1920, 30 fps).

Uso: python pepa_video.py CARPETA/plan.json

plan.json (rutas relativas al propio plan):
{
  "voz": "voz/voz.mp3", "subtitulos": "voz/subtitulos.srt",
  "fondo": "../../fondos/pexels_5451503.jpg",
  "musica": "../../../../musica/pepa_pita/Travelling Light - Blue Deer Studio.mp3", "musica_db": -22,
  "cabecera": "¿LAVAS EL POLLO?",
  "planos": [{"desde": 0, "imagen": "busto"}, {"desde": 2.0, "imagen": "pose_ojo"}],
  "rotulos": [{"desde": 21.2, "hasta": 23.3, "texto": "168.396 CASOS", "sub": "UE · 2024 · EFSA"}],
  "salida": "salida/PEPA_001.mp4"
}
«busto» usa el primer plano con el pico que se abre al ritmo de la voz.
Las demás imágenes son los recortes de redes/pepa_pita/recortes (exp_*, pose_*).
"""
import json, math, os, re, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from comun import FFMPEG, FFPROBE, RAIZ

sys.stdout.reconfigure(encoding="utf-8")
W, H, FPS = 1080, 1920, 30
REC = os.path.join(RAIZ, "redes", "pepa_pita", "recortes")
FUENTE = os.path.join(RAIZ, "herramientas", "fuentes", "ArchivoBlack-Regular.ttf")
ROJO, AMARILLO, TINTA, PAPEL = (224, 96, 79), (245, 179, 1), (18, 22, 28), (251, 250, 246)


def srt(path):
    out = []
    for b in open(path, encoding="utf-8").read().strip().split("\n\n"):
        l = b.split("\n")
        a, z = l[1].split(" --> ")
        f = lambda s: int(s[:2]) * 3600 + int(s[3:5]) * 60 + int(s[6:8]) + int(s[9:]) / 1000
        out.append((f(a), f(z), " ".join(l[2:])))
    return out


def trozos(subs, maxp=4):
    """Divide cada frase en trozos cortos (estilo Reels) repartiendo el tiempo por letras."""
    res = []
    for a, z, t in subs:
        pal = t.split()
        grupos = [pal[i:i + maxp] for i in range(0, len(pal), maxp)]
        if len(grupos) > 1 and len(grupos[-1]) == 1:
            ultima = grupos.pop()
            grupos[-1] += ultima
        tot = sum(len(" ".join(g)) for g in grupos) or 1
        t0 = a
        for g in grupos:
            d = (z - a) * len(" ".join(g)) / tot
            res.append((t0, t0 + d, " ".join(g)))
            t0 += d
    return res


def envolvente(voz, n):
    raw = subprocess.run([FFMPEG, "-loglevel", "error", "-i", voz, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                         capture_output=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32)
    paso = 16000 // FPS
    rms = np.array([np.sqrt(np.mean(x[i * paso:(i + 1) * paso] ** 2)) if i * paso < len(x) else 0 for i in range(n)])
    return rms / (np.percentile(rms[rms > 0], 95) if (rms > 0).any() else 1)


def fondo_base(ruta):
    im = Image.open(ruta).convert("RGB")
    esc = max(W * 1.1 / im.width, H * 1.1 / im.height)
    im = im.resize((int(im.width * esc), int(im.height * esc)), Image.LANCZOS)
    im = im.filter(ImageFilter.GaussianBlur(7))
    return Image.eval(im, lambda v: int(v * 0.82))


def cargar(nombre, alto):
    im = Image.open(os.path.join(REC, nombre + ".png")).convert("RGBA")
    esc = alto / im.height
    im = im.resize((int(im.width * esc), alto), Image.LANCZOS)
    return im.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2)) if esc > 1.6 else im


def texto_centrado(d, y, txt, fuente, relleno, borde=10, ancho_max=980, resaltar_numeros=True):
    # parte en líneas si no cabe
    pal, lineas, act = txt.split(), [], ""
    for p in pal:
        prueba = (act + " " + p).strip()
        if d.textlength(prueba, font=fuente) > ancho_max and act:
            lineas.append(act); act = p
        else:
            act = prueba
    lineas.append(act)
    alto = fuente.size * 1.12
    for i, l in enumerate(lineas):
        x = (W - d.textlength(l, font=fuente)) / 2
        for p in l.split(" "):
            color = AMARILLO if resaltar_numeros and re.search(r"\d", p) else relleno
            d.text((x, y + i * alto), p, font=fuente, fill=color, stroke_width=borde, stroke_fill=TINTA)
            x += d.textlength(p + " ", font=fuente)
    return len(lineas) * alto


def main():
    plan_p = os.path.abspath(sys.argv[1])
    base = os.path.dirname(plan_p)
    P = json.load(open(plan_p, encoding="utf-8"))
    rel = lambda r: os.path.join(base, r)
    subs = srt(rel(P["subtitulos"]))
    dur_voz = float(subprocess.run([FFPROBE, "-v", "error", "-show_entries",
                                    "format=duration", "-of", "csv=p=0", rel(P["voz"])], capture_output=True, text=True).stdout)
    dur = dur_voz + 1.2
    n = int(dur * FPS)
    env = envolvente(rel(P["voz"]), n)
    chunks = trozos(subs)
    fondo = fondo_base(rel(P["fondo"]))
    f_sub = ImageFont.truetype(FUENTE, 84)
    f_cab = ImageFont.truetype(FUENTE, 70)
    f_rot = ImageFont.truetype(FUENTE, 96)
    f_rsub = ImageFont.truetype(FUENTE, 40)
    f_marca = ImageFont.truetype(FUENTE, 30)

    busto_c, busto_a = cargar("busto_cerrado", 1150), cargar("busto_abierto", 1150)
    cache = {}
    planos = sorted(P["planos"], key=lambda x: x["desde"])

    salida = rel(P.get("salida", "salida/PEPA.mp4"))
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    args = [FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
            "-i", rel(P["voz"])]
    if P.get("musica"):
        args += ["-stream_loop", "-1", "-i", rel(P["musica"]), "-filter_complex",
                 f"[2:a]volume={P.get('musica_db', -22)}dB,aformat=channel_layouts=stereo[m];"
                 f"[1:a]aformat=channel_layouts=stereo,asplit=2[v1][v2];"
                 f"[m][v1]sidechaincompress=threshold=0.03:ratio=5:attack=20:release=350[md];"
                 f"[v2][md]amix=inputs=2:duration=first:normalize=0,apad=pad_dur=1.2,afade=t=out:st={dur-1.0:.2f}:d=1,alimiter=limit=0.95[a]",
                 "-map", "0:v", "-map", "[a]"]
    else:
        args += ["-map", "0:v", "-map", "1:a"]
    args += ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
             "-t", f"{dur:.2f}", "-movflags", "+faststart", salida]
    ff = subprocess.Popen(args, stdin=subprocess.PIPE)

    abierto, ultimo_cambio = False, -99
    for i in range(n):
        t = i / FPS
        # fondo con zoom lento
        z = 1 + 0.06 * t / dur
        fw, fh = int(W * z), int(H * z)
        bg = fondo.crop(((fondo.width - fw) // 2, (fondo.height - fh) // 2,
                         (fondo.width - fw) // 2 + fw, (fondo.height - fh) // 2 + fh)).resize((W, H), Image.BILINEAR)
        frame = bg.convert("RGBA")

        # plano actual
        actual = planos[0]
        for p in planos:
            if t >= p["desde"]:
                actual = p
        hablando = env[i] > 0.22
        if actual["imagen"] == "busto":
            if hablando and (i - ultimo_cambio) >= 3:
                abierto = not abierto; ultimo_cambio = i
            elif not hablando:
                abierto = False
            img = busto_a if abierto else busto_c
            y_base = H - img.height + 40
        else:
            nombre = actual["imagen"]
            alto = 880 if nombre.startswith("exp_") else 1120
            if nombre not in cache:
                cache[nombre] = cargar(nombre, alto)
            img = cache[nombre]
            y_base = H - img.height - 40
        # entrada con rebote y balanceo suave
        dt = t - actual["desde"]
        pop = 1 if dt > 0.25 else 0.9 + 0.1 * math.sin(dt / 0.25 * math.pi / 2)
        bob = math.sin(t * 2 * math.pi * 0.9) * 8
        im2 = img if pop == 1 else img.resize((int(img.width * pop), int(img.height * pop)), Image.BILINEAR)
        x = (W - im2.width) // 2
        y = int(y_base + (img.height - im2.height) + bob)
        frame.alpha_composite(im2, (x, max(y, 0)) if y >= 0 else (x, 0))

        d = ImageDraw.Draw(frame)
        # marca y cabecera
        d.rounded_rectangle((W // 2 - 130, 70, W // 2 + 130, 122), 26, fill=TINTA)
        d.text((W // 2, 96), "PEPA PITA", font=f_marca, fill=AMARILLO, anchor="mm")
        cab = P.get("cabecera", "")
        if cab:
            tw = d.textlength(cab, font=f_cab)
            d.rounded_rectangle(((W - tw) / 2 - 36, 150, (W + tw) / 2 + 36, 262), 22, fill=ROJO)
            d.text((W / 2, 206), cab, font=f_cab, fill=PAPEL, anchor="mm")
        # rótulo (dato destacado)
        for r in P.get("rotulos", []):
            if r["desde"] <= t < r["hasta"]:
                k = min(1, (t - r["desde"]) / 0.2)
                fr = f_rot
                while d.textlength(r["texto"], font=fr) > W - 160 and fr.size > 40:  # que quepa siempre
                    fr = ImageFont.truetype(FUENTE, fr.size - 6)
                tw = max(d.textlength(r["texto"], font=fr), d.textlength(r.get("sub", ""), font=f_rsub))
                y0 = 310 + (1 - k) * 30
                d.rounded_rectangle(((W - tw) / 2 - 40, y0, (W + tw) / 2 + 40, y0 + 176), 18, fill=PAPEL, outline=TINTA, width=6)
                d.text((W / 2, y0 + 70), r["texto"], font=fr, fill=TINTA, anchor="mm")
                if r.get("sub"):
                    d.text((W / 2, y0 + 140), r["sub"], font=f_rsub, fill=(90, 96, 104), anchor="mm")
        # subtítulos grandes
        for a, z_, txt in chunks:
            if a <= t < z_:
                texto_centrado(d, 540, txt.upper(), f_sub, PAPEL)
                break
        ff.stdin.write(frame.convert("RGB").tobytes())
        if i % 150 == 0:
            print(f"{t:5.1f}/{dur:.1f} s", flush=True)
    ff.stdin.close()
    ff.wait()
    print("Vídeo listo:", salida)


if __name__ == "__main__":
    main()
