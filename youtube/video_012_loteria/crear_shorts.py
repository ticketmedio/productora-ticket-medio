"""Shorts verticales del vídeo 12. OJO: en txt() y mano() el orden es (texto, y, tam, x)."""
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
"01": {"salida": "../../output/SHORT_01_cuanto_queda_del_gordo.mp4", "escenas": [
  {"id": "a", "desde": "¿Cuánto te queda", "fondo": "administracion_loteria", "zoom": [1.0, 1.08], "capas": [panel(640), cab("EL GORDO"), cifra(400000, 540, 150, sufijo=" €", color=ROJO, en="cuatrocientos mil euros"), mano("por décimo (4 M€ por serie)", 700, 46, en="por décimo"), masc("pensativo", 880, 340, entra="der", t=0.2)]},
  {"id": "b", "desde": "Restas los cuarenta mil", "fondo": "#E3E7EC", "capas": [cab("HACIENDA RETIENE"), mano("400.000 − 40.000 = 360.000", 480, 48, en="trescientos sesenta mil"), rect(110, 600, 860, 100, ROJO, texto="Retención 20 %: 72.000 €", tam=40, en="setenta y dos mil", dur=0.8), rect(110, 730, 860, 100, VERDE, texto="Cobras: 328.000 €", tam=44, en="Cobras trescientos veintiocho", dur=0.8), masc("moneda", 960, 240, t=0.2)]},
  {"id": "c", "desde": "El segundo premio, ciento veinticinco", "fondo": "#F4E9D0", "capas": [cab("2.º Y 3.º PREMIO"), mano("125.000 € por décimo →\nretención 17.000 €", 520, 48, en="paga diecisiete mil"), mano("50.000 € por décimo →\nretención 2.000 €", 800, 48, en="paga dos mil"), sello("CÁLCULO PROPIO", 1000, 50, en="cálculo nuestro")]}]},
"02": {"salida": "../../output/SHORT_02_70_por_ciento_premios.mp4", "escenas": [
  {"id": "a", "desde": "¿Cuánto dinero reparte", "fondo": "administracion_loteria", "zoom": [1.0, 1.08], "capas": [panel(640), cab("SORTEO DE 2025"), cifra(198, 540, 170, sufijo=" series", en="ciento noventa y ocho series"), mano("de 100.000 números cada una", 700, 46, en="cien mil números"), masc("normal", 880, 340, entra="der", t=0.2)]},
  {"id": "b", "desde": "Cada décimo cuesta", "fondo": "#FFF3C4", "capas": [cab("LA EMISIÓN"), rect(110, 460, 760, 100, AMAR, texto="Décimo: 20 €", tam=44, en="Cada décimo cuesta"), rect(110, 590, 860, 100, ROJO, texto="Total: 3.960 M€", tam=44, en="tres mil novecientos sesenta"), masc("lupa", 920, 240, t=0.2)]},
  {"id": "c", "desde": "Según los datos publicados", "fondo": "#E3E7EC", "capas": [cab("70 % A PREMIOS"), cifra(2772, 560, 170, sufijo=" M€", color="#2E8B57", en="dos mil setecientos setenta y dos"), mano("según datos publicados del sorteo", 740, 42, t=0.6), masc("contento", 920, 240, t=0.2)]}]},
"03": {"salida": "../../output/SHORT_03_14_de_20.mp4", "escenas": [
  {"id": "a", "desde": "¿Cuánto devuelve", "fondo": "#FFF3C4", "capas": [cab("UN DÉCIMO DE 20 €"), cifra(14, 560, 220, sufijo=" €", color="#2E8B57", en="catorce euros por décimo"), mano("vuelven de media en premios", 740, 46, t=0.8), masc("pensativo", 920, 320, t=0.2)]},
  {"id": "b", "desde": "Ojo: es la media", "fondo": "#E3E7EC", "capas": [cab("OJO"), mano("Media de todos,\nantes de impuestos", 520, 52, en="antes de impuestos"), sello("CASI NADIE RECIBE 14 €", 800, 52, en="Casi nadie recibe catorce"), mano("pocos premios enormes + muchos pequeños", 960, 38, en="pocos premios enormes"), masc("encoge_hombros", 1060, 230, t=0.2)]}]},
