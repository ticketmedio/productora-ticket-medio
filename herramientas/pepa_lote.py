"""Produce un Reel de Pepa Pita de principio a fin a partir de una ficha JSON.

Uso: python3 pepa_lote.py FICHA.json [--sin-render]

Ficha (todas las rutas son relativas a redes/pepa_pita):
{
  "id": "019", "slug": "caducidad", "fecha": "2026-11-03", "largo": false,
  "cabecera": "¿CADUCIDAD?",                      (≤ 18 caracteres)
  "fondo": "pexels_5451503",
  "gancho": {"tipo": "A", "texto": "¿FECHA PASADA? ¿A LA BASURA?"},
  "guion": "texto hablado (las cifras, en letra para la voz)",
  "rotulos": [{"clave": "consumo preferente", "texto": "CONSUMO PREFERENTE", "sub": "calidad, no seguridad · AESAN"}],
  "fuentes": ["- AESAN, ..."],                    (líneas de fuentes.md)
  "texto_pub": "texto de Instagram/Facebook/TikTok"
}
Genera voz (Marta MAI-Voice-2 ×1,12), planos de Pepa que cambian cada 3-6 s, rótulos anclados a la frase que
contiene su «clave», plan.json, fuentes.md, TEXTO_PUBLICACION.txt y el MP4 en salida/.
"""
import json, os, re, subprocess, sys, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(RAIZ, "redes", "pepa_pita")
HERR = os.path.join(RAIZ, "herramientas")
MUSICA = "../../../../musica/pepa_pita/Travelling Light - Blue Deer Studio.mp3"
CICLO = ["exp_sorprendida", "pose_senala", "exp_pensativa", "pose_sartenes", "exp_preocupada", "exp_riendo", "pose_senala", "exp_contenta"]


def seg(s):
    h, m, r = s.split(":"); x, ms = r.split(",")
    return int(h) * 3600 + int(m) * 60 + int(x) + int(ms) / 1000


def bloques(ruta):
    out = []
    for b in open(ruta, encoding="utf-8").read().strip().split("\n\n"):
        l = b.split("\n"); a, z = l[1].split(" --> ")
        out.append((seg(a), seg(z), " ".join(l[2:])))
    return out


def plano(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def main():
    ficha = json.load(open(sys.argv[1], encoding="utf-8"))
    nombre = f"{ficha['id']}_{ficha['slug']}"
    d = os.path.join(BASE, "videos", nombre)
    for sub in ("voz", "salida"):
        os.makedirs(os.path.join(d, sub), exist_ok=True)
    assert len(ficha["cabecera"]) <= 18, "cabecera > 18 caracteres"
    for r in ficha.get("rotulos", []):
        assert len(r["sub"]) <= 43, f"sub > 43: {r['sub']}"
    open(os.path.join(d, "guion.txt"), "w", encoding="utf-8").write(ficha["guion"].strip() + "\n")
    open(os.path.join(d, "fuentes.md"), "w", encoding="utf-8").write(
        f"# Fuentes — Pepa Pita {ficha['id']} «{ficha.get('titulo', ficha['slug'])}»\n" + "\n".join(ficha["fuentes"]) + "\n")
    open(os.path.join(d, "salida", "TEXTO_PUBLICACION.txt"), "w", encoding="utf-8").write(ficha["texto_pub"].strip() + "\n")

    if not os.path.exists(os.path.join(d, "voz", "voz_original.mp3")):
        subprocess.run([sys.executable, os.path.join(HERR, "voz.py"), os.path.join(d, "guion.txt"), os.path.join(d, "voz"),
                        "--voz", "es-ES-Marta:MAI-Voice-2"], check=True, cwd=HERR, capture_output=True)
        subprocess.run([sys.executable, os.path.join(HERR, "acelerar_voz.py"), os.path.join(d, "voz"), "1.12"],
                       check=True, cwd=HERR, capture_output=True)
    bl = bloques(os.path.join(d, "voz", "subtitulos.srt"))
    fin = bl[-1][1]

    planos, ult, k = [{"desde": 0, "imagen": "busto"}], 0.0, 0
    for i, (a, z, t) in enumerate(bl):
        if i == 0:
            continue
        if i == len(bl) - 1:
            planos.append({"desde": round(a, 2), "imagen": "exp_guino"}); break
        if a - ult >= 3.2 and (a + 2.5) < bl[-1][0]:
            img = "busto" if (len(planos) % 3 == 0) else CICLO[k % len(CICLO)]
            k += 0 if img == "busto" else 1
            planos.append({"desde": round(a, 2), "imagen": img}); ult = a

    rot = []
    usados = set()
    for r in ficha.get("rotulos", []):
        c = plano(r["clave"])
        i = next((j for j, b in enumerate(bl) if j not in usados and c in plano(b[2])), None)
        assert i is not None, f"No encuentro la clave «{r['clave']}» en el guion"
        usados.add(i)
        a, z = bl[i][0], bl[i][1]
        j = i
        while z - a < 3.0 and j + 1 < len(bl) - 1:
            j += 1; z = bl[j][1]
        rot.append({"desde": round(a, 2), "hasta": round(z, 2), "texto": r["texto"], "sub": r["sub"]})
    rot.sort(key=lambda x: x["desde"])
    for x, y in zip(rot, rot[1:]):
        x["hasta"] = min(x["hasta"], round(y["desde"] - 0.05, 2))

    g = dict(ficha["gancho"]); g["hasta"] = round(bl[0][1] if bl[0][1] >= 1.5 else bl[1][1], 2)
    plan = {"voz": "voz/voz.mp3", "subtitulos": "voz/subtitulos.srt", "musica": MUSICA, "musica_db": -22,
            "fondo": f"../../fondos/{ficha['fondo']}.jpg", "cabecera": ficha["cabecera"], "planos": planos,
            "rotulos": rot, "salida": f"salida/PEPA_{nombre}.mp4", "gancho": g}
    json.dump(plan, open(os.path.join(d, "plan.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{nombre}: voz {fin:.1f} s, {len(planos)} planos, {len(rot)} rótulos")
    if "--sin-render" in sys.argv:
        return
    r = subprocess.run([sys.executable, os.path.join(HERR, "pepa_video.py"), os.path.join(d, "plan.json")],
                       capture_output=True, text=True, cwd=HERR)
    print("OK" if r.returncode == 0 else "ERROR\n" + (r.stdout + r.stderr)[-600:])


main()
