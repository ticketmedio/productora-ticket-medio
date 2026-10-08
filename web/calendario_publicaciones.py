"""Regenera en la Sala las tareas de PUBLICACIÓN del usuario hasta el 15/12/2026 (decisión del 8/10/2026).

Uso: python3 web/calendario_publicaciones.py   (idempotente: se puede ejecutar cuantas veces haga falta)

- Pepa Pita: 1 Reel de lunes a viernes a las 19:00 desde el 26/10 (013, 014…). Los jueves (largos de 61–75 s) van a
  Facebook + TikTok; el resto, a Instagram + Facebook. Una tarea por semana, el MIÉRCOLES anterior (se puede hacer antes).
- Ticket Medio: vídeo largo los viernes a las 18:00 y un Short al día a las 13:00 (3 del vídeo + 4 de ángulos nuevos).
  Una tarea por vídeo, el jueves anterior.
- Nunca en fin de semana, festivo ni puente (ver CLAUDE.md).
Los títulos salen de redes/pepa_pita/lote/*.json y youtube/video_0NN_*/ cuando ya existen.
"""
import datetime, glob, json, os, sys

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(RAIZ, "web", "datos.json")
D = datetime.date
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
FESTIVOS = {D(2026, 10, 9), D(2026, 10, 12), D(2026, 12, 7), D(2026, 12, 8), D(2026, 12, 25), D(2027, 1, 1), D(2027, 1, 6)}
LISTA = """LISTA DE COMPROBACIÓN (redes/LISTA_COMPROBACION.md), en CADA publicación antes de pasar a la siguiente:
  ☐ Texto pegado entero (no vacío ni cortado)
  ☐ Hashtags: 5 como máximo
  ☐ Fecha y hora correctas (ojo al MES; que la hora no se quede en la actual)
  ☐ Cuenta y archivo correctos (Pepa Pita o Ticket Medio; en TikTok, el archivo con TIKTOK en el nombre, si lo hay)"""


def f(d): return f"{DIAS[d.weekday()]} {d.day} de {MESES[d.month]}"
def f2(d): return f"{DIAS[d.weekday()][:3]} {d.day}/{d.month}"


def laborable(d):
    while d.weekday() >= 5 or d in FESTIVOS:
        d -= datetime.timedelta(days=1)
    return d


def siguiente_laborable(d):
    while d.weekday() >= 5 or d in FESTIVOS:
        d += datetime.timedelta(days=1)
    return d


def titulo_pepa(n):
    for ruta in glob.glob(os.path.join(RAIZ, "redes", "pepa_pita", "lote", f"{n:03d}_*.json")):
        return json.load(open(ruta, encoding="utf-8")).get("titulo", "")
    ruta = glob.glob(os.path.join(RAIZ, "redes", "pepa_pita", "videos", f"{n:03d}_*"))
    return os.path.basename(ruta[0])[4:].replace("_", " ").capitalize() if ruta else "(en producción)"


def carpeta_pepa(n):
    ruta = glob.glob(os.path.join(RAIZ, "redes", "pepa_pita", "videos", f"{n:03d}_*"))
    return os.path.basename(ruta[0]) if ruta else f"{n:03d}_…"


# ───────────────────────── Pepa ─────────────────────────
def reels_pepa():
    """Lista de (número, fecha, plataformas) desde el 26/10 hasta el 15/12."""
    out, n, d = [], 13, D(2026, 10, 26)
    while d <= D(2026, 12, 15):
        if d.weekday() < 5:
            out.append((n, d, "Facebook + TikTok" if d.weekday() == 3 else "Instagram + Facebook"))
            n += 1
        d += datetime.timedelta(days=1)
    return out


