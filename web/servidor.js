// Servidor local de la Sala de Producción.
// Sirve la página en http://localhost:4321 y guarda todo en datos.json (misma carpeta).
// Claude lee y escribe datos.json directamente; la página lo relee cada 5 segundos.
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 4321;
const DATA = path.join(__dirname, 'datos.json');
const PAGE = path.join(__dirname, 'sala_produccion.html');

const WHO = ['tu', 'claude'];
const KINDS = ['tarea', 'publicacion', 'material'];
const PROJECTS = ['youtube', 'redes', 'general'];
const STATUSES = ['pendiente', 'en_curso', 'hecho'];
const PLATFORMS = ['YouTube', 'Shorts', 'Instagram', 'TikTok', 'Facebook'];

function read() {
  try {
    const d = JSON.parse(fs.readFileSync(DATA, 'utf8'));
    if (!Array.isArray(d.tareas)) d.tareas = [];
    if (!Array.isArray(d.mensajes)) d.mensajes = [];
    return d;
  } catch (e) {
    return { tareas: [], mensajes: [] };
  }
}

function write(d) {
  const tmp = DATA + '.tmp';
  fs.writeFileSync(tmp, JSON.stringify(d, null, 2), 'utf8');
  fs.renameSync(tmp, DATA);
  publicarPronto();
}

// ── Publicación en GitHub: la versión web de la Sala (GitHub Pages) lee web/datos.json del repositorio ──
const { execFile } = require('child_process');
const RAIZ = path.join(__dirname, '..');
let temporizador = null, publicando = false;
function git(args) {
  return new Promise((ok) => execFile('git', args, { cwd: RAIZ, windowsHide: true }, (e, out) => ok({ e, out: String(out || '') })));
}
async function publicar() {
  if (publicando) return publicarPronto();
  publicando = true;
  try {
    const cambios = await git(['status', '--porcelain', 'web/datos.json']);
    if (cambios.out.trim()) {
      await git(['add', 'web/datos.json']);
      await git(['commit', '-q', '-m', 'Sala: actualización']);
      await git(['pull', '-q', '--rebase', '--autostash']);
      const r = await git(['push', '-q']);
      console.log(r.e ? 'No se pudo subir a GitHub (se reintentará).' : 'Sala publicada en la web: ' + new Date().toLocaleTimeString('es-ES'));
    }
  } finally { publicando = false; }
}
function publicarPronto() { clearTimeout(temporizador); temporizador = setTimeout(publicar, 15000); }
setInterval(publicar, 60000);   // también recoge los cambios que hace Claude directamente en datos.json

function readBody(req) {
  return new Promise((resolve, reject) => {
    let s = '';
    req.on('data', (c) => { s += c; if (s.length > 1e6) req.destroy(); });
    req.on('end', () => { try { resolve(s ? JSON.parse(s) : {}); } catch (e) { reject(e); } });
    req.on('error', reject);
  });
}

function send(res, code, obj) {
  res.writeHead(code, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' });
  res.end(JSON.stringify(obj));
}

const text = (v, n) => String(v == null ? '' : v).slice(0, n);
const pick = (v, list, def) => (list.includes(v) ? v : def);

function cleanTask(id, b) {
  return {
    id,
    title: text(b.title, 200),
    date: /^\d{4}-\d{2}-\d{2}$/.test(b.date || '') ? b.date : '',
    who: pick(b.who, WHO, 'tu'),
    kind: pick(b.kind, KINDS, 'tarea'),
    project: pick(b.project, PROJECTS, 'general'),
    status: pick(b.status, STATUSES, 'pendiente'),
    platforms: Array.isArray(b.platforms) ? b.platforms.filter((p) => PLATFORMS.includes(p)) : [],
    notes: text(b.notes, 4000),
    createdAt: text(b.createdAt, 40) || new Date().toISOString(),
    createdBy: pick(b.createdBy, WHO, 'tu'),
    comentarios: Array.isArray(b.comentarios) ? b.comentarios.slice(-300) : [],
    updatedAt: new Date().toISOString(),
  };
}

const server = http.createServer(async (req, res) => {
  try {
    const url = new URL(req.url, 'http://localhost');

    if (req.method === 'GET' && (url.pathname === '/' || url.pathname === '/index.html')) {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
      return res.end(fs.readFileSync(PAGE));
    }

    if (req.method === 'GET' && url.pathname === '/api/data') return send(res, 200, read());

    const m = url.pathname.match(/^\/api\/tareas\/([A-Za-z0-9_-]{1,60})$/);
    if (m && req.method === 'PUT') {
      const body = await readBody(req);
      const d = read();
      const i = d.tareas.findIndex((t) => t.id === m[1]);
      const prev = i >= 0 ? d.tareas[i] : {};
      const task = cleanTask(m[1], { ...prev, ...body, createdAt: prev.createdAt || body.createdAt, createdBy: prev.createdBy || body.createdBy });
      if (!task.title) return send(res, 400, { error: 'Falta el título' });
      if (i >= 0) d.tareas[i] = task; else d.tareas.push(task);
      write(d);
      return send(res, 200, task);
    }
    if (m && req.method === 'DELETE') {
      const d = read();
      d.tareas = d.tareas.filter((t) => t.id !== m[1]);
      write(d);
      return send(res, 200, { ok: true });
    }

    const c = url.pathname.match(/^\/api\/tareas\/([A-Za-z0-9_-]{1,60})\/comentarios$/);
    if (c && req.method === 'POST') {
      const body = await readBody(req);
      const msg = text(body.text, 4000).trim();
      if (!msg) return send(res, 400, { error: 'Comentario vacío' });
      const d = read();
      const task = d.tareas.find((t) => t.id === c[1]);
      if (!task) return send(res, 404, { error: 'Tarea no encontrada' });
      if (!Array.isArray(task.comentarios)) task.comentarios = [];
      const entry = { id: 'c-' + Date.now().toString(36), text: msg, author: 'tu', createdAt: new Date().toISOString() };
      task.comentarios.push(entry);
      write(d);
      return send(res, 200, entry);
    }

    if (req.method === 'POST' && url.pathname === '/api/mensajes') {
      const body = await readBody(req);
      const msg = text(body.text, 4000).trim();
      if (!msg) return send(res, 400, { error: 'Mensaje vacío' });
      const d = read();
      const entry = { id: 'm-' + Date.now().toString(36), text: msg, author: 'tu', createdAt: new Date().toISOString() };
      d.mensajes.push(entry);
      write(d);
      return send(res, 200, entry);
    }

    send(res, 404, { error: 'No encontrado' });
  } catch (e) {
    console.error(e);
    send(res, 500, { error: 'Error interno' });
  }
});

server.on('error', (e) => {
  if (e.code === 'EADDRINUSE') {
    console.log('La Sala de Producción ya estaba abierta.');
    process.exit(0);
  }
  throw e;
});

server.listen(PORT, '127.0.0.1', () => {
  console.log('Sala de Producción funcionando en http://localhost:' + PORT);
  console.log('Deja esta ventana abierta (puedes minimizarla). Ciérrala para apagar la Sala.');
});
