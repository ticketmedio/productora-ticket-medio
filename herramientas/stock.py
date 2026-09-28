"""Busca y descarga vídeos o fotos de stock de Pexels (licencia gratuita, uso comercial permitido).

Uso:
  python stock.py video "warehouse workers" CARPETA [--n 3] [--vertical]
  python stock.py foto "supermarket aisle" CARPETA [--n 3] [--vertical]

- Busca mejor en inglés (hay muchos más resultados).
- Guarda cada archivo como pexels_<id>.mp4/.jpg y apunta autor, enlace y licencia en
  CARPETA/licencias.csv, que después se copia a 10_FUENTES.md.
"""
import argparse, csv, json, os, sys, urllib.parse, urllib.request
from comun import RAIZ

sys.stdout.reconfigure(encoding="utf-8")


def clave():
    for linea in open(os.path.join(RAIZ, "config", "claves.txt"), encoding="utf-8"):
        if linea.startswith("PEXELS_CLAVE:"):
            k = linea.split(":", 1)[1].strip()
            if k:
                return k
    sys.exit("Falta PEXELS_CLAVE en config/claves.txt (PASO 8).")


def pedir(url, k):
    req = urllib.request.Request(url, headers={"Authorization": k, "User-Agent": "ticketmedio"})
    return json.load(urllib.request.urlopen(req, timeout=30))


def descargar(url, destino):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(destino, "wb") as f:
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            f.write(b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tipo", choices=["video", "foto"])
    ap.add_argument("busqueda")
    ap.add_argument("carpeta")
    ap.add_argument("--n", type=int, default=3)
    ap.add_argument("--vertical", action="store_true")
    a = ap.parse_args()
    k = clave()
    os.makedirs(a.carpeta, exist_ok=True)
    orient = "portrait" if a.vertical else "landscape"
    q = urllib.parse.quote(a.busqueda)
    registro = os.path.join(a.carpeta, "licencias.csv")
    nuevo = not os.path.exists(registro)
    guardados = 0
    with open(registro, "a", newline="", encoding="utf-8") as fcsv:
        w = csv.writer(fcsv)
        if nuevo:
            w.writerow(["archivo", "tipo", "autor", "url_pexels", "busqueda", "licencia"])
        if a.tipo == "video":
            datos = pedir(f"https://api.pexels.com/videos/search?query={q}&orientation={orient}&size=medium&per_page=15", k)
            for v in datos.get("videos", []):
                if guardados >= a.n:
                    break
                if v.get("duration", 0) < 4:
                    continue
                # el archivo más cercano a 1080p sin pasarse de 4K
                archivos = [f for f in v["video_files"] if f.get("width") and f["file_type"] == "video/mp4"]
                objetivo = 1080 if not a.vertical else 1920
                archivos.sort(key=lambda f: (abs((f["height"] if not a.vertical else f["height"]) - objetivo), -f["width"]))
                if not archivos:
                    continue
                nombre = f"pexels_{v['id']}.mp4"
                destino = os.path.join(a.carpeta, nombre)
                if not os.path.exists(destino):
                    descargar(archivos[0]["link"], destino)
                w.writerow([nombre, "vídeo", v["user"]["name"], v["url"], a.busqueda, "Licencia Pexels (uso gratuito, comercial permitido)"])
                guardados += 1
                print(f"✓ {nombre} ({v['duration']} s) de {v['user']['name']}")
        else:
            datos = pedir(f"https://api.pexels.com/v1/search?query={q}&orientation={orient}&per_page=15", k)
            for p in datos.get("photos", [])[: a.n]:
                nombre = f"pexels_{p['id']}.jpg"
                destino = os.path.join(a.carpeta, nombre)
                if not os.path.exists(destino):
                    descargar(p["src"]["large2x"], destino)
                w.writerow([nombre, "foto", p["photographer"], p["url"], a.busqueda, "Licencia Pexels (uso gratuito, comercial permitido)"])
                guardados += 1
                print(f"✓ {nombre} de {p['photographer']}")
    if not guardados:
        print("No se ha encontrado nada. Prueba otra búsqueda (mejor en inglés).")


if __name__ == "__main__":
    main()
