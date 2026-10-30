"""Pone al día los textos de un vídeo de YouTube rehecho con video_real.py (voz nueva = tiempos nuevos).

Uso: python3 herramientas/textos_real.py youtube/video_NNN_x
- 06_SUBTITULOS.srt: se rehace con el texto de 05_VOICEOVER_V2.txt y los tiempos de la voz nueva (real/palabras_oidas.json).
  Se escribe en audio/subtitulos.srt (la antigua queda en audio/subtitulos_voz_antigua.srt) y después se llama a
  textos_video.py, que rehace 06_SUBTITULOS.srt, 08_DESCRIPCION.txt (capítulos con los tiempos nuevos + créditos), etc.
  Si una frase de capítulo de textos.json ya no está en el guion V2, textos_video.py lo dice: se cambia la frase en textos.json.
"""
import difflib, json, os, re, shutil, subprocess, sys, unicodedata

V = sys.argv[1].rstrip("/")


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return [w for w in re.split(r"[^a-z0-9ñ]+", "".join(c for c in s if unicodedata.category(c) != "Mn")) if w]


def seg(t):
    return t.count(":") and sum(int(x) * 60 ** i for i, x in enumerate(reversed(t.split(":"))))


def srt_t(x):
    return f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{int(x % 60):02d},{int(round(x % 1 * 1000)) % 1000:03d}"


# palabras del guion V2 con los tiempos de la voz (igual que palabras_alineadas() de video_real.py)
guion = open(os.path.join(V, "05_VOICEOVER_V2.txt"), encoding="utf-8").read().split()
oidas = json.load(open(os.path.join(V, "real", "palabras_oidas.json")))
gn, on = [" ".join(norm(t)) for t in guion], [" ".join(norm(w[0])) for w in oidas]
tiempos = [None] * len(guion)
for a, b, n in difflib.SequenceMatcher(None, gn, on, autojunk=False).get_matching_blocks():
    for j in range(n):
        tiempos[a + j] = (oidas[b + j][1], oidas[b + j][2])
conocidos = [i for i, t in enumerate(tiempos) if t]
for i in range(len(guion)):
    if tiempos[i] is None:
        ant = max([k for k in conocidos if k < i], default=None); sig = min([k for k in conocidos if k > i], default=None)
        t0 = tiempos[ant][1] if ant is not None else 0.0
        t1 = tiempos[sig][0] if sig is not None else oidas[-1][2]
        hueco = (sig if sig is not None else len(guion)) - (ant if ant is not None else -1)
        pos = i - (ant if ant is not None else -1)
        tiempos[i] = (t0 + (t1 - t0) * (pos - 1) / hueco, t0 + (t1 - t0) * pos / hueco)

# 1) subtítulos: una frase por bloque (las largas se parten en trozos de ~12 palabras)
bloques, ini = [], 0
for i, w in enumerate(guion):
    if re.search(r"[.!?…:]$", w) or i - ini >= 11 and re.search(r"[,;]$", w) or i - ini >= 15 or i == len(guion) - 1:
        bloques.append((tiempos[ini][0], tiempos[i][1], " ".join(guion[ini:i + 1]))); ini = i + 1
srt = os.path.join(V, "audio", "subtitulos.srt"); os.makedirs(os.path.dirname(srt), exist_ok=True)
viejo = os.path.join(V, "audio", "subtitulos_voz_antigua.srt")
if os.path.exists(srt) and not os.path.exists(viejo):
    shutil.copy(srt, viejo)
with open(srt, "w", encoding="utf-8") as f:
    for k, (a, b, txt) in enumerate(bloques):
        fin = min(b + 0.3, bloques[k + 1][0]) if k + 1 < len(bloques) else b + 0.5
        f.write(f"{k + 1}\n{srt_t(a)} --> {srt_t(fin)}\n{txt}\n\n")
print(f"{V}: {len(bloques)} subtítulos con la voz nueva")
sys.exit(subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "textos_video.py"), V]).returncode)
