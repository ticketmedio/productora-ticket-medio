# Rutina SEO diaria de Claude (la lanza sola una tarea programada de Windows, de lunes a viernes a las 9:00)

Trabajas sin nadie delante. Todo en ESPAÑOL DE ESPAÑA. Lee antes seo/00_ESTRATEGIA_SEO.md (sobre todo las líneas rojas).

1. `git pull`.
2. `node herramientas/estadisticas.js` (tarda unos minutos). Si alguna plataforma sale «SIN SESIÓN», NO intentes entrar: apúntalo y avisa en la Sala de que el usuario tiene que abrir ABRIR_SESIONES_REDES.bat y volver a entrar.
3. Lee los .txt de privado/estadisticas/<hoy>/ (y las .png si hace falta) y el último informe de privado/seo_diario/. Saca, para cada plataforma: suscriptores/seguidores, visualizaciones, CTR y duración media (YouTube), y las cifras de cada vídeo o Reel publicado. Busca comentarios nuevos en nuestros vídeos.
4. Escribe privado/seo_diario/<hoy>.md: cifras de hoy, diferencia con el último informe, qué funciona y qué no, UNA recomendación concreta (título, miniatura, gancho, horario, tema) y, para cada comentario nuevo, una respuesta propuesta (distinta cada vez, cercana, sin enlaces ni «suscríbete»).
5. Publica el resumen en la Sala con `python web/claude_sala.py mensaje "..."`, que empiece por «📈 Resumen SEO del <día>:». Máximo ~600 caracteres, sin nombres de personas (la Sala es pública), con las 2–3 cifras clave y la recomendación. Si hay que hacer algo (volver a entrar, responder comentarios que Claude aún no puede responder solo), dilo en una frase.
6. Si de ahí sale una mejora para un vídeo aún no publicado, apúntala en seo/PENDIENTES.md (crea el archivo si no existe). NO toques los vídeos ni los textos ya programados.
7. `git add -A`, comprueba con `git ls-files | grep -i privado` que no sale nada, `git commit -m "SEO: resumen diario <fecha>"` y `git push`.

PROHIBIDO en esta rutina: seguir cuentas, dar «me gusta», comentar, publicar o cambiar nada en YouTube, Meta o TikTok desde el navegador. Solo leer.

NOTA (30/09): los Reels de Instagram SÍ tienen su texto (lo confirmó el usuario); las estadísticas de Meta a veces no lo enseñan. No vuelvas a pedirle que lo ponga.
