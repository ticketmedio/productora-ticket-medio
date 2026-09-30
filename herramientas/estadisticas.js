// Descarga las estadísticas de YouTube Studio, Meta Business Suite y TikTok Studio
// usando el perfil PRIVADO de Edge (privado/perfil_navegador), donde el usuario
// ya entró una vez con ABRIR_SESIONES_REDES.bat. No usa ni guarda contraseñas.
//
// Uso:  node herramientas/estadisticas.js            (todas las plataformas)
//       node herramientas/estadisticas.js youtube    (solo una: youtube | meta | tiktok)
//       node herramientas/estadisticas.js url https://...   (una página suelta)
//       añadir --ver para ver la ventana (si un sitio rechaza el modo oculto)
// Salida: privado/estadisticas/AAAA-MM-DD/<nombre>.png y <nombre>.txt

const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const RAIZ = path.resolve(__dirname, '..');
const PERFIL = path.join(RAIZ, 'privado', 'perfil_navegador');
const EDGE = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const hoy = new Date().toISOString().slice(0, 10);
const SALIDA = path.join(RAIZ, 'privado', 'estadisticas', hoy);

// {canal} se sustituye por el identificador del canal que devuelve YouTube Studio
const PAGINAS = {
  youtube: [
    ['yt_resumen_28d', 'https://studio.youtube.com/channel/{canal}/analytics/tab-overview/period-default'],
    ['yt_contenido', 'https://studio.youtube.com/channel/{canal}/analytics/tab-content/period-default'],
    ['yt_audiencia', 'https://studio.youtube.com/channel/{canal}/analytics/tab-build_audience/period-default'],
    ['yt_videos', 'https://studio.youtube.com/channel/{canal}/videos/upload'],
    ['yt_shorts', 'https://studio.youtube.com/channel/{canal}/videos/short'],
  ],
  meta: [
    ['meta_resumen', 'https://business.facebook.com/latest/insights/overview'],
    ['meta_resultados', 'https://business.facebook.com/latest/insights/results'],
    ['meta_contenido', 'https://business.facebook.com/latest/insights/content'],
    ['meta_audiencia', 'https://business.facebook.com/latest/insights/audience'],
  ],
  tiktok: [
    ['tt_resumen', 'https://www.tiktok.com/tiktokstudio/analytics'],
    ['tt_contenido', 'https://www.tiktok.com/tiktokstudio/analytics/content'],
    ['tt_seguidores', 'https://www.tiktok.com/tiktokstudio/analytics/followers'],
    ['tt_publicaciones', 'https://www.tiktok.com/tiktokstudio/content'],
  ],
};

const PISTAS_LOGIN = /(iniciar sesi[oó]n|log in|sign in|inicia sesi[oó]n|accounts\.google\.com|\/login)/i;

async function capturar(pagina, nombre, url) {
  try {
    await pagina.goto(url, { waitUntil: 'networkidle2', timeout: 60000 });
  } catch (e) { /* algunas páginas nunca dejan la red en calma: seguimos */ }
  await new Promise(r => setTimeout(r, 6000)); // gráficos y tablas cargan tarde
  // las listas largas (TikTok, Meta) cargan más filas al bajar: bajamos hasta el final
  for (let i = 0; i < 15; i++) {
    const alto = await pagina.evaluate(() => {
      const caja = [...document.querySelectorAll('*')].filter(e => e.scrollHeight > e.clientHeight + 50 &&
        /(auto|scroll)/.test(getComputedStyle(e).overflowY)).sort((a, b) => b.scrollHeight - a.scrollHeight)[0];
      (caja || document.scrollingElement).scrollTop = 1e9;
      window.scrollTo(0, 1e9);
      return (caja || document.scrollingElement).scrollHeight;
    });
    await new Promise(r => setTimeout(r, 1500));
    const nuevo = await pagina.evaluate(() => document.body.innerText.length);
    if (i > 0 && nuevo === capturar._ultimo && alto === capturar._alto) break;
    capturar._ultimo = nuevo; capturar._alto = alto;
  }
  const final = pagina.url();
  const texto = await pagina.evaluate(() => document.body ? document.body.innerText : '');
  fs.writeFileSync(path.join(SALIDA, nombre + '.txt'), `URL: ${final}\n\n${texto}`);
  await pagina.screenshot({ path: path.join(SALIDA, nombre + '.png'), fullPage: true });
  const sinSesion = PISTAS_LOGIN.test(final) || (texto.length < 1500 && PISTAS_LOGIN.test(texto));
  console.log(`${sinSesion ? 'SIN SESIÓN' : 'ok'}  ${nombre}  (${texto.length} caracteres)  ${final}`);
  return { final, texto, sinSesion };
}

(async () => {
  if (!fs.existsSync(PERFIL)) {
    console.log('Falta el perfil privado: el usuario tiene que abrir ABRIR_SESIONES_REDES.bat y entrar en las 3 webs.');
    process.exit(1);
  }
  fs.mkdirSync(SALIDA, { recursive: true });
  const args = process.argv.slice(2);
  const ver = args.includes('--ver');
  const pedidos = args.filter(a => a !== '--ver');

  const navegador = await puppeteer.launch({
    executablePath: EDGE,
    userDataDir: PERFIL,
    headless: !ver,
    defaultViewport: { width: 1600, height: 1000 },
    args: ['--no-first-run', '--no-default-browser-check', '--lang=es-ES'],
    ignoreDefaultArgs: ['--enable-automation'],
  });
  const pagina = await navegador.newPage();
  await pagina.setUserAgent((await navegador.userAgent()).replace('HeadlessChrome', 'Chrome'));

  try {
    if (pedidos[0] === 'url') {
      await capturar(pagina, 'suelta_' + Date.now(), pedidos[1]);
    } else {
      const plataformas = pedidos.length ? pedidos : Object.keys(PAGINAS);
      for (const p of plataformas) {
        let canal = null;
        if (p === 'youtube') {
          const r = await capturar(pagina, 'yt_panel', 'https://studio.youtube.com');
          const m = r.final.match(/channel\/(UC[\w-]+)/);
          if (!m) { console.log('YouTube: no se encontró el canal (¿sesión cerrada?)'); continue; }
          canal = m[1];
        }
        for (const [nombre, url] of PAGINAS[p] || []) {
          const r = await capturar(pagina, nombre, url.replace('{canal}', canal));
          if (r.sinSesion) break; // sin sesión no tiene sentido seguir con esta plataforma
        }
      }
    }
  } finally {
    await navegador.close();
  }
  console.log('Guardado en ' + SALIDA);
})();
