"""Renderiza y monta los Shorts de un vídeo (shorts/short_NN con escenas_v2.json y audio/) que aún no tengan su MP4 final en output/.
Uso: python3 herramientas/render_shorts.py CARPETA_VIDEO [ids...]   (lanzar con `nice -n 5`)"""
import json, os, subprocess, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.abspath(sys.argv[1]); solo = sys.argv[2:]
for d in sorted(os.listdir(os.path.join(V, "shorts"))):
    if not d.startswith("short_") or (solo and d[6:] not in solo):
        continue
    S = os.path.join(V, "shorts", d)
    esc = json.load(open(os.path.join(S, "escenas_v2.json"), encoding="utf-8"))
    final = os.path.normpath(os.path.join(S, esc["salida"]))
    if os.path.exists(final) and os.path.getsize(final) > 300000:
        continue
    r1 = subprocess.run(["node", os.path.join(RAIZ, "herramientas", "escenas.js"), S], capture_output=True, text=True)
    r2 = subprocess.run([sys.executable, os.path.join(RAIZ, "herramientas", "finalizar_video.py"), S, "1.5"], capture_output=True, text=True)
    print(d, "OK" if os.path.exists(final) else "ERROR " + (r1.stderr + r2.stderr)[-300:], flush=True)
print("SHORTS TERMINADOS", flush=True)
