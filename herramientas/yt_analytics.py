"""Estadísticas PRIVADAS de nuestro canal de YouTube con la API oficial (YouTube Analytics API).
Sirve para la NUBE: no usa navegador ni sesión iniciada, solo un permiso de solo lectura que autorizó el usuario.

Credenciales (nunca en el repositorio ni en el chat): variables de entorno YT_CLIENT_ID, YT_CLIENT_SECRET y
YT_REFRESH_TOKEN (en la nube) o esas mismas claves en config/claves.txt y config/youtube_token.txt (en el PC).

Uso:
  python herramientas/yt_analytics.py resumen [dias]       -> canal: visualizaciones, horas, suscriptores; total y por tipo (largo / Shorts)
  python herramientas/yt_analytics.py diario [dias]        -> lo mismo, día a día
  python herramientas/yt_analytics.py videos [dias]        -> los 25 vídeos con más visualizaciones del periodo (título, horas, duración media, % visto, suscriptores)
  python herramientas/yt_analytics.py retencion VIDEO_ID   -> curva de retención: dónde se va la gente
Salida: JSON por consola. Por defecto, los últimos 28 días (los datos de YouTube llevan 1-2 días de retraso).
OJO: las horas de los Shorts probablemente NO cuentan para el Programa de Socios; por eso `resumen` las separa.
"""
import datetime, json, os, sys, urllib.error, urllib.parse, urllib.request

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAVES = ("YT_CLIENT_ID", "YT_CLIENT_SECRET", "YT_REFRESH_TOKEN")


def leer_credenciales():
    datos = {k: os.environ.get(k, "") for k in CLAVES}
    for nombre in ("claves.txt", "youtube_token.txt"):
        ruta = os.path.join(RAIZ, "config", nombre)
        if os.path.exists(ruta):
            for linea in open(ruta, encoding="utf-8"):
                if ":" in linea:
                    k, v = linea.split(":", 1)
                    if k.strip() in CLAVES and not datos[k.strip()]:
                        datos[k.strip()] = v.strip()
    faltan = [k for k in CLAVES if not datos[k]]
    if faltan:
        sys.exit("Faltan credenciales de la API de YouTube: " + ", ".join(faltan) +
                 ". El usuario tiene que completar la tarea «Conectar la API de YouTube» de la Sala (AUTORIZAR_YOUTUBE.bat).")
    return datos


def token_de_acceso():
    d = leer_credenciales()
    cuerpo = urllib.parse.urlencode({"client_id": d["YT_CLIENT_ID"], "client_secret": d["YT_CLIENT_SECRET"],
                                     "refresh_token": d["YT_REFRESH_TOKEN"], "grant_type": "refresh_token"}).encode()
    try:
        r = urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=cuerpo), timeout=30)
        return json.loads(r.read())["access_token"]
    except urllib.error.HTTPError as e:
        sys.exit(f"Google rechazó las credenciales ({e.code}): {e.read()[:300]!r}. Si pone invalid_grant, hay que repetir AUTORIZAR_YOUTUBE.bat.")


TOKEN = None


def get(url, params):
    global TOKEN
    TOKEN = TOKEN or token_de_acceso()
    req = urllib.request.Request(url + "?" + urllib.parse.urlencode(params), headers={"Authorization": "Bearer " + TOKEN})
    try:
        return json.loads(urllib.request.urlopen(req, timeout=60).read())
    except urllib.error.HTTPError as e:
        return {"error": e.code, "detalle": e.read()[:400].decode("utf-8", "replace")}


def reporte(metricas, dias, **extra):
    fin = datetime.date.today() - datetime.timedelta(days=1)
    ini = fin - datetime.timedelta(days=dias - 1)
    p = {"ids": "channel==MINE", "startDate": ini.isoformat(), "endDate": fin.isoformat(), "metrics": metricas}
    p.update(extra)
    return get("https://youtubeanalytics.googleapis.com/v2/reports", p)


def tabla(r):
    if "error" in r:
        return r
    cols = [c["name"] for c in r.get("columnHeaders", [])]
    return [dict(zip(cols, fila)) for fila in r.get("rows", [])]


def horas(filas):
    for f in filas if isinstance(filas, list) else []:
        if "estimatedMinutesWatched" in f:
            f["horas"] = round(f.pop("estimatedMinutesWatched") / 60, 2)
    return filas


METR = "views,estimatedMinutesWatched,averageViewDuration,subscribersGained,subscribersLost,likes,comments,shares"

if __name__ == "__main__":
    orden = sys.argv[1] if len(sys.argv) > 1 else ""
    dias = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 28
    if orden == "resumen":
        total = horas(tabla(reporte(METR, dias)))
        tipos = horas(tabla(reporte(METR, dias, dimensions="creatorContentType")))
        print(json.dumps({"dias": dias, "total": total, "por_tipo": tipos}, ensure_ascii=False, indent=1))
    elif orden == "diario":
        print(json.dumps(horas(tabla(reporte(METR, dias, dimensions="day", sort="day"))), ensure_ascii=False, indent=1))
    elif orden == "videos":
        filas = horas(tabla(reporte(METR + ",averageViewPercentage", dias, dimensions="video", sort="-views", maxResults=25)))
        if isinstance(filas, list) and filas:
            info = get("https://www.googleapis.com/youtube/v3/videos",
                       {"part": "snippet,contentDetails", "id": ",".join(f["video"] for f in filas)})
            nombres = {i["id"]: {"titulo": i["snippet"]["title"], "publicado": i["snippet"]["publishedAt"][:10],
                                 "duracion": i["contentDetails"]["duration"]} for i in info.get("items", [])} if "items" in info else {}
            for f in filas:
                f.update(nombres.get(f["video"], {}))
        print(json.dumps(filas, ensure_ascii=False, indent=1))
    elif orden == "retencion" and len(sys.argv) > 2:
        r = reporte("audienceWatchRatio,relativeRetentionPerformance", 365, dimensions="elapsedVideoTimeRatio",
                    filters="video==" + sys.argv[2])
        print(json.dumps(tabla(r), ensure_ascii=False, indent=1))
    else:
        print(__doc__)
