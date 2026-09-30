# Estrategia SEO y de crecimiento — Ticket Medio y Pepa Pita

Redactada por Claude el 30/09/2026, a partir de fuentes oficiales de YouTube, Meta y TikTok (enlaces al final).
El usuario encarga a Claude el SEO diario de las cuentas y un resumen diario en la Sala.

## 1. Líneas rojas (no se negocian)

**Nada de seguir cuentas, dar «me gusta» ni comentar con scripts o con el navegador automatizado.**
Las tres plataformas lo prohíben expresamente:

- **YouTube** prohíbe en sus Condiciones el acceso «mediante cualquier medio automatizado» y los comentarios «repetitivos o en masa».
  - Castigo: faltas, pérdida de la monetización o cierre del canal.
- **Instagram** prohíbe el acceso automatizado, incluso con la sesión iniciada.
  - Meta prohíbe interactuar «de forma manual o automática, con una frecuencia muy alta».
  - Castigo: bloqueos de acciones y que la cuenta deje de recomendarse a quien no la sigue.
- **TikTok** prohíbe usar «scripts automatizados para interactuar» y manipular la interacción.

Además, hoy ya no sirve para crecer. Seguir para que te sigan no mejora ninguna de las señales que usan los algoritmos (ver el punto 2). Solo atrae seguidores que no ven los vídeos, y eso hunde el porcentaje de interacción. Para el canal de YouTube el riesgo es doble: la entrada en el Programa de Socios se revisa a nivel de canal.

**Lo que SÍ está permitido**
- Publicar y programar con las herramientas oficiales (YouTube Studio, Meta Business Suite, TikTok Studio) o con sus API oficiales.
- Leer nuestras propias estadísticas una vez al día.
- Responder a los comentarios en nuestros propios vídeos, sin textos repetidos.

## 2. Qué premia cada plataforma (según las fuentes oficiales)

| Plataforma | Señales que mandan | Qué hacemos |
|---|---|---|
| YouTube | Que se elija el vídeo (clics en la miniatura), el tiempo que se ve y la satisfacción (encuestas, «me gusta») | Título y miniatura antes que el guion; gancho en los primeros 30 s; cumplir la promesa de la miniatura; probar varios títulos y miniaturas con Test & Compare |
| Instagram | Tiempo de visualización, «me gusta» por alcance y **envíos por mensaje** por alcance; contenido original | Reels de Pepa que den ganas de reenviar («mándaselo a quien lava el pollo»); carruseles útiles; reels de prueba en cuanto se puedan usar |
| Facebook | Contenido original (el reutilizado pierde alcance desde julio de 2025) | Los mismos Reels + carruseles propios |
| TikTok | Que se vean enteros; texto de la publicación, sonido y hashtags; idioma y país. El número de seguidores **no** cuenta directamente | Palabra clave dicha en voz, en pantalla y en el texto; buscar ideas en TikTok Studio → Inspiración (Creator Search Insights) |

## 3. SEO práctico (reglas para cada publicación)

**YouTube**
- 1–2 palabras clave por vídeo, en el título y en las dos primeras líneas de la descripción.
- Capítulos: el primero en 00:00, al menos 3, de 10 s como mínimo cada uno.
- 3–5 hashtags; con más de 60, YouTube los ignora todos.
- Etiquetas: solo unas pocas, porque apenas influyen.
- Ideas de palabras clave: pestaña «Investigación» de YouTube Analytics.

**Instagram**
- Máximo 5 hashtags, desde el 18/12/2025.
- Palabras clave en el texto de la publicación, en la biografía y en el texto alternativo: Google indexa las cuentas profesionales desde julio de 2025.

**TikTok**
- 3–5 hashtags concretos.
- La palabra clave, en las primeras palabras del texto de la publicación.

**Etiqueta de IA**
- YouTube no la exige para animación claramente irreal y dice que declararla no resta alcance.
- Meta y TikTok la exigen para lo realista. Pepa es claramente de dibujos, pero ya lo decimos en el texto («Pepa es un personaje animado con IA»), y así seguimos.

