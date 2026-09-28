"""Genera escenas_v2.json del vídeo 3 (Zara). Se deja en la carpeta para poder retocarlo y volver a generarlo."""
import json, os

V = os.path.dirname(os.path.abspath(__file__))
CAMISETA = "file:///" + os.path.join(V, "assets", "camiseta.svg").replace("\\", "/")

def panel(x=90, y=120, w=1230, h=870): return {"tipo": "panel", "x": x, "y": y, "w": w, "h": h, "t": 0}
def titulo(txt, **k): return {"tipo": "texto", "texto": txt, "x": 1010, "y": 200, "tam": 76, "papel": True, **({"t": 0.2} if not k else k)}
def txt(contenido, x, y, tam=60, **k): return {"tipo": "texto", "texto": contenido, "x": x, "y": y, "tam": tam, **k}
def mano(contenido, x, y, tam=56, **k): return txt(contenido, x, y, tam, fuente="mano", **k)
def cifra(n, x, y, tam=170, **k): return {"tipo": "cifra", "hasta": n, "x": x, "y": y, "tam": tam, **k}
def masc(pose, x=1600, h=520, **k): return {"tipo": "mascota", "pose": pose, "x": x, "y": 1015, "h": h, **k}
def hud(v, cambios=()): return {"tipo": "hud", "valor": v, "cambios": [{"en": e, "valor": n} for e, n in cambios]}
def sello(contenido, x, y, tam=70, **k): return {"tipo": "sello", "texto": contenido, "x": x, "y": y, "tam": tam, **k}
def rect(x, y, w, h, color, **k): return {"tipo": "rect", "x": x, "y": y, "w": w, "h": h, "color": color, **k}
def camiseta(x, y, h, **k): return {"tipo": "imagen", "src": CAMISETA, "x": x, "y": y, "h": h, **k}
def precio(x, y, tam=30, **k): return txt("25,95 €", x, y, tam, color="#E0521B", **k)

def leyenda(filas, x=900, y0=300, paso=95):
    capas = []
    for i, (texto, color, en) in enumerate(filas):
        y = y0 + i * paso
        capas.append(rect(x, y - 28, 56, 56, color, en=en, dur=0.3))
        capas.append(txt(texto, x + 85, y, 50, ancla="izq", en=en, **({"color": "#E0521B"} if color == "#E0521B" else {})))
    return capas

E = []
def escena(id, desde, fondo, capas, **k):
    E.append({"id": id, "desde": desde, "fondo": fondo, "capas": capas, **k})

# ── GANCHO ─────────────────────────────────────────────
escena("01", "Pongamos que te compras", "tienda_ropa", [
    panel(90, 120, 1230, 870),
    camiseta(560, 470, 560, t=0.2), precio(560 + 205 * 560 / 620, 470 + 130 * 560 / 620, 28, t=0.6),
    mano("Hacienda", 250, 230, 60, papel=True, anim="pop", rot=-4, en="Se reparte entre Hacienda"),
    mano("una fábrica", 950, 230, 60, papel=True, anim="pop", rot=3, en="una fábrica en Marruecos"),
    mano("la cajera", 230, 820, 60, papel=True, anim="pop", rot=2, en="la persona que te cobra"),
    mano("el dueño del local", 900, 870, 56, papel=True, anim="pop", rot=-3, en="el dueño del local"),
    txt("≈ 9 M€ al día", 1000, 560, 80, color="#E0521B", anim="pop", rot=-6, en="casi nueve millones"),
    masc("sorprendido", 1620, 520, entra="der", t=0.3, poses=[{"en": "un señor de A Coruña", "pose": "lupa"}]),
], zoom=[1.0, 1.06], fuente="Ejemplo con una camiseta de 25,95 €")

