"""Genera escenas_v2.json (vertical) de los 7 Shorts de Ryanair. OJO: en txt() y mano() el orden es (texto, y, tam, x): la x va con nombre."""
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
AMAR, ROJO, AZUL, VERDE = "#F5B301", "#E0521B", "#9CC5E8", "#8FD18F"
shorts = {
 "01": {"salida": "../../output/SHORT_01_billete_medio_74_euros.mp4", "escenas": [
   {"id": "a", "desde": "El billete medio de Ryanair no cuesta", "fondo": "puerto_avion", "zoom": [1.0, 1.08], "capas": [
     panel(700), cab("EL BILLETE MEDIO"),
     txt("NO CUESTA 10 €", 520, 90, color=ROJO, anim="pop", t=0.3),
     cifra(74.57, 760, 150, sufijo=" €", dec=2, en="setenta y cuatro con cincuenta y siete"), mano("de media por pasajero", 900, 44, t=2.5),
     masc("sorprendido", 880, 340, entra="der", t=0.2)]},
   {"id": "b", "desde": "De la tarifa, cincuenta euros", "fondo": "#F4E9D0", "capas": [
     cab("¿DE DÓNDE SALEN?"),
     rect(110, 480, 860, 120, AZUL, texto="Tarifa 50,67 € · 68 %", tam=44, en="el sesenta y ocho por ciento", dur=0.8),
     mano("la media de los de 10 € y los de 200 €", 690, 42, en="los de diez euros y los de doscientos"),
     rect(110, 790, 450, 120, AMAR, texto="Extras 24 € · 32 %", tam=36, en="veinticuatro euros", dur=0.8),
     mano("todo lo que pagas aparte del asiento", 990, 42, en="aparte del asiento"),
     masc("pensativo", 910, 240, t=0.2)]},
 ]},
 "02": {"salida": "../../output/SHORT_02_adonde_va_el_euro.mp4", "escenas": [
   {"id": "a", "desde": "¿Adónde va cada euro de un billete", "fondo": "centro_logistico", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("PARADA 1: COMBUSTIBLE"),
     cifra(26, 540, 190, sufijo=" €", color=ROJO, en="Veintiséis euros por pasajero"), mano("por pasajero · 35 % del billete", 680, 42, en="el treinta y cinco por ciento"),
     mano("80 % cubierto a ≈ 67 $/barril", 840, 46, en="cubierto el ochenta por ciento"),
     masc("senala", 880, 360, entra="der", t=0.2)]},
   {"id": "b", "desde": "Segunda parada: el personal", "fondo": "#E3E7EC", "capas": [
     cab("PARADAS 2 Y 3"),
     rect(110, 450, 640, 110, AMAR, texto="Personal 8,9 € · 12 %", tam=40, en="Casi nueve euros", dur=0.8),
     rect(110, 620, 600, 110, AZUL, texto="Aeropuertos 8,45 € · 11 %", tam=38, en="Ocho euros con cuarenta y cinco", dur=0.8),
     masc("lupa", 900, 280, t=0.2)]},
 ]},
 "03": {"salida": "../../output/SHORT_03_cuanto_gana_por_billete.mp4", "escenas": [
   {"id": "a", "desde": "¿Cuánto gana Ryanair de cada billete", "fondo": "oficina_financiera", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("¿CUÁNTO GANA?"),
     mano("Antes de impuestos:", 480, 50, t=0.4), cifra(11.37, 620, 150, sufijo=" €", dec=2, en="once euros con treinta y siete"),
     mano("Beneficio neto:", 790, 50, en="el beneficio neto antes"), cifra(10.84, 930, 150, sufijo=" €", dec=2, color=ROJO, en="diez euros con ochenta y cuatro"),
     masc("sorprendido", 880, 340, entra="der", t=0.2)]},
   {"id": "b", "desde": "Un catorce y medio por ciento", "fondo": "#E3E7EC", "capas": [
     cab("BENEFICIO POR CADA EURO"),
     rect(110, 450, 860, 100, ROJO, texto="Ryanair 14,5 c", tam=40, en="catorce céntimos y medio", dur=0.8),
     rect(110, 590, 280, 100, AMAR, texto="Mercadona ≈ 4 c", tam=32, en="Mercadona, unos cuatro", dur=0.8),
     rect(110, 730, 250, 100, VERDE, texto="Lidl ≈ 3,6 c", tam=32, en="Lidl, tres y medio", dur=0.8),
     mano("Sectores muy distintos", 960, 44, en="sectores muy distintos"),
     masc("pensativo", 900, 240, t=0.2)]},
 ]},
 "04": {"salida": "../../output/SHORT_04_maletas_extras_32.mp4", "escenas": [
   {"id": "a", "desde": "¿Gana Ryanair con las maletas", "fondo": "supermercado", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("¿GANA CON LAS MALETAS?"),
     cifra(24, 540, 180, sufijo=" €", t=0.5), mano("de extras por pasajero", 680, 46, t=0.7),
     sello("32 % DE LOS INGRESOS", 840, 60, en="el treinta y dos por ciento"),
     masc("lupa", 880, 360, entra="der", t=0.2)]},
   {"id": "b", "desde": "Y fíjate en cómo crece cada parte", "fondo": "#E6E0F5", "capas": [
     cab("¿QUÉ CRECE MÁS?"),
     rect(110, 450, 860, 110, AZUL, texto="Tarifas +14 %", tam=44, en="un catorce por ciento", dur=0.8),
     rect(110, 600, 420, 110, AMAR, texto="Extras +6 %", tam=44, en="los de los extras, un seis", dur=0.8),
     txt("La tarifa crece más deprisa", 860, 56, color=ROJO, en="la tarifa crece más deprisa"),
     masc("senala", 900, 260, t=0.2)]},
   {"id": "c", "desde": "Fíjate en algo", "fondo": "#FFF3C4", "capas": [
     cab("EL REPARTO"),
     txt("68 % tarifa", 500, 100, color="#2E8B57", en="los dos tercios"), txt("32 % extras", 700, 100, color=ROJO, en="casi un tercio"),
     mano("El negocio no es solo la maleta", 920, 50, papel=True, en="no es solo cobrar por la maleta"),
     masc("encoge_hombros", 900, 260, t=0.2)]},
 ]},
 "05": {"salida": "../../output/SHORT_05_cada_avion_al_ano.mp4", "escenas": [
   {"id": "a", "desde": "Según sus cuentas, cada avión", "fondo": "puerto_avion", "zoom": [1.0, 1.08], "capas": [
     panel(700), cab("CADA AVIÓN, AL AÑO"),
     cifra(322000, 520, 130, en="trescientos veintidós mil"), mano("pasajeros", 630, 46, en="trescientos veintidós mil"),
     cifra(24, 780, 130, sufijo=" M€", en="veinticuatro millones"), mano("ingresos", 890, 46, en="veinticuatro millones"),
     cifra(3.5, 1030, 130, sufijo=" M€", dec=1, color=ROJO, en="tres millones y medio"), mano("beneficio", 1140, 46, en="tres millones y medio"),
     masc("sorprendido", 900, 300, entra="der", t=0.2)]},
   {"id": "b", "desde": "Y cada empleado", "fondo": "#F4E9D0", "capas": [
     cab("CADA EMPLEADO, AL AÑO"),
     cifra(518000, 520, 120, sufijo=" €", en="quinientos dieciocho mil"), mano("de ingresos", 640, 46, en="quinientos dieciocho mil"),
     cifra(75000, 820, 120, sufijo=" €", color=ROJO, en="setenta y cinco mil"), mano("de beneficio", 940, 46, en="setenta y cinco mil"),
     mano("Medias de todo el grupo", 1070, 42, en="medias de todo el grupo"),
     masc("pensativo", 900, 240, t=0.2)]},
 ]},
 "06": {"salida": "../../output/SHORT_06_tres_trucos.mp4", "escenas": [
   {"id": "a", "desde": "¿Cuál es el truco de Ryanair", "fondo": "#FFF3C4", "capas": [
     cab("LOS 3 TRUCOS"),
     txt("1 · Llenar el avión", 480, 64, en="Uno: llenar el avión"), mano("94 % de ocupación", 570, 46, en="noventa y cuatro por ciento"),
     txt("2 · Un solo modelo", 740, 64, en="Dos: un solo modelo"), mano("más fácil mantenerlos y formar", 830, 42, en="mantenimiento y la formación"),
     txt("3 · Cobrar aparte lo que\nno es el asiento", 1000, 56, en="Y tres: cobrar aparte"),
     masc("pensativo", 900, 220, t=0.2)]},
 ]},
 "07": {"salida": "../../output/SHORT_07_ley_europea_precio_final.mp4", "escenas": [
   {"id": "a", "desde": "¿Pueden los extras aparecer", "fondo": "#E6E0F5", "capas": [
     cab("LA LEY EUROPEA"),
     mano("Reglamento (CE) 1008/2008, art. 23", 470, 46, t=0.3),
     txt("Precio final siempre visible:\ntarifa + impuestos + tasas", 700, 56, en="el precio final tiene que mostrarse"),
     mano("Extras opcionales: claros al principio\ny aceptados de forma expresa", 960, 46, papel=True, en="suplementos opcionales"),
     masc("lupa", 900, 260, t=0.2)]},
 ]},
}
for n, s in shorts.items():
    d = os.path.join(V, "shorts", f"short_{n}"); os.makedirs(d, exist_ok=True)
    json.dump({**BASE, **s}, open(os.path.join(d, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
