"""Prepara los Shorts de un vídeo largo: recorta la voz en pausas naturales y crea sus subtítulos.

Uso: python herramientas/shorts_prep.py CARPETA_VIDEO
Lee CARPETA_VIDEO/shorts.json:
  {"shorts": [{"id": "01", "tramos": [["frase inicial", "frase final"], ...]}, ...]}
Crea CARPETA_VIDEO/shorts/short_ID/audio/voz.mp3 y subtitulos.srt (listos para escenas.js en vertical).
"""
import json, os, re, subprocess, sys, unicodedata
from comun import FFMPEG

sys.stdout.reconfigure(encoding="utf-8")
V = os.path.abspath(sys.argv[1])
VOZ = os.path.join(V, "audio", "voz.mp3")


def seg(s):
    h, m, r = s.split(":"); sec, ms = r.split(",")
    return int(h) * 3600 + int(m) * 60 + int(sec) + int(ms) / 1000


def fmt(t):
    t = max(t, 0); ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9ñ ]", " ", "".join(c for c in s if unicodedata.category(c) != "Mn"))).strip()


srt = []
for b in open(os.path.join(V, "audio", "subtitulos.srt"), encoding="utf-8").read().strip().split("\n\n"):
    l = b.splitlines(); a, z = l[1].split(" --> ")
    srt.append({"ini": seg(a.strip()), "fin": seg(z.strip()), "texto": " ".join(l[2:])})

# silencios de la locución, para cortar siempre en una pausa
r = subprocess.run([FFMPEG, "-hide_banner", "-nostats", "-i", VOZ, "-af", "silencedetect=noise=-38dB:d=0.18", "-f", "null", "-"],
                   capture_output=True, text=True)
ini_s = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
fin_s = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
silencios = list(zip(ini_s, fin_s))


def pausa_cerca(t):
    """Centro del silencio más próximo a t (máximo 1,2 s de distancia)."""
    mejor = min(silencios, key=lambda s: abs((s[0] + s[1]) / 2 - t))
    c = (mejor[0] + mejor[1]) / 2
    return c if abs(c - t) <= 1.2 else t


def frase(trozo, desde=0):
    n = norm(trozo)
    for i, f in enumerate(srt):
        if f["fin"] >= desde and n in norm(f["texto"]):
            return i
    raise SystemExit(f"No encuentro «{trozo}» en el SRT")


cfg = json.load(open(os.path.join(V, "shorts.json"), encoding="utf-8"))
for sh in cfg["shorts"]:
    d = os.path.join(V, "shorts", f"short_{sh['id']}", "audio")
    os.makedirs(d, exist_ok=True)
    partes, subs, t_acum = [], [], 0.0
    for k, (a, z) in enumerate(sh["tramos"]):
        i = frase(a); j = frase(z, srt[i]["ini"])
        t0, t1 = pausa_cerca(srt[i]["ini"]), pausa_cerca(srt[j]["fin"])
        parte = os.path.join(d, f"_p{k}.wav")
        subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", f"{t0:.3f}", "-to", f"{t1:.3f}", "-i", VOZ, "-af",
                        "afade=t=in:d=0.04,areverse,afade=t=in:d=0.08,areverse", parte], check=True)
        partes.append(parte)
        for f in srt[i:j + 1]:
            subs.append((t_acum + max(f["ini"] - t0, 0), t_acum + min(f["fin"], t1) - t0, f["texto"]))
        t_acum += t1 - t0
    lista = os.path.join(d, "_lista.txt")
    open(lista, "w", encoding="utf-8").write("".join(f"file '{p}'\n" for p in partes))
    subprocess.run([FFMPEG, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lista, "-c:a", "libmp3lame", "-b:a", "192k",
                    os.path.join(d, "voz.mp3")], check=True)
    for p in partes + [lista]:
        os.remove(p)
    # subtítulos cortos (máx. ~5 palabras por línea) para leer en el móvil
    lineas = []
    for a, z, texto in subs:
        pal = texto.split(); n = max(1, -(-len(pal) // 4)); paso = (z - a) / n
        for q in range(n):
            lineas.append((a + q * paso, a + (q + 1) * paso, " ".join(pal[q * 4:(q + 1) * 4])))
    def escribir(nombre, filas):
        open(os.path.join(d, nombre), "w", encoding="utf-8").write(
            "\n".join(f"{k + 1}\n{fmt(a)} --> {fmt(z)}\n{t}\n" for k, (a, z, t) in enumerate(filas)))
    escribir("subtitulos.srt", subs)            # frases completas: para anclar las escenas
    escribir("subtitulos_cortos.srt", lineas)   # trozos cortos: los que se queman en el vídeo
    print(f"✓ short_{sh['id']}: {t_acum:.1f} s, {len(lineas)} subtítulos")
