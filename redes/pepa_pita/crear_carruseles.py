"""Carruseles de Pepa Pita para el muro de Instagram y Facebook (1080x1350, 4:5).

Uso: python redes/pepa_pita/crear_carruseles.py
Salida: redes/pepa_pita/carruseles/<id>/01.png, 02.png... + TEXTO_PUBLICACION.txt
Todos los datos salen de los textos ya verificados de los vídeos (archivo/pepa_pita/*/fuentes.md).
"""
import os, re, sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8")
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", ".."))
REC = os.path.join(AQUI, "recortes")
TITULAR = os.path.join(RAIZ, "herramientas", "fuentes", "ArchivoBlack-Regular.ttf")
TEXTO = "C:/Windows/Fonts/segoeuib.ttf"
TEXTO_FINO = "C:/Windows/Fonts/segoeui.ttf"
W, H = 1080, 1350
ROJO, AMARILLO, TINTA, PAPEL, GRIS = (224, 96, 79), (245, 179, 1), (18, 22, 28), (251, 250, 246), (110, 110, 110)
VERDE = (46, 139, 87)


def f(ruta, tam):
    return ImageFont.truetype(ruta, tam)


def ajustar(d, txt, fuente, ancho):
    """Parte el texto en líneas que quepan en «ancho» píxeles."""
    txt = re.sub(r"(\d) (°C|h\b|horas|hora|días|minutos?)", lambda m: m.group(1) + "\u00a0" + m.group(2), txt)  # espacio duro: no separa número y unidad
    lineas, linea = [], ""
    for p in txt.split(" "):
        prueba = (linea + " " + p).strip()
        if d.textlength(prueba, font=fuente) <= ancho:
            linea = prueba
        else:
            lineas.append(linea)
            linea = p
    lineas.append(linea)
    return lineas


def parrafo(d, txt, fuente, x, y, ancho, color, interlinea=1.25):
    for l in ajustar(d, txt, fuente, ancho):
        d.text((x, y), l, font=fuente, fill=color)
        y += int(fuente.size * interlinea)
    return y


def pepa(lienzo, nombre, alto, x, y):
    im = Image.open(os.path.join(REC, nombre + ".png")).convert("RGBA")
    esc = alto / im.height
    im = im.resize((int(im.width * esc), alto), Image.LANCZOS)
    lienzo.alpha_composite(im, (x, y))


def base(n, total, fuente_txt):
    lienzo = Image.new("RGBA", (W, H), PAPEL + (255,))
    d = ImageDraw.Draw(lienzo)
    d.rectangle([0, 0, W, 18], fill=AMARILLO)
    d.text((60, H - 70), "@soypepapita", font=f(TEXTO, 30), fill=TINTA)
    pie = f"{n}/{total}"
    d.text((W - 60 - d.textlength(pie, font=f(TEXTO, 30)), H - 70), pie, font=f(TEXTO, 30), fill=GRIS)
    if fuente_txt:
        parrafo(d, "Fuente: " + fuente_txt, f(TEXTO_FINO, 24), 60, H - 125, W - 120, GRIS)
    return lienzo, d


def portada(titulo, sub, pose, n, total):
    lienzo, d = base(n, total, None)
    y = 110
    for l in ajustar(d, titulo, f(TITULAR, 96), W - 120):
        d.text((60, y), l, font=f(TITULAR, 96), fill=TINTA)
        y += 112
    y = parrafo(d, sub, f(TEXTO, 44), 60, y + 20, W - 120, ROJO)
    pepa(lienzo, pose, 640, W - 480, H - 760)
    d.rounded_rectangle([60, H - 330, 470, H - 240], radius=45, fill=AMARILLO)
    d.text((95, H - 315), "Desliza  →", font=f(TITULAR, 44), fill=TINTA)
    return lienzo