def tareas_pepa(ahora):
    reels = reels_pepa()
    semanas = {}
    for n, d, p in reels:
        semanas.setdefault(d - datetime.timedelta(days=d.weekday()), []).append((n, d, p))
    tareas = []
    for i, (lunes, lista) in enumerate(sorted(semanas.items()), 1):
        tarea_dia = laborable(lunes - datetime.timedelta(days=5))  # miércoles anterior
        filas = "\n".join(f"   · {carpeta_pepa(n)} → {f(d)}, 19:00 — {p}  [{titulo_pepa(n)}]" for n, d, p in lista)
        primero, ultimo = lista[0][0], lista[-1][0]
        tareas.append({
            "id": f"pub-pepa-sem-{i}", "kind": "publicacion", "who": "tu", "project": "redes",
            "platforms": ["Instagram", "Facebook", "TikTok"], "date": tarea_dia.isoformat(), "status": "pendiente",
            "title": f"Programar los Reels de Pepa {primero:03d}–{ultimo:03d} (semana del {lunes.day}/{lunes.month}) en Instagram, Facebook y TikTok (45 min)",
            "createdBy": "claude", "createdAt": ahora, "updatedAt": ahora,
            "notes": f"""Un Reel de Pepa cada día laborable a las 19:00. Puedes hacerlo ANTES de esta fecha: los vídeos ya estarán listos y no hay que esperar a nadie.
Carpetas: Descargas › faceless › redes › pepa_pita › videos › 0XX_… › salida (vídeo .mp4 + TEXTO_PUBLICACION.txt).

Fechas (hora de España):
{filas}

A) INSTAGRAM + FACEBOOK (lunes, martes, miércoles y viernes; https://business.facebook.com/latest/home con TU Facebook personal; arriba a la izquierda «Pepa Pita»): «Crear reel» → marca Instagram y Facebook → vídeo → texto (Ctrl+E, Ctrl+C, Ctrl+V) → portada con Pepa de frente → «Siguiente» hasta «Share» → «Scheduling options» → «Schedule» → fecha y 07:00 PM → «Schedule». Si se queda en «Scheduling your post…», mira https://business.facebook.com/latest/content_calendar antes de repetir.
B) FACEBOOK + TIKTOK (jueves, el vídeo largo de 61–75 s): en Meta, marca solo Facebook (no Instagram). En TikTok (https://www.tiktok.com/tiktokstudio/upload, cuenta de Pepa): vídeo → mismo texto → portada → «Mostrar más» → «Contenido generado por IA» → «Programar» → fecha, 19:00.
Al terminar, escribe «Pepa programada» (y si alguno no se dejó programar, cuál).

{LISTA}""",
        })
    return tareas


# ───────────────────── Ticket Medio ─────────────────────
VIDEOS = [  # nº, viernes de publicación, título corto
    (5, D(2026, 10, 23), "Lidl: el súper que más crece en España"),
    (6, D(2026, 10, 30), "La factura de la luz: ¿dónde va cada euro?"),
    (7, D(2026, 11, 6), "Ryanair: cómo gana dinero con vuelos a 10 €"),
    (8, D(2026, 11, 13), "¿Qué pasa con lo que devuelves a Amazon?"),
    (9, D(2026, 11, 20), "Black Friday: ¿de verdad es más barato?"),
    (10, D(2026, 11, 27), "Primark: cómo vende una camiseta a 3 €"),
    (11, D(2026, 12, 4), "Lotería de Navidad: ¿quién gana siempre?"),
    (12, D(2026, 12, 11), "Correos pierde dinero: ¿por qué no cierra?"),
]


def carpeta_video(n):
    ruta = glob.glob(os.path.join(RAIZ, "youtube", f"video_{n:03d}_*"))
    return os.path.basename(ruta[0]) if ruta else f"video_{n:03d}_…"


