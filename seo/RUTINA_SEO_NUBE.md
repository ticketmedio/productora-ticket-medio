# Informe SEO en la NUBE (rutina diaria, 8:30 hora de Madrid)

Funciona SIN ordenador del usuario. Usa la API oficial de YouTube (`herramientas/yt_analytics.py`, credenciales en las variables de entorno del entorno de la nube; NUNCA se imprimen ni se citan) y datos públicos. NO hay navegador ni sesiones: las estadísticas privadas de Meta (Facebook e Instagram) y de TikTok SOLO las lee la rutina local de las 8:00 (`seo/RUTINA_DIARIA.md`) cuando el PC del trabajo está encendido.

Todo en ESPAÑOL DE ESPAÑA. Solo se lee: nunca seguir, dar «me gusta», comentar ni cambiar nada en ninguna plataforma. La Sala es PÚBLICA: nada de datos personales ni textos de comentarios de personas. Si algo falla, dilo con franqueza en «Para ti» y NO inventes datos.

## Paso 0 · ¿Ya hay informe de hoy?
1. `git pull`.
2. Comprueba si `web/datos.json` ya tiene un informe de la fecha de hoy (Madrid: `TZ=Europe/Madrid date +%F`) con clave `seo` (o sin clave): `python3 -c "import json;d=json.load(open('web/datos.json',encoding='utf-8'));print([ (r['fecha'],r.get('clave','seo')) for r in d.get('informes',[])][:6])"`.
3. Si YA existe el de hoy (lo hizo el PC del trabajo, que tiene los datos privados de Meta y TikTok), NO hagas nada más: termina diciendo «ya existe el informe SEO de hoy».
4. Si no existe, sigue.

## Paso 1 · Datos de YouTube (API oficial)
- `python herramientas/yt_analytics.py resumen 28` y `python herramientas/yt_analytics.py resumen 7`.
- `python herramientas/yt_analytics.py videos 7` y `videos 28` (si avisa de que no puede leer los títulos, usa los ID y dilo).
- **Separa SIEMPRE vídeos largos de Shorts** (`creatorContentType`: `videoOnDemand` = largos, `shorts`): las horas de los Shorts probablemente NO cuentan para el Programa de Socios. Las horas VÁLIDAS son las de `videoOnDemand`.
- Para el vídeo largo publicado más reciente: `python herramientas/yt_analytics.py retencion ID` y apunta en qué punto se va la gente.
- Cifras públicas de nuestro canal también con `python herramientas/yt_buscar.py canal @TicketMedio` (suscriptores y últimos vídeos).

## Paso 2 · Comparar con el informe anterior
Lee el último informe de clave `seo` de `web/datos.json` y compara: visualizaciones, horas (largos y Shorts), suscriptores y el vídeo o Short que mejor y peor ha funcionado.

## Paso 3 · Pepa, Instagram, Facebook y TikTok
No hay estadísticas privadas aquí. Repite las últimas cifras conocidas del informe anterior marcándolas con su fecha («de ayer», «del lunes»…) y no las presentes como de hoy.

## Paso 4 · Escribe el informe y publícalo
1. Escribe `/tmp/informe_seo.md` con apartados `## `: «Lo más importante» (3 puntos), «YouTube (Ticket Medio)», «Facebook, Instagram y TikTok (Pepa Pita)» (con la fecha de las cifras), «Comparación con el día anterior», «Qué funciona y qué no», «Recomendación del día» (UNA concreta: título, gancho, miniatura, Shorts enlazados…) y «Para ti» (lo que tenga que hacer el usuario, o «Nada»). Añade siempre en «Para ti» una línea: «Hoy el informe SEO lo ha hecho la nube con la API de YouTube; las cifras de Meta y TikTok son del último informe del PC». Listas con «- » y **negrita** en las cifras clave.
2. Los lunes, añade además un apartado «Panel de dinero»: horas VÁLIDAS (vídeos largos) frente a las 8.000 y las de Shorts aparte; suscriptores frente a 1.000; días hasta el 1/7/2027 y horas por semana necesarias a este ritmo; una frase de si vamos a ritmo o no. Sin adornos.
3. Publica: `python web/claude_sala.py informe <hoy AAAA-MM-DD> "<titular de una línea>" /tmp/informe_seo.md` (clave `seo`, la de por defecto) y un mensaje corto en el Tablón: `python web/claude_sala.py mensaje "📈 Resumen SEO del <día>: ... Informe completo en Informes diarios."` (máx. ~500 caracteres, sin nombres de personas).
4. **Subida (síncrona)**: `git add web/datos.json`, `git commit -m "SEO nube <fecha>"`, `git pull --rebase`, `git push`. Si el push falla, reintenta una vez tras otro `git pull --rebase`. Comprueba con `git status` que no queda nada sin subir.