escena("02", "Hoy vamos a abrir el ticket", "#FFF3C4", [
    txt("Hoy abrimos el ticket de tu ropa", 800, 250, 80),
    {"tipo": "bocadillo", "texto": "¿Vende ropa *barata*… y gana más que casi nadie?", "x": 780, "y": 560, "ancho": 900, "tam": 64, "piensa": True, "en": "cómo puede una empresa"},
    masc("pensativo", 1620, 520, entra="der", t=0.2),
])

# ── PRESENTACIONES ─────────────────────────────────────
escena("03", "Primero, las presentaciones", "calle_comercial", [
    panel(), txt("INDITEX", 700, 300, 170, anim="pop", en="Zara es la marca"),
    mano("8 marcas: Zara · Pull&Bear · Massimo Dutti ·\nBershka · Stradivarius · Oysho · Zara Home · Lefties", 700, 620, 50, en="entre ellas"),
    masc("saluda", 1620, 520, entra="der", t=0.2),
], zoom=[1.0, 1.06])

escena("04", "En su último año fiscal", "#F4E9D0", [
    cifra(39864, 620, 250, 150, sufijo=" M€", en="casi cuarenta mil"), mano("de ventas", 620, 370, 60, en="casi cuarenta mil"),
    txt("≈ 1.260 € cada segundo", 620, 480, 64, papel=True, en="mil doscientos sesenta"),
    cifra(6220, 620, 660, 150, sufijo=" M€", color="#E0521B", en="seis mil doscientos veinte"), mano("de beneficio", 620, 780, 60, en="seis mil doscientos veinte"),
    txt("≈ 200 € de beneficio por segundo", 620, 890, 60, papel=True, en="casi doscientos euros"),
    masc("sorprendido", 1600, 540, entra="der", en="casi cuarenta mil"),
], fuente="Inditex, resultados del ejercicio 2025 (cálculo propio por segundo)")

