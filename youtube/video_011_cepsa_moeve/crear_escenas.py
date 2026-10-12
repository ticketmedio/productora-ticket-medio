"""Escenas del vídeo 11 (Cepsa → Moeve). Datos: INVESTIGACION.md."""
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
M25 = "Moeve, resultados 2025 (comunicado del 2/3/2026)"; M26 = "Moeve, primer semestre de 2026 (comunicado del 31/7/2026)"
escena("01", "El treinta de octubre", "centro_logistico", [
    panel(), mano("30 de octubre de 2024", 700, 230, 56, t=0.2),
    txt("CEPSA", 380, 480, 120, color="#9A9A9A", t=0.4), txt("→", 700, 480, 100, t=0.8), txt("MOEVE", 1000, 480, 120, color=ROJO, anim="pop", en="Ahora es Moeve"),
    sello("¿NOS ESTÁN ENGAÑANDO?", 700, 760, 64, t=2.0),
    masc("pensativo", 1630, 520, entra="der", t=0.3),
], zoom=[1.0, 1.06], fuente="Forbes España (30/10/2024)")
escena("02", "Hoy lo comprobamos", "#FFF3C4", [
    txt("Lo comprobamos con lo que\nla propia empresa publica", 800, 300, 72, t=0.2),
    sello("SIN ACUSAR A NADIE", 800, 600, 70, en="sin acusar a nadie"),
    mano("Cada dato, al lado de otro", 800, 820, 58, papel=True, en="cada dato al lado"),
    masc("lupa", 1620, 520, entra="der", t=0.2),
])
escena("03", "Empecemos por lo básico", "oficina_financiera", [
    panel(), titulo("¿HA CAMBIADO DE DUEÑO?"),
    txt("No hay ningún dato que lo indique", 700, 380, 56, en="No hay ningún dato"),
    mano("Es la misma sociedad con otra marca", 700, 500, 54, en="la misma sociedad"),
    rect(150, 600, 780, 100, AMAR, texto="Mubadala (Abu Dabi) > 61 %", tam=42, en="Mubadala, con algo más del sesenta", dur=0.8),
    rect(150, 730, 380, 100, AZUL, texto="Carlyle > 38 %", tam=42, en="el grupo Carlyle", dur=0.8),
    masc("normal", 1670, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="Informe de 2024, según prensa (cifras aproximadas)")
escena("04", "¿Qué dijo la empresa", "#E6E0F5", [
    titulo("LO QUE DIJO LA EMPRESA"),
    mano("Estrategia «Positive Motion 2030»", 700, 380, 54, en="Positive Motion"),
    mano("Acelerar su descarbonización\ny la de sus clientes", 700, 520, 52, en="acelerar su descarbonización"),
    txt("Hasta 8.000 M€ · > 60 % sostenible", 700, 740, 60, color=ROJO, en="hasta ocho mil millones"),
    mano("hidrógeno verde · biocombustibles · recarga ultrarrápida", 700, 860, 42, en="hidrógeno verde"),
    masc("saluda", 1660, 500, mira="izq", entra="der", t=0.2),
], fuente="Forbes España (30/10/2024)")
escena("05", "Hasta aquí, lo que dice", "#FFF3C4", [
    txt("Hasta aquí, lo que DICE", 800, 280, 80, t=0.2), txt("Ahora, lo que PUBLICA", 800, 520, 80, color=ROJO, anim="pop", en="Ahora, lo que publica"),
    masc("senala", 1620, 520, mira="izq", entra="der", t=0.2),
])
escena("06", "En dos mil veinticinco, Moeve invirtió", "fabrica_alimentos", [
    panel(), titulo("INVERSIÓN 2025"),
    cifra(1151, 450, 440, 140, sufijo=" M€", en="mil ciento cincuenta y un"), mano("de capex", 450, 570, 44, en="mil ciento cincuenta y un"),
    cifra(55, 1000, 440, 190, sufijo=" %", color="#2E8B57", en="el cincuenta y cinco por ciento"), mano("a transición energética (récord)", 1000, 620, 42, en="récord"),
    mano("≈ 633 M€ (cálculo propio) · en 2024: 43 %", 700, 850, 46, papel=True, en="Unos seiscientos treinta"),
    masc("contento", 1680, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=M25)
escena("07", "Y en el primer semestre", "#F4E9D0", [
    titulo("PRIMER SEMESTRE 2026"),
    cifra(605, 450, 440, 150, sufijo=" M€", en="seiscientos cinco millones"), mano("invertidos", 450, 570, 44, en="seiscientos cinco millones"),
    cifra(69, 1000, 440, 190, sufijo=" %", color="#2E8B57", en="el sesenta y nueve por ciento"), mano("a transición energética", 1000, 620, 42, en="el sesenta y nueve por ciento"),
    sello("OTRO RÉCORD", 700, 840, 60, t=1.5),
    masc("riendo", 1680, 500, mira="izq", entra="der", t=0.2),
], fuente=M26)
escena("08", "Lo que están construyendo", "torre_electrica", [
    panel(), titulo("LO QUE CONSTRUYE"),
    mano("304 M€ de fondos europeos · Valle Andaluz\ndel Hidrógeno Verde", 700, 400, 46, en="trescientos cuatro"),
    mano("Planta de biocombustibles 2G (Huelva): > 50 % construida", 700, 590, 46, en="Una planta de biocombustibles"),
    mano("> 280 puntos de recarga ultrarrápida", 700, 720, 46, en="Más de doscientos ochenta"),
    mano("500 estaciones renovadas con la nueva imagen", 700, 850, 46, en="quinientas estaciones"),
    masc("normal", 1680, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=M25)
escena("09", "Ahora, la otra columna", "#FFF3C4", [
    txt("Ahora, la otra columna", 800, 280, 84, t=0.3), mano("¿De dónde sale el dinero?", 800, 520, 70, en="¿De dónde sale el dinero"),
    masc("pensativo", 1620, 520, entra="der", t=0.2),
])
escena("10", "En dos mil veinticinco, la empresa ganó", "#E3E7EC", [
    mano("EBITDA 2025 (antes de intereses, impuestos\ny amortizaciones)", 800, 220, 48, papel=True, t=0.2),
    rect(150, 340, 1100, 100, AZUL, texto="Grupo: 1.685 M€", tam=44, en="mil seiscientos ochenta", dur=0.8),
    rect(150, 480, 910, 100, ROJO, texto="Energía: 1.400 M€ · 83 %", tam=44, en="mil cuatrocientos vinieron", dur=0.9),
    mano("Refino, estaciones, comercio de combustibles\ny energías limpias comerciales", 800, 700, 44, en="refinerías"),
    masc("lupa", 1680, 500, mira="izq", entra="der", t=0.2),
], fuente=M25 + " (porcentaje: cálculo propio)")
escena("11", "Y en el primer semestre de dos mil veintiséis", "#F4E9D0", [
    mano("EBITDA primer semestre 2026", 800, 220, 52, papel=True, t=0.2),
    rect(150, 340, 1100, 100, AZUL, texto="Grupo: 1.178 M€", tam=44, en="mil ciento setenta y ocho", dur=0.8),
    rect(150, 480, 880, 100, ROJO, texto="Energía: 945 M€ · 80 %", tam=44, en="novecientos cuarenta y cinco", dur=0.9),
    masc("normal", 1680, 500, mira="izq", entra="der", t=0.2),
], fuente=M26 + " (porcentaje: cálculo propio)")
escena("12", "Fíjate en lo que dice el comunicado", "centro_logistico", [
    panel(), titulo("LO QUE DICE EL COMUNICADO"),
    cifra(18.2, 450, 440, 150, sufijo=" Mt", dec=1, en="dieciocho millones doscientas mil"), mano("de productos comerciales (+6 %)", 450, 570, 42, en="un seis por ciento"),
    txt("7,0 → 7,9 $/barril", 1010, 470, 64, color=ROJO, en="de siete a casi ocho dólares"), mano("margen de refino", 1010, 580, 44, en="margen de refino"),
    masc("senala", 1680, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=M25)
escena("13", "O sea: lo que más se invierte", "#FFF3C4", [
    txt("Lo que más se INVIERTE\nes verde", 800, 270, 70, color="#2E8B57", t=0.3, en="lo que más se invierte es verde"),
    txt("Lo que más INGRESA\nsigue siendo la energía de siempre", 800, 520, 62, color=ROJO, en="Y lo que más ingresa"),
    mano("No es una contradicción: es una transición", 800, 800, 52, papel=True, en="No es una contradicción"),
    masc("pensativo", 1650, 500, entra="der", t=0.2),
])
escena("14", "Y otro dato curioso", "calle_comercial", [
    panel(), titulo("BALLENOIL"),
    mano("La cadena low cost también es de Moeve", 700, 400, 52, en="la dueña de Ballenoil"),
    cifra(370, 700, 600, 190, color=ROJO, en="trescientas setenta"), mano("estaciones (65 abiertas en 2025)", 700, 750, 46, en="trescientas setenta"),
    masc("sorprendido", 1680, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=M25)
escena("15", "Ahora, una norma", "#E6E0F5", [
    titulo("DESDE EL 27/9/2026"),
    mano("Directiva (UE) 2024/825 · afirmaciones «verdes»", 700, 380, 46, en="Desde el veintisiete"),
    txt("Prohíbe, entre otras:", 700, 500, 54, en="prohíbe"),
    mano("· «Respetuoso con el clima», «verde»… sin prueba", 700, 610, 44, en="genéricas"),
    mano("· Presentar toda la empresa como verde\n  si solo lo es un aspecto", 700, 730, 44, en="toda una empresa"),
    mano("· Neutralidad basada en compensar emisiones", 700, 880, 44, en="compensar emisiones"),
    masc("lupa", 1680, 500, mira="izq", entra="der", t=0.2),
], fuente="Directiva (UE) 2024/825 (EUR-Lex), art. 4 y anexo I de la Directiva 2005/29/CE")
escena("16", "No decimos que Moeve incumpla", "#FFF3C4", [
    sello("NO DECIMOS QUE INCUMPLA NADA", 800, 280, 56, t=0.2),
    mano("No hemos revisado ningún anuncio concreto\nni cómo España ha incorporado la norma", 800, 520, 50, en="ningún anuncio concreto"),
    mano("Es la vara de medir: toda afirmación verde\ndebe poder comprobarse y ser específica", 800, 780, 48, papel=True, en="la vara de medir"),
    masc("encoge_hombros", 1650, 500, entra="der", t=0.2),
])
escena("17", "Vamos con lo que no sabemos", "#E3E7EC", [
    sello("LO QUE NO SABEMOS", 800, 240, 80, t=0.2),
    mano("· Si el cambio de nombre influye en los precios", 800, 440, 46, en="influye en los precios"),
    mano("· Cuántas estaciones tiene en total", 800, 570, 46, en="cuántas estaciones"),
    mano("· Qué parte de las ganancias será verde en 2030", 800, 700, 46, en="qué parte de las ganancias"),
    masc("encoge_hombros", 1660, 500, entra="der", t=0.2),
])
escena("18", "Así que, ¿nos están engañando", "supermercado", [
    panel(), titulo("¿NOS ESTÁN ENGAÑANDO?"),
    mano("Sobre quién es la empresa: no.\nEs la misma y sus datos son públicos.", 700, 450, 54, en="no sobre quién es"),
    txt("¿Cuánto de lo que se llama Moeve\nya es lo que dice su nombre?", 700, 740, 60, color=ROJO, en="cuánto de lo que se llama"),
    masc("pensativo", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06])
escena("19", "Y un detalle final", "#F4E9D0", [
    titulo("IMPUESTOS EN ESPAÑA · 1.er SEM. 2026"),
    cifra(2088, 700, 430, 170, sufijo=" M€", en="dos mil ochenta y ocho"),
    rect(150, 560, 700, 100, AZUL, texto="1.269 M€ soportados por la empresa", tam=36, en="Mil doscientos sesenta y nueve", dur=0.8),
    rect(150, 690, 520, 100, GRIS, texto="819 M€ recaudados para Hacienda", tam=34, en="ochocientos diecinueve", dur=0.8),
    masc("moneda", 1680, 500, mira="izq", entra="der", t=0.2),
], fuente=M26)
escena("20", "Aquí, cada semana, abrimos", "#F5B301", [
    masc("saluda", 960, 560, entra="abajo", t=0.2), txt("TICKET MEDIO", 960, 170, 150, anim="pop", t=0.3),
    mano("Cada semana, el ticket de algo que pagas todos los días", 960, 300, 50, papel=True, t=1.0),
], sin_marca=True)
json.dump({"musica": "audio/musica.mp3", "musica_db": -26, "cola": 3, "escenas": E_}, open(os.path.join(V, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("escenas:", len(E_))