## 4. Cifras de referencia

- **Porcentaje de clics de la miniatura (CTR):** la mitad de los canales está entre el 2 % y el 10 % (dato oficial de YouTube). Con menos de 100 visualizaciones, la cifra no significa casi nada.
- **Parte del vídeo que se ve:** en vídeos de 9–11 min, apuntar a un 30–40 % (cifra de terceros; YouTube no da una oficial).
- **Punto de partida (30/09):**
  - Gasolina: 5 visualizaciones, CTR 18,2 %, duración media 0:40 de 5:27 (≈12 %). **El problema es la retención**, no la miniatura.
  - Los vídeos de Mercadona, Zara y El Corte Inglés ya se hicieron con más gancho y escenas ilustradas.

## 5. Rutina diaria de Claude (lunes a viernes, por la mañana, de forma automática)

1. Descargar las estadísticas de las tres plataformas (`node herramientas/estadisticas.js`).
2. Compararlas con el día anterior y apuntarlas en `privado/seo_diario/AAAA-MM-DD.md`. Es privado: puede incluir nombres de suscriptores o de quienes comentan.
3. Detectar qué ha funcionado y qué no, y proponer un cambio concreto en el siguiente vídeo, título o miniatura.
4. Leer los comentarios nuevos y preparar una respuesta para cada uno, distinta y personal.
5. Escribir en la Sala el **resumen del día**, sin nombres de personas, porque la Sala es pública.

## 6. Hoja de ruta

- **Semana del 30/09**
  - Estrategia y rutina diaria automática (hecho).
  - Primer lote de carruseles de Pepa para el muro de Instagram y Facebook: 2 a la semana, lunes y miércoles, que no son días de Reel.
  - Publicaciones de comunidad en YouTube (encuestas del tipo «¿qué empresa abrimos la próxima semana?»). Hace falta tener activadas las funciones avanzadas de YouTube Studio, que se activan verificando el teléfono.
- **Semana del 5/10:** conectar las **API oficiales**, para que Claude publique y responda comentarios él mismo sin saltarse ninguna norma.
  - YouTube Data API: responder comentarios, retocar títulos y descripciones, estadísticas exactas.
  - Meta Graph API: publicar carruseles en Facebook e Instagram y responder comentarios.
  - TikTok exige una auditoría de su API: allí se sigue programando a mano en lotes, como ahora.
- **Octubre:**
  - Test & Compare de títulos en cada vídeo nuevo.
  - Reels de prueba en Instagram.
  - Primer resumen mensual con conclusiones.
- **Colaboraciones:** cuando haya algo que enseñar (más de 500 seguidores), proponerlas a cuentas pequeñas de cocina y de economía. Siempre por mensaje personal escrito uno a uno, nunca en masa.

## Fuentes

- YouTube, cómo recomienda: https://support.google.com/youtube/answer/11914225
- YouTube, encuestas de satisfacción: https://support.google.com/youtube/answer/16089387
- YouTube, contenido no auténtico: https://support.google.com/youtube/answer/1311392
- YouTube, etiquetas: https://support.google.com/youtube/answer/146402
- YouTube, hashtags: https://support.google.com/youtube/answer/6390658
- YouTube, capítulos: https://support.google.com/youtube/answer/9884579
- YouTube, CTR: https://support.google.com/youtube/answer/7628154
- YouTube, Condiciones: https://www.youtube.com/t/terms
- YouTube, interacción falsa: https://support.google.com/youtube/answer/3399767
- YouTube, spam en comentarios: https://support.google.com/youtube/answer/2801973
- YouTube, contenido alterado o sintético: https://support.google.com/youtube/answer/14328491
- Instagram, clasificación explicada: https://about.instagram.com/blog/announcements/instagram-ranking-explained
- Instagram, reels de prueba: https://creators.instagram.com/blog/instagram-trial-reels
- Instagram, Condiciones: https://help.instagram.com/581066165581870/
- Meta, spam: https://transparency.meta.com/policies/community-standards/spam/
- Meta, etiquetas de IA: https://transparency.meta.com/governance/tracking-impact/labeling-ai-content
- Mosseri, señales de 2025 (Social Media Today): https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/
- Límite de 5 hashtags en Instagram (Social Media Today): https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/
- TikTok, cómo recomienda: https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you
- TikTok, Creator Search Insights: https://www.tiktok.com/creator-academy/article/finding-creator-search-insights
- TikTok, Condiciones: https://www.tiktok.com/legal/page/row/terms-of-service/en
- TikTok, etiqueta de IA: https://www.tiktok.com/creator-academy/en/article/ai-generated-content-label

