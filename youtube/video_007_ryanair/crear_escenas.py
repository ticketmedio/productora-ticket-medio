"""Genera escenas_v2.json del vídeo 7 (Ryanair). Datos: INVESTIGACION.md (comunicado FY26 del 18/5/2026, Reg. 1008/2008)."""
import json, os
V = os.path.dirname(os.path.abspath(__file__))
def panel(x=90, y=120, w=1230, h=870): return {"tipo": "panel", "x": x, "y": y, "w": w, "h": h, "t": 0}
def titulo(txt, **k): return {"tipo": "texto", "texto": txt, "x": 1010, "y": 200, "tam": 76, "papel": True, **({"t": 0.2} if not k else k)}
def txt(c, x, y, tam=60, **k): return {"tipo": "texto", "texto": c, "x": x, "y": y, "tam": tam, **k}
def mano(c, x, y, tam=56, **k): return txt(c, x, y, tam, fuente="mano", **k)
def cifra(n, x, y, tam=170, **k): return {"tipo": "cifra", "hasta": n, "x": x, "y": y, "tam": tam, **k}
def masc(pose, x=1600, h=520, **k): return {"tipo": "mascota", "pose": pose, "x": x, "y": 1015, "h": h, **k}
def sello(c, x, y, tam=70, **k): return {"tipo": "sello", "texto": c, "x": x, "y": y, "tam": tam, **k}
def rect(x, y, w, h, color, **k): return {"tipo": "rect", "x": x, "y": y, "w": w, "h": h, "color": color, **k}
def moneda(t, x, y, r=110, color="#F5B301", **k): return {"tipo": "moneda", "texto": t, "r": r, "x": x, "y": y, "color": color, **k}
def leyenda(filas, x=900, y0=300, paso=95, tam=50):
    capas = []
    for i, (texto, color, en) in enumerate(filas):
        y = y0 + i * paso
        capas += [rect(x, y - 28, 56, 56, color, en=en, dur=0.3), txt(texto, x + 85, y, tam, ancla="izq", en=en)]
    return capas
E = []
def escena(id, desde, fondo, capas, **k): E.append({"id": id, "desde": desde, "fondo": fondo, "capas": capas, **k})
RY = "Ryanair Holdings plc, resultados del ejercicio FY26 (1/4/2025–31/3/2026), comunicado del 18/5/2026"
AMAR, ROJO, AZUL, VERDE, GRIS = "#F5B301", "#E0521B", "#9CC5E8", "#8FD18F", "#D9D2C0"

