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
     mano("Hamad bin Jassim Al Thani,\nex primer ministro de Catar", 500, 50, en="Hamad bin Jassim"),
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
     txt("< 1 c", 560, 200, color="#E0521B", anim="pop", en="menos de un céntimo"),
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
}
for n, s in shorts.items():
    d = os.path.join(V, "shorts", f"short_{n}")
    with open(os.path.join(d, "escenas_v2.json"), "w", encoding="utf-8") as f:
        json.dump({**BASE, **s}, f, ensure_ascii=False, indent=1)
print("ok")
