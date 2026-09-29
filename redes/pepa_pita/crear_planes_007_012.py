"""Genera plan.json de Pepa 007–012 (tiempos sacados de voz/subtitulos.srt, voz ya acelerada ×1,12)."""
import json, os
V = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos")
MUS = "../../../../musica/pepa_pita/Travelling Light - Blue Deer Studio.mp3"
def P(*a): return [{"desde": d, "imagen": i} for d, i in a]
def R(*a): return [{"desde": d, "hasta": h, "texto": t, "sub": s} for d, h, t, s in a]
planes = {
 "007_tabla_de_cortar": ("pexels_5451503", "¿UNA SOLA TABLA?",
   P((0, "busto"), (3.5, "exp_sorprendida"), (5.3, "busto"), (11.4, "pose_senala"), (18.7, "exp_pensativa"), (20.4, "busto"), (27.7, "pose_ojo"), (33.4, "exp_preocupada"), (36.7, "exp_guino")),
   R((5.4, 11.3, "CRUDO → TABLA → ENSALADA", "así viajan las bacterias · AESAN"),
     (11.5, 18.6, "UNA PARA LO CRUDO", "y otra para lo que va directo a la boca · OMS"),
     (20.4, 27.6, "VERDURA → CARNE → JABÓN", "si solo tienes una · FSA"),
     (29.4, 33.3, "MADERA O PLÁSTICO: LAS DOS", "el plástico se limpia mejor · USDA"),
     (33.4, 36.6, "¿SURCOS? A LA BASURA", "USDA"))),
 "008_sobras": ("pexels_29148450", "¿LAS SOBRAS?",
   P((0, "busto"), (3.9, "exp_preocupada"), (6.8, "busto"), (15.0, "pose_senala"), (20.6, "busto"), (25.2, "exp_pensativa"), (26.2, "busto"), (32.5, "pose_sartenes"), (35.8, "exp_guino")),
   R((9.9, 14.9, "MÁXIMO 2 H FUERA", "1 h si hace más de 30 °C · AESAN"),
     (15.0, 20.5, "TÁPERES PEQUEÑOS", "y sin apilar · AESAN"),
     (20.6, 25.1, "3 DÍAS COMO MUCHO", "y con la fecha puesta · AESAN · OMS"),
     (26.3, 32.4, "RECALIENTA UNA VEZ", "muy caliente por todas partes · AESAN · OMS"),
     (32.5, 35.8, "SOPAS Y SALSAS: QUE HIERVAN", "AESAN"))),
 "009_moho": ("pexels_33640979", "¿MOHO?",
   P((0, "busto"), (2.9, "exp_sorprendida"), (4.2, "pose_ojo"), (8.2, "exp_preocupada"), (11.9, "busto"), (21.7, "pose_senala"), (26.4, "exp_pensativa"), (27.5, "busto"), (34.8, "exp_riendo"), (36.2, "exp_guino")),
   R((4.3, 8.1, "TIENE RAÍCES", "lo que ves es solo la punta · USDA"),
     (8.2, 11.8, "TOXINAS QUE NO SE VAN", "ni al cocinar · AESAN"),
     (12.0, 21.6, "A LA BASURA, ENTERO", "pan · mermelada · yogur · queso fresco · sobras"),
     (21.7, 26.3, "FRUTA Y VERDURA: ENTERAS", "AESAN"),
     (27.6, 34.7, "QUESO CURADO: 2,5 CM", "alrededor y por debajo · USDA (EE. UU.)"))),
 "010_mayonesa_casera": ("pexels_5451503", "¿MAYONESA CASERA?",
   P((0, "busto"), (3.5, "exp_riendo"), (4.4, "exp_preocupada"), (11.9, "busto"), (16.8, "pose_senala"), (22.5, "busto"), (27.6, "exp_pensativa"), (30.5, "busto"), (34.5, "exp_guino")),
   R((4.5, 11.8, "HUEVO CRUDO = RIESGO", "de salmonela · AESAN"),
     (11.9, 16.7, "N.º 1 EN BROTES EN LA UE", "salmonela y huevo · EFSA 2025"),
     (16.9, 22.4, "JUSTO ANTES DE COMER", "huevos en otro cuenco y sin lavar · AESAN"),
     (22.5, 27.5, "LO QUE SOBRE, FUERA", "ese mismo día · AESAN"),
     (30.5, 34.4, "BARES: HUEVO PASTEURIZADO", "por ley · Real Decreto 1021/2022"))),
 "011_lavar_la_fruta": ("pexels_29148450", "¿LAVAS LA FRUTA?",
   P((0, "busto"), (3.8, "exp_sorprendida"), (5.6, "busto"), (11.8, "pose_senala"), (16.4, "exp_preocupada"), (20.2, "busto"), (25.0, "exp_pensativa"), (28.0, "busto"), (38.8, "exp_guino")),
   R((5.7, 11.7, "BAJO EL GRIFO", "aunque la vayas a pelar · AESAN"),
     (16.4, 20.1, "SIN JABÓN", "la fruta lo absorbe · FDA (EE. UU.)"),
     (20.2, 25.0, "PIEL DURA: CEPILLO", "melón · sandía · pepino · AESAN"),
     (28.0, 34.5, "LEJÍA «APTA PARA AGUA DE BEBIDA»", "solo si se come cruda · AESAN"),
     (34.6, 38.7, "LA DOSIS: LA DE LA ETIQUETA", "y aclara con mucha agua"))),
 "012_la_nevera": ("pexels_33640979", "¿TU NEVERA, BIEN?",
   P((0, "busto"), (1.8, "exp_riendo"), (3.3, "busto"), (8.5, "pose_ojo"), (12.2, "pose_senala"), (21.4, "busto"), (24.8, "exp_pensativa"), (29.6, "busto"), (34.8, "exp_guino")),
   R((3.4, 12.1, "5 °C O MENOS", "mejor a 4 · AESAN · OMS · FDA"),
     (12.3, 15.6, "ARRIBA: LO COCINADO", "y lo listo para comer · AESAN"),
     (15.7, 21.4, "ABAJO: LO CRUDO, TAPADO", "que no gotee · AESAN · FSA"),
     (21.5, 24.8, "CAJONES: FRUTA Y VERDURA", "AESAN"),
     (24.9, 29.6, "SIN LLENARLA", "el aire frío tiene que circular · FDA"),
     (29.7, 34.8, "PUERTA: BEBIDAS Y SALSAS", "es la zona que más se calienta · USDA"))),
}
for v, (fondo, cab, planos, rot) in planes.items():
    n = v[:3]
    plan = {"voz": "voz/voz.mp3", "subtitulos": "voz/subtitulos.srt", "musica": MUS, "musica_db": -22,
            "fondo": f"../../fondos/{fondo}.jpg", "cabecera": cab, "planos": planos, "rotulos": rot,
            "salida": f"salida/PEPA_{n}_{v[4:]}.mp4"}
    json.dump(plan, open(os.path.join(V, v, "plan.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