def tareas_youtube(ahora):
    tareas = []
    for n, viernes, titulo in VIDEOS:
        sh = [viernes + datetime.timedelta(days=k) for k in range(1, 8)]
        principales, extras = [sh[0], sh[2], sh[4]], [sh[1], sh[3], sh[5], sh[6]]
        tarea_dia = laborable(viernes - datetime.timedelta(days=1))
        carp = carpeta_video(n)
        lin_p = " · ".join(f"SHORT_0{i + 1} → {f(d)}" for i, d in enumerate(principales))
        lin_e = " · ".join(f"SHORT_0{i + 4} → {f(d)}" for i, d in enumerate(extras))
        tareas.append({
            "id": f"pub-yt-{n}", "kind": "publicacion", "who": "tu", "project": "youtube",
            "platforms": ["YouTube", "Shorts"], "date": tarea_dia.isoformat(), "status": "pendiente",
            "title": f"Ver, subir y programar el vídeo {n} y sus 7 Shorts (50 min)",
            "createdBy": "claude", "createdAt": ahora, "updatedAt": ahora,
            "notes": f"""Vídeo {n}: «{titulo}». Sale el {f(viernes)} a las 18:00, con un Short cada día a las 13:00 durante la semana siguiente. Unos 50 minutos. Puedes hacerlo ANTES de esta fecha: si el vídeo ya está listo (te lo aviso en un comentario), no hay que esperar al día.
Todo estará en:  Descargas › faceless › youtube › {carp} › output

1. VER (10 min): abre FINAL_YOUTUBE_1080P.mp4 y los SHORT_…mp4. Si algo se ve o se oye raro, dime el minuto aquí.

2. SUBIR EL VÍDEO LARGO (studio.youtube.com; comprueba el logo del ticket amarillo arriba a la derecha): «CREAR» → «Subir vídeos» → FINAL_YOUTUBE_1080P.mp4
   · Título: el marcado como ELEGIDO en 07_TITULOS.md · Descripción: todo 08_DESCRIPCION.txt · Miniatura: MINIATURA_1280x720.png · No es contenido para niños.
   · «Mostrar más» (en este orden): Contenido alterado o sintético «No» · Etiquetas (al final de 07_TITULOS.md) · Idioma Español (España) · Subtítulos: «Subir archivo» → «Con sincronización» → 06_SUBTITULOS.srt · Categoría Educación.
   · Elementos: pantalla final «1 vídeo, 1 suscripción» (vídeo más reciente). Visibilidad: «Programar» → {f(viernes)}, 18:00.

3. LOS 7 SHORTS («CREAR» → «Subir vídeos», uno a uno; títulos y descripciones en SHORTS_TEXTOS.txt): no son para niños · Contenido alterado «No» · Idioma Español (España) · Categoría Educación · sin archivo de subtítulos. Todos a las 13:00:
   Los 3 del vídeo: {lin_p}
   Los 4 de ángulos nuevos: {lin_e}

4. ENLAZAR LOS SHORTS AL VÍDEO LARGO (cuando ya esté publicado, viernes a partir de las 18:00): studio.youtube.com → Contenido → Shorts → lápiz de «Editar» de cada Short → «Vídeo relacionado» → elige el vídeo {n} → Guardar.

5. Escribe «programado» aquí.

{LISTA}""",
        })
        tareas.append({
            "id": f"pub-yt-{n}-comentario", "kind": "publicacion", "who": "tu", "project": "youtube",
            "platforms": ["YouTube"], "date": siguiente_laborable(viernes + datetime.timedelta(days=3)).isoformat(), "status": "pendiente",
            "title": f"Fijar el comentario con las fuentes del vídeo {n} (2 min)",
            "createdBy": "claude", "createdAt": ahora, "updatedAt": ahora,
            "notes": f"""Abre el vídeo ya publicado (studio.youtube.com → «Contenido» → título → «Ver en YouTube»), pega como comentario el texto de Descargas › faceless › youtube › {carp} › output › COMENTARIO_FIJADO.txt, publícalo y en sus tres puntos → «Fijar».

{LISTA}""",
        })
    return tareas


def main():
    d = json.load(open(DATA, encoding="utf-8"))
    ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    nuevas = tareas_pepa(ahora) + tareas_youtube(ahora)
    ids_nuevos = {t["id"] for t in nuevas}
    viejos = {"pub-pepa-lote-3", "pub-pepa-lote-4", "pub-pepa-lote-5", "pub-pepa-lote-6"}
    previas = {t["id"]: t for t in d["tareas"]}
    resultado = []
    for t in d["tareas"]:
        if t["id"] in viejos:
            continue
        if t["id"] in ids_nuevos:
            n = next(x for x in nuevas if x["id"] == t["id"])
            if t["status"] == "hecho":      # no se pisa lo que el usuario ya hizo
                resultado.append(t); continue
            n["status"], n["createdAt"] = t["status"], t.get("createdAt", ahora)
            n["comentarios"] = t.get("comentarios", [])
            resultado.append(n)
        else:
            resultado.append(t)
    existentes = {t["id"] for t in resultado}
    resultado += [t for t in nuevas if t["id"] not in existentes]
    d["tareas"] = resultado
    json.dump(d, open(DATA, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Pepa: {len(reels_pepa())} Reels, {len([t for t in nuevas if t['id'].startswith('pub-pepa')])} tareas semanales; "
          f"YouTube: {len(VIDEOS)} vídeos con sus Shorts. Total tareas: {len(resultado)}")


main()
