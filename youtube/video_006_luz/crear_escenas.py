"""Genera escenas_v2.json del vídeo 6 (factura de la luz). Datos: INVESTIGACION.md (Eurostat nrg_pc_204_c, BOE, MITECO)."""
import json, os

V = os.path.dirname(os.path.abspath(__file__))

def panel(x=90, y=120, w=1230, h=870): return {"tipo": "panel", "x": x, "y": y, "w": w, "h": h, "t": 0}
def titulo(txt, **k): return {"tipo": "texto", "texto": txt, "x": 1010, "y": 200, "tam": 76, "papel": True, **({"t": 0.2} if not k else k)}
def txt(contenido, x, y, tam=60, **k): return {"tipo": "texto", "texto": contenido, "x": x, "y": y, "tam": tam, **k}
def mano(contenido, x, y, tam=56, **k): return txt(contenido, x, y, tam, fuente="mano", **k)
def cifra(n, x, y, tam=170, **k): return {"tipo": "cifra", "hasta": n, "x": x, "y": y, "tam": tam, **k}
def masc(pose, x=1600, h=520, **k): return {"tipo": "mascota", "pose": pose, "x": x, "y": 1015, "h": h, **k}
def sello(contenido, x, y, tam=70, **k): return {"tipo": "sello", "texto": contenido, "x": x, "y": y, "tam": tam, **k}
def rect(x, y, w, h, color, **k): return {"tipo": "rect", "x": x, "y": y, "w": w, "h": h, "color": color, **k}
def moneda(texto, x, y, r=110, color="#F5B301", **k): return {"tipo": "moneda", "texto": texto, "r": r, "x": x, "y": y, "color": color, **k}

def leyenda(filas, x=900, y0=300, paso=95, tam=50):
    capas = []
    for i, (texto, color, en) in enumerate(filas):
        y = y0 + i * paso
        capas.append(rect(x, y - 28, 56, 56, color, en=en, dur=0.3))
        capas.append(txt(texto, x + 85, y, tam, ancla="izq", en=en))
    return capas

E = []
def escena(id, desde, fondo, capas, **k):
    E.append({"id": id, "desde": desde, "fondo": fondo, "capas": capas, **k})

EU = "Eurostat, nrg_pc_204_c (hogares, todas las bandas; actualizado el 7/10/2026)"
AMAR, ROJO, AZUL, VERDE, GRIS = "#F5B301", "#E0521B", "#9CC5E8", "#8FD18F", "#D9D2C0"

escena("01", "En dos años, la energía", "oficina_financiera", [
    panel(90, 120, 1230, 870), mano("2023 → 2025, tu factura de la luz", 700, 220, 56, t=0.2),
    txt("−14 %", 380, 420, 130, color="#2E8B57", anim="pop", en="se ha abaratado un catorce"), mano("la energía", 380, 540, 46, en="se ha abaratado un catorce"),
    txt("+9 %", 1000, 420, 130, color=ROJO, anim="pop", en="pagas un nueve por ciento más"), mano("lo que pagas", 1000, 540, 46, en="pagas un nueve por ciento más"),
    sello("IMPUESTOS ×2,7", 700, 800, 70, en="casi tres"),
    masc("sorprendido", 1620, 520, entra="der", t=0.3),
], zoom=[1.0, 1.06], fuente=EU + " (cálculo propio)")

escena("02", "Hoy vamos a abrir el ticket", "#FFF3C4", [
    txt("El ticket de tu\nfactura de la luz", 800, 260, 84, t=0.2),
    mano("Cifras oficiales de Eurostat, publicadas este mes", 800, 520, 52, en="Eurostat"),
    mano("¿Adónde va cada euro?", 800, 700, 64, papel=True, en="publicadas este mismo mes"),
    masc("saluda", 1620, 520, entra="der", t=0.2),
], fuente=EU)

