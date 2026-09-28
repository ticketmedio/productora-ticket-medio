"""Borra las carpetas de producción cuando ya se ha publicado todo lo que contienen.

Uso: python herramientas/limpiar_publicados.py [--simular]
Lee archivo/publicaciones.json:
  {"carpetas": [{"ruta": "redes/pepa_pita/videos/001_no_laves_el_pollo", "ultima_publicacion": "2026-09-29"}, ...]}
Una carpeta se borra al día SIGUIENTE de su última publicación (margen por si una programación falla).
Antes de borrar, copia sus textos ligeros (.txt, .md, .srt, plan/escenas .json) a archivo/<nombre>/.
"""
import datetime, json, os, shutil, sys

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(RAIZ, "archivo", "publicaciones.json")
TEXTOS = (".txt", ".md", ".srt")
JSON_UTILES = ("plan.json", "escenas_v2.json", "shorts.json", "montaje.json")
simular = "--simular" in sys.argv
hoy = datetime.date.today()

reg = json.load(open(REG, encoding="utf-8"))
for c in reg["carpetas"]:
    if c.get("borrada"):
        continue
    ruta = os.path.join(RAIZ, c["ruta"])
    fecha = datetime.date.fromisoformat(c["ultima_publicacion"])
    if hoy <= fecha:
        print(f"· Se conserva hasta después del {fecha:%d/%m}: {c['ruta']}")
        continue
    if not os.path.isdir(ruta):
        c["borrada"] = str(hoy)
        continue
    destino = os.path.join(RAIZ, "archivo", c.get("archivo", os.path.basename(c["ruta"])))
    copiados = 0
    for base, dirs, archivos in os.walk(ruta):
        dirs[:] = [d for d in dirs if not d.startswith("_")]      # sin carpetas temporales (_trozos…)
        for a in archivos:
            if a.endswith(TEXTOS) or a in JSON_UTILES:
                if "fuentes" in os.path.relpath(base, ruta).split(os.sep) and a.endswith("_raw.txt"):
                    continue                                        # textos en bruto de PDF: pesan y no hacen falta
                rel = os.path.relpath(os.path.join(base, a), ruta)
                dst = os.path.join(destino, rel)
                if not simular:
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.copy2(os.path.join(base, a), dst)
                copiados += 1
    if simular:
        print(f"✗ (simulación) Se borraría {c['ruta']} — {copiados} textos al archivo")
        continue
    shutil.rmtree(ruta)
    c["borrada"] = str(hoy)
    print(f"✗ Borrada {c['ruta']} — {copiados} textos guardados en archivo/{os.path.relpath(destino, os.path.join(RAIZ, 'archivo'))}")
if not simular:
    json.dump(reg, open(REG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
