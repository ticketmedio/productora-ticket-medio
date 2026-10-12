"""Carruseles 007–015 de Pepa Pita (26/10 → 14/12/2026). Reutilizan las funciones de crear_carruseles.py.
Cada dato sale de las fichas verificadas de redes/pepa_pita/lote/ y de investigacion_013_018.md."""
import os
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "crear_carruseles.py"), encoding="utf-8").read()
exec(_src.split("# ── Carrusel 001")[0])

# ── 007 · lunes 26/10 · otoño: castañas y calabaza ──
T = 7
guardar("007_otono_castanas_calabaza", [
    portada("Castañas y calabaza: lo que casi nadie sabe", "Cuatro avisos para el otoño. Guárdalo.", "pose_senala", 1, T),
    ficha_numero("1 CORTE", "Antes de asar las castañas", "Hazles un pequeño corte en la cáscara para que no estallen. Lo recoge un texto clásico digitalizado por el Ministerio de Agricultura de España (no es una guía actual).", "MAPA (Biblioteca digital, J. Elorrieta y Artaza)", 2, T, "exp_contenta"),
    ficha_veredicto("NO SE COME", ROJO, "La castaña de Indias (la de los parques)", "Se confunde con la castaña dulce: en Francia, es el 11 % de las confusiones registradas por la agencia ANSES.", "ANSES (Francia), 2019", 3, T, "exp_preocupada"),
    ficha_veredicto("NO SE COME", ROJO, "Las calabazas decorativas", "Las de adorno se consideran tóxicas. Revisa la etiqueta o pregunta en la tienda.", "ANSES (Francia), 2019", 4, T, "exp_pensativa"),
    ficha_veredicto("ESCÚPELA Y TÍRALA", AMARILLO, "Si una calabaza o calabacín amarga", "Prueba un trocito crudo: si amarga, tírala entera. Las cucurbitacinas no se destruyen al cocinar.", "ANSES (Francia) y BfR (Alemania)", 5, T, "exp_sorprendida"),
    ficha_numero("RED", "La castaña fresca se vende en red", "Tiene entre un 50 y un 60 % de humedad al recogerla, por eso se vende en embalajes que ventilan, o congelada.", "Xunta de Galicia (IGP Castaña de Galicia, 2024)", 6, T, "exp_guino"),
    cierre("¿Cuál no sabías?", "Compártelo con quien asa castañas en casa.", "exp_riendo", 7, T),
], """
Castañas y calabaza: lo que casi nadie sabe 🌰🎃 Guárdalo para este otoño.

✂️ Castañas: un pequeño corte en la cáscara para que no estallen.
🚫 La castaña de Indias (la de los parques) no se come.
🚫 Las calabazas decorativas tampoco.
😖 Si una calabaza o un calabacín amarga: tírala entera. Cocinarla no lo arregla.
🕸️ La castaña fresca se vende en red porque tiene mucha agua.

¿Cuál no sabías? Compártelo con quien asa castañas en casa 😉

📊 Fuentes: Ministerio de Agricultura de España (texto clásico digitalizado), ANSES (Francia), BfR (Alemania) y Xunta de Galicia.
Pepa es un personaje animado con IA; los datos, no 😉

#otoño #castañas #calabaza #seguridadalimentaria #pepapita
""")

