"""Analiza un vídeo público de YouTube: datos, subtítulos y fotogramas del storyboard.

  python herramientas/yt_video.py ID_DEL_VIDEO carpeta_salida
Guarda: datos.json (con «momentos_mas_vistos»: la gráfica pública de lo más visto, picos y valles),
transcripcion.txt (si hay subtítulos), storyboard_XX.jpg y miniatura.jpg
"""
import json, os, re, sys, urllib.request

sys.path.insert(0, os.path.dirname(__file__))
from yt_buscar import CABECERAS


def bajar(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=CABECERAS), timeout=30).read()


def json_en(html, variable):
    i = html.find(variable + " = ")
    if i < 0:
        return {}
    return json.JSONDecoder().raw_decode(html[i + len(variable) + 3:])[0]


def main(vid, salida):
    os.makedirs(salida, exist_ok=True)
    html = bajar(f"https://www.youtube.com/watch?v={vid}&gl=ES&hl=es").decode("utf-8")
    jug = json_en(html, "ytInitialPlayerResponse")
    ini = json_en(html, "ytInitialData")
    det = jug.get("videoDetails", {})
    micro = jug.get("microformat", {}).get("playerMicroformatRenderer", {})
    texto_ini = json.dumps(ini, ensure_ascii=False, separators=(",", ":"))
    megusta = re.search(r'"accessibilityText":"([^"]*Me gusta[^"]*)"', texto_ini)
    coment = re.search(r'"contextualInfo":\{"runs":\[\{"text":"([^"]+)"', texto_ini)
    capitulos = re.findall(r'"chapterRenderer":\{"title":\{"simpleText":"([^"]+)"\}.*?"timeRangeStartMillis":(\d+)', texto_ini)
    datos = {
        "titulo": det.get("title"), "canal": det.get("author"), "duracion_s": det.get("lengthSeconds"),
        "visitas": det.get("viewCount"), "publicado": micro.get("publishDate"), "categoria": micro.get("category"),
        "etiquetas": det.get("keywords"), "descripcion": det.get("shortDescription"),
        "me_gusta": megusta.group(1) if megusta else None, "comentarios": coment.group(1) if coment else None,
        "capitulos": [(t, int(ms) // 1000) for t, ms in capitulos],
    }
    json.dump(datos, open(os.path.join(salida, "datos.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    # «momentos más vistos» (gráfica pública sobre la barra de reproducción): lo más parecido
    # a la retención de un vídeo ajeno. Solo existe si el vídeo tiene bastantes visitas.
    marcas = re.search(r'"markerType":"MARKER_TYPE_HEATMAP","markers":(\[.*?\])', texto_ini)
    if marcas:
        puntos = [(int(m["startMillis"]) // 1000, round(float(m["intensityScoreNormalized"]), 3)) for m in json.loads(marcas.group(1))]
        tramo = lambda s: f"{s // 60}:{s % 60:02d}"
        despues = [p for p in puntos if p[0] >= 30]  # los primeros segundos siempre salen altos
        datos["momentos_mas_vistos"] = {
            "puntos_seg_intensidad": puntos,
            "picos": [tramo(s) for s, _ in sorted(despues, key=lambda p: -p[1])[:5]],
            "valles": [tramo(s) for s, _ in sorted(despues, key=lambda p: p[1])[:5]],
            "intensidad_media_tras_30s": round(sum(v for _, v in despues) / max(len(despues), 1), 3),
        }
    else:
        datos["momentos_mas_vistos"] = "no disponible (pocas visitas)"

    # miniatura
    for nombre in ("maxresdefault", "hqdefault"):
        try:
            open(os.path.join(salida, "miniatura.jpg"), "wb").write(bajar(f"https://i.ytimg.com/vi/{vid}/{nombre}.jpg"))
            break
        except Exception:
            pass

    # subtítulos (preferencia: español)
    pistas = jug.get("captions", {}).get("playerCaptionsTracklistRenderer", {}).get("captionTracks", [])
    pistas.sort(key=lambda p: (not p.get("languageCode", "").startswith("es"), p.get("kind") == "asr"))
    if pistas:
        try:
            crudo = json.loads(bajar(pistas[0]["baseUrl"] + "&fmt=json3"))
            lineas = []
            for ev in crudo.get("events", []):
                t = "".join(s.get("utf8", "") for s in ev.get("segs", []) or []).strip()
                if t:
                    s = ev.get("tStartMs", 0) // 1000
                    lineas.append(f"[{s // 60:02d}:{s % 60:02d}] {t}")
            open(os.path.join(salida, "transcripcion.txt"), "w", encoding="utf-8").write("\n".join(lineas))
            datos["subtitulos"] = pistas[0].get("languageCode") + (" (auto)" if pistas[0].get("kind") == "asr" else "")
        except Exception as e:
            datos["subtitulos"] = f"error: {e}"

    # storyboard: la especificación trae varios niveles; usamos el de más resolución
    spec = jug.get("storyboards", {}).get("playerStoryboardSpecRenderer", {}).get("spec", "")
    if spec:
        partes = spec.split("|")
        base = partes[0]
        nivel = len(partes) - 2
        ancho, alto, total, cols, filas, _, nombre, sigh = partes[-1].split("#")
        por_hoja = int(cols) * int(filas)
        hojas = -(-int(total) // por_hoja)
        for n in range(hojas):
            url = base.replace("$L", str(nivel)).replace("$N", nombre.replace("$M", str(n))) + "&sigh=" + sigh
            try:
                open(os.path.join(salida, f"storyboard_{n:02d}.jpg"), "wb").write(bajar(url))
            except Exception as e:
                print("storyboard", n, e)
        datos["storyboard"] = {"fotogramas": int(total), "por_hoja": por_hoja, "cols": int(cols), "hojas": hojas,
                               "tam": f"{ancho}x{alto}"}
    json.dump(datos, open(os.path.join(salida, "datos.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in datos.items() if k != "descripcion"}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv[1], sys.argv[2])
