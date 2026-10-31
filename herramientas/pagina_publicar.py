"""Página «Qué publicar cada día» (Meta y YouTube) con los textos listos para copiar y pegar.

Uso: python3 herramientas/pagina_publicar.py   → escribe privado/publicar.html (se publica como Artifact de claude.ai)
Lee las fechas de redes/pepa_pita/PLAN_PROGRAMACION.md (Reels y carruseles) y de youtube/video_0NN_*/textos.json (Shorts),
y los textos de cada TEXTO_PUBLICACION.txt, 08_DESCRIPCION.txt y COMENTARIO_FIJADO.txt. Volver a ejecutarlo tras cambiar un texto.
"""
import datetime, glob, html, json, os, re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = datetime.date
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
DESDE = D(2026, 11, 2)
# Ya programados en Meta con la versión ANTIGUA (hay que borrarlos y poner el nuevo) y carruseles ya programados
REEMPLAZAR = {f"{n:03d}" for n in range(18, 28)}
CARRUSELES_HECHOS = {"009", "010"}
# Meta ya programado y comprobado por Claude en Meta Business Suite (31/10: todo hasta el viernes 27/11)
META_HECHO_HASTA = D(2026, 11, 27)
# vídeo largo de Ticket Medio: viernes 18:00
FECHA_LARGO = {7: D(2026, 11, 6), 8: D(2026, 11, 13), 9: D(2026, 11, 20), 10: D(2026, 11, 27), 11: D(2026, 12, 4), 12: D(2026, 12, 11)}


def leer(*p):
    return open(os.path.join(RAIZ, *p), encoding="utf-8").read().strip()


def ruta_bonita(rel):
    return "~/Downloads/faceless/" + rel.strip("/")


def fecha_es(txt):
    m = re.search(r"(\d+) de (\w+)", txt)
    return D(2026 if MESES.index(m.group(2)) >= 10 else 2027, MESES.index(m.group(2)), int(m.group(1)))


items = []
# ── Pepa Pita: Reels y carruseles (Meta Business Suite) ──
for fila in leer("redes", "pepa_pita", "PLAN_PROGRAMACION.md").splitlines():
    c = [x.strip() for x in fila.split("|")]
    if len(c) < 7 or not re.search(r"\d+ de ", c[2]):
        continue
    dia, hora, que, donde, archivo = fecha_es(c[2]), c[3], c[4], c[5], c[6]
    if dia < DESDE or dia <= META_HECHO_HASTA:
        continue
    carpeta = archivo.split(" ")[0].rstrip("/")
    n = re.search(r"(\d{3})", que).group(1)
    if que.startswith("Carrusel"):
        if n in CARRUSELES_HECHOS:
            continue
        imgs = sorted(os.path.basename(f) for f in glob.glob(os.path.join(RAIZ, carpeta, "*.png")))
        items.append({"dia": dia.isoformat(), "hora": hora, "red": "meta", "tipo": "Carrusel",
                      "titulo": f"Carrusel {n}", "destino": "Instagram + Facebook · «Crear publicación»",
                      "ruta": ruta_bonita(carpeta), "archivo": f"{len(imgs)} imágenes ({imgs[0]} a {imgs[-1]})" if imgs else "",
                      "aviso": "", "campos": [["Texto", leer(carpeta, "TEXTO_PUBLICACION.txt")]]})
        continue
    nombre = re.search(r"«(.+?)»", que).group(1)
    solo_fb = "TikTok" in donde
    mp4 = next(iter(sorted(glob.glob(os.path.join(RAIZ, carpeta, "PEPA_*.mp4")))), "")
    items.append({"dia": dia.isoformat(), "hora": hora, "red": "meta", "tipo": "Reel",
                  "titulo": f"Reel {n} · {nombre}",
                  "destino": "Solo Facebook (el jueves, Instagram no; TikTok ya lo tienes)" if solo_fb else "Instagram + Facebook · «Crear reel»",
                  "ruta": ruta_bonita(carpeta), "archivo": os.path.basename(mp4),
                  "aviso": "Ya hay uno ANTIGUO programado este día: bórralo en Publicaciones programadas y programa este." if n in REEMPLAZAR else "",
                  "campos": [["Texto", leer(carpeta, "TEXTO_PUBLICACION.txt")]]})

# ── Ticket Medio: vídeo largo + 7 Shorts (YouTube Studio) ──
for v in sorted(glob.glob(os.path.join(RAIZ, "youtube", "video_0*"))):
    num = int(re.search(r"video_(\d+)", v).group(1))
    if num not in FECHA_LARGO:
        continue
    cfg = json.load(open(os.path.join(v, "textos.json"), encoding="utf-8"))
    rel = os.path.relpath(os.path.join(v, "output"), RAIZ)
    items.append({"dia": FECHA_LARGO[num].isoformat(), "hora": "18:00", "red": "youtube", "tipo": "Vídeo largo",
                  "titulo": f"Vídeo {num} · {cfg['titulo']}", "destino": "YouTube · «Programar»",
                  "ruta": ruta_bonita(rel), "archivo": "FINAL_YOUTUBE_1080P.mp4 · miniatura MINIATURA_1280x720.png · subtítulos ../06_SUBTITULOS.srt",
                  "aviso": "No es para niños · Contenido alterado «No» · Idioma Español (España) · Categoría Educación · pantalla final «1 vídeo, 1 suscripción».",
                  "campos": [["Título", cfg["titulo"]], ["Descripción", leer(v, "08_DESCRIPCION.txt")],
                             ["Etiquetas", cfg["etiquetas"]], ["Comentario fijado (cuando salga)", leer(v, "COMENTARIO_FIJADO.txt")]]})
    for s in cfg["shorts"]:
        dd, mm = map(int, re.search(r"(\d+)/(\d+)", s["dia"]).groups())
        items.append({"dia": D(2026, mm, dd).isoformat(), "hora": "13:00", "red": "youtube", "tipo": "Short",
                      "titulo": f"Short {int(s['id'])} del vídeo {num}", "destino": "YouTube · «Programar»",
                      "ruta": ruta_bonita(rel), "archivo": s["archivo"],
                      "aviso": f"Cuando el vídeo {num} ya esté publicado: «Vídeo relacionado» → vídeo {num}.",
                      "campos": [["Título", f"{s['titulo']} #shorts"],
                                 ["Descripción", f"{s['descripcion']} El vídeo completo, en el canal.\n{s['hashtags']}"]]})

items.sort(key=lambda x: (x["dia"], x["hora"], x["red"]))
for k, it in enumerate(items):
    it["id"] = f"{it['dia']}_{it['hora']}_{it['red']}_{re.sub(r'[^a-z0-9]', '', it['titulo'].lower())[:24]}"
plantilla = leer("herramientas", "pagina_publicar.html")
datos = json.dumps(items, ensure_ascii=False).replace("</", "<\\/")
salida = os.path.join(RAIZ, "privado", "publicar.html")
open(salida, "w", encoding="utf-8").write(plantilla.replace("/*DATOS*/[]", datos).replace(
    "{{GENERADO}}", datetime.datetime.now().strftime("%d/%m/%Y %H:%M")))
print(salida, len(items), "publicaciones")