## 7. Monetización: requisitos en España y objetivo julio 2027 (revisado el 30/09/2026)

| Plataforma | Qué hace falta para cobrar | Cómo se cobra | Objetivo realista a julio 2027 |
|---|---|---|---|
| YouTube (Ticket Medio) | 1.000 suscriptores + 8.000 h de visualización en 12 meses (desde el 1/2/2027) | Anuncios (RPM prudente: 3 €) | Posible, pero menos probable que no llegar; más probable a finales de 2027 |
| Facebook (Pepa) | Programa de monetización de contenido: **solo por invitación** (España ya puede recibirlas). Terceros hablan de 10.000 seguidores y 600.000 min vistos en 60 días (no oficial) | Reels y vídeos | La plataforma más prometedora para Pepa: los Reels ya llegan a gente que no nos sigue |
| Instagram (Pepa) | Regalos desde 500 seguidores; suscripciones desde 10.000. Los bonos por Reels son solo por invitación | Regalos, suscripciones y, sobre todo, **colaboraciones con marcas** | Colaboraciones con marcas de cocina o alimentación con 5.000–10.000 seguidores |
| TikTok (Pepa) | 10.000 seguidores + 100.000 visualizaciones en 30 días, cuenta PERSONAL (no de empresa), 18+ y **vídeos originales de más de 1 minuto** subidos después de la aceptación | Programa de recompensas para creadores | Solo si un vídeo se hace viral; lo más incierto |

**Consecuencias para la producción:**
- TikTok paga solo por vídeos de más de 60 s, y Pepa dura hoy 33–46 s. DECIDIDO el 30/09: desde Pepa 019, versión de 61–75 s para TikTok (consejo extra); en Instagram y Facebook, vídeos cortos. Los vídeos ya subidos no se pierden: sirven para conseguir los seguidores y las visualizaciones que pide el programa, y TikTok solo paga por lo que se sube después de la aceptación.
- Comprobar que la cuenta de TikTok es personal y no de empresa.

## 8. Puntos de control (los vigila la rutina diaria)

| Fecha | Vamos bien si… | Si no, se cambia… |
|---|---|---|
| Fin de noviembre 2026 | YouTube: los vídeos nuevos retienen más del 25 % y alguno pasa de 500 visitas. Pepa: más del 40 % de visualizaciones de 3 s en Facebook | Ganchos, duración y miniaturas |
| Fin de enero 2027 | YouTube: 200–300 suscriptores y algún vídeo de más de 5.000 visitas. Pepa: 1.000 seguidores en alguna red | Temas: doblar lo que funcione |
| Abril 2027 | YouTube: más de 2.000 h acumuladas. Pepa: 5.000 seguidores en alguna red | Plantearse 2 vídeos por semana, un formato más largo o más Reels |
| Julio 2027 | Solicitar la monetización en las plataformas que cumplan los requisitos | Revisar el plan entero con los datos |

Fuentes: TikTok Creator Rewards (resumen de requisitos y países): https://shortsfast.com/blog/tiktok-creator-rewards-eligibility-2026/ · Facebook, países de la monetización de contenido (oficial): https://www.facebook.com/business/help/267128784014981 · Facebook, qué es (oficial): https://www.facebook.com/business/help/1049081556813520 · Instagram, monetización 2026 (terceros): https://www.conbersa.ai/learn/instagram-creator-monetization-2026

