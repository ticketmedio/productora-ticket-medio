// Lee (SOLO LECTURA) los Reels del perfil de Instagram de Pepa Pita con el perfil privado del Mac:
// fecha, visualizaciones, «me gusta» y comentarios de cada uno. No sigue, no da «me gusta», no comenta.
// Uso: node herramientas/ig_reels.js [usuario]    Salida: privado/estadisticas/AAAA-MM-DD/ig_reels.json
const fs = require('fs'), path = require('path'), puppeteer = require('puppeteer-core');
const RAIZ = path.resolve(__dirname, '..');
const usuario = process.argv[2] || 'soypepapita';
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const dia = new Date().toISOString().slice(0, 10);
const SAL = path.join(RAIZ, 'privado', 'estadisticas', dia); fs.mkdirSync(SAL, { recursive: true });
(async () => {
  const b = await puppeteer.launch({ executablePath: CHROME, userDataDir: path.join(RAIZ, 'privado', 'perfil_navegador_mac'), headless: true,
    defaultViewport: { width: 1400, height: 1000 }, args: ['--no-first-run', '--lang=es-ES'], ignoreDefaultArgs: ['--enable-automation', '--use-mock-keychain', '--password-store=basic'] });
  const p = await b.newPage();
  await p.goto(`https://www.instagram.com/${usuario}/reels/`, { waitUntil: 'networkidle2', timeout: 60000 }).catch(() => {});
  await new Promise(r => setTimeout(r, 4000));
  for (let i = 0; i < 6; i++) { await p.evaluate(() => window.scrollTo(0, 1e9)); await new Promise(r => setTimeout(r, 1500)); }
  const tarjetas = await p.evaluate(() => [...document.querySelectorAll('a[href*="/reel/"]')].map(a => ({ href: a.href, texto: a.innerText.replace(/\n+/g, ' ').trim() })));
  const vistos = new Set(), lista = [];
  for (const t of tarjetas) if (!vistos.has(t.href)) { vistos.add(t.href); lista.push(t); }
  const salida = [];
  for (const t of lista) {
    const q = await b.newPage();
    await q.goto(t.href, { waitUntil: 'networkidle2', timeout: 60000 }).catch(() => {});
    await new Promise(r => setTimeout(r, 2500));
    const d = await q.evaluate(() => ({
      fecha: (document.querySelector('time') || {}).dateTime || '',
      titulo: (document.querySelector('time') || {}).title || '',
      texto: document.body.innerText.slice(0, 1200).replace(/\n+/g, ' | '),
    }));
    salida.push({ ...t, ...d }); await q.close();
  }
  fs.writeFileSync(path.join(SAL, 'ig_reels.json'), JSON.stringify(salida, null, 1));
  for (const s of salida) console.log(s.fecha.slice(0, 10), '|', s.texto_tarjeta || s.texto.slice(0, 160));
  await b.close();
})();
