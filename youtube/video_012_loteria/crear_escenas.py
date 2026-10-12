"""Escenas del vídeo 12 (Lotería de Navidad). Datos: INVESTIGACION.md."""
import json, os
V = os.path.dirname(os.path.abspath(__file__))
def panel(x=90, y=120, w=1230, h=870): return {"tipo": "panel", "x": x, "y": y, "w": w, "h": h, "t": 0}
def titulo(t, **k): return {"tipo": "texto", "texto": t, "x": 1010, "y": 200, "tam": 76, "papel": True, **({"t": 0.2} if not k else k)}
def txt(c, x, y, tam=60, **k): return {"tipo": "texto", "texto": c, "x": x, "y": y, "tam": tam, **k}
def mano(c, x, y, tam=56, **k): return txt(c, x, y, tam, fuente="mano", **k)
def cifra(n, x, y, tam=170, **k): return {"tipo": "cifra", "hasta": n, "x": x, "y": y, "tam": tam, **k}
def masc(p, x=1600, h=520, **k): return {"tipo": "mascota", "pose": p, "x": x, "y": 1015, "h": h, **k}
def sello(c, x, y, tam=70, **k): return {"tipo": "sello", "texto": c, "x": x, "y": y, "tam": tam, **k}
def rect(x, y, w, h, c, **k): return {"tipo": "rect", "x": x, "y": y, "w": w, "h": h, "color": c, **k}
E_ = []
def escena(i, d, f, c, **k): E_.append({"id": i, "desde": d, "fondo": f, "capas": c, **k})
AMAR, ROJO, AZUL, VERDE, GRIS = "#F5B301", "#E0521B", "#9CC5E8", "#8FD18F", "#D9D2C0"
AG = "Agencia Tributaria, premios Lotería de Navidad (17/12/2024)"; PR = "Prensa con datos de SELAE (sorteo 2025)"
escena("01", "Cada veintidós de diciembre", "administracion_loteria", [
    panel(), mano("22 de diciembre", 700, 230, 58, t=0.2),
    cifra(20, 700, 460, 200, sufijo=" €", color=ROJO, en="Cuesta veinte euros"), mano("un décimo de Lotería de Navidad", 700, 640, 52, en="un décimo"),
    sello("¿QUIÉN GANA DE VERDAD?", 700, 820, 64, en="quién gana de verdad"),
    masc("pensativo", 1630, 520, entra="der", t=0.3),
], zoom=[1.0, 1.06])
escena("02", "Hoy abrimos el ticket", "#FFF3C4", [
    txt("Solo los números", 800, 350, 90, t=0.2), sello("SIN ACONSEJAR JUGAR NI NO JUGAR", 800, 640, 56, en="Sin aconsejar"),
    masc("lupa", 1620, 520, entra="der", t=0.2),
])
escena("03", "Primero, el tamaño", "administracion_loteria", [
    panel(), titulo("EL SORTEO DE 2025"),
    cifra(198, 500, 400, 150, sufijo=" series", en="ciento noventa y ocho series"), mano("de 100.000 números cada una", 700, 560, 50, en="cien mil números"),
    rect(150, 650, 700, 100, AMAR, texto="Décimo: 20 €", tam=44, en="Cada décimo cuesta"), rect(150, 780, 880, 100, ROJO, texto="Emisión: 3.960 M€", tam=44, en="tres mil novecientos sesenta"),
    masc("normal", 1680, 500, entra="der", t=0.2),
], fuente=PR)
escena("04", "Según los datos publicados del sorteo, el setenta", "#E3E7EC", [
    titulo("70 % A PREMIOS"), cifra(2772, 700, 400, 170, sufijo=" M€", en="dos mil setecientos setenta y dos"),
    mano("Ventas del sorteo: 3.554 M€ (+1,4 %)", 700, 600, 50, en="tres mil quinientos cincuenta y cuatro"),
    masc("normal", 1680, 500, entra="der", t=0.2),
], fuente=PR)
escena("05", "Ahora, una cuenta propia", "#F4E9D0", [
    titulo("CUENTA PROPIA"), mano("De cada 20 €, 70 % son premios", 700, 330, 56, en="el setenta por ciento son premios"),
    cifra(14, 700, 520, 220, sufijo=" €", color="#2E8B57", en="catorce euros por décimo"), mano("de media por décimo, antes de impuestos", 700, 700, 48, en="antes de impuestos"),
    sello("ES UN PROMEDIO", 700, 860, 60, en="Casi nadie recibe catorce"),
    masc("encoge_hombros", 1640, 500, entra="der", t=0.2),
])
escena("06", "Mira cómo se reparte", "administracion_loteria", [
    panel(), titulo("EL GORDO"), cifra(400000, 600, 400, 150, sufijo=" €", en="cuatrocientos mil euros por décimo"), mano("por décimo (4 M€ por serie)", 700, 560, 50, en="cuatro millones de euros por serie"),
    rect(150, 650, 880, 100, AZUL, texto="Probabilidad: 1 entre 100.000", tam=40, en="una entre cien mil", dur=0.8),
    rect(150, 780, 880, 100, AMAR, texto="Aporta 4 € de esos 14", tam=42, en="cuatro de esos catorce", dur=0.8),
    masc("moneda", 1680, 500, entra="der", t=0.2),
], fuente=PR)
escena("07", "El segundo premio", "#FFF3C4", [
    titulo("LOS TRES GRANDES"), mano("2.º: 1.250.000 € por serie", 700, 330, 52, en="un millón doscientos cincuenta mil"), mano("3.º: 500.000 € por serie", 700, 450, 52, en="quinientos mil"),
    cifra(41, 700, 640, 190, sufijo=" %", color=ROJO, en="cuarenta y uno por ciento"), mano("de todo el dinero en premios (cálculo propio)", 700, 810, 46, en="cálculo nuestro"),
    masc("lupa", 1640, 500, entra="der", t=0.2),
])
escena("08", "Y ahora, Hacienda", "oficina_financiera", [
    panel(), titulo("HACIENDA"), mano("Ley 16/2012", 700, 330, 54, en="Ley dieciséis"),
    rect(150, 440, 880, 110, VERDE, texto="Hasta 40.000 €: exento", tam=44, en="cuarenta mil euros de cada décimo"),
    rect(150, 580, 880, 110, ROJO, texto="El exceso: retención del 20 %", tam=42, en="retención del veinte por ciento"),
    mano("Lo dice la Agencia Tributaria", 700, 800, 48, en="Lo dice la Agencia Tributaria"),
    masc("senala", 1680, 500, entra="der", t=0.2),
], fuente=AG)
escena("09", "El ejemplo oficial", "#E3E7EC", [
    titulo("EJEMPLO OFICIAL"), mano("Premio de 100.000 €", 700, 330, 56, en="cien mil euros"),
    mano("(100.000 − 40.000) × 20 % =", 700, 470, 50, en="veinte por ciento de sesenta mil"), cifra(12000, 700, 640, 150, sufijo=" € de retención", en="doce mil euros"),
    mano("Cobras 88.000 €", 700, 830, 56, en="ochenta y ocho mil"),
    masc("normal", 1680, 500, entra="der", t=0.2),
], fuente=AG)
escena("10", "Aplicado al Gordo", "administracion_loteria", [
    panel(), titulo("EL GORDO, NETO"), mano("400.000 − 40.000 = 360.000", 700, 330, 50, en="trescientos sesenta mil"),
    rect(150, 440, 880, 100, ROJO, texto="Retención: 72.000 €", tam=44, en="setenta y dos mil euros"),
    rect(150, 570, 880, 100, VERDE, texto="Cobras: 328.000 €", tam=44, en="trescientos veintiocho mil"),
    mano("2.º (125.000 €): retención 17.000 €", 700, 770, 42, en="diecisiete mil"), mano("3.º (50.000 €): retención 2.000 €", 700, 860, 42, en="paga dos mil"),
    masc("moneda", 1680, 500, entra="der", t=0.2),
], fuente="Cálculo propio con la regla de la " + AG)
escena("11", "La retención se aplica", "#FFF3C4", [
    titulo("CADA DÉCIMO, POR SEPARADO"), mano("SELAE retiene al cobrar", 700, 340, 56, en="en el momento del cobro"),
    mano("Décimo compartido:\nlos 40.000 € exentos se reparten", 700, 520, 52, en="Si un décimo es compartido"),
    sello("COMPARTIR NO TE HACE PAGAR MÁS", 700, 820, 52, en="compartir no te hace pagar más"),
    masc("contento", 1640, 500, entra="der", t=0.2),
])
escena("12", "Quedan dos preguntas", "#E6E0F5", [
    titulo("¿QUIÉN SE QUEDA EL 30 %?"), cifra(30, 700, 400, 200, sufijo=" %", color=ROJO, en="treinta por ciento que no es premio"),
    sello("SELAE NO LO DESGLOSA\n(que hayamos podido consultar)", 700, 700, 50, en="no desglosa"),
    masc("encoge_hombros", 1640, 500, entra="der", t=0.2),
])
escena("13", "Lo que sí es público", "oficina_financiera", [
    panel(), titulo("SELAE EN 2024"), mano("Ventas, todos sus juegos", 700, 330, 46, en="diez mil trescientos noventa y seis"), cifra(10396, 700, 440, 130, sufijo=" M€", en="diez mil trescientos noventa y seis"),
    rect(150, 600, 880, 100, VERDE, texto="Beneficio: 2.437 M€ (23 %)", tam=42, en="dos mil cuatrocientos treinta y siete"),
    rect(150, 730, 880, 100, GRIS, texto="Impuesto de sociedades: 812 M€", tam=38, en="ochocientos doce millones"),
    mano("Es el negocio entero, no solo Navidad", 700, 900, 44, en="Es el negocio entero"),
    masc("lupa", 1680, 500, entra="der", t=0.2),
], fuente="Cuentas de SELAE 2024, según El Economista y Sector del Juego")
escena("14", "La segunda pregunta", "#F4E9D0", [
    titulo("¿QUIÉN GANA SIEMPRE?"), mano("No gana siempre el mismo", 700, 340, 56, en="no gana siempre el mismo"),
    rect(150, 450, 880, 110, VERDE, texto="14 € → premios", tam=48, en="catorce van a premios"), rect(150, 590, 880, 110, GRIS, texto="6 € → no son premios", tam=48, en="seis no"),
    mano("De media, un décimo devuelve menos de lo que cuesta", 700, 800, 44, en="devuelve menos de lo que cuesta"),
    masc("pensativo", 1640, 500, entra="der", t=0.2),
])
escena("15", "Eso no significa", "#FFF3C4", [
    txt("Un juego de azar con un\nprecio y un reparto conocidos", 800, 330, 66, t=0.2),
    mano("Se compra por ilusión, tradición,\npor compartirlo con quien quieres", 800, 640, 52, en="la ilusión"),
    masc("contento", 1620, 520, entra="der", t=0.2),
])
escena("16", "Así que, la próxima vez", "administracion_loteria", [
    panel(), titulo("EL VIAJE DE TU DÉCIMO"), cifra(20, 500, 380, 160, sufijo=" € cuesta", en="Veinte euros."), cifra(14, 500, 560, 160, sufijo=" € vuelven (media)", color="#2E8B57", en="Catorce, de media"),
    mano("Y si te toca algo grande,\nHacienda retiene su parte", 700, 800, 50, en="Hacienda retiene su parte"),
    masc("moneda", 1680, 500, entra="der", t=0.2),
])
escena("17", "Aquí, cada semana, abrimos", "#F5B301", [
    masc("saluda", 960, 560, entra="abajo", t=0.2), txt("TICKET MEDIO", 960, 170, 150, anim="pop", t=0.3),
    mano("Cada semana, el ticket de algo que pagas todos los días", 960, 300, 50, papel=True, t=1.0),
], sin_marca=True)
json.dump({"musica": "audio/musica.mp3", "musica_db": -26, "cola": 3, "escenas": E_}, open(os.path.join(V, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("escenas:", len(E_))
