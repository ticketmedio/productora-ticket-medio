# Productora Ticket Medio / Pepa Pita — instrucciones para Claude

Esta carpeta es una productora de vídeos *faceless* que lleva Claude para el usuario. **Lee antes de nada:**

1. `memoria_claude/user-profile.md`: quién es el usuario y cómo trabajar con él.
2. `memoria_claude/project-youtube-faceless.md`: estado del proyecto, cuentas, herramientas, decisiones y lecciones.
3. `youtube/00_BRIEF.md`: el encargo original, literal. Es la especificación del sistema.

Si la memoria automática de Claude Code en este ordenador está vacía o es más antigua, copia a ella los archivos de `memoria_claude/`. Si la guardas de nuevo, actualiza también esta carpeta, que es la que viaja entre ordenadores.

## GitHub (repositorio PÚBLICO: lo ve cualquiera; decisión del usuario del 28/09/2026)
- https://github.com/ticketmedio/productora-ticket-medio (cuenta de GitHub del proyecto: ticketmedio; gh ya tiene la sesión iniciada).
- Al empezar cada sesión: `git pull`. Al terminar cada trabajo importante: `git add -A`, `git commit` y `git push`.
- Al ser PÚBLICO, NUNCA se sube: claves (`config/`), música de la Biblioteca de audio de YouTube, audios, vídeos, PDF descargados, el texto extraído de esos PDF ni artículos de prensa copiados (`fuentes/*.txt`), ni fotogramas o transcripciones de vídeos de otros canales (`referencia_*`). Todo eso está en `.gitignore`: antes de cada subida, comprueba con `git ls-files` que no se cuela nada. Tampoco datos personales del usuario.
- En otro ordenador: `git clone` + `INSTALAR_EN_ESTE_ORDENADOR.bat` + crear `config/claves.txt` a mano + volver a poner la música de la Biblioteca de audio de YouTube en `musica/`.
- **Sala de Producción en la web:** https://ticketmedio.github.io/productora-ticket-medio/ (GitHub Pages lee `web/datos.json`). `claude_sala.py` (comentar, mensaje, estado) y el servidor local suben `datos.json` solos. Si editas `datos.json` con otro script, ejecuta después `python web/claude_sala.py publicar`.
- **Desde la web el usuario puede marcar tareas, comentar y escribir en el Tablón (29/09, AUTORIZADO expresamente por el usuario):** la página crea un «issue» con la API de GitHub usando una llave (token de grano fino, solo permiso «Issues») que el usuario pega una vez en cada navegador y que se guarda solo en su localStorage (nunca en el repositorio ni en el chat). `.github/workflows/sala_web.yml` + `web/aplicar_peticion.py` lo guardan en `web/web_cambios.json` (solo si el autor es la cuenta ticketmedio) y cierran el issue. Ese archivo solo lo escribe GitHub Actions; `claude_sala.py` (en cada orden, con `git pull`) y `servidor.js` (cada minuto) lo fusionan en `datos.json` (lista `aplicadosWeb`). Crear o borrar tareas sigue siendo solo en local o pidiéndoselo a Claude.
- Queda una copia antigua PRIVADA en MaletaLista79/productora-ticket-medio, que ya no se usa.

## Al empezar cada sesión
- Ejecuta `python web/claude_sala.py novedades` y contesta a lo que haya escrito el usuario en la Sala de Producción.
- Ejecuta `python herramientas/limpiar_publicados.py`: borra las carpetas de producción ya publicadas (guarda antes sus textos en `archivo/`). Cada vídeo nuevo que se programe se añade a `archivo/publicaciones.json` con su fecha de publicación. La carpeta `archivo/` no se borra nunca.
- Si el usuario viene de otro ordenador («seguimos desde casa»), comprueba que las herramientas funcionan: `python -c "import PIL, numpy"`, `node --version`, `python herramientas/comun.py`, y que exista `herramientas/navegador`. Si falta algo, dile que ejecute `INSTALAR_EN_ESTE_ORDENADOR.bat`, o instálalo tú.
- Si el usuario lo pide, vuelve a programar la revisión de la Sala cada 10 minutos con CronCreate.

## Reglas clave
- Español de España. El usuario no programa: ejecuta tú todo el código y dale solo pasos prácticos muy detallados (subir, publicar, crear cuentas).
- Las decisiones editoriales (guion, voz, gráficos, calidad) son tuyas: no le pidas opinión sobre ellas.
- Nunca pongas tareas en fin de semana.
- Nunca muestres ni pidas en el chat las claves de `config/claves.txt`.
- Todo dato debe ser verificable y tener su fuente en `10_FUENTES.md`.
