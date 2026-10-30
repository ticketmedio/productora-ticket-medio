"""Vídeo de YouTube en formato nuevo (30/10/2026): voz de narrador con emoción (Gemini TTS, gratis) + un clip real de Pexels por frase
+ subtítulos con la palabra que suena resaltada + logo de Ticket Medio. Después, sus Shorts verticales recortados del largo.

Uso: python3 herramientas/video_real.py youtube/video_NNN_tema [--solo-largo | --solo-shorts]
Lee:  CARPETA/05_VOICEOVER.txt (guion; si existe 05_VOICEOVER_V2.txt, usa ese) y CARPETA/shorts.json (tramos de cada Short).
Deja: CARPETA/output/FINAL_YOUTUBE_1080P.mp4 y CARPETA/output/SHORT_NN_*.mp4 (los nombres de los Shorts se mantienen).
Trabajo intermedio en CARPETA/real/ (voz, palabras, escenas, clips): se reutiliza al repetir, así no se gasta cupo de voz."""
import array, base64, difflib, json, os, re, subprocess, sys, time, unicodedata, urllib.parse, urllib.request, wave
from comun import FFMPEG, FFPROBE

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MPT = os.path.expanduser("~/herramientas_externas/MoneyPrinterTurbo")
PY_MPT = os.path.join(MPT, ".venv", "bin", "python")
V = os.path.abspath(sys.argv[1]); R = os.path.join(V, "real"); os.makedirs(R, exist_ok=True)
claves = open(os.path.join(RAIZ, "config", "claves.txt")).read()
GEM = re.search(r"GEMINI_CLAVE:\s*(\S+)", claves).group(1)
PEX = re.search(r"PEXELS_CLAVE:\s*(\S+)", claves).group(1)
CACHE = os.path.join(RAIZ, "privado", "pexels_cache"); os.makedirs(CACHE, exist_ok=True)
FUENTES = os.path.join(RAIZ, "herramientas", "fuentes")
MUSICA = os.path.join(RAIZ, "musica", "ticket_medio", "Cutscene Crush - Blue Deer Studio.mp3")
VOZ_NOMBRE = "Fenrir"
# Formato de la guía de Google (perfil + notas + TRANSCRIPT): con «lee solo lo que va tras los dos puntos», 3.8 leía las notas en voz alta
DIRECCION = ("# AUDIO PROFILE: Narrator\n### DIRECTOR'S NOTES\n"
             'Narrate this like a gripping Spanish true-story documentary on YouTube: a male narrator from Spain (Castilian, peninsular accent), warm but intense, full of emotion and suspense. Hook hard at the start, build tension, use dramatic pauses before key numbers, sound genuinely surprised or indignant at the revelations, and keep a confident, punchy rhythm.'
             "\nDo not read these notes aloud.\n#### TRANSCRIPT\n")
guion_txt = open(os.path.join(V, "05_VOICEOVER_V2.txt" if os.path.exists(os.path.join(V, "05_VOICEOVER_V2.txt")) else "05_VOICEOVER.txt"),
                 encoding="utf-8").read().strip()
guion = " ".join(guion_txt.split())


def dur(p):
    return float(subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout)


def norm(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-zñ0-9 ]", " ", s).split()


def api_gemini(modelo, cuerpo, timeout=300):
    req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent",
                                 data=json.dumps(cuerpo).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": GEM})
    return json.load(urllib.request.urlopen(req, timeout=timeout))


def transcribir(audio, salida_json, modelo="small"):
    if not os.path.exists(salida_json):
        subprocess.run([PY_MPT, "-c",
                        "import json;from faster_whisper import WhisperModel;"
                        f"m=WhisperModel({modelo!r},device='cpu',compute_type='int8');"
                        f"s,_=m.transcribe({audio!r},language='es',word_timestamps=True);"
                        f"json.dump([[w.word.strip(),w.start,w.end] for x in s for w in x.words],open({salida_json!r},'w'),ensure_ascii=False)"],
                       check=True)
    return json.load(open(salida_json))


# ── 1) Voz: el guion en trozos de ~2.500 caracteres (por párrafos), cada uno una petición; se comprueba que no lea las instrucciones ──
MODELOS = ["gemini-3.8-flash-tts", "gemini-3.1-flash-tts-preview", "gemini-2.5-flash-preview-tts"]


