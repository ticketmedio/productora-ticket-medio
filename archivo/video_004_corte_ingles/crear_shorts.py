"""Genera escenas_v2.json (vertical) de los 3 Shorts de El Corte Inglés.
OJO: en txt() y mano() el orden es (texto, y, tam, x): la x va SIEMPRE con nombre."""
import json, os

V = os.path.dirname(os.path.abspath(__file__))
BASE = {"formato": "vertical", "fondos": "../../fondos", "musica": "../../audio/musica.mp3", "musica_db": -26, "cola": 1.5}

def cab(t): return {"tipo": "texto", "texto": t, "x": 540, "y": 220, "tam": 72, "papel": True, "t": -1, "dur": 0.01}
def panel(h=700): return {"tipo": "panel", "x": 60, "y": 360, "w": 960, "h": h}
def txt(c, y, tam=64, x=540, **k): return {"tipo": "texto", "texto": c, "x": x, "y": y, "tam": tam, **k}
def mano(c, y, tam=58, x=540, **k): return txt(c, y, tam, x, fuente="mano", **k)
def masc(pose, x=540, h=400, **k): return {"tipo": "mascota", "pose": pose, "x": x, "y": 1310, "h": h, **k}
def rect(x, y, w, h, color, **k): return {"tipo": "rect", "x": x, "y": y, "w": w, "h": h, "color": color, **k}
def sello(c, y, tam=64, x=540, **k): return {"tipo": "sello", "texto": c, "x": x, "y": y, "tam": tam, **k}

