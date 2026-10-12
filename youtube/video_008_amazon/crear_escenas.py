"""Genera escenas_v2.json del vídeo 8 (devoluciones de Amazon). Datos: INVESTIGACION.md (TRLGDCU, Ley 7/2022, Reg. UE 2024/1781, comunicado de Amazon 22/10/2021, ITV News vía Xataka)."""
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
E_ = []
def escena(id, desde, fondo, capas, **k): E_.append({"id": id, "desde": desde, "fondo": fondo, "capas": capas, **k})
AMAR, ROJO, AZUL, VERDE, GRIS = "#F5B301", "#E0521B", "#9CC5E8", "#8FD18F", "#D9D2C0"
LEY = "Real Decreto Legislativo 1/2007 (TRLGDCU), arts. 68, 71, 102–108"
AMZ = "Amazon, «¿Qué sucede en Amazon con los productos devueltos o no vendidos?» (22/10/2021)"

escena("01", "Devuelves un paquete a Amazon", "centro_logistico", [
    panel(), mano("Devuelves un paquete a Amazon…", 700, 230, 58, t=0.2),
    txt("¿Se revende?", 700, 430, 90, en="¿Se revende"), txt("¿Se regala?", 700, 600, 90, en="se regala"), txt("¿Se destruye?", 700, 770, 90, color=ROJO, en="¿Adónde va"),
    masc("pensativo", 1620, 520, entra="der", t=0.3),
], zoom=[1.0, 1.06])
escena("02", "Hoy vamos a abrir el ticket", "#FFF3C4", [
    txt("El ticket de una devolución", 800, 240, 76, t=0.2),
    sello("NO HAY CIFRAS PÚBLICAS", 800, 440, 66, en="no publica cuántos"),
    mano("Amazon no publica cuántos productos devueltos\nrevende, dona o destruye en España", 800, 650, 50, en="no publica cuántos"),
    mano("Sí hay: la ley · la empresa · la prensa", 800, 860, 54, papel=True, en="lo que dice la ley"),
    masc("encoge_hombros", 1620, 520, entra="der", t=0.2),
])
escena("03", "Primero, tu derecho", "oficina_financiera", [
    panel(), titulo("TU DERECHO"),
    cifra(14, 450, 450, 220, color=ROJO, en="catorce días naturales"), mano("días naturales para devolver", 450, 630, 46, en="catorce días naturales"),
    txt("sin explicar por qué\nsin penalización", 1010, 470, 56, en="sin tener que explicar"),
    mano("Ley General de Defensa de Consumidores (TRLGDCU)", 700, 850, 42, papel=True, en="Ley General para la Defensa"),
    masc("senala", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=LEY)
escena("04", "Ojo: no es lo mismo", "#E3E7EC", [
    mano("Ojo:", 800, 230, 70, t=0.2),
    txt("DERECHO LEGAL", 800, 400, 76, en="un derecho legal"), txt("≠", 800, 540, 90, color=ROJO, en="no es lo mismo"),
    txt("POLÍTICA DE LA TIENDA", 800, 700, 70, en="política de devoluciones"), mano("que puede ser más generosa", 800, 830, 52, en="no es lo mismo que la política"),
    masc("lupa", 1620, 520, entra="der", t=0.2),
])
escena("05", "Y la tienda tiene que devolverte", "#F4E9D0", [
    titulo("EL REEMBOLSO"),
    mano("Sin demoras indebidas y, en todo caso,", 700, 380, 54, en="sin demoras indebidas"),
    txt("en menos de 14 días", 700, 520, 90, color=ROJO, anim="pop", en="en menos de catorce días"),
    mano("desde que le comunicas que desistes", 700, 650, 52, en="que desistes"),
    mano("Puede esperar a recibir el producto\no a que le enseñes la prueba de envío", 700, 830, 50, papel=True, en="puede esperar a recibir"),
    masc("normal", 1640, 500, entra="der", t=0.2),
], fuente=LEY + " (art. 107)")
escena("06", "Hay excepciones", "#FFF3C4", [
    titulo("NO SE PUEDEN DEVOLVER, POR ESTA VÍA…"),
    txt("· hechos a medida o personalizados", 700, 380, 50, en="hechos a medida"),
    txt("· los que se estropean o caducan rápido", 700, 500, 50, en="se estropean o caducan"),
    txt("· precintados por higiene, ya abiertos", 700, 620, 50, en="los precintados"),
    txt("· discos o programas desprecintados", 700, 740, 50, en="ni los discos"),
    masc("encoge_hombros", 1640, 500, entra="der", t=0.2),
], fuente=LEY + " (art. 103)")
escena("07", "Y tú también tienes obligaciones", "#E6E0F5", [
    titulo("TUS OBLIGACIONES"),
    txt("· Devolver en 14 días desde que comunicas", 700, 360, 46, en="catorce días desde que comunicas"),
    txt("· Los costes directos de devolución son tuyos…", 700, 480, 46, en="costes directos"), mano("salvo que la tienda los asuma o no te informe", 700, 560, 40, en="no te haya informado"),
    txt("· Solo respondes si manipulas de más", 700, 690, 46, en="pérdida de valor"),
    txt("· La prueba del desistimiento es tuya", 700, 810, 46, color=ROJO, en="carga de la prueba"), mano("guarda el justificante", 700, 890, 42, en="guarda el justificante"),
    masc("senala", 1660, 500, mira="izq", entra="der", t=0.2),
], fuente=LEY + " (arts. 106 y 108)")
escena("08", "Ahora, la pregunta", "#FFF3C4", [
    txt("¿Qué pasa con tu paquete?", 800, 320, 90, t=0.3),
    masc("pensativo", 1620, 520, entra="der", t=0.2),
])
escena("09", "Según Amazon, en un comunicado", "centro_logistico", [
    panel(), titulo("SEGÚN AMAZON (oct. 2021)"),
    mano("Cada artículo devuelto pasa por\nuna inspección detallada", 700, 400, 52, en="una inspección detallada"),
    txt("¿Como nuevo? → se vende como NUEVO", 700, 590, 56, en="se etiqueta como nuevo"),
    mano("«La mayoría de los productos devueltos se pueden volver a vender así»", 700, 740, 44, papel=True, en="la mayoría de los productos"),
    mano("Es lo que cuenta la empresa; no hay cifra pública", 700, 880, 42, en="no hay una cifra pública"),
    masc("lupa", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente=AMZ)
escena("10", "Si no se puede vender como nuevo", "#F4E9D0", [
    titulo("SI NO SE PUEDE COMO NUEVO"),
    mano("Si el producto es de Amazon:", 700, 340, 52, en="Si es de Amazon"),
    rect(120, 400, 540, 90, AZUL, texto="Devolver al proveedor", tam=36, en="devolverlo al proveedor", dur=0.7),
    rect(120, 520, 540, 90, AMAR, texto="Venta como usado (Segunda Mano)", tam=32, en="Amazon Segunda Mano", dur=0.7),
    rect(120, 640, 540, 90, VERDE, texto="Donación (p. ej. Cruz Roja)", tam=34, en="Cruz Roja", dur=0.7),
    rect(120, 790, 540, 90, GRIS, texto="Solo sin otra opción: desechar", tam=32, en="Y solo si no queda otra opción", dur=0.7),
    mano("(higiene, motivos legales o dañado)", 960, 840, 42, en="por motivos legales"),
    masc("normal", 1680, 480, entra="der", t=0.2),
], fuente=AMZ)
escena("11", "Pero hay un detalle importante", "#E3E7EC", [
    cifra(50, 700, 330, 200, prefijo=">", sufijo=" %", color=ROJO, en="más de la mitad"),
    mano("de lo que se vende en Amazon (en todo el mundo)\nes de vendedores independientes", 700, 520, 52, en="vendedores independientes"),
    sello("ELLOS DECIDEN QUÉ HACER", 700, 760, 60, en="vendedores independientes"),
    mano("con lo que devuelves", 700, 880, 48, en="vendedores independientes", t=1.2),
    masc("senala", 1640, 500, mira="izq", entra="der", t=0.2),
], fuente=AMZ)
escena("12", "Para eso, Amazon les ofrece", "#FFF3C4", [
    titulo("LOS PROGRAMAS PARA VENDEDORES"),
    txt("FBA Liquidations", 700, 380, 76, en="FBA Liquidations"), mano("liquidar lo devuelto o no vendido\npor el canal mayorista de Amazon", 700, 510, 46, en="canal de liquidación mayorista"),
    txt("FBA Grade and Resell", 700, 660, 70, en="FBA Grade and Resell"), mano("revender lo devuelto como usado", 700, 750, 46, en="FBA Grade and Resell", t=1.0),
    mano("→ Una vía por la que un producto devuelto\npuede acabar en un lote de liquidación", 700, 880, 44, papel=True, en="Es una de las vías"),
    masc("lupa", 1660, 500, mira="izq", entra="der", t=0.2),
], fuente=AMZ)
escena("13", "Pero ojo: no podemos decirte", "#E6E0F5", [
    sello("PERO NO PODEMOS DECIR", 800, 360, 66, t=0.3),
    mano("de dónde sale cada palé o caja de devoluciones\nque ves en internet", 800, 760, 50, en="cada palé"),
    masc("encoge_hombros", 1620, 520, entra="der", t=0.2),
])
escena("14", "¿Y la destrucción?", "#FFF3C4", [
    titulo("ITV NEWS · REINO UNIDO · 2021"),
    mano("Según un exempleado, en una semana de abril\nel objetivo registrado era destruir…", 700, 380, 50, en="el objetivo registrado"),
    cifra(124000, 700, 610, 170, color=ROJO, en="ciento veinticuatro mil"), mano("productos, muchos de ellos nuevos", 700, 770, 50, en="ciento veinticuatro mil", t=1.5),
    masc("preocupado", 1660, 500, mira="izq", entra="der", t=0.2),
], fuente="ITV News (21/6/2021), según Xataka")
escena("15", "Amazon respondió", "#E3E7EC", [
    mano("Amazon respondió:", 800, 220, 60, t=0.2),
    txt("«Prioridad: revender, donar o reciclar»", 800, 380, 54, en="su prioridad es revender"),
    txt("«En el Reino Unido no se envían\nartículos a vertederos»", 800, 540, 54, en="no se envían artículos"),
    txt("«Trabajamos para llegar a cero»", 800, 730, 54, en="trabaja para llegar"),
    mano("Investigación británica y de hace 5 años:\nno se puede aplicar a España", 800, 890, 44, papel=True, en="no se puede aplicar"),
    masc("normal", 1660, 500, entra="der", t=0.2),
], fuente="Amazon, respuesta a ITV News (2021)")
escena("16", "Lo que sí cambia es la ley", "oficina_financiera", [
    panel(), titulo("ESPAÑA · LEY 7/2022"),
    mano("Prohibido destruir o llevar a vertedero\nlos excedentes no vendidos de productos\nno perecederos", 700, 400, 48, en="prohíbe destruir"),
    txt("Textiles · juguetes · aparatos eléctricos", 700, 640, 50, en="textiles, juguetes"),
    mano("Primero, a reutilización: incluida la donación", 700, 820, 46, papel=True, en="deben ir primero"),
    masc("senala", 1660, 500, mira="izq", entra="der", t=0.2),
], zoom=[1.0, 1.06], fuente="Ley 7/2022, de residuos y suelos contaminados, art. 18.2")
escena("17", "Y la Unión Europea va más lejos", "#F4E9D0", [
    titulo("UE · DESDE EL 19/7/2026"),
    mano("El Reglamento de ecodiseño prohíbe a las\ngrandes empresas destruir…", 700, 380, 50, en="prohíbe a las grandes empresas"),
    txt("ropa · complementos · calzado\nsin vender", 700, 580, 66, color=ROJO, en="destruir la ropa"),
    mano("Medianas empresas: desde 2030", 700, 820, 46, papel=True, t=2.5),
    masc("lupa", 1660, 500, mira="izq", entra="der", t=0.2),
], fuente="Reglamento (UE) 2024/1781, art. 25 y anexo VII")
escena("18", "La propia norma reconoce el motivo", "#E3E7EC", [
    mano("La propia norma reconoce el motivo:", 800, 230, 52, t=0.2),
    txt("«…debido, en particular, al rápido\ncrecimiento de las ventas en línea»", 800, 470, 56, en="rápido crecimiento"),
    mano("Excepciones: daños que no puedan repararse\nde forma rentable (también tras una devolución)", 800, 780, 46, papel=True, en="deja excepciones"),
    masc("pensativo", 1650, 500, entra="der", t=0.2),
], fuente="Reglamento (UE) 2024/1781, considerando 55 y art. 25.5")
escena("19", "Así que, ¿qué sabemos?", "#FFF3C4", [
    titulo("¿QUÉ SABEMOS?"),
    txt("✓ Tienes derecho a devolver", 700, 380, 50, en="derecho a devolver"),
    txt("✓ La ley obliga a reembolsarte", 700, 500, 50, en="obliga a reembolsarte"),
    txt("✓ La UE prohíbe destruir ropa y calzado\n   nuevos sin vender", 700, 640, 48, en="prohíbe destruir ropa"),
    txt("✓ Amazon dice: revender, donar, reciclar", 700, 800, 48, en="prioridad es revender"),
    masc("contento", 1660, 500, entra="der", t=0.2),
])
escena("20", "Y lo que no sabemos", "#E3E7EC", [
    sello("LO QUE NO SABEMOS", 800, 270, 80, t=0.2),
    mano("Cuántos productos devueltos acaban\nen cada camino", 800, 520, 60, en="cuántos productos devueltos"),
    mano("Esa cifra no es pública", 800, 740, 64, papel=True, en="no es pública"),
    txt("La respuesta honesta: depende", 800, 900, 56, color=ROJO, en="la más honesta posible"),
    masc("encoge_hombros", 1640, 500, entra="der", t=0.2),
])
escena("21", "Lo que devuelves a Amazon no tiene", "#FFF3C4", [
    txt("Varios caminos", 800, 270, 86, t=0.3, en="varios caminos"),
    txt("y la ley está cerrando uno", 800, 440, 66, color=ROJO, en="cerrando uno de ellos"),
    mano("¿Cuánto de lo que cuentan\nse puede comprobar?", 800, 700, 60, papel=True, en="la pregunta ya no es"),
    masc("pensativo", 1650, 500, entra="der", t=0.2),
])
escena("22", "Aquí, cada semana, abrimos", "#F5B301", [
    masc("saluda", 960, 560, entra="abajo", t=0.2),
    txt("TICKET MEDIO", 960, 170, 150, anim="pop", t=0.3),
    mano("Cada semana, el ticket de algo que pagas todos los días", 960, 300, 50, papel=True, t=1.0),
], sin_marca=True)
cfg = {"musica": "audio/musica.mp3", "musica_db": -26, "cola": 3, "escenas": E_}
json.dump(cfg, open(os.path.join(V, "escenas_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("escenas:", len(E_))
