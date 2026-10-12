"""Escenas del vídeo 9 (marcas blancas de Mercadona). Datos: INVESTIGACION.md."""
import json, os
V = os.path.dirname(os.path.abspath(__file__))
def panel(x=90, y=120, w=1230, h=870): return {"tipo": "panel", "x": x, "y": y, "w": w, "h": h, "t": 0}
def titulo(t, **k): return {"tipo": "texto", "texto": t, "x": 1010, "y": 200, "tam": 76, "papel": True, **({"t": 0.2} if not k else k)}
def txt(c, x, y, tam=60, **k): return {"tipo": "texto", "texto": c, "x": x, "y": y, "tam": tam, **k}
def mano(c, x, y, tam=56, **k): return txt(c, x, y, tam, fuente="mano", **k)
def cifra(n, x, y, tam=170, **k): return {"tipo": "cifra", "hasta": n, "x": x, "y": y, "tam": tam, **k}
def masc(p, x=1600, h=520, **k): return {"tipo": "mascota", "pose": p, "x": x, "y": 1015, "h": h, **k}
def sello(c, x, y, tam=70, **k): return {"tipo": "sello", "texto": c, "x": x, "y": y, "tam": tam, **k}
def rect(x, y, w, h, color, **k): return {"tipo": "rect", "x": x, "y": y, "w": w, "h": h, "color": color, **k}
E_ = []
def escena(i, d, f, c, **k): E_.append({"id": i, "desde": d, "fondo": f, "capas": c, **k})
AMAR, ROJO, AZUL, VERDE, GRIS = "#F5B301", "#E0521B", "#9CC5E8", "#8FD18F", "#D9D2C0"
UE = "Reglamento (UE) 1169/2011, arts. 8 y 9"; AE = "AESAN, Marca de identificación (Reg. CE 853/2004, anexo II)"
PR = "El Español (20/3/2026) y Cinco Días (7/1/2026), vía Xataka (23/2/2026)"

