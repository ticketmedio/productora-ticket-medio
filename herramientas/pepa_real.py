"""Reel de Pepa en formato nuevo (29/10/2026): voz de Gemini con emoción + vídeo real de Pexels + subtítulos palabra a palabra
(MoneyPrinterTurbo) + Pepa hablando en una esquina (pico sincronizado con la voz).

Uso: python3 herramientas/pepa_real.py NNN_slug [--solo-voz]
Lee redes/pepa_pita/real/reels.json: {"NNN_slug": {"guion": "...", "terminos": "a,b,c", "largo": false}}
Deja el MP4 en redes/pepa_pita/videos/NNN_slug/salida/PEPA_NNN_slug.mp4 (sustituye al del formato antiguo)."""
import base64, json, os, re, shutil, subprocess, sys, time, urllib.request, wave
from comun import FFMPEG, FFPROBE

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MPT = os.path.expanduser("~/herramientas_externas/MoneyPrinterTurbo")
REC = os.path.join(RAIZ, "redes", "pepa_pita", "recortes")
# Formato de la guía de Google (perfil + notas + TRANSCRIPT): con «lee solo lo que va tras los dos puntos», 3.8 leía las notas en voz alta
DIRECCION = ("# AUDIO PROFILE: Pepa\n### DIRECTOR'S NOTES\n"
             'Perform this as Pepa, a hilarious, warm and very expressive Spanish hen who gives kitchen tips on Instagram. Native Spanish accent from Spain (Castilian, peninsular). Lots of emotion and variety: start with surprise and alarm, explain with a cheeky, friendly complicity, raise the energy on the warnings, and end laughing on the final «cloc, cloc». Fast, punchy Reel rhythm.'
             "\nDo not read these notes aloud.\n#### TRANSCRIPT\n")

slug = sys.argv[1]
cfg = json.load(open(os.path.join(RAIZ, "redes", "pepa_pita", "real", "reels.json"), encoding="utf-8"))[slug]
D = os.path.join(RAIZ, "redes", "pepa_pita", "real", slug); os.makedirs(D, exist_ok=True)
guion = " ".join(cfg["guion"].split())
clave = re.search(r"GEMINI_CLAVE:\s*(\S+)", open(os.path.join(RAIZ, "config", "claves.txt")).read()).group(1)


def dur(p):
    return float(subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout)


def norm(s):
    import unicodedata
    s = "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-zñ ]", " ", s).split()


