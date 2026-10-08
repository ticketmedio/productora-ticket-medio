"""Ejecuta, uno detrás de otro, los trabajos pesados de render del proyecto.
Lee privado/cola_trabajos.txt (una orden de shell por línea; «#» = comentario; «ESPERAR archivo|texto» espera a que el archivo contenga ese texto).
Guarda cuántas líneas ha hecho en privado/cola_trabajos.hecho y se queda esperando líneas nuevas. Uso: python3 herramientas/orquestador.py"""
import os, subprocess, time
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = os.path.join(RAIZ, "privado", "cola_trabajos.txt"); H = F.replace(".txt", ".hecho"); LOG = os.path.join(RAIZ, "privado", "cola_trabajos.log")
os.makedirs(os.path.dirname(F), exist_ok=True); open(F, "a").close()
env = dict(os.environ, PATH=os.path.expanduser("~/.local/bin") + ":" + os.environ.get("PATH", ""))
def hechos(): return int(open(H).read() or 0) if os.path.exists(H) else 0
while True:
    lineas = open(F, encoding="utf-8").read().splitlines(); n = hechos()
    if n >= len(lineas):
        time.sleep(30); continue
    l = lineas[n].strip()
    if l and not l.startswith("#"):
        ini = time.strftime("%H:%M:%S")
        if l.startswith("ESPERAR "):
            arch, texto = l[8:].split("|", 1)
            while not (os.path.exists(arch) and texto in open(arch, encoding="utf-8", errors="ignore").read()):
                time.sleep(20)
            r = 0
        else:
            r = subprocess.run(["nice", "-n", "5", "bash", "-c", l], cwd=RAIZ, env=env, stdout=open(LOG, "a"), stderr=subprocess.STDOUT).returncode
        open(LOG, "a").write(f"[{ini} → {time.strftime('%H:%M:%S')}] rc={r} :: {l[:150]}\n")
    open(H, "w").write(str(n + 1))
