"""Escribe salida/TEXTO_PUBLICACION.txt y fuentes.md de Pepa 007–012 (datos de investigacion_007_012.md)."""
import os

V = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos")
PIE = "Pepa es un personaje animado con IA; los datos, no 😉"
T = {
"007_tabla_de_cortar": ("Tabla de cortar",
"""¿Cortas el pollo crudo y luego la ensalada en la misma tabla? 🔪🐔 ¡Alto ahí, que me desplumo!

Las bacterias de lo crudo se quedan en la tabla y pasan a lo que ya no vas a cocinar. Lo ideal: una tabla para lo crudo y otra para lo que va directo a la boca.

¿Solo tienes una? Primero la verdura, la carne al final, y después agua caliente y jabón. ¿Madera o plástico? Las dos valen; el plástico se limpia más fácil. Y cuando tenga surcos, a la basura. 🗑️

📊 Fuentes: AESAN, OMS (5 claves), FSA (Reino Unido) y USDA (EE. UU.).""",
"#cocina #trucosdecocina #seguridadalimentaria #tabladecortar #recetasfaciles #pepapita",
["AESAN, campaña «Recomendaciones de seguridad alimentaria para el verano», punto 6: lo cocinado se contamina por contacto con tablas que han tocado lo crudo. https://www.aesan.gob.es/actualidad/campanyas-seguridad-alimentaria/campania_verano",
 "OMS, Manual de las cinco claves (2007), clave 2: utensilios y tablas diferentes para lo crudo.",
 "FSA (Reino Unido), Why avoiding cross-contamination is important (18/12/2017): orden verdura → carne y lavar con jabón.",
 "USDA/FSIS, Cutting Boards (27/08/2024): madera o superficie no porosa; la no porosa se limpia más fácil; agua caliente y jabón; tirar la tabla con surcos."]),
"008_sobras": ("Las sobras",
"""¿Dejas la olla en el fuego toda la tarde para que se enfríe? 🍲 ¡Ay, que se me ponen las plumas de punta!

Las sobras, a la nevera cuanto antes: nunca más de 2 horas fuera, y 1 si hace más de 30 °C. Repártelas en táperes pequeños y no los apiles, que así se enfrían antes.

En la nevera, 3 días como mucho, con la fecha apuntada. ¿Recalentar? Solo lo que te vayas a comer, una sola vez y que humee por todas partes. Sopas y salsas, que hiervan. 🔥

📊 Fuentes: AESAN (campaña de verano, «De tu cocina a la oficina» y ficha Bacillus cereus 2026) y OMS.""",
"#sobras #cocina #trucosdecocina #seguridadalimentaria #tuppers #pepapita",
["AESAN, campaña de verano, punto 5: sobras a la nevera lo antes posible, no más de 2 horas a temperatura ambiente.",
 "AESAN, De tu cocina a la oficina (2016): 1 hora si hace más de 30 °C; no más de 3 días en la nevera; recalentar a más de 75 °C; hervir sopas y salsas.",
 "AESAN, ficha Bacillus cereus (14/01/2026): porciones y no apilar los recipientes.",
 "OMS, Manual de las cinco claves (2007), clave 4: sobras no más de 3 días y recalentar una sola vez."]),
"009_moho": ("El moho",
"""¿Le quitas el moho a la mermelada y te la comes? 🍓 ¡Ni se te ocurra!

Lo que ves es solo la punta: el moho tiene raíces por dentro, y algunos fabrican toxinas que no se van al cocinar.

Pan, mermelada, yogur, queso fresco o rallado y sobras con moho: a la basura, enteros. La fruta y la verdura, también enteras. ¿El queso curado? En EE. UU. aconsejan cortar al menos 2,5 cm alrededor y por debajo, sin tocar el moho con el cuchillo. Y no lo huelas. 👃🚫

📊 Fuentes: AESAN (micotoxinas; tríptico de frutas y verduras 2024) y USDA (EE. UU.).""",
"#moho #cocina #trucosdecocina #seguridadalimentaria #nodesperdicies #pepapita",
["AESAN, página Micotoxinas: las micotoxinas no suelen desaparecer con el cocinado. https://www.aesan.gob.es/seguridad-alimentaria/contaminantes-quimicos/micotoxinas",
 "AESAN, tríptico Frutas y verduras siempre seguras (2024): si hay hongos, descartar la pieza entera.",
 "USDA/FSIS, Molds on Food: Are They Dangerous? (22/08/2013): raíces del moho; qué alimentos se tiran; queso duro: cortar al menos 1 pulgada (2,5 cm); no olerlo."]),
"010_mayonesa_casera": ("Mayonesa casera",
"""¿Mayonesa casera para la ensaladilla? 🥚 ¡Qué rica! Pero ojo: el huevo crudo puede traer salmonela, y la mayonesa no se cocina.

En Europa, la salmonela en el huevo es la pareja que más brotes da. Así que hazla justo antes de comer, casca los huevos en otro cuenco y no los laves. Siempre en la nevera, y lo que sobre ese día, a la basura. 🗑️

¿Sabías que en bares y restaurantes, por ley, la mayonesa que no se cocina se hace con huevo pasteurizado?

📊 Fuentes: AESAN (ficha Salmonelosis), EFSA/ECDC (informe de zoonosis 2024) y Real Decreto 1021/2022, art. 9.""",
"#mayonesa #ensaladilla #cocina #seguridadalimentaria #trucosdecocina #pepapita",
["AESAN, ficha Salmonelosis: huevo crudo; cascar en otro recipiente; menor antelación posible; refrigerar; desechar lo que no se consuma en el día; no lavar los huevos.",
 "EFSA/ECDC, The European Union One Health 2024 Zoonoses Report (09/12/2025): Salmonella en huevos y ovoproductos, la pareja agente/alimento que más preocupa (83 brotes con pruebas sólidas en 2024).",
 "Real Decreto 1021/2022, art. 9 (BOE 21/12/2022): sin tratamiento térmico, ovoproductos en lugar de huevo crudo. El RD 1254/1991 está derogado. https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681"]),
"011_lavar_la_fruta": ("Lavar la fruta",
"""¿Lavas la fruta con un chorrito de lavavajillas? 🍎 ¡Alto, que eso no!

La fruta y la verdura, bajo el grifo, con agua corriente, aunque las vayas a pelar: así, al cortar, no arrastras lo de la piel hacia dentro. Sin jabón, que la fruta lo puede absorber. Melón, sandía o pepino, con un cepillo.

¿Lechuga, o fruta que te comes con piel? Puedes desinfectarla con lejía que ponga «apta para la desinfección del agua de bebida». Sigue la dosis de la etiqueta y aclara con mucha agua. 💧

📊 Fuentes: AESAN (tríptico de frutas y verduras 2024), Ministerio de Consumo y FDA (EE. UU.).""",
"#fruta #verdura #cocina #trucosdecocina #seguridadalimentaria #pepapita",
["AESAN, tríptico Frutas y verduras siempre seguras (2024): bajo el grifo aunque se vayan a pelar; cepillo para piel dura; con lejía, consultar la etiqueta.",
 "Ministerio de Derechos Sociales, Consumo y Agenda 2030, Frutas y verduras siempre seguras: lejía «apta para la desinfección de agua de bebida», aclarar con abundante agua.",
 "FDA (EE. UU.), Selecting and Serving Produce Safely (05/03/2024): no lavar con jabón ni detergentes; la fruta es porosa.",
 "Real Decreto 3360/1983: la lejía apta para agua de bebida debe indicar la cantidad en la etiqueta."]),
"012_la_nevera": ("La nevera por dentro",
"""¿Tu nevera parece un tetris? 🧊 ¡Vamos a ordenarla!

Temperatura: 5 °C o menos; mejor, 4. Un termómetro de nevera cuesta muy poco.

Arriba, lo cocinado y lo listo para comer. Debajo, la carne y el pescado crudos, bien tapados, para que no goteen. En los cajones, la fruta y la verdura. No la llenes hasta arriba, que el aire frío tiene que circular. Y la puerta es lo que más se calienta: ahí, bebidas y salsas. 🥤

📊 Fuentes: AESAN («Pon en orden tu nevera» y campaña de verano), OMS, FDA y USDA (EE. UU.).""",
"#nevera #orden #cocina #trucosdecocina #seguridadalimentaria #pepapita",
["AESAN, campaña de verano, punto 4: frío a 5 °C como máximo. OMS (2007), clave 4: preferiblemente por debajo de 5 °C.",
 "FDA (EE. UU.), Are You Storing Food Safely? (18/01/2023): nevera a 4 °C o menos; no llenarla tanto que el aire no circule.",
 "AESAN, Pon en orden tu nevera (2016): de arriba abajo, cocinado, crudo y frutas y verduras en el cajón; recipientes cerrados. https://www.aesan.gob.es/dam/jcr:66cc3ec1-1894-4fef-8197-fe8489aef934/nevera.pdf",
 "USDA/FSIS, Refrigeration and Food Safety (23/03/2015): la temperatura de la puerta es la que más cambia."]),
}

for v, (tit, texto, tags, fuentes) in T.items():
    d = os.path.join(V, v)
    os.makedirs(os.path.join(d, "salida"), exist_ok=True)
    with open(os.path.join(d, "salida", "TEXTO_PUBLICACION.txt"), "w", encoding="utf-8") as f:
        f.write(f"{texto}\n{PIE}\n\n{tags}\n")
    with open(os.path.join(d, "fuentes.md"), "w", encoding="utf-8") as f:
        f.write(f"# Fuentes — Pepa Pita {v[:3]} «{tit}»\n" + "".join(f"- {x}\n" for x in fuentes)
                + "- Detalle completo con citas literales: redes/pepa_pita/investigacion_007_012.md\n")
print("ok")
