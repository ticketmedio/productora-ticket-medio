"""Genera plan.json de Pepa 013–018 (tiempos de voz/subtitulos.srt, voz ya acelerada ×1,12).
Límites de pepa_video.py: cabecera ≤ 18 caracteres, «sub» de los rótulos ≤ 43."""
import json, os

V = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos")
MUS = "../../../../musica/pepa_pita/Travelling Light - Blue Deer Studio.mp3"
def P(*a): return [{"desde": d, "imagen": i} for d, i in a]
def R(*a): return [{"desde": d, "hasta": h, "texto": t, "sub": s} for d, h, t, s in a]
planes = {
 "013_castanas": ("pexels_5451503", "¿CASTAÑAS ASADAS?",
   P((0, "busto"), (4.1, "exp_sorprendida"), (7.0, "pose_senala"), (12.4, "busto"), (17.8, "pose_sartenes"), (24.3, "exp_preocupada"), (29.6, "busto"), (31.3, "exp_guino")),
   R((7.0, 12.4, "UN CORTE EN LA PIEL", "para que no estallen · MAPA"),
     (12.5, 17.7, "50–60 % DE AGUA", "se estropea pronto · IGP Castaña de Galicia"),
     (17.8, 24.2, "EN RED… O AL CONGELADOR", "que ventile"),
     (24.4, 31.2, "LA DEL PARQUE, NO", "castaña de Indias · ANSES (Francia)"))),
 "014_calabaza": ("pexels_29148450", "¿CALABAZA?",
   P((0, "busto"), (2.3, "exp_riendo"), (3.7, "busto"), (10.1, "pose_senala"), (13.5, "exp_preocupada"), (17.5, "busto"), (23.5, "exp_pensativa"), (25.8, "pose_sartenes"), (31.7, "exp_guino")),
   R((3.8, 10.0, "TEMPORADA ALTA", "octubre y noviembre · MAPA"),
     (10.1, 13.5, "LAS PIPAS, TOSTADAS", "30 g de proteína por 100 g · BEDCA"),
     (13.6, 17.4, "LAS DE ADORNO, NO", "son tóxicas · ANSES (Francia)"),
     (17.5, 25.7, "¿AMARGA? ESCUPE Y TIRA", "cocinarla no lo arregla · ANSES · BfR"),
     (25.8, 31.6, "NEVERA O CONGELADOR", "lo que cortes"))),
 "015_setas": ("pexels_33640979", "¿SETAS?",
   P((0, "busto"), (3.0, "exp_sorprendida"), (4.9, "pose_senala"), (11.2, "exp_pensativa"), (17.8, "exp_preocupada"), (24.9, "busto"), (37.3, "pose_senala"), (40.0, "exp_guino")),
   R((4.9, 11.1, "SI NO LA CONOCES, NO", "ni cogerla ni aceptarla · AESAN"),
     (11.2, 17.7, "NINGÚN TRUCO SIRVE", "ni plata, ni ajo, ni bichos · AESAN"),
     (17.8, 24.8, "AMANITA PHALLOIDES", "90 % de las muertes: amanitinas · INTCF"),
     (28.8, 40.0, "112 · 91 562 04 20", "Toxicología, 24 horas · lleva las setas"))),
 "016_menu_otono": ("pexels_5451503", "¿MENÚ BARATO?",
   P((0, "busto"), (1.8, "exp_riendo"), (3.8, "pose_senala"), (10.0, "busto"), (19.7, "pose_sartenes"), (30.9, "busto"), (39.5, "exp_guino"), (45.1, "exp_guino")),
   R((3.8, 9.9, "LEGUMBRES: 4 O MÁS", "días a la semana · AESAN"),
     (10.0, 19.6, "PESCADO 3 · CARNE ≤3", "huevos, hasta 4 · AESAN"),
     (19.7, 30.8, "VERDURA DE TEMPORADA", "calabaza · coliflor · coles · MAPA"),
     (30.9, 39.4, "FRUTA DE TEMPORADA", "caqui · granada · mandarina · MAPA"),
     (39.5, 45.0, "MENÚ Y LISTA EL DOMINGO", "compras lo justo · AESAN"))),
 "017_legumbres": ("pexels_29148450", "¿LEGUMBRES?",
   P((0, "busto"), (1.9, "exp_preocupada"), (4.4, "busto"), (10.3, "pose_senala"), (21.5, "exp_pensativa"), (25.5, "exp_riendo"), (27.6, "busto"), (30.1, "pose_sartenes"), (33.3, "exp_guino")),
   R((4.5, 10.2, "LECTINAS", "si no se cocinan bien, sientan mal · EFSA"),
     (10.3, 15.0, "REMOJO 6–12 H", "y tira esa agua · EFSA 2026"),
     (15.1, 21.4, "HERVIR 30 MIN O MÁS", "hasta que estén blandas · EFSA 2026"),
     (21.5, 25.4, "VAPOR O MICRO: MENOS", "quitan menos lectinas · EFSA"),
     (27.6, 33.2, "4 VECES POR SEMANA", "al menos · AESAN"))),
 "018_pan_duro": ("pexels_33640979", "¿PAN DURO?",
   P((0, "busto"), (1.5, "exp_preocupada"), (3.8, "busto"), (10.6, "exp_sorprendida"), (14.8, "exp_pensativa"), (15.8, "pose_sartenes"), (20.2, "pose_senala"), (27.4, "exp_preocupada"), (31.1, "exp_guino")),
   R((3.9, 10.5, "23 KG POR PERSONA", "de comida tirada en casa en 2025 · MAPA"),
     (10.6, 14.7, "EL PAN, 5.º", "de lo que se tira sin tocar · MAPA"),
     (15.8, 20.1, "TORRIJAS · MIGAS · SOPA", "o pan rallado"),
     (20.2, 27.3, "SE CONGELA", "en rebanadas · AESAN"),
     (27.4, 31.0, "¿MOHO? ENTERO FUERA", "AESAN"))),
}
for v, (fondo, cab, planos, rot) in planes.items():
    assert len(cab) <= 18, cab
    for r in rot: assert len(r["sub"]) <= 43, r["sub"]
    plan = {"voz": "voz/voz.mp3", "subtitulos": "voz/subtitulos.srt", "musica": MUS, "musica_db": -22,
            "fondo": f"../../fondos/{fondo}.jpg", "cabecera": cab, "planos": planos, "rotulos": rot,
            "salida": f"salida/PEPA_{v}.mp4"}
    with open(os.path.join(V, v, "plan.json"), "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=1)
print("ok")
