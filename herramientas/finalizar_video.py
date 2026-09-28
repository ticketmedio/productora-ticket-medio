"""Monta el vídeo final a partir de los clips de escenas.js: voz con cola final, música y volumen a -14 LUFS.

Uso: python herramientas/finalizar_video.py CARPETA_VIDEO [segundos_de_cola]
La salida es la que diga montaje.json (por defecto output/FINAL_YOUTUBE_1080P.mp4).
"""
import json, os, subprocess, sys
from comun import FFMPEG, RAIZ

sys.stdout.reconfigure(encoding="utf-8")
d = os.path.abspath(sys.argv[1])
cola = float(sys.argv[2]) if len(sys.argv) > 2 else 3.2
run = lambda args: subprocess.run([FFMPEG, "-v", "error", "-y"] + args, check=True)

run(["-i", os.path.join(d, "audio", "voz.mp3"), "-af", f"apad=pad_dur={cola}", "-c:a", "libmp3lame", "-b:a", "192k",
     os.path.join(d, "audio", "voz_cola.mp3")])
pm = os.path.join(d, "montaje.json")
m = json.load(open(pm, encoding="utf-8"))
final = m.get("salida_final") or m["salida"]
if final.endswith("_sin_normalizar.mp4"):
    final = "output/FINAL_YOUTUBE_1080P.mp4"
m["voz"], m["salida"], m["salida_final"] = "audio/voz_cola.mp3", "output/_sin_normalizar.mp4", final
json.dump(m, open(pm, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, os.path.join(RAIZ, "herramientas", "montaje.py"), pm], check=True)
tmp = os.path.join(d, "output", "_sin_normalizar.mp4")
run(["-i", tmp, "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
     "-movflags", "+faststart", os.path.join(d, final)])
os.remove(tmp)
print(f"✓ {final} listo")