def ficha_numero(cifra, que, detalle, fuente_txt, n, total, cara="exp_contenta"):
    lienzo, d = base(n, total, fuente_txt)
    tam = 230 if len(cifra) <= 5 else 170
    d.text((60, 120), cifra, font=f(TITULAR, tam), fill=ROJO)
    y = 120 + int(tam * 1.25)
    y = parrafo(d, que, f(TITULAR, 64), 60, y, W - 120, TINTA, 1.15)
    parrafo(d, detalle, f(TEXTO_FINO, 50), 60, y + 30, W - 120, TINTA, 1.3)
    pepa(lienzo, cara, 300, W - 280, H - 460)
    return lienzo


def ficha_mito(mito, realidad, fuente_txt, n, total, cara="exp_pensativa"):
    lienzo, d = base(n, total, fuente_txt)
    d.rounded_rectangle([60, 110, 330, 180], radius=35, fill=ROJO)
    d.text((95, 118), "MITO", font=f(TITULAR, 46), fill=PAPEL)
    y = parrafo(d, "«" + mito + "»", f(TITULAR, 62), 60, 220, W - 120, TINTA, 1.15)
    y += 50
    d.rounded_rectangle([60, y, 420, y + 70], radius=35, fill=VERDE)
    d.text((95, y + 8), "REALIDAD", font=f(TITULAR, 46), fill=PAPEL)
    parrafo(d, realidad, f(TEXTO_FINO, 50), 60, y + 110, W - 120, TINTA, 1.3)
    pepa(lienzo, cara, 300, W - 280, H - 460)
    return lienzo


