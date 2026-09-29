"""Genera escenas_v2.json del vídeo 4 (El Corte Inglés). Se deja en la carpeta para poder retocarlo y volver a generarlo.
Datos: INVESTIGACION.md (cuentas consolidadas del ejercicio 2025 y reparto propio de cada euro)."""
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
def moneda(texto, x, y, r=110, color="#F5B301", **k): return {"tipo": "moneda", "texto": texto, "r": r, "x": x, "y": y, "color": color, **k}

def leyenda(filas, x=900, y0=300, paso=95, tam=50):
    capas = []
    for i, (texto, color, en) in enumerate(filas):
        y = y0 + i * paso
        capas.append(rect(x, y - 28, 56, 56, color, en=en, dur=0.3))
        capas.append(txt(texto, x + 85, y, tam, ancla="izq", en=en, **({"color": "#E0521B"} if color == "#E0521B" else {})))
    return capas

E = []
def escena(id, desde, fondo, capas, **k):
    E.append({"id": id, "desde": desde, "fondo": fondo, "capas": capas, **k})

CUENTAS = "El Corte Inglés, cuentas anuales consolidadas del ejercicio 2025 (mar. 2025 – feb. 2026)"

# ── GANCHO ─────────────────────────────────────────────
escena("01", "De cada euro que te gastas", "fachada", [
    panel(90, 120, 1230, 870),
    moneda("1 €", 420, 460, 170, t=0.2),
    txt("→", 700, 460, 120, en="la empresa se queda"),
    moneda("3,5 c", 960, 460, 90, color="#E0521B", en="tres céntimos y medio"),
    mano("Hacienda (IVA): ×5", 700, 720, 70, papel=True, anim="pop", rot=-3, en="se lleva cinco veces"),
    sello("MEJOR AÑO EN MUCHO TIEMPO", 700, 880, 50, en="su mejor año"),
    masc("sorprendido", 1620, 520, entra="der", t=0.3, poses=[{"en": "Hacienda, solo con el IVA", "pose": "lupa"}]),
], zoom=[1.0, 1.06], fuente=CUENTAS + " (cálculo propio)")

escena("02", "Llevamos años oyendo", "#FFF3C4", [
    txt("«El Corte Inglés se hunde»", 800, 230, 76, t=0.2),
    txt("Hoy abrimos su ticket, con sus cuentas", 800, 380, 60, en="Hoy vamos a abrir"),
    {"tipo": "bocadillo", "texto": "Si gana tan poco… ¿*cómo sigue vivo*?", "x": 780, "y": 640, "ancho": 900, "tam": 66, "piensa": True, "en": "si gana tan poco"},
    masc("pensativo", 1620, 520, entra="der", t=0.2),
])

