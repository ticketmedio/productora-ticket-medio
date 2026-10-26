# Lecciones de YouTube (Ticket Medio): léelas ANTES de crear, titular o programar cualquier vídeo o Short

Se actualiza cada vez que los datos enseñen algo nuevo. Fecha de la primera versión: 26/10/2026.

## Qué pasa (datos 26/10/2026, 28 días)
- Shorts: ~9.000 visualizaciones; casi nadie se suscribe (+6) y menos de 1 de cada 100 pasa a un largo.
- Largos: 1–14 visualizaciones. Largo de Lidl en 3 días: **26 impresiones, 3,9 % de clics, 2 visualizaciones**. El problema es el alcance (YouTube no lo enseña), no la miniatura.

## Reglas (aplicar siempre)
1. **Título que responde a una búsqueda real** («cómo gana dinero X», «quién fabrica Hacendado», «… 2026») con la marca conocida, la sospecha o la cifra en las primeras palabras. Sin asteriscos ni formato markdown al copiar (07_TITULOS.md ya no los lleva).
2. **Cada Short enlaza al largo de su tema:** «Vídeo relacionado» en Studio (solo se puede elegir cuando el largo ya es público: tarea del usuario el día que sale), comentario fijado y «el vídeo completo, en el canal» en la descripción.
3. **Shorts de 10–15 s con UNA comparación o dato** son los que mejor funcionan (Shein vs Zara, 10 s: 969 en 24 h; casero del Corte Inglés, 27 s: 1.868). Preferirlos a los de 40–50 s.
4. **Marca española conocida + sospecha/escándalo + cifra** es la fórmula de los canales pequeños que despegan (Peluch: TOUS 155 mil con ~6 mil suscriptores; Demand Lab: Corte Inglés 204 mil). Contar una historia, no solo explicar.
5. Tras publicar un largo, medir a los 7 días: impresiones, % de clics y visualizaciones, y anotarlo en seo/PENDIENTES.md.
6. Objetivo realista: las 8.000 h con solo largos no llegan a julio de 2027; los Shorts son el único tráfico que escala. Puntos de decisión: 9/11 y final de noviembre (apartado 13/14 de seo/00_ESTRATEGIA_SEO.md).

## Retoques ya aplicados (26/10/2026) a lo no publicado
- Títulos de los vídeos 7, 8, 9, 10 y 12 pasados a versión buscable (los antiguos quedan como alternativa A/B en 07_TITULOS.md). El 11 (Cepsa) se queda: «¿Nos están engañando?» sigue la fórmula de Peluch.
- Los 42 Shorts de los vídeos 7–12 llevan al final (últimos 2,6 s) el rótulo «VÍDEO COMPLETO EN EL CANAL» (`python3 herramientas/cierre_shorts.py CARPETA_VIDEO`, se añade sobre el MP4 ya renderizado y no se repite). Hacerlo con todo Short nuevo, después de `render_shorts.py`.
- Corregido un fallo visual: los rótulos de cabecera largos (más de 20 letras) se cortaban por los lados; `cab()` de los `crear_shorts.py` ahora reduce el tamaño. 14 Shorts se volvieron a renderizar.