# ── 008 · miércoles 28/10 · setas ──
T = 7
guardar("008_setas_mitos", [
    portada("Setas: 5 mitos que pueden matar", "Si no las conoces, no las cojas.", "pose_ojo", 1, T),
    ficha_mito("Si ennegrece una cuchara de plata, es tóxica", "Falso. La Amanita phalloides, que puede ser mortal, no lo hace.", "AESAN, «Consejos para la recolección de setas» (2020)", 2, T, "exp_preocupada"),
    ficha_mito("Hervirlas o cocinarlas elimina el veneno", "Falso. Hay toxinas muy peligrosas que aguantan el tratamiento térmico.", "AESAN (2020)", 3, T, "exp_sorprendida"),
    ficha_mito("Si huelen o saben bien, son comestibles", "Falso. La Amanita phalloides tiene un sabor agradable y puede ser mortal.", "AESAN (2020)", 4, T),
    ficha_mito("Si las comen los caracoles, no son venenosas", "Falso. No sabemos si los animales han muerto o morirán tras comerlas.", "AESAN (2020)", 5, T, "exp_pensativa"),
    ficha_veredicto("LA REGLA", VERDE, "Si no la conoces, no la cojas", "Consulta a una persona experta o a una asociación micológica de tu zona. Y no te fíes solo de una foto.", "AESAN (2020)", 6, T, "exp_contenta"),
    cierre("¿Cuál te creías?", "Compártelo con quien va a buscar setas este otoño. Si te sientes mal: urgencias (en España, 112) con una muestra.", "exp_preocupada", 7, T),
], """
Setas: 5 mitos que pueden matar 🍄 Si no las conoces, no las cojas.

❌ «Si ennegrece la plata, es tóxica» → falso.
❌ «Hervirlas elimina el veneno» → falso: hay toxinas que aguantan el calor.
❌ «Si huele o sabe bien, es comestible» → falso.
❌ «Si las comen los caracoles, no son venenosas» → falso.
✅ Regla: ante la duda, consulta a una persona experta o a una asociación micológica de tu zona. Y no te fíes solo de una foto.

Si te sientes mal tras comerlas: urgencias con una muestra (en España, 112).

Compártelo con quien va a buscar setas este otoño.

📊 Fuente: AESAN, «Consejos para la recolección y el autoconsumo de setas silvestres» (2020).
Pepa es un personaje animado con IA; los datos, no 😉

#setas #micología #seguridadalimentaria #otoño #pepapita
""")

# ── 009 · lunes 2/11 · pan duro y legumbres ──
T = 7
guardar("009_pan_duro_legumbres", [
    portada("Pan duro y legumbres: dos errores de cocina", "Uno cuesta dinero. El otro puede sentarte mal.", "pose_sartenes", 1, T),
    ficha_numero("23,5 kg", "Comida que tira cada persona al año", "Los hogares españoles tiraron 1.101,8 millones de kilos o litros en 2025: 23,51 kg por persona.", "MAPA, informe sobre desperdicio alimentario 2025", 2, T, "exp_preocupada"),
    ficha_numero("4,9 %", "Es pan fresco", "De lo que se tira sin usar, el pan fresco es el 4,9 % (5.º puesto) y su volumen subió un 4 % respecto a 2024.", "MAPA (2025)", 3, T, "exp_pensativa"),
    ficha_numero("CONGELA", "El pan se puede congelar", "Divide en raciones y apunta la fecha. La AESAN no da un tiempo para el pan congelado.", "AESAN, «¿Congelas y descongelas de forma segura?»", 4, T, "exp_contenta"),
    ficha_numero("6–12 h", "Legumbres: el remojo", "Remójalas de 6 a 12 horas hasta que se ablanden y cambia el agua.", "EFSA y AESAN (enero de 2026)", 5, T, "exp_guino"),
    ficha_numero("30 min", "Y hiérvelas a 100 °C", "Al menos media hora. Al vapor, en microondas o al horno es menos eficaz. Las alubias poco cocidas llevan lectinas que dan náuseas, vómitos y diarrea.", "EFSA y AESAN (enero de 2026)", 6, T, "exp_sorprendida"),
    cierre("¿Tú qué hacías?", "Compártelo con quien tira el pan o cocina las alubias con prisa.", "exp_riendo", 7, T),
], """
Pan duro y legumbres: dos errores de cocina 🍞🫘

🗑️ Cada persona tiró en España 23,51 kg de comida en 2025 (MAPA).
🍞 El pan fresco es el 4,9 % de lo que se tira sin usar. Se puede congelar.
🫘 Legumbres: remojo de 6 a 12 horas, cambia el agua y hierve al menos media hora a 100 °C.
⚠️ Alubias poco cocidas = lectinas: náuseas, vómitos y diarrea.

Guárdalo y compártelo con quien tira el pan 😉

📊 Fuentes: MAPA (desperdicio 2025), AESAN y EFSA (lectinas, enero de 2026).
Pepa es un personaje animado con IA; los datos, no 😉

#pan #legumbres #nodesperdicies #seguridadalimentaria #pepapita
""")

