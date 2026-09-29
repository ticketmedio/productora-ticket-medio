"""Lo ejecuta GitHub Actions (.github/workflows/sala_web.yml) cuando se abre una petición («issue») desde la Sala web.

Lee la petición, la valida y la añade a web/web_cambios.json. NUNCA toca datos.json: así no choca con el
servidor local, que es quien fusiona web_cambios.json en datos.json (y claude_sala.py, al empezar).
Deja en /tmp/respuesta.txt el texto con el que se cerrará la petición.

Uso: python3 web/aplicar_peticion.py RUTA_DEL_EVENTO_JSON
"""
import json, os, re, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CAMBIOS = os.path.join(HERE, "web_cambios.json")
RESPUESTA = os.path.join(tempfile.gettempdir(), "respuesta.txt")  # /tmp en GitHub Actions
ESTADOS = ("pendiente", "en_curso", "hecho")


def responder(texto):
    with open(RESPUESTA, "w", encoding="utf-8") as f:
        f.write(texto)
    print(texto)


def main():
    ev = json.load(open(sys.argv[1], encoding="utf-8"))
    issue = ev["issue"]
    dueno = ev["repository"]["owner"]["login"]
    if issue["user"]["login"] != dueno:
        return responder("Solo la cuenta del proyecto puede cambiar la Sala. Petición ignorada.")

    m = re.search(r"```json\s*(\{.*?\})\s*```", issue.get("body") or "", re.S)
    try:
        p = json.loads(m.group(1))
    except Exception:
        return responder("No he entendido la petición (¿se ha borrado el bloque del final?). Vuelve a pulsar el botón en la Sala.")

    accion = p.get("accion")
    tareas = {t["id"]: t for t in json.load(open(os.path.join(HERE, "datos.json"), encoding="utf-8"))["tareas"]}
    texto = str(p.get("texto") or "").strip()[:4000]
    cambio = {"id": f"w-{issue['number']}", "accion": accion, "fecha": issue["created_at"]}

    if accion in ("estado", "comentario"):
        if p.get("tarea") not in tareas:
            return responder("Esa tarea ya no existe en la Sala. Petición ignorada.")
        cambio["tarea"] = p["tarea"]
    if accion == "estado":
        if p.get("estado") not in ESTADOS:
            return responder("Estado desconocido. Petición ignorada.")
        cambio["estado"] = p["estado"]
        ok = f"Hecho ✅ «{tareas[p['tarea']]['title']}» → {p['estado'].replace('_', ' ')}."
    elif accion in ("comentario", "mensaje"):
        if not texto:
            return responder("El texto estaba vacío. Petición ignorada.")
        cambio["texto"] = texto
        ok = "Hecho ✅ Comentario guardado en la Sala." if accion == "comentario" else "Hecho ✅ Mensaje guardado en el Tablón."
    else:
        return responder("Acción desconocida. Petición ignorada.")

    try:
        d = json.load(open(CAMBIOS, encoding="utf-8"))
    except Exception:
        d = {"cambios": []}
    if all(c["id"] != cambio["id"] for c in d["cambios"]):
        d["cambios"].append(cambio)
    with open(CAMBIOS, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    responder(ok + " Se verá en la Sala web en 1–2 minutos.")


if __name__ == "__main__":
    main()
