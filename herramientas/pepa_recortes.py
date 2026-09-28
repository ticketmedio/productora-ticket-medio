"""Recorta a Pepa de los fondos azules y guarda cada imagen como PNG con transparencia.

Uso: python pepa_recortes.py
Lee redes/pepa_pita/personaje/*.jfif y escribe en redes/pepa_pita/recortes/.
"""
import os, sys
import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIG = os.path.join(RAIZ, "redes", "pepa_pita", "personaje")
SAL = os.path.join(RAIZ, "redes", "pepa_pita", "recortes")


def quitar_azul(img):
    a = np.asarray(img.convert("RGB")).astype(np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    azul = b - np.maximum(r, g)                      # cuánto "más azul" que el resto
    alfa = np.clip((45 - azul) / 30.0, 0, 1)         # transición suave en los bordes
    # quitar el reflejo azul de los bordes (despill)
    tope = np.maximum(r, g) + 8
    b2 = np.where(azul > 8, np.minimum(b, tope), b)
    out = np.dstack([r, g, b2, (alfa * 255)]).clip(0, 255).astype(np.uint8)
    im = Image.fromarray(out, "RGBA")
    caja = im.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox()
    return im.crop(caja) if caja else im


def solo_figura_principal(im):
    """Deja solo la mancha más grande (quita trozos de las figuras vecinas)."""
    from collections import deque
    a = np.asarray(im.getchannel("A")) > 40
    f = 4
    m = a[::f, ::f]
    h, w = m.shape
    lab = np.zeros((h, w), np.int32)
    mejor, mejor_n, n = 0, 0, 0
    for y in range(h):
        for x in range(w):
            if m[y, x] and not lab[y, x]:
                n += 1; cnt = 0; q = deque([(y, x)]); lab[y, x] = n
                while q:
                    cy, cx = q.popleft(); cnt += 1
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and m[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = n; q.append((ny, nx))
                if cnt > mejor_n:
                    mejor, mejor_n = n, cnt
    keep = np.kron(lab == mejor, np.ones((f, f), bool))[: a.shape[0], : a.shape[1]]
    # margen de unos píxeles para no comerse el borde suave
    from PIL import ImageFilter
    km = Image.fromarray((keep * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9))
    arr = np.asarray(im).copy()
    arr[..., 3] = (arr[..., 3] * (np.asarray(km) / 255)).astype(np.uint8)
    out = Image.fromarray(arr, "RGBA")
    return out.crop(out.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox())


def guardar(im, nombre):
    im.save(os.path.join(SAL, nombre + ".png"))
    print("✓", nombre, im.size)


def main():
    os.makedirs(SAL, exist_ok=True)
    # 6 expresiones (3x2), con el rótulo de texto debajo de cada una que hay que cortar
    ex = Image.open(os.path.join(ORIG, "pepa pita 2.jfif"))
    W, H = ex.size
    nombres = [["contenta", "sorprendida", "pensativa"], ["riendo", "guino", "preocupada"]]
    for fila in range(2):
        for col in range(3):
            x0, x1 = col * W // 3, (col + 1) * W // 3
            y0, y1 = fila * H // 2, (fila + 1) * H // 2 - int(H * 0.075)
            guardar(solo_figura_principal(quitar_azul(ex.crop((x0, y0, x1, y1)))), "exp_" + nombres[fila][col])
    # 4 poses en columnas
    po = Image.open(os.path.join(ORIG, "pepa pita 3.jfif"))
    W, H = po.size
    for i, n in enumerate(["senala", "sartenes", "ojo", "aplaude"]):
        x0, x1 = max(0, i * W // 4 - 60), min(W, (i + 1) * W // 4 + 60)
        guardar(solo_figura_principal(quitar_azul(po.crop((x0, 0, x1, H)))), "pose_" + n)
    # primer plano: pico cerrado (izquierda) y abierto (derecha), alineados
    bo = Image.open(os.path.join(ORIG, "pepa pita 4.jfif"))
    W, H = bo.size
    mitad = W // 2
    for n, caja in (("busto_cerrado", (0, 0, mitad - 6, H)), ("busto_abierto", (mitad + 6, 0, W, H))):
        im = bo.crop(caja)
        a = np.asarray(im.convert("RGB")).astype(np.int16)
        r, g, b = a[..., 0], a[..., 1], a[..., 2]
        azul = b - np.maximum(r, g)
        alfa = np.clip((45 - azul) / 30.0, 0, 1)
        b2 = np.where(azul > 8, np.minimum(b, np.maximum(r, g) + 8), b)
        im = Image.fromarray(np.dstack([r, g, b2, alfa * 255]).clip(0, 255).astype(np.uint8), "RGBA")
        guardar(im, n)  # sin recortar la caja: así las dos mitades siguen alineadas


if __name__ == "__main__":
    main()
