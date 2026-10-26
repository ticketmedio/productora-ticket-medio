"""Shorts verticales del vídeo 9. OJO: en txt() y mano() el orden es (texto, y, tam, x)."""
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
"01": {"salida": "../../output/SHORT_01_la_ley_no_obliga.mp4", "escenas": [
  {"id": "a", "desde": "La ley no obliga a que la etiqueta", "fondo": "pasillo_marca_blanca", "zoom": [1.0, 1.08], "capas": [panel(640), cab("¿QUIÉN LA FABRICA?"), sello("LA ETIQUETA NO LO DICE", 560, 60, t=0.4), mano("La ley no obliga a ponerlo", 720, 50, t=1.0), masc("sorprendido", 880, 380, entra="der", t=0.2)]},
  {"id": "b", "desde": "El reglamento europeo", "fondo": "#F4E9D0", "capas": [cab("LO QUE SÍ PONE"), mano("Responsable: quien lo COMERCIALIZA", 500, 52, en="comercializa el alimento"), txt("Nombre y dirección\nde quien lo vende", 720, 66, en="nombre y la dirección"), txt("≠ quien lo fabrica", 940, 70, color=ROJO, en="no de quien lo fabrica"), masc("lupa", 900, 260, t=0.2)]}]},
"02": {"salida": "../../output/SHORT_02_el_ovalo.mp4", "escenas": [
  {"id": "a", "desde": "Hay un código en las etiquetas", "fondo": "fabrica_alimentos", "zoom": [1.0, 1.08], "capas": [panel(640), cab("EL ÓVALO"), {"tipo": "moneda", "texto": "ES", "r": 130, "x": 540, "y": 600, "color": "#FFFDF6", "t": 0.4}, mano("+ nº de autorización de la fábrica", 800, 48, en="número de autorización"), masc("lupa", 880, 360, entra="der", t=0.2)]},
  {"id": "b", "desde": "Esa marca está en el envase", "fondo": "#FFF3C4", "capas": [cab("PRODUCTOS DE ORIGEN ANIMAL"), mano("Carne · leche · queso · pescado", 520, 52, t=0.2), txt("Es la pista\nque sí tienes", 780, 80, color=ROJO, anim="pop", en="la pista que sí tienes"), masc("senala", 900, 280, t=0.2)]}]},
"03": {"salida": "../../output/SHORT_03_buscar_fabrica.mp4", "escenas": [
  {"id": "a", "desde": "Así se busca la fábrica", "fondo": "#E6E0F5", "capas": [cab("BUSCADOR DE LA AESAN"), mano("1 · Apunta el nº del óvalo", 480, 52, t=0.4), mano("2 · Búscalo en el registro público", 620, 50, en="Metes el número"), mano("3 → qué establecimiento es", 760, 52, en="qué empresa está inscrita"), sello("NO DICE PARA QUIÉN FABRICA", 960, 50, en="no para quién fabrica"), masc("encoge_hombros", 920, 250, t=0.2)]}]},
"04": {"salida": "../../output/SHORT_04_cuatro_gigantes.mp4", "escenas": [
  {"id": "a", "desde": "Cuatro proveedores de Mercadona", "fondo": "oficina_financiera", "zoom": [1.0, 1.08], "capas": [panel(640), cab("> 1.000 M€ CADA UNO"), cifra(4, 540, 190, color=ROJO, t=0.4), mano("proveedores de Mercadona (ventas 2024)", 700, 44, t=0.6), masc("sorprendido", 880, 380, entra="der", t=0.2)]},
  {"id": "b", "desde": "Cuatro de ellos superaron", "fondo": "#E3E7EC", "capas": [cab("LOS CUATRO"), rect(110, 460, 860, 100, AMAR, texto="Casa Tarradellas", tam=42, en="Casa Tarradellas", dur=0.7), rect(110, 590, 860, 100, AZUL, texto="Incarlopsa", tam=42, en="Incarlopsa", dur=0.7), rect(110, 720, 860, 100, VERDE, texto="J. García Carrión", tam=42, en="García Carrión", dur=0.7), rect(110, 850, 860, 100, GRIS, texto="Covap", tam=42, en="García Carrión", t=2.0, dur=0.7), masc("senala", 900, 220, t=0.2)]},
  {"id": "c", "desde": "Ojo con lo que significa", "fondo": "#FFF3C4", "capas": [cab("OJO"), mano("Proveedor de Mercadona ≠ fabricar\nsu marca blanca", 520, 50, en="no quiere decir"), mano("Y venden también a otros clientes", 800, 50, en="otros clientes"), masc("encoge_hombros", 900, 280, t=0.2)]}]},
