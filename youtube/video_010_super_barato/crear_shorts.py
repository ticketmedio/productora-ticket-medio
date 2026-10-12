"""Shorts verticales del vídeo 10. OJO: en txt() y mano() el orden es (texto, y, tam, x)."""
import json, os
V = os.path.dirname(os.path.abspath(__file__))
BASE = {"formato": "vertical", "fondos": "../../fondos", "musica": "../../audio/musica.mp3", "musica_db": -26, "cola": 1.5}
def cab(t): return {"tipo": "texto", "texto": t, "x": 540, "y": 220, "tam": 72, "papel": True, "t": -1, "dur": 0.01}
def panel(h=700): return {"tipo": "panel", "x": 60, "y": 360, "w": 960, "h": h}
def txt(c, y, tam=64, x=540, **k): return {"tipo": "texto", "texto": c, "x": x, "y": y, "tam": tam, **k}
def mano(c, y, tam=58, x=540, **k): return txt(c, y, tam, x, fuente="mano", **k)
def cifra(n, y, tam=150, x=540, **k): return {"tipo": "cifra", "hasta": n, "x": x, "y": y, "tam": tam, **k}
def masc(p, x=540, h=400, **k): return {"tipo": "mascota", "pose": p, "x": x, "y": 1310, "h": h, **k}
def rect(x, y, w, h, c, **k): return {"tipo": "rect", "x": x, "y": y, "w": w, "h": h, "color": c, **k}
def sello(c, y, tam=64, x=540, **k): return {"tipo": "sello", "texto": c, "x": x, "y": y, "tam": tam, **k}
AMAR, ROJO, AZUL, VERDE, GRIS = "#F5B301", "#E0521B", "#9CC5E8", "#8FD18F", "#D9D2C0"
S = {
"01": {"salida": "../../output/SHORT_01_1310_euros.mp4", "escenas": [
  {"id": "a", "desde": "Entre el supermercado más barato", "fondo": "pasillo_marca_blanca", "zoom": [1.0, 1.08], "capas": [panel(700), cab("AHORRO AL AÑO"), cifra(1310, 560, 190, sufijo=" €", color="#2E8B57", t=0.3), mano("de media entre el súper más barato\ny el más caro de tu ciudad", 700, 44, t=0.6), cifra(4381, 880, 150, sufijo=" €", color=ROJO, en="cuatro mil trescientos ochenta y uno"), mano("en Madrid", 1000, 50, en="en Madrid"), masc("sorprendido", 880, 330, entra="der", t=0.2)]},
  {"id": "b", "desde": "¿Y cuál es el más barato", "fondo": "#FFF3C4", "capas": [cab("¿CUÁL ES EL MÁS BARATO?"), txt("Depende de\ndónde vivas", 560, 90, color=ROJO, anim="pop", en="Depende de dónde vivas"), mano("Estudio OCU 2026 · 690 supermercados", 900, 44, t=1.0), masc("pensativo", 900, 300, t=0.2)]}]},
"02": {"salida": "../../output/SHORT_02_ranking_cadenas.mp4", "escenas": [
  {"id": "a", "desde": "Vamos con el ranking de cadenas", "fondo": "#E3E7EC", "capas": [cab("RANKING OCU 2026"), rect(110, 440, 500, 100, VERDE, texto="Dani 100", tam=40, en="Dani, con índice cien", dur=0.7), rect(110, 570, 620, 100, VERDE, texto="Family Cash · Tifer 102", tam=34, en="Family Cash y Tifer", dur=0.7), rect(110, 700, 680, 100, AMAR, texto="Alcampo · Supeco 103", tam=34, en="Alcampo y Supeco", dur=0.7), rect(110, 860, 860, 100, ROJO, texto="Sánchez Romero 176", tam=38, en="Sánchez Romero", dur=0.8), masc("senala", 920, 230, t=0.2)]},
  {"id": "b", "desde": "Y aquí viene lo curioso", "fondo": "centro_comercial", "zoom": [1.0, 1.08], "capas": [panel(640), cab("EL MÁS BARATO VISITADO"), txt("Un Alcampo en un centro\ncomercial de Aldaia", 600, 60, t=0.4), mano("(Valencia)", 790, 52, en="en Valencia"), masc("sorprendido", 880, 360, entra="der", t=0.2)]}]},
"03": {"salida": "../../output/SHORT_03_frescos_47.mp4", "escenas": [
  {"id": "a", "desde": "Según la OCU, los productos frescos", "fondo": "supermercado", "zoom": [1.0, 1.08], "capas": [panel(640), cab("FRESCOS"), cifra(4.7, 560, 190, prefijo="+", sufijo=" %", dec=1, color=ROJO, t=0.4), mano("en un año (OCU 2026)", 700, 50, t=0.6), masc("preocupado", 880, 360, entra="der", t=0.2)]},
  {"id": "b", "desde": "Los frescos suben un cuatro", "fondo": "#F4E9D0", "capas": [cab("¿QUÉ SUBE MÁS?"), rect(110, 480, 860, 100, ROJO, texto="Pescado +8,6 %", tam=42, en="un ocho coma seis", dur=0.8), rect(110, 620, 520, 100, AMAR, texto="Carne +3,7 %", tam=42, en="la carne, un tres coma siete", dur=0.8), rect(110, 760, 500, 100, AZUL, texto="Fruta y verdura +3,5 %", tam=34, en="un tres coma cinco", dur=0.8), masc("lupa", 920, 220, t=0.2)]}]},
"04": {"salida": "../../output/SHORT_04_marca_propia_baja.mp4", "escenas": [
  {"id": "a", "desde": "¿Dónde han bajado precios", "fondo": "#E6E0F5", "capas": [cab("CESTA ECONÓMICA"), txt("Mercadona −5,6 %", 520, 80, color="#2E8B57", en="Mercadona baja un cinco coma seis"), txt("Lidl −4,7 %", 700, 80, color="#2E8B57", en="Mercadona baja un cinco coma seis", t=1.0), mano("(los productos más baratos de cada tienda)", 880, 42, t=1.5), masc("riendo", 920, 250, t=0.2)]},
  {"id": "b", "desde": "En la cesta de marcas de fabricante", "fondo": "#FFF3C4", "capas": [cab("CESTA DE MARCAS"), txt("+2,5 %", 560, 170, color=ROJO, anim="pop", en="dos coma cinco"), mano("de media: la marca de fabricante sube", 800, 48, en="La marca de fabricante"), mano("Las cadenas compiten con productos\neconómicos y de marca propia", 980, 42, en="Es decir"), masc("pensativo", 920, 230, t=0.2)]}]},
"05": {"salida": "../../output/SHORT_05_desde_2021.mp4", "escenas": [
  {"id": "a", "desde": "Desde dos mil veintiuno", "fondo": "pasillo_marca_blanca", "zoom": [1.0, 1.08], "capas": [panel(640), cab("DESDE 2021"), cifra(40, 560, 190, prefijo="≈ +", sufijo=" %", color=ROJO, t=0.4), mano("sube la compra (Cesta OCU)", 700, 48, t=0.6), masc("sorprendido", 880, 360, entra="der", t=0.2)]},
  {"id": "b", "desde": "El café molido económico", "fondo": "#F4E9D0", "capas": [cab("LO QUE MÁS HA SUBIDO"), txt("Café molido +142 %", 520, 66, en="El café molido económico"), txt("Huevos M +135 %", 700, 66, en="Los huevos M"), mano("Solo bajan: detergente, yogur natural\ny bebida de arroz", 900, 44, en="Solo tres productos"), masc("preocupado", 920, 220, t=0.2)]}]},
"06": {"salida": "../../output/SHORT_06_ciudades.mp4", "escenas": [
  {"id": "a", "desde": "¿En qué ciudades españolas", "fondo": "#E3E7EC", "capas": [cab("PRECIOS POR LOCALIDAD"), rect(110, 440, 440, 100, VERDE, texto="Torrent 100", tam=40, en="Torrent", dur=0.7), rect(110, 580, 860, 100, ROJO, texto="Getxo · Pozuelo · Majadahonda 114", tam=34, en="Getxo", dur=0.8), rect(110, 720, 700, 100, AMAR, texto="Barcelona 110", tam=40, en="Barcelona, con ciento diez", dur=0.7), rect(110, 860, 660, 100, AMAR, texto="Bilbao · San Sebastián 109", tam=34, en="Bilbao y San Sebastián", dur=0.8), masc("senala", 920, 220, t=0.2)]}]},
"07": {"salida": "../../output/SHORT_07_indice_ocu.mp4", "escenas": [
  {"id": "a", "desde": "¿Cómo se comparan los precios", "fondo": "calle_comercial", "zoom": [1.0, 1.08], "capas": [panel(700), cab("ASÍ SE MIDIÓ"), cifra(690, 520, 130, t=0.3), mano("establecimientos · 38 ciudades", 630, 42, t=0.5), cifra(244, 800, 130, en="doscientos cuarenta y cuatro"), mano("productos (marcas y marcas blancas)", 910, 42, en="doscientos cuarenta y cuatro"), masc("lupa", 900, 320, entra="der", t=0.2)]},
  {"id": "b", "desde": "Con eso construye un índice", "fondo": "#F4E9D0", "capas": [cab("EL ÍNDICE"), txt("La más barata = 100", 520, 66, en="la tienda más barata vale cien"), txt("Índice 110 =\n10 % más cara", 760, 76, color=ROJO, en="índice ciento diez"), masc("normal", 900, 250, t=0.2)]}]},
}
for n, s in S.items():
    d = os.path.join(V, "shorts", f"short_{n}"); os.makedirs(d, exist_ok=True)
    json.dump({**BASE, **s}, open(os.path.join(d, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
