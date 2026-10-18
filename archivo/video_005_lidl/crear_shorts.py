"""Genera escenas_v2.json (vertical) de los 7 Shorts de Lidl.
OJO: en txt() y mano() el orden es (texto, y, tam, x): la x va SIEMPRE con nombre."""
import json, os

V = os.path.dirname(os.path.abspath(__file__))
BASE = {"formato": "vertical", "fondos": "../../fondos", "musica": "../../audio/musica.mp3", "musica_db": -26, "cola": 1.5}

def cab(t): return {"tipo": "texto", "texto": t, "x": 540, "y": 220, "tam": 72, "papel": True, "t": -1, "dur": 0.01}
def panel(h=700): return {"tipo": "panel", "x": 60, "y": 360, "w": 960, "h": h}
def txt(c, y, tam=64, x=540, **k): return {"tipo": "texto", "texto": c, "x": x, "y": y, "tam": tam, **k}
def mano(c, y, tam=58, x=540, **k): return txt(c, y, tam, x, fuente="mano", **k)
def cifra(n, y, tam=150, x=540, **k): return {"tipo": "cifra", "hasta": n, "x": x, "y": y, "tam": tam, **k}
def masc(pose, x=540, h=400, **k): return {"tipo": "mascota", "pose": pose, "x": x, "y": 1310, "h": h, **k}
def rect(x, y, w, h, color, **k): return {"tipo": "rect", "x": x, "y": y, "w": w, "h": h, "color": color, **k}
def sello(c, y, tam=64, x=540, **k): return {"tipo": "sello", "texto": c, "x": x, "y": y, "tam": tam, **k}

