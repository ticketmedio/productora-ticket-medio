"""Shorts verticales del vídeo 8. OJO: en txt() y mano() el orden es (texto, y, tam, x)."""
import json, os
V = os.path.dirname(os.path.abspath(__file__))
BASE = {"formato": "vertical", "fondos": "../../fondos", "musica": "../../audio/musica.mp3", "musica_db": -26, "cola": 1.5}
def cab(t): return {"tipo": "texto", "texto": t, "x": 540, "y": 220, "tam": min(72, int(72 * 20 / max(len(t), 1))), "papel": True, "t": -1, "dur": 0.01}
def panel(h=700): return {"tipo": "panel", "x": 60, "y": 360, "w": 960, "h": h}
def txt(c, y, tam=64, x=540, **k): return {"tipo": "texto", "texto": c, "x": x, "y": y, "tam": tam, **k}
def mano(c, y, tam=58, x=540, **k): return txt(c, y, tam, x, fuente="mano", **k)
def cifra(n, y, tam=150, x=540, **k): return {"tipo": "cifra", "hasta": n, "x": x, "y": y, "tam": tam, **k}
def masc(p, x=540, h=400, **k): return {"tipo": "mascota", "pose": p, "x": x, "y": 1310, "h": h, **k}
def rect(x, y, w, h, c, **k): return {"tipo": "rect", "x": x, "y": y, "w": w, "h": h, "color": c, **k}
def sello(c, y, tam=64, x=540, **k): return {"tipo": "sello", "texto": c, "x": x, "y": y, "tam": tam, **k}
AMAR, ROJO, AZUL, VERDE, GRIS = "#F5B301", "#E0521B", "#9CC5E8", "#8FD18F", "#D9D2C0"
S = {
"01": {"salida": "../../output/SHORT_01_que_hace_amazon.mp4", "escenas": [
  {"id": "a", "desde": "¿Qué hace Amazon", "fondo": "almacen_devoluciones", "zoom": [1.0, 1.08], "capas": [panel(640), cab("TU DEVOLUCIÓN"), txt("¿QUÉ HACE AMAZON\nCON LO QUE DEVUELVES?", 580, 62, color=ROJO, t=0.4), mano("Esto dice la propia empresa", 800, 48, t=1.2), masc("pensativo", 900, 340, entra="der", t=0.2)]},
  {"id": "b", "desde": "Si está como nuevo", "fondo": "#E3E7EC", "capas": [cab("SEGÚN AMAZON"), mano("Inspección detallada de cada artículo", 480, 46, en="inspección detallada"), mano("Si está como nuevo →\nse vuelve a vender", 680, 52, en="Si está como nuevo"), sello("SIN CIFRA PÚBLICA", 920, 56, en="no hay una cifra pública"), masc("lupa", 1000, 240, t=0.2)]}]},
"02": {"salida": "../../output/SHORT_02_plazo_devolucion.mp4", "escenas": [
  {"id": "a", "desde": "¿Cuánto tiempo tienes", "fondo": "puerta_paquete", "zoom": [1.0, 1.08], "capas": [panel(640), cab("TU DERECHO"), cifra(14, 540, 200, sufijo=" días", color=ROJO, en="catorce días"), mano("naturales para devolver una compra online", 720, 44, en="catorce días"), masc("contento", 880, 340, entra="der", t=0.2)]},
  {"id": "b", "desde": "sin tener que explicar", "fondo": "#F4E9D0", "capas": [cab("SIN EXPLICAR POR QUÉ"), mano("Sin penalización", 520, 56, t=0.3), mano("Ojo: la política de cada tienda\npuede ser más generosa", 760, 46, en="Ojo"), masc("senala", 920, 260, t=0.2)]}]},
"03": {"salida": "../../output/SHORT_03_tus_obligaciones.mp4", "escenas": [
  {"id": "a", "desde": "Cuando devuelves una compra online", "fondo": "#FFF3C4", "capas": [cab("TUS OBLIGACIONES"), mano("Devolver el producto en\nmáximo 14 días", 520, 50, en="catorce días"), mano("Los costes de devolución\nsuelen ser tuyos", 780, 50, en="Los costes directos"), masc("normal", 940, 260, t=0.2)]},
  {"id": "b", "desde": "Solo respondes", "fondo": "#E3E7EC", "capas": [cab("TAMBIÉN"), mano("Respondes de la pérdida de valor\nsi lo manipulas de más", 500, 46, en="Solo respondes"), sello("GUARDA EL JUSTIFICANTE", 820, 56, en="guarda el justificante"), masc("encoge_hombros", 940, 250, t=0.2)]}]},
"04": {"salida": "../../output/SHORT_04_vendedores_liquidan.mp4", "escenas": [
  {"id": "a", "desde": "Los vendedores independientes", "fondo": "almacen_devoluciones", "zoom": [1.0, 1.08], "capas": [panel(700), cab("VENDEDORES DE AMAZON"), mano("Pueden liquidar lo devuelto", 520, 50, t=0.3), rect(110, 640, 860, 100, AMAR, texto="FBA Liquidations", tam=44, en="FBA Liquidations", dur=0.8), rect(110, 770, 860, 100, AZUL, texto="FBA Grade and Resell", tam=40, en="FBA Grade and Resell", dur=0.8), masc("normal", 960, 240, t=0.2)]},
  {"id": "b", "desde": "Es una de las vías", "fondo": "#F4E9D0", "capas": [cab("¿Y ESOS PALÉS?"), mano("Una vía para acabar\nen un lote de liquidación", 520, 50, t=0.3), sello("NO SABEMOS DE DÓNDE SALE CADA PALÉ", 840, 44, en="no podemos decirte"), masc("encoge_hombros", 980, 250, t=0.2)]}]},
"05": {"salida": "../../output/SHORT_05_investigacion_itv.mp4", "escenas": [
  {"id": "a", "desde": "¿Destruye Amazon", "fondo": "almacen_devoluciones", "zoom": [1.0, 1.08], "capas": [panel(640), cab("¿DESTRUYE AMAZON?"), cifra(124000, 540, 150, color=ROJO, en="ciento veinticuatro mil"), mano("objetivo registrado en una semana\n(Reino Unido, 2021, ITV News)", 720, 42, en="una semana de abril"), masc("sorprendido", 900, 330, entra="der", t=0.2)]},
  {"id": "b", "desde": "Amazon respondió", "fondo": "#E3E7EC", "capas": [cab("LA RESPUESTA"), mano("Prioridad: revender, donar o reciclar", 500, 46, en="su prioridad"), mano("Sin vertederos en el Reino Unido", 660, 46, en="no se envían"), sello("NO SE PUEDE APLICAR A ESPAÑA", 880, 46, en="no se puede aplicar"), masc("lupa", 1000, 240, t=0.2)]}]},
"06": {"salida": "../../output/SHORT_06_ley_residuos.mp4", "escenas": [
  {"id": "a", "desde": "¿Es legal destruir", "fondo": "#E6E0F5", "capas": [cab("LEY DE RESIDUOS 2022"), txt("¿ES LEGAL DESTRUIR\nLO NUEVO SIN VENDER?", 540, 62, color=ROJO, t=0.4), masc("pensativo", 900, 340, entra="der", t=0.2)]},
  {"id": "b", "desde": "En España, la ley de residuos", "fondo": "#FFF3C4", "capas": [cab("EN ESPAÑA"), mano("Prohíbe destruir o llevar a vertedero\nlos excedentes no perecederos", 500, 44, t=0.3), mano("Textiles, juguetes, aparatos eléctricos", 760, 44, en="como textiles"), mano("Primero reutilización o donación", 900, 46, en="Y deben ir primero"), masc("senala", 1020, 240, t=0.2)]}]},
"07": {"salida": "../../output/SHORT_07_ue_prohibe_destruir_ropa.mp4", "escenas": [
  {"id": "a", "desde": "La Unión Europea tiene", "fondo": "#E3E7EC", "capas": [cab("DESDE EL 19/7/2026"), txt("LA UE PROHÍBE DESTRUIR\nROPA Y CALZADO\nSIN VENDER", 560, 58, color=ROJO, t=0.4), mano("Reglamento de ecodiseño\n(grandes empresas)", 900, 44, en="Reglamento de ecodiseño"), masc("riendo", 1040, 240, t=0.2)]},
  {"id": "b", "desde": "Y deja excepciones", "fondo": "#F4E9D0", "capas": [cab("PERO HAY EXCEPCIONES"), mano("Daños que no se puedan reparar\nde forma rentable", 520, 48, t=0.3), mano("Incluidos los detectados\ntras una devolución", 780, 48, en="incluidos los detectados"), masc("encoge_hombros", 960, 250, t=0.2)]}]},
}
for n, s in S.items():
    d = os.path.join(V, "shorts", f"short_{n}"); os.makedirs(d, exist_ok=True)
    json.dump({**BASE, **s}, open(os.path.join(d, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
