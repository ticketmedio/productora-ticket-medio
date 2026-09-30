@echo off
rem Abre el Edge PRIVADO de Claude (perfil en privado\perfil_navegador, que no se sube a GitHub)
rem con YouTube Studio, Meta Business Suite y TikTok Studio. Entra en las tres y cierra la ventana.
cd /d "%~dp0"
if not exist "privado\perfil_navegador" mkdir "privado\perfil_navegador"
start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --user-data-dir="%~dp0privado\perfil_navegador" --no-first-run --no-default-browser-check "https://studio.youtube.com" "https://business.facebook.com/latest/insights" "https://www.tiktok.com/tiktokstudio/analytics"
