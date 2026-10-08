@echo off
rem Rutina SEO diaria de Claude. La lanza la tarea programada "Claude SEO diario" (todos los días, 8:00).
rem Usa el modelo Sonnet (30/09) para no gastar la cuota de la mañana del usuario.
rem Para quitarla: Programador de tareas de Windows > "Claude SEO diario" > Eliminar.
cd /d "%~dp0.."
set LOG=privado\seo_diario\registro.log
rem Fecha AAAA-MM-DD (en este Windows la fecha sale como DD/MM/AAAA). Si hoy ya se hizo, no se repite.
set F=%date:~6,4%-%date:~3,2%-%date:~0,2%
if exist "privado\seo_diario\%F%.hecho" exit /b 0
echo ===== %date% %time% >> %LOG%
"%USERPROFILE%\.local\bin\claude.exe" -p --model sonnet "Ejecuta la rutina de seo/RUTINA_DIARIA.md tal como esta escrita." --permission-mode acceptEdits --allowedTools "Read" "Write" "Edit" "Glob" "Grep" "Bash(node herramientas/estadisticas.js:*)" "Bash(python web/claude_sala.py:*)" "Bash(python herramientas/yt_buscar.py:*)" "Bash(python herramientas/yt_video.py:*)" "WebSearch" "WebFetch" "Bash(git pull:*)" "Bash(git add:*)" "Bash(git commit:*)" "Bash(git push:*)" "Bash(git ls-files:*)" "Bash(ls:*)" "Bash(cat:*)" "Bash(grep:*)" "Bash(date:*)" >> %LOG% 2>&1
echo. > "privado\seo_diario\%F%.hecho"
echo ===== fin %date% %time% >> %LOG%
