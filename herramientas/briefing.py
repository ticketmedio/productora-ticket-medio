"""Resumen de lo que dicen los informes diarios (Sala) y las ideas, para leerlo ANTES de producir un vídeo, Short o Reel.
Uso: python3 herramientas/briefing.py [días=4]
Imprime «Lo más importante», «Qué funciona/no funciona» y «Recomendación» de los informes de clave seo, mercado-manana y mercado-tarde."""
import datetime, json, os, re, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dias = int(sys.argv[1]) if len(sys.argv) > 1 else 4
d = json.load(open(os.path.join(RAIZ, "web", "datos.json"), encoding="utf-8"))
corte = (datetime.date.today() - datetime.timedelta(days=dias)).isoformat()
CLAVES = ("lo más importante", "qué funciona", "recomendación", "mejora aplicable", "ideas")
for i in sorted(d["informes"], key=lambda x: (x["fecha"], x.get("clave", "seo")), reverse=True):
    if i["fecha"] < corte:
        continue
    print(f"\n######## {i['fecha']} · {i.get('clave', 'seo')} · {i['titulo']}")
    for bloque in re.split(r"\n(?=## )", i["texto"]):
        if bloque.lower().lstrip("# ").startswith(CLAVES):
            print(bloque.strip()[:1500])
print("\n######## seo/IDEAS.md (última entrada)")
t = open(os.path.join(RAIZ, "seo", "IDEAS.md"), encoding="utf-8").read().split("\n## ")
print("## " + t[1][:2500] if len(t) > 1 else "")