LIDL = "Lidl España, comunicado del 30/9/2026"
shorts = {
 "01": {"salida": "../../output/SHORT_01_compra_mas_de_lo_que_vende.mp4", "escenas": [
   {"id": "a", "desde": "Lidl compra en España más de lo que vende", "fondo": "supermercado", "zoom": [1.0, 1.08], "capas": [
     panel(700), cab("¿COMPRA MÁS DE LO QUE VENDE?"),
     mano("VENDE en España", 480, 56, t=0.3),
     cifra(7641, 600, 140, sufijo=" M€", t=0.4),
     mano("COMPRA producto español", 800, 56, en="Compró producto español"),
     cifra(8400, 920, 140, sufijo=" M€", color="#E0521B", en="ocho mil cuatrocientos millones"),
     masc("sorprendido", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "Y de ese volumen", "fondo": "puerto_avion", "zoom": [1.0, 1.08], "capas": [
     panel(760), cab("¿COMPRA MÁS DE LO QUE VENDE?"),
     rect(110, 470, 860, 110, "#9CC5E8", texto="Compras: 8.400 M€", tam=48, t=0.2, dur=0.7),
     rect(110, 640, 440, 110, "#E0521B", texto="4.255 M€ fuera", tam=44, en="cuatro mil doscientos cincuenta y cinco", dur=0.8),
     rect(550, 640, 420, 110, "#F5B301", texto="4.145 M€ aquí*", tam=44, en="Más de la mitad", dur=0.8),
     mano("*cálculo propio: 8.400 − 4.255", 840, 38, en="Más de la mitad"),
     txt("Más de la mitad, a una treintena de países", 960, 50, papel=True, en="treintena de países europeos"),
     masc("senala", 880, 340, entra="der", t=0.2)]},
   {"id": "c", "desde": "España no es solo un mercado", "fondo": "#FFF3C4", "capas": [
     cab("¿COMPRA MÁS DE LO QUE VENDE?"),
     sello("ESPAÑA = LA DESPENSA DE LIDL EN EUROPA", 520, 56, t=0.2),
     mano("Compra en España\nmás de lo que vende en España", 800, 56, papel=True, en="la frase exacta"),
     mano("porque compra para media Europa", 1010, 50, en="porque compra para media Europa"),
     masc("pensativo", 880, 340, t=0.2)]},
 ]},
 "02": {"salida": "../../output/SHORT_02_3200_vs_8000.mp4", "escenas": [
   {"id": "a", "desde": "Lidl vende tres mil doscientos productos", "fondo": "supermercado", "zoom": [1.0, 1.08], "capas": [
     panel(700), cab("¿POCOS PRODUCTOS?"),
     cifra(3200, 540, 150, color="#E0521B", t=0.3), mano("referencias en Lidl", 660, 52, t=0.4),
     cifra(8000, 800, 150, color="#9A9A9A", en="ocho mil"), mano("en Mercadona", 920, 52, en="ocho mil"),
     masc("pensativo", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "Lidl tiene unas tres mil doscientas", "fondo": "#F4E9D0", "capas": [
     cab("¿POCOS PRODUCTOS?"),
     txt("> 80 %", 520, 170, color="#E0521B", anim="pop", en="ochenta por ciento"),
     mano("de su surtido es\nmarca propia", 720, 56, en="marca propia"),
     mano("(unas 3.200 referencias)", 900, 44, en="tres mil doscientas"),
     masc("senala", 880, 340, t=0.2)]},
   {"id": "c", "desde": "¿Por qué importa?", "fondo": "#E6E0F5", "capas": [
     cab("¿POR QUÉ LE SALE A CUENTA?"),
     mano("Sin duplicidades,\nsolo lo que más se pide…", 480, 56, en="eliminando duplicidades"),
     txt("más demanda\npor producto", 740, 66, en="junta más demanda"),
     txt("mejor precio\nde compra", 960, 66, color="#2E8B57", en="mejores precios"),
     sello("COMPRAS ENORMES", 1130, 60, en="cantidades enormes"),
     masc("normal", 880, 300, t=0.2)]},
 ]},
 "03": {"salida": "../../output/SHORT_03_ocu_18_a_60.mp4", "escenas": [
   {"id": "a", "desde": "Según la OCU", "fondo": "oficina_financiera", "zoom": [1.0, 1.08], "capas": [
     panel(700), cab("OCU 2026"),
     mano("Lidl, la más barata en…", 480, 54, t=0.2),
     cifra(18, 640, 170, color="#9A9A9A", en="hace un año"), mano("localidades, el año pasado", 790, 44, en="hace un año"),
     cifra(60, 940, 190, color="#E0521B", en="Hoy, en sesenta"), mano("localidades, este año", 1090, 44, en="Hoy, en sesenta"),
     masc("sorprendido", 880, 340, entra="der", t=0.2)]},
   {"id": "b", "desde": "Y ojo con el método", "fondo": "#F4E9D0", "capas": [
     cab("EL MÉTODO DE LA OCU"),
     txt("690 tiendas", 480, 90, en="seiscientos noventa establecimientos"),
     txt("38 ciudades", 640, 90, en="treinta y ocho ciudades"),
     txt("244 productos", 800, 90, en="doscientos cuarenta y cuatro productos"),
     masc("lupa", 880, 340, t=0.2)]},
   {"id": "c", "desde": "Entre el súper más barato", "fondo": "#E3E7EC", "capas": [
     cab("EL AHORRO MEDIO"),
     mano("Entre el súper más barato\ny el más caro de tu ciudad", 470, 54, t=0.2),
     cifra(1310, 760, 190, sufijo=" €", color="#2E8B57", en="mil trescientos diez euros"),
     mano("al año", 930, 60, en="al año"),
     masc("moneda", 880, 320, t=0.2)]},
 ]},
 "04": {"salida": "../../output/SHORT_04_cuota_2_a_7.mp4", "escenas": [
   {"id": "a", "desde": "Según Kantar, Lidl ha pasado", "fondo": "calle_comercial", "zoom": [1.0, 1.08], "capas": [
     panel(700), cab("LA CUOTA DE LIDL"),
     txt("2,3 %", 560, 150, en="dos coma tres"), mano("hace 20 años", 690, 46, en="dos coma tres"),
     txt("7,3 %", 860, 170, color="#E0521B", anim="pop", en="más del siete"), mano("hoy (Kantar)", 1000, 46, en="más del siete"),
     masc("riendo", 880, 340, entra="der", t=0.2)]},
   {"id": "b", "desde": "de cada cien euros", "fondo": "#FFF3C4", "capas": [
     cab("¿QUIÉN SE LLEVA TU GASTO?"),
     mano("De cada 100 € en el súper:", 440, 52, t=0.2),
     rect(110, 540, 780, 110, "#F5B301", texto="27 € · Mercadona", tam=48, en="veintisiete van a Mercadona", dur=0.8),
     rect(110, 700, 210, 110, "#E0521B", texto="7 € · Lidl", tam=40, en="siete a Lidl", dur=0.8),
     txt("Lidl, la que más sube: +0,5 puntos", 940, 54, color="#E0521B", en="la que más sube"),
     masc("senala", 880, 320, t=0.2)]},
   {"id": "c", "desde": "Para que te hagas una idea", "fondo": "#E3E7EC", "capas": [
     cab("LA CUOTA DE LIDL"),
     txt("2006 · 2,3 %", 480, 80, en="hace veinte años"),
     txt("2020 · 4,8 %", 640, 80, en="En dos mil veinte"),
     txt("2026 · 7,3 %", 820, 100, color="#E0521B", anim="pop", en="el siete coma tres"),
     mano("Fuente: Kantar", 990, 42, t=1.0),
     masc("contento", 880, 320, t=0.2)]},
 ]},
 "05": {"salida": "../../output/SHORT_05_3_6_centimos.mp4", "escenas": [
   {"id": "a", "desde": "Lidl ingresa unos doscientos", "fondo": "supermercado", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("¿CUÁNTO GANA?"),
     txt("≈ 242 €", 540, 150, color="#2E8B57", anim="pop", t=0.3), mano("cada segundo", 660, 54, t=0.4),
     txt("¿Y cuánto se queda?", 860, 66, en="¿Cuánto gana de cada euro?"),
     masc("pensativo", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "De cada euro que gastas en Lidl", "fondo": "#F4E9D0", "capas": [
     cab("¿CUÁNTO GANA?"),
     {"tipo": "moneda", "texto": "1 €", "r": 120, "x": 300, "y": 600, "color": "#F5B301", "t": 0.2},
     txt("→", 600, 100, x=540, en="la empresa se queda"),
     {"tipo": "moneda", "texto": "3,6 c", "r": 100, "x": 780, "y": 600, "color": "#E0521B", "en": "tres céntimos y medio"},
     mano("beneficio: 274 millones", 860, 54, en="doscientos setenta y cuatro millones"),
     masc("moneda", 880, 340, t=0.2)]},
   {"id": "c", "desde": "Para ponerlo en perspectiva", "fondo": "#E3E7EC", "capas": [
     cab("LIDL vs MERCADONA"),
     mano("Beneficio por euro", 440, 52, t=0.2),
     rect(110, 520, 800, 110, "#F5B301", texto="Mercadona ≈ 4,1 c", tam=46, en="cuatro céntimos por euro", dur=0.8),
     rect(110, 680, 700, 110, "#E0521B", texto="Lidl ≈ 3,6 c", tam=46, en="cuatro céntimos por euro", dur=0.8, t=1.4),
     txt("Pero Mercadona vende 5,5 veces más", 900, 52, color="#E0521B", en="más de cinco veces más"),
     masc("lupa", 880, 300, t=0.2)]},
 ]},
 "06": {"salida": "../../output/SHORT_06_palets_logistica.mp4", "escenas": [
   {"id": "a", "desde": "Lidl expone sus productos", "fondo": "supermercado", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("¿POR QUÉ EN PALÉS?"),
     sello("PRODUCTOS EN PALÉS", 540, 66, t=0.3),
     mano("Es literal: está en su web", 720, 52, en="Es literal"),
     masc("senala", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "La idea: ahorrar", "fondo": "#FFF3C4", "capas": [
     cab("¿POR QUÉ EN PALÉS?"),
     mano("Los artículos de mayor rotación,\ndirectamente en palés", 470, 52, en="mayor rotación"),
     txt("Ahorra lo que\nel cliente no nota", 760, 70, color="#E0521B", anim="pop", en="ahorrar todo lo que el cliente no nota"),
     masc("pensativo", 880, 320, t=0.2)]},
   {"id": "c", "desde": "Y detrás, una logística", "fondo": "centro_logistico", "zoom": [1.0, 1.08], "capas": [
     panel(760), cab("LA LOGÍSTICA"),
     cifra(14, 520, 130, en="catorce plataformas"), mano("plataformas", 620, 46, en="catorce plataformas"),
     cifra(140, 760, 130, sufijo=" M€", en="ciento cuarenta millones"), mano("invertidos en Martorell", 860, 46, en="Martorell"),
     cifra(130, 1000, 130, prefijo="+", en="más de ciento treinta tiendas"), mano("tiendas servidas", 1100, 46, en="más de ciento treinta tiendas"),
     masc("normal", 880, 260, t=0.2)]},
 ]},
 "07": {"salida": "../../output/SHORT_07_fruta_81.mp4", "escenas": [
   {"id": "a", "desde": "Lidl compra en España dos millones", "fondo": "#E8F3E0", "capas": [
     cab("FRUTA Y VERDURA"),
     cifra(2, 520, 190, prefijo="+", sufijo=" M t", t=0.3), mano("compradas en España", 650, 52, t=0.4),
     cifra(81, 860, 190, sufijo=" %", color="#E0521B", en="el ochenta y uno"), mano("se va fuera", 990, 52, en="se va fuera"),
     masc("carrito", 880, 340, entra="der", t=0.2)]},
   {"id": "b", "desde": "El ochenta y un por ciento", "fondo": "puerto_avion", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("FRUTA Y VERDURA"),
     txt("81 % a otros mercados europeos", 520, 60, en="otros mercados europeos"),
     mano("Previsión de compras en 2026", 700, 50, en="para este año"),
     cifra(9400, 840, 140, sufijo=" M€", color="#E0521B", en="nueve mil cuatrocientos millones"),
     masc("senala", 880, 360, entra="der", t=0.2)]},
 ]},
}
for n, s in shorts.items():
    d = os.path.join(V, "shorts", f"short_{n}")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "escenas_v2.json"), "w", encoding="utf-8") as f:
        json.dump({**BASE, **s}, f, ensure_ascii=False, indent=1)
print("ok")
