// SOLO LECTURA: abre el panel profesional de Instagram con el perfil privado del Mac y vuelca (1) el público (países, edad, género)
// y (2) los insights de cada Reel («Ver insights»). No sigue, no da «me gusta», no comenta. Salida: privado/estadisticas/AAAA-MM-DD/ig_*.txt
const fs = require('fs'), path = require('path'), puppeteer = require('puppeteer-core');
const RAIZ = path.resolve(__dirname, '..');
const dia = new Date().toISOString().slice(0, 10), SAL = path.join(RAIZ, 'privado', 'estadisticas', dia); fs.mkdirSync(SAL, { recursive: true });
const espera = (ms) => new Promise(r => setTimeout(r, ms));
async function clic(p, texto, ultimo) {
  return p.evaluate((t, u) => {
    const c = [...document.querySelectorAll('a,div[role=button],button,span')].filter(e => e.innerText && e.innerText.trim() === t && e.offsetParent);
    const e = u ? c[c.length - 1] : c[0]; if (e) { e.click(); return true; } return false;
  }, texto, !!ultimo);
}
(async () => {
  const b = await puppeteer.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', userDataDir: path.join(RAIZ, 'privado', 'perfil_navegador_mac'), headless: true,
    defaultViewport: { width: 1400, height: 1100 }, args: ['--no-first-run', '--lang=es-ES'], ignoreDefaultArgs: ['--enable-automation', '--use-mock-keychain', '--password-store=basic'] });
  const p = await b.newPage();
  await p.goto('https://www.instagram.com/accounts/insights/?timeframe=30', { waitUntil: 'networkidle2', timeout: 60000 }).catch(() => {});
  await espera(4000);
  console.log('clic seguidores:', await clic(p, 'Seguidores', true)); await espera(4000);
  fs.writeFileSync(path.join(SAL, 'ig_publico.txt'), p.url() + '\n\n' + await p.evaluate(() => document.body.innerText));
  await p.screenshot({ path: path.join(SAL, 'ig_publico.png'), fullPage: true });
  const reels = JSON.parse(fs.readFileSync(path.join(SAL, 'ig_reels.json'), 'utf8'));
  let n = 0;
  for (const r of reels) {
    const q = await b.newPage();
    await q.goto(r.href, { waitUntil: 'networkidle2', timeout: 60000 }).catch(() => {}); await espera(2500);
    const ok = await clic(q, 'Ver insights'); await espera(4000);
    const txt = await q.evaluate(() => [...document.querySelectorAll('[role=dialog]')].map(d => d.innerText).join('\n---\n') || document.body.innerText.slice(0, 3000));
    fs.writeFileSync(path.join(SAL, `ig_reel_${++n}.txt`), r.href + ' (ver insights: ' + ok + ')\n\n' + txt);
    await q.screenshot({ path: path.join(SAL, `ig_reel_${n}.png`) }); await q.close();
  }
  await b.close();
})();