"05": {"salida": "../../output/SHORT_05_cuatro_vs_tres.mp4", "escenas": [
  {"id": "a", "desde": "¿Gana más Mercadona", "fondo": "supermercado", "zoom": [1.0, 1.08], "capas": [panel(640), cab("¿QUIÉN GANA MÁS?"), mano("Beneficio por euro de ventas", 520, 48, t=0.4), rect(110, 600, 760, 100, AMAR, texto="Mercadona ≈ 4,1 c", tam=40, en="se quedó con unos cuatro", dur=0.8), rect(110, 740, 700, 100, AZUL, texto="20 proveedores ≈ 3 c", tam=38, en="unos tres céntimos", dur=0.8), masc("pensativo", 880, 320, entra="der", t=0.2)]},
  {"id": "b", "desde": "Es un cálculo nuestro", "fondo": "#F4E9D0", "capas": [cab("CON PRUDENCIA"), mano("360 M€ de beneficio / 12.000 M€ de ventas", 520, 46, t=0.3), mano("Cálculo propio: años distintos y ventas\nno solo a Mercadona", 760, 46, en="ejercicios distintos"), masc("lupa", 900, 280, t=0.2)]}]},
"06": {"salida": "../../output/SHORT_06_inversion_proveedores.mp4", "escenas": [
  {"id": "a", "desde": "¿Cuánto invierten los proveedores", "fondo": "fabrica_alimentos", "zoom": [1.0, 1.08], "capas": [panel(640), cab("INVERSIÓN 2025"), cifra(1700, 540, 160, sufijo=" M€", t=0.5), mano("de proveedores · 5.200 empleos (según Mercadona)", 700, 42, t=0.8), masc("contento", 880, 380, entra="der", t=0.2)]},
  {"id": "b", "desde": "El que más invirtió", "fondo": "#E3E7EC", "capas": [cab("LOS QUE MÁS INVIRTIERON"), rect(110, 460, 860, 100, AMAR, texto="Casa Tarradellas 117 M€", tam=38, en="Casa Tarradellas", dur=0.7), rect(110, 590, 600, 100, AZUL, texto="Vall Companys 70", tam=38, en="Vall Companys", dur=0.7), rect(110, 720, 520, 100, VERDE, texto="Avinatur 60", tam=38, en="Avinatur", dur=0.7), rect(110, 850, 520, 100, GRIS, texto="Incarlopsa 60", tam=38, en="Incarlopsa", t=1.2, dur=0.7), masc("senala", 900, 220, t=0.2)]}]},
"07": {"salida": "../../output/SHORT_07_dependencia_53_94.mp4", "escenas": [
  {"id": "a", "desde": "Aun así, hay un dato revelador", "fondo": "#E6E0F5", "capas": [cab("VENDEN A MERCADONA"), mano("Ventas ligadas a Mercadona, según\nalgunas empresas:", 480, 48, t=0.3), cifra(53, 700, 150, sufijo=" %", t=0.6), mano("hasta", 820, 50, t=0.8), cifra(94, 960, 150, sufijo=" %", color=ROJO, t=1.0), mano("(el diario no dice cuáles)", 1100, 44, t=3.0), masc("sorprendido", 900, 230, t=0.2)]}]},
}
for n, s in S.items():
    d = os.path.join(V, "shorts", f"short_{n}"); os.makedirs(d, exist_ok=True)
    json.dump({**BASE, **s}, open(os.path.join(d, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