shorts = {
 "01": {"salida": "../../output/SHORT_01_el_jeque.mp4", "escenas": [
   {"id": "a", "desde": "Un jeque de Catar tiene", "fondo": "fachada", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("UN AS EN LA MANGA"),
     mano("Hamad bin Jassim Al Thani,\nex primer ministro de Catar", 500, 50, t=0.2),
     txt("2015", 700, 110, color="#E0521B", anim="pop", en="En dos mil quince"),
     txt("le presta 1.000 M€", 840, 76, en="le prestó mil millones"),
     masc("sorprendido", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "En dos mil dieciocho se los", "fondo": "#E6E0F5", "capas": [
     cab("UN AS EN LA MANGA"),
     txt("2018", 420, 100, color="#E0521B", t=0.1), mano("lo cobra en acciones:\n> 10 % de la empresa", 570, 58, t=0.2),
     txt("2022", 780, 100, color="#E0521B", en="Y en dos mil veintidós"), mano("El Corte Inglés le recompra\nla mitad por 485 M€", 930, 56, papel=True, en="le recompró la mitad"),
     masc("pensativo", 880, 320, t=0.2)]},
   {"id": "c", "desde": "Y la cuarta: el jeque", "fondo": "#F4E9D0", "capas": [
     cab("UN AS EN LA MANGA"),
     mano("Aún puede pedirle que le\nrecompre sus acciones en…", 460, 56, papel=True, t=0.1),
     txt("2028", 680, 120, color="#E0521B", anim="pop", en="dos mil veintiocho"),
     txt("2031", 830, 120, color="#E0521B", anim="pop", en="dos mil treinta y uno"),
     txt("2034", 980, 120, color="#E0521B", anim="pop", en="dos mil treinta y cuatro"),
     masc("preocupado", 880, 300, t=0.2)]},
 ]},
 "02": {"salida": "../../output/SHORT_02_su_propio_casero.mp4", "escenas": [
   {"id": "a", "desde": "El Corte Inglés casi no paga", "fondo": "fachada", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("¿SIN ALQUILER?"),
     txt("< 1 c", 560, 200, color="#E0521B", anim="pop", t=0.3),
     mano("por euro vendido, en alquileres", 720, 54, en="menos de un céntimo"),
     txt("Zara: 6 c", 880, 90, en="Zara paga seis"),
     masc("sorprendido", 880, 360, entra="der", t=0.2, poses=[{"en": "¿Por qué?", "pose": "pensativo"}])]},
   {"id": "b", "desde": "Porque casi todos sus edificios", "fondo": "#F4E9D0", "capas": [
     cab("¿SIN ALQUILER?"),
     sello("LOS EDIFICIOS SON SUYOS", 420, 56, t=0.1),
     {"tipo": "cifra", "hasta": 15666, "sufijo": " M€", "x": 540, "y": 600, "tam": 130, "color": "#2E8B57", "en": "están tasados"},
     mano("valen sus inmuebles", 710, 56, en="están tasados"),
     txt("Deuda: 1.648 M€", 860, 76, en="Su deuda hoy"),
     txt("× 9,5", 1020, 130, color="#E0521B", anim="pop", en="nueve veces y media"),
     masc("contento", 880, 300, t=0.2)]},
 ]},
 "03": {"salida": "../../output/SHORT_03_zara_13_eci_3.mp4", "escenas": [
   {"id": "a", "desde": "¿Por qué Zara gana trece", "fondo": "#FFF3C4", "capas": [
     cab("¿13 c O 3,5 c?"),
     mano("Beneficio por cada euro", 420, 56, t=0.1),
     rect(110, 490, 860, 120, "#F5B301", texto="Zara: 13 c", tam=52, t=0.3, dur=1.0),
     rect(110, 650, 232, 120, "#E0521B", texto="ECI: 3,5 c", tam=34, en="El Corte Inglés, solo", dur=0.6),
     masc("pensativo", 540, 420, entra="abajo", t=0.2)]},
   {"id": "b", "desde": "Zara, que vimos en el vídeo", "fondo": "planta_electronica", "zoom": [1.0, 1.06], "capas": [
     panel(700), cab("¿13 c O 3,5 c?"),
     txt("Zara fabrica lo suyo", 460, 66, t=0.1),
     mano("le cuesta 1 € → lo vende por ≈ 2,40 €", 580, 52, papel=True, en="casi dos y medio"),
     txt("El Corte Inglés revende\nmarcas de otros", 820, 64, color="#E0521B", en="revende sobre todo"),
     masc("lupa", 880, 320, t=0.2)]},
   {"id": "c", "desde": "Por eso su margen es mucho", "fondo": "#E3E7EC", "capas": [
     cab("¿13 c O 3,5 c?"),
     mano("Margen bruto (lo que le queda\nde lo que vende)", 440, 52, t=0.1),
     rect(110, 580, 500, 120, "#9CC5E8", texto="ECI: 34 %", tam=48, en="treinta y cuatro por ciento", dur=0.8),
     rect(110, 740, 860, 120, "#F5B301", texto="Zara: 58 %", tam=52, t=0.4, dur=1.0),
     masc("encoge_hombros", 880, 300, t=0.2)]},
   {"id": "d", "desde": "Y lo que queda, al final", "fondo": "#FFF3C4", "capas": [
     cab("¿13 c O 3,5 c?"),
     {"tipo": "moneda", "texto": "3,5 c", "r": 150, "x": 540, "y": 560, "color": "#E0521B", "t": 0.2},
     mano("de beneficio por cada euro", 780, 58, t=0.4),
     txt("Mercadona: 4 c · Zara: 13 c", 920, 60, en="Mercadona se quedaba"),
     masc("sorprendido", 880, 300, t=0.2)]},
 ]},
 "04": {"salida": "../../output/SHORT_04_pandemia.mp4", "escenas": [
   {"id": "a", "desde": "¿Cuánto perdió El Corte Inglés", "fondo": "grandes_almacenes", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("LA PANDEMIA"),
     mano("Año 2020: tiendas cerradas", 500, 56, t=0.3),
     txt("Ventas: −1/3", 760, 96, color="#E0521B", anim="pop", en="Con las tiendas cerradas"),
     masc("preocupado", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "Y, según la prensa, perdió", "fondo": "#F4E9D0", "capas": [
     cab("LA PANDEMIA"),
     mano("Pérdida de aquel año", 450, 56, t=0.1),
     {"tipo": "cifra", "hasta": 2945, "sufijo": " M€", "x": 540, "y": 640, "tam": 140, "color": "#E0521B", "en": "dos mil novecientos cuarenta y cinco"},
     sello("LA MAYOR DE SU HISTORIA", 880, 54, en="La mayor pérdida de su historia"),
     masc("sorprendido", 880, 320, t=0.2)]},
   {"id": "c", "desde": "Ahí es cuando todo el mundo", "fondo": "#E3E7EC", "capas": [
     cab("LA PANDEMIA"),
     txt("¿Cuánto le quedaba?", 560, 92, color="#E0521B", anim="pop", t=0.2),
     mano("La respuesta, en el vídeo completo", 780, 52, t=0.9),
     masc("pensativo", 880, 360, t=0.2)]},
 ]},
 "05": {"salida": "../../output/SHORT_05_vendio.mp4", "escenas": [
   {"id": "a", "desde": "¿Qué ha vendido El Corte Inglés", "fondo": "oficina_financiera", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("SE DESHIZO DE TODO"),
     mano("Para pagar la deuda…", 500, 58, t=0.3),
     masc("pensativo", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "Vendió Óptica dos mil", "fondo": "#E6E0F5", "capas": [
     cab("SE DESHIZO DE TODO"),
     txt("Óptica 2000", 450, 90, color="#E0521B", t=0.1),
     txt("Informática\nEl Corte Inglés", 700, 80, en="Vendió Informática"),
     masc("encoge_hombros", 880, 330, t=0.2)]},
   {"id": "c", "desde": "Y en dos mil veintidós, Mutua", "fondo": "#F4E9D0", "capas": [
     cab("SE DESHIZO DE TODO"),
     txt("2022", 430, 110, color="#E0521B", anim="pop", t=0.1),
     mano("Mutua Madrileña le paga", 600, 56, en="Mutua Madrileña le pagó"),
     {"tipo": "cifra", "hasta": 1105, "sufijo": " M€", "x": 540, "y": 790, "tam": 140, "color": "#2E8B57", "en": "mil ciento cinco millones"},
     mano("por la mitad de seguros\ny el 8 % de la empresa", 980, 50, papel=True, en="por la mitad de su negocio"),
     masc("contento", 880, 300, t=0.2)]},
 ]},
 "06": {"salida": "../../output/SHORT_06_tiendas.mp4", "escenas": [
   {"id": "a", "desde": "¿Cuántas tiendas ha cerrado", "fondo": "grandes_almacenes", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("MENOS TIENDAS"),
     mano("Grandes almacenes", 520, 60, t=0.3),
     masc("preocupado", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "En dos mil dieciocho tenía noventa y tres", "fondo": "#F4E9D0", "capas": [
     cab("MENOS TIENDAS"),
     txt("2018", 420, 100, color="#E0521B", t=0.1),
     {"tipo": "cifra", "hasta": 93, "x": 540, "y": 620, "tam": 170, "color": "#2E8B57", "en": "noventa y tres"},
     txt("Hoy", 840, 100, color="#E0521B", en="Hoy, setenta y dos"),
     {"tipo": "cifra", "hasta": 72, "x": 540, "y": 1040, "tam": 170, "color": "#E0521B", "en": "setenta y dos"},
     sello("21 MENOS", 1250, 80, en="Hoy, setenta y dos"),
     masc("sorprendido", 880, 280, t=0.2)]},
   {"id": "c", "desde": "Y la plantilla ha bajado", "fondo": "#E3E7EC", "capas": [
     cab("MENOS TIENDAS"),
     txt("La plantilla", 560, 84, t=0.2),
     mano("90.000 → menos de 82.000", 760, 58, en="noventa mil personas"),
     masc("preocupado", 880, 300, t=0.2)]},
   {"id": "d", "desde": "La segunda: las ventas", "fondo": "#FFF3C4", "capas": [
     cab("MENOS VENTAS"),
     mano("Frente a 2007", 450, 58, t=0.1),
     txt("−3.000 M€", 660, 120, color="#E0521B", anim="pop", en="tres mil millones"),
     txt("−17 %", 900, 160, color="#E0521B", anim="pop", en="diecisiete por ciento"),
     mano("sin descontar la inflación", 1060, 52, en="sin descontar la inflación"),
     masc("pensativo", 880, 260, t=0.2)]},
 ]},
 "07": {"salida": "../../output/SHORT_07_fundacion.mp4", "escenas": [
   {"id": "a", "desde": "¿Sabes quién manda de verdad", "fondo": "fachada", "zoom": [1.0, 1.08], "capas": [
     panel(640), cab("¿QUIÉN MANDA?"),
     mano("No es una familia\nni un fondo", 540, 60, t=0.5),
     masc("pensativo", 880, 380, entra="der", t=0.2)]},
   {"id": "b", "desde": "Es una fundación, la Fundación Ramón Areces", "fondo": "#E6E0F5", "capas": [
     cab("¿QUIÉN MANDA?"),
     sello("FUNDACIÓN RAMÓN ARECES", 430, 50, t=0.1),
     mano("dedica su dinero a la\ninvestigación científica", 650, 54, en="que dedica su dinero"),
     masc("contento", 880, 340, t=0.2)]},
   {"id": "c", "desde": "Tiene el cuarenta por ciento", "fondo": "#F4E9D0", "capas": [
     cab("¿QUIÉN MANDA?"),
     rect(110, 470, 700, 100, "#E0521B", texto="Fundación 40 %", tam=44, t=0.1, dur=0.7),
     rect(110, 620, 315, 100, "#F5B301", en="Otro dieciocho por ciento", dur=0.6),
     txt("Hermanas Álvarez 18 %", 670, 44, x=450, ancla="izq", en="Otro dieciocho por ciento"),
     rect(110, 770, 140, 100, "#9CC5E8", en="Mutua Madrileña tiene", dur=0.5),
     txt("Mutua Madrileña 8 %", 820, 44, x=275, ancla="izq", en="Mutua Madrileña tiene"),
     rect(110, 920, 96, 100, "#8FD18F", en="Y un jeque de Catar", dur=0.5),
     txt("Jeque de Catar ≈ 5,5 %", 970, 44, x=230, ancla="izq", en="Y un jeque de Catar"),
     masc("encoge_hombros", 940, 260, t=0.2)]},
   {"id": "d", "desde": "El Corte Inglés no cotiza en bolsa", "fondo": "#E3E7EC", "capas": [
     cab("¿QUIÉN MANDA?"),
     sello("NO COTIZA EN BOLSA", 600, 64, t=0.2),
     mano("Nadie puede comprar sus\nacciones en el mercado", 820, 52, t=1.0),
     masc("sorprendido", 880, 340, t=0.2)]},
 ]},
}
for n, s in shorts.items():
    d = os.path.join(V, "shorts", f"short_{n}")
    with open(os.path.join(d, "escenas_v2.json"), "w", encoding="utf-8") as f:
        json.dump({**BASE, **s}, f, ensure_ascii=False, indent=1)
print("ok")
