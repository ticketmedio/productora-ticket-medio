// Descarga un PDF con Chrome oculto (para webs que bloquean curl). Uso: node herramientas/bajar_pdf.js URL destino.pdf
const puppeteer = require('puppeteer-core'), fs = require('fs');
(async () => {
  const [url, destino] = process.argv.slice(2);
  const b = await puppeteer.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: 'new', args: ['--no-first-run'] });
  const p = await b.newPage();
  await p.goto(new URL(url).origin + '/', { waitUntil: 'domcontentloaded', timeout: 60000 }).catch(() => {});
  const datos = await p.evaluate(async (u) => { const r = await fetch(u); const buf = new Uint8Array(await r.arrayBuffer()); let s = ''; for (let i = 0; i < buf.length; i += 32768) s += String.fromCharCode.apply(null, buf.subarray(i, i + 32768)); return btoa(s); }, url);
  fs.writeFileSync(destino, Buffer.from(datos, 'base64')); await b.close();
})().catch(e => { console.error(e.message); process.exit(1); });
