"""Añade a los Shorts terminados un rótulo final «Vídeo completo en el canal» (últimos 2,6 s), sin volver a renderizar las escenas.
Uso: python3 herramientas/cierre_shorts.py CARPETA_VIDEO [ids...]
Anota en privado/cierres_hechos.json los MP4 ya tratados (con su tamaño) para no repetirlo; si un Short se vuelve a renderizar, se trata de nuevo."""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
from comun import FFMPEG, FFPROBE
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.abspath(sys.argv[1]); solo = sys.argv[2:]
REG = os.path.join(RAIZ, "privado", "cierres_hechos.json")
hechos = json.load(open(REG)) if os.path.exists(REG) else {}
PNG = os.path.join(RAIZ, "privado", "cierre_banner.png")
def banner():
    im = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    f = ImageFont.truetype(os.path.join(RAIZ, "herramientas", "fuentes", "ArchivoBlack-Regular.ttf"), 46)
    t = "VÍDEO COMPLETO EN EL CANAL"; w = d.textlength(t, font=f)
    W, H, y = int(w + 150), 120, 1570; x = (1080 - W) // 2
    d.rounded_rectangle((x + 6, y + 8, x + W + 6, y + H + 8), 30, fill=(0, 0, 0, 90))
    d.rounded_rectangle((x, y, x + W, y + H), 30, fill=(245, 179, 1, 255), outline=(27, 27, 27, 255), width=6)
    tx = x + 40; cy = y + H // 2
    d.polygon([(tx, cy - 26), (tx, cy + 26), (tx + 44, cy)], fill=(224, 82, 27, 255), outline=(27, 27, 27, 255))
    d.text((tx + 78, cy), t, font=f, fill=(27, 27, 27, 255), anchor="lm")
    im.save(PNG)
banner()
for d in sorted(os.listdir(os.path.join(V, "shorts"))):
    if not d.startswith("short_") or (solo and d[6:] not in solo): continue
    S = os.path.join(V, "shorts", d)
    esc = json.load(open(os.path.join(S, "escenas_v2.json"), encoding="utf-8"))
    mp4 = os.path.normpath(os.path.join(S, esc["salida"]))
    if not os.path.exists(mp4): print(d, "no existe"); continue
    firma = os.path.getsize(mp4)
    if hechos.get(mp4) == firma: print(d, "ya tiene cierre"); continue
    dur = float(subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mp4], capture_output=True, text=True).stdout)
    ini = max(dur - 2.6, 1)
    tmp = mp4 + ".tmp.mp4"
    r = subprocess.run([FFMPEG, "-y", "-v", "error", "-i", mp4, "-loop", "1", "-i", PNG, "-filter_complex",
        f"[1:v]format=rgba,fade=in:st={ini:.2f}:d=0.3:alpha=1[b];[0:v][b]overlay=0:0:enable='gte(t,{ini:.2f})':shortest=1,format=yuv420p[v]",
        "-map", "[v]", "-map", "0:a", "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-c:a", "copy", "-movflags", "+faststart", tmp], capture_output=True, text=True)
    if r.returncode or not os.path.exists(tmp): print(d, "ERROR", r.stderr[-200:]); continue
    os.replace(tmp, mp4); hechos[mp4] = os.path.getsize(mp4)
    json.dump(hechos, open(REG, "w"), indent=1); print(d, "cierre añadido", flush=True)
