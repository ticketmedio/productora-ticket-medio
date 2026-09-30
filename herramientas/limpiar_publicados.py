"""Borra las carpetas de producción cuando ya se ha publicado todo lo que contienen.

Uso: python herramientas/limpiar_publicados.py [--simular]
Lee archivo/publicaciones.json:
  {"carpetas": [{"ruta": "redes/pepa_pita/videos/001_no_laves_el_pollo", "ultima_publicacion": "2026-09-29"}, ...]}
Una carpeta se borra al día SIGUIENTE de su última publicación (margen por si una programación falla).
Antes de borrar, copia a archivo/<nombre>/ la «copia de autoría» (decisión del usuario del 30/09, por si YouTube
pide justificar la aportación propia en la revisión del Programa de Socios): guion y textos (.txt, .md, .srt),
voz (voz.mp3), plan.json / escenas_v2.json / montaje.json / shorts.json, scripts propios del vídeo (.py) y la
miniatura (MINIATURA*.png, miniatura.html). Los .mp3 no se suben a GitHub (.gitignore): solo quedan en este ordenador.
"""
import datetime, json, os, shutil, sys

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(RAIZ, "archivo", "publicaciones.json")
TEXTOS = (".txt", ".md", ".srt")
JSON_UTILES = ("plan.json", "escenas_v2.json", "shorts.json", "montaje.json")
OTROS = ("voz.mp3", "miniatura.html")


def se_guarda(a):
    return (a.endswith(TEXTOS + (".py",)) or a in JSON_UTILES or a in OTROS
            or (a.upper().startswith("MINIATURA") and a.lower().endswith(".png")))
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
            if se_guarda(a):
                if "fuentes" in os.path.relpath(base, ruta).split(os.sep) and a.endswith("_raw.txt"):
                    continue                                        # textos en bruto de PDF: pesan y no hacen falta
                rel = os.path.relpath(os.path.join(base, a), ruta)
                dst = os.path.join(destino, rel)
                if not simular:
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.copy2(os.path.join(base, a), dst)
                copiados += 1
    if simular:
        print(f"✗ (simulación) Se borraría {c['ruta']} — {copiados} archivos al archivo")
        continue
    shutil.rmtree(ruta)
    c["borrada"] = str(hoy)
    print(f"✗ Borrada {c['ruta']} — {copiados} archivos (textos, voz, planes y miniatura) guardados en archivo/{os.path.relpath(destino, os.path.join(RAIZ, 'archivo'))}")
if not simular:
    json.dump(reg, open(REG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