# ── PRESENTACIONES ─────────────────────────────────────
escena("03", "Primero, las presentaciones", "grandes_almacenes", [
    panel(),
    cifra(70, 380, 290, 170, en="setenta grandes almacenes"), mano("grandes almacenes\nen España (+2 en Portugal)", 380, 450, 46, en="setenta grandes almacenes"),
    cifra(34, 1000, 290, 170, en="treinta y cuatro"), mano("Hipercor", 1000, 420, 56, en="treinta y cuatro"),
    mano("+ supermercados · Sfera · ≈ 400 agencias de viajes", 700, 700, 50, papel=True, en="unas cuatrocientas"),
    masc("saluda", 1620, 520, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=CUENTAS + ", informe de gestión")

escena("04", "Trabajan allí ochenta", "agencia_viajes", [
    panel(),
    cifra(81830, 700, 250, 140, en="ochenta y un mil"), mano("personas", 700, 360, 60, en="ochenta y un mil"),
    cifra(14988, 700, 560, 140, sufijo=" M€", color="#E0521B", en="casi quince mil millones"), mano("facturados en su último año", 700, 670, 56, en="casi quince mil millones"),
    txt("≈ 475 € cada segundo", 700, 850, 66, papel=True, en="cuatrocientos setenta y cinco"),
    masc("sorprendido", 1620, 520, entra="der", en="ochenta y un mil"),
], fuente=CUENTAS + " (cálculo propio por segundo)")

escena("05", "Y aquí va el primer dato curioso", "#E6E0F5", [
    txt("¿De quién es?", 470, 130, 70, papel=True, t=0.2),
    {"tipo": "tarta", "x": 470, "y": 590, "r": 300, "t": 0.3, "porciones": [
        {"v": 40.04, "color": "#E0521B", "en": "la Fundación Ramón Areces"},
        {"v": 18.4, "color": "#F5B301", "en": "Otro dieciocho por ciento"},
        {"v": 8, "color": "#9CC5E8", "en": "Mutua Madrileña tiene"},
        {"v": 5.5, "color": "#8FD18F", "en": "Y un jeque de Catar"},
        {"v": 28.06, "color": "#D9D2C0", "en": "Y un jeque de Catar"}]},
    *leyenda([("40 % · Fundación Ramón Areces", "#E0521B", "la Fundación Ramón Areces"),
              ("18 % · hermanas Álvarez (IASA)", "#F5B301", "Otro dieciocho por ciento"),
              ("8 % · Mutua Madrileña", "#9CC5E8", "Mutua Madrileña tiene"),
              ("≈ 5,5 % · jeque de Catar (prensa)", "#8FD18F", "Y un jeque de Catar"),
              ("resto y acciones propias", "#D9D2C0", "Y un jeque de Catar")], x=850, y0=330, paso=95, tam=46),
    sello("NO COTIZA EN BOLSA", 1210, 880, 50, en="no cotiza en bolsa"),
], fuente=CUENTAS + " (nota 15); Mutua (2022); participación del jeque: prensa")

# ── EL VIAJE DE TU EURO ────────────────────────────────
escena("06", "Vamos a lo nuestro", "planta_electronica", [
    panel(90, 170, 1230, 820), hud(100),
    camiseta(380, 560, 460, t=0.1),
    txt("El aviso de siempre", 930, 300, 70, en="el aviso de siempre"),
    mano("No publica lo que\ncuesta cada producto", 930, 480, 58, en="no publica lo que cuesta"),
    mano("Repartimos cada euro\ncon sus cuentas", 930, 680, 58, papel=True, en="Lo que sí publica"),
    txt("Es una media, no tu factura", 930, 880, 56, color="#E0521B", en="Es una media"),
    masc("senala", 1660, 470, mira="izq", entra="der", t=0.2),
], zoom=[1.02, 1.08])

escena("07", "Primera parada: Hacienda", "#E3E7EC", [
    hud(100, [("unos diecisiete céntimos", 83)]), titulo("PARADA 1: Hacienda (IVA)"),
    txt("Ropa y electrónica: 21 %", 700, 410, 80, en="veintiuno por ciento"),
    moneda("17 c", 700, 640, 110, color="#9CC5E8", en="unos diecisiete céntimos",
           vuela={"en": "Van directos al Estado", "x": 2150, "y": 400, "dur": 1.2, "arco": 200}),
    mano("Comida: 10 % · pan, leche, fruta: 4 %", 700, 880, 54, papel=True, en="Si compras comida"),
    masc("encoge_hombros", 1600, 520, entra="der", t=0.2),
], fuente="AEAT, tipos de IVA 2025 (cálculo propio)")

escena("08", "Segunda parada, y la más grande", "planta_electronica", [
    panel(), hud(83, [("Cincuenta y cinco céntimos", 28)]), titulo("PARADA 2: el producto"),
    cifra(55, 700, 470, 260, sufijo=" c", color="#E0521B", en="Cincuenta y cinco céntimos"),
    mano("para quien lo fabrica o la marca que lo vende", 700, 700, 54, papel=True, en="a quien lo fabrica"),
    txt("más de la mitad de tu euro", 700, 860, 64, en="Más de la mitad"),
    masc("moneda", 1620, 520, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=CUENTAS + ": aprovisionamientos 9.896 M€ (cálculo propio)")

escena("09", "Y aquí está la primera clave", "#F4E9D0", [
    txt("Margen bruto: lo que le queda de lo que vende", 800, 150, 54, papel=True, t=0.2),
    mano("Zara fabrica lo suyo", 220, 330, 54, ancla="izq", en="fabrica su propia ropa"),
    rect(220, 380, 870, 110, "#F5B301", texto="Zara: 58 %", tam=50, en="fabrica su propia ropa", dur=1.2),
    mano("El Corte Inglés revende marcas de otros", 220, 600, 54, ancla="izq", en="revende sobre todo marcas"),
    rect(220, 650, 510, 110, "#9CC5E8", texto="El Corte Inglés: 34 %", tam=46, en="un treinta y cuatro por ciento", dur=1.2),
    txt("La diferencia está en la mercancía", 700, 900, 60, color="#E0521B", anim="pop", rot=-2, en="Zara se queda con"),
    masc("lupa", 1640, 500, entra="der", t=0.2),
], fuente=CUENTAS + " (margen bruto 34,0 %); Inditex, ejercicio 2025 (58,3 %)")

escena("10", "Tercera parada: la gente", "escaleras_mecanicas", [
    panel(), hud(28, [("Catorce céntimos", 14)]), titulo("PARADA 3: la plantilla"),
    cifra(14, 450, 470, 240, sufijo=" c", color="#E0521B", en="Catorce céntimos"),
    mano("sueldos y\nSeguridad Social", 450, 680, 54, en="Catorce céntimos"),
    txt("+80.000 personas", 950, 480, 80, en="más de ochenta mil"),
    mano("vendedores en cada planta", 950, 620, 54, papel=True, en="vendedores en cada planta"),
    masc("riendo", 1650, 500, entra="der", t=0.1),
], zoom=[1.04, 1.12], fuente=CUENTAS + ": gastos de personal 2.604 M€ (cálculo propio)")

escena("11", "Cuarta parada: el local", "fachada", [
    panel(), hud(14, [("menos de un céntimo por euro", 13)]), titulo("PARADA 4: el local"),
    txt("< 1 c", 380, 430, 180, color="#E0521B", anim="pop", en="menos de un céntimo por euro"),
    mano("en alquileres", 380, 570, 56, en="menos de un céntimo por euro"),
    txt("Zara: 6 c", 960, 440, 90, en="Zara paga seis"),
    sello("LOS EDIFICIOS SON SUYOS", 700, 720, 64, en="casi todos sus edificios"),
    cifra(15666, 700, 890, 100, sufijo=" M€", en="están tasados en"),
    masc("sorprendido", 1620, 520, entra="der", t=0.2, poses=[{"en": "Guárdate esa cifra", "pose": "senala"}]),
], zoom=[1.0, 1.06], fuente=CUENTAS + ": alquileres 170 M€; tasación de inmuebles 15.666 M€")

escena("12", "Quinta parada: todo lo que", "supermercado", [
    panel(), hud(13, [("Un céntimo va a publicidad", 12), ("Unos cinco, a la logística", 6.5), ("Y otros dos son", 4.2)]),
    titulo("PARADA 5: lo que no se ve"),
    mano("Publicidad: 1 c", 400, 380, 64, papel=True, anim="pop", rot=-2, en="Un céntimo va a publicidad"),
    mano("Logística · informática · seguridad ·\nluz · transporte · comisiones: 5 c", 700, 560, 54, papel=True, anim="pop", rot=2, en="Unos cinco, a la logística"),
    mano("Desgaste de edificios, reformas\ny tecnología: 2 c", 700, 800, 54, papel=True, anim="pop", rot=-2, en="Y otros dos son"),
    masc("corriendo", 1640, 480, entra="der", t=0.1),
], zoom=[1.04, 1.1], fuente=CUENTAS + " (notas 9 y 22; cálculo propio)")

escena("13", "Sexta parada: Hacienda, otra vez", "#E3E7EC", [
    hud(4.2, [("Entre los dos, menos de un céntimo", 3.5)]), titulo("PARADA 6: impuestos e intereses"),
    mano("Impuesto sobre el beneficio", 600, 380, 56, papel=True, en="impuesto sobre el beneficio"),
    mano("Intereses de la deuda", 600, 500, 56, papel=True, en="los intereses de la deuda"),
    txt("< 1 c entre los dos", 600, 650, 80, color="#E0521B", en="Entre los dos, menos"),
    mano("Este año, más bajo de lo normal:\ncréditos fiscales de los años de pérdidas", 600, 860, 48, en="créditos fiscales"),
    masc("enfadado", 1600, 520, entra="der", t=0.2, poses=[{"en": "Ojo: el impuesto", "pose": "pensativo"}]),
], fuente=CUENTAS + ": impuesto sobre sociedades 74 M€ (tipo efectivo 10,2 %)")

escena("14", "Y lo que queda, al final", "#FFF3C4", [
    hud(3.5),
    moneda("3,5 c", 420, 420, 150, color="#E0521B", t=0.3), mano("de beneficio por cada euro", 420, 640, 56, t=0.5),
    mano("Beneficio por euro:", 850, 300, 50, ancla="izq", en="Para que te hagas una idea"),
    rect(850, 360, 120, 80, "#E0521B", texto="3,5 c", tam=34, en="Para que te hagas una idea", dur=0.6),
    rect(850, 460, 140, 80, "#9CC5E8", texto="Mercadona 4 c", tam=26, en="Mercadona se quedaba", dur=0.6),
    rect(850, 560, 460, 80, "#F5B301", texto="Zara 13 c", tam=34, en="Mercadona se quedaba", dur=1.0),
    masc("pensativo", 1650, 500, entra="der", t=0.2),
], fuente=CUENTAS + " (beneficio neto 628 M€); vídeos de Mercadona y Zara")

escena("15", "De esos tres céntimos y medio", "#E6E0F5", [
    hud(3.5),
    {"tipo": "tarta", "x": 480, "y": 560, "r": 280, "t": 0.1, "porciones": [
        {"v": 1.4, "color": "#F5B301", "en": "casi uno y medio"},
        {"v": 2.1, "color": "#D9D2C0", "en": "casi uno y medio"}]},
    *leyenda([("≈ 1,4 c · dividendo para los accionistas", "#F5B301", "casi uno y medio"),
              ("≈ 2,1 c · se queda en la empresa", "#D9D2C0", "casi uno y medio"),
              ("≈ 0,6 c · a la Fundación Ramón Areces", "#E0521B", "algo más de medio céntimo")], x=820, y0=420, paso=110, tam=46),
    masc("moneda", 1700, 440, entra="der", t=0.2),
], fuente=CUENTAS + ": dividendo propuesto 250 M€ (cálculo propio)")

escena("16", "Así que ya ves el problema", "#F4E9D0", [
    txt("Con 3,5 c por euro…", 700, 330, 90, t=0.2),
    txt("…cualquier tropiezo se nota", 700, 520, 80, color="#E0521B", en="cualquier tropiezo"),
    sello("Y HA TROPEZADO", 700, 760, 90, en="Y El Corte Inglés ha tropezado"),
    masc("preocupado", 1620, 520, entra="der", t=0.2),
])

# ── LA HISTORIA ────────────────────────────────────────
escena("17", "Pero antes, déjame contarte", "sastreria_1930", [
    panel(90, 120, 1080, 870),
    txt("1890", 380, 260, 150, color="#E0521B", anim="pop", en="En mil ochocientos noventa"),
    mano("una sastrería en Madrid", 380, 390, 54, papel=True, en="pequeña sastrería"),
    txt("1935", 880, 260, 150, color="#E0521B", anim="pop", en="En mil novecientos treinta y cinco"),
    mano("la compra Ramón Areces", 880, 390, 54, papel=True, en="Ramón Areces, con el aval"),
    txt("1940", 630, 640, 150, color="#E0521B", anim="pop", en="En mil novecientos cuarenta"),
    mano("7 empleados", 630, 790, 70, papel=True, anim="pop", rot=-3, en="Tenían siete empleados"),
    masc("lupa", 1560, 520, entra="der", t=0.2),
], zoom=[1.0, 1.08], fuente="El Corte Inglés, historia corporativa")

escena("18", "Luego llegaron las cosas", "grandes_almacenes", [
    panel(),
    txt("1960", 300, 300, 100, color="#E0521B", en="En mil novecientos sesenta, el primer"), mano("«Ya es primavera…»", 720, 300, 60, ancla="izq", en="En mil novecientos sesenta, el primer"),
    txt("1966", 300, 500, 100, color="#E0521B", en="sesenta y seis"), mano("su tarjeta de compra", 720, 500, 60, ancla="izq", en="sesenta y seis"),
    txt("1972", 300, 700, 100, color="#E0521B", en="setenta y dos"), mano("«Si no queda satisfecho,\nle devolvemos su dinero»", 720, 720, 54, ancla="izq", papel=True, en="si no queda satisfecho"),
    masc("riendo", 1640, 500, entra="der", t=0.2),
], zoom=[1.04, 1.1], fuente="El Corte Inglés, historia corporativa")

escena("19", "Durante décadas fue el rey", "#F4E9D0", [
    txt("2007: el récord", 700, 200, 80, papel=True, t=0.2),
    mano("≈ 18.000 M€ vendidos", 700, 360, 70, en="casi dieciocho mil millones"),
    mano("+700 M€ de beneficio", 700, 470, 64, en="más de setecientos millones"),
    sello("NUNCA HA VUELTO A VENDER TANTO", 700, 620, 50, en="Nunca ha vuelto"),
    txt("Deuda: ≈ 5.000 M€", 700, 830, 90, color="#E0521B", anim="pop", en="hasta unos cinco mil millones"),
    masc("preocupado", 1620, 520, entra="der", en="Llegó la crisis"),
], fuente="Prensa (Público, 2009; deuda 2013-2014: prensa económica)")

escena("20", "Y luego, la pandemia", "#E3E7EC", [
    titulo("2020: la pandemia", t=0.1),
    txt("Ventas: −31 %", 600, 420, 110, en="casi un tercio"),
    cifra(-2945, 600, 650, 150, sufijo=" M€", color="#E0521B", en="dos mil novecientos cuarenta"),
    mano("la mayor pérdida de su historia (prensa)", 600, 820, 54, papel=True, en="La mayor pérdida"),
    masc("sorprendido", 1600, 520, entra="der", t=0.2),
], fuente="Ventas: nota de resultados 2021 de El Corte Inglés; pérdidas: prensa (junio de 2021)")

escena("21", "Ahí es cuando todo el mundo", "#FFF3C4", [
    {"tipo": "bocadillo", "texto": "¿Cuánto le queda?", "x": 600, "y": 350, "ancho": 800, "tam": 76, "t": 0.2},
    txt("¿Cómo ha salido de ahí?", 700, 750, 90, color="#E0521B", anim="pop", rot=-2, en="cómo ha salido de ahí"),
    masc("pensativo", 1620, 520, entra="der", t=0.2, poses=[{"en": "cómo ha salido de ahí", "pose": "lupa"}]),
])

# ── LAS CUATRO PIEZAS ──────────────────────────────────
escena("22", "La primera pieza son los edificios", "fachada", [
    panel(), titulo("PIEZA 1: los edificios"),
    mano("Sus inmuebles", 200, 360, 50, ancla="izq", en="Recuerda: quince mil"),
    rect(200, 400, 1000, 110, "#8FD18F", texto="15.666 M€", tam=56, en="Recuerda: quince mil", dur=1.2),
    mano("Su deuda", 200, 590, 50, ancla="izq", en="Su deuda hoy"),
    rect(200, 630, 105, 110, "#E0521B", texto="1.648", tam=28, en="Su deuda hoy", dur=0.6),
    txt("× 9,5", 700, 860, 110, color="#E0521B", anim="pop", en="nueve veces y media"),
    masc("contento", 1640, 500, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=CUENTAS + ": tasación de inmuebles y deuda financiera neta")

escena("23", "La segunda pieza es vender", "oficina_financiera", [
    panel(), titulo("PIEZA 2: vender lo que sobraba"),
    mano("Óptica 2000", 450, 380, 64, papel=True, anim="pop", rot=-3, en="Vendió Óptica"),
    mano("Informática El Corte Inglés", 900, 380, 58, papel=True, anim="pop", rot=2, en="Vendió Informática"),
    txt("Mutua Madrileña (2022)", 700, 590, 64, en="Mutua Madrileña le pagó"),
    cifra(1105, 700, 740, 140, sufijo=" M€", color="#E0521B", en="mil ciento cinco"),
    mano("½ de los seguros + 8 % de la empresa", 700, 890, 54, en="por la mitad de su negocio"),
    masc("moneda", 1640, 500, entra="der", t=0.2),
], zoom=[1.04, 1.1], fuente="El Corte Inglés, historia corporativa; Mutua Madrileña (31/05/2022)")

escena("24", "La tercera pieza es el dinero", "oficina_financiera", [
    panel(), titulo("PIEZA 3: lo que no se ve en la caja"),
    txt("49 % de su financiera", 700, 380, 70, en="casi la mitad de su financiera"),
    mano("11,7 millones de tarjetas activas", 700, 500, 56, papel=True, en="once millones setecientas"),
    txt("≈ 50 % de sus seguros", 700, 650, 70, en="casi la mitad de sus seguros"),
    txt("1 de cada 10 € de beneficio", 700, 850, 70, color="#E0521B", anim="pop", rot=-2, en="uno de cada diez euros"),
    masc("lupa", 1640, 500, entra="der", t=0.2),
], fuente=CUENTAS + ": Seguros y Financiera, 10,1 % del resultado neto")

escena("25", "Y la cuarta pieza es un personaje", "#E6E0F5", [
    titulo("PIEZA 4: un jeque de Catar", t=0.1),
    txt("2015", 280, 390, 90, color="#E0521B", en="En dos mil quince"), mano("le presta 1.000 M€", 780, 390, 60, ancla="izq", en="le prestó mil millones"),
    txt("2018", 280, 580, 90, color="#E0521B", en="En dos mil dieciocho"), mano("lo cobra en acciones: > 10 %", 780, 580, 60, ancla="izq", en="se los cobró en acciones"),
    txt("2022", 280, 770, 90, color="#E0521B", en="Y en dos mil veintidós"), mano("le recompra la mitad: 485 M€", 780, 770, 60, ancla="izq", en="le recompró la mitad"),
    masc("sorprendido", 1700, 480, entra="der", t=0.2),
], fuente=CUENTAS.replace("2025 (mar. 2025 – feb. 2026)", "2018 y 2022") + " (nota 15)")

escena("26", "Con todo eso, la deuda", "#F4E9D0", [
    mano("Deuda", 200, 200, 54, ancla="izq", t=0.2),
    rect(200, 250, 1000, 100, "#D9D2C0", texto="≈ 5.000 M€ (2014, prensa)", tam=40, en="la deuda ha bajado", dur=0.8),
    rect(200, 380, 330, 100, "#8FD18F", texto="1.648 M€ (hoy)", tam=36, en="mil seiscientos cuarenta y ocho", dur=0.8),
    txt("Beneficio: 628 M€", 700, 620, 90, color="#E0521B", en="seiscientos veintiocho"),
    sello("GRADO DE INVERSIÓN (2023)", 700, 820, 60, en="grado de inversión"),
    masc("contento", 1620, 520, entra="der", t=0.2),
], fuente=CUENTAS + "; rating BBB- de S&P y Fitch")

# ── LO QUE NO CUADRA ───────────────────────────────────
escena("27", "Ahora bien, esto no significa", "#E3E7EC", [
    titulo("SOMBRA 1: las tiendas", en="La primera sombra"),
    mano("Grandes almacenes", 200, 350, 52, ancla="izq", en="noventa y tres"),
    rect(200, 400, 930, 100, "#D9D2C0", texto="2018: 93", tam=44, en="noventa y tres", dur=0.8),
    rect(200, 520, 720, 100, "#E0521B", texto="hoy: 72", tam=44, en="Hoy, setenta y dos", dur=0.8),
    txt("21 menos", 1080, 570, 70, color="#E0521B", anim="pop", en="Veintiuno menos"),
    mano("Plantilla: de 90.004 a 81.830 personas", 660, 800, 56, papel=True, en="la plantilla ha bajado"),
    masc("preocupado", 1640, 500, entra="der", t=0.2),
], fuente="El Corte Inglés, informe financiero 2018 y cuentas del ejercicio 2025")

escena("28", "La segunda: las ventas", "#F4E9D0", [
    titulo("SOMBRA 2: las ventas", t=0.1),
    mano("Ventas", 200, 350, 52, ancla="izq", en="tres mil millones menos"),
    rect(200, 400, 1000, 100, "#D9D2C0", texto="2007: ≈ 18.000 M€ (prensa)", tam=40, en="tres mil millones menos", dur=0.8),
    rect(200, 520, 830, 100, "#9CC5E8", texto="2025: 14.988 M€", tam=40, en="tres mil millones menos", dur=1.1),
    txt("−17 % (sin descontar la inflación)", 700, 780, 70, color="#E0521B", en="diecisiete por ciento"),
    masc("pensativo", 1640, 500, entra="der", t=0.2),
], fuente="2007: prensa; 2025: " + CUENTAS)

escena("29", "La tercera: internet", "#E3E7EC", [
    titulo("SOMBRA 3: internet", t=0.1),
    txt("2021: 12 % en línea", 600, 400, 90, en="el doce por ciento"),
    mano("desde entonces, sin cifra de ventas", 600, 540, 58, papel=True, en="Desde entonces solo publica"),
    txt("Comercio electrónico en España: +20 %", 600, 760, 64, color="#E0521B", en="más de un veinte por ciento"),
    masc("lupa", 1620, 520, entra="der", t=0.2),
], fuente="El Corte Inglés, resultados 2021; CNMC (03/07/2026): comercio electrónico 2025, +20,6 %")

escena("30", "Y la cuarta: el jeque todavía", "#E6E0F5", [
    titulo("SOMBRA 4: el jeque", t=0.1),
    mano("Puede pedirle que le recompre sus acciones en…", 700, 380, 56, papel=True, en="el jeque todavía puede"),
    txt("2028", 380, 600, 110, color="#E0521B", anim="pop", en="en dos mil veintiocho"),
    txt("2031", 700, 600, 110, color="#E0521B", anim="pop", en="dos mil treinta y uno"),
    txt("2034", 1020, 600, 110, color="#E0521B", anim="pop", en="dos mil treinta y cuatro"),
    masc("preocupado", 1640, 500, entra="der", t=0.2),
], fuente=CUENTAS + " (nota 15.4)")

# ── RESUMEN Y CIERRE ───────────────────────────────────
escena("31", "Así que, la próxima vez", "#FFF3C4", [
    txt("El viaje de tu euro", 960, 110, 72, papel=True, t=0.2),
    {"tipo": "tarta", "x": 470, "y": 590, "r": 300, "t": 0.5, "porciones": [
        {"v": 17.4, "color": "#9CC5E8", "en": "Diecisiete céntimos, para Hacienda"},
        {"v": 54.6, "color": "#F5B301", "en": "Cincuenta y cinco, para quien"},
        {"v": 14.4, "color": "#8FD18F", "en": "Catorce, para la plantilla"},
        {"v": 0.9, "color": "#C9B8E8", "en": "Menos de uno, para el alquiler"},
        {"v": 9.2, "color": "#F7DCC8", "en": "Casi nueve, para la publicidad"},
        {"v": 3.5, "color": "#E0521B", "en": "Y tres céntimos y medio"}]},
    *leyenda([("17 c · Hacienda (IVA)", "#9CC5E8", "Diecisiete céntimos, para Hacienda"),
              ("55 c · el producto", "#F5B301", "Cincuenta y cinco, para quien"),
              ("14 c · plantilla", "#8FD18F", "Catorce, para la plantilla"),
              ("< 1 c · alquiler (la casa es suya)", "#C9B8E8", "Menos de uno, para el alquiler"),
              ("≈ 9 c · publicidad, logística, luz, reformas…", "#F7DCC8", "Casi nueve, para la publicidad"),
              ("3,5 c · beneficio", "#E0521B", "Y tres céntimos y medio")], x=840, y0=260, paso=105, tam=46),
], fuente="Cálculo propio con la cuenta de resultados de El Corte Inglés 2025 (media del grupo, IVA del 21 %); «≈ 9 c» incluye impuestos e intereses")

escena("32", "El Corte Inglés no gana dinero", "fachada", [
    panel(150, 200, 1150, 720),
    mano("No gana por vender caro…", 725, 310, 66, t=0.2),
    txt("es dueño de sus edificios,", 725, 470, 70, en="es dueño de sus propios"),
    txt("vendió lo que le sobraba", 725, 600, 70, en="ha vendido todo"),
    txt("y pagó casi toda su deuda", 725, 730, 70, en="céntimo a céntimo"),
    txt("¿Bastan 3 céntimos por euro?", 725, 860, 64, color="#E0521B", anim="pop", rot=-2, en="Es si tres céntimos"),
    masc("pensativo", 1650, 500, entra="der", t=0.1),
], zoom=[1.04, 1.12])

escena("33", "Aquí, cada semana, abrimos", "#F5B301", [
    masc("saluda", 960, 560, entra="abajo", t=0.2),
    txt("TICKET MEDIO", 960, 170, 150, anim="pop", t=0.3),
    mano("Cada semana, el ticket de algo que pagas todos los días", 960, 300, 50, papel=True, t=1.0),
], sin_marca=True)

cfg = {"musica": "audio/musica.mp3", "musica_db": -26, "cola": 3, "escenas": E}
json.dump(cfg, open(os.path.join(V, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("escenas:", len(E))
