"""Genera escenas_v2.json del vídeo 5 (Lidl). Se deja en la carpeta para poder retocarlo y volver a generarlo.
Datos: INVESTIGACION.md (comunicado de Lidl España del 30/9/2026, web corporativa, Kantar, OCU y Memoria de Mercadona)."""
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

LIDL = "Comunicado de resultados de Lidl España (30/9/2026; ejercicio 2025, de marzo de 2025 a febrero de 2026)"

# ── GANCHO ─────────────────────────────────────────────
escena("01", "Lidl vendió en España", "supermercado", [
    panel(90, 120, 1230, 870),
    mano("VENDIÓ en España", 700, 230, 60, t=0.2),
    cifra(7641, 700, 380, 150, sufijo=" M€", en="siete mil seiscientos cuarenta y un millones"),
    mano("pero COMPRÓ producto español por…", 700, 560, 58, en="compró producto español"),
    cifra(8400, 700, 720, 150, sufijo=" M€", color="#E0521B", en="ocho mil cuatrocientos millones"),
    sello("MÁS DE LO QUE VENDIÓ", 700, 900, 54, en="Más de lo que vendió"),
    masc("sorprendido", 1620, 520, entra="der", t=0.3),
], zoom=[1.0, 1.06], fuente=LIDL)

escena("02", "Hoy vamos a abrir el ticket", "#FFF3C4", [
    txt("¿Cómo se compra más\nde lo que se vende?", 800, 250, 76, t=0.2),
    mano("Hoy abrimos el ticket de Lidl", 800, 470, 60, en="el ticket de Lidl"),
    {"tipo": "bocadillo", "texto": "No es magia: es un sistema *alemán*", "x": 780, "y": 700, "ancho": 900, "tam": 66, "piensa": True, "en": "no tiene nada de magia"},
    masc("pensativo", 1620, 520, entra="der", t=0.2),
])