escena("01", "El billete medio de Ryanair", "puerto_avion", [
    panel(), mano("El billete medio de Ryanair…", 700, 230, 58, t=0.2),
    txt("NO CUESTA 10 €", 700, 400, 100, color=ROJO, anim="pop", en="no cuesta diez euros"),
    cifra(74.57, 700, 620, 170, sufijo=" €", dec=2, en="setenta y cuatro con cincuenta y siete"),
    mano("y le deja de beneficio 10,84 €", 700, 830, 56, papel=True, en="diez euros con ochenta y cuatro"),
    masc("sorprendido", 1620, 520, entra="der", t=0.3),
], zoom=[1.0, 1.06], fuente=RY + " (cálculo propio por pasajero)")
escena("02", "Hoy vamos a abrir el ticket", "#FFF3C4", [
    txt("El ticket de un\nbillete de Ryanair", 800, 270, 84, t=0.2),
    mano("con las cuentas de la propia aerolínea", 800, 520, 56, en="cuentas que acaba de publicar"),
    mano("¿Adónde va cada euro?", 800, 700, 64, papel=True, en="Y a ver adónde va"),
    masc("saluda", 1620, 520, entra="der", t=0.2),
], fuente=RY)
escena("03", "Primero, las presentaciones", "calle_comercial", [
    panel(), mano("Ryanair · ejercicio cerrado en marzo de 2026", 700, 220, 52, t=0.2),
    cifra(208.4, 360, 430, 130, sufijo=" M", dec=1, en="doscientos ocho millones"), mano("pasajeros", 360, 540, 44, en="doscientos ocho millones"),
    cifra(647, 1000, 430, 130, en="seiscientos cuarenta y siete"), mano("aviones", 1000, 540, 44, en="seiscientos cuarenta y siete"),
    cifra(621, 360, 720, 130, en="seiscientos veintiuno"), mano("son Boeing 737", 360, 830, 44, en="seiscientos veintiuno"),
    cifra(30000, 1000, 720, 130, en="seiscientos veintiuno", t=1.8), mano("empleados", 1000, 830, 44, en="seiscientos veintiuno", t=2.0),
    masc("saluda", 1630, 500, entra="der", t=0.2),
], zoom=[1.0, 1.05], fuente=RY)
escena("04", "Sus aviones iban llenos", "#E3E7EC", [
    cifra(94, 800, 340, 220, sufijo=" %", color="#2E8B57", t=0.3), mano("de ocupación", 800, 500, 60, t=0.4),
    mano("De cada 100 asientos, solo 6 volaron vacíos", 800, 700, 54, papel=True, en="solo seis volaron vacíos"),
    masc("contento", 1620, 520, entra="der", t=0.2),
], fuente=RY)
escena("05", "Para que te hagas una idea del tamaño", "#F4E9D0", [
    mano("Ingresos anuales (distintos ejercicios y sectores)", 800, 190, 48, papel=True, t=0.2),
    rect(150, 290, 1000, 100, AMAR, texto="Mercadona · casi 42.000 M€", tam=42, en="casi cuarenta y dos mil", dur=0.9),
    rect(150, 430, 370, 100, AZUL, texto="Ryanair · 15.540 M€", tam=38, en="quince mil quinientos millones", dur=0.9, t=0.6),
    rect(150, 570, 190, 100, VERDE, texto="Lidl España · 7.641 M€", tam=34, en="siete mil seiscientos", dur=0.9),
    masc("lupa", 1650, 500, entra="der", t=0.2),
], fuente=RY + " · Mercadona, Memoria 2025 · Lidl España, comunicado del 30/9/2026")
escena("06", "Con eso, ingresó quince mil", "puerto_avion", [
    panel(), mano("Último ejercicio", 700, 230, 56, t=0.2),
    cifra(15540, 700, 400, 150, sufijo=" M€", en="quince mil quinientos cuarenta"), txt("ingresos · +11 %", 700, 540, 56, color="#2E8B57", en="Un once por ciento"),
    cifra(2260, 700, 710, 150, sufijo=" M€", color=ROJO, en="dos mil doscientos sesenta"), txt("beneficio neto · +40 %", 700, 850, 56, color="#2E8B57", en="un cuarenta por ciento"),
    masc("sorprendido", 1620, 520, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=RY)
escena("07", "Hagamos primero unas cuentas rápidas", "#E6E0F5", [
    mano("Medias por avión y por empleado", 800, 190, 54, papel=True, t=0.2),
    cifra(322000, 450, 400, 130, en="trescientos veintidós mil"), mano("pasajeros por avión", 450, 510, 44, en="trescientos veintidós mil"),
    cifra(24, 1150, 400, 130, sufijo=" M€", en="veinticuatro millones"), mano("ingresos por avión", 1150, 510, 44, en="veinticuatro millones"),
    cifra(3.5, 450, 700, 130, sufijo=" M€", dec=1, color=ROJO, en="tres millones y medio"), mano("beneficio por avión", 450, 810, 44, en="tres millones y medio"),
    cifra(518000, 1150, 700, 120, sufijo=" €", en="quinientos dieciocho mil"), mano("ingresos por empleado", 1150, 810, 44, en="quinientos dieciocho mil"),
    masc("pensativo", 1680, 480, entra="der", t=0.2),
], fuente="Cálculo propio con las cifras de Ryanair (medias de todo el grupo)")
escena("08", "Y mira lo que pasó con los costes", "#FFF3C4", [
    mano("Costes vs ingresos (variación anual)", 800, 190, 54, papel=True, t=0.2),
    rect(150, 290, 450, 120, GRIS, texto="Costes  +6 %", tam=48, en="Los costes subieron", dur=0.8),
    rect(150, 450, 830, 120, AMAR, texto="Ingresos  +11 %", tam=48, en="Los ingresos, un once", dur=0.8),
    txt("Beneficio operativo  +52 %", 800, 760, 76, color="#2E8B57", anim="pop", en="cincuenta y dos por ciento"),
    masc("riendo", 1650, 500, entra="der", t=0.2),
], fuente=RY)
escena("09", "Ahora, pongamos todo eso", "#E3E7EC", [
    sello("EN UN SOLO BILLETE", 800, 260, 80, t=0.2),
    mano("Cada cifra ÷ 208,4 millones de pasajeros", 800, 480, 56, en="Dividimos cada cifra"),
    mano("Un cálculo nuestro: una media,\nno el precio de ningún vuelo", 800, 700, 56, papel=True, en="Es un cálculo nuestro"),
    masc("lupa", 1620, 520, entra="der", t=0.2),
], fuente="Cálculo propio con " + RY)
escena("10", "Cada pasajero le deja", "supermercado", [
    panel(), mano("Cada pasajero le deja a Ryanair", 700, 230, 56, t=0.2),
    cifra(74.57, 700, 420, 190, sufijo=" €", dec=2, t=0.4),
    mano("de media (cálculo propio)", 700, 580, 50, t=2.0),
    masc("moneda", 1620, 520, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=RY)
escena("11", "De la tarifa, cincuenta euros", "#F4E9D0", [
    mano("De la tarifa: 50,67 €  (68 %)", 800, 190, 58, papel=True, t=0.2),
    rect(150, 300, 1000, 110, AZUL, texto="Tarifa media ≈ 51 € (+10 %)", tam=46, en="cincuenta euros con sesenta y siete", dur=0.9),
    mano("Es la media de todos los billetes:\nlos de 10 € y los de 200 €", 800, 540, 54, en="los de diez euros y los de doscientos"),
    mano("Ryanair no dice cuántos billetes vende a cada precio", 800, 780, 48, papel=True, en="Ryanair dice que la tarifa media"),
    masc("encoge_hombros", 1660, 500, entra="der", t=0.2),
], fuente=RY)
escena("12", "Y de los extras, veinticuatro", "#FFF3C4", [
    mano("De los extras: 23,94 €  (32 %)", 800, 190, 58, papel=True, t=0.2),
    rect(150, 300, 560, 110, AMAR, texto="Extras ≈ 24 € por pasajero", tam=40, en="veinticuatro euros", dur=0.9),
    mano("Todo lo que pagas aparte del asiento", 800, 540, 56, en="aparte del asiento"),
    mano("La empresa solo da el total", 800, 700, 52, papel=True, en="no lo desglosa"),
    masc("normal", 1650, 480, entra="der", t=0.2),
], fuente=RY)
escena("13", "Y fíjate en cómo crece", "#E6E0F5", [
    mano("Cómo crece cada parte (último año)", 800, 190, 54, papel=True, t=0.2),
    rect(150, 290, 900, 110, AZUL, texto="Tarifas  +14 %", tam=48, en="un catorce por ciento", dur=0.8),
    rect(150, 450, 400, 110, AMAR, texto="Extras  +6 %", tam=48, en="un seis", dur=0.8),
    txt("La tarifa crece más deprisa", 800, 720, 70, color=ROJO, anim="pop", en="la tarifa crece más deprisa"),
    masc("senala", 1650, 500, mira="izq", entra="der", t=0.2),
], fuente=RY)
escena("14", "Fíjate en algo", "#E3E7EC", [
    {"tipo": "tarta", "x": 470, "y": 560, "r": 290, "t": 0.3, "porciones": [
        {"v": 68, "color": AZUL, "en": "pero los dos tercios"},
        {"v": 32, "color": AMAR, "en": "casi un tercio"}]},
    *leyenda([("68 % · tarifa", AZUL, "pero los dos tercios"), ("32 % · extras", AMAR, "casi un tercio")], x=860, y0=440, paso=110, tam=52),
    mano("El negocio no es solo la maleta", 1180, 860, 52, papel=True, en="no es solo cobrar por la maleta"),
], fuente=RY + " (porcentajes: cálculo propio)")
escena("15", "Ahora, la otra mitad del ticket", "#FFF3C4", [
    txt("Ahora, adónde va", 800, 260, 90, t=0.2),
    mano("el dinero de ese billete", 800, 430, 70, en="adónde va ese dinero"),
    masc("pensativo", 1620, 520, entra="der", t=0.2),
])
escena("16", "Primera parada, y la más grande", "centro_logistico", [
    panel(), titulo("PARADA 1: combustible"),
    cifra(26, 450, 460, 220, sufijo=" €", color=ROJO, en="Veintiséis euros por pasajero"), mano("por pasajero · 35 % del billete", 450, 640, 46, en="el treinta y cinco por ciento"),
    txt("80 % cubierto\npara el próximo año", 1020, 480, 60, en="cubierto el ochenta por ciento"), mano("a ≈ 67 $ el barril", 1020, 680, 48, en="sesenta y siete dólares"),
    masc("senala", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=RY)
escena("17", "Segunda parada: el personal", "#E3E7EC", [
    titulo("PARADA 2: el personal"),
    cifra(8.93, 700, 450, 200, sufijo=" €", dec=2, color=ROJO, en="Casi nueve euros"), mano("por pasajero · 12 % del billete", 700, 640, 54, en="el doce por ciento"),
    mano("1.860 M€ al año", 700, 800, 52, papel=True, t=1.5),
    masc("riendo", 1640, 500, entra="der", t=0.2),
], fuente=RY)
escena("18", "Tercera parada: los aeropuertos", "oficina_financiera", [
    panel(), titulo("PARADA 3: los aeropuertos"),
    cifra(8.45, 450, 460, 200, sufijo=" €", dec=2, color=ROJO, en="Ocho euros con cuarenta y cinco"), mano("por pasajero · 11 % del billete", 450, 640, 46, en="El once por ciento"),
    cifra(1760, 1010, 460, 150, sufijo=" M€", en="Mil setecientos sesenta"), mano("en tasas aeroportuarias al año", 1010, 620, 44, en="tasas aeroportuarias"),
    masc("lupa", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=RY)
escena("19", "Y el resto de costes", "#F4E9D0", [
    titulo("EL RESTO DE COSTES"),
    cifra(19.43, 700, 450, 200, sufijo=" €", dec=2, color=ROJO, en="unos diecinueve euros"), mano("mantenimiento, rutas y todo lo demás · 26 %", 700, 640, 46, en="mantenimiento, rutas"),
    masc("normal", 1640, 500, entra="der", t=0.2),
], fuente=RY + " (resto = costes totales − combustible − personal − tasas; cálculo propio)")
escena("20", "Lo que queda, antes de impuestos", "#FFF3C4", [
    titulo("LO QUE QUEDA"),
    rect(150, 300, 760, 110, AMAR, texto="Beneficio operativo: 11,37 €", tam=44, en="beneficio operativo", dur=0.8),
    rect(150, 450, 700, 110, ROJO, texto="Beneficio neto: 10,84 €", tam=44, en="beneficio neto antes", dur=0.8),
    txt("14,5 % de los ingresos", 700, 740, 70, color="#2E8B57", anim="pop", en="catorce y medio por ciento"),
    mano("(neto, antes de partidas excepcionales)", 700, 850, 40, t=1.8),
    masc("contento", 1650, 500, entra="der", t=0.2),
], fuente=RY + " (cálculo propio)")
escena("21", "Para ponerlo en perspectiva", "#E3E7EC", [
    mano("Beneficio por cada euro ingresado", 800, 190, 54, papel=True, t=0.2),
    rect(150, 290, 1000, 100, ROJO, texto="Ryanair  14,5 c", tam=44, en="catorce céntimos y medio", dur=0.8),
    rect(150, 430, 320, 100, AMAR, texto="Mercadona  ≈ 4 c", tam=36, en="Mercadona, unos cuatro", dur=0.8),
    rect(150, 570, 290, 100, VERDE, texto="Lidl  ≈ 3,6 c", tam=36, en="Lidl, tres y medio", dur=0.8),
    mano("Sectores muy distintos", 800, 800, 52, papel=True, en="sectores muy distintos"),
    masc("pensativo", 1660, 500, entra="der", t=0.2),
], fuente=RY + " · Mercadona, Memoria 2025 · Lidl España, comunicado 30/9/2026 (ejercicios distintos)")
escena("22", "Y esto no se detiene", "puerto_avion", [
    panel(), titulo("Lo que viene"),
    cifra(216, 450, 440, 170, sufijo=" M", en="doscientos dieciséis millones"), mano("pasajeros previstos (+4 %)", 450, 590, 44, en="doscientos dieciséis millones"),
    cifra(300, 1000, 440, 170, en="trescientos aviones"), mano("Boeing 737 MAX-10 encargados", 1000, 590, 44, en="trescientos aviones"),
    cifra(1900, 700, 800, 120, sufijo=" M€", en="mil novecientos millones"), mano("invertidos el último año", 700, 900, 44, en="invirtió"),
    masc("corriendo", 1660, 500, entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=RY)
escena("23", "Entonces, ¿cuál es el truco?", "#FFF3C4", [
    txt("Tres trucos, con sus cifras", 800, 220, 70, t=0.2),
    txt("1 · Llenar el avión (94 %)", 800, 420, 62, en="Uno: llenar el avión"),
    txt("2 · Un solo modelo de avión", 800, 580, 62, en="un solo modelo de avión"),
    txt("3 · Cobrar aparte lo que no es el asiento", 800, 740, 56, en="Y tres: cobrar aparte"),
    masc("pensativo", 1650, 500, entra="der", t=0.2),
], fuente=RY)
escena("24", "Y aquí entra la ley europea", "#E6E0F5", [
    sello("LA LEY EUROPEA", 800, 240, 76, t=0.2),
    mano("Precio final siempre visible:\ntarifa + impuestos + tasas obligatorias", 800, 470, 56, en="el precio final tiene que mostrarse"),
    mano("Extras opcionales: claros desde el principio,\ny aceptados de forma expresa", 800, 700, 52, papel=True, en="suplementos opcionales"),
    masc("lupa", 1640, 500, entra="der", t=0.2),
], fuente="Reglamento (CE) 1008/2008, art. 23.1")
escena("25", "Ahora, lo que no sabemos", "#E3E7EC", [
    sello("LO QUE NO SABEMOS", 800, 250, 80, t=0.2),
    mano("· Cuántos billetes vende a 10 € ni su margen", 800, 450, 50, en="cuántos billetes vende a diez euros"),
    mano("· La tarifa de 51 € es una media", 800, 580, 50, en="es una media"),
    mano("· Las cuentas son de todo el grupo, no solo de España", 800, 710, 48, en="de todo el grupo"),
    mano("Nadie con el dato dice «pierde en cada billete»", 800, 880, 44, papel=True, en="Así que cualquiera que te diga"),
    masc("encoge_hombros", 1660, 500, entra="der", t=0.2),
])
escena("26", "Así que, la próxima vez que mires", "supermercado", [
    panel(), titulo("El viaje de tu billete"),
    {"tipo": "tarta", "x": 420, "y": 640, "r": 260, "t": 0.3, "porciones": [
        {"v": 34.9, "color": ROJO, "en": "veintiséis, para combustible"},
        {"v": 12.0, "color": AMAR, "en": "Nueve, para el personal"},
        {"v": 11.3, "color": AZUL, "en": "para los aeropuertos"},
        {"v": 26.1, "color": GRIS, "en": "Diecinueve, para el resto"},
        {"v": 15.7, "color": VERDE, "en": "Y once, de beneficio"}]},
    *leyenda([("26 € · combustible", ROJO, "veintiséis, para combustible"), ("9 € · personal", AMAR, "Nueve, para el personal"),
              ("8,5 € · aeropuertos", AZUL, "para los aeropuertos"), ("19 € · resto", GRIS, "Diecinueve, para el resto"),
              ("11 € · beneficio", VERDE, "Y once, de beneficio")], x=760, y0=400, paso=100, tam=44),
    masc("saluda", 1660, 500, entra="der", t=0.2),
], fuente=RY + " (74,57 € por pasajero; cálculo propio, cifras redondeadas)")
escena("27", "Ryanair no gana dinero por regalar", "#FFF3C4", [
    txt("Llenar aviones", 800, 240, 80, t=0.3, en="llenar aviones"),
    txt("Gastar poco en cada uno", 800, 400, 76, en="gastar poco en cada uno"),
    txt("Cobrar aparte lo que no es el asiento", 800, 560, 64, en="cobrar aparte lo que no es el asiento"),
    txt("¿Cuánto de lo que pagas es tarifa y cuánto, extras?", 800, 800, 56, color=ROJO, anim="pop", rot=-2, en="La pregunta ya no es"),
    masc("pensativo", 1650, 500, entra="der", t=0.2),
])
escena("28", "Aquí, cada semana, abrimos", "#F5B301", [
    masc("saluda", 960, 560, entra="abajo", t=0.2),
    txt("TICKET MEDIO", 960, 170, 150, anim="pop", t=0.3),
    mano("Cada semana, el ticket de algo que pagas todos los días", 960, 300, 50, papel=True, t=1.0),
], sin_marca=True)
cfg = {"musica": "audio/musica.mp3", "musica_db": -26, "cola": 3, "escenas": E}
json.dump(cfg, open(os.path.join(V, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("escenas:", len(E))
