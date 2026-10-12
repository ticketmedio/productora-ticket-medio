#!/bin/bash
# Sube el trabajo a GitHub sin quedarse atascado: uso  herramientas/subir.sh "mensaje"
cd "$(dirname "$0")/.."
export PATH="$HOME/.local/bin:$PATH"
[ -d .git/rebase-merge ] && [ -z "$(git diff --name-only --diff-filter=U)" ] && rm -rf .git/rebase-merge   # restos de un rebase ya terminado
rm -f .git/index.lock 2>/dev/null
git add -A web seo herramientas youtube redes archivo memoria_claude CLAUDE.md .gitignore 2>/dev/null
git commit -q -m "${1:-Actualización}

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" 2>/dev/null
git pull --rebase 2>&1 | tail -1
git push 2>&1 | tail -1
git status -sb | head -2
