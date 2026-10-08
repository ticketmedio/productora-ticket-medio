"""Genera los textos de publicación de un vídeo largo de Ticket Medio a partir de un `textos.json`.

Uso: python3 herramientas/textos_video.py CARPETA_VIDEO
Lee CARPETA_VIDEO/textos.json y CARPETA_VIDEO/audio/subtitulos.srt y escribe:
  06_SUBTITULOS.srt, 07_TITULOS.md, 08_DESCRIPCION.txt (con capítulos), COMENTARIO_FIJADO.txt, SHORTS_TEXTOS.txt

textos.json:
{ "n": 6, "nombre": "la factura de la luz", "titulo": "...", "alternativas": ["...", "..."], "miniatura": "texto de la miniatura",
  "etiquetas": "a, b, c", "descripcion": "párrafos antes de los capítulos", "capitulos": [["Nombre", "frase del guion"], ...],
  "vistos": "Vídeos anteriores: ...", "hashtags": "#A #B #C", "comentario": ["· fuente 1", "· fuente 2"],
  "shorts": [{"id": "01", "archivo": "SHORT_01_x.mp4", "dia": "sábado 24/10", "titulo": "...", "descripcion": "...", "hashtags": "#A #B"}] }
"""
import json, os, re, shutil, sys, unicodedata

V = os.path.abspath(sys.argv[1])
cfg = json.load(open(os.path.join(V, "textos.json"), encoding="utf-8"))
sys.stdout.reconfigure(encoding="utf-8")


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9ñ ]", " ", s)).strip()


def seg(s):
    h, m, r = s.split(":"); x, ms = r.split(",")
    return int(h) * 3600 + int(m) * 60 + int(x) + int(ms) / 1000


srt = []
for b in open(os.path.join(V, "audio", "subtitulos.srt"), encoding="utf-8").read().strip().split("\n\n"):
    l = b.splitlines(); a = l[1].split(" --> ")[0]
    srt.append((seg(a), " ".join(l[2:])))


def t(frase):
    n = norm(frase)
    for a, x in srt:
        if n in norm(x):
            return a
    raise SystemExit(f"No encuentro en el SRT: «{frase}»")


def f(x):
    x = int(x)
    return f"{x // 60}:{x % 60:02d}"


shutil.copy(os.path.join(V, "audio", "subtitulos.srt"), os.path.join(V, "06_SUBTITULOS.srt"))
caps = "\n".join(f"{f(0) if i == 0 else f(t(fr))} {nom}" for i, (nom, fr) in enumerate(cfg["capitulos"]))
n = cfg["n"]
alts = "\n".join(f"{i + 2}. {a}" + (" (prueba A/B)." if i == 0 else ".") for i, a in enumerate(cfg["alternativas"]))
open(os.path.join(V, "07_TITULOS.md"), "w", encoding="utf-8").write(
    f"# 07 · TÍTULOS — Vídeo {n:03d} ({cfg['nombre']})\n\nDecididos ANTES del guion (ver `00_PACKAGING.md`).\n\n"
    f"1. **{cfg['titulo']}** ← ELEGIDO ({len(cfg['titulo'])} caracteres).\n{alts}\n\n"
    f"Miniatura: output/MINIATURA_1280x720.png («{cfg['miniatura']}»).\n\n## Etiquetas (copiar tal cual en «Etiquetas»)\n{cfg['etiquetas']}\n")
open(os.path.join(V, "08_DESCRIPCION.txt"), "w", encoding="utf-8").write(
    cfg["descripcion"].strip() + "\n\nCAPÍTULOS\n" + caps +
    "\n\nEn Ticket Medio explicamos cómo ganan dinero las empresas y servicios que pagas cada día en España. Explicamos, no aconsejamos: "
    "nada de este vídeo es una recomendación de inversión ni de contratación.\n\n" + cfg.get("vistos", "") + "\n\n" + cfg["hashtags"] + "\n")
open(os.path.join(V, "COMENTARIO_FIJADO.txt"), "w", encoding="utf-8").write(
    "📌 Fuentes de las cifras del vídeo:\n\n" + "\n".join(cfg["comentario"]) + "\n\n¿Qué empresa o servicio quieres que analicemos la próxima vez? 👇\n")
out = f"SHORTS DEL VÍDEO {n} ({cfg['nombre'].upper()})\nPara cada Short: copia el TÍTULO en «Título» y la DESCRIPCIÓN en «Descripción». En «Vídeo relacionado» elige el vídeo largo de este tema.\n"
for s in cfg["shorts"]:
    out += (f"\n────────────────────────────────────────\nSHORT {int(s['id'])} · archivo {s['archivo']} · sale el {s['dia']} a las 13:00\n\n"
            f"TÍTULO:\n{s['titulo']} #shorts\n\nDESCRIPCIÓN:\n{s['descripcion']} El vídeo completo, en el canal.\n{s['hashtags']}\n")
open(os.path.join(V, "SHORTS_TEXTOS.txt"), "w", encoding="utf-8").write(out)
print("✓ textos del vídeo", n, "·", len(cfg["shorts"]), "Shorts ·", len(cfg["capitulos"]), "capítulos")
