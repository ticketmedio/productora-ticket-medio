# Productora Ticket Medio / Pepa Pita — instrucciones para Claude

Esta carpeta es una productora de vídeos *faceless* que lleva Claude para el usuario. **Lee antes de nada:**

1. `memoria_claude/user-profile.md`: quién es el usuario y cómo trabajar con él.
2. `memoria_claude/project-youtube-faceless.md`: estado del proyecto, cuentas, herramientas, decisiones y lecciones.
3. `youtube/00_BRIEF.md`: el encargo original, literal. Es la especificación del sistema.

Si la memoria automática de Claude Code en este ordenador está vacía o es más antigua, copia a ella los archivos de `memoria_claude/`. Si la guardas de nuevo, actualiza también esta carpeta, que es la que viaja entre ordenadores.

## GitHub (copia privada para verlo desde cualquier sitio)
- Repositorio PRIVADO: https://github.com/MaletaLista79/productora-ticket-medio (cuenta de GitHub del usuario: MaletaLista79).
- Al empezar cada sesión: `git pull`. Al terminar cada trabajo importante: `git add -A`, `git commit` y `git push`.
- `.gitignore` deja fuera las claves (`config/claves.txt`), el navegador, `node_modules`, los vídeos (.mp4), las voces y los clips. NUNCA subas claves: antes de cada subida, comprueba con `git ls-files` que no aparezca `config/claves.txt`.
- En otro ordenador: `git clone` del repositorio + `INSTALAR_EN_ESTE_ORDENADOR.bat` + crear `config/claves.txt` a mano (no está en GitHub).

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
