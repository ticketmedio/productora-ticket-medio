"""Utilidades compartidas: localizar FFmpeg y rutas del proyecto."""
import glob, os, shutil

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _buscar(nombre):
    ruta = shutil.which(nombre)
    if ruta:
        return ruta
    base = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Microsoft", "WinGet")
    for patron in (os.path.join(base, "Links", nombre + ".exe"),
                   os.path.join(base, "Packages", "Gyan.FFmpeg*", "*", "bin", nombre + ".exe")):
        hallado = glob.glob(patron)
        if hallado:
            return hallado[0]
    raise SystemExit(f"No encuentro {nombre}. ¿Está instalado FFmpeg?")


FFMPEG = _buscar("ffmpeg")
FFPROBE = _buscar("ffprobe")
