"""Vuelca en la Sala el calendario hasta el 1/1/2027 (ver youtube/CALENDARIO_EDITORIAL.md)."""
import datetime as dt, json, os, sys

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(RAIZ, "web", "datos.json")
d = json.load(open(P, encoding="utf-8"))
T = {t["id"]: t for t in d["tareas"]}
ahora = dt.datetime.now(dt.UTC).strftime("%Y-%m-%dT%H:%M:%S.000Z")
FESTIVOS = {dt.date(2026, 10, 12), dt.date(2026, 12, 8), dt.date(2026, 12, 25), dt.date(2027, 1, 1)}
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def laborable(f):
    while f.weekday() >= 5 or f in FESTIVOS:
        f += dt.timedelta(days=1)
    return f
def txt(f): return f"{DIAS[f.weekday()]} {f.day} de {MESES[f.month]}"
def tarea(id, fecha, quien, tipo, proyecto, titulo, notas, plataformas=()):
    base = {"id": id, "title": titulo, "date": fecha.isoformat(), "who": quien, "kind": tipo, "project": proyecto,
            "platforms": list(plataformas), "notes": notas, "updatedAt": ahora}
    if id in T:
        if T[id].get("status") != "hecho":
            T[id].update(base)
        return
    base.update({"status": "pendiente", "comentarios": [], "createdAt": ahora, "createdBy": "claude"})
    d["tareas"].append(base); T[id] = base

def pasos_youtube(n, tema, viernes):
    s1, s2, s3 = viernes + dt.timedelta(1), viernes + dt.timedelta(3), viernes + dt.timedelta(5)
    return f"""Vídeo {n}: «{tema}». Sale el {txt(viernes)} a las 18:00. Unos 35 minutos.
Todo estará en:  Descargas › faceless › youtube › video_{n:03d}_… › output  (te confirmo la carpeta exacta en los comentarios cuando esté listo).

1. VER (10 min): abre FINAL_YOUTUBE_1080P.mp4 y los 3 SHORT_…mp4. Si algo se ve o se oye raro, dime el minuto aquí.

2. SUBIR EL VÍDEO LARGO (studio.youtube.com; comprueba el logo del ticket amarillo arriba a la derecha):
   «CREAR» → «Subir vídeos» → FINAL_YOUTUBE_1080P.mp4
   · Título: el primero de 07_TITULOS.md (el marcado como ELEGIDO).
   · Descripción: todo 08_DESCRIPCION.txt (Ctrl+E, Ctrl+C, Ctrl+V).
   · Miniatura: output › MINIATURA_1280x720.png
   · No es contenido para niños.
   · «Mostrar más» (en este orden): Contenido alterado o sintético «No» · Etiquetas (vienen al final de 07_TITULOS.md) · Idioma Español (España) · Subtítulos: «Subir archivo» → «Con sincronización» → 06_SUBTITULOS.srt · Categoría Educación.
   · Elementos: pantalla final «1 vídeo, 1 suscripción» (vídeo más reciente).
   · Visibilidad: «Programar» → {txt(viernes)}, 18:00.

3. LOS 3 SHORTS («CREAR» → «Subir vídeos», uno a uno; títulos y descripciones en output › SHORTS_TEXTOS.txt):
   No son para niños · Contenido alterado «No» · Idioma Español (España) · Categoría Educación · sin archivo de subtítulos.
   Programar: SHORT_01 → {txt(s1)} 13:00 · SHORT_02 → {txt(s2)} 13:00 · SHORT_03 → {txt(s3)} 13:00.

4. Escribe «programado» aquí."""