escena("05", "Tiene cinco mil cuatrocientas", "calle_comercial", [
    panel(),
    cifra(5460, 420, 300, 150, en="cinco mil cuatrocientas"), mano("tiendas", 420, 420, 60, en="cinco mil cuatrocientas"),
    cifra(214, 1000, 300, 150, en="doscientos catorce"), mano("mercados", 1000, 420, 60, en="doscientos catorce"),
    rect(160, 580, 1050, 120, "#D9D2C0", texto="todo el grupo", tam=44, en="siete de cada diez"),
    rect(160, 580, 735, 120, "#F5B301", texto="Zara + Zara Home + Lefties: 70 %", tam=44, en="siete de cada diez", dur=1.2),
    masc("senala", 1640, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.04, 1.1], fuente="Inditex, resultados del ejercicio 2025")

escena("06", "Todo empezó en 1975", "tienda_1975", [
    panel(90, 120, 1000, 870),
    txt("1975", 590, 290, 190, color="#E0521B", anim="pop", en="Todo empezó en 1975"),
    mano("Calle Juan Flórez, A Coruña", 590, 480, 64, papel=True, en="Juan Flórez"),
    sello("CERRÓ EN ENERO DE 2026", 590, 680, 64, en="esa primera tienda cerró"),
    mano("casi 51 años después", 590, 860, 56, en="casi cincuenta y un"),
    masc("sorprendido", 1500, 520, entra="der", en="esa primera tienda cerró"),
], zoom=[1.0, 1.08], fuente="EFE (30/01/2026)")

escena("07", "Detrás de todo está Amancio", "estudio_diseno", [
    panel(90, 120, 1230, 870),
    {"tipo": "tarta", "x": 480, "y": 560, "r": 280, "t": 0.1, "porciones": [
        {"v": 59.3, "color": "#E0521B", "t": 0.4, "lx": 590, "ly": 520, "etiqueta": "≈ 59 %\nAmancio\nOrtega", "tam": 50},
        {"v": 40.7, "color": "#D9D2C0", "t": 0.6, "lx": 330, "ly": 500, "etiqueta": "resto", "tam": 44}]},
    mano("Presidenta desde 2022:\nMarta Ortega", 1030, 560, 60, papel=True, en="Su hija Marta"),
    masc("lupa", 1640, 500, entra="der", t=0.2),
], zoom=[1.0, 1.05], fuente="Inditex, cuentas anuales consolidadas 2025 (nota 30)")

# ── EL VIAJE DE TU EURO ────────────────────────────────
escena("08", "Vamos a lo nuestro", "tienda_ropa", [
    panel(90, 170, 1230, 820), hud(100),
    camiseta(380, 560, 460, t=0.1), precio(380 + 205 * 460 / 620, 560 + 130 * 460 / 620, 22, t=0.3),
    txt("El aviso de siempre", 930, 300, 70, en="el aviso de siempre"),
    mano("Inditex no publica\nlo que cuesta cada prenda", 930, 480, 58, en="no publica lo que cuesta"),
    mano("Repartimos cada euro\ncon sus cuentas", 930, 680, 58, papel=True, en="Lo que sí publica"),
    txt("Es una media, no tu factura", 930, 880, 58, color="#E0521B", en="Es una media"),
    masc("senala", 1660, 470, mira="izq", entra="der", t=0.2),
], zoom=[1.02, 1.08])

escena("09", "Primera parada: Hacienda", "#E3E7EC", [
    hud(100, [("unos diecisiete céntimos", 83)]), titulo("PARADA 1: Hacienda (IVA)"),
    txt("IVA de la ropa: 21 %", 700, 430, 90, en="veintiuno por ciento"),
    {"tipo": "moneda", "texto": "17 c", "r": 110, "x": 700, "y": 700, "color": "#9CC5E8", "en": "unos diecisiete céntimos",
     "vuela": {"en": "Van directos al Estado", "x": 2150, "y": 400, "dur": 1.2, "arco": 200}},
    txt("¡ni siquiera son de Zara!", 700, 900, 64, color="#E0521B", anim="pop", rot=-3, en="ni siquiera son de Zara"),
    masc("encoge_hombros", 1600, 520, entra="der", t=0.2),
], fuente="IVA general del 21 % en España (cálculo propio)")

escena("10", "Segunda parada, y la más grande", "taller_costura", [
    panel(), hud(83, [("Unos treinta y cuatro", 48)]), titulo("PARADA 2: la prenda"),
    cifra(34, 700, 470, 260, sufijo=" c", color="#E0521B", en="Unos treinta y cuatro"),
    mano("para fabricarla y traerla", 700, 700, 64, papel=True, en="fabricarla y traerla"),
    masc("moneda", 1620, 520, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="Inditex, ejercicio 2025: coste de la mercancía 16.642 M€ (cálculo propio)")

escena("11", "Y aquí viene la primera sorpresa", "taller_costura", [
    panel(),
    cifra(6684, 700, 260, 160, en="seis mil seiscientas"), mano("fábricas en 49 países", 700, 390, 60, en="cuarenta y nueve"),
    mano("+3 millones de personas", 700, 490, 56, papel=True, en="tres millones"),
    sello("CASI NINGUNA ES SUYA", 700, 660, 72, en="casi ninguna es suya"),
    mano("solo unas pocas, cerca de Arteixo", 700, 800, 52, en="Solo unas pocas"),
    txt("6 de cada 10, en Asia", 700, 910, 64, color="#E0521B", en="seis de cada diez"),
    masc("sorprendido", 1620, 520, t=0, poses=[{"en": "El resto son proveedores", "pose": "lupa"}]),
], zoom=[1.06, 1.12], fuente="Inditex, Estado de información no financiera 2025")

escena("12", "Ahora fíjate en la cuenta", "#F4E9D0", [
    txt("Sin IVA:", 250, 250, 60, ancla="izq", en="Por cada euro"),
    rect(250, 360, 300, 130, "#9CC5E8", texto="le cuesta 1 €", tam=44, en="Por cada euro"),
    rect(250, 560, 720, 130, "#F5B301", texto="la vende por ≈ 2,40 €", tam=48, en="dos euros y cuarenta", dur=1.3),
    txt("Ahí empieza a verse la máquina", 700, 850, 70, color="#E0521B", anim="pop", rot=-3, en="Ahí empieza"),
    masc("pensativo", 1620, 520, entra="der", t=0.2),
], fuente="Inditex, ejercicio 2025: margen bruto del 58,3 %")

escena("13", "Tercera parada: la gente", "tienda_ropa", [
    panel(), hud(48, [("Unos doce céntimos", 36)]), titulo("PARADA 3: la plantilla"),
    cifra(12, 450, 450, 220, sufijo=" c", color="#E0521B", en="Unos doce céntimos"),
    cifra(163000, 950, 420, 130, en="ciento sesenta y tres"), mano("personas en plantilla", 950, 530, 56, en="ciento sesenta y tres"),
    mano("≈ 3 de cada 4, mujeres", 700, 720, 60, papel=True, en="tres de cada cuatro"),
    mano("la inmensa mayoría, en tiendas", 700, 860, 56, en="la inmensa mayoría"),
    masc("contento", 1640, 500, entra="der", t=0.2),
], zoom=[1.04, 1.1], fuente="Inditex, cuentas anuales consolidadas 2025")

escena("14", "Cuarta parada: el local", "calle_comercial", [
    panel(), hud(36, [("Unos seis céntimos", 30)]), titulo("PARADA 4: el local"),
    cifra(6, 400, 430, 220, sufijo=" c", color="#E0521B", en="Unos seis céntimos"),
    mano("las mejores calles del mundo", 900, 430, 54, papel=True, en="las mejores calles"),
    txt("670 M€ de alquiler según lo que vende", 700, 650, 56, en="seiscientos setenta"),
    mano("Algunos locales: de sociedades ligadas a Amancio Ortega", 700, 780, 48, papel=True, en="algunos de esos locales"),
    txt("¡se queda en casa!", 700, 900, 72, color="#E0521B", anim="pop", rot=-4, en="Así que, a veces"),
    masc("normal", 1640, 500, entra="der", t=0.2, poses=[{"en": "Así que, a veces", "pose": "riendo"}]),
], zoom=[1.0, 1.06], fuente="Inditex, cuentas anuales consolidadas 2025 (notas 16 y 30)")

escena("15", "Quinta parada: la máquina", "centro_logistico", [
    panel(), hud(30, [("Y otros tres o cuatro", 16)]), titulo("PARADA 5: la máquina"),
    mano("Transporte", 330, 380, 64, papel=True, anim="pop", rot=-3, en="el transporte"),
    mano("Tarjetas", 700, 370, 64, papel=True, anim="pop", rot=2, en="las comisiones"),
    mano("Tienda online: +1 de cada 4 €", 1000, 470, 54, papel=True, anim="pop", rot=-2, en="más de uno de cada cuatro"),
    mano("Luz y mantenimiento", 400, 560, 60, papel=True, anim="pop", rot=3, en="la luz"),
    mano("Inversiones: tiendas, almacenes, tecnología", 700, 700, 54, papel=True, anim="pop", rot=-2, en="el desgaste"),
    txt("Plan logístico: 900 M€ + 900 M€", 700, 880, 62, color="#E0521B", en="novecientos millones"),
    masc("corriendo", 1640, 480, entra="der", t=0.1),
], zoom=[1.04, 1.1], fuente="Inditex, resultados y cuentas consolidadas 2025")

escena("16", "Sexta parada: Hacienda, otra vez", "#E3E7EC", [
    hud(16, [("Casi cuatro céntimos", 13)]), titulo("PARADA 6: Hacienda, otra vez"),
    mano("Impuesto sobre el beneficio", 700, 380, 64, papel=True, en="impuesto sobre el beneficio"),
    {"tipo": "moneda", "texto": "4 c", "r": 90, "x": 700, "y": 560, "color": "#9CC5E8", "en": "Casi cuatro céntimos"},
    txt("IVA + impuesto ≈ 21 c", 700, 740, 84, en="unos veintiún céntimos"),
    sello("MÁS DE LO QUE GANA ZARA", 700, 890, 60, en="Más de lo que gana"),
    masc("enfadado", 1600, 520, entra="der", t=0.2),
], fuente="Inditex, ejercicio 2025: impuesto 1.800 M€ (cálculo propio)")

escena("17", "Porque lo que queda, al final", "#FFF3C4", [
    hud(13),
    {"tipo": "moneda", "texto": "13 c", "r": 170, "x": 500, "y": 450, "color": "#E0521B", "en": "trece céntimos de beneficio"},
    mano("de beneficio por cada euro", 500, 690, 60, en="trece céntimos de beneficio"),
    rect(880, 380, 390, 110, "#E0521B", texto="Zara: 13 c", tam=48, en="Mercadona se quedaba"),
    rect(880, 540, 120, 110, "#9CC5E8", texto="4 c", tam=44, en="Mercadona se quedaba"),
    mano("Mercadona", 1080, 595, 50, ancla="izq", en="Mercadona se quedaba"),
    masc("sorprendido", 1650, 480, entra="der", en="Mercadona se quedaba"),
], fuente="Inditex 2025 y Mercadona 2025 (cálculo propio)")

escena("18", "¿Y adónde van esos trece", "#F4E9D0", [
    txt("¿Adónde van los 13 céntimos?", 700, 150, 70, papel=True, t=0.1),
    {"tipo": "tarta", "x": 460, "y": 580, "r": 280, "t": 0.2, "porciones": [
        {"v": 52, "color": "#E0521B", "en": "casi siete céntimos"},
        {"v": 35, "color": "#F5B301", "en": "Casi once se reparten"},
        {"v": 13, "color": "#D9D2C0", "en": "Casi once se reparten"}]},
    *leyenda([("≈ 7 c · Amancio Ortega", "#E0521B", "casi siete céntimos"),
              ("≈ 4 c · otros accionistas", "#F5B301", "Casi once se reparten"),
              ("≈ 2 c · se queda en la empresa", "#D9D2C0", "Casi once se reparten")], x=860, y0=330, paso=100),
    cifra(3200, 1180, 740, 110, sufijo=" M€", prefijo="≈ ", color="#E0521B", en="tres mil doscientos"),
    txt("≈ 9 M€ al día", 1180, 880, 70, anim="pop", en="Casi nueve millones"),
    masc("sorprendido", 1750, 360, t=0.3),
], fuente="Inditex 2025: dividendo de 1,75 €/acción; Ortega, 59,29 % (cálculo propio)")

# ── EL TRUCO ───────────────────────────────────────────
escena("19", "Y ahora, la pregunta importante", "probadores", [
    panel(150, 250, 1050, 500),
    txt("¿Cómo lo hace?", 675, 420, 140, color="#E0521B", anim="pop", en="cómo lo hace"),
    mano("ropa barata + 13 c por euro ≠ lo normal", 675, 620, 56, en="Porque vender ropa barata"),
    masc("pensativo", 1580, 540, entra="der", t=0.2),
], zoom=[1.04, 1.1])

escena("20", "La primera pieza es que casi nunca", "tienda_ropa", [
    panel(), titulo("Pieza 1: casi nunca malvende"),
    cifra(0.57, 700, 440, 200, dec=2, sufijo=" %", color="#E0521B", en="cero coma cincuenta"),
    mano("de ropa sin vender (2024)", 700, 590, 60, en="cero coma cincuenta"),
    txt("< 1 prenda de cada 170", 700, 720, 70, papel=True, en="Menos de una prenda"),
    txt("Margen bruto: 58,3 %", 700, 880, 66, en="cincuenta y ocho por ciento"),
    masc("contento", 1640, 500, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="Inditex, Estado de información no financiera 2025; resultados 2025")

escena("21", "La segunda pieza es cómo fabrica", "taller_costura", [
    panel(), titulo("Pieza 2: cerca y en tandas cortas"),
    mano("España · Portugal · Marruecos · Turquía", 700, 400, 60, papel=True, en="en Portugal"),
    txt("Tandas cortas", 700, 560, 80, en="tandas cortas"),
    mano("¿Se vende? → se repone rápido", 700, 700, 58, en="Si algo se vende"),
    mano("¿No? → se deja de fabricar", 700, 820, 58, en="se deja de fabricar"),
    masc("lupa", 1640, 500, entra="der", t=0.2),
], zoom=[1.04, 1.1], fuente="Inditex, Estado de información no financiera 2025")

escena("22", "Seguro que has oído", "estudio_diseno", [
    panel(),
    txt("«De la idea a la tienda en 2 semanas»", 700, 250, 58, papel=True, en="Seguro que has oído"),
    sello("VERDAD A MEDIAS", 700, 420, 80, en="verdad a medias"),
    mano("Harvard, 2003: reponer o retocar → 2 semanas", 700, 590, 54, en="eso valía para reponer"),
    mano("Diseño nuevo → 4 o 5 semanas", 700, 710, 60, en="Un diseño totalmente nuevo"),
    txt("Resto del sector: meses", 700, 860, 70, color="#E0521B", en="podían pasar meses"),
    masc("pensativo", 1640, 500, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="Ghemawat y Nueno, «ZARA: Fast Fashion», Harvard Business School (2003)")

escena("23", "La tercera pieza es la logística", "centro_logistico", [
    panel(), titulo("Pieza 3: la logística"),
    txt("Casi todo pasa por España", 700, 420, 76, en="se centraliza en España"),
    txt("2 envíos por semana", 700, 580, 90, color="#E0521B", anim="pop", en="dos veces por semana"),
    mano("poco y a menudo = siempre hay algo nuevo", 700, 760, 56, papel=True, en="poco y a menudo"),
    masc("corriendo", 300, 470, entra="izq", t=0, camina=[{"en": "dos veces por semana", "x": 1640, "dur": 2.5}]),
], zoom=[1.06, 1.12], fuente="Prensa especializada (WWD/Sourcing Journal, 2023)")

escena("24", "La cuarta pieza son las tiendas", "calle_comercial", [
    panel(), titulo("Pieza 4: menos tiendas, más grandes"),
    rect(300, 330, 250, 560, "#D9D2C0", crece="arriba", texto="7.469", tam=56, en="dos mil tiendas menos"),
    txt("2019", 425, 940, 52, en="dos mil tiendas menos"),
    rect(650, 480, 250, 410, "#F5B301", crece="arriba", texto="5.460", tam=56, en="dos mil tiendas menos"),
    txt("2025", 775, 940, 52, en="dos mil tiendas menos"),
    txt("ventas: +41 %", 1100, 500, 90, color="#E0521B", anim="pop", rot=-4, en="cuarenta y uno por ciento"),
    masc("senala", 1660, 470, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="Inditex, resultados 2019 y 2025 (cálculo propio)")

escena("25", "Y la quinta pieza te sonará", "#F4E9D0", [
    titulo("Pieza 5: cobra antes de pagar", y=180),
    mano("Tú pagas al momento…", 600, 380, 64, en="Tú pagas la camiseta"),
    mano("…muchos proveedores cobran después", 700, 490, 60, en="muchos proveedores"),
    cifra(10958, 700, 690, 170, sufijo=" M€", color="#E0521B", en="casi once mil millones"), mano("en caja", 700, 820, 60, en="casi once mil millones"),
    sello("DEUDA ≈ 0", 1250, 680, 70, en="prácticamente nada"),
    masc("riendo", 1680, 460, entra="der", t=0.2),
], fuente="Inditex, resultados 2025: caja neta y fondo de maniobra")

# ── LA OTRA CARA ───────────────────────────────────────
escena("26", "Ahora bien, esta historia", "taller_costura", [
    panel(), titulo("La otra cara (1): las fábricas"),
    txt("+10.000 auditorías en 2025", 700, 420, 76, en="diez mil auditorías"),
    mano("406 fábricas (6 %) con un plan para corregir problemas", 700, 570, 52, papel=True, en="cuatrocientas seis"),
    {"tipo": "bocadillo", "texto": "Una auditoría *no garantiza* un salario digno", "x": 700, "y": 780, "ancho": 900, "tam": 56, "en": "una auditoría no garantiza"},
    masc("preocupado", 1640, 500, entra="der", t=0.2),
], zoom=[1.0, 1.05], fuente="Inditex, Estado de información no financiera 2025")

escena("27", "Y hay un nombre que sigue pesando", "#E6E0F5", [
    txt("Rana Plaza · Bangladés · 2013", 700, 250, 70, papel=True, en="Rana Plaza"),
    txt("más de 1.100 muertos", 700, 420, 80, color="#E0521B", en="más de mil cien"),
    mano("Inditex: no tenía talleres allí", 700, 600, 60, en="Inditex dijo"),
    mano("Aportó al fondo para las víctimas y firmó\nel acuerdo de seguridad de los edificios", 700, 790, 52, papel=True, en="aportó dinero"),
    masc("preocupado", 1640, 500, t=0.2),
], fuente="eldiario.es (2014); Clean Clothes Campaign (2015); BHRRC (2013)")

escena("28", "La segunda cara son los precios", "tienda_ropa", [
    panel(), titulo("La otra cara (2): los precios"),
    cifra(22, 600, 470, 220, prefijo="+", sufijo=" %", color="#E0521B", en="veintidós por ciento"),
    mano("de media en Europa desde 2020\n(Bloomberg, vía prensa)", 600, 680, 52, en="veintidós por ciento"),
    txt("Margen bruto: 55,9 % → 58,3 %", 700, 870, 64, papel=True, en="no ha dejado de crecer"),
    masc("pensativo", 1640, 500, entra="der", t=0.2),
], zoom=[1.04, 1.1], fuente="Consumidor Global (2025), citando a Bloomberg; Inditex 2019 y 2025")

escena("29", "La tercera son los impuestos", "#E3E7EC", [
    titulo("La otra cara (3): los impuestos", y=160),
    mano("2016 · Los Verdes (Parlamento Europeo):", 620, 290, 52, en="En 2016"),
    cifra(585, 620, 420, 130, prefijo="≥ ", sufijo=" M€", color="#E0521B", en="quinientos ochenta y cinco"),
    mano("2011–2014 → Países Bajos, Irlanda, Suiza", 620, 540, 52, en="llevando beneficios"),
    mano("Inditex: «premisas erróneas»", 620, 650, 56, papel=True, en="Inditex respondió"),
    rect(250, 760, 520, 90, "#F5B301", texto="España: 26 % de sus impuestos", tam=38, en="paga en España"),
    rect(250, 870, 320, 90, "#9CC5E8", texto="16 % de sus ventas", tam=38, en="dieciséis por ciento"),
    masc("pensativo", 1640, 500, entra="der", t=0.2),
], fuente="Greens/EFA «Tax Shopping» (2016); Inditex, informe 2025")

escena("30", "¿Y Shein, la gran amenaza?", "#F4E9D0", [
    txt("¿Y Shein?", 620, 180, 100, anim="pop", t=0.1),
    mano("Ventas", 250, 320, 50, ancla="izq", en="vendió casi lo mismo"),
    rect(250, 360, 700, 90, "#F5B301", texto="Inditex ≈ 40.000 M€", tam=40, en="vendió casi lo mismo"),
    rect(250, 470, 650, 90, "#9CC5E8", texto="Shein ≈ 41.800 M$", tam=40, en="vendió casi lo mismo"),
    mano("Beneficio", 250, 620, 50, ancla="izq", en="tres veces menos"),
    rect(250, 660, 700, 90, "#F5B301", texto="Inditex: 6.220 M€", tam=40, en="tres veces menos"),
    rect(250, 770, 215, 90, "#9CC5E8", texto="Shein ≈ 2.060 M$", tam=30, en="tres veces menos"),
    txt("vender barato es fácil…", 1200, 780, 58, en="Vender barato es fácil"),
    txt("…ganar dinero, no tanto", 1200, 890, 64, color="#E0521B", anim="pop", en="Ganar dinero vendiendo"),
    masc("riendo", 1720, 420, entra="der", t=0.2),
], fuente="Inditex 2025; Shein, folleto de salida a bolsa (2026), vía prensa; tipo de cambio aproximado")

# ── RESUMEN Y CIERRE ───────────────────────────────────
escena("31", "Así que, la próxima vez", "#FFF3C4", [
    txt("El viaje de tus 25,95 €", 960, 110, 72, papel=True, t=0.2),
    {"tipo": "tarta", "x": 470, "y": 590, "r": 300, "t": 0.5, "porciones": [
        {"v": 17.4, "color": "#9CC5E8", "en": "Unos cuatro euros y medio"},
        {"v": 34.5, "color": "#F5B301", "en": "Casi nueve"},
        {"v": 12.3, "color": "#8FD18F", "en": "Unos tres, para la plantilla"},
        {"v": 6.0, "color": "#C9B8E8", "en": "Un euro y medio"},
        {"v": 13.8, "color": "#F7DCC8", "en": "Unos tres y medio"},
        {"v": 3.7, "color": "#9CC5E8", "en": "Un euro, para Hacienda"},
        {"v": 12.3, "color": "#E0521B", "en": "algo más de tres euros"}]},
    *leyenda([("≈ 4,50 € · Hacienda (IVA)", "#9CC5E8", "Unos cuatro euros y medio"),
              ("≈ 9 € · fabricarla y traerla", "#F5B301", "Casi nueve"),
              ("≈ 3 € · plantilla", "#8FD18F", "Unos tres, para la plantilla"),
              ("≈ 1,50 € · alquiler", "#C9B8E8", "Un euro y medio"),
              ("≈ 3,50 € · transporte, tarjetas, tiendas", "#F7DCC8", "Unos tres y medio"),
              ("≈ 1 € · Hacienda otra vez", "#9CC5E8", "Un euro, para Hacienda"),
              ("≈ 3,30 € · beneficio (≈ 1,75 € para Ortega)", "#E0521B", "algo más de tres euros")], x=840, y0=240, paso=100),
], fuente="Cálculo propio con la cuenta de resultados de Inditex 2025 (media del grupo, IVA de España)")

escena("32", "El secreto de Zara no es", "tienda_ropa", [
    panel(150, 200, 1150, 720),
    mano("No es vender ropa barata…", 725, 330, 70, t=0.2),
    txt("…es venderla casi toda,", 725, 500, 76, en="Es vender casi todo"),
    txt("al precio que decide,", 725, 640, 76, en="al precio que ha decidido"),
    txt("y cobrarla antes de pagarla", 725, 790, 76, color="#E0521B", anim="pop", rot=-2, en="y cobrarlo antes"),
    masc("riendo", 1650, 500, entra="der", t=0.1),
], zoom=[1.04, 1.12])

escena("33", "Aquí, cada semana, abrimos", "#F5B301", [
    masc("saluda", 960, 560, entra="abajo", t=0.2),
    txt("TICKET MEDIO", 960, 170, 150, anim="pop", t=0.3),
    mano("Cada semana, el ticket de algo que pagas todos los días", 960, 300, 50, papel=True, t=1.0),
], sin_marca=True)

cfg = {"musica": "audio/musica.mp3", "musica_db": -26, "cola": 3, "escenas": E}
json.dump(cfg, open(os.path.join(V, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("escenas:", len(E))
