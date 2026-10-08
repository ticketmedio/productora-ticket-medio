@echo off
rem Autoriza UNA VEZ el acceso de solo lectura a las estadisticas de YouTube (API oficial). Ver la tarea de la Sala.
cd /d "%~dp0"
python herramientas\youtube_autorizar.py
echo.
pause