def pasos_pepa(desde_n, fechas):
    filas = "\n".join(f"   · Vídeo {desde_n + i:03d} → {txt(f)}, 19:00" for i, f in enumerate(fechas))
    return f"""Programamos de una vez los 6 vídeos de Pepa de las dos semanas siguientes (unos 45 min). Carpetas: Descargas › faceless › redes › pepa_pita › videos › 0XX_… › salida (vídeo .mp4 + TEXTO_PUBLICACION.txt). Los títulos para Facebook te los dejo en los comentarios.

Fechas (todas a las 19:00, en Instagram + Facebook y en TikTok):
{filas}

A) INSTAGRAM + FACEBOOK (https://business.facebook.com/latest/home con TU Facebook personal; arriba a la izquierda «Pepa Pita»):
   «Crear reel» → marca Facebook e Instagram → vídeo → texto (Ctrl+E, Ctrl+C, Ctrl+V) → portada con Pepa de frente → «Siguiente» hasta «Share» → «Scheduling options» → «Schedule» → fecha y 07:00 PM → botón azul «Schedule».
   Si se queda en «Scheduling your post…»: mira https://business.facebook.com/latest/content_calendar antes de repetir.
B) TIKTOK (https://www.tiktok.com/tiktokstudio/upload, cuenta de Pepa):
   Vídeo → mismo texto → portada → «Mostrar más» → «Contenido generado por IA» → «Programar» → fecha, 19:00.
Al terminar, escribe «Pepa programada» (y si alguno de TikTok no se dejó programar, cuál)."""

# ── TICKET MEDIO: vídeos 4 a 14 ───────────────────────
temas = [(4, "¿Cuánto le queda a El Corte Inglés?", dt.date(2026, 10, 16)),
         (5, "Lidl: el súper que más crece en España", dt.date(2026, 10, 23)),
         (6, "La factura de la luz: ¿dónde va cada euro?", dt.date(2026, 10, 30)),
         (7, "Ryanair: cómo gana dinero con vuelos a 10 €", dt.date(2026, 11, 6)),
         (8, "¿Qué pasa con lo que devuelves a Amazon?", dt.date(2026, 11, 13)),
         (9, "Black Friday: ¿de verdad es más barato?", dt.date(2026, 11, 20)),
         (10, "Primark: cómo vende una camiseta a 3 €", dt.date(2026, 11, 27)),
         (11, "Lotería de Navidad: ¿quién gana siempre?", dt.date(2026, 12, 4)),
         (12, "Correos pierde dinero: ¿por qué no cierra?", dt.date(2026, 12, 11)),
         (13, "Por qué el marisco y el cordero se disparan en Navidad", dt.date(2026, 12, 18)),
         (14, "Rebajas de enero: el truco de los precios", dt.date(2026, 12, 25))]
for n, tema, viernes in temas:
    lunes = viernes - dt.timedelta(4)
    tarea(f"c-video-{n}", lunes, "claude", "tarea", "youtube", f"Vídeo {n} de Ticket Medio: «{tema}» + 3 Shorts",
          "Título y miniatura primero; investigación con fuentes oficiales; guion, voz, escenas ilustradas, Shorts, textos y auditoría. Listo el miércoles.")
    tarea(f"u-fondos-v{n}", laborable(lunes), "tu", "material", "youtube", f"Solo si te lo pido: escenarios en Gemini para el vídeo {n} (15 min)",
          "Si el vídeo necesita escenarios nuevos, te dejo aquí los textos para Gemini el día anterior. Si no hay textos, no hay que hacer nada.")
    tarea(f"pub-yt-{n}", viernes - dt.timedelta(1), "tu", "publicacion", "youtube", f"Ver, subir y programar el vídeo {n} y sus 3 Shorts (35 min)",
          pasos_youtube(n, tema, viernes), ["YouTube", "Shorts"])
    tarea(f"pub-yt-{n}-comentario", laborable(viernes + dt.timedelta(3)), "tu", "publicacion", "youtube",
          f"Fijar el comentario con las fuentes del vídeo {n} (2 min)",
          "Abre el vídeo ya publicado (studio.youtube.com → «Contenido» → título → «Ver en YouTube»), pega como comentario el texto de Descargas › faceless › archivo › video_0XX… › COMENTARIO_FIJADO.txt, publícalo y en sus tres puntos → «Fijar».",
          ["YouTube"])
# el vídeo 3 (Zara): mismas instrucciones completas
tarea("pub-yt-3", dt.date(2026, 10, 8), "tu", "publicacion", "youtube", "Ver, subir y programar el vídeo 3 (Zara) y sus 3 Shorts (35 min)",
      pasos_youtube(3, "ZARA: ¿quién se queda el dinero de tu camiseta?", dt.date(2026, 10, 9)), ["YouTube", "Shorts"])
