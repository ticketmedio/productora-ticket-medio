"""Shorts verticales del vídeo 11. OJO: en txt() y mano() el orden es (texto, y, tam, x)."""
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
"01": {"salida": "../../output/SHORT_01_cepsa_ya_no_es_cepsa.mp4", "escenas": [
  {"id": "a", "desde": "El treinta de octubre", "fondo": "centro_logistico", "zoom": [1.0, 1.08], "capas": [panel(640), cab("30/10/2024"), txt("CEPSA → MOEVE", 560, 90, color=ROJO, anim="pop", t=0.4), sello("¿NOS ESTÁN ENGAÑANDO?", 760, 54, t=1.2), masc("pensativo", 880, 360, entra="der", t=0.2)]},
  {"id": "b", "desde": "¿Ha cambiado de dueño", "fondo": "#E3E7EC", "capas": [cab("¿HA CAMBIADO DE DUEÑO?"), mano("No hay ningún dato que lo indique:\nes la misma sociedad", 520, 50, en="No hay ningún dato"), rect(110, 760, 800, 100, AMAR, texto="Mubadala > 61 %", tam=40, en="Mubadala, con algo más", dur=0.8), rect(110, 890, 420, 100, AZUL, texto="Carlyle > 38 %", tam=38, en="el grupo Carlyle", dur=0.8), masc("normal", 920, 230, t=0.2)]}]},
"02": {"salida": "../../output/SHORT_02_inversion_verde.mp4", "escenas": [
  {"id": "a", "desde": "¿Cuánto invierte Moeve", "fondo": "fabrica_alimentos", "zoom": [1.0, 1.08], "capas": [panel(640), cab("TRANSICIÓN ENERGÉTICA"), cifra(55, 540, 190, sufijo=" %", color="#2E8B57", en="el cincuenta y cinco"), mano("de la inversión de 2025 (récord)", 700, 46, en="récord"), mano("antes: 43 %", 820, 50, en="el cuarenta y tres"), masc("contento", 880, 340, entra="der", t=0.2)]},
  {"id": "b", "desde": "Y en el primer semestre", "fondo": "#F4E9D0", "capas": [cab("1.er SEMESTRE 2026"), cifra(69, 560, 190, sufijo=" %", color="#2E8B57", en="el sesenta y nueve"), mano("de 605 M€ invertidos", 700, 50, en="seiscientos cinco"), sello("OTRO RÉCORD", 880, 60, en="Otro récord"), masc("riendo", 920, 240, t=0.2)]}]},
"03": {"salida": "../../output/SHORT_03_de_donde_sale_el_dinero.mp4", "escenas": [
  {"id": "a", "desde": "Moeve invierte sobre todo en verde", "fondo": "#FFF3C4", "capas": [cab("¿DE DÓNDE SALE EL DINERO?"), txt("Invierte en verde…", 560, 66, color="#2E8B57", t=0.4), txt("…¿e ingresa con?", 760, 66, color=ROJO, en="¿De dónde sale el dinero"), masc("pensativo", 900, 300, t=0.2)]},
  {"id": "b", "desde": "En dos mil veinticinco, la empresa ganó", "fondo": "#E3E7EC", "capas": [cab("EBITDA 2025"), rect(110, 460, 860, 100, AZUL, texto="Grupo: 1.685 M€", tam=40, en="mil seiscientos ochenta", dur=0.8), rect(110, 590, 700, 100, ROJO, texto="Energía: 1.400 M€ · 83 %", tam=36, en="mil cuatrocientos", dur=0.8), mano("refino, estaciones, comercio y energías limpias comerciales", 780, 38, en="junto con las energías limpias"), masc("lupa", 920, 220, t=0.2)]},
  {"id": "c", "desde": "Y en el primer semestre de dos mil veintiséis", "fondo": "#F4E9D0", "capas": [cab("1.er SEMESTRE 2026"), rect(110, 460, 860, 100, AZUL, texto="Grupo: 1.178 M€", tam=40, en="mil ciento setenta y ocho", dur=0.8), rect(110, 590, 690, 100, ROJO, texto="Energía: 945 M€ · 80 %", tam=36, en="novecientos cuarenta y cinco", dur=0.8), masc("normal", 920, 240, t=0.2)]}]},
"04": {"salida": "../../output/SHORT_04_lo_que_construye.mp4", "escenas": [
  {"id": "a", "desde": "Esto es lo que Moeve dice", "fondo": "torre_electrica", "zoom": [1.0, 1.08], "capas": [panel(700), cab("LO QUE CONSTRUYE"), mano("304 M€ de fondos europeos\npara el Valle del Hidrógeno Verde", 520, 46, en="trescientos cuatro"), mano("Planta de biocombustibles en Huelva:\n> 50 % construida", 740, 44, en="Una planta"), mano("> 280 puntos de recarga ultrarrápida", 940, 42, en="doscientos ochenta"), mano("500 estaciones renovadas", 1050, 44, en="quinientas"), masc("normal", 900, 230, t=0.2)]}]},
"05": {"salida": "../../output/SHORT_05_ballenoil.mp4", "escenas": [
  {"id": "a", "desde": "La gasolinera low cost Ballenoil", "fondo": "calle_comercial", "zoom": [1.0, 1.08], "capas": [panel(640), cab("BALLENOIL"), mano("La low cost también es de Moeve", 520, 50, t=0.4), cifra(370, 680, 190, color=ROJO, en="trescientas setenta"), mano("estaciones (65 abiertas en 2025)", 820, 44, en="trescientas setenta"), masc("sorprendido", 880, 340, entra="der", t=0.2)]}]},
"06": {"salida": "../../output/SHORT_06_norma_afirmaciones_verdes.mp4", "escenas": [
  {"id": "a", "desde": "Desde el veintisiete de septiembre", "fondo": "#E6E0F5", "capas": [cab("DESDE EL 27/9/2026"), mano("Directiva (UE) 2024/825", 480, 50, t=0.3), txt("Presumir de «verde»\nsin demostrarlo", 700, 70, color=ROJO, en="entre otras cosas"), masc("lupa", 900, 280, t=0.2)]},
  {"id": "b", "desde": "También prohíbe presentar toda una empresa", "fondo": "#FFF3C4", "capas": [cab("TAMBIÉN PROHÍBE"), mano("Presentar toda una empresa como verde\nsi solo lo es un aspecto", 520, 46, t=0.3), mano("Neutralidad basada en\ncompensar emisiones", 820, 50, en="compensar emisiones"), masc("encoge_hombros", 920, 250, t=0.2)]}]},
"07": {"salida": "../../output/SHORT_07_impuestos_2088.mp4", "escenas": [
  {"id": "a", "desde": "Moeve contribuyó con dos mil ochenta", "fondo": "oficina_financiera", "zoom": [1.0, 1.08], "capas": [panel(640), cab("IMPUESTOS · 1.er SEM. 2026"), cifra(2088, 540, 170, sufijo=" M€", t=0.4), mano("en solo seis meses", 700, 48, en="en solo seis meses"), rect(110, 830, 800, 100, GRIS, texto="819 M€ por cuenta de Hacienda", tam=34, en="ochocientos diecinueve", dur=0.8), masc("moneda", 900, 330, entra="der", t=0.2)]}]},
}
for n, s in S.items():
    d = os.path.join(V, "shorts", f"short_{n}"); os.makedirs(d, exist_ok=True)
    json.dump({**BASE, **s}, open(os.path.join(d, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
