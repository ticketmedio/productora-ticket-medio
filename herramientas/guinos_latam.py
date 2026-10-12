"""Añade a algunos Reels de Pepa un guiño al público latinoamericano (decisión del usuario, 12/10/2026):
la voz sigue siendo la de siempre (Marta); se añaden una frase hablada con vocabulario/estaciones/datos de allí, un rótulo y una fuente
internacional (USDA, FDA, AAP) ya verificada. Idempotente: no repite el guiño si la ficha ya lo tiene (campo «latam»)."""
import json, glob, os, shutil, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOTE = os.path.join(RAIZ, "redes", "pepa_pita", "lote")
VID = os.path.join(RAIZ, "redes", "pepa_pita", "videos")
USDA_CONG = "- USDA FSIS (EE. UU.), «Freezing and Food Safety» (actualizada 09/08/2024; leída el 12/10/2026 en copia del Internet Archive): "
USDA_LEFT = "- USDA FSIS (EE. UU.), «Leftovers and Food Safety» (leída el 12/10/2026 en copia del Internet Archive del 08/10/2026): "
FDA_SH = "- FDA (EE. UU.), «Safe Food Handling» (leída el 12/10/2026): "
FDA_EGG = "- FDA (EE. UU.), «What You Need to Know About Egg Safety» (leída el 12/10/2026): "
FDA_4 = "- FDA / foodsafety.gov (EE. UU.), «4 Steps to Food Safety» (copia del Internet Archive del 10/10/2026): "
AAP = "- Academia Americana de Pediatría (healthychildren.org), «Choking Prevention» (leída el 12/10/2026): "
G = {
"019": ("Y si me ves desde Latinoamérica, mira qué frase pone tu etiqueta: «consumir preferentemente antes de» o «fecha de vencimiento». En Estados Unidos, el Departamento de Agricultura aclara que la fecha de «mejor si se usa antes de» es de calidad, no de seguridad.",
        ("no de seguridad", "CALIDAD, NO SEGURIDAD", "«Best if Used By» · USDA (EE. UU.)"),
        USDA_LEFT.replace("Leftovers and Food Safety", "Food Product Dating") + "«\"Best if Used By/Before\" … is not a purchase or safety date»; solo en la leche de fórmula infantil la fecha es de seguridad. Fecha de publicación del documento no indicada en la copia."),
"020": ("Y si me ves desde Argentina, Paraguay o Colombia, freezer o congelador, da igual: el Departamento de Agricultura de Estados Unidos dice que, a menos dieciocho grados, la comida es segura casi indefinidamente. Los tiempos son solo por calidad.",
        ("segura casi indefinidamente", "−18 °C: SEGURA SIEMPRE", "Los tiempos son por calidad · USDA"),
        USDA_CONG + "«Food stored constantly at 0 °F will always be safe. Only the quality suffers with lengthy freezer storage.» (0 °F ≈ −18 °C)."),
"021": ("Y si me ves desde Argentina, Paraguay o Colombia, vianda, lonchera o fiambrera, da igual. Con más de treinta y dos grados, como en un día de verano, el Departamento de Agricultura de Estados Unidos baja el límite a una hora.",
        ("baja el límite a una hora", "CON CALOR: 1 HORA", "Más de 32 °C (90 °F) · USDA (EE. UU.)"),
        USDA_LEFT + "«Throw away all perishable foods that have been left in room temperature for more than 2 hours (1 hour if the temperature is over 90° F, such as at an outdoor picnic during summer).» (90 °F ≈ 32 °C)."),
"024": ("Y si me ves desde Argentina o Paraguay, heladera; desde Colombia, nevera. Da igual. El Departamento de Agricultura de Estados Unidos añade otra opción segura: en agua fría, en una bolsa bien cerrada, cambiando el agua cada treinta minutos, y cocinándolo enseguida.",
        ("cada treinta minutos", "AGUA FRÍA: CAMBIA CADA 30 MIN", "Bolsa cerrada y cocinar ya · USDA (EE. UU.)"),
        USDA_CONG + "«There are three safe ways to thaw food: in the refrigerator, in cold water, or in the microwave»; en agua fría: bolsa a prueba de fugas y «Change the water every 30 minutes. After thawing, cook immediately»."),
"026": ("Y el Departamento de Agricultura de Estados Unidos da tiempos muy parecidos: carne molida de tres a cuatro meses, y fiambres, de uno a dos.",
        ("muy parecidos", "USDA (EE. UU.): MUY PARECIDO", "Molida 3–4 meses · fiambres 1–2"),
        USDA_CONG + "tabla «Freezer Storage Chart (0 °F)»: carne molida cruda 3 a 4 meses; jamón, perritos y fiambres 1 a 2; aves crudas enteras 12; partes 9; sopas y guisos 2 a 3. «Frozen foods remain safe indefinitely.»"),
"027": ("En Estados Unidos, el Departamento de Agricultura da la cifra exacta: ciento sesenta y cinco grados Fahrenheit en las aves, unos setenta y cuatro Celsius, medidos con un termómetro.",
        ("ciento sesenta y cinco grados", "AVES: 74 °C (165 °F)", "Con termómetro · USDA y FDA (EE. UU.)"),
        FDA_SH + "tabla de temperaturas mínimas internas: aves (molidas, partes, enteras y relleno) 165 °F; carne molida 160 °F; huevos «cook until yolk & white are firm». (165 °F ≈ 74 °C; 160 °F ≈ 71 °C)."),
"028": ("En Estados Unidos piden llegar a ciento sesenta y cinco grados Fahrenheit, unos setenta y cuatro Celsius, y llevar las sopas y las salsas a ebullición.",
        ("llevar las sopas", "SOPAS Y SALSAS: A EBULLICIÓN", "Sobras a 74 °C (165 °F) · USDA"),
        USDA_LEFT + "«When reheating leftovers, be sure they reach 165° F as measured with a food thermometer. Reheat sauces, soups and gravies by bringing them to a rolling boil.»"),
"029": ("La FDA de Estados Unidos dice lo mismo: cocinar los huevos hasta que la yema y la clara estén firmes, y los platos con huevo, a setenta y un grados, ciento sesenta Fahrenheit.",
        ("ciento sesenta Fahrenheit", "PLATOS CON HUEVO: 71 °C", "160 °F · FDA (EE. UU.)"),
        FDA_EGG + "«Cook eggs until both the yolk and the white are firm. Scrambled eggs should not be runny. Casseroles and other dishes containing eggs should be cooked to 160° F.»"),
"030": ("La FDA de Estados Unidos añade un truco: lávate las manos con jabón normal, no hace falta el antibacteriano, durante al menos veinte segundos. Para medirlos, tararea dos veces el «Cumpleaños feliz».",
        ("tararea dos veces", "20 SEGUNDOS: 2 × «CUMPLEAÑOS FELIZ»", "Jabón normal · FDA (EE. UU.)"),
        FDA_4 + "«Use plain soap and water—skip the antibacterial soap—and scrub … for at least 20 seconds. Need a timer? Hum the “Happy Birthday” song from beginning to end twice.» Y la FDA (Safe Food Handling): si usas paños de tela, lávalos a menudo en el ciclo caliente."),
"031": ("La FDA de Estados Unidos lo resume en cuatro verbos: limpiar, separar, cocinar y enfriar. Si me ves desde Argentina, Colombia o Paraguay, cuéntame de qué ciudad.",
        ("cuatro verbos", "LIMPIAR · SEPARAR · COCINAR · ENFRIAR", "Los 4 pasos · FDA (EE. UU.)"),
        FDA_SH + "«follow these four simple steps: clean, separate, cook, and chill». Cocinar: «Color and texture are unreliable indicators of safety. Using a food thermometer is the only way to ensure the safety of meat, poultry, seafood, and egg products.»"),
"040": ("Y ojo si me ves desde Argentina o Paraguay: tu Navidad es en pleno verano. Con más de treinta y dos grados, el límite baja a una hora.",
        ("baja a una hora", "CON MÁS DE 32 °C: 1 HORA", "Navidad en verano · USDA (EE. UU.)"),
        USDA_LEFT + "«Throw away all perishable foods that have been left in room temperature for more than 2 hours (1 hour if the temperature is over 90° F …).» (90 °F ≈ 32 °C)."),
"041": ("Y si me ves desde Argentina o Paraguay, tu Navidad es en pleno verano: con más de treinta y dos grados, el tiempo fuera del frío baja a una hora.",
        ("baja a una hora", "NAVIDAD EN VERANO: 1 HORA", "Más de 32 °C (90 °F) · USDA (EE. UU.)"),
        USDA_LEFT + "«… (1 hour if the temperature is over 90° F, such as at an outdoor picnic during summer).» FDA (Safe Food Handling): «Refrigerate within 1 hour if the temperature outside is above 90° F.»"),
"044": ("Ojo: la FDA de Estados Unidos va más allá y dice que el color y la textura no son indicadores fiables, y que solo un termómetro lo asegura: sesenta y tres grados en cordero y cerdo, con tres minutos de reposo; setenta y uno en carne molida.",
        ("no son indicadores fiables", "EL COLOR NO ES FIABLE", "Termómetro: 63 °C cortes · 71 °C molida"),
        FDA_SH + "«Color and texture are unreliable indicators of safety. Using a food thermometer is the only way…»; «Beef, Pork, Veal, and Lamb (chops, roasts, steaks) 145 °F with a 3 minute rest time; Ground Meat 160 °F». (145 °F ≈ 63 °C; 160 °F ≈ 71 °C)."),
"045": ("La Academia Americana de Pediatría coincide: incluye los caramelos duros, pegajosos o blandos entre los alimentos de riesgo y aconseja evitarlos hasta los cuatro años o más.",
        ("Academia Americana", "AAP (EE. UU.): HASTA LOS 4 AÑOS", "Caramelos duros, blandos o pegajosos"),
        AAP + "«Keep high-risk foods from children until 4 years of age or older…»; entre los alimentos a evitar o modificar: «Hard, gooey, or sticky candy»."),
"046": ("Si en tu país también se toman uvas en Nochevieja, ojo: la Academia Americana de Pediatría coincide y dice que las uvas enteras son un riesgo; solo se pueden servir si están completamente picadas en trocitos diminutos.",
        ("Academia Americana", "AAP (EE. UU.): UVAS ENTERAS, NO", "Solo picadas en trocitos diminutos"),
        AAP + "«round, firm foods, such as hot dogs or grapes, can be served if completely chopped into tiny pieces»; entre los alimentos a evitar o modificar: «Whole grapes»."),
"049": ("En Estados Unidos, el Departamento de Agricultura dice que la carne, las aves y los guisos se pueden cocinar directamente congelados, pero tardan aproximadamente una vez y media más.",
        ("una vez y media más", "CONGELADO: 1,5 × MÁS TIEMPO", "Carne, aves y guisos · USDA (EE. UU.)"),
        USDA_CONG + "«Raw or cooked meat, poultry or casseroles can be cooked or reheated from the frozen state. However, it will take approximately one and a half times as long to cook.» Algunos productos precocinados rellenos DEBEN cocinarse congelados: leer la etiqueta."),
}
CIERRE = "Sígueme, que aquí aprendemos todos."
LATAM_PUB = "🌎 ¿Me ves desde Argentina, Paraguay, Colombia u otro país? Cuéntame cómo le llamáis a esto en tu casa 👇\n\n"
ids = sys.argv[1:] or sorted(G)
for n in ids:
    f = glob.glob(os.path.join(LOTE, f"{n}_*.json"))[0]
    d = json.load(open(f, encoding="utf-8"))
    if d.get("latam"): print(n, "ya tiene guiño"); continue
    frase, (clave, rot, sub), fuente = G[n]
    assert CIERRE in d["guion"], n
    d["guion"] = d["guion"].replace(CIERRE, frase + "\n\n" + CIERRE, 1)
    d.setdefault("rotulos", []).append({"clave": clave, "texto": rot, "sub": sub})
    d["fuentes"].append(fuente)
    assert "📊 Fuente" in d["texto_pub"], n
    d["texto_pub"] = d["texto_pub"].replace("📊 Fuente", LATAM_PUB + "📊 Fuente", 1)
    d["latam"] = True
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for sub_ in ("voz", "salida"):
        shutil.rmtree(os.path.join(VID, f"{n}_{d['slug']}", sub_), ignore_errors=True)
    print(n, "guiño añadido")
