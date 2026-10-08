"""Genera escenas_v2.json (vertical) de los 7 Shorts de la luz. OJO: en txt() y mano() el orden es (texto, y, tam, x): la x va con nombre."""
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
AMAR, ROJO, AZUL = "#F5B301", "#E0521B", "#9CC5E8"
shorts = {
 "01": {"salida": "../../output/SHORT_01_energia_baja_impuestos_x27.mp4", "escenas": [
   {"id": "a", "desde": "Según Eurostat, desde dos mil veintitrés", "fondo": "oficina_financiera", "zoom": [1.0, 1.08], "capas": [
     panel(700), cab("TU FACTURA DE LA LUZ"),
     txt("−14 %", 560, 150, color="#2E8B57", anim="pop", en="ha bajado un catorce"), mano("la energía", 680, 52, en="ha bajado un catorce"),
     txt("×2,7", 880, 160, color=ROJO, anim="pop", t=3.5), mano("los impuestos y gravámenes", 1000, 50, t=3.7),
     masc("sorprendido", 880, 340, entra="der", t=0.2)]},
   {"id": "b", "desde": "Entonces, la energía costaba", "fondo": "#F4E9D0", "capas": [
     cab("2023 → 2025 (c/kWh)"),
     mano("Energía", 440, 48, t=0.1), rect(110, 480, 800, 90, "#D9D2C0", texto="2023 · 13,5", tam=42, en="trece coma cinco", dur=0.7),
     rect(110, 590, 690, 90, AMAR, texto="2025 · 11,6", tam=42, en="once coma seis", dur=0.7),
     mano("Red", 760, 48, en="Los costes de red"), rect(110, 800, 560, 90, "#D9D2C0", texto="2023 · 9,3", tam=42, en="nueve coma tres", dur=0.7),
     rect(110, 910, 490, 90, AZUL, texto="2025 · 8,1", tam=42, en="ocho coma uno", dur=0.7),
     masc("pensativo", 900, 260, t=0.2)]},
   {"id": "c", "desde": "Pero los impuestos, tasas", "fondo": "#FFF3C4", "capas": [
     cab("¿Y LOS IMPUESTOS?"),
     txt("3,3 → 6,3 → 8,7", 520, 96, en="tres coma tres"), mano("2023 · 2024 · 2025 (c/kWh)", 620, 44, en="tres coma tres"),
     sello("×2,7", 800, 120, en="dos coma siete"),
     mano("Total: 26,0 → 28,4 c (+9 %)", 1010, 50, papel=True, en="un nueve por ciento más"),
     masc("preocupado", 900, 280, t=0.2)]},
 ]},
 "02": {"salida": "../../output/SHORT_02_reparto_euro_luz.mp4", "escenas": [
   {"id": "a", "desde": "En dos mil veinticinco, un hogar", "fondo": "calle_comercial", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("TU EURO DE LA LUZ"),
     cifra(28.4, 540, 170, sufijo=" c", dec=1, t=0.4), mano("por kilovatio hora, con todo incluido", 680, 44, t=0.5),
     mano("Eurostat · hogares · 2025", 820, 44, t=1.2),
     masc("lupa", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "La primera es la energía", "fondo": "#F4E9D0", "capas": [
     cab("TU EURO DE LA LUZ"),
     rect(110, 450, 860, 120, AMAR, texto="41 c · energía y suministro", tam=44, en="Once coma seis", dur=0.8),
     rect(110, 620, 600, 120, AZUL, texto="28 c · redes", tam=44, en="Ocho coma uno", dur=0.8),
     masc("senala", 880, 300, t=0.2)]},
   {"id": "c", "desde": "Y la tercera es la que Eurostat", "fondo": "#E3E7EC", "capas": [
     cab("TU EURO DE LA LUZ"),
     rect(110, 450, 880, 120, ROJO, texto="31 c · impuestos y cargos", tam=44, en="Ocho coma siete céntimos", dur=0.8),
     txt("Casi 1 euro de cada 3", 760, 66, en="Casi un euro de cada tres"),
     masc("sorprendido", 880, 300, t=0.2)]},
 ]},
 "03": {"salida": "../../output/SHORT_03_iva_impuesto_electrico.mp4", "escenas": [
   {"id": "a", "desde": "¿Por qué los impuestos de la luz", "fondo": "#FFF3C4", "capas": [
     cab("¿POR QUÉ SUBEN?"),
     mano("Se han ido retirando las\nrebajas fiscales de la crisis", 520, 58, papel=True, en="rebajas fiscales"),
     masc("pensativo", 880, 360, entra="der", t=0.2)]},
   {"id": "b", "desde": "En dos mil veinticuatro, el IVA", "fondo": "#E3E7EC", "capas": [
     cab("2024 · LO QUE DICE EL BOE"),
     txt("IVA: 10 %", 480, 110, en="del diez por ciento"), mano("hasta 10 kW y mercado > 45 €/MWh", 590, 40, en="cuarenta y cinco euros"),
     txt("Impuesto eléctrico:\n2,5 % → 3,8 %", 800, 72, en="dos coma cinco"),
     masc("lupa", 880, 280, t=0.2)]},
   {"id": "c", "desde": "En dos mil veinticinco, el IVA es el general", "fondo": "#F4E9D0", "capas": [
     cab("2025 · EL TIPO GENERAL"),
     txt("IVA: 21 %", 520, 130, color=ROJO, anim="pop", en="veintiuno por ciento"),
     txt("Impuesto eléctrico: 5,11 %", 760, 70, color=ROJO, anim="pop", en="cinco coma uno uno"),
     mano("El IVA, ×3 en dos años (Eurostat)", 960, 44, en="se multiplicó por tres"),
     masc("senala", 880, 280, t=0.2)]},
 ]},
 "04": {"salida": "../../output/SHORT_04_71_euros_mas.mp4", "escenas": [
   {"id": "a", "desde": "Un hogar que consume tres mil", "fondo": "supermercado", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("HOGAR DE 3.000 kWh/AÑO"),
     sello("+71 € AL AÑO", 560, 80, t=0.4), mano("frente a 2023", 700, 50, t=0.6),
     masc("moneda", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "Con los precios medios de dos mil veintitrés", "fondo": "#E6E0F5", "capas": [
     cab("HOGAR DE 3.000 kWh/AÑO"),
     txt("2023: 781 €", 480, 100, en="setecientos ochenta y un euros"),
     txt("2025: 851 €", 680, 100, color=ROJO, en="ochocientos cincuenta y uno"),
     sello("+71 €", 900, 100, en="Con los de dos mil veinticinco"),
     masc("pensativo", 900, 260, t=0.2)]},
   {"id": "c", "desde": "Pero la energía le costaría", "fondo": "#F4E9D0", "capas": [
     cab("¿DE DÓNDE SALE?"),
     mano("Energía  −57 €", 470, 62, en="cincuenta y siete euros menos"),
     mano("Red  −36 €", 600, 62, en="treinta y seis menos"),
     txt("Impuestos y gravámenes\n+164 €", 820, 76, color=ROJO, anim="pop", en="ciento sesenta y cuatro"),
     mano("Cálculo propio con medias de Eurostat", 1050, 38, en="un cálculo nuestro"),
     masc("senala", 900, 260, t=0.2)]},
 ]},
 "05": {"salida": "../../output/SHORT_05_costes_sistema_electrico.mp4", "escenas": [
   {"id": "a", "desde": "Los costes del sistema eléctrico", "fondo": "centro_logistico", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("COSTES DEL SISTEMA 2026"),
     cifra(8510, 540, 150, sufijo=" M€", t=0.4), mano("Ministerio para la Transición Ecológica", 680, 42, t=0.6),
     masc("lupa", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "Pagan, según el propio Ministerio", "fondo": "#E6E0F5", "capas": [
     cab("¿QUÉ PAGAN?"),
     mano("Renovables, cogeneración\ny residuos", 470, 52, en="retribución específica"),
     mano("Sobrecostes de las islas\ny territorios no peninsulares", 660, 52, en="territorios no peninsulares"),
     mano("Antiguos déficits del sistema", 860, 52, en="antiguos déficits"),
     masc("normal", 900, 280, t=0.2)]},
   {"id": "c", "desde": "Los otros cuatro mil cincuenta", "fondo": "#FFF3C4", "capas": [
     cab("¿QUIÉN LOS PAGA?"),
     cifra(48, 520, 190, sufijo=" €", color=ROJO, en="cuarenta y ocho"), mano("de cada 100 € los pagas tú", 660, 48, en="cuarenta y ocho"),
     cifra(52, 840, 190, sufijo=" €", color="#2E8B57", en="cincuenta y dos"), mano("otros ingresos", 980, 48, en="cincuenta y dos"),
     masc("senala", 900, 240, t=0.2)]},
 ]},
 "06": {"salida": "../../output/SHORT_06_luz_espana_vs_europa.mp4", "escenas": [
   {"id": "a", "desde": "¿Es la luz en España más cara", "fondo": "puerto_avion", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("¿MÁS CARA QUE EN EUROPA?"),
     mano("Eurostat · 2025 · c/kWh", 480, 46, t=0.4),
     txt("España 28,4", 640, 90, color=ROJO, en="España, veintiocho coma cuatro"),
     txt("UE-27: 29,4", 800, 80, en="Unión Europea"),
     masc("pensativo", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "Alemania, cuarenta", "fondo": "#E3E7EC", "capas": [
     cab("¿MÁS CARA QUE EN EUROPA?"),
     rect(110, 470, 860, 90, "#9A9A9A", texto="Alemania 40,2", tam=40, en="Alemania, cuarenta", dur=0.7),
     rect(110, 590, 750, 90, "#9A9A9A", texto="Italia 35,1", tam=40, en="Italia, treinta y cinco", dur=0.7),
     rect(110, 710, 560, 90, "#9A9A9A", texto="Portugal 25,6 · Francia 25,5", tam=34, en="Francia y Portugal", dur=0.7),
     masc("encoge_hombros", 900, 280, t=0.2)]},
 ]},
 "07": {"salida": "../../output/SHORT_07_consumo_bajo_paga_mas.mp4", "escenas": [
   {"id": "a", "desde": "Según Eurostat, quien consume poco", "fondo": "#E6E0F5", "capas": [
     cab("¿QUIÉN PAGA MÁS POR kWh?"),
     cifra(32.6, 520, 170, sufijo=" c", dec=1, color=ROJO, en="treinta y dos coma seis"), mano("1.000–2.500 kWh al año", 650, 46, en="entre mil y dos mil quinientos"),
     cifra(26.4, 860, 170, sufijo=" c", dec=1, color="#2E8B57", en="Los que gastan entre dos mil quinientos"), mano("2.500–5.000 kWh al año", 990, 46, en="Los que gastan entre dos mil quinientos"),
     masc("sorprendido", 900, 260, t=0.2)]},
   {"id": "b", "desde": "Eurostat no lo explica", "fondo": "#FFF3C4", "capas": [
     cab("¿POR QUÉ?"),
     mano("Eurostat no lo explica", 480, 56, t=0.2),
     mano("Parte puede venir de los\ntérminos fijos de la factura,\nque se reparten entre menos kWh", 700, 52, papel=True, en="términos fijos"),
     masc("pensativo", 900, 300, t=0.2)]},
 ]},
}
for n, s in shorts.items():
    d = os.path.join(V, "shorts", f"short_{n}"); os.makedirs(d, exist_ok=True)
    json.dump({**BASE, **s}, open(os.path.join(d, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
