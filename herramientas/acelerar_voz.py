"""Acelera una locución sin cambiar el tono (atempo) y reescala sus subtítulos.

Uso: python herramientas/acelerar_voz.py CARPETA_VOZ 1.12
(Para voces que ignoran la velocidad de Azure, como Marta MAI-Voice-2.)
"""
import os, shutil, subprocess, sys
from comun import FFMPEG

sys.stdout.reconfigure(encoding="utf-8")
d, f = sys.argv[1], float(sys.argv[2])
voz, srt = os.path.join(d, "voz.mp3"), os.path.join(d, "subtitulos.srt")
orig = os.path.join(d, "voz_original.mp3")
if not os.path.exists(orig):
    shutil.copy(voz, orig)
    shutil.copy(srt, os.path.join(d, "subtitulos_original.srt"))
subprocess.run([FFMPEG, "-v", "error", "-y", "-i", orig, "-af", f"atempo={f}", "-c:a", "libmp3lame", "-b:a", "192k", voz], check=True)

def seg(s):
    h, m, r = s.split(":"); x, ms = r.split(","); return int(h) * 3600 + int(m) * 60 + int(x) + int(ms) / 1000
def fmt(t):
    ms = int(round(t * 1000)); return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"

bloques = []
for b in open(os.path.join(d, "subtitulos_original.srt"), encoding="utf-8").read().strip().split("\n\n"):
    l = b.splitlines(); a, z = l[1].split(" --> ")
    bloques.append(f"{l[0]}\n{fmt(seg(a) / f)} --> {fmt(seg(z) / f)}\n" + "\n".join(l[2:]) + "\n")
open(srt, "w", encoding="utf-8").write("\n".join(bloques))
print(f"✓ {d}: ×{f}")