def voz():
    body = {"contents": [{"parts": [{"text": DIRECCION + guion}]}],
            "generationConfig": {"responseModalities": ["AUDIO"], "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Sadachbia"}}}}}
    # el nivel gratuito da ~10 peticiones al día por modelo: si uno se agota (429), se pasa al siguiente
    modelos = ["gemini-3.8-flash-tts", "gemini-3.1-flash-tts-preview", "gemini-2.5-flash-preview-tts"]
    for intento in range(6):
        modelo = modelos[0]
        try:
            req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent",
                                         data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": clave})
            d = json.load(urllib.request.urlopen(req, timeout=300))
            pcm = base64.b64decode(d["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
        except urllib.error.HTTPError as e:
            if e.code == 429 and len(modelos) > 1:
                print("voz:", modelo, "sin cupo hoy, paso a", modelos[1], flush=True); modelos.pop(0); continue
            if e.code == 429:
                print("SIN_CUPO: los tres modelos de voz gratuitos están agotados hasta mañana (9:00)", flush=True); sys.exit(75)
            print("voz: reintento", e.code, flush=True); time.sleep(10 * (intento + 1)); continue
        except Exception as e:
            print("voz: reintento", type(e).__name__, flush=True); time.sleep(10 * (intento + 1)); continue
        tmp = os.path.join(D, "voz_prueba.wav")   # solo pasa a voz.wav si supera la comprobación (si no, se reutilizaría una voz mala)
        w = wave.open(tmp, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000); w.writeframes(pcm); w.close()
        # comprobar que no ha leído las instrucciones: las primeras palabras deben ser las del guion
        t = subprocess.run([os.path.join(MPT, ".venv", "bin", "python"), "-c",
                            "from faster_whisper import WhisperModel;m=WhisperModel('base',device='cpu',compute_type='int8');"
                            f"s,_=m.transcribe({tmp!r},language='es');print(' '.join(x.text for x in s))"],
                           capture_output=True, text=True).stdout
        ini, oido = norm(guion)[:6], norm(t)[:12]
        if sum(p in oido for p in ini) >= 3:
            os.replace(tmp, os.path.join(D, "voz.wav")); return
        os.remove(tmp)
        print("voz: ha leído algo que no es el guion, repito →", t[:80], flush=True)
    raise SystemExit("No consigo una voz limpia")


if not os.path.exists(os.path.join(D, "voz.wav")):
    voz()
maximo = 74 if cfg.get("largo") else 58
d0 = dur(os.path.join(D, "voz.wav")); vel = min(max(1.0, d0 / maximo), 1.15)
subprocess.run([FFMPEG, "-v", "error", "-y", "-i", os.path.join(D, "voz.wav"), "-af", f"atempo={vel:.3f},loudnorm=I=-16:TP=-1.5", "-ar", "44100",
                os.path.join(D, "voz.mp3")], check=True)
print(f"voz: {d0:.1f} s → {dur(os.path.join(D, 'voz.mp3')):.1f} s (×{vel:.2f})", flush=True)
if "--solo-voz" in sys.argv:
    raise SystemExit

# ── Montaje: cada escena (frase del guion) lleva su propio clip de Pexels, sincronizado con la voz ──
PEX = re.search(r"PEXELS_CLAVE:\s*(\S+)", open(os.path.join(RAIZ, "config", "claves.txt")).read()).group(1)
CACHE = os.path.join(RAIZ, "privado", "pexels_cache"); os.makedirs(CACHE, exist_ok=True)
VOZ = os.path.join(D, "voz.mp3"); TOTAL = dur(VOZ) + 0.6

# 1) tiempos de cada palabra (faster-whisper)
pal_json = os.path.join(D, "palabras.json")
if not os.path.exists(pal_json):
    subprocess.run([os.path.join(MPT, ".venv", "bin", "python"), "-c",
                    "import json;from faster_whisper import WhisperModel;m=WhisperModel('small',device='cpu',compute_type='int8');"
                    f"s,_=m.transcribe({VOZ!r},language='es',word_timestamps=True);"
                    f"json.dump([[w.word.strip(),w.start,w.end] for x in s for w in x.words],open({pal_json!r},'w'),ensure_ascii=False)"], check=True)
oidas = json.load(open(pal_json))
# el texto de los subtítulos sale del GUION (el transcriptor se equivoca: «tenegor», «cuco»); de la voz solo se toman los tiempos
import difflib
gtok = guion.split()
gn, on = [" ".join(norm(t)) for t in gtok], [" ".join(norm(w[0])) for w in oidas]
tiempos = [None] * len(gtok)
for a, b, n_ in difflib.SequenceMatcher(None, gn, on, autojunk=False).get_matching_blocks():
    for j in range(n_):
        tiempos[a + j] = (oidas[b + j][1], oidas[b + j][2])
conocidos = [i for i, t in enumerate(tiempos) if t]
for i in range(len(gtok)):                      # las palabras sin pareja se reparten entre sus vecinas
    if tiempos[i] is None:
        ant = max([k for k in conocidos if k < i], default=None); sig = min([k for k in conocidos if k > i], default=None)
        t0 = tiempos[ant][1] if ant is not None else 0.0
        t1 = tiempos[sig][0] if sig is not None else (oidas[-1][2] if oidas else t0 + 0.4)
        hueco = (sig if sig is not None else len(gtok)) - (ant if ant is not None else -1)
        pos = i - (ant if ant is not None else -1)
        tiempos[i] = (t0 + (t1 - t0) * (pos - 1) / hueco, t0 + (t1 - t0) * pos / hueco)
palabras = [[t, a, b] for t, (a, b) in zip(gtok, tiempos)]
pn = [" ".join(norm(w[0])) for w in palabras]


def momento(frase, desde_i):
    """Índice y segundo de la palabra donde empieza `frase` (busca las 3 primeras palabras, con tolerancia)."""
    obj = norm(frase)[:3]
    mejor = None
    for i in range(desde_i, len(pn)):
        aciertos = sum(1 for j, o in enumerate(obj) if i + j < len(pn) and pn[i + j] == o)
        if aciertos == len(obj):
            return i, palabras[i][1]
        if aciertos >= 2 and mejor is None:
            mejor = (i, palabras[i][1])
    if mejor:
        return mejor
    raise SystemExit(f"No encuentro en la voz el comienzo de la escena «{frase}»")


cortes, k = [], 0
for n, e in enumerate(cfg["escenas"]):
    k, t = momento(e["desde"], k) if n else (0, 0.0)
    cortes.append(t)
cortes.append(TOTAL)
# Pepa en primer plano (2–5 s, sin vídeo detrás) al empezar la última escena de al menos 2 s: el consejo final lo da ella a cámara
k_pp = next((n for n in range(len(cfg["escenas"]) - 1, -1, -1) if cortes[n + 1] - cortes[n] >= 2), len(cfg["escenas"]) - 1)
pp_a = cortes[k_pp]; pp_b = pp_a + min(4.5, cortes[k_pp + 1] - pp_a)
if cortes[k_pp + 1] - pp_b < 1.0 and cortes[k_pp + 1] - pp_a <= 5.5:   # si el resto del clip sería un parpadeo, toda la escena es de Pepa
    pp_b = cortes[k_pp + 1]

# 2) un clip de Pexels por escena (vertical si hay; si no, horizontal recortado), sin repetir
usados = set()


VACIAS = {"a", "an", "the", "of", "in", "on", "into", "with", "and", "to", "at", "for", "close", "up"}


def buscar(q, minimo, exigir=2):
    """Primer clip cuya descripción (el enlace de Pexels la lleva: /video/persona-cortando-pan-123/) contiene las palabras clave."""
    claves = [w for w in q.lower().split() if w not in VACIAS]
    pedir = min(exigir, len(claves))
    for orient in ("portrait", "landscape"):
        url = "https://api.pexels.com/videos/search?" + urllib.parse.urlencode({"query": q, "orientation": orient, "per_page": 40, "size": "medium"})
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"Authorization": PEX, "User-Agent": "Mozilla/5.0"}), timeout=60))
        for v in d.get("videos", []):
            desc = {w.rstrip("s") for w in re.split(r"[^a-z]+", v["url"].lower().rstrip("/").split("/")[-1])}
            if v["id"] in usados or v["duration"] < min(minimo, 6):
                continue
            if sum(1 for w in claves if w.rstrip("s") in desc) < pedir:   # palabras completas de la descripción
                continue
            fs = [f for f in v["video_files"] if f.get("file_type") == "video/mp4" and f.get("height")]
            fs.sort(key=lambda f: abs(min(f["height"], f["width"]) - 1080))
            if not fs:
                continue
            usados.add(v["id"])
            ruta = os.path.join(CACHE, f"{v['id']}.mp4")
            if not os.path.exists(ruta):
                with urllib.request.urlopen(urllib.request.Request(fs[0]["link"], headers={"User-Agent": "Mozilla/5.0"}), timeout=120) as resp:
                    open(ruta + ".tmp", "wb").write(resp.read())
                os.replace(ruta + ".tmp", ruta)
            return ruta, v["duration"], v["url"]
    return None


