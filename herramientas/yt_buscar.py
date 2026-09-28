"""Lee búsquedas y canales públicos de YouTube (España) para estudiar nichos.

Uso:
  python herramientas/yt_buscar.py buscar "consulta" [más consultas...]
  python herramientas/yt_buscar.py canal @identificador
Salida en JSON por consola.
"""
import json, re, sys, urllib.parse, urllib.request

CABECERAS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9",
    "Cookie": "CONSENT=YES+cb; SOCS=CAI",
}


def _datos(url):
    req = urllib.request.Request(url, headers=CABECERAS)
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html)
    return json.loads(m.group(1)) if m else {}


def _texto(o):
    if not o:
        return ""
    if "simpleText" in o:
        return o["simpleText"]
    return "".join(r.get("text", "") for r in o.get("runs", []))


def _recorrer(o, clave, salida):
    if isinstance(o, dict):
        if clave in o:
            salida.append(o[clave])
        for v in o.values():
            _recorrer(v, clave, salida)
    elif isinstance(o, list):
        for v in o:
            _recorrer(v, clave, salida)
    return salida


def buscar(consulta):
    url = "https://www.youtube.com/results?gl=ES&hl=es&search_query=" + urllib.parse.quote(consulta)
    videos = []
    for v in _recorrer(_datos(url), "videoRenderer", []):
        dueño = (v.get("ownerText", {}).get("runs") or [{}])[0]
        nav = dueño.get("navigationEndpoint", {}).get("browseEndpoint", {})
        videos.append({
            "titulo": _texto(v.get("title")),
            "visitas": _texto(v.get("viewCountText")),
            "canal": dueño.get("text", ""),
            "canal_url": nav.get("canonicalBaseUrl", ""),
            "hace": _texto(v.get("publishedTimeText")),
            "duracion": _texto(v.get("lengthText")),
            "id": v.get("videoId"),
        })
    return videos


def canal(ident):
    base = "https://www.youtube.com/" + ident.lstrip("/")
    d = _datos(base + "/videos?gl=ES&hl=es")
    cab = json.dumps(d.get("header", {}), ensure_ascii=False, separators=(",", ":"))
    subs = re.search(r'"content":"([^"]*suscriptor[^"]*)"', cab)
    nvid = re.search(r'"content":"([^"]*vídeo[^"]*)"', cab)
    videos = []
    for v in _recorrer(d, "videoRenderer", []):
        videos.append({"titulo": _texto(v.get("title")), "visitas": _texto(v.get("viewCountText")),
                       "hace": _texto(v.get("publishedTimeText")), "duracion": _texto(v.get("lengthText"))})
    for v in _recorrer(d, "lockupViewModel", []):
        meta = json.dumps(v, ensure_ascii=False, separators=(",", ":"))
        t = re.search(r'"title":\{"content":"([^"]+)"', meta)
        vis = re.search(r'"(?:content|accessibilityLabel)":"([^"]*visualizaci[^"]*)"', meta)
        hace = re.search(r'"content":"(hace [^"]+)"', meta)
        if t:
            videos.append({"titulo": t.group(1), "visitas": vis.group(1) if vis else "",
                           "hace": hace.group(1) if hace else ""})
    return {"canal": ident, "suscriptores": subs.group(1) if subs else "", "num_videos": nvid.group(1) if nvid else "",
            "videos": videos}


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    orden, *args = sys.argv[1:]
    if orden == "buscar":
        print(json.dumps({c: buscar(c) for c in args}, ensure_ascii=False, indent=1))
    else:
        print(json.dumps([canal(a) for a in args], ensure_ascii=False, indent=1))