# ── 010 · lunes 9/11 · etiquetas y huevos ──
T = 7
guardar("010_etiquetas_huevos_suelo", [
    portada("Etiquetas, huevos y suelo: 3 dudas resueltas", "Lo que dice la norma, no el «yo siempre lo he hecho así».", "pose_ojo", 1, T),
    ficha_veredicto("NO ES LO MISMO", AMARILLO, "Consumo preferente ≠ caducidad", "El consumo preferente es hasta cuándo conserva sus propiedades. Pasado, baja la calidad. La fecha de caducidad es otra cosa: pasada, no se considera seguro.", "Reglamento (UE) 1169/2011", 2, T, "exp_pensativa"),
    ficha_numero("1 · 2 · 3", "El primer número del huevo", "1 = camperas (aire libre) · 2 = criadas en el suelo · 3 = en jaula. Después, el país y la granja.", "Reglamento Delegado (UE) 2023/2465", 3, T, "exp_contenta"),
    ficha_numero("L", "Las letras son por peso", "XL: 73 g o más · L: de 63 a menos de 73 g · M: de 53 a menos de 63 g · S: menos de 53 g.", "Reglamento Delegado (UE) 2023/2465", 4, T, "exp_guino"),
    ficha_veredicto("CASI MEJOR NO", ROJO, "La regla de los 5 segundos", "Un estudio de Rutgers (EE. UU.) vio que cuanto más tiempo, más bacterias pasan, y que algo se transfiere desde menos de 1 segundo. Fue con una bacteria de laboratorio.", "Universidad de Rutgers (2016)", 5, T, "exp_preocupada"),
    ficha_numero("OJO", "Importa qué cae y dónde", "En ese estudio, la sandía recogió más bacterias que una gominola.", "Applied and Environmental Microbiology (2016)", 6, T, "exp_sorprendida"),
    cierre("¿Cuál no sabías?", "Compártelo con quien siempre dice «solo han sido 5 segundos».", "exp_riendo", 7, T),
], """
Etiquetas, huevos y suelo: 3 dudas resueltas 🥚

📅 Consumo preferente no es caducidad: tras la caducidad, no se considera seguro.
🥚 El primer número del huevo: 1 camperas, 2 suelo, 3 jaula.
⚖️ Las letras (S, M, L, XL) son por peso.
🍪 La regla de los 5 segundos: un estudio de Rutgers vio que algo se transfiere en menos de 1 segundo.

Compártelo con quien siempre dice «solo han sido 5 segundos» 😅

📊 Fuentes: Reglamento (UE) 1169/2011, Reglamento Delegado (UE) 2023/2465 y estudio de la Universidad de Rutgers (2016).
Pepa es un personaje animado con IA; los datos, no 😉

#huevos #etiquetas #seguridadalimentaria #trucosdecocina #pepapita
""")

