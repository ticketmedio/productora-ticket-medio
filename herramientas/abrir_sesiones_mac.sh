#!/bin/bash
# Abre Chrome con el perfil PRIVADO de Claude en el Mac (privado/perfil_navegador_mac) para que el usuario entre UNA vez en las webs.
# No guarda contraseñas en el repositorio: las sesiones quedan solo en esa carpeta (privado/ está en .gitignore).
cd "$(dirname "$0")/.."
open -na "Google Chrome" --args --user-data-dir="$PWD/privado/perfil_navegador_mac" --no-first-run \
  "https://business.facebook.com/latest/insights/overview" "https://business.facebook.com/business/loginpage/?login_options[0]=IG"
