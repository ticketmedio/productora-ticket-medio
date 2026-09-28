"""Cambia la PRIMERA frase de la voz de un Short por otra (misma voz), para que el gancho funcione suelto.

Uso: python herramientas/short_intro.py CARPETA_SHORT "Frase nueva." [voz] [velocidad]
- Genera la frase con voz.py, la recorta y la une al resto del audio (desde la pausa tras la 1.ª frase).
- Reescribe audio/subtitulos.srt (frases) y audio/subtitulos_cortos.srt (trozos de 4 palabras).
"""
import os, re, shutil, subprocess, sys, tempfile
from comun import FFMPEG, FFPROBE, RAIZ

sys.stdout.reconfigure(encoding="utf-8")
d = os.path.join(os.path.abspath(sys.argv[1]), "audio")
frase = sys.argv[2]
voz = sys.argv[3] if len(sys.argv) > 3 else "es-ES-Tristan:DragonHDLatestNeural"
vel = sys.argv[4] if len(sys.argv) > 4 else "-12%"

def seg(s):
    h, m, r = s.split(":"); x, ms = r.split(","); return int(h) * 3600 + int(m) * 60 + int(x) + int(ms) / 1000
def fmt(t):
    ms = int(round(max(t, 0) * 1000)); return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"
def leer(p):
    out = []
    for b in open(p, encoding="utf-8").read().strip().split("\n\n"):
        l = b.splitlines(); a, z = l[1].split(" --> "); out.append((seg(a), seg(z), " ".join(l[2:])))
    return out
def dur(p):
    return float(subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout)

frases = leer(os.path.join(d, "subtitulos.srt"))
# corte: centro del hueco entre la 1.ª y la 2.ª frase (mejor, el silencio real más cercano)
t = (frases[0][1] + frases[1][0]) / 2
r = subprocess.run([FFMPEG, "-hide_banner", "-nostats", "-i", os.path.join(d, "voz.mp3"), "-af", "silencedetect=noise=-38dB:d=0.12", "-f", "null", "-"], capture_output=True, text=True)
sil = list(zip(map(float, re.findall(r"silence_start: ([\d.]+)", r.stderr)), map(float, re.findall(r"silence_end: ([\d.]+)", r.stderr))))
if sil:
    c = min(((a + b) / 2 for a, b in sil), key=lambda x: abs(x - t))
    if abs(c - t) < 1.5:
        t = c

tmp = tempfile.mkdtemp()
open(os.path.join(tmp, "f.txt"), "w", encoding="utf-8").write(frase)
subprocess.run([sys.executable, os.path.join(RAIZ, "herramientas", "voz.py"), os.path.join(tmp, "f.txt"), os.path.join(tmp, "v"), "--voz", voz, f"--velocidad={vel}"],
               check=True, stdout=subprocess.DEVNULL)
if not os.path.exists(os.path.join(d, "voz_original.mp3")):
    shutil.copy(os.path.join(d, "voz.mp3"), os.path.join(d, "voz_original.mp3"))
f1 = os.path.join(tmp, "f1.wav")
subprocess.run([FFMPEG, "-v", "error", "-y", "-i", os.path.join(tmp, "v", "voz.mp3"), "-af",
                "silenceremove=start_periods=1:start_threshold=-40dB,areverse,silenceremove=start_periods=1:start_threshold=-40dB,areverse,adelay=150,apad=pad_dur=0.3", f1], check=True)
resto = os.path.join(tmp, "resto.wav")
subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", os.path.join(d, "voz_original.mp3"), resto], check=True)
subprocess.run([FFMPEG, "-v", "error", "-y", "-i", f1, "-i", resto, "-filter_complex", "[0][1]concat=n=2:v=0:a=1",
                "-c:a", "libmp3lame", "-b:a", "192k", os.path.join(d, "voz.mp3")], check=True)
d1 = dur(f1); desp = d1 - t

nuevas = [(0.15, d1 - 0.3, frase)] + [(a + desp, z + desp, x) for a, z, x in frases[1:]]
cortos = []
for a, z, x in nuevas:
    pal = x.split(); n = max(1, -(-len(pal) // 4)); p = (z - a) / n
    cortos += [(a + q * p, a + (q + 1) * p, " ".join(pal[q * 4:(q + 1) * 4])) for q in range(n)]
for nombre, filas in (("subtitulos.srt", nuevas), ("subtitulos_cortos.srt", cortos)):
    open(os.path.join(d, nombre), "w", encoding="utf-8").write("\n".join(f"{k + 1}\n{fmt(a)} --> {fmt(z)}\n{x}\n" for k, (a, z, x) in enumerate(filas)))
shutil.rmtree(tmp, ignore_errors=True)
print(f"✓ {sys.argv[1]}: frase nueva de {d1:.1f} s; audio total {dur(os.path.join(d, 'voz.mp3')):.1f} s")