# ── 011 · lunes 16/11 · congelar bien ──
T = 8
guardar("011_congelar_bien", [
    portada("Congelar bien: guía en 6 pasos", "Para que no pierdas comida ni sabor.", "pose_aplaude", 1, T),
    ficha_numero("−18 °C", "La temperatura del congelador", "Se recomienda congelar a menos de −18 °C.", "AESAN, «¿Congelas y descongelas de forma segura?»", 2, T, "exp_contenta"),
    ficha_numero("RACIONES", "No congeles en un solo bloque", "Divide en raciones individuales o según las personas de la casa: se congela antes y no tiras nada.", "AESAN", 3, T, "exp_guino"),
    ficha_numero("FRÍO", "Nunca lo metas caliente", "Déjalo enfriar en la nevera antes de pasarlo al congelador. Apunta qué es y la fecha.", "AESAN", 4, T, "exp_preocupada"),
    ficha_numero("12 h", "Descongela en la nevera", "Sácalo con al menos 12 horas de antelación, en la parte más fría. Entre 5 y 65 °C los microorganismos se reproducen más rápido.", "AESAN", 5, T, "exp_pensativa"),
    ficha_veredicto("NO SE RECONGELA", AMARILLO, "Lo descongelado", "Salvo que lo cocines a más de 70 °C durante al menos 2 minutos.", "AESAN", 6, T, "exp_sorprendida"),
    ficha_veredicto("MEJOR NO", ROJO, "Qué no congelar", "Pierden sabor o textura (no son peligrosos): lechuga, tomate, patatas, huevos con cáscara, mayonesa y fritos.", "AESAN", 7, T, "exp_pensativa"),
    cierre("¿Qué congelabas mal?", "Guárdalo y compártelo con quien congela todo en un bloque.", "exp_riendo", 8, T),
], """
Congelar bien: guía en 6 pasos 🧊 Guárdala.

1️⃣ A −18 °C o menos.
2️⃣ En raciones, no en un bloque.
3️⃣ Nunca caliente: primero enfría en la nevera. Apunta la fecha.
4️⃣ Descongela en la nevera, con 12 horas de antelación.
5️⃣ Lo descongelado no se vuelve a congelar, salvo que lo cocines a más de 70 °C durante 2 minutos.
6️⃣ Mejor no congelar: lechuga, tomate, patatas, huevos con cáscara, mayonesa y fritos (pierden sabor o textura).

Compártelo con quien congela todo en un bloque 😅

📊 Fuente: AESAN, «¿Congelas y descongelas los alimentos de forma segura en casa?».
Pepa es un personaje animado con IA; los datos, no 😉

#congelar #cocina #seguridadalimentaria #trucosdecocina #pepapita
""")

# ── 012 · lunes 23/11 · sobras y táper ──
T = 7
guardar("012_sobras_taper", [
    portada("Sobras y táper: las reglas de las 2 horas", "Para que el táper de mañana no te sorprenda.", "pose_sartenes", 1, T),
    ficha_numero("2 h", "Fuera de la nevera, como máximo", "Una sola hora si hace más de 30 °C.", "AESAN, «De tu cocina a la oficina»", 2, T, "exp_preocupada"),
    ficha_numero("FRÍO", "No metas el guiso caliente", "Déjalo enfriar antes de guardarlo: meterlo caliente afecta a la temperatura de los demás alimentos.", "Ministerio de Consumo de España", 3, T, "exp_pensativa"),
    ficha_numero("70 °C", "Al recalentar, también en el centro", "Todas las partes deben llegar al menos a 70 °C durante 15 segundos. (La AESAN, para el táper del trabajo, pide más de 75 °C.)", "Ministerio de Consumo y AESAN", 4, T, "exp_sorprendida"),
    ficha_numero("SOLO LO QUE COMES", "Cada recalentado suma riesgo", "Recalienta solo la cantidad que te vas a comer.", "Ministerio de Consumo de España", 5, T, "exp_guino"),
    ficha_numero("COPA Y TENEDOR", "Fíjate en el recipiente", "Debe llevar el símbolo de la copa y el tenedor o «para contacto con alimentos», y el del microondas si lo vas a calentar ahí.", "AESAN", 6, T, "exp_contenta"),
    cierre("¿Cuál no cumples?", "Compártelo con quien deja el táper toda la mañana fuera.", "exp_riendo", 7, T),
], """
Sobras y táper: las reglas de las 2 horas 🥡

⏱️ Máximo 2 horas fuera de la nevera (1 si hace más de 30 °C).
❄️ No metas el guiso caliente: déjalo enfriar antes.
🔥 Al recalentar, todo el alimento, también el centro, a 70 °C durante 15 segundos como mínimo (la AESAN pide más de 75 °C para el táper del trabajo).
🍽️ Recalienta solo lo que te vas a comer.
🥄 Recipiente con el símbolo de la copa y el tenedor.

Compártelo con quien deja el táper toda la mañana fuera 😅

📊 Fuentes: Ministerio de Consumo de España y AESAN («De tu cocina a la oficina»).
Pepa es un personaje animado con IA; los datos, no 😉

#sobras #táper #seguridadalimentaria #trucosdecocina #pepapita
""")

