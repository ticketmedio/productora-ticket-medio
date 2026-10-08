"""Herramienta de Claude para leer y escribir en la Sala de Producción (datos.json).

Uso:
  python claude_sala.py novedades              -> lo nuevo del usuario desde la última revisión
  python claude_sala.py comentar ID "texto"    -> comentario de Claude en una tarea
  python claude_sala.py mensaje "texto"        -> mensaje de Claude en el Tablón
  python claude_sala.py estado ID ESTADO       -> pendiente | en_curso | hecho
  python claude_sala.py informe AAAA-MM-DD "titular" ARCHIVO.md [CLAVE]
                                               -> informe en «Informes diarios». CLAVE: seo (por defecto) | mercado-manana |
                                                  mercado-tarde. Si ya hay uno de esa fecha y clave, lo sustituye

Antes de cada orden trae de GitHub lo que el usuario haya hecho en la Sala web (web/web_cambios.json,
lo escribe GitHub Actions) y lo fusiona en datos.json.
"""
import json, sys, os, datetime

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "datos.json")
SEEN = os.path.join(HERE, ".claude_visto.json")
CAMBIOS_WEB = os.path.join(HERE, "web_cambios.json")


def now():
    return datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def load():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


def save(d):
    tmp = DATA + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    os.replace(tmp, DATA)


def aplicar_web(d):
    """Fusiona en d los cambios hechos desde la Sala web que aún no se habían aplicado. Devuelve True si hubo alguno."""
    try:
        cambios = json.load(open(CAMBIOS_WEB, encoding="utf-8"))["cambios"]
    except Exception:
        return False
    hechos = d.setdefault("aplicadosWeb", [])
    nuevo = False
    for c in cambios:
        if c["id"] in hechos:
            continue
        t = next((t for t in d["tareas"] if t["id"] == c.get("tarea")), None)
        if c["accion"] == "estado" and t:
            t["status"], t["updatedAt"] = c["estado"], now()
        elif c["accion"] == "comentario" and t:
            t.setdefault("comentarios", []).append({"id": "c-" + c["id"], "author": "tu", "text": c["texto"], "createdAt": now()})
        elif c["accion"] == "mensaje":
            d["mensajes"].append({"id": "m-" + c["id"], "author": "tu", "text": c["texto"], "createdAt": now()})
        hechos.append(c["id"])
        nuevo = True
    return nuevo


def sincronizar():
    """git pull y fusión de los cambios de la Sala web. Si hubo alguno, se publicará datos.json al terminar."""
    import subprocess
    subprocess.run("git pull -q --rebase --autostash", cwd=os.path.dirname(HERE), shell=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    d = load()
    if aplicar_web(d):
        save(d)
        return True
    return False


def novedades():
    d = load()
    try:
        seen = json.load(open(SEEN, encoding="utf-8"))
    except Exception:
        seen = {"desde": "", "estados": {}}
    desde, estados = seen.get("desde", ""), seen.get("estados", {})
    out = []
    for t in d["tareas"]:
        if t.get("createdBy") == "tu" and t.get("createdAt", "") > desde:
            out.append(f"NUEVA TAREA [{t['id']}] {t['title']} ({t['date']}, {t['who']}) notas: {t.get('notes','')}")
        prev = estados.get(t["id"])
        if prev is not None and prev != t["status"]:
            out.append(f"ESTADO [{t['id']}] {t['title']}: {prev} -> {t['status']}")
        for c in t.get("comentarios", []):
            if c["author"] == "tu" and c["createdAt"] > desde:
                out.append(f"COMENTARIO [{t['id']}] {t['title']}: {c['text']}")
    for m in d["mensajes"]:
        if m["author"] == "tu" and m["createdAt"] > desde:
            out.append(f"TABLÓN: {m['text']}")
    known = {t["id"] for t in d["tareas"]}
    for gone in set(estados) - known:
        out.append(f"TAREA BORRADA [{gone}]")
    print("\n".join(out) if out else "Sin novedades.")
    json.dump({"desde": now(), "estados": {t["id"]: t["status"] for t in d["tareas"]}},
              open(SEEN, "w", encoding="utf-8"))


def comentar(tid, texto):
    d = load()
    for t in d["tareas"]:
        if t["id"] == tid:
            t.setdefault("comentarios", []).append(
                {"id": "c-" + datetime.datetime.now().strftime("%H%M%S%f"), "author": "claude", "text": texto, "createdAt": now()})
            save(d)
            print("ok")
            return
    print("No existe la tarea", tid)


def mensaje(texto):
    d = load()
    d["mensajes"].append({"id": "m-" + datetime.datetime.now().strftime("%H%M%S%f"), "author": "claude", "text": texto, "createdAt": now()})
    save(d)
    print("ok")


def estado(tid, st):
    assert st in ("pendiente", "en_curso", "hecho")
    d = load()
    for t in d["tareas"]:
        if t["id"] == tid:
            t["status"] = st
            t["updatedAt"] = now()
            save(d)
            print("ok")
            return
    print("No existe la tarea", tid)


CLAVES_INFORME = ("seo", "mercado-manana", "mercado-tarde")


def informe(fecha, titulo, archivo, clave="seo"):
    assert clave in CLAVES_INFORME, f"clave debe ser una de {CLAVES_INFORME}"
    datetime.date.fromisoformat(fecha)
    with open(archivo, encoding="utf-8") as f:
        texto = f.read().strip()
    d = load()
    lista = [r for r in d.setdefault("informes", []) if not (r["fecha"] == fecha and r.get("clave", "seo") == clave)]
    lista.append({"fecha": fecha, "clave": clave, "titulo": titulo, "texto": texto, "createdAt": now()})
    d["informes"] = sorted(lista, key=lambda r: r["fecha"], reverse=True)
    save(d)
    print("ok")


def publicar():
    """Sube datos.json a GitHub para que la Sala web (GitHub Pages) se actualice. No bloquea."""
    import subprocess
    raiz = os.path.dirname(HERE)
    orden = ("git add web/datos.json && git commit -q -m \"Sala: actualización de Claude\" "
             "&& git pull -q --rebase --autostash && git push -q")
    subprocess.Popen(orden, cwd=raiz, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "novedades"
    hubo_web = cmd != "publicar" and sincronizar()
    if hubo_web or cmd in ("comentar", "mensaje", "estado", "informe", "publicar"):
        import atexit
        atexit.register(publicar)
    if cmd == "novedades":
        novedades()
    elif cmd == "comentar":
        comentar(sys.argv[2], sys.argv[3])
    elif cmd == "mensaje":
        mensaje(sys.argv[2])
    elif cmd == "estado":
        estado(sys.argv[2], sys.argv[3])
    elif cmd == "informe":
        informe(sys.argv[2], sys.argv[3], sys.argv[4], *(sys.argv[5:6]))
