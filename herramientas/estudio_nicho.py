"""Estudio de nichos: busca en YouTube España, lee los canales y mide outliers.

Guarda cada petición en youtube/estudio_nicho/cache/, así que si se corta se puede
volver a lanzar y continúa donde lo dejó.

  python herramientas/estudio_nicho.py        (recoge datos y escribe el resumen)
"""
import csv, hashlib, json, os, re, statistics, sys, time

sys.path.insert(0, os.path.dirname(__file__))
import yt_buscar

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "youtube", "estudio_nicho")
CACHE = os.path.join(SALIDA, "cache")
CANALES_POR_NICHO = 20

NICHOS = {
    "economia_cotidiana": ["cómo gana dinero Mercadona", "por qué Mercadona es tan barato", "cómo gana dinero Zara Inditex explicado",
        "por qué El Corte Inglés sigue existiendo", "cuánto gana una gasolinera por litro", "por qué la gasolina es tan cara en España",
        "cómo gana dinero Lidl España", "negocio de los supermercados en España explicado"],
    "vivienda": ["por qué la vivienda es tan cara en España", "hipoteca fija o variable explicado", "cómo funciona una hipoteca explicado",
        "burbuja inmobiliaria España 2026", "por qué suben los alquileres en España", "cuánto cuesta comprar una casa gastos",
        "ley de vivienda explicada", "okupas España explicado"],
    "energia": ["factura de la luz explicada", "por qué sube la luz en España", "merecen la pena las placas solares",
        "aerotermia merece la pena", "cuánto cuesta cargar un coche eléctrico en España", "tarifa PVPC o mercado libre",
        "apagón España explicado", "cómo funciona el mercado eléctrico español"],
    "bancos_estafas": ["estafa bancaria SMS cómo funciona", "cómo ganan dinero los bancos España", "estafas más comunes en España",
        "por qué los bancos no pagan intereses", "tarjetas revolving explicado", "por qué suben los seguros de coche",
        "timo del hijo en apuros WhatsApp", "comisiones bancarias explicado"],
    "impuestos_pensiones": ["declaración de la renta explicada", "cómo funciona el IVA explicado", "cuánto paga un autónomo en España",
        "pensiones en España quiebra explicado", "cuánto cobraré de pensión", "impuestos en España explicado",
        "a dónde van mis impuestos", "por qué se pagan tantos impuestos en España"],
    "inversion": ["fondos indexados explicado", "qué es un ETF explicado", "cómo funciona la bolsa explicado",
        "invertir en bolsa desde cero España", "interés compuesto explicado", "letras del tesoro explicado",
        "por qué cae la bolsa", "cómo invertir 1000 euros España"],
    "coches": ["comprar coche segunda mano consejos", "ITV qué revisan", "coches chinos en España merecen la pena",
        "averías más caras coche", "cómo ganan dinero los concesionarios", "financiar coche trampa concesionario",
        "coche eléctrico o híbrido cuál comprar", "por qué los coches son tan caros"],
    "ia_trabajo": ["inteligencia artificial para autónomos", "herramientas IA para empresas", "automatizar tareas con IA pymes",
        "chatgpt para negocios tutorial", "IA para pequeñas empresas España", "automatizaciones n8n español",
        "claude code tutorial español", "ganar dinero con inteligencia artificial"],
    "consumidor": ["cómo reclamar a una aerolínea", "reclamar retraso vuelo indemnización", "letra pequeña lo que no te cuentan",
        "cómo reclamar a compañía telefónica", "derechos del consumidor España garantía", "trucos de supermercados para que gastes más",
        "obsolescencia programada explicado", "por qué todo es una suscripción"],
    "negocios": ["cuánto cuesta montar un bar en España", "franquicias rentables España", "cuánto gana un kiosco",
        "amazon fba España empezar", "montar un negocio en España cuánto cuesta", "negocios rentables España 2026",
        "cuánto gana una peluquería", "por qué cierran los bares"],
    "empleo_sueldos": ["sueldos en España por profesión", "oposiciones mejor pagadas", "nómina explicada",
        "trabajar en Suiza sueldo", "cuánto gana un camionero en España", "profesiones mejor pagadas España sin carrera",
        "cuánto gana un controlador aéreo", "por qué los sueldos son bajos en España"],
    "ingenieria_obras": ["megaestructuras de España", "cómo funciona el puerto de Algeciras", "AVE España ingeniería",
        "obras más caras de España", "aeropuertos fantasma España", "cómo funciona un centro logístico Amazon",
        "túnel más largo de España", "infraestructuras abandonadas España"],
    "historia_marcas": ["historia de Zara", "auge y caída empresa española", "qué pasó con Pescanova",
        "marcas españolas que desaparecieron", "historia de Mercadona", "qué fue de Fórum Filatélico",
        "historia de Chupa Chups", "empresas españolas que quebraron"],
}


def num(s):
    if not s:
        return None
    s = s.lower().replace("\xa0", " ")
    if "sin visualiz" in s or "ninguna" in s:
        return 0
    m = re.search(r"([\d.,]+)\s*(mil|m(?![a-zé])|k|mill)?", s)
    if not m:
        return None
    n, suf = m.group(1), m.group(2)
    if suf:
        return int(float(n.replace(".", "").replace(",", ".")) * (1000 if suf in ("mil", "k") else 1_000_000))
    return int(n.replace(".", "").replace(",", ""))