# ── 013 · lunes 30/11 · embarazo y pescado ──
T = 7
guardar("013_embarazo_pescado_navidad", [
    portada("Embarazo y fiestas: qué evitar", "Lo que dice el Ministerio de Consumo. Ante la duda, tu médico.", "pose_senala", 1, T),
    ficha_veredicto("EVITAR", ROJO, "Huevo crudo y lo que lo lleve", "Mayonesas y salsas caseras, mousses, merengues, tiramisú, helados caseros y ponches de huevo.", "Ministerio de Consumo de España", 2, T, "exp_preocupada"),
    ficha_veredicto("EVITAR", ROJO, "Carne o pescado crudos", "La carne, bien cocinada, hasta 71 °C. Evita también el pescado crudo y los moluscos crudos.", "Ministerio de Consumo de España", 3, T, "exp_pensativa"),
    ficha_veredicto("EVITAR", ROJO, "Pez espada, tiburón, atún rojo y lucio", "Acumulan mercurio. Se evitan en el embarazo, la lactancia y en menores de 3 años.", "AESAN (mercurio en pescado)", 4, T, "exp_sorprendida"),
    ficha_veredicto("OJO", AMARILLO, "Quesos frescos o de pasta blanda", "Brie, Camembert o tipo Burgos, si no dice en la etiqueta que son de leche pasteurizada.", "Ministerio de Consumo de España", 5, T, "exp_guino"),
    ficha_veredicto("OJO", AMARILLO, "La cabeza de las gambas", "La AESAN recomienda limitar la carne oscura de la cabeza: el cadmio se acumula allí (4 veces más que en el abdomen).", "AESAN (cadmio en crustáceos)", 6, T, "exp_pensativa"),
    cierre("Información general", "No sustituye a tu médico. Compártelo con quien está embarazada.", "exp_contenta", 7, T),
], """
Embarazo y fiestas: qué evitar 🤰 Información general del Ministerio de Consumo; ante cualquier duda, pregunta a tu médico.

🚫 Huevo crudo y lo que lo lleve: mayonesa casera, mousse, merengue, tiramisú, helados caseros, ponches.
🚫 Carne cruda o poco hecha (bien cocinada, 71 °C) y pescado crudo.
🚫 Pez espada, tiburón, atún rojo y lucio (mercurio).
⚠️ Quesos frescos o de pasta blanda si no dicen «leche pasteurizada».
⚠️ La cabeza de las gambas: el cadmio se acumula allí.

Compártelo con quien está embarazada 💛

📊 Fuentes: Ministerio de Derechos Sociales, Consumo y Agenda 2030 y AESAN.
Pepa es un personaje animado con IA; los datos, no 😉

#embarazo #navidad #seguridadalimentaria #nutrición #pepapita
""")

