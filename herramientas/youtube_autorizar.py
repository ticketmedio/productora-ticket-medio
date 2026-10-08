"""Autoriza UNA VEZ el acceso de solo lectura a las estadísticas de nuestro canal de YouTube (API oficial).

Uso: doble clic en AUTORIZAR_YOUTUBE.bat (en la carpeta del proyecto), con YT_CLIENT_ID y YT_CLIENT_SECRET ya puestos
en config/claves.txt (los da Google Cloud Console al crear el «ID de cliente de OAuth» de tipo aplicación de escritorio).

Qué hace: abre el navegador para que el usuario elija el canal y pulse «Permitir», recibe el código en este mismo
ordenador (127.0.0.1), lo cambia por un «refresh token» y lo guarda en:
  - config/youtube_token.txt           (para usar la API desde este PC)
  - config/YOUTUBE_PARA_LA_NUBE.txt    (las 3 variables que hay que pegar en el entorno de la nube de Claude; borrar después)
Esos archivos están en config/, que NUNCA se sube a GitHub. No se imprime ningún secreto en pantalla.
"""
import http.server, json, os, sys, threading, urllib.parse, urllib.request, webbrowser

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUERTO = 8765
ALCANCES = "https://www.googleapis.com/auth/yt-analytics.readonly https://www.googleapis.com/auth/youtube.readonly"


def claves():
    d = {}
    ruta = os.path.join(RAIZ, "config", "claves.txt")
    for linea in open(ruta, encoding="utf-8"):
        if ":" in linea:
            k, v = linea.split(":", 1)
            d[k.strip()] = v.strip()
    return d


c = claves()
cid, secreto = c.get("YT_CLIENT_ID", ""), c.get("YT_CLIENT_SECRET", "")
if not cid or not secreto:
    sys.exit("Faltan YT_CLIENT_ID y YT_CLIENT_SECRET en config/claves.txt. Sigue los pasos de la tarea de la Sala.")

redirect = f"http://127.0.0.1:{PUERTO}"
resultado = {}


class Manejador(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        resultado["code"] = (q.get("code") or [""])[0]
        resultado["error"] = (q.get("error") or [""])[0]
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h2>Listo. Ya puedes cerrar esta pestaña y volver a la ventana negra.</h2>".encode("utf-8"))

    def log_message(self, *a):
        pass


servidor = http.server.HTTPServer(("127.0.0.1", PUERTO), Manejador)
hilo = threading.Thread(target=servidor.handle_request)
hilo.start()
url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
    "client_id": cid, "redirect_uri": redirect, "response_type": "code", "scope": ALCANCES,
    "access_type": "offline", "prompt": "consent"})
print("Se abre el navegador. Elige el canal «Ticket Medio» y pulsa Permitir.")
print("Si Google avisa de «aplicación no verificada»: Configuración avanzada → Ir a la aplicación (es la tuya).")
webbrowser.open(url)
hilo.join(timeout=300)
servidor.server_close()
if not resultado.get("code"):
    sys.exit("No se recibió la autorización" + (f" ({resultado.get('error')})" if resultado.get("error") else " a tiempo") + ". Vuelve a intentarlo.")

cuerpo = urllib.parse.urlencode({"code": resultado["code"], "client_id": cid, "client_secret": secreto,
                                 "redirect_uri": redirect, "grant_type": "authorization_code"}).encode()
try:
    tokens = json.loads(urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=cuerpo), timeout=30).read())
except Exception as e:
    sys.exit(f"Google no aceptó el código: {e}")
refresco = tokens.get("refresh_token")
if not refresco:
    sys.exit("Google no devolvió el permiso de larga duración. Vuelve a ejecutar AUTORIZAR_YOUTUBE.bat y pulsa Permitir en todo.")

os.makedirs(os.path.join(RAIZ, "config"), exist_ok=True)
open(os.path.join(RAIZ, "config", "youtube_token.txt"), "w", encoding="utf-8").write(f"YT_REFRESH_TOKEN: {refresco}\n")
open(os.path.join(RAIZ, "config", "YOUTUBE_PARA_LA_NUBE.txt"), "w", encoding="utf-8").write(
    f"YT_CLIENT_ID={cid}\nYT_CLIENT_SECRET={secreto}\nYT_REFRESH_TOKEN={refresco}\n")
print("\nHecho. Se han guardado los permisos en la carpeta config (privada).")
print("Siguiente paso: abre config\\YOUTUBE_PARA_LA_NUBE.txt, copia las 3 líneas y pégalas en las variables de entorno de la nube (paso 9 de la tarea).")
