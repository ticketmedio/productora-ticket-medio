// Lee TODAS las publicaciones de TikTok Studio (publicadas y programadas) con el perfil privado del navegador. Solo lectura.
// La tabla es «virtual» (solo existen las filas que se ven), así que se baja poco a poco y se apunta cada fila.
// Uso: node herramientas/tiktok_programados.js   → imprime «fecha | duración | inicio del texto» y lo guarda en privado/estadisticas/AAAA-MM-DD/tt_todas.txt
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const RAIZ = path.resolve(__dirname, '..');
const PERFIL = path.join(RAIZ, 'privado', process.platform === 'darwin' ? 'perfil_navegador_mac' : 'perfil_navegador');
const CHROME = ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'].find((p) => fs.existsSync(p));
const SALIDA = path.join(RAIZ, 'privado', 'estadisticas', new Date().toISOString().slice(0, 10));
const espera = (ms) => new Promise((r) => setTimeout(r, ms));

(async () => {
  fs.mkdirSync(SALIDA, { recursive: true });
  const nav = await puppeteer.launch({
    executablePath: CHROME, userDataDir: PERFIL, headless: true, defaultViewport: { width: 1600, height: 1000 },
    args: ['--no-first-run', '--no-default-browser-check', '--lang=es-ES'],
    ignoreDefaultArgs: ['--enable-automation', '--use-mock-keychain', '--password-store=basic'],
  });
  const p = await nav.newPage();
  await p.setUserAgent((await nav.userAgent()).replace('HeadlessChrome', 'Chrome'));
  const filas = new Map();
  try {
    try { await p.goto('https://www.tiktok.com/tiktokstudio/content', { waitUntil: 'networkidle2', timeout: 60000 }); } catch (e) { /* sigue */ }
    await espera(6000);
    let quietas = 0;
    for (let i = 0; i < 200 && quietas < 6; i++) {
      const vistas = await p.evaluate(() => {
        const fecha = /^\d+ \S+,? \d+:\d+$/;
        const out = [];
        for (const el of document.querySelectorAll('div, span, p')) {
          const t = (el.innerText || '').trim();
          if (!fecha.test(t) || el.children.length) continue;
          let fila = el; for (let k = 0; k < 8 && fila && !/\d\d:\d\d\n/.test(fila.innerText || ''); k++) fila = fila.parentElement;
          const txt = (fila ? fila.innerText : '').split('\n').map((x) => x.trim()).filter(Boolean);
          out.push([t, txt.find((x) => /^\d\d:\d\d$/.test(x)) || '', txt.find((x) => x.length > 25) || '']);
        }
        const caja = [...document.querySelectorAll('*')].filter((e) => e.scrollHeight > e.clientHeight + 50 &&
          /(auto|scroll)/.test(getComputedStyle(e).overflowY)).sort((a, b) => b.scrollHeight - a.scrollHeight)[0] || document.scrollingElement;
        caja.scrollTop += 500; window.scrollBy(0, 500);
        return out;
      });
      const antes = filas.size;
      for (const [f, d, t] of vistas) filas.set(f + '|' + t.slice(0, 40), [f, d, t]);
      quietas = filas.size === antes ? quietas + 1 : 0;
      await espera(1200);
    }
  } finally { await nav.close(); }
  const lineas = [...filas.values()].map(([f, d, t]) => `${f} | ${d} | ${t.slice(0, 90)}`);
  fs.writeFileSync(path.join(SALIDA, 'tt_todas.txt'), lineas.join('\n') + '\n');
  console.log(lineas.join('\n'));
  console.log(`${lineas.length} publicaciones`);
})();
