@echo off
rem Abre la Sala de Produccion: arranca el servidor (si no estaba ya) y abre el navegador.
rem Funciona en cualquier ordenador y desde cualquier carpeta (usa rutas relativas).
cd /d "%~dp0"

set "NODE=node"
where node >nul 2>nul
if errorlevel 1 (
  if exist "%ProgramFiles%\nodejs\node.exe" (
    set "NODE=%ProgramFiles%\nodejs\node.exe"
  ) else if exist "%LOCALAPPDATA%\Programs\nodejs\node.exe" (
    set "NODE=%LOCALAPPDATA%\Programs\nodejs\node.exe"
  ) else (
    echo.
    echo  Falta instalar Node.js en este ordenador.
    echo  Haz doble clic en INSTALAR_EN_ESTE_ORDENADOR.bat
    echo  ^(esta en la carpeta principal del proyecto^) y vuelve a probar.
    echo.
    pause
    exit /b 1
  )
)

start "Sala de Produccion (no cerrar)" /min "%NODE%" "%~dp0servidor.js"
timeout /t 2 /nobreak >nul
start "" http://localhost:4321