if "u-revisar-3" in T and T["u-revisar-3"].get("status") != "hecho":
    d["tareas"] = [t for t in d["tareas"] if t["id"] != "u-revisar-3"]   # incluida en «Ver, subir y programar»
if "pub-yt-3-comentario" in T:
    T["pub-yt-3-comentario"]["date"] = "2026-10-13"                     # el 12 es festivo

# ── PEPA PITA: tandas 3 a 7 ────────────────────────────
def publica(desde, n=6):
    f, out = desde, []
    while len(out) < n:
        if f.weekday() in (1, 3, 5): out.append(f)
        f += dt.timedelta(1)
    return out
tandas = [(3, 13, dt.date(2026, 10, 27), "Castañas · Calabaza · Setas · Menú barato de otoño · Legumbres · Pan duro"),
          (4, 19, dt.date(2026, 11, 10), "Caducidad y consumo preferente · Congelar en raciones · Menú de noviembre · El táper · Código de los huevos · Fruta de temporada"),
          (5, 25, dt.date(2026, 11, 24), "Cocina y Black Friday · Gambas y langostinos · Marisco congelado · Descongelar el pavo · Menú de Navidad barato (1) · Turrón"),
          (6, 31, dt.date(2026, 12, 8), "Cordero y cochinillo · Sobras de Navidad · Menú de Navidad barato (2) · Aperitivos · Bebidas frías · Canapés"),
          (7, 37, dt.date(2026, 12, 22), "Roscón · Uvas de Nochevieja · Sobras de las fiestas · Menú de Año Nuevo · Brindis seguro · Comer mejor gastando menos")]
for k, n0, desde, temas_p in tandas:
    fechas = publica(desde)
    jueves_prog = desde - dt.timedelta(5)          # jueves de la semana anterior
    tarea(f"c-pepa-tanda-{k}", jueves_prog - dt.timedelta(3), "claude", "tarea", "redes",
          f"Producir Pepa {n0:03d}–{n0 + 5:03d} ({temas_p.split(' · ')[0]}…)", f"Temas: {temas_p}. Datos verificados en fuentes oficiales.")
    tarea(f"pub-pepa-lote-{k}", jueves_prog, "tu", "publicacion", "redes",
          f"Programar de una vez Pepa {n0:03d}–{n0 + 5:03d} en Instagram, Facebook y TikTok (45 min)", pasos_pepa(n0, fechas),
          ["Instagram", "Facebook", "TikTok"])
if "pub-pepa-lote-2" in T:
    T["pub-pepa-lote-2"]["notes"] = pasos_pepa(7, publica(dt.date(2026, 10, 13)))

# ── RESULTADOS mensuales ───────────────────────────────
for id, f in (("u-resultados-nov", dt.date(2026, 11, 2)), ("u-resultados-dic", dt.date(2026, 12, 1))):
    tarea(id, f, "tu", "tarea", "general", "RESULTADOS del mes: capturas de YouTube Studio e Instagram (15 min)",
          """1. studio.youtube.com → «Estadísticas» → pestañas «Resumen», «Contenido» y «Audiencia»: una captura de cada una.
2. Instagram (app, cuenta soypepapita) → «Panel profesional» → «Estadísticas»: una captura.
3. Pégalas en el chat. Yo las analizo y ajustamos temas, títulos y miniaturas.""")

# hoja de ruta: fase 2
for f in d["hojaDeRuta"]["fases"]:
    if f["nombre"].startswith("Fase 2"):
        f["hitos"] = ["Vídeos de temporada: Black Friday (20/11), Lotería de Navidad (4/12), Navidad (18/12) y rebajas (25/12)",
                      "Pepa Pita: menús y trucos de otoño y de Navidad, 3 a la semana",
                      "RESULTADOS el 2/11 y el 1/12: decidir qué repetir",
                      "Calendario completo en youtube/CALENDARIO_EDITORIAL.md"]
json.dump(d, open(P + ".tmp", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
os.replace(P + ".tmp", P)
print("tareas:", len(d["tareas"]))
