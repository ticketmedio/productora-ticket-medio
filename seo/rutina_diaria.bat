@echo off
rem Rutina SEO diaria de Claude. La lanza la tarea programada "Claude SEO diario" (lunes a viernes, 9:00).
rem Para quitarla: Programador de tareas de Windows > "Claude SEO diario" > Eliminar.
cd /d "%~dp0.."
set LOG=privado\seo_diario\registro.log
echo ===== %date% %time% >> %LOG%
"%USERPROFILE%\.local\bin\claude.exe" -p "Ejecuta la rutina de seo/RUTINA_DIARIA.md tal como esta escrita." --permission-mode acceptEdits --allowedTools "Read" "Write" "Edit" "Glob" "Grep" "Bash(node herramientas/estadisticas.js:*)" "Bash(python web/claude_sala.py:*)" "Bash(git pull:*)" "Bash(git add:*)" "Bash(git commit:*)" "Bash(git push:*)" "Bash(git ls-files:*)" "Bash(ls:*)" "Bash(cat:*)" "Bash(grep:*)" "Bash(date:*)" >> %LOG% 2>&1
echo ===== fin %date% %time% >> %LOG%
