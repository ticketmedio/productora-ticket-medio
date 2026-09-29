"""Escribe salida/TEXTO_PUBLICACION.txt y fuentes.md de Pepa 013–018 (datos de investigacion_013_018.md)."""
import os

V = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos")
PIE = "Pepa es un personaje animado con IA; los datos, no 😉"
T = {
"013_castanas": ("Castañas asadas",
"""¿Castañas asadas en casa y te explotan en el horno? 🌰💥 ¡Qué susto en el gallinero!

El truco: antes de asarlas, hazles un corte en la piel, y así no estallan.

La castaña fresca tiene mucha agua (entre un 50 y un 60 %) y se estropea pronto: guárdala en una red, que ventile, y cómetela pronto… o congélala. Y ojo: las del parque, tan brillantes, son castañas de Indias. Esas no se comen. 🚫

📊 Fuentes: Ministerio de Agricultura (biblioteca), IGP Castaña de Galicia y ANSES (Francia).""",
"#castañas #otoño #cocina #trucosdecocina #recetasdeotoño #pepapita",
["Biblioteca del Ministerio de Agricultura, «La castaña» (J. Elorrieta), cap. XVII: el corte en la corteza, «para evitar su estallido». https://www.mapa.gob.es/ministerio/pags/biblioteca/fondo/pdf/37753_18.pdf",
 "Xunta de Galicia (AGACAL), documento único IGP «Castaña de Galicia» (diciembre de 2024): 50–60 % de humedad; venta en redes o congelada.",
 "ANSES (Francia): la castaña de Indias no es comestible."]),
"014_calabaza": ("La calabaza",
"""¿Vas a vaciar una calabaza para Halloween? 🎃 ¡No tires las pipas!

Octubre y noviembre son temporada alta de calabaza, y se aprovecha casi entera. Las pipas, tostadas, son pura proteína.

Pero ojo: las calabacitas de adorno no se comen. Y si una calabaza o un calabacín te sabe amargo, escúpelo y tíralo entero: cocinarlo no lo arregla. Lo que cortes, a la nevera; y si sobra mucha, al congelador. ❄️

📊 Fuentes: Ministerio de Agricultura (calendario de temporada), BEDCA, ANSES (Francia) y BfR (Alemania).""",
"#calabaza #halloween #otoño #cocina #trucosdecocina #pepapita",
["Ministerio de Agricultura, calendario «Hortalizas de temporada»: máxima comercialización de la calabaza de septiembre a marzo.",
 "BEDCA (AESAN), «Pipa de calabaza»: unos 30 g de proteína por 100 g. https://www.bedca.net/bdpub/",
 "ANSES (Francia), «Beware of inedible gourds!» (31/10/2019): las calabazas decorativas no se comen; si amarga, escupir y tirar.",
 "BfR (Alemania), aviso 027/2015 sobre calabacines amargos: las cucurbitacinas no se destruyen al cocinar."]),
"015_setas": ("Setas",
"""¿Te vas al monte a por setas? 🍄 ¡Quieta esa pluma! Si no la conoces, no la cojas. Y si te la regalan, tampoco.

Ningún truco sirve: ni la cuchara de plata, ni el ajo, ni que la haya mordido un bicho. La más peligrosa, la Amanita phalloides, sabe bien y no cambia de color, y casi todas las muertes por setas son por su tipo de veneno.

Si te encuentras mal, aunque sea horas después: 📞 112 o Toxicología, 91 562 04 20 (24 horas). Y lleva las setas que sobren.

📊 Fuentes: AESAN (consejos para la recolección de setas) e Instituto Nacional de Toxicología.""",
"#setas #otoño #micologia #seguridadalimentaria #cocina #pepapita",
["AESAN, «Consejos para la recolección y el autoconsumo de setas silvestres» (2020): no recolectar ni aceptar setas sin seguridad; los trucos populares son mitos.",
 "Instituto Nacional de Toxicología y Ciencias Forenses, «Prevención de intoxicaciones: por setas»: el 90 % de las muertes se debe a las amanitinas; síntomas tardíos (más de 6 horas).",
 "INTCF, Servicio de Información Toxicológica: 91 562 04 20, 24 horas. https://www.mjusticia.gob.es/es/institucional/organismos/instituto-nacional/servicios/servicio-informacion/servicio-informacion1"]),
"016_menu_otono": ("Menú barato de otoño",
"""¿Comer bien y barato en otoño? 🍂 ¡Apunta, que te hago el menú!

Legumbres, al menos cuatro días a la semana: son baratas y llenan. Pescado, tres veces (congelado o en lata también vale). Carne, como mucho tres. Y huevos, hasta cuatro.

De temporada: calabaza, coliflor, brócoli, coles, puerros y espinacas. Y de fruta, caquis, granadas, mandarinas y manzanas. Haz el menú el domingo y la lista con él: compras lo justo y no tiras nada. 📝

📊 Fuentes: AESAN (recomendaciones dietéticas, 2022) y calendarios de temporada del Ministerio de Agricultura.""",
"#menusemanal #comerbarato #otoño #recetasfaciles #cocina #pepapita",
["AESAN, «Recomendaciones dietéticas saludables y sostenibles» (2022): legumbres ≥ 4 raciones a la semana; pescado ≥ 3; carne 0–3; huevos hasta 4; planificar menú y compra.",
 "Ministerio de Agricultura, calendarios «Hortalizas de temporada» y «Frutas de temporada»: productos con máxima comercialización en octubre y noviembre."]),
"017_legumbres": ("Legumbres: remojo y cocción",
"""¿Alubias poco hechas? 🫘 ¡Ay, qué dolor de tripa!

Las legumbres crudas llevan lectinas, y si no se cocinan bien, sientan fatal. La receta de la agencia europea: remojo de 6 a 12 horas, tira esa agua, agua nueva y a hervir al menos media hora, hasta que estén blandas. Al vapor, al microondas o al horno quitan menos.

Y bien hechas, ¡a comerlas! Al menos cuatro veces por semana. Haz olla grande y congela en raciones. 🍲

📊 Fuentes: EFSA (lectinas, enero de 2026) y AESAN (recomendaciones dietéticas, 2022).""",
"#legumbres #lentejas #alubias #cocina #trucosdecocina #pepapita",
["EFSA, «Lectins in food: undercooked beans pose health risk» (28/01/2026) y opinión científica del Panel CONTAM: remojo de 6 a 12 horas, desechar el agua y hervir al menos 30 minutos a 100 °C; vapor, microondas u horno, menos eficaces. https://www.efsa.europa.eu/en/news/lectins-food-undercooked-beans-pose-health-risk-says-efsa",
 "AESAN, noticia sobre la opinión de la EFSA (28/01/2026).",
 "AESAN, «Recomendaciones dietéticas saludables y sostenibles» (2022): al menos 4 raciones de legumbres a la semana."]),
"018_pan_duro": ("El pan duro no se tira",
"""¿Tiras el pan de ayer? 🥖 ¡Ay, que se me cae la cresta!

En España, cada persona tiró en casa unos 23 kilos de comida en 2025, y el pan es de lo que más tiramos sin tocar.

¿Pan duro? Torrijas, migas, sopa de ajo o pan rallado. Y el pan se congela: en rebanadas, y sacas solo lo que vayas a usar. Eso sí: si tiene moho, a la basura entero. 🗑️

📊 Fuentes: Ministerio de Agricultura (desperdicio alimentario en los hogares 2025) y AESAN.""",
"#pan #nodesperdicies #torrijas #cocina #trucosdecocina #pepapita",
["Ministerio de Agricultura, «Informe sobre el desperdicio alimentario en los hogares 2025» y presentación del panel: 1.101,8 millones de kg o l; 23,51 kg por persona; pan fresco, 4,9 % de lo que se tira sin usar (5.º puesto).",
 "AESAN, «¿Congelas y descongelas los alimentos de forma segura en casa?» (2021): el pan se puede congelar.",
 "Moho: ver fuentes del vídeo 009 (AESAN y USDA)."]),
}

for v, (tit, texto, tags, fuentes) in T.items():
    d = os.path.join(V, v)
    os.makedirs(os.path.join(d, "salida"), exist_ok=True)
    with open(os.path.join(d, "salida", "TEXTO_PUBLICACION.txt"), "w", encoding="utf-8") as f:
        f.write(f"{texto}\n{PIE}\n\n{tags}\n")
    with open(os.path.join(d, "fuentes.md"), "w", encoding="utf-8") as f:
        f.write(f"# Fuentes — Pepa Pita {v[:3]} «{tit}»\n" + "".join(f"- {x}\n" for x in fuentes)
                + "- Detalle completo con citas literales: redes/pepa_pita/investigacion_013_018.md\n")
print("ok")