## 9. PLAN DE INGRESOS (prioridad n.º 1 desde el 30/09/2026)

El objetivo del proyecto es COBRAR EN TODAS LAS PLATAFORMAS. Cada decisión de formato, duración, tema o publicación se justifica por cómo acerca el cobro. Antes de diseñar cualquier formato, se comprueban los requisitos de monetización.

| Plataforma | Palanca para cobrar | Qué cambiamos para llegar antes |
|---|---|---|
| YouTube | Horas de visualización (8.000) + 1.000 suscriptores | Vídeos de 12–15 min cuando la retención aguante (más horas por visita); Shorts para captar suscriptores; probar títulos y miniaturas en cada vídeo |
| Facebook | Invitación al programa de monetización | Reels todos los días que se pueda (hoy, 3 a la semana) y vídeos de más de 1 minuto; Facebook es donde Pepa ya llega a gente que no nos sigue |
| Instagram | Regalos (500 seguidores), suscripciones (10.000) y marcas | Activar los regalos en cuanto lleguemos a 500; preparar un dosier para marcas a partir de 5.000 |
| TikTok | 10.000 seguidores + 100.000 visualizaciones en 30 días + vídeos de más de 60 s | Versión de 61–75 s desde Pepa 019; más frecuencia (TikTok recomienda publicar a menudo) |
| Todas, desde 500 seguidores | **Enlaces de afiliado** (Amazon Afiliados España). Ayuda oficial: la página debe estar «consolidada» y tener «en la mayoría de los casos, al menos 500» seguidores orgánicos; tras el alta hay 180 días para conseguir 3 ventas, y solo entonces revisan la solicitud. NO darse de alta antes de los 500 (se gastaría el plazo) | Pepa: termómetro de nevera, tablas de cortar, táperes… Ticket Medio: libros sobre las empresas que contamos. Siempre avisando de que es un enlace de afiliado. Requiere que el usuario abra la cuenta (datos fiscales) |

Orden previsto de los primeros ingresos:
1. Afiliados y regalos de Instagram, en cuanto una cuenta llegue a 500 seguidores (fuente: https://afiliados.amazon.es/help/node/topic/G8TW5AE9XL2VX9VM).
2. Invitación de Facebook.
3. YouTube.
4. TikTok y marcas.

## 10. Quién sube y programa (revisado el 30/09/2026)

Claude NO sube vídeos manejando el navegador: las tres plataformas prohíben el acceso «por medios automatizados» y subir es la acción más vigilada. El paso al 100 % automático va por las API oficiales:

| Plataforma | API oficial | Limitación | Plan |
|---|---|---|---|
| Facebook | Graph API: Reels y publicaciones en la página, con programación | App de Meta en modo desarrollo (vale para cuentas propias) | Tarea u-meta-api (5/10). Después, Claude publica y programa |
| Instagram | Graph API: Reels y carruseles (máx. 90 s por Reel y 25 publicaciones al día) | **No admite programar**: se publica en el momento, y el ordenador tiene que estar encendido a esa hora | Publicar con una tarea de Windows a la hora elegida o pasar Instagram a horario de mañana. Se decide con los datos |
| YouTube | Data API: subir, título, etiquetas, capítulos, programar (publishAt) | Proyecto sin auditar = los vídeos se quedan en privado. Hay que pedir la auditoría a Google (semanas) | Tarea u-youtube-api (6/10) y solicitud de auditoría. Mientras, sube el usuario con las fichas de Claude |
| TikTok | Content Posting API | Sin auditoría, solo publica en privado (SELF_ONLY), y la auditoría es para empresas con app pública | Sigue a mano, en lotes quincenales |

Fuentes: https://developers.google.com/youtube/v3/docs/videos/insert · https://developers.tiktok.com/docs/en/content-sharing-guidelines · https://postproxy.dev/how-to/schedule-instagram-reels/