escena("01", "Mercadona tiene más de dos mil", "pasillo_marca_blanca", [
    panel(), mano("Mercadona · proveedores", 700, 230, 56, t=0.2),
    cifra(2000, 380, 420, 150, prefijo="+", en="más de dos mil proveedores"), mano("proveedores e interproveedores", 380, 540, 40, en="más de dos mil proveedores"),
    cifra(4, 1000, 420, 170, color=ROJO, en="cuatro de ellos"), mano("facturan > 1.000 M€ cada uno", 1000, 540, 40, en="mil millones de euros cada uno"),
    sello("¿QUIÉN FABRICA TU MARCA BLANCA?", 700, 800, 56, en="¿quién fabrica de verdad"),
    masc("pensativo", 1630, 520, entra="der", t=0.3),
], zoom=[1.0, 1.06], fuente=PR)
escena("02", "Y aquí va lo sorprendente", "#FFF3C4", [
    txt("La ley NO obliga a que\nla etiqueta te lo diga", 800, 330, 80, color=ROJO, anim="pop", t=0.4, en="la ley no obliga"),
    masc("sorprendido", 1620, 520, entra="der", t=0.2),
])
escena("03", "Hoy vamos a abrir el ticket", "#E3E7EC", [
    txt("El ticket de una marca blanca", 800, 260, 76, t=0.2),
    mano("No vamos a repartir un euro:\nvamos a seguir la pista", 800, 480, 56, en="seguir la pista"),
    mano("Con la ley y los datos públicos", 800, 730, 56, papel=True, en="con la ley en la mano"),
    masc("lupa", 1620, 520, entra="der", t=0.2),
])
escena("04", "Empecemos por la etiqueta", "pasillo_marca_blanca", [
    panel(), titulo("LA ETIQUETA"),
    mano("Responsable de la información:", 700, 360, 52, en="responsable de la información"),
    txt("quien lo COMERCIALIZA", 700, 480, 76, color=ROJO, en="comercializa el alimento"),
    mano("Nombre y dirección de ese operador", 700, 650, 52, en="nombre y la dirección"),
    txt("quien lo vende ≠ quien lo fabrica", 700, 820, 60, papel=True, en="de quien lo vende"),
    masc("senala", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=UE)
escena("05", "La Agencia Española de Seguridad", "#F4E9D0", [
    titulo("EL Nº DE REGISTRO SANITARIO"),
    mano("«Es meramente de identificación administrativa»", 700, 400, 50, en="identificación administrativa"),
    txt("El operador NO está obligado a\nponerlo en la etiqueta", 700, 600, 62, color=ROJO, en="no está obligado"),
    mano("…salvo en la marca sanitaria", 700, 830, 52, papel=True, t=2.5),
    masc("normal", 1640, 500, entra="der", t=0.2),
], fuente="AESAN, Empresas/Establecimientos alimentarios registrados en España (RGSEAA)")
escena("06", "La excepción son los productos", "fabrica_alimentos", [
    panel(), titulo("LA EXCEPCIÓN: ORIGEN ANIMAL"),
    mano("Carne · leche · queso · pescado", 700, 360, 54, en="carne, leche, queso"),
    {"tipo": "moneda", "texto": "ES", "r": 130, "x": 400, "y": 640, "color": "#FFFDF6", "en": "las siglas del país"},
    txt("nº de autorización\ndel establecimiento", 920, 640, 54, en="número de autorización"),
    mano("Marca ovalada en el envase o la etiqueta: «la pista que sí tienes»", 700, 880, 44, en="es la pista"),
    masc("lupa", 1670, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=AE)
escena("07", "Y con ese número puedes hacer algo", "#E6E0F5", [
    titulo("EL BUSCADOR DE LA AESAN"),
    mano("1 · Apunta el nº del óvalo", 700, 380, 56, en="Y con ese número"),
    mano("2 · Búscalo en el registro público", 700, 520, 56, en="buscador público"),
    mano("3 → qué establecimiento es", 700, 660, 56, en="qué empresa está inscrita"),
    sello("OJO: NO DICE PARA QUIÉN FABRICA", 700, 860, 52, en="no para quién fabrica"),
    masc("encoge_hombros", 1640, 500, entra="der", t=0.2),
], fuente="AESAN, consulta al registro RGSEAA")
escena("08", "Hay excepciones", "#FFF3C4", [
    titulo("NO LLEVAN LA MARCA"),
    txt("· Huevos con código de centro de embalaje", 700, 380, 46, en="los huevos"),
    txt("· Productos compuestos (animal + vegetal)", 700, 510, 46, en="productos compuestos"),
    txt("· Productos vegetales: pasta, galletas…", 700, 640, 46, en="productos vegetales"),
    masc("normal", 1660, 500, entra="der", t=0.2),
], fuente=AE)
escena("09", "Entonces, ¿qué sabemos", "oficina_financiera", [
    panel(), titulo("LOS PROVEEDORES"),
    cifra(2000, 450, 450, 150, prefijo="+", en="más de dos mil proveedores"), mano("proveedores e interproveedores\nespecialistas (memoria)", 450, 590, 42, en="más de dos mil proveedores"),
    cifra(14000, 1020, 450, 150, prefijo="+", t=1.0), mano("en todo el ecosistema\n(con servicios y transporte)", 1020, 590, 42, t=1.2),
    masc("saluda", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=PR)
escena("10", "En dos mil veinticinco, según la propia cadena", "fabrica_alimentos", [
    panel(), titulo("INVERSIÓN 2025 (según Mercadona)"),
    cifra(1700, 440, 440, 140, sufijo=" M€", en="mil setecientos millones"), mano("de proveedores", 440, 570, 44, en="mil setecientos millones"),
    cifra(5200, 1000, 440, 140, en="cinco mil doscientos"), mano("empleos creados", 1000, 570, 44, en="cinco mil doscientos"),
    mano("Casa Tarradellas 117 · Vall Companys 70\nAvinatur 60 · Incarlopsa 60 (M€)", 700, 820, 46, papel=True, en="Casa Tarradellas"),
    masc("contento", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="El Español (20/3/2026), a partir de la información de Mercadona")
escena("11", "Y hay otra fuente", "#F4E9D0", [
    titulo("LAS CUENTAS DEL REGISTRO MERCANTIL"),
    mano("Los 20 mayores proveedores, en 2024:", 700, 360, 52, en="los veinte mayores"),
    cifra(12000, 700, 540, 170, prefijo="+", sufijo=" M€", en="más de doce mil millones"), mano("de ventas", 700, 660, 48, en="más de doce mil millones"),
    txt("+18 % frente a 2022", 700, 800, 66, color="#2E8B57", en="dieciocho por ciento"),
    masc("pensativo", 1660, 500, entra="der", t=0.2),
], fuente="Cinco Días (7/1/2026), vía Xataka (23/2/2026)")
escena("12", "Cuatro de ellos superaron", "#E3E7EC", [
    mano("Superaron los 1.000 millones de euros:", 800, 210, 54, papel=True, t=0.2),
    rect(150, 310, 1000, 100, AMAR, texto="Casa Tarradellas", tam=46, en="Casa Tarradellas", dur=0.7),
    rect(150, 440, 1000, 100, AZUL, texto="Incarlopsa", tam=46, en="Incarlopsa", dur=0.7),
    rect(150, 570, 1000, 100, VERDE, texto="J. García Carrión", tam=46, en="García Carrión", dur=0.7),
    rect(150, 700, 1000, 100, GRIS, texto="Covap", tam=46, en="García Carrión", t=1.5, dur=0.7),
    masc("senala", 1660, 500, mira="izq", entra="der", t=0.2),
], fuente="Cinco Días (7/1/2026), vía Xataka (23/2/2026): ventas de 2024")
escena("13", "Ojo con lo que significa", "#FFF3C4", [
    sello("OJO", 800, 240, 90, t=0.2),
    mano("Ser proveedor de Mercadona ≠ fabricar\nsu marca blanca", 800, 470, 54, en="no quiere decir que todo"),
    mano("Y no todo lo que venden\nlo compra Mercadona", 800, 700, 54, en="ni que todo lo que vende"),
    masc("encoge_hombros", 1620, 520, entra="der", t=0.2),
])
escena("14", "Aun así, hay un dato revelador", "#E6E0F5", [
    mano("Hay empresas que declaran que sus ventas\nligadas a Mercadona son del…", 800, 250, 52, t=0.2),
    cifra(53, 450, 560, 190, sufijo=" %", en="cincuenta y tres"), cifra(94, 1150, 560, 190, sufijo=" %", color=ROJO, en="noventa y cuatro"),
    mano("(el diario no dice cuáles)", 800, 840, 46, papel=True, t=2.0),
    masc("sorprendido", 1670, 500, entra="der", t=0.2),
], fuente="Cinco Días (7/1/2026), vía Xataka")
escena("15", "Y ahora, la cuenta que nos gusta", "#FFF3C4", [
    mano("Beneficio por cada euro de ventas", 800, 190, 54, papel=True, t=0.2),
    rect(150, 290, 820, 110, AMAR, texto="Mercadona ≈ 4,1 c", tam=46, en="Mercadona, en su último", dur=0.8),
    rect(150, 430, 750, 110, AZUL, texto="Sus 20 mayores proveedores ≈ 3 c", tam=40, en="unos tres céntimos", dur=0.8),
    mano("360 M€ de beneficio / 12.000 M€ de ventas", 800, 640, 46, en="trescientos sesenta"),
    mano("Cálculo propio: ejercicios distintos y ventas\nno solo a Mercadona. Con prudencia.", 800, 800, 42, papel=True, en="un cálculo nuestro"),
    masc("lupa", 1670, 500, mira="izq", entra="der", t=0.2),
], fuente="Cinco Días (2024) · Mercadona, Memoria Anual 2025 · cálculo propio")
escena("16", "Vamos con lo que no sabemos", "#E3E7EC", [
    sello("LO QUE NO SABEMOS", 800, 250, 80, t=0.2),
    mano("No hay una lista pública oficial que diga\nqué fábrica hace cada producto", 800, 480, 50, en="ninguna lista pública oficial"),
    mano("Ni la memoria ni la prensa la dan", 800, 680, 52, papel=True, en="ni la memoria"),
    txt("No diremos «X fabrica Y»", 800, 860, 60, color=ROJO, en="no te vamos a decir"),
    masc("encoge_hombros", 1640, 500, entra="der", t=0.2),
])
escena("17", "Lo que sí puedes hacer", "pasillo_marca_blanca", [
    panel(), titulo("LO QUE SÍ PUEDES HACER"),
    mano("Mira el óvalo de tu etiqueta", 700, 400, 60, en="mirar el óvalo"),
    mano("Apunta el número", 700, 560, 60, en="apuntar el número"),
    mano("Consulta el registro de la AESAN", 700, 720, 60, en="consultar el registro"),
    txt("La única pista oficial", 700, 880, 56, color=ROJO, en="la única pista oficial"),
    masc("senala", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=AE)
escena("18", "Así que, la próxima vez que cojas", "supermercado", [
    panel(), titulo("EL VIAJE DE TU MARCA BLANCA"),
    mano("Etiqueta → el nombre de quien lo vende", 700, 400, 52, en="el nombre de quien lo vende"),
    mano("Óvalo → (si lo lleva) el nº de la fábrica", 700, 560, 52, en="el número de la fábrica"),
    mano("Detrás → miles de proveedores", 700, 720, 52, en="miles de proveedores"),
    txt("≈ 3 c de beneficio por euro", 700, 880, 58, color=ROJO, en="tres céntimos por euro"),
    masc("saluda", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06])
escena("19", "La marca blanca no tiene", "#FFF3C4", [
    txt("Miles de fabricantes", 800, 270, 84, t=0.3, en="miles de ellos"),
    mano("¿Quién fabrica tu producto?", 800, 460, 62, en="la pregunta ya no es"),
    txt("¿Por qué la ley deja que no lo sepas?", 800, 700, 66, color=ROJO, anim="pop", rot=-2, en="por qué la ley"),
    masc("pensativo", 1650, 500, entra="der", t=0.2),
])
escena("20", "Aquí, cada semana, abrimos", "#F5B301", [
    masc("saluda", 960, 560, entra="abajo", t=0.2),
    txt("TICKET MEDIO", 960, 170, 150, anim="pop", t=0.3),
    mano("Cada semana, el ticket de algo que pagas todos los días", 960, 300, 50, papel=True, t=1.0),
], sin_marca=True)
json.dump({"musica": "audio/musica.mp3", "musica_db": -26, "cola": 3, "escenas": E_}, open(os.path.join(V, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("escenas:", len(E_))
