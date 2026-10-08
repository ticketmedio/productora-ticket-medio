"""Descarga una URL (HTML o PDF) y guarda su texto en privado/fuentes_cache/. Uso: python3 leer_fuente.py URL [palabra_clave ...]
Con palabras clave, imprime solo los fragmentos que las contienen (±300 caracteres)."""
import hashlib, html, io, os, re, subprocess, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
url, claves = sys.argv[1], sys.argv[2:]
datos = subprocess.run(["curl", "-sL", "--max-time", "90", "-A", "Mozilla/5.0", url], capture_output=True).stdout
if datos[:4] == b"%PDF":
    import pypdf
    texto = "\n".join((p.extract_text() or "") for p in pypdf.PdfReader(io.BytesIO(datos)).pages)
else:
    s = datos.decode("utf-8", "ignore")
    s = re.sub(r"(?s)<(script|style).*?</\1>", "", s)
    texto = html.unescape(re.sub(r"<[^>]+>", "\n", s))
texto = re.sub(r"\n\s*\n+", "\n", texto)
ruta = os.path.join(RAIZ, "privado", "fuentes_cache", hashlib.md5(url.encode()).hexdigest()[:10] + ".txt")
open(ruta, "w", encoding="utf-8").write(url + "\n" + texto)
print(f"[{len(texto)} caracteres → {ruta}]")
if claves:
    vistos = 0
    for m in re.finditer("|".join(re.escape(c) for c in claves), texto, re.I):
        print("…" + texto[max(0, m.start() - 300): m.end() + 300].replace("\n", " ") + "…\n"); vistos += 1
        if vistos >= 6: break
else:
    print(texto[:6000])