import urllib.parse
trozos, creditos = [], []
fondo = os.path.join(D, "fondo_pepa.png")
from PIL import Image, ImageDraw, ImageFilter
im = Image.new("RGB", (1080, 1920), (24, 46, 52)); dr = ImageDraw.Draw(im)
for r in range(1100, 0, -20):                       # degradado radial: el azul petróleo de Pepa, más claro detrás de ella
    c = int(24 + 40 * (1 - r / 1100)); dr.ellipse((540 - r, 1250 - r, 540 + r, 1250 + r), fill=(c, c * 46 // 24 + 8, c * 52 // 24 + 8))
im.filter(ImageFilter.GaussianBlur(40)).save(fondo)
for n, e in enumerate(cfg["escenas"]):
    d_esc = cortes[n + 1] - cortes[n]
    tr = os.path.join(D, f"esc_{n:02d}.mp4")
    if n == k_pp:
        pp = os.path.join(D, "esc_pepa.mp4")
        subprocess.run([FFMPEG, "-v", "error", "-y", "-loop", "1", "-i", fondo, "-t", f"{pp_b - pp_a:.3f}", "-vf", "fps=30,setsar=1,format=yuv420p",
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", pp], check=True)
        trozos.append(pp)
        print(f"  escena {n + 1}: {pp_a:.1f}–{pp_b:.1f} s · Pepa en primer plano", flush=True)
        d_esc = cortes[n + 1] - pp_b
        if d_esc < 0.05:
            continue
    for _ in range(4):                # si un clip no se puede convertir (formato raro), se prueba el siguiente
        r = None
        for exigir in (2, 1, 0):      # primero clips cuya descripción encaja del todo; si no hay, se relaja
            for q in [e["buscar"]] + e.get("alt", []):
                r = buscar(q, d_esc, exigir)
                if r:
                    break
            if r:
                break
        if not r:
            raise SystemExit(f"Pexels no tiene clip para «{e['buscar']}»")
        ruta, dclip, enlace = r
        lento = max(1.0, d_esc / max(dclip - 0.5, 0.5))          # si el clip es más corto que la frase, se ralentiza un poco
        ini = max(0.0, min(dclip * 0.25, dclip - d_esc / lento - 0.2))   # saltar fundidos de entrada del clip
        ok = subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", f"{ini}", "-i", ruta, "-t", f"{d_esc / lento + 0.05:.3f}", "-an", "-vf",
                             f"setpts={lento:.3f}*PTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p,"
                             f"zoompan=z='min(zoom+0.0006,1.06)':d=1:s=1080x1920:fps=30",
                             "-t", f"{d_esc:.3f}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", tr], capture_output=True).returncode == 0
        if ok:
            break
        print(f"  escena {n + 1}: clip {enlace.rstrip('/').split('/')[-1]} no se puede convertir, pruebo otro", flush=True)
    else:
        raise SystemExit(f"No consigo un clip válido para «{e['buscar']}»")
    creditos.append(enlace); trozos.append(tr)
    print(f"  escena {n + 1}: {cortes[n + 1] - d_esc:.1f}–{cortes[n + 1]:.1f} s · {e['buscar']} → {enlace.rstrip('/').split('/')[-1]}", flush=True)
with open(os.path.join(D, "escenas.txt"), "w") as f:
    f.writelines(f"file '{t}'\n" for t in trozos)
open(os.path.join(D, "creditos_pexels.txt"), "w").write("\n".join(creditos) + "\n")

# 3) subtítulos ASS: 2–3 palabras a la vez, la que suena en amarillo y un poco más grande
def ts(x):
    return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"


grupos, g = [], []
for w in palabras:
    g.append(w)
    if len(g) == 3 or re.search(r"[.,;:!?…]$", w[0]):
        grupos.append(g); g = []
if g:
    grupos.append(g)
ass = ["[Script Info]", "PlayResX: 1080", "PlayResY: 1920", "ScaledBorderAndShadow: yes", "", "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: P,Archivo Black,86,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,7,3,2,60,60,560,1",
       "Style: PT,Archivo Black,86,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,7,3,8,60,60,330,1", "",
       "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for gi, gr in enumerate(grupos):
    fin_g = grupos[gi + 1][0][1] if gi + 1 < len(grupos) else gr[-1][2] + 0.4
    for wi, w in enumerate(gr):
        a = w[1]; b = gr[wi + 1][1] if wi + 1 < len(gr) else fin_g
        txt = " ".join(("{\\c&H00D4FF&\\fscx112\\fscy112}" + x[0].upper() + "{\\r}") if j == wi else x[0].upper() for j, x in enumerate(gr))
        estilo = "PT" if pp_a - 0.05 <= gr[0][1] < pp_b else "P"   # con Pepa en primer plano, los subtítulos suben arriba
        ass.append(f"Dialogue: 0,{ts(a)},{ts(max(b, a + 0.05))},{estilo},,0,0,0,,{txt}")
open(os.path.join(D, "subs.ass"), "w", encoding="utf-8").write("\n".join(ass) + "\n")

# 4) Pepa hablando en la esquina: pico abierto cuando hay voz (ventanas de 1/12 s)
w = wave.open(os.path.join(D, "voz.wav")); n = w.getnframes(); pcm = w.readframes(n); w.close()
import array
mu = array.array("h", pcm); paso = int(24000 / 12)
niveles = [sum(abs(x) for x in mu[i:i + paso]) / max(1, len(mu[i:i + paso])) for i in range(0, len(mu), paso)]
umbral = sorted(niveles)[len(niveles) // 2] * 0.9
from PIL import Image
for nom in ("abierto", "cerrado"):
    Image.open(os.path.join(REC, f"busto_{nom}.png")).convert("RGBA").save(os.path.join(D, f"b_{nom}.png"))   # tamaño completo: se escala en el montaje
# con voz, el pico alterna abierto/cerrado cada 1/12 s; en silencio, cerrado
estados = ["abierto" if v > umbral and i % 2 == 0 else "cerrado" for i, v in enumerate(niveles)]
lista, t0 = [], 0
for i in range(1, len(estados) + 1):
    if i == len(estados) or estados[i] != estados[t0]:
        lista.append((estados[t0], (i - t0) / 12 / vel)); t0 = i
with open(os.path.join(D, "boca.txt"), "w") as f:
    for est, s in lista:
        f.write(f"file 'b_{est}.png'\nduration {s:.3f}\n")
    f.write(f"file 'b_cerrado.png'\n")
salida = os.path.join(RAIZ, "redes", "pepa_pita", "videos", slug, "salida"); os.makedirs(salida, exist_ok=True)
final = os.path.join(salida, f"PEPA_{slug}.mp4")
# en la esquina, Pepa cambia de lado en cada escena (izquierda, derecha…); durante el primer plano no sale
def lado(n):
    return "30" if n % 2 == 0 else "W-w-30"


x_esq = lado(len(cfg["escenas"]) - 1)
for n in range(len(cfg["escenas"]) - 2, -1, -1):
    x_esq = f"if(lt(t,{cortes[n + 1]:.2f}),{lado(n)},{x_esq})"
pp_t = f"between(t,{pp_a:.2f},{pp_b:.2f})"
musica = os.path.join(RAIZ, "musica", "pepa_pita", "Travelling Light - Blue Deer Studio.mp3")
fuentes = os.path.join(RAIZ, "herramientas", "fuentes")
subprocess.run([FFMPEG, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", os.path.join(D, "escenas.txt"),
                "-f", "concat", "-safe", "0", "-i", os.path.join(D, "boca.txt"), "-i", VOZ, "-stream_loop", "-1", "-i", musica,
                "-filter_complex",
                f"[1:v]format=rgba,split[pa][pb];[pa]scale=300:-1[p];[pb]scale=1000:-1[pg];"
                f"[0:v][p]overlay=x='{x_esq}':y='120+6*sin(2*PI*t*1.3)':eof_action=pass:enable='not({pp_t})'[v1];"
                f"[v1][pg]overlay=x=(W-w)/2:y='830+8*sin(2*PI*t*1.1)':eof_action=pass:enable='{pp_t}',"
                f"ass={os.path.join(D, 'subs.ass')}:fontsdir={fuentes},format=yuv420p[v];"
                "[3:a]volume=0.10[m];[2:a][m]amix=inputs=2:duration=first:dropout_transition=0,apad=pad_dur=0.6[a]",
                "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-c:a", "aac", "-b:a", "192k",
                "-movflags", "+faststart", "-t", f"{TOTAL:.2f}", final], check=True)
print("OK", final, f"{dur(final):.1f} s", flush=True)
open(os.path.join(D, "hecho"), "w").write(final + "\n")
