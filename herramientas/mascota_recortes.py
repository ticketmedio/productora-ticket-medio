"""Recorta la mascota de Ticket Medio de los fondos azules (PNG con transparencia).

Uso: python herramientas/mascota_recortes.py
Lee youtube/marca/mascota/1..5.jfif (3 figuras por imagen) y escribe en youtube/marca/mascota/recortes/.
"""
import os, sys
from collections import deque
import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, os.path.dirname(__file__))
from pepa_recortes import quitar_azul

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIG = os.path.join(RAIZ, "youtube", "marca", "mascota")
SAL = os.path.join(ORIG, "recortes")
NOMBRES = {
    1: ["normal", "contento", "sorprendido"],
    2: ["pensativo", "enfadado", "riendo"],
    3: ["preocupado", "encoge_hombros", "corriendo"],
    4: ["senala", "carrito", "moneda"],
    5: ["lupa", "espaldas", "saluda"],
}


def manchas(im, f=4):
    """Etiqueta las figuras. Reduce por bloques con máximo para no romper brazos y piernas finos."""
    a = np.asarray(im.getchannel("A")) > 40
    h, w = a.shape[0] // f, a.shape[1] // f
    m = a[: h * f, : w * f].reshape(h, f, w, f).max(axis=(1, 3))
    lab = np.zeros((h, w), np.int32)
    tam, n = {}, 0
    for y in range(h):
        for x in range(w):
            if m[y, x] and not lab[y, x]:
                n += 1; cnt = 0; q = deque([(y, x)]); lab[y, x] = n
                while q:
                    cy, cx = q.popleft(); cnt += 1
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            ny, nx = cy + dy, cx + dx
                            if 0 <= ny < h and 0 <= nx < w and m[ny, nx] and not lab[ny, nx]:
                                lab[ny, nx] = n; q.append((ny, nx))
                tam[n] = cnt
    return lab, tam, f


def main():
    os.makedirs(SAL, exist_ok=True)
    for num, nombres in NOMBRES.items():
        im = quitar_azul(Image.open(os.path.join(ORIG, f"{num}.jfif")).convert("RGB"))
        lab, tam, f = manchas(im)
        grandes = sorted((k for k, v in tam.items() if v > 0.02 * lab.size), key=lambda k: -tam[k])[:3]
        # de izquierda a derecha
        grandes.sort(key=lambda k: np.argwhere(lab == k)[:, 1].mean())
        if len(grandes) != 3:
            print("⚠", num, "figuras encontradas:", len(grandes))
        for k, nombre in zip(grandes, nombres):
            keep = np.kron(lab == k, np.ones((f, f), bool))
            full = np.zeros(im.size[::-1], bool)
            full[: keep.shape[0], : keep.shape[1]] = keep
            km = np.asarray(Image.fromarray((full * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(7))) / 255
            arr = np.asarray(im).copy()
            arr[..., 3] = (arr[..., 3] * km).astype(np.uint8)
            out = Image.fromarray(arr, "RGBA")
            out = out.crop(out.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox())
            out.save(os.path.join(SAL, nombre + ".png"))
            print("✓", nombre, out.size)


if __name__ == "__main__":
    main()