escena("03", "Primero, una advertencia", "#E3E7EC", [
    sello("ES UNA MEDIA", 800, 260, 90, t=0.2),
    mano("Tu factura depende de:", 800, 470, 56, en="Tu factura depende"),
    txt("tu tarifa · tu potencia · tu consumo", 800, 600, 54, en="tu tarifa"),
    mano("Pero el orden de magnitud es real", 800, 800, 56, papel=True, en="orden de magnitud"),
    masc("encoge_hombros", 1620, 520, entra="der", t=0.2),
])

escena("04", "En dos mil veinticinco, un hogar", "calle_comercial", [
    panel(), mano("Un hogar español, 2025, de media", 700, 230, 56, t=0.2),
    cifra(28.4, 700, 450, 190, sufijo=" c", dec=1, en="veintiocho coma cuatro"),
    mano("por cada kilovatio hora (kWh), con todo incluido", 700, 620, 52, en="con todo incluido"),
    txt("1 kWh = 28,4 c", 700, 820, 70, papel=True, en="un kilovatio hora"),
    masc("lupa", 1620, 500, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=EU)

escena("05", "La primera es la energía", "#F4E9D0", [
    txt("Tu euro de la luz, en 3 partes", 470, 130, 56, papel=True, t=0.2),
    {"tipo": "tarta", "x": 470, "y": 590, "r": 300, "t": 0.3, "porciones": [
        {"v": 40.8, "color": AMAR, "en": "Once coma seis céntimos"},
        {"v": 28.4, "color": AZUL, "en": "Ocho coma uno céntimos"},
        {"v": 30.8, "color": ROJO, "en": "Ocho coma siete céntimos"}]},
    *leyenda([("41 c · energía y suministro (11,6)", AMAR, "Once coma seis céntimos"),
              ("28 c · redes (8,1)", AZUL, "Ocho coma uno céntimos"),
              ("31 c · impuestos, tasas y cargos (8,7)", ROJO, "Ocho coma siete céntimos")], x=830, y0=380, paso=125, tam=42),
    mano("Casi 1 euro de cada 3", 1210, 900, 50, en="Casi un euro de cada tres"),
], fuente=EU + " (porcentajes: cálculo propio)")

escena("06", "De esos ocho coma siete", "#E3E7EC", [
    mano("De los 8,7 c de impuestos, tasas y cargos…", 800, 200, 54, papel=True, t=0.2),
    rect(220, 330, 900, 130, ROJO, texto="IVA: 4,8 c · 17 % del total", tam=50, en="cuatro coma ocho son el IVA", dur=1.0),
    rect(220, 520, 440, 130, AZUL, texto="Otros: 3,9 c · 14 %", tam=44, en="El resto, casi cuatro céntimos", dur=1.0),
    mano("otros impuestos y gravámenes", 700, 740, 52, en="otros impuestos y gravámenes"),
    masc("senala", 1620, 520, mira="izq", entra="der", t=0.2),
], fuente=EU + " (resto = total − IVA; cálculo propio)")

escena("07", "Fíjate en dos mil veintitrés", "#FFF3C4", [
    mano("Energía y suministro (c/kWh)", 800, 190, 54, papel=True, t=0.2),
    rect(150, 290, 1000, 90, GRIS, texto="2023 · 13,5", tam=44, en="trece coma cinco", dur=0.8),
    rect(150, 400, 860, 90, AMAR, texto="2025 · 11,6  (−14 %)", tam=44, en="once coma seis", dur=0.8),
    mano("Costes de red (c/kWh)", 800, 580, 54, papel=True, en="Los costes de red"),
    rect(150, 680, 700, 90, GRIS, texto="2023 · 9,3", tam=44, en="de nueve coma tres", dur=0.8),
    rect(150, 790, 610, 90, AZUL, texto="2025 · 8,1  (−13 %)", tam=44, en="a ocho coma uno", dur=0.8),
    masc("pensativo", 1650, 500, entra="der", t=0.2),
], fuente=EU)

escena("08", "Pero los impuestos, tasas", "#F4E9D0", [
    mano("Impuestos, tasas, gravámenes y cargos (c/kWh)", 800, 190, 50, papel=True, t=0.2),
    txt("3,3", 330, 430, 150, en="tres coma tres"), mano("2023", 330, 560, 50, en="tres coma tres"),
    txt("6,3", 800, 430, 150, en="seis coma tres"), mano("2024", 800, 560, 50, en="seis coma tres"),
    txt("8,7", 1270, 430, 160, color=ROJO, anim="pop", en="ocho coma siete"), mano("2025", 1270, 570, 50, en="ocho coma siete"),
    sello("×2,7", 800, 760, 110, en="dos coma siete"),
    mano("Total: 26,0 → 28,4 c  (+9 %)", 800, 920, 54, papel=True, en="un nueve por ciento más"),
    masc("preocupado", 1650, 500, entra="der", t=0.2),
], fuente=EU + " (cálculo propio de las variaciones)")

escena("09", "Para que lo veas en euros", "#E6E0F5", [
    mano("Hogar de 3.000 kWh al año (ejemplo)", 800, 190, 54, papel=True, t=0.2),
    txt("2023: 781 €", 450, 400, 90, en="setecientos ochenta y un euros"),
    txt("2025: 851 €", 1150, 400, 90, color=ROJO, en="ochocientos cincuenta y uno"),
    sello("+71 € AL AÑO", 800, 590, 80, en="Setenta y un euros más"),
    mano("Energía −57 €   ·   Red −36 €", 800, 760, 56, en="cincuenta y siete euros menos"),
    txt("Impuestos y gravámenes +164 €", 800, 880, 60, color=ROJO, en="ciento sesenta y cuatro"),
    masc("moneda", 1650, 500, entra="der", t=0.2),
], fuente="Cálculo propio con las medias de Eurostat (3.000 kWh × precio medio de cada año); no es la factura de nadie en concreto")

escena("10", "¿Por qué ha pasado?", "#FFF3C4", [
    txt("¿Por qué?", 800, 280, 110, t=0.2),
    mano("Se han ido retirando las rebajas\nfiscales de la crisis energética", 800, 520, 62, papel=True, en="rebajas fiscales"),
    masc("pensativo", 1620, 520, entra="der", t=0.2),
])

escena("11", "En dos mil veinticuatro, el IVA", "#E3E7EC", [
    titulo("2024 · lo que dice el BOE"),
    txt("IVA de la luz: 10 %", 700, 380, 80, en="diez por ciento"),
    mano("contratos de hasta 10 kW,\ncon el mercado diario > 45 €/MWh", 700, 540, 48, en="superara los cuarenta y cinco"),
    txt("Impuesto eléctrico: 2,5 % → 3,8 %", 700, 770, 66, en="dos coma cinco"),
    mano("1.er trimestre → 2.º trimestre", 700, 880, 44, en="dos coma cinco"),
    masc("lupa", 1620, 500, entra="der", t=0.2),
], fuente="BOE: Real Decreto-ley 8/2023, arts. 21 y 22")

escena("12", "En dos mil veinticinco, el IVA es el general", "#F4E9D0", [
    titulo("2025 · el tipo general"),
    txt("IVA: 21 %", 700, 420, 110, color=ROJO, anim="pop", en="veintiuno por ciento"),
    txt("Impuesto eléctrico: 5,11 %", 700, 680, 80, color=ROJO, anim="pop", en="cinco coma uno uno"),
    mano("Ley 37/1992 (art. 90) y Ley 38/1992 (art. 99)", 700, 860, 44, en="el general"),
    masc("senala", 1620, 500, mira="izq", entra="der", t=0.2),
], fuente="BOE: Ley 37/1992, art. 90; Ley 38/1992, art. 99.1")

escena("13", "Ahora, otra cifra que conviene conocer", "#E6E0F5", [
    sello("LOS CARGOS DEL SISTEMA", 800, 260, 76, t=0.2),
    mano("Otra clasificación: Eurostat y el Ministerio\nno agrupan igual, así que no se suman", 800, 520, 52, papel=True, en="no clasifican las cosas igual"),
    masc("encoge_hombros", 1620, 520, entra="der", t=0.2),
])

escena("14", "Para dos mil veintiséis, el Ministerio", "centro_logistico", [
    panel(), titulo("Costes del sistema 2026"),
    cifra(8510, 700, 400, 170, sufijo=" M€", t=0.4),
    mano("Pagan, según el Ministerio:", 700, 560, 50, en="Pagan, según el propio Ministerio"),
    txt("· Renovables, cogeneración y residuos", 700, 660, 46, en="retribución específica"),
    txt("· Sobrecostes de las islas y otros\nterritorios no peninsulares", 700, 770, 46, en="territorios no peninsulares"),
    txt("· Antiguos déficits del sistema", 700, 900, 46, en="antiguos déficits"),
    masc("normal", 1650, 480, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="MITECO, memoria de la Orden TED/1524/2025")

escena("15", "De esos ocho mil quinientos diez", "#FFF3C4", [
    mano("Quién paga los 8.510 M€ (2026)", 800, 190, 56, papel=True, t=0.2),
    rect(150, 290, 1100, 100, AZUL, texto="Costes del sistema: 8.510 M€", tam=46, t=0.4, dur=0.8),
    rect(150, 450, 570, 120, VERDE, texto="Otros ingresos: 4.453 M€", tam=42, en="unos cuatro mil cuatrocientos", dur=0.9),
    rect(720, 450, 530, 120, ROJO, texto="Consumidores: 4.057 M€", tam=42, en="Los otros cuatro mil cincuenta", dur=0.9),
    mano("Impuesto a la generación: ≈ 2.000 M€", 700, 680, 46, en="con el impuesto a la generación"),
    mano("Subastas de CO₂: 1.100 M€", 700, 780, 46, en="subastas de derechos"),
    masc("senala", 1650, 500, mira="izq", entra="der", t=0.2),
], fuente="MITECO, memoria de la Orden TED/1524/2025 (BOE-A-2025-26705)")

escena("16", "O sea: de cada cien euros", "#E3E7EC", [
    mano("De cada 100 € de costes del sistema…", 800, 250, 58, papel=True, t=0.2),
    cifra(48, 450, 520, 200, sufijo=" €", color=ROJO, en="cuarenta y ocho"), mano("los pagas tú", 450, 680, 52, en="cuarenta y ocho"),
    cifra(52, 1150, 520, 200, sufijo=" €", color="#2E8B57", en="cuarenta y ocho", t=1.0), mano("los pagan otros ingresos", 1150, 680, 48, en="cuarenta y ocho", t=1.2),
    masc("normal", 1650, 500, entra="der", t=0.2),
], fuente="MITECO (4.057 / 8.510 = 47,7 %; cálculo propio)")

escena("17", "Y ahora, una pregunta incómoda", "puerto_avion", [
    panel(), mano("¿Es más cara que en Europa? (2025, c/kWh)", 700, 200, 50, papel=True, t=0.2),
    rect(150, 290, 1010, 80, "#9A9A9A", texto="Alemania 40,2", tam=40, en="Alemania, cuarenta", dur=0.7),
    rect(150, 390, 790, 80, "#9A9A9A", texto="Italia 35,1", tam=40, en="Italia, treinta y cinco", dur=0.7),
    rect(150, 490, 680, 80, AMAR, texto="UE-27: 29,4", tam=40, en="unos veintinueve coma cuatro", dur=0.7),
    rect(150, 590, 640, 80, ROJO, texto="España 28,4", tam=40, en="España, veintiocho coma cuatro", dur=0.7),
    rect(150, 690, 580, 80, "#9A9A9A", texto="Portugal 25,6", tam=40, en="Francia y Portugal", dur=0.7),
    rect(150, 790, 575, 80, "#9A9A9A", texto="Francia 25,5", tam=40, en="algo más de veinticinco", dur=0.7),
    masc("sorprendido", 1650, 500, entra="der", t=0.2),
], zoom=[1.0, 1.05], fuente=EU)

escena("18", "Pero sí hay una diferencia", "#F4E9D0", [
    mano("Impuestos y gravámenes: % de la factura", 800, 190, 52, papel=True, t=0.2),
    rect(150, 290, 1010, 80, "#9A9A9A", texto="Portugal 34 %", tam=40, en="el treinta y cuatro", dur=0.7),
    rect(150, 390, 930, 80, "#9A9A9A", texto="Alemania 31,5 %", tam=40, en="el treinta y uno y medio", dur=0.7),
    rect(150, 490, 900, 80, ROJO, texto="España 31 %", tam=40, en="treinta y uno por ciento", dur=0.7),
    rect(150, 590, 880, 80, "#9A9A9A", texto="Francia 30 %", tam=40, en="casi el treinta", dur=0.7),
    rect(150, 690, 820, 80, AMAR, texto="UE-27: 28 %", tam=40, en="el veintiocho", dur=0.7),
    rect(150, 790, 790, 80, "#9A9A9A", texto="Italia 27 %", tam=40, en="casi el treinta", t=0.9, dur=0.7),
    masc("lupa", 1650, 500, entra="der", t=0.2),
], fuente=EU + " (porcentajes: cálculo propio)")

escena("19", "Y un dato más", "#E6E0F5", [
    mano("Precio por kWh según lo que consumes (2025)", 800, 190, 52, papel=True, t=0.2),
    cifra(32.6, 450, 500, 150, sufijo=" c", dec=1, color=ROJO, en="treinta y dos coma seis"), mano("1.000–2.500 kWh al año", 450, 630, 46, en="entre mil y dos mil quinientos"),
    cifra(26.4, 1150, 500, 150, sufijo=" c", dec=1, color="#2E8B57", en="veintiséis coma cuatro"), mano("2.500–5.000 kWh al año", 1150, 630, 46, en="entre dos mil quinientos y cinco mil"),
    mano("Parte puede venir de los términos fijos\n(Eurostat no lo explica)", 800, 860, 46, papel=True, en="términos fijos"),
    masc("pensativo", 1650, 500, entra="der", t=0.2),
], fuente=EU)

escena("20", "Así que, la próxima vez", "supermercado", [
    panel(), titulo("El viaje de tu euro"),
    {"tipo": "tarta", "x": 420, "y": 640, "r": 260, "t": 0.3, "porciones": [
        {"v": 40.8, "color": AMAR, "en": "cuarenta y un céntimos"},
        {"v": 28.4, "color": AZUL, "en": "Veintiocho, las redes"},
        {"v": 30.8, "color": ROJO, "en": "treinta y uno, impuestos"}]},
    *leyenda([("41 c · energía y suministro", AMAR, "cuarenta y un céntimos"),
              ("28 c · redes", AZUL, "Veintiocho, las redes"),
              ("31 c · impuestos y cargos (17 de IVA)", ROJO, "treinta y uno, impuestos")], x=760, y0=440, paso=120, tam=42),
    masc("saluda", 1650, 500, entra="der", t=0.2),
], fuente=EU + " (cálculo propio de los porcentajes)")

escena("21", "La luz no se ha encarecido", "#FFF3C4", [
    txt("La energía ha bajado", 800, 260, 84, t=0.3, en="que ha bajado"),
    txt("Lo que se ha sumado alrededor, no", 800, 440, 66, color=ROJO, en="Se ha encarecido por lo que"),
    mano("¿Cuánto decide el mercado\ny cuánto deciden las normas?", 800, 720, 62, papel=True, en="cuánto de lo que pagas decide"),
    masc("pensativo", 1640, 500, entra="der", t=0.2),
])

escena("22", "Aquí, cada semana, abrimos", "#F5B301", [
    masc("saluda", 960, 560, entra="abajo", t=0.2),
    txt("TICKET MEDIO", 960, 170, 150, anim="pop", t=0.3),
    mano("Cada semana, el ticket de algo que pagas todos los días", 960, 300, 50, papel=True, t=1.0),
], sin_marca=True)

cfg = {"musica": "audio/musica.mp3", "musica_db": -26, "cola": 3, "escenas": E}
json.dump(cfg, open(os.path.join(V, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("escenas:", len(E))