"04": {"salida": "../../output/SHORT_04_40000_exentos.mp4", "escenas": [
  {"id": "a", "desde": "¿Paga impuestos", "fondo": "oficina_financiera", "zoom": [1.0, 1.08], "capas": [panel(640), cab("LEY 16/2012"), rect(110, 460, 860, 110, VERDE, texto="Hasta 40.000 €: exento", tam=44, en="cuarenta mil euros de cada décimo"), rect(110, 600, 860, 110, ROJO, texto="El exceso: retención 20 %", tam=42, en="retención del veinte por ciento"), masc("senala", 900, 330, entra="der", t=0.2)]},
  {"id": "b", "desde": "Lo dice la Agencia Tributaria", "fondo": "#E3E7EC", "capas": [cab("EJEMPLO OFICIAL"), mano("Premio de 100.000 €", 480, 52, en="cien mil euros"), mano("20 % de 60.000 =", 640, 48, en="veinte por ciento de sesenta mil"), cifra(12000, 800, 130, sufijo=" € retención", color=ROJO, en="doce mil euros"), mano("Cobras 88.000 €", 960, 52, en="ochenta y ocho mil"), masc("normal", 1060, 220, t=0.2)]}]},
"05": {"salida": "../../output/SHORT_05_reparto_premios.mp4", "escenas": [
  {"id": "a", "desde": "¿Cómo se reparte", "fondo": "administracion_loteria", "zoom": [1.0, 1.08], "capas": [panel(640), cab("EL GORDO"), cifra(400000, 540, 150, sufijo=" €", color=ROJO, en="cuatrocientos mil euros"), mano("probabilidad: 1 entre 100.000", 700, 46, en="una entre cien mil"), masc("moneda", 880, 340, entra="der", t=0.2)]},
  {"id": "b", "desde": "El segundo premio", "fondo": "#FFF3C4", "capas": [cab("LOS TRES GRANDES"), mano("2.º: 1.250.000 € por serie", 480, 46, en="un millón doscientos cincuenta mil"), mano("3.º: 500.000 € por serie", 600, 46, en="quinientos mil"), mano("Suman 1.138,5 M€", 760, 50, en="mil ciento treinta y ocho"), masc("lupa", 960, 230, t=0.2)]},
  {"id": "c", "desde": "Es el cuarenta y uno", "fondo": "#E3E7EC", "capas": [cab("DEL DINERO EN PREMIOS"), cifra(41, 560, 220, sufijo=" %", color=ROJO, en="cuarenta y uno por ciento"), mano("cálculo propio con cifras publicadas", 760, 42, en="cálculo nuestro"), masc("normal", 960, 240, t=0.2)]}]},
"06": {"salida": "../../output/SHORT_06_decimo_compartido.mp4", "escenas": [
  {"id": "a", "desde": "Si compartes un décimo", "fondo": "#FFF3C4", "capas": [cab("DÉCIMO COMPARTIDO"), txt("¿PAGAS MÁS\nSI TOCA?", 560, 80, color=ROJO, t=0.4), mano("La retención es por décimo", 820, 46, en="por separado"), masc("pensativo", 960, 280, t=0.2)]},
  {"id": "b", "desde": "Si un décimo es compartido", "fondo": "#E3E7EC", "capas": [cab("LOS 40.000 € EXENTOS"), mano("se reparten entre los dueños", 520, 50, en="se reparten entre los dueños"), sello("COMPARTIR NO TE HACE PAGAR MÁS", 800, 48, en="compartir no te hace pagar más"), masc("contento", 960, 260, t=0.2)]}]},
"07": {"salida": "../../output/SHORT_07_quien_gana_siempre.mp4", "escenas": [
  {"id": "a", "desde": "Lotería de Navidad: ¿quién gana", "fondo": "administracion_loteria", "zoom": [1.0, 1.08], "capas": [panel(640), cab("LOTERÍA DE NAVIDAD"), txt("¿QUIÉN GANA\nSIEMPRE?", 580, 90, color=ROJO, t=0.4), masc("pensativo", 880, 340, entra="der", t=0.2)]},
  {"id": "b", "desde": "De cada veinte euros", "fondo": "#F4E9D0", "capas": [cab("DE CADA 20 €"), rect(110, 460, 860, 110, VERDE, texto="14 € → premios", tam=48, en="catorce van a premios"), rect(110, 600, 860, 110, GRIS, texto="6 € → no son premios", tam=46, en="seis no"), mano("Y si toca algo grande,\nHacienda retiene su parte", 860, 44, en="Hacienda le retiene"), masc("encoge_hombros", 1060, 220, t=0.2)]}]},
}
for n, s in S.items():
    d = os.path.join(V, "shorts", f"short_{n}"); os.makedirs(d, exist_ok=True)
    json.dump({**BASE, **s}, open(os.path.join(d, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
