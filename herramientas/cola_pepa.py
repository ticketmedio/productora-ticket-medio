"""Renderiza, uno detrás de otro, todos los Reels de Pepa de redes/pepa_pita/lote/*.json que aún no tienen MP4.
Uso: python3 herramientas/cola_pepa.py [desde_nº] [hasta_nº]   (se puede lanzar con `nice -n 10`)"""
import glob, json, os, subprocess, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
desde = int(sys.argv[1]) if len(sys.argv) > 1 else 0
hasta = int(sys.argv[2]) if len(sys.argv) > 2 else 999
for ficha in sorted(glob.glob(os.path.join(RAIZ, "redes", "pepa_pita", "lote", "*.json"))):
    n = int(os.path.basename(ficha)[:3])
    if not desde <= n <= hasta:
        continue
    f = json.load(open(ficha, encoding="utf-8"))
    mp4 = os.path.join(RAIZ, "redes", "pepa_pita", "videos", f"{f['id']}_{f['slug']}", "salida", f"PEPA_{f['id']}_{f['slug']}.mp4")
    if os.path.exists(mp4) and os.path.getsize(mp4) > 500000:
        continue
    r = subprocess.run([sys.executable, os.path.join(RAIZ, "herramientas", "pepa_lote.py"), ficha], capture_output=True, text=True)
    print(f['id'], 'OK' if 'OK' in r.stdout else 'ERROR ' + (r.stdout + r.stderr)[-300:], flush=True)
print("COLA TERMINADA", flush=True)
