@echo off
chcp 65001 >nul
title Instalar la productora en este ordenador
cd /d "%~dp0"
echo.
echo  ============================================================
echo    PRODUCTORA TICKET MEDIO / PEPA PITA - INSTALACION
echo  ============================================================
echo.
echo  Esto instala (gratis) los programas que usa Claude para
echo  hacer los videos: Node.js, Python y FFmpeg.
echo  Solo hace falta hacerlo UNA VEZ en cada ordenador.
echo  Puede tardar 5-10 minutos. Si Windows pregunta si quieres
echo  permitir cambios, pulsa "Si".
echo.
pause

where winget >nul 2>nul
if errorlevel 1 (
  echo.
  echo  [!] Este Windows no tiene "winget". Abre la Microsoft Store,
  echo      busca "Instalador de aplicacion" ^(App Installer^), instalalo
  echo      y vuelve a ejecutar este archivo.
  pause
  exit /b 1
)

echo.
echo  [1/5] Node.js ...
winget install --id OpenJS.NodeJS.LTS -e --silent --accept-source-agreements --accept-package-agreements
echo.
echo  [2/5] Python ...
winget install --id Python.Python.3.13 -e --silent --accept-source-agreements --accept-package-agreements
echo.
echo  [3/5] FFmpeg ...
winget install --id Gyan.FFmpeg -e --silent --accept-source-agreements --accept-package-agreements

echo.
echo  [4/5] Complementos de Python y de los graficos ...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$env:Path=[Environment]::GetEnvironmentVariable('Path','Machine')+';'+[Environment]::GetEnvironmentVariable('Path','User');" ^
  "python -m pip install --quiet --upgrade pillow numpy;" ^
  "if (-not (Test-Path '.\herramientas\node_modules\puppeteer-core')) { Push-Location .\herramientas; npm install --no-fund --no-audit; Pop-Location };" ^
  "if (-not (Test-Path '.\herramientas\navegador\chrome-headless-shell')) { Push-Location .\herramientas; npx --yes @puppeteer/browsers install chrome-headless-shell@stable --path (Join-Path (Get-Location) 'navegador'); Pop-Location }"

echo.
echo  [5/5] Icono "Sala de Produccion" en el escritorio ...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$d=[Environment]::GetFolderPath('Desktop'); $w=New-Object -ComObject WScript.Shell;" ^
  "$l=$w.CreateShortcut((Join-Path $d 'Sala de Produccion.lnk'));" ^
  "$l.TargetPath=(Resolve-Path '.\web\Abrir Sala de Produccion.bat').Path; $l.WorkingDirectory=(Resolve-Path '.\web').Path;" ^
  "$l.WindowStyle=7; $l.IconLocation='C:\Windows\System32\shell32.dll,165'; $l.Save()"

echo.
echo  ============================================================
echo    LISTO. Ya puedes abrir la Sala con el icono del escritorio.
echo    Despues abre esta carpeta en VS Code y dile a Claude:
echo       "Seguimos desde casa"
echo  ============================================================
echo.
pause