def tts(texto, destino):
    if os.path.exists(destino):
        return
    for intento in range(8):
        modelo = MODELOS[0]
        try:
            d = api_gemini(modelo, {"contents": [{"parts": [{"text": DIRECCION + texto}]}],
                                    "generationConfig": {"responseModalities": ["AUDIO"],
                                                         "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": VOZ_NOMBRE}}}}}, 600)
            pcm = base64.b64decode(d["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
        except urllib.error.HTTPError as e:
            if e.code == 429 and len(MODELOS) > 1:
                print("voz:", modelo, "sin cupo hoy, paso a", MODELOS[1], flush=True); MODELOS.pop(0); continue
            if e.code == 429:
                print("SIN_CUPO: los modelos de voz gratuitos están agotados hasta mañana (9:00)", flush=True); sys.exit(75)
            print("voz: reintento", e.code, flush=True); time.sleep(15 * (intento + 1)); continue
        except Exception as e:
            print("voz: reintento", type(e).__name__, flush=True); time.sleep(15 * (intento + 1)); continue
        tmp = destino + ".tmp.wav"
        w = wave.open(tmp, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000); w.writeframes(pcm); w.close()
        oido = norm(" ".join(x[0] for x in transcribir(tmp, tmp + ".json", "base")[:14]))
        os.remove(tmp + ".json")
        if sum(p in oido for p in norm(texto)[:6]) >= 3:
            os.replace(tmp, destino); return
        print("voz: ha leído algo que no es el guion, repito", flush=True); os.remove(tmp)
    raise SystemExit("No consigo una voz limpia")


def voz_completa():
    final = os.path.join(R, "voz.mp3")
    if os.path.exists(final):
        return final
    trozos, actual = [], ""
    for par in [p.strip() for p in guion_txt.split("\n\n") if p.strip()]:
        if actual and len(actual) + len(par) > 2500:
            trozos.append(actual); actual = ""
        actual = (actual + "\n\n" + par).strip()
    trozos.append(actual)
    lista = []
    for i, t in enumerate(trozos):
        p = os.path.join(R, f"voz_{i:02d}.wav"); tts(" ".join(t.split()), p); lista.append(p)
        print(f"voz: trozo {i + 1}/{len(trozos)} ({dur(p):.0f} s)", flush=True)
    with open(os.path.join(R, "voz_lista.txt"), "w") as f:
        for p in lista:
            f.write(f"file '{p}'\nfile '{os.path.join(R, 'pausa.wav')}'\n")
    subprocess.run([FFMPEG, "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", "0.35", os.path.join(R, "pausa.wav")], check=True)
    subprocess.run([FFMPEG, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", os.path.join(R, "voz_lista.txt"),
                    "-af", "loudnorm=I=-16:TP=-1.5", "-ar", "44100", final], check=True)
    return final


# ── 2) Palabras con tiempos; el texto sale del guion (el transcriptor se equivoca), los tiempos de la voz ──
def palabras_alineadas(voz):
    oidas = transcribir(voz, os.path.join(R, "palabras_oidas.json"))
    gtok = guion.split()
    gn, on = [" ".join(norm(t)) for t in gtok], [" ".join(norm(w[0])) for w in oidas]
    tiempos = [None] * len(gtok)
    for a, b, n_ in difflib.SequenceMatcher(None, gn, on, autojunk=False).get_matching_blocks():
        for j in range(n_):
            tiempos[a + j] = (oidas[b + j][1], oidas[b + j][2])
    conocidos = [i for i, t in enumerate(tiempos) if t]
    for i in range(len(gtok)):
        if tiempos[i] is None:
            ant = max([k for k in conocidos if k < i], default=None); sig = min([k for k in conocidos if k > i], default=None)
            t0 = tiempos[ant][1] if ant is not None else 0.0
            t1 = tiempos[sig][0] if sig is not None else (oidas[-1][2] if oidas else t0 + 0.4)
            hueco = (sig if sig is not None else len(gtok)) - (ant if ant is not None else -1)
            pos = i - (ant if ant is not None else -1)
            tiempos[i] = (t0 + (t1 - t0) * (pos - 1) / hueco, t0 + (t1 - t0) * pos / hueco)
    return [[t, a, b] for t, (a, b) in zip(gtok, tiempos)]


# ── 3) Escenas: una por frase (mínimo ~3 s); las búsquedas de Pexels las propone Gemini (texto, gratis) y se guardan para revisarlas ──
def escenas(palabras):
    ruta = os.path.join(R, "escenas.json")
    if os.path.exists(ruta):
        return json.load(open(ruta))
    frases, ini = [], 0
    for i, w in enumerate(palabras):
        fin_frase = re.search(r"[.!?…:]$", w[0]) is not None
        if (fin_frase and palabras[i][2] - palabras[ini][1] >= 3.0) or i == len(palabras) - 1:
            frases.append({"i0": ini, "i1": i, "texto": " ".join(x[0] for x in palabras[ini:i + 1])}); ini = i + 1
    prompt = ("You choose stock footage for a Spanish YouTube documentary about how Spanish/European companies make money. "
              "For EACH numbered Spanish sentence, give 3 short English search queries for Pexels stock VIDEOS (2–4 words each, concrete and "
              "filmable: objects, places, people doing actions; e.g. 'airplane taking off', 'airport check in queue', 'woman paying cashier'). "
              "Show literally what the sentence talks about; for numbers or abstract ideas use a related concrete scene (money counting, "
              "charts on laptop, busy airport...). Never use brand names or people's names in queries. "
              "Answer ONLY JSON: [{\"n\":1,\"q\":[\"...\",\"...\",\"...\"]}, ...]\n\n" +
              "\n".join(f"{k + 1}. {f['texto']}" for k, f in enumerate(frases)))
    for modelo in ("gemini-3-flash-preview", "gemini-flash-latest", "gemini-2.5-flash"):   # los 2.5 ya no se dan a cuentas nuevas
        try:
            d = api_gemini(modelo, {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"responseMimeType": "application/json"}}, 300)
            qs = {x["n"]: x["q"] for x in json.loads(d["candidates"][0]["content"]["parts"][0]["text"])}
            break
        except Exception as e:
            print("búsquedas:", modelo, "falla", type(e).__name__, flush=True)
    else:
        raise SystemExit("No consigo las búsquedas de clips")
    for k, f in enumerate(frases):
        f["q"] = qs.get(k + 1, ["business office", "money counting", "city street people"])
    json.dump(frases, open(ruta, "w"), ensure_ascii=False, indent=1)
    return frases


VACIAS = {"a", "an", "the", "of", "in", "on", "into", "with", "and", "to", "at", "for", "close", "up", "people", "person"}
usados = set()


def pexels_busca(q, orient):
    """Búsqueda en Pexels con caché en disco (la API permite 200 peticiones por hora)."""
    c = os.path.join(CACHE, "busquedas", re.sub(r"[^a-z0-9]+", "_", f"{q}_{orient}".lower()) + ".json")
    if os.path.exists(c):
        return json.load(open(c))
    os.makedirs(os.path.dirname(c), exist_ok=True)
    url = "https://api.pexels.com/videos/search?" + urllib.parse.urlencode({"query": q, "orientation": orient, "per_page": 40, "size": "medium"})
    for intento in range(6):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"Authorization": PEX, "User-Agent": "Mozilla/5.0"}), timeout=60))
            json.dump(d, open(c, "w")); return d
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print("Pexels: límite por hora alcanzado, espero 10 min", flush=True); time.sleep(600); continue
            time.sleep(5)
        except Exception:
            time.sleep(5)
    return {"videos": []}