# ── PRESENTACIONES ─────────────────────────────────────
escena("03", "Lidl es una cadena alemana", "fachada", [
    panel(),
    mano("Lidl · cadena alemana", 700, 230, 62, t=0.2),
    txt("1930", 380, 380, 120, color="#E0521B", en="mil novecientos treinta"), mano("su historia, según su web", 380, 490, 44, en="mil novecientos treinta"),
    txt("1994", 1000, 380, 120, color="#E0521B", en="mil novecientos noventa y cuatro"), mano("llega a España", 1000, 490, 44, en="mil novecientos noventa y cuatro"),
    cifra(730, 330, 700, 130, prefijo="+", en="más de setecientas treinta tiendas"), mano("tiendas", 330, 790, 44, en="más de setecientas treinta tiendas"),
    cifra(14, 700, 700, 130, en="catorce plataformas"), mano("plataformas\nlogísticas", 700, 810, 44, en="catorce plataformas"),
    cifra(20000, 1070, 700, 130, prefijo="+", en="catorce plataformas", t=1.0), mano("empleados", 1070, 790, 44, en="catorce plataformas", t=1.2),
    masc("saluda", 1620, 520, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="Lidl España, empresa.lidl.es y comunicado de resultados (30/9/2026)")

escena("04", "Está presente en más de treinta", "#E6E0F5", [
    cifra(30, 560, 330, 200, prefijo="+", t=0.2), mano("países", 560, 480, 60, t=0.3),
    cifra(12900, 1100, 330, 160, en="doce mil novecientas tiendas"), mano("tiendas en total", 1100, 470, 54, en="doce mil novecientas tiendas"),
    sello("GRUPO SCHWARZ", 800, 700, 80, en="Grupo Schwarz"),
    mano("Lidl España es filial de la alemana Lidl Stiftung", 800, 880, 48, papel=True, en="Grupo Schwarz"),
    masc("normal", 1650, 480, entra="der", t=0.2),
], fuente="Lidl España, empresa.lidl.es/sobre-lidl")

escena("05", "vendió siete mil seiscientos cuarenta", "supermercado", [
    panel(),
    mano("Ventas netas del último año", 700, 230, 60, t=0.2),
    cifra(7641, 700, 400, 170, sufijo=" M€", en="siete mil seiscientos cuarenta y un millones"),
    txt("+10 %", 700, 590, 100, color="#2E8B57", anim="pop", en="Un diez por ciento más"),
    mano("≈ 242 € cada segundo", 700, 800, 64, papel=True, en="Un diez por ciento más"),
    masc("sorprendido", 1620, 520, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=LIDL + " (cálculo propio por segundo)")

escena("06", "De cada euro que gastas en Lidl", "#F4E9D0", [
    mano("De cada euro que gastas en Lidl…", 800, 220, 62, t=0.2),
    moneda("1 €", 420, 520, 170, t=0.4),
    txt("→", 720, 520, 120, en="la empresa se queda"),
    moneda("3,6 c", 1040, 520, 130, color="#E0521B", en="tres céntimos y medio"),
    mano("de beneficio: 274 millones en total", 800, 820, 60, papel=True, en="doscientos setenta y cuatro millones"),
    masc("moneda", 1650, 480, entra="der", t=0.2),
], fuente=LIDL + " (beneficio 274 M€ sobre 7.641 M€ = 3,6 c; cálculo propio)")

escena("07", "Para ponerlo en perspectiva", "#E3E7EC", [
    mano("Beneficio por cada euro vendido", 800, 190, 58, papel=True, t=0.2),
    mano("Mercadona", 220, 390, 54, ancla="izq", en="Mercadona, el líder"),
    rect(220, 440, 880, 110, "#F5B301", texto="≈ 4,1 c", tam=56, en="cuatro céntimos por euro", dur=1.2),
    mano("Lidl", 220, 650, 54, ancla="izq", en="cuatro céntimos por euro"),
    rect(220, 700, 770, 110, "#E0521B", texto="≈ 3,6 c", tam=56, en="Mercadona, el líder", dur=1.2, t=1.0),
    txt("Pero Mercadona vende 5,5 veces más", 700, 910, 56, color="#E0521B", en="unos cuatro céntimos por euro"),
    masc("lupa", 1650, 500, entra="der", t=0.2),
], fuente="Lidl: comunicado 30/9/2026 · Mercadona: Memoria Anual 2025 (41.858 M€; 4,1 c, cálculo propio). Ejercicios distintos")

escena("08", "Según Kantar", "#FFF3C4", [
    txt("¿Quién se lleva tu gasto en el súper?", 960, 130, 60, papel=True, t=0.2),
    {"tipo": "tarta", "x": 470, "y": 590, "r": 300, "t": 0.3, "porciones": [
        {"v": 27.2, "color": "#F5B301", "en": "veintisiete van a Mercadona"},
        {"v": 7.3, "color": "#E0521B", "en": "siete a Lidl"},
        {"v": 9.0, "color": "#9CC5E8", "en": "siete a Lidl"},
        {"v": 56.5, "color": "#D9D2C0", "en": "siete a Lidl"}]},
    *leyenda([("27,2 % · Mercadona", "#F5B301", "veintisiete van a Mercadona"),
              ("7,3 % · Lidl (+0,5)", "#E0521B", "siete a Lidl"),
              ("9,0 % · Carrefour", "#9CC5E8", "siete a Lidl"),
              ("resto de cadenas", "#D9D2C0", "siete a Lidl")], x=850, y0=360, paso=100, tam=48),
    mano("1.er trimestre de 2026", 1210, 880, 50, en="en el primer trimestre"),
], fuente="Kantar, primer trimestre de 2026 (vía El Español, 20/4/2026)")

escena("09", "Para que te hagas una idea", "#E3E7EC", [
    mano("Cuota de Lidl en España", 800, 190, 58, papel=True, t=0.2),
    txt("2,3 %", 360, 480, 120, en="dos coma tres por ciento"), mano("hace 20 años", 360, 590, 50, en="hace veinte años"),
    txt("4,8 %", 800, 480, 120, en="el cuatro coma ocho"), mano("2020", 800, 590, 50, en="En dos mil veinte"),
    txt("7,3 %", 1240, 480, 140, color="#E0521B", anim="pop", en="el siete coma tres"), mano("hoy", 1240, 600, 50, en="el siete coma tres"),
    mano("Es la que más sube", 800, 860, 62, papel=True, en="Lidl es la que más sube"),
    masc("riendo", 1650, 500, entra="der", t=0.2),
], fuente="Kantar (vía El Español, 20/4/2026)")

escena("10", "Y aquí viene lo curioso", "oficina_financiera", [
    panel(),
    mano("OCU · estudio de supermercados 2026", 700, 220, 58, t=0.2),
    txt("Lidl, la más barata en…", 700, 340, 60, en="La OCU acaba de publicar"),
    cifra(60, 440, 550, 180, en="sesenta de las localidades"), mano("localidades este año", 440, 680, 46, en="sesenta de las localidades"),
    cifra(18, 1000, 550, 180, color="#9A9A9A", en="eran dieciocho"), mano("el año anterior", 1000, 680, 46, en="eran dieciocho"),
    txt("690 tiendas · 38 ciudades · 244 productos", 700, 830, 50, papel=True, en="seiscientos noventa establecimientos"),
    masc("sorprendido", 1620, 520, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="OCU, estudio de supermercados 2026 (25/9/2026)")

escena("11", "Entre el súper más barato", "#F4E9D0", [
    mano("Entre el súper más barato y el más caro de tu ciudad…", 800, 220, 54, t=0.2),
    cifra(1310, 800, 520, 200, sufijo=" €", color="#2E8B57", en="mil trescientos diez euros"),
    mano("de ahorro medio al año", 800, 700, 62, en="el ahorro medio"),
    masc("moneda", 1640, 500, entra="der", t=0.2),
], fuente="OCU, estudio de supermercados 2026 (25/9/2026)")

# ── LOS TRES TRUCOS ────────────────────────────────────
escena("12", "¿Cómo lo hace?", "#FFF3C4", [
    txt("¿Cómo lo hace?", 800, 300, 110, t=0.2),
    mano("Tres trucos, con lo que dice la propia empresa", 800, 520, 60, papel=True, en="tres trucos"),
    masc("pensativo", 1620, 520, entra="der", t=0.2),
])

escena("13", "El primer truco", "supermercado", [
    panel(), titulo("TRUCO 1: pocas cosas"),
    cifra(3200, 440, 420, 150, en="tres mil doscientas referencias"), mano("referencias en Lidl", 440, 540, 46, en="tres mil doscientas referencias"),
    txt("> 80 % marca propia", 440, 700, 56, color="#E0521B", en="ochenta por ciento"),
    cifra(8000, 1000, 420, 150, color="#9A9A9A", en="ochenta por ciento"), mano("en Mercadona", 1000, 540, 46, en="ochenta por ciento"),
    masc("senala", 1650, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="Lidl España (empresa.lidl.es, modelo de negocio) · Mercadona, Memoria Anual 2025")

escena("14", "¿Por qué importa?", "#E6E0F5", [
    mano("Menos productos…", 800, 250, 66, t=0.2),
    txt("más demanda por producto", 800, 400, 64, en="junta más demanda"),
    txt("mejor precio de compra", 800, 540, 64, color="#2E8B57", en="mejores precios"),
    sello("COMPRAS ENORMES", 800, 760, 70, en="Menos productos, pero comprados"),
    masc("normal", 1650, 480, entra="der", t=0.2),
], fuente="Lidl España (empresa.lidl.es, modelo de negocio)")

escena("15", "Y hay otra consecuencia", "fachada", [
    panel(), mano("Ventas medias por tienda y año", 700, 200, 56, papel=True, t=0.2),
    mano("Mercadona", 220, 360, 54, ancla="izq", en="una tienda de Mercadona"),
    rect(220, 410, 940, 110, "#F5B301", texto="≈ 25 M€", tam=56, en="veinticinco millones", dur=1.2),
    mano("Lidl", 220, 600, 54, ancla="izq", en="Una de Lidl"),
    rect(220, 650, 400, 110, "#E0521B", texto="≈ 10,5 M€", tam=56, en="diez millones y medio", dur=1.2),
    txt("Menos donde elegir", 700, 880, 62, color="#E0521B", anim="pop", rot=-2, en="menos donde elegir"),
    masc("encoge_hombros", 1650, 500, entra="der", t=0.2),
], fuente="Cálculo propio: ventas / tiendas (Lidl 7.641 M€ / 730; Mercadona 41.858 M€ / 1.672). Ejercicios distintos")

escena("16", "El segundo truco", "puerto_avion", [
    panel(), titulo("TRUCO 2: comprar para todos"),
    txt("Compra en España…", 700, 400, 70, en="no solo para sus tiendas españolas"),
    txt("…para +30 países", 700, 560, 80, color="#E0521B", anim="pop", en="los más de treinta países"),
    mano("Así junta una demanda gigante", 700, 780, 58, papel=True, en="demanda gigante"),
    masc("senala", 1640, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="Lidl España (empresa.lidl.es, modelo de negocio)")

escena("17", "Mira lo que eso significa", "centro_logistico", [
    panel(), mano("Compras de producto español en 2025", 700, 200, 54, papel=True, t=0.2),
    rect(150, 330, 1100, 130, "#9CC5E8", texto="8.400 M€ · más de 800 proveedores", tam=50, en="a más de ochocientos proveedores", dur=0.8, t=0.5),
    rect(150, 560, 556, 150, "#E0521B", texto="4.255 M€ exportados", tam=44, en="cuatro mil doscientos cincuenta y cinco", dur=1.0),
    rect(706, 560, 544, 150, "#F5B301", texto="4.145 M€ para España*", tam=44, en="más de la mitad", dur=1.0),
    txt("Más de la mitad se vende fuera", 700, 840, 62, color="#E0521B", anim="pop", rot=-2, en="más de la mitad"),
    mano("*cálculo propio: 8.400 − 4.255", 700, 930, 36, en="más de la mitad"),
    masc("sorprendido", 1650, 500, entra="der", t=0.2),
], fuente=LIDL + " (exportaciones «a una treintena de países europeos»)")

escena("18", "España no es solo un mercado", "puerto_avion", [
    sello("ESPAÑA = LA DESPENSA DE LIDL EN EUROPA", 960, 440, 70, t=0.3),
    mano("Compra en España y vende en\nuna treintena de países europeos", 960, 640, 54, papel=True, en="España no es solo un mercado"),
    masc("saluda", 1650, 500, entra="der", t=0.2),
], zoom=[1.0, 1.08])

escena("19", "Se nota sobre todo en la fruta", "#E8F3E0", [
    mano("Fruta y verdura", 700, 200, 70, papel=True, t=0.2),
    cifra(2, 380, 420, 190, sufijo=" M t", prefijo="+", en="más de dos millones de toneladas"), mano("compradas", 380, 570, 50, en="más de dos millones de toneladas"),
    cifra(81, 1000, 420, 190, sufijo=" %", color="#E0521B", en="El ochenta y un por ciento"), mano("a otros mercados europeos", 1000, 570, 46, en="otros mercados europeos"),
    txt("2026, previsión: 9.400 M€ de compras", 700, 820, 56, papel=True, en="Y para este año"),
    masc("carrito", 1650, 500, entra="der", t=0.2),
], fuente="Lidl España, comunicado 30/9/2026 (vía FreshPlaza)")

escena("20", "Así que, cuando dices", "#FFF3C4", [
    txt("La frase exacta:", 800, 220, 62, t=0.2),
    txt("Compra en España\nmás de lo que vende\nen España", 800, 440, 70, color="#E0521B", en="la frase exacta es esta"),
    mano("…porque compra para media Europa", 800, 760, 58, papel=True, en="porque compra para media Europa"),
    masc("lupa", 1640, 500, entra="der", t=0.2),
])

escena("21", "El tercer truco", "centro_logistico", [
    panel(), titulo("TRUCO 3: gastar lo mínimo"),
    mano("Eliminar todo lo que el cliente no nota", 700, 400, 58, en="todo lo que no aporte nada"),
    txt("Productos en palés", 700, 530, 70, en="en palés"),
    cifra(14, 380, 760, 120, en="catorce plataformas"), mano("plataformas", 380, 850, 44, en="catorce plataformas"),
    cifra(140, 850, 760, 120, sufijo=" M€", en="ciento cuarenta millones"), mano("Martorell (Barcelona)", 850, 850, 44, en="Martorell"),
    cifra(130, 1180, 760, 120, prefijo="+", en="más de ciento treinta tiendas"), mano("tiendas servidas", 1180, 850, 44, en="más de ciento treinta tiendas"),
    masc("senala", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="Lidl España (empresa.lidl.es) y comunicado 30/9/2026")

escena("22", "Y detrás hay personas", "oficina_financiera", [
    panel(), titulo("Las personas"),
    cifra(1200, 450, 450, 150, prefijo="+", en="más de mil doscientos empleos"), mano("empleos creados en 2025", 450, 570, 46, en="más de mil doscientos empleos"),
    cifra(94, 1000, 450, 150, sufijo=" %", en="el noventa y cuatro por ciento"), mano("contrato indefinido", 1000, 570, 46, en="contrato indefinido"),
    txt("Convenio: > 280 M€ en 4 años", 700, 790, 58, papel=True, en="Y que su convenio"),
    mano("según la empresa", 700, 900, 44, en="Y que su convenio"),
    masc("contento", 1650, 500, entra="der", t=0.2),
], fuente="Lidl España, comunicado 30/9/2026 (datos de la empresa)")

escena("23", "Tampoco es barato crecer", "fachada", [
    panel(), titulo("Inversión"),
    cifra(320, 440, 440, 150, sufijo=" M€", en="trescientos veinte millones"), mano("2025: ≈ 50 tiendas\nabiertas o reformadas", 440, 600, 46, en="trescientos veinte millones"),
    cifra(440, 1000, 440, 150, prefijo="+", sufijo=" M€", color="#E0521B", en="cuatrocientos cuarenta millones"), mano("2026: >60 actuaciones,\n≈ 50 tiendas nuevas", 1000, 600, 46, en="cuatrocientos cuarenta millones"),
    masc("corriendo", 1650, 500, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="Lidl España, comunicado 30/9/2026")

escena("24", "Y la empresa dice que su contribución", "oficina_financiera", [
    panel(), titulo("Impuestos"),
    cifra(643, 700, 430, 180, sufijo=" M€", en="seiscientos cuarenta y tres millones"), mano("contribución tributaria 2025", 700, 580, 50, en="contribución tributaria"),
    txt("≈ 8,4 c por euro de ventas", 700, 760, 66, color="#E0521B", anim="pop", en="ocho céntimos y medio"),
    mano("Ojo: incluye impuestos que recauda para el Estado", 700, 890, 44, papel=True, en="incluye impuestos que recauda"),
    masc("encoge_hombros", 1650, 500, entra="der", t=0.2),
], fuente="Lidl España, comunicado 30/9/2026 (643 M€ / 7.641 M€ = 8,4 c; cálculo propio)")

# ── LO QUE NO SABEMOS ──────────────────────────────────
escena("25", "Ahora, la parte que Lidl no cuenta", "#E3E7EC", [
    sello("LO QUE NO SABEMOS", 800, 260, 80, t=0.2),
    mano("Lidl no publica una memoria anual\ncon el reparto de cada euro", 800, 470, 56, en="no publica una memoria anual"),
    mano("Sueldos · alquileres · logística: sin desglose", 800, 700, 54, papel=True, en="cuánto va a sueldos"),
    masc("preocupado", 1640, 500, entra="der", t=0.2),
])

escena("26", "También hay que ser prudente", "#F4E9D0", [
    mano("La OCU dice…", 800, 200, 62, t=0.2),
    txt("Lidl: la más barata en 60 localidades", 800, 360, 60, en="sesenta localidades"),
    txt("No dice que lo sea en todas, ni siempre", 800, 520, 56, color="#E0521B", en="en todas, ni siempre"),
    mano("Cesta OCU:  Lidl −1,9 %  ·  Mercadona −1,8 %", 800, 720, 56, papel=True, en="la cesta de Mercadona"),
    masc("pensativo", 1640, 500, entra="der", t=0.2),
], fuente="OCU, estudio de supermercados 2026 (25/9/2026)")

# ── CIERRE ─────────────────────────────────────────────
escena("27", "Así que, la próxima vez", "supermercado", [
    panel(), titulo("El viaje de tu euro"),
    {"tipo": "tarta", "x": 420, "y": 640, "r": 260, "t": 0.3, "porciones": [
        {"v": 3.6, "color": "#E0521B", "en": "Tres céntimos y medio"},
        {"v": 8.4, "color": "#9CC5E8", "en": "Unos ocho y medio"},
        {"v": 88.0, "color": "#D9D2C0", "en": "el producto, la plantilla"}]},
    *leyenda([("3,6 c · beneficio", "#E0521B", "Tres céntimos y medio"),
              ("≈ 8,4 c · impuestos*", "#9CC5E8", "Unos ocho y medio"),
              ("resto: producto y gastos", "#D9D2C0", "el producto, la plantilla")], x=760, y0=440, paso=120, tam=46),
    masc("saluda", 1650, 500, entra="der", t=0.2),
], fuente="Lidl España, comunicado 30/9/2026 (cálculo propio sobre ventas netas; los impuestos incluyen los que recauda para el Estado)")

escena("28", "Lidl no gana dinero por vender caro", "#FFF3C4", [
    txt("Pocas cosas", 800, 240, 80, t=0.3, en="vender pocas cosas"),
    txt("Comprar para media Europa", 800, 400, 80, en="comprar para media Europa"),
    txt("Gastar lo mínimo en todo lo demás", 800, 560, 70, en="gastar lo mínimo"),
    txt("¿Y si todos empiezan a copiarle?", 800, 800, 66, color="#E0521B", anim="pop", rot=-2, en="empiecen a copiarle"),
    masc("pensativo", 1640, 500, entra="der", t=0.2),
])

escena("29", "Aquí, cada semana, abrimos", "#F5B301", [
    masc("saluda", 960, 560, entra="abajo", t=0.2),
    txt("TICKET MEDIO", 960, 170, 150, anim="pop", t=0.3),
    mano("Cada semana, el ticket de algo que pagas todos los días", 960, 300, 50, papel=True, t=1.0),
], sin_marca=True)

cfg = {"musica": "audio/musica.mp3", "musica_db": -26, "cola": 3, "escenas": E}
json.dump(cfg, open(os.path.join(V, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("escenas:", len(E))
