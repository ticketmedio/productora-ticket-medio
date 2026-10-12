"""Escenas del vídeo 10 (súper más barato, estudio OCU 2026). Datos: INVESTIGACION.md."""
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
OCU = "OCU, estudio de supermercados 2026 (25/9/2026)"
escena("01", "Entre el supermercado más barato", "pasillo_marca_blanca", [
    panel(), mano("Entre el súper más barato y el más caro de tu ciudad…", 700, 220, 48, t=0.2),
    cifra(1310, 700, 400, 190, sufijo=" €", color="#2E8B57", en="mil trescientos diez euros"), mano("de ahorro medio al año", 700, 540, 52, en="un hogar medio ahorra"),
    cifra(4381, 700, 730, 150, sufijo=" €", color=ROJO, en="cuatro mil trescientos ochenta y uno"), mano("en Madrid capital", 700, 860, 52, en="En Madrid"),
    masc("sorprendido", 1630, 520, entra="der", t=0.3),
], zoom=[1.0, 1.06], fuente=OCU)
escena("02", "¿Y cuál es el más barato", "#FFF3C4", [
    txt("¿Cuál es el más barato?", 800, 280, 86, t=0.3), txt("Depende de dónde vivas", 800, 480, 70, color=ROJO, en="Depende de dónde vivas"),
    mano("690 supermercados · el mayor estudio que existe", 800, 720, 54, papel=True, en="el mayor estudio"),
    masc("pensativo", 1620, 520, entra="der", t=0.2),
])
escena("03", "Abrimos el ticket del súper", "#E3E7EC", [
    txt("El ticket del súper", 800, 260, 80, t=0.2),
    mano("No hemos comprado una cesta:\nusamos el estudio de la OCU 2026", 800, 480, 56, en="usamos el estudio"),
    mano("Publicado el 25 de septiembre", 800, 720, 52, papel=True, en="veinticinco de septiembre"),
    masc("lupa", 1620, 520, entra="der", t=0.2),
], fuente=OCU)
escena("04", "Primero, cómo se hizo", "calle_comercial", [
    panel(), titulo("CÓMO SE HIZO"),
    cifra(690, 400, 440, 150, en="seiscientos noventa establecimientos"), mano("establecimientos", 400, 560, 42, en="seiscientos noventa establecimientos"),
    cifra(38, 820, 440, 150, en="treinta y ocho ciudades"), mano("ciudades", 820, 560, 42, en="treinta y ocho ciudades"),
    cifra(244, 1200, 440, 150, en="doscientos cuarenta y cuatro productos"), mano("productos", 1200, 560, 42, en="doscientos cuarenta y cuatro productos"),
    mano("Abril y mayo de 2026 · marcas y marcas blancas", 700, 800, 46, papel=True, en="abril y mayo"),
    masc("saluda", 1670, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=OCU)
escena("05", "Con eso construye un índice", "#F4E9D0", [
    titulo("EL ÍNDICE"),
    txt("La más barata = 100", 700, 380, 70, en="la tienda más barata vale cien"),
    txt("Índice 110 = un 10 % más cara", 700, 560, 66, color=ROJO, en="una tienda con índice ciento diez"),
    mano("Cada punto de más = un 1 % más caro", 700, 760, 52, en="cada punto de más"),
    masc("normal", 1660, 500, entra="der", t=0.2),
], fuente=OCU)
escena("06", "Vamos con el ranking de cadenas", "#FFF3C4", [
    mano("Ranking de cadenas (índice OCU)", 800, 190, 56, papel=True, t=0.2),
    rect(150, 290, 480, 100, VERDE, texto="Dani 100", tam=44, en="Dani, con índice cien", dur=0.7),
    rect(150, 410, 560, 100, VERDE, texto="Family Cash · Tifer 102", tam=40, en="Family Cash y Tifer", dur=0.7),
    rect(150, 530, 620, 100, AMAR, texto="Alcampo · Supeco 103", tam=40, en="Alcampo y Supeco", dur=0.7),
    rect(150, 700, 1050, 100, ROJO, texto="Sánchez Romero 176", tam=44, en="Sánchez Romero", dur=0.8),
    masc("senala", 1660, 500, mira="izq", entra="der", t=0.2),
], fuente=OCU)
escena("07", "Y aquí viene lo curioso", "centro_comercial", [
    panel(), titulo("EL MÁS BARATO VISITADO"),
    txt("Un Alcampo en un centro comercial\nde Aldaia (Valencia)", 700, 460, 62, en="un Alcampo"),
    mano("No es de una cadena pequeña", 700, 740, 54, papel=True, en="no es de una cadena"),
    masc("sorprendido", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=OCU)
escena("08", "Pero la gran noticia", "supermercado", [
    panel(), titulo("LIDL GANA TERRENO"),
    cifra(18, 450, 450, 190, color="#9A9A9A", en="El año pasado eran dieciocho"), mano("localidades el año anterior", 450, 620, 42, en="El año pasado eran dieciocho"),
    cifra(60, 1050, 450, 210, color=ROJO, en="sesenta de las localidades"), mano("localidades donde es la más barata", 1050, 640, 42, en="sesenta de las localidades"),
    mano("Mercadona duplica las suyas · Supeco 18 → 28", 700, 850, 46, papel=True, en="Mercadona también duplica"),
    masc("riendo", 1670, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=OCU)
escena("09", "Porque las grandes cadenas", "#E6E0F5", [
    mano("Cesta OCU: variación en el año", 800, 190, 54, papel=True, t=0.2),
    rect(150, 290, 760, 90, VERDE, texto="Carrefour Market −2,7 %", tam=40, en="Carrefour Market", dur=0.7),
    rect(150, 400, 600, 90, VERDE, texto="Lidl −1,9 %", tam=40, en="Lidl, un uno coma nueve", dur=0.7),
    rect(150, 510, 580, 90, VERDE, texto="Mercadona −1,8 %", tam=40, en="Mercadona, un uno coma ocho", dur=0.7),
    rect(150, 620, 520, 90, VERDE, texto="Aldi −1,4 %", tam=40, en="Aldi, un uno coma cuatro", dur=0.7),
    rect(150, 760, 640, 90, ROJO, texto="BM Urban +5,1 % · Ahorramás +4,4 %", tam=34, en="BM Urban sube", dur=0.8),
    masc("lupa", 1670, 500, mira="izq", entra="der", t=0.2),
], fuente=OCU)
escena("10", "Y fíjate dónde se baja", "#FFF3C4", [
    titulo("DÓNDE SE BAJA"),
    mano("Cesta económica", 450, 360, 52, en="la cesta económica"), txt("Mercadona −5,6 %\nLidl −4,7 %", 450, 520, 60, color="#2E8B57", en="Mercadona baja un cinco coma seis"),
    mano("Cesta de marcas de fabricante", 1030, 360, 46, en="cesta de marcas"), txt("+2,5 %\nde media", 1030, 520, 76, color=ROJO, en="suben de media"),
    masc("encoge_hombros", 1680, 500, mira="izq", entra="der", t=0.2),
], fuente=OCU)
escena("11", "Es decir: las grandes cadenas", "#E3E7EC", [
    mano("Las grandes cadenas compiten con…", 800, 250, 56, t=0.2),
    txt("productos económicos\ny de marca propia", 800, 460, 72, en="productos económicos"),
    mano("La marca de fabricante, mientras tanto, sube", 800, 760, 54, papel=True, en="La marca de fabricante"),
    masc("pensativo", 1650, 500, entra="der", t=0.2),
], fuente=OCU)
escena("12", "Eso sí, no todo baja", "pasillo_marca_blanca", [
    panel(), titulo("NO TODO BAJA"),
    cifra(1.8, 450, 440, 170, sufijo=" %", dec=1, en="un uno coma ocho"), mano("sube la Cesta OCU", 450, 590, 42, en="un uno coma ocho"),
    cifra(149, 960, 440, 150, color=ROJO, en="ciento cuarenta y nueve"), mano("productos más caros", 960, 580, 42, en="ciento cuarenta y nueve"),
    cifra(92, 1240, 440, 150, color="#2E8B57", en="noventa y dos"), mano("más baratos", 1240, 580, 42, en="noventa y dos"),
    masc("normal", 1680, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=OCU)
escena("13", "Los frescos suben un cuatro", "#F4E9D0", [
    titulo("LOS FRESCOS: +4,7 %"),
    rect(150, 300, 1000, 100, ROJO, texto="Pescado +8,6 %", tam=46, en="un ocho coma seis", dur=0.8),
    rect(150, 430, 560, 100, AMAR, texto="Carne +3,7 %", tam=46, en="la carne, un tres coma siete", dur=0.8),
    rect(150, 560, 540, 100, AZUL, texto="Frutas y verduras +3,5 %", tam=40, en="un tres coma cinco", dur=0.8),
    masc("preocupado", 1670, 500, entra="der", t=0.2),
], fuente=OCU)
escena("14", "Y si miramos más atrás", "#FFF3C4", [
    titulo("DESDE 2021"),
    cifra(40, 450, 450, 190, prefijo="≈ ", sufijo=" %", color=ROJO, en="casi un cuarenta por ciento"), mano("sube la Cesta OCU", 450, 620, 44, en="casi un cuarenta por ciento"),
    txt("Café molido económico +142 %\nHuevos M +135 %", 1030, 480, 50, en="El café molido económico"),
    mano("Solo cuestan menos: detergente,\nyogur natural y bebida de arroz", 1030, 740, 40, en="Solo tres productos"),
    masc("sorprendido", 1690, 500, mira="izq", entra="der", t=0.2),
], fuente=OCU)
escena("15", "Ahora, las ciudades", "#E3E7EC", [
    mano("Nivel de precios por localidad (índice OCU)", 800, 190, 50, papel=True, t=0.2),
    rect(150, 290, 450, 90, VERDE, texto="Torrent 100", tam=40, en="Torrent, en Valencia", dur=0.7),
    rect(150, 400, 1000, 90, ROJO, texto="Getxo · Pozuelo · Majadahonda 114", tam=38, en="Getxo, Pozuelo", dur=0.8),
    rect(150, 540, 780, 90, AMAR, texto="Barcelona 110", tam=40, en="Barcelona, con ciento diez", dur=0.7),
    rect(150, 650, 740, 90, AMAR, texto="Bilbao · San Sebastián 109", tam=38, en="Bilbao y San Sebastián", dur=0.8),
    masc("senala", 1670, 500, mira="izq", entra="der", t=0.2),
], fuente=OCU)
escena("16", "Y la diferencia en euros", "oficina_financiera", [
    panel(), titulo("EL AHORRO POSIBLE AL AÑO"),
    rect(150, 300, 1000, 90, ROJO, texto="Madrid 4.381 €", tam=44, en="cuatro mil trescientos ochenta", dur=0.8),
    rect(150, 410, 520, 90, AMAR, texto="Barcelona ≈ 1.823 €", tam=40, en="mil ochocientos veintitrés", dur=0.8),
    rect(150, 520, 480, 90, AZUL, texto="Zaragoza · Vigo ≈ 1.950–2.150 €", tam=36, en="entre mil novecientos", dur=0.8),
    rect(150, 630, 160, 90, VERDE, texto="Mieres 381 €", tam=34, en="trescientos ochenta y uno", dur=0.8),
    mano("«Incluso allí, comparar sale a cuenta»", 700, 850, 46, papel=True, en="comparar sale a cuenta"),
    masc("moneda", 1680, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=OCU)
escena("17", "Ahora, lo que hay que tener", "#FFF3C4", [
    sello("A TENER EN CUENTA", 800, 230, 70, t=0.2),
    mano("· Depende de las cadenas que tengas cerca", 800, 400, 46, en="depende de las cadenas"),
    mano("· Es una media de abril y mayo", 800, 520, 46, en="media de abril y mayo"),
    mano("· No recoge los efectos de la guerra de Irán", 800, 640, 46, en="guerra de Irán"),
    mano("· El ranking completo es de pago", 800, 760, 46, en="es de pago"),
    masc("encoge_hombros", 1650, 500, entra="der", t=0.2),
], fuente=OCU)
escena("18", "Así que, la próxima vez que vayas", "supermercado", [
    panel(), titulo("EL VIAJE DE TU COMPRA"),
    mano("Tienda barata vs cara de tu ciudad:", 700, 400, 52, en="la tienda más barata y la más cara"),
    txt("≈ 1.300 € al año de media", 700, 540, 72, color="#2E8B57", en="mil trescientos euros"),
    mano("Bajan: productos económicos y marca propia", 700, 730, 48, en="bajan precios en productos"),
    mano("Suben: marcas de fabricante", 700, 840, 48, color=ROJO, en="de fabricante suben"),
    masc("saluda", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=OCU)
escena("19", "No hay un supermercado más barato", "#FFF3C4", [
    txt("No hay un súper más barato\npara todo el mundo", 800, 320, 76, t=0.3),
    txt("¿Cuál es el más barato\ndonde tú vives?", 800, 640, 70, color=ROJO, anim="pop", rot=-2, en="la pregunta ya no es"),
    masc("pensativo", 1650, 500, entra="der", t=0.2),
])
escena("20", "Aquí, cada semana, abrimos", "#F5B301", [
    masc("saluda", 960, 560, entra="abajo", t=0.2), txt("TICKET MEDIO", 960, 170, 150, anim="pop", t=0.3),
    mano("Cada semana, el ticket de algo que pagas todos los días", 960, 300, 50, papel=True, t=1.0),
], sin_marca=True)
json.dump({"musica": "audio/musica.mp3", "musica_db": -26, "cola": 3, "escenas": E_}, open(os.path.join(V, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("escenas:", len(E_))