# ── 014 · lunes 7/12 · mesa de Navidad ──
T = 7
guardar("014_mesa_navidad", [
    portada("La mesa de Navidad sin sustos", "Cuatro reglas de la EFSA y de la norma europea.", "pose_aplaude", 1, T),
    ficha_numero("2 h", "Comida cocinada sobre la mesa", "No más de 2 horas a temperatura ambiente.", "EFSA (Safe2Eat)", 2, T, "exp_preocupada"),
    ficha_numero("60 °C / 5 °C", "Caliente o frío, nunca templado", "Si se come enseguida, mantenla por encima de 60 °C. Si no, refrigérala cuanto antes, por debajo de 5 °C.", "EFSA (Safe2Eat)", 3, T, "exp_pensativa"),
    ficha_numero("70 °C", "El caldo y los guisos", "Llévalos a ebullición para asegurar los 70 °C. Idealmente, con termómetro.", "EFSA (Safe2Eat)", 4, T, "exp_contenta"),
    ficha_numero("14", "Alérgenos que la ley obliga a destacar", "Cereales con gluten, crustáceos, huevos, pescado, cacahuetes, soja, leche, frutos de cáscara, apio, mostaza, sésamo, sulfitos, altramuces y moluscos.", "Reglamento (UE) 1169/2011", 5, T, "exp_sorprendida"),
    ficha_numero("ETIQUETA", "Si tienes alergia, léela siempre", "Deben aparecer destacados en la lista de ingredientes. No te fíes de la memoria.", "Reglamento (UE) 1169/2011", 6, T, "exp_guino"),
    cierre("¿Cuál olvidabas?", "Guárdalo para la cena de Navidad y compártelo con quien cocina.", "exp_riendo", 7, T),
], """
La mesa de Navidad sin sustos 🎄

⏱️ Comida cocinada: máximo 2 horas a temperatura ambiente.
🔥 Caliente (más de 60 °C) o frío (menos de 5 °C), nunca templado.
🍲 Caldos y guisos: a ebullición, 70 °C.
⚠️ 14 alérgenos que la ley obliga a destacar en la etiqueta. Si tienes alergia, léela siempre.

Guárdalo para la cena de Navidad y compártelo con quien cocina 💛

📊 Fuentes: EFSA (campaña Safe2Eat) y Reglamento (UE) 1169/2011.
Pepa es un personaje animado con IA; los datos, no 😉

#navidad #cenadenavidad #seguridadalimentaria #alergias #pepapita
""")

# ── 015 · lunes 14/12 · niños: uvas, caramelos, atragantamiento ──
T = 7
guardar("015_ninos_atragantamiento", [
    portada("Niños en Navidad: atragantamientos", "Lo que recomiendan los pediatras. Guárdalo.", "pose_senala", 1, T),
    ficha_numero("4–5 años", "Uvas enteras, no antes", "Hasta entonces: peladas, sin semillas y partidas en cuatro trozos a lo largo, no en rodajas.", "Asociación Española de Pediatría (2025)", 2, T, "exp_preocupada"),
    ficha_numero("0–5 años", "Los caramelos, ni uno", "Según los pediatras, ningún caramelo es seguro antes de los 5 años: no se deshacen rápido y encajan en la garganta.", "Asociación Española de Pediatría (2025)", 3, T, "exp_sorprendida"),
    ficha_numero("SENTADO", "Y con un adulto al lado", "Que el niño esté sentado y tranquilo, y siempre acompañado.", "Asociación Española de Pediatría (2025)", 4, T, "exp_contenta"),
    ficha_mito("Meter el dedo para sacar el objeto", "Falso: puede empujarlo más adentro. Levantarlo por los pies también es ineficaz y peligroso.", "Asociación Española de Pediatría (2025)", 5, T, "exp_preocupada"),
    ficha_numero("TOS", "Si tose con fuerza, no intervengas", "Es la forma natural de expulsarlo. Si no puede toser o le cuesta respirar: pide ayuda o llama a emergencias (en España, 112), y 5 golpes en la espalda seguidos de 5 compresiones.", "Asociación Española de Pediatría (2025)", 6, T, "exp_pensativa"),
    cierre("Apúntate a un curso", "Esto no sustituye a un curso de primeros auxilios. Compártelo con las familias.", "exp_contenta", 7, T),
], """
Niños en Navidad: atragantamientos 🎄 Lo que recomiendan los pediatras.

🍇 Uvas enteras, no antes de los 4–5 años: peladas, sin semillas y en cuatro trozos a lo largo.
🍬 Caramelos: según los pediatras, ninguno es seguro antes de los 5 años.
🪑 Sentado, tranquilo y con un adulto al lado.
❌ Meter el dedo en la boca o levantarlo por los pies: no.
🗣️ Si tose con fuerza, no intervengas. Si no puede toser: pide ayuda (en España, 112), 5 golpes en la espalda y 5 compresiones.

Esto no sustituye a un curso de primeros auxilios. Compártelo con las familias 💛

📊 Fuente: Asociación Española de Pediatría, Comité de Soporte Vital (23/12/2025).
Pepa es un personaje animado con IA; los datos, no 😉

#navidad #niños #atragantamiento #pediatría #pepapita
""")