def buscar(q, minimo, exigir, orient_pref):
    claves_q = [w for w in q.lower().split() if w not in VACIAS]
    pedir = min(exigir, len(claves_q))
    for orient in (orient_pref, "portrait" if orient_pref == "landscape" else "landscape"):
        d = pexels_busca(q, orient)
        for v in d.get("videos", []):
            desc = {w.rstrip("s") for w in re.split(r"[^a-z]+", v["url"].lower().rstrip("/").split("/")[-1])}
            if v["id"] in usados or v["duration"] < min(minimo, 6):
                continue
            if sum(1 for w in claves_q if w.rstrip("s") in desc) < pedir:
                continue
            fs = [f for f in v["video_files"] if f.get("file_type") == "video/mp4" and f.get("height")]
            fs.sort(key=lambda f: abs(min(f["height"], f["width"]) - 1080))
            if not fs:
                continue
            usados.add(v["id"])
            ruta = os.path.join(CACHE, f"{v['id']}.mp4")
            if not os.path.exists(ruta):
                with urllib.request.urlopen(urllib.request.Request(fs[0]["link"], headers={"User-Agent": "Mozilla/5.0"}), timeout=180) as resp:
                    open(ruta + ".tmp", "wb").write(resp.read())
                os.replace(ruta + ".tmp", ruta)
            return ruta, v["duration"], v["url"]
    return None