def cierre(frase, llamada, pose, n, total):
    lienzo, d = base(n, total, None)
    y = parrafo(d, frase, f(TITULAR, 80), 60, 130, W - 120, TINTA, 1.15)
    parrafo(d, llamada, f(TEXTO, 46), 60, y + 30, W - 120, ROJO, 1.3)
    pepa(lienzo, pose, 560, (W - 330) // 2, H - 720)
    return lienzo


def guardar(ident, fichas, texto):
    carpeta = os.path.join(AQUI, "carruseles", ident)
    os.makedirs(carpeta, exist_ok=True)
    for i, im in enumerate(fichas, 1):
        im.convert("RGB").save(os.path.join(carpeta, f"{i:02d}.png"), optimize=True)
    open(os.path.join(carpeta, "TEXTO_PUBLICACION.txt"), "w", encoding="utf-8").write(texto.strip() + "\n")
    print(ident, len(fichas), "imágenes")


# ── Carrusel 001: lunes 5/10/2026, 13:00 ──
T = 8
guardar("001_numeros_cocina", [
    portada("6 números que tu cocina tiene que saber", "Guárdatelo: te va a salvar más de una cena.", "pose_senala", 1, T),
    ficha_numero("5 °C", "La nevera, como máximo", "Si tienes un termómetro de nevera, mejor aún: 4 °C.", "AESAN", 2, T),
    ficha_numero("2 h", "Lo cocinado, fuera de la nevera", "Nunca más de 2 horas a temperatura ambiente. Si hace más de 30 °C, solo 1 hora.", "AESAN", 3, T, "exp_preocupada"),
    ficha_numero("3 días", "Las sobras en la nevera", "Como mucho. Apunta la fecha en el táper.", "AESAN y OMS", 4, T, "exp_pensativa"),
    ficha_numero("1 vez", "Recalentar las sobras", "Solo una, y que queden muy calientes por todas partes. Recalienta solo lo que te vayas a comer.", "OMS y AESAN", 5, T, "exp_guino"),
    ficha_numero("74 °C", "En el interior del pollo", "Lo que mata las bacterias es el calor, no lavarlo. Lavarlo solo las reparte por la cocina.", "EFSA/ECDC (informe de zoonosis 2024)", 6, T, "exp_sorprendida"),
    ficha_numero("−15 °C", "El pescado para el anisakis", "Congélalo a −15 °C o menos y cuenta al menos 5 días antes de comerlo crudo o en vinagre.", "AESAN, cartel sobre la anisakiasis (3.ª ed., 2025)", 7, T, "exp_preocupada"),
    cierre("¿Cuál no sabías?", "Mándaselo a quien deja la olla fuera toda la tarde.", "exp_guino", 8, T),
], """
6 números que tu cocina tiene que saber 📌 Guárdatelo.

🌡️ 5 °C: la nevera, como máximo.
⏱️ 2 horas: lo cocinado, fuera de la nevera (1 si hace más de 30 °C).
📅 3 días: las sobras en la nevera.
🔁 1 vez: recalentar, y muy caliente por todas partes.
🐔 74 °C: en el interior del pollo.
🐟 −15 °C y 5 días: el pescado, contra el anisakis.

¿Cuál no sabías? Mándaselo a quien deja la olla fuera toda la tarde 😉

📊 Fuentes: AESAN (campaña de verano, «Pon en orden tu nevera», cartel sobre la anisakiasis de 2025), OMS y EFSA/ECDC.
Pepa es un personaje animado con IA; los datos, no 😉

#seguridadalimentaria #trucosdecocina #cocina #nevera #pepapita
""")

# ── Carrusel 002: miércoles 7/10/2026, 13:00 ──
T = 7
guardar("002_mitos_cocina", [
    portada("5 mitos de cocina que te creíste", "Pepa los desmonta con datos. ¿Cuántos te sabías?", "pose_ojo", 1, T),
    ficha_mito("Lavar el pollo lo deja más limpio", "El agua salpica y reparte bacterias como la Campylobacter por el fregadero y la encimera. Lo que las mata es el calor: 74 °C en el interior.", "EFSA/ECDC (informe de zoonosis 2024)", 2, T, "exp_preocupada"),
    ficha_mito("Los huevos, mejor lavados antes de guardarlos", "La cáscara tiene una capa invisible que tapa sus poros. Si la mojas, el agua puede meter la salmonela hacia dentro. En la UE, los huevos del súper no se pueden lavar.", "AESAN y Reglamento (UE) 2023/2465", 3, T),
    ficha_mito("El vinagre mata el anisakis", "No. Ni el vinagre ni la sal de casa. Lo matan el frío (−15 °C o menos, al menos 5 días) o el calor (60 °C durante 1 minuto en toda la pieza).", "AESAN, cartel sobre la anisakiasis (2025)", 4, T, "exp_sorprendida"),
    ficha_mito("El arroz de ayer se arregla recalentándolo", "Si se enfría despacio, el Bacillus cereus fabrica una toxina que resiste hasta 121 °C. Lo que sobre, a la nevera antes de 2 horas.", "AESAN, ficha sobre Bacillus cereus (2026)", 5, T),
    ficha_mito("Lo descongelado nunca se puede volver a congelar", "Crudo, no. Pero si lo cocinas a más de 70 °C durante 2 minutos, ese guiso sí puede ir al congelador.", "AESAN, «¿Congelas y descongelas de forma segura?»", 6, T, "exp_guino"),
    cierre("¿Cuál te creías tú?", "Cuéntamelo en los comentarios y mándaselo a quien lava el pollo.", "exp_riendo", 7, T),
], """
5 mitos de cocina que te creíste 🐔 ¿Cuántos te sabías?

❌ Lavar el pollo lo deja más limpio → reparte las bacterias; lo que las mata es el calor (74 °C dentro).
❌ Los huevos, mejor lavados → el agua puede meter la salmonela; en la UE no se lavan.
❌ El vinagre mata el anisakis → no: congelar a −15 °C, al menos 5 días, o cocinar a 60 °C durante 1 minuto.
❌ El arroz de ayer se arregla recalentándolo → su toxina resiste hasta 121 °C.
❌ Lo descongelado nunca se recongela → si lo cocinas antes, sí.

¿Cuál te creías tú? Cuéntamelo 👇 y mándaselo a quien lava el pollo.

📊 Fuentes: AESAN (fichas de salmonelosis y Bacillus cereus, cartel sobre la anisakiasis de 2025, guía de congelación), EFSA/ECDC (zoonosis 2024) y Reglamento (UE) 2023/2465.
Pepa es un personaje animado con IA; los datos, no 😉

#seguridadalimentaria #mitos #trucosdecocina #cocina #pepapita
""")
