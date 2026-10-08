"""Genera escenas_v2.json (vertical) de los 3 Shorts de Zara."""
import json, os

V = os.path.dirname(os.path.abspath(__file__))
CAMISETA = "file:///" + os.path.join(V, "assets", "camiseta.svg").replace("\\", "/")
BASE = {"formato": "vertical", "fondos": "../../fondos", "musica": "../../audio/musica.mp3", "musica_db": -26, "cola": 1.5}

def cab(t): return {"tipo": "texto", "texto": t, "x": 540, "y": 220, "tam": 72, "papel": True, "t": -1, "dur": 0.01}
def panel(h=700): return {"tipo": "panel", "x": 60, "y": 360, "w": 960, "h": h}
def txt(c, y, tam=64, x=540, **k): return {"tipo": "texto", "texto": c, "x": x, "y": y, "tam": tam, **k}
def mano(c, y, tam=58, x=540, **k): return txt(c, y, tam, x, fuente="mano", **k)
def masc(pose, x=540, h=400, **k): return {"tipo": "mascota", "pose": pose, "x": x, "y": 1310, "h": h, **k}
def rect(x, y, w, h, color, **k): return {"tipo": "rect", "x": x, "y": y, "w": w, "h": h, "color": color, **k}
def sello(c, y, tam=64, x=540, **k): return {"tipo": "sello", "texto": c, "x": x, "y": y, "tam": tam, **k}