def clip_escena(f, d_esc, salida, W, H, orient):
    """Convierte el mejor clip de la escena al tamaño final; si un clip falla, prueba otro."""
    for _ in range(4):
        r = None
        for exigir in (2, 1, 0):
            for q in f["q"]:
                r = buscar(q, d_esc, exigir, orient)
                if r:
                    break
            if r:
                break
        if not r:
            r = buscar("city street people walking", d_esc, 0, orient)
        ruta, dclip, enlace = r
        lento = max(1.0, d_esc / max(dclip - 0.5, 0.5))
        ini = max(0.0, min(dclip * 0.25, dclip - d_esc / lento - 0.2))
        ok = subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", f"{ini}", "-i", ruta, "-t", f"{d_esc / lento + 0.05:.3f}", "-an", "-vf",
                             f"setpts={lento:.3f}*PTS,scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,setsar=1,format=yuv420p",
                             "-t", f"{d_esc:.3f}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", salida], capture_output=True).returncode == 0
        if ok:
            return enlace
    raise SystemExit(f"No consigo un clip válido para «{f['texto'][:60]}»")


def ass_subs(palabras, t_ini, t_fin, W, H, tam, margen_v, ruta):
    def ts(x):
        x = max(0.0, x); return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
    ws = [w for w in palabras if w[1] >= t_ini - 0.05 and w[1] < t_fin]
    grupos, g = [], []
    for w in ws:
        g.append(w)
        if len(g) == 4 or re.search(r"[.,;:!?…]$", w[0]):
            grupos.append(g); g = []
    if g:
        grupos.append(g)
    lin = ["[Script Info]", f"PlayResX: {W}", f"PlayResY: {H}", "ScaledBorderAndShadow: yes", "", "[V4+ Styles]",
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
           f"Style: P,Archivo Black,{tam},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,{max(4, tam // 12)},3,2,60,60,{margen_v},1", "",
           "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    for gi, gr in enumerate(grupos):
        fin_g = grupos[gi + 1][0][1] if gi + 1 < len(grupos) else min(gr[-1][2] + 0.4, t_fin)
        for wi, w in enumerate(gr):
            a = w[1]; b = gr[wi + 1][1] if wi + 1 < len(gr) else fin_g
            txt = " ".join(("{\\c&H00D4FF&\\fscx110\\fscy110}" + x[0].upper() + "{\\r}") if j == wi else x[0].upper() for j, x in enumerate(gr))
            lin.append(f"Dialogue: 0,{ts(a - t_ini)},{ts(max(b, a + 0.05) - t_ini)},P,,0,0,0,,{txt}")
    open(ruta, "w", encoding="utf-8").write("\n".join(lin) + "\n")


def montar(lista_clips, audio, subs, logo_y, W, H, salida, t_total):
    with open(salida + ".lista.txt", "w") as f:
        f.writelines(f"file '{c}'\n" for c in lista_clips)
    logo = os.path.join(RAIZ, "youtube", "marca", "logo_800.png")
    filtro = (f"[2:v]scale={W // 9}:-1[l];[0:v][l]overlay=x=W-w-30:y={logo_y}," f"ass={subs}:fontsdir={FUENTES}")
    filtro += ",format=yuv420p[v];[3:a]volume=0.07[m];[1:a][m]amix=inputs=2:duration=first:dropout_transition=0,apad=pad_dur=0.8[a]"
    subprocess.run([FFMPEG, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", salida + ".lista.txt", "-i", audio, "-i", logo,
                    "-stream_loop", "-1", "-i", MUSICA, "-filter_complex", filtro, "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "20",
                    "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-t", f"{t_total:.2f}", salida], check=True)
    os.remove(salida + ".lista.txt")


voz = voz_completa()
palabras = palabras_alineadas(voz)
frases = escenas(palabras)
T = dur(voz) + 0.8
cortes = [palabras[f["i0"]][1] if k else 0.0 for k, f in enumerate(frases)] + [T]

# ── 4) Largo 1920x1080 ──
if "--solo-shorts" not in sys.argv:
    clips, creditos = [], []
    for k, f in enumerate(frases):
        c = os.path.join(R, f"h_{k:03d}.mp4")
        if not os.path.exists(c):
            creditos.append(clip_escena(f, cortes[k + 1] - cortes[k], c, 1920, 1080, "landscape"))
        clips.append(c)
        if k % 10 == 0:
            print(f"largo: escena {k + 1}/{len(frases)}", flush=True)
    if creditos:
        open(os.path.join(R, "creditos_pexels.txt"), "a").write("\n".join(creditos) + "\n")
    ass_subs(palabras, 0, T, 1920, 1080, 62, 70, os.path.join(R, "subs_largo.ass"))
    final = os.path.join(V, "output", "FINAL_YOUTUBE_1080P.mp4"); os.makedirs(os.path.dirname(final), exist_ok=True)
    montar(clips, voz, os.path.join(R, "subs_largo.ass"), 30, 1920, 1080, final, T)
    print("OK largo", final, f"{dur(final):.0f} s", flush=True)

# ── 5) Shorts 1080x1920: tramos del largo (shorts.json), mismos clips recortados en vertical, rótulo final hacia el largo ──
if "--solo-largo" not in sys.argv and os.path.exists(os.path.join(V, "shorts.json")):
    pn = [" ".join(norm(w[0])) for w in palabras]

    def busca(frase, desde=0):
        obj = norm(frase)
        for i in range(desde, len(pn)):
            if pn[i:i + len(obj)] == obj:
                return i
        obj = obj[:3]
        for i in range(desde, len(pn)):
            if pn[i:i + len(obj)] == obj:
                return i
        raise SystemExit(f"Short: no encuentro «{frase}» en la voz")

    viejos = {re.match(r"SHORT_(\d+)_", n).group(1): n for n in os.listdir(os.path.join(V, "output")) if re.match(r"SHORT_\d+_.*\.mp4$", n)}
    for s in json.load(open(os.path.join(V, "shorts.json")))["shorts"]:
        nombre = viejos.get(s["id"], f"SHORT_{s['id']}.mp4"); destino = os.path.join(V, "output", nombre)
        marca = os.path.join(R, f"short_{s['id']}.hecho")
        if os.path.exists(marca):
            continue
        rangos = []
        for a, b in s["tramos"]:
            i0 = busca(a); i1 = busca(b, i0); i1 = i1 + len(norm(b)) - 1
            rangos.append((max(0, palabras[i0][1] - 0.15), min(T, palabras[min(i1, len(palabras) - 1)][2] + 0.35)))
        partes, clips, pal_s, t_acum = [], [], [], 0.0
        for n_r, (a, b) in enumerate(rangos):
            p = os.path.join(R, f"s{s['id']}_audio_{n_r}.wav")
            subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", voz, p], check=True); partes.append(p)
            pal_s += [[w[0], w[1] - a + t_acum, w[2] - a + t_acum] for w in palabras if a <= w[1] < b]
            for k, f in enumerate(frases):              # clips de las escenas que caen en el tramo, en vertical
                ca, cb = max(cortes[k], a), min(cortes[k + 1], b)
                if cb - ca > 0.05:
                    c = os.path.join(R, f"v_{k:03d}.mp4")
                    if not os.path.exists(c):
                        clip_escena(f, cortes[k + 1] - cortes[k], c, 1080, 1920, "portrait")
                    corte = os.path.join(R, f"s{s['id']}_{n_r}_{k:03d}.mp4")
                    subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", f"{ca - cortes[k]:.3f}", "-i", c, "-t", f"{cb - ca:.3f}", "-c:v", "libx264",
                                    "-preset", "veryfast", "-crf", "20", "-an", corte], check=True)
                    clips.append(corte)
            t_acum += b - a
        audio_s = os.path.join(R, f"s{s['id']}_audio.wav")
        with open(audio_s + ".txt", "w") as f:
            f.writelines(f"file '{p}'\n" for p in partes)
        subprocess.run([FFMPEG, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", audio_s + ".txt", audio_s], check=True)
        ass_subs(pal_s, 0, t_acum + 1, 1080, 1920, 82, 560, os.path.join(R, f"s{s['id']}.ass"))
        montar(clips, audio_s, os.path.join(R, f"s{s['id']}.ass"), 120, 1080, 1920, destino, t_acum + 0.8)
        subprocess.run([sys.executable, os.path.join(RAIZ, "herramientas", "cierre_shorts.py"), V, s["id"]], capture_output=True)
        open(marca, "w").write(destino + "\n")
        print("OK short", s["id"], nombre, f"{dur(destino):.0f} s", flush=True)
# subtítulos y capítulos de la descripción con los tiempos de la voz nueva (si falla una frase de capítulo, se avisa y se arregla a mano)
r = subprocess.run([sys.executable, os.path.join(RAIZ, "herramientas", "textos_real.py"), V], capture_output=True, text=True)
print("textos:", (r.stdout + r.stderr).strip().replace("\n", " · "), flush=True)
print("TERMINADO", V, flush=True)