def meses(s):
    if not s:
        return None
    m = re.search(r"(\d+)\s*([a-zñí]+)", s.lower())
    if not m:
        return None
    n, u = int(m.group(1)), m.group(2)
    if u.startswith(("seg", "min", "hora", "h")) and not u.startswith("hace"):
        return 0
    if u.startswith(("día", "dia", "d")):
        return n / 30
    if u.startswith(("sem",)):
        return n / 4.3
    if u.startswith(("mes", "m")):
        return n
    if u.startswith(("año", "a")):
        return n * 12
    return None


def cacheado(tipo, clave, funcion):
    os.makedirs(CACHE, exist_ok=True)
    ruta = os.path.join(CACHE, f"{tipo}_{hashlib.md5(clave.encode()).hexdigest()[:12]}.json")
    if os.path.exists(ruta):
        return json.load(open(ruta, encoding="utf-8"))
    for intento in range(3):
        try:
            datos = funcion(clave)
            break
        except Exception as e:
            print("  error", clave, e, flush=True)
            time.sleep(3 + 5 * intento)
    else:
        return None
    json.dump(datos, open(ruta, "w", encoding="utf-8"), ensure_ascii=False)
    time.sleep(1)
    return datos


def analizar_canal(c):
    vids = [v for v in c["videos"] if num(v.get("visitas")) is not None]
    subs = num(c.get("suscriptores")) or 0
    visitas = [num(v["visitas"]) for v in vids]
    ult12 = [v for v in vids if (meses(v.get("hace")) or 99) <= 12]
    mejor = max(ult12, key=lambda v: num(v["visitas"]), default=None)
    mediana = statistics.median(visitas) if visitas else 0
    edades = sorted(m for m in (meses(v.get("hace")) for v in vids) if m is not None)
    return {
        "suscriptores": subs, "num_videos": num(c.get("num_videos")), "mediana_visitas": int(mediana),
        "mejor_12m": mejor["titulo"] if mejor else "", "visitas_mejor_12m": num(mejor["visitas"]) if mejor else 0,
        "hace_mejor": mejor.get("hace", "") if mejor else "",
        "ratio_mejor": round((num(mejor["visitas"]) if mejor else 0) / max(subs, 1), 1),
        "ratio_mediana": round(mediana / max(subs, 1), 2),
        "videos_ult_3m": sum(1 for m in edades if m <= 3),
        "canal_nuevo": bool(edades) and edades[-1] <= 12 if len(vids) < 30 else False,
    }


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    filas, resumen = [], {}
    for nicho, consultas in NICHOS.items():
        print("NICHO", nicho, flush=True)
        videos = []
        for q in consultas:
            r = cacheado("busq", q, yt_buscar.buscar) or []
            for v in r:
                v["consulta"] = q
            videos += r
        # canales ordenados por el mejor vídeo que aparece en las búsquedas
        mejores = {}
        for v in videos:
            h = v.get("canal_url", "")
            if h.startswith("/@") and (num(v["visitas"]) or 0) >= (mejores.get(h, {}).get("n", -1)):
                mejores[h] = {"n": num(v["visitas"]) or 0, "canal": v["canal"]}
        handles = sorted(mejores, key=lambda h: -mejores[h]["n"])[:CANALES_POR_NICHO]
        # saturación: vídeos de menos de 6 meses con menos de 500 visitas
        recientes = [v for v in videos if (meses(v.get("hace")) or 99) <= 6]
        flojos = [v for v in recientes if (num(v["visitas"]) or 0) < 500]
        top = sorted(videos, key=lambda v: -(num(v["visitas"]) or 0))
        vistos, top_unicos = set(), []
        for v in top:
            if v["id"] not in vistos:
                vistos.add(v["id"]); top_unicos.append(v)
        top10 = top_unicos[:10]
        resumen[nicho] = {
            "videos_en_busquedas": len(videos),
            "recientes_6m": len(recientes), "recientes_flojos_<500": len(flojos),
            "canales_distintos_flojos": len({v["canal"] for v in flojos}),
            "top10": [{"titulo": v["titulo"], "visitas": num(v["visitas"]), "canal": v["canal"], "hace": v["hace"],
                       "duracion": v["duracion"]} for v in top10],
            "mediana_top10": statistics.median([num(v["visitas"]) or 0 for v in top10]) if top10 else 0,
            "edad_media_top10_meses": round(statistics.mean([meses(v["hace"]) or 0 for v in top10]), 1) if top10 else 0,
        }
        for h in handles:
            c = cacheado("canal", h.lstrip("/"), yt_buscar.canal)
            if not c or not c.get("videos"):
                continue
            a = analizar_canal(c)
            filas.append({"nicho": nicho, "canal": mejores[h]["canal"], "handle": h.lstrip("/"), **a})
        print("  canales", len(handles), flush=True)

    campos = list(filas[0].keys())
    with open(os.path.join(SALIDA, "canales.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=campos, delimiter=";")
        w.writeheader(); w.writerows(filas)
    for nicho in resumen:
        propios = [f for f in filas if f["nicho"] == nicho]
        peq = [f for f in propios if 0 < f["suscriptores"] <= 100_000]
        resumen[nicho]["outliers"] = sorted(peq, key=lambda f: -f["ratio_mejor"])[:6]
        resumen[nicho]["canales_pequenos_con_video_>=3x_subs"] = sum(1 for f in peq if f["ratio_mejor"] >= 3 and f["visitas_mejor_12m"] >= 20_000)
        resumen[nicho]["canales_analizados"] = len(propios)
    json.dump(resumen, open(os.path.join(SALIDA, "resumen.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("HECHO", flush=True)


if __name__ == "__main__":
    main()