shorts = {
 "01": {"salida": "../../output/SHORT_01_9_millones_al_dia.mp4", "escenas": [
   {"id": "a", "desde": "Hay un señor de A Coruña", "fondo": "calle_comercial", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("¿9 MILLONES AL DÍA?"),
     mano("Un señor de A Coruña…", 500, 70, t=0),
     txt("≈ 9 M€\nal día", 780, 120, color="#E0521B", anim="pop", en="nueve millones"),
     masc("sorprendido", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "¿Y adónde van esos trece", "fondo": "#FFF3C4", "capas": [
     cab("¿9 MILLONES AL DÍA?"),
     mano("De cada € que pagas en Zara,\n13 c son beneficio", 420, 56, papel=True, t=0.1),
     {"tipo": "tarta", "x": 540, "y": 760, "r": 220, "t": 0.2, "porciones": [
       {"v": 52, "color": "#E0521B", "en": "casi siete céntimos"},
       {"v": 35, "color": "#F5B301", "en": "Casi once se reparten"},
       {"v": 13, "color": "#D9D2C0", "en": "Casi once se reparten"}]},
     txt("≈ 7 c · Amancio Ortega", 1060, 58, color="#E0521B", en="casi siete céntimos"),
     mano("≈ 4 c · otros accionistas · ≈ 2 c · la empresa", 1150, 44, en="Casi once se reparten")]},
   {"id": "c", "desde": "Este año cobrará", "fondo": "#F4E9D0", "capas": [
     cab("¿9 MILLONES AL DÍA?"),
     {"tipo": "cifra", "hasta": 3200, "prefijo": "≈ ", "sufijo": " M€", "x": 540, "y": 520, "tam": 150, "color": "#E0521B", "t": 0.1},
     mano("en dividendos de Inditex, este año", 660, 54),
     txt("≈ 9 M€ al día", 830, 110, anim="pop", en="Casi nueve millones"),
     masc("sorprendido", 540, 360, entra="abajo", t=0.2)]},
 ]},
 "02": {"salida": "../../output/SHORT_02_zara_casi_no_malvende.mp4", "escenas": [
   {"id": "a", "desde": "El gran secreto de Zara", "fondo": "tienda_ropa", "zoom": [1.0, 1.08], "capas": [
     panel(560), cab("EL SECRETO DE ZARA"),
     txt("Casi nunca\nmalvende", 620, 110, color="#E0521B", anim="pop", t=0),
     masc("lupa", 540, 400, entra="abajo", t=0.1)]},
   {"id": "b", "desde": "En 2024, la ropa", "fondo": "#F4E9D0", "capas": [
     cab("EL SECRETO DE ZARA"),
     {"tipo": "cifra", "hasta": 0.57, "dec": 2, "sufijo": " %", "x": 540, "y": 500, "tam": 190, "color": "#E0521B", "t": 0.1},
     mano("de ropa sin vender (2024)", 640, 58),
     txt("< 1 prenda de cada 170", 790, 66, papel=True, en="Menos de una prenda"),
     txt("Margen: 58,3 %", 960, 76, en="cincuenta y ocho"),
     masc("contento", 880, 320, t=0.2)]},
   {"id": "c", "desde": "La segunda pieza es cómo fabrica", "fondo": "taller_costura", "zoom": [1.04, 1.1], "capas": [
     panel(720), cab("EL SECRETO DE ZARA"),
     mano("Fabrica cerca:", 440, 60, t=0.1),
     txt("España · Portugal\nMarruecos · Turquía", 580, 62, en="en Portugal"),
     txt("Tandas cortas", 760, 84, color="#E0521B", anim="pop", en="tandas cortas"),
     mano("¿Se vende? → se repone", 890, 56, en="Si algo se vende"),
     mano("¿No? → se deja de fabricar", 990, 56, en="se deja de fabricar"),
     masc("lupa", 880, 300, t=0.2)]},
 ]},
 "03": {"salida": "../../output/SHORT_03_hacienda_gana_mas.mp4", "escenas": [
   {"id": "a", "desde": "¿Quién gana más con tu ropa", "fondo": "#E3E7EC", "capas": [
     cab("¿QUIÉN GANA MÁS?"),
     {"tipo": "imagen", "src": CAMISETA, "x": 540, "y": 640, "h": 480, "t": 0},
     txt("25,95 €", 640 + 130 * 480 / 620, 24, x=540 + 205 * 480 / 620, color="#E0521B", t=0.2),
     txt("Parada 1: Hacienda", 980, 70, papel=True, t=2.2),
     masc("pensativo", 880, 300, t=0.2)]},
   {"id": "b", "desde": "En España, la ropa paga", "fondo": "#E3E7EC", "capas": [
     cab("¿QUIÉN GANA MÁS?"),
     txt("IVA de la ropa: 21 %", 460, 72, en="veintiuno por ciento"),
     {"tipo": "moneda", "texto": "17 c", "r": 130, "x": 540, "y": 720, "color": "#9CC5E8", "en": "unos diecisiete céntimos"},
     mano("de cada euro, directos al Estado", 940, 56, en="Van directos"),
     masc("encoge_hombros", 880, 300, t=0.2)]},
   {"id": "c", "desde": "Sexta parada: Hacienda", "fondo": "#E3E7EC", "capas": [
     cab("¿QUIÉN GANA MÁS?"),
     mano("Y luego, el impuesto\nsobre el beneficio:", 440, 58, t=0.1),
     txt("≈ 4 c", 600, 110, en="Casi cuatro"),
     txt("IVA + impuesto\n≈ 21 c", 790, 90, color="#E0521B", en="unos veintiún"),
     {"tipo": "sello", "texto": "MÁS QUE ZARA (13 c)", "x": 540, "y": 1010, "tam": 62, "en": "Más de lo que gana"},
     masc("enfadado", 880, 280, t=0.2)]},
 ]},
 "04": {"salida": "../../output/SHORT_04_dos_semanas.mp4", "escenas": [
   {"id": "a", "desde": "¿Es verdad que Zara tiene una prenda", "fondo": "estudio_diseno", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("¿EN 2 SEMANAS?"),
     mano("Una prenda nueva en tienda…", 520, 56, t=0.3),
     masc("pensativo", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "Es verdad a medias", "fondo": "#F4E9D0", "capas": [
     cab("¿EN 2 SEMANAS?"),
     sello("VERDAD A MEDIAS", 450, 70, t=0.1),
     mano("Estudio de Harvard, 2003", 680, 56, en="Universidad de Harvard"),
     txt("Reponer o retocar:\n2 semanas", 900, 64, color="#E0521B", en="reponer o retocar prendas"),
     masc("encoge_hombros", 880, 300, t=0.2)]},
   {"id": "c", "desde": "Un diseño totalmente nuevo tardaba", "fondo": "#E3E7EC", "capas": [
     cab("¿EN 2 SEMANAS?"),
     txt("Un diseño nuevo", 460, 80, t=0.1),
     txt("4–5 semanas", 680, 130, color="#E0521B", anim="pop", en="entre cuatro y cinco semanas"),
     mano("para la época, rapidísimo", 900, 56, en="rapidísimo"),
     masc("contento", 880, 300, t=0.2)]},
 ]},
 "05": {"salida": "../../output/SHORT_05_fabricas.mp4", "escenas": [
   {"id": "a", "desde": "¿Quién fabrica de verdad", "fondo": "taller_costura", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("¿QUIÉN LA FABRICA?"),
     mano("La ropa de Zara…", 520, 60, t=0.3),
     masc("pensativo", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "Inditex trabaja con seis mil", "fondo": "#E6E0F5", "capas": [
     cab("¿QUIÉN LA FABRICA?"),
     {"tipo": "cifra", "hasta": 6684, "x": 540, "y": 560, "tam": 150, "color": "#E0521B", "en": "seis mil seiscientas ochenta y cuatro"},
     mano("fábricas en 49 países", 700, 58, en="cuarenta y nueve países"),
     txt("+ 3 millones de personas", 880, 60, en="tres millones de personas"),
     masc("sorprendido", 880, 300, t=0.2)]},
   {"id": "c", "desde": "Y casi ninguna es suya", "fondo": "#F4E9D0", "capas": [
     cab("¿QUIÉN LA FABRICA?"),
     sello("CASI NINGUNA ES SUYA", 470, 66, t=0.1),
     mano("Solo unas pocas, cerca de\nArteixo, son del grupo", 700, 52, en="Solo unas pocas"),
     mano("El resto, proveedores", 920, 58, en="El resto son proveedores"),
     masc("encoge_hombros", 880, 300, t=0.2)]},
   {"id": "d", "desde": "Y seis de cada diez", "fondo": "#E3E7EC", "capas": [
     cab("¿QUIÉN LA FABRICA?"),
     txt("6 de cada 10", 520, 120, color="#E0521B", anim="pop", t=0.2),
     mano("están en Asia", 720, 66, t=0.6),
     masc("pensativo", 880, 320, t=0.2)]},
 ]},
 "06": {"salida": "../../output/SHORT_06_precios.mp4", "escenas": [
   {"id": "a", "desde": "¿Cuánto ha subido Zara sus precios", "fondo": "tienda_ropa", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("¿MÁS CARA?"),
     mano("Precios de Zara en Europa", 520, 56, t=0.3),
     masc("preocupado", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "Según un análisis de Bloomberg", "fondo": "#FFF3C4", "capas": [
     cab("¿MÁS CARA?"),
     mano("Análisis de Bloomberg", 440, 56, t=0.1),
     mano("En Europa, de media, desde 2020", 600, 54, en="Zara ha subido sus precios"),
     txt("+22 %", 840, 190, color="#E0521B", anim="pop", en="un veintidós por ciento"),
     masc("sorprendido", 880, 300, t=0.2)]},
   {"id": "c", "desde": "Y su margen, en ese tiempo", "fondo": "#E3E7EC", "capas": [
     cab("¿MÁS CARA?"),
     txt("Y su margen", 450, 80, t=0.1),
     txt("no ha dejado de crecer", 650, 66, en="no ha dejado de crecer"),
     sello("MARGEN ↑", 900, 80, en="no ha dejado de crecer"),
     masc("encoge_hombros", 880, 300, t=0.2)]},
 ]},
 "07": {"salida": "../../output/SHORT_07_shein.mp4", "escenas": [
   {"id": "a", "desde": "¿Por qué Shein vende casi lo mismo", "fondo": "calle_comercial", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("ZARA VS SHEIN"),
     mano("Casi las mismas ventas…", 520, 58, t=0.3),
     masc("sorprendido", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "En 2025 vendió casi lo mismo", "fondo": "#F4E9D0", "capas": [
     cab("ZARA VS SHEIN"),
     txt("Ventas 2025: casi iguales", 450, 62, t=0.1),
     rect(110, 600, 860, 110, "#F5B301", texto="Inditex (Zara)", tam=46, t=0.3, dur=0.8),
     rect(110, 750, 830, 110, "#9CC5E8", texto="Shein", tam=46, t=0.7, dur=0.8),
     masc("pensativo", 880, 300, t=0.2)]},
   {"id": "c", "desde": "Pero ganó unas tres veces menos", "fondo": "#E3E7EC", "capas": [
     cab("ZARA VS SHEIN"),
     txt("Beneficio", 450, 76, t=0.1),
     rect(110, 560, 860, 110, "#F5B301", texto="Inditex (Zara)", tam=46, t=0.2, dur=0.7),
     rect(110, 710, 290, 110, "#9CC5E8", texto="Shein ÷ 3", tam=38, t=0.9, dur=0.7),
     masc("preocupado", 880, 300, t=0.2)]},
   {"id": "d", "desde": "Vender barato es fácil", "fondo": "#FFF3C4", "capas": [
     cab("ZARA VS SHEIN"),
     txt("Vender barato: fácil", 520, 76, t=0.2),
     txt("Ganar dinero: no tanto", 720, 76, color="#E0521B", en="Ganar dinero vendiendo barato"),
     masc("pensativo", 880, 320, t=0.2)]},
 ]},
}
for n, s in shorts.items():
    d = os.path.join(V, "shorts", f"short_{n}")
    json.dump({**BASE, **s}, open(os.path.join(d, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
