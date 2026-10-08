// Motor de gráficos animados de Ticket Medio.
// Uso: node graficos.js graficos.json CARPETA_SALIDA [id1 id2 ...]
// Cada tarjeta del JSON se dibuja en HTML (colores y tipografías del canal), se anima
// fotograma a fotograma con Edge y se guarda como clip MP4 1920x1080 a 30 fps.
const fs = require('fs');
const path = require('path');
const os = require('os');
const { spawn } = require('child_process');
const puppeteer = require('puppeteer-core');

const FPS = 30;
// Navegador propio (chrome-headless-shell en herramientas/navegador); si no está, se usa Edge.
function navegador() {
  const base = path.join(__dirname, 'navegador', 'chrome-headless-shell');
  if (fs.existsSync(base)) {
    for (const v of fs.readdirSync(base).sort().reverse()) {
      const exe = path.join(base, v, 'chrome-headless-shell-win64', 'chrome-headless-shell.exe');
      if (fs.existsSync(exe)) return exe;
    }
  }
  for (const p of ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                   '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge']) {
    if (fs.existsSync(p)) return p;
  }
  return 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
}
const EDGE = navegador();

function ffmpegPath() {
  const base = path.join(process.env.LOCALAPPDATA || '', 'Microsoft', 'WinGet', 'Packages');
  for (const d of fs.existsSync(base) ? fs.readdirSync(base) : []) {
    if (!d.startsWith('Gyan.FFmpeg')) continue;
    for (const sub of fs.readdirSync(path.join(base, d))) {
      const p = path.join(base, d, sub, 'bin', 'ffmpeg.exe');
      if (fs.existsSync(p)) return p;
    }
  }
  return 'ffmpeg';
}

const LOGO = path.join(__dirname, '..', 'youtube', 'marca', 'logo_800.png').replace(/\\/g, '/');

const CSS = `
*{box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;overflow:hidden}
body{background:#12161C;color:#FBFAF6;font-family:"JetBrains Mono",Consolas,monospace;position:relative}
body::before{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(251,250,246,.06) 1.6px,transparent 1.6px);background-size:34px 34px}
.brand{position:absolute;left:70px;top:52px;font-size:22px;letter-spacing:5px;color:#F5B301;font-weight:700}
.fuente{position:absolute;left:70px;bottom:48px;font-size:22px;color:#8A93A0;max-width:1500px}
.nota{position:absolute;right:70px;bottom:48px;font-size:20px;color:#8A93A0;letter-spacing:1px}
.stripe{position:absolute;left:0;right:0;bottom:0;height:10px;background:repeating-linear-gradient(-45deg,#F5B301 0 18px,#12161C 18px 36px)}
.big{font-family:"Big Shoulders Display","Archivo Black",sans-serif;font-weight:900;text-transform:uppercase;line-height:.9;letter-spacing:1px;margin:0}
.eyebrow{font-size:28px;letter-spacing:6px;color:#F5B301;font-weight:700;text-transform:uppercase}
.center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:28px;padding:0 140px}
.left{position:absolute;left:140px;right:140px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;gap:26px}
.amber{color:#F5B301}.naranja{color:#E0521B}.gris{color:#8A93A0}
.receipt{background:#FBFAF6;color:#12161C;width:820px;padding:44px 52px 60px;position:relative;box-shadow:0 30px 60px rgba(0,0,0,.5)}
.receipt::after{content:"";position:absolute;left:0;right:0;bottom:-22px;height:22px;background:linear-gradient(-45deg,transparent 15px,#FBFAF6 0) 0 0/30px 22px repeat-x,linear-gradient(45deg,transparent 15px,#FBFAF6 0) 0 0/30px 22px repeat-x}
.rh{text-align:center;font-weight:700;letter-spacing:4px;font-size:26px}
.rs{text-align:center;font-size:22px;color:#555C66;margin-top:6px}
.sep{border-top:3px dashed #12161C;margin:22px 0}
.rl{display:flex;justify-content:space-between;gap:18px;font-size:34px;line-height:1.7}
.rl .d{flex:1;border-bottom:3px dotted rgba(18,22,28,.3);transform:translateY(-14px)}
.rt{display:flex;justify-content:space-between;font-size:40px;font-weight:700;background:#12161C;color:#F5B301;padding:10px 16px}
.sello{position:absolute;z-index:3;right:-150px;bottom:-40px;border:8px solid #E0521B;color:#E0521B;font-family:"Big Shoulders Display",sans-serif;font-weight:900;font-size:66px;padding:6px 22px;text-transform:uppercase;letter-spacing:2px;background:rgba(251,250,246,.9)}
.barwrap{width:1560px;height:150px;background:rgba(251,250,246,.08);display:flex;overflow:hidden}
.seg{height:100%;display:flex;align-items:center;justify-content:center;font-family:"Big Shoulders Display",sans-serif;font-weight:900;font-size:64px;color:#12161C;white-space:nowrap;overflow:hidden}
.leyendas{width:1560px;display:flex;gap:0}
.ley{font-size:28px;line-height:1.35;padding-top:14px;overflow:hidden}
.item{display:flex;align-items:center;gap:36px;font-size:52px;font-weight:700}
.num{width:96px;height:96px;border-radius:50%;border:5px solid currentColor;display:flex;align-items:center;justify-content:center;font-family:"Big Shoulders Display",sans-serif;font-weight:900;font-size:60px;flex:none}
.panel{flex:1;border:4px solid rgba(251,250,246,.25);padding:46px 50px;display:flex;flex-direction:column;gap:14px;text-align:left}
.panel.hl{border-color:#E0521B;background:rgba(224,82,27,.12)}
.pv{font-family:"Big Shoulders Display",sans-serif;font-weight:900;font-size:170px;line-height:.9}
.pe{font-size:34px;letter-spacing:2px;text-transform:uppercase;color:#C9CDD3}
.pn{font-size:28px;color:#C9CDD3;line-height:1.4}
`;

// Código que corre dentro de la página: construye la tarjeta y define pintar(t)
const MOTOR = `
const S = window.SPEC; const $ = (h)=>{const d=document.createElement('div');d.innerHTML=h.trim();return d.firstChild;};
const cl=(x)=>Math.max(0,Math.min(1,x)); const ease=(x)=>1-Math.pow(1-cl(x),3);
const P=(t,a,d)=>ease((t-a)/d);
const esc=(s)=>String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/\\n/g,'<br>');
const fmt=(n,dec)=>n.toLocaleString('es-ES',{minimumFractionDigits:dec,maximumFractionDigits:dec,useGrouping:'always'});
document.body.append($('<div class="brand">TICKET MEDIO</div>'));
if(S.fuente) document.body.append($('<div class="fuente">Fuente: '+esc(S.fuente)+'</div>'));
if(S.nota) document.body.append($('<div class="nota">'+esc(S.nota)+'</div>'));
document.body.append($('<div class="stripe"></div>'));
const fade=(el,p,dy)=>{el.style.opacity=p;el.style.transform='translateY('+((1-p)*(dy||30))+'px)';};
let pintar=()=>{}; window.FIN=3;

if(S.tipo==='titular'){
  const c=$('<div class="center"></div>');
  const e=S.eyebrow?$('<div class="eyebrow">'+esc(S.eyebrow)+'</div>'):null;
  const h=$('<h1 class="big" style="font-size:'+(S.tam||150)+'px">'+esc(S.titulo).replace(/\\*(.+?)\\*/g,'<span class="amber">$1</span>')+'</h1>');
  const bar=$('<div style="height:10px;background:#F5B301;width:0"></div>');
  const sub=S.sub?$('<div style="font-size:38px;color:#C9CDD3;max-width:1300px;line-height:1.4">'+esc(S.sub)+'</div>'):null;
  [e,h,bar,sub].forEach(x=>x&&c.append(x)); document.body.append(c);
  pintar=(t)=>{ if(e)fade(e,P(t,0,.5)); fade(h,P(t,.15,.7),50); bar.style.width=(P(t,.5,.7)*260)+'px'; if(sub)fade(sub,P(t,.8,.6)); };
  window.FIN=1.6;
}

if(S.tipo==='cifra'){
  const c=$('<div class="center"></div>');
  const e=S.eyebrow?$('<div class="eyebrow">'+esc(S.eyebrow)+'</div>'):null;
  const n=$('<div class="big amber" style="font-size:'+(S.tam||300)+'px;display:flex;align-items:baseline;gap:20px"><span class="pre" style="font-size:.45em;color:#FBFAF6"></span><span class="v"></span><span class="suf" style="font-size:.42em;color:#FBFAF6;text-transform:none"></span></div>');
  n.querySelector('.pre').textContent=S.prefijo||''; n.querySelector('.suf').textContent=S.sufijo||'';
  const tx=S.texto?$('<div style="font-size:42px;max-width:1350px;line-height:1.35">'+esc(S.texto)+'</div>'):null;
  [e,n,tx].forEach(x=>x&&c.append(x)); document.body.append(c);
  const v=n.querySelector('.v'); const dec=S.decimales||0; const desde=S.desde||0;
  pintar=(t)=>{ if(e)fade(e,P(t,0,.5)); fade(n,P(t,.1,.5),40); v.textContent=fmt(desde+(S.numero-desde)*P(t,.1,1.4),dec); if(tx)fade(tx,P(t,1.1,.6)); };
  window.FIN=2;
}

if(S.tipo==='ticket'){
  const wrap=$('<div class="center"></div>');
  const r=$('<div class="receipt"></div>'); r.style.transform='rotate(-1.5deg)';
  r.append($('<div class="rh">'+esc(S.titulo||'TICKET')+'</div>'));
  if(S.subtitulo) r.append($('<div class="rs">'+esc(S.subtitulo)+'</div>'));
  r.append($('<div class="sep"></div>'));
  const ls=(S.lineas||[]).map(l=>{const el=$('<div class="rl"><span></span><span class="d"></span><span></span></div>');
    el.children[0].textContent=l.c; el.children[2].textContent=l.v; if(l.color==='naranja'){el.style.color='#E0521B';el.style.fontWeight=700;}
    r.append(el); return [el,l.t||0];});
  let tot=null; if(S.total){ r.append($('<div class="sep"></div>')); tot=$('<div class="rt"><span></span><span></span></div>');
    tot.children[0].textContent=S.total.c; tot.children[1].textContent=S.total.v; r.append(tot);}
  let sello=null; if(S.sello){ sello=$('<div class="sello"></div>'); sello.textContent=S.sello.texto; r.append(sello);}
  wrap.append(r); document.body.append(wrap);
  pintar=(t)=>{ fade(r,P(t,0,.6),80);
    ls.forEach(([el,a])=>{const p=P(t,a,.45); el.style.opacity=p; el.style.transform='translateX('+((1-p)*-30)+'px)';});
    if(tot){const p=P(t,S.total.t||0,.4); tot.style.opacity=p; tot.style.transform='scale('+(0.9+0.1*p)+')';}
    if(sello){const p=P(t,S.sello.t,.35); sello.style.opacity=p; sello.style.transform='rotate(-12deg) scale('+(1.8-0.8*p)+')';}
  };
  const ts=[...ls.map(x=>x[1]), S.total?S.total.t||0:0, S.sello?S.sello.t:0]; window.FIN=Math.max(...ts)+1;
}

if(S.tipo==='barra'){
  const c=$('<div class="center" style="gap:34px"></div>');
  const h=$('<h1 class="big" style="font-size:96px">'+esc(S.titulo).replace(/\\*(.+?)\\*/g,'<span class="amber">$1</span>')+'</h1>');
  const bw=$('<div class="barwrap"></div>'); const lw=$('<div class="leyendas"></div>');
  const segs=S.segmentos.map(s=>{const el=$('<div class="seg"></div>'); el.style.background=s.color; el.textContent=s.pct+' %'; if(s.oscuro)el.style.color='#FBFAF6'; bw.append(el);
    const ly=$('<div class="ley"></div>'); ly.style.width=(s.pct/100*1560)+'px'; ly.innerHTML='<b style="color:'+s.color+'">'+esc(s.label)+'</b><br>'+esc(s.valor||''); lw.append(ly); return [el,ly,s];});
  c.append(h); c.append(bw); c.append(lw); document.body.append(c);
  pintar=(t)=>{ fade(h,P(t,0,.6)); segs.forEach(([el,ly,s])=>{const p=P(t,s.t||0,.8); el.style.width=(p*s.pct/100*1560)+'px'; ly.style.opacity=P(t,(s.t||0)+.4,.5);}); };
  window.FIN=Math.max(...S.segmentos.map(s=>(s.t||0)))+1.4;
}

if(S.tipo==='curvas'){
  const c=$('<div class="left" style="gap:10px"></div>');
  const h=$('<h1 class="big" style="font-size:84px">'+esc(S.titulo||'').replace(/\\*(.+?)\\*/g,'<span class="amber">$1</span>')+'</h1>');
  const NS='http://www.w3.org/2000/svg';
  const svg=document.createElementNS(NS,'svg'); svg.setAttribute('width','1640'); svg.setAttribute('height','640'); svg.setAttribute('viewBox','-60 50 1520 530');
  const A='M0 480 L300 480 L380 200 L780 200 L860 480 L1400 480';
  const B='M0 490 L300 490 L392 212 L790 212 L960 222 L1150 400 L1300 490 L1400 490';
  const AREA='M790 212 L860 480 L1300 480 L1300 490 L1150 400 L960 222 Z';
  const mk=(tag,attrs)=>{const e=document.createElementNS(NS,tag); for(const k in attrs)e.setAttribute(k,attrs[k]); svg.append(e); return e;};
  for(let w=0;w<=8;w++){ mk('line',{x1:w*175,y1:140,x2:w*175,y2:520,stroke:'rgba(251,250,246,.08)','stroke-width':2});
    if(w<8){const tx=mk('text',{x:w*175+87,y:560,fill:'#8A93A0','font-size':24,'text-anchor':'middle','font-family':'JetBrains Mono'}); tx.textContent='Sem. '+(w+1);} }
  const area=mk('path',{d:AREA,fill:'rgba(224,82,27,.35)'});
  const pa=mk('path',{d:A,fill:'none',stroke:'#8A93A0','stroke-width':8,'stroke-linejoin':'round'});
  const pb=mk('path',{d:B,fill:'none',stroke:'#F5B301','stroke-width':10,'stroke-linejoin':'round'});
  const la=mk('text',{x:1400,y:92,'text-anchor':'end',fill:'#8A93A0','font-size':28,'font-family':'JetBrains Mono','font-weight':700}); la.textContent=S.a||'Precio internacional';
  const lb=mk('text',{x:1400,y:130,'text-anchor':'end',fill:'#F5B301','font-size':28,'font-family':'JetBrains Mono','font-weight':700}); lb.textContent=S.b||'Precio en el surtidor';
  const t1=mk('text',{x:330,y:160,fill:'#FBFAF6','font-size':34,'font-family':'Big Shoulders Display','font-weight':900}); t1.textContent='SUBE COMO UN COHETE';
  const t2=mk('text',{x:900,y:170,fill:'#FBFAF6','font-size':34,'font-family':'Big Shoulders Display','font-weight':900}); t2.textContent='BAJA COMO UNA PLUMA';
  const t3=mk('text',{x:880,y:450,fill:'#E0521B','font-size':30,'font-family':'JetBrains Mono','font-weight':700}); t3.textContent=S.area||'Pagas de más';
  c.append(h); c.append(svg); document.body.append(c);
  const LA=pa.getTotalLength(), LB=pb.getTotalLength();
  [[pa,LA],[pb,LB]].forEach(([p,L])=>{p.style.strokeDasharray=L;});
  const T=S.ritmo||1;
  pintar=(t)=>{ fade(h,P(t,0,.6)); const pr=P(t,.4*T,3.2*T); pa.style.strokeDashoffset=LA*(1-pr); pb.style.strokeDashoffset=LB*(1-P(t,.6*T,3.4*T));
    la.style.opacity=P(t,.8*T,.5); lb.style.opacity=P(t,1*T,.5); t1.style.opacity=P(t,1.2*T,.5); t2.style.opacity=P(t,2.8*T,.5);
    area.style.opacity=P(t,4*T,.8); t3.style.opacity=P(t,4.4*T,.6); };
  window.FIN=5.2*T;
}

if(S.tipo==='lista'){
  const c=$('<div class="left" style="gap:44px"></div>');
  const h=$('<h1 class="big" style="font-size:96px">'+esc(S.titulo).replace(/\\*(.+?)\\*/g,'<span class="amber">$1</span>')+'</h1>'); c.append(h);
  const its=S.items.map((x,i)=>{const el=$('<div class="item"><div class="num"></div><div></div></div>'); el.children[0].textContent=i+1; el.children[1].textContent=x;
    const act=(S.activo===undefined||S.activo<0)?true:S.activo===i; el.style.color=act?(S.activo>=0?'#F5B301':'#FBFAF6'):'rgba(251,250,246,.28)'; c.append(el); return el;});
  document.body.append(c);
  pintar=(t)=>{ fade(h,P(t,0,.5)); its.forEach((el,i)=>{const p=P(t,.3+i*(S.paso||.35),.5); el.style.opacity=p; el.style.transform='translateX('+((1-p)*-40)+'px)';}); };
  window.FIN=.3+S.items.length*(S.paso||.35)+.6;
}

if(S.tipo==='comparacion'){
  const c=$('<div class="left" style="gap:46px"></div>');
  const h=$('<h1 class="big" style="font-size:92px">'+esc(S.titulo).replace(/\\*(.+?)\\*/g,'<span class="amber">$1</span>')+'</h1>');
  const row=$('<div style="display:flex;gap:50px"></div>');
  const mkp=(d,hl)=>{const p=$('<div class="panel'+(hl?' hl':'')+'"><div class="pe"></div><div class="pv"></div><div class="pn"></div></div>');
    p.children[0].textContent=d.etiqueta; p.children[1].textContent=d.valor; p.children[1].style.color=hl?'#E0521B':'#F5B301'; p.children[2].textContent=d.nota||''; return p;};
  const a=mkp(S.izq,false), b=mkp(S.der,S.resaltar!=='izq'); row.append(a); row.append(b); c.append(h); c.append(row); document.body.append(c);
  pintar=(t)=>{ fade(h,P(t,0,.5)); fade(a,P(t,.4,.6),50); fade(b,P(t,1.1,.6),50); };
  window.FIN=2;
}

if(S.tipo==='idea'){
  const c=$('<div class="left"></div>'); const box=$('<div style="border-left:14px solid #F5B301;padding-left:48px;display:flex;flex-direction:column;gap:30px"></div>');
  const e=S.eyebrow?$('<div class="eyebrow">'+esc(S.eyebrow)+'</div>'):null;
  const tx=$('<div style="font-size:64px;font-weight:700;line-height:1.3;max-width:1450px"></div>');
  const words=String(S.texto).split(' ').map(w=>{const s=document.createElement('span'); s.textContent=w+' '; tx.append(s); return s;});
  [e,tx].forEach(x=>x&&box.append(x)); c.append(box); document.body.append(c);
  pintar=(t)=>{ if(e)fade(e,P(t,0,.5)); words.forEach((s,i)=>{s.style.opacity=.15+.85*P(t,.3+i*.06,.3);}); };
  window.FIN=.3+words.length*.06+.5;
}

if(S.tipo==='final'){
  const c=$('<div class="center" style="gap:34px"></div>');
  const img=$('<img src="${LOGO}" style="width:300px;height:300px;border-radius:50%">');
  const h=$('<h1 class="big" style="font-size:170px">Ticket <span class="amber">Medio</span></h1>');
  const s=$('<div style="font-size:40px;color:#C9CDD3">'+esc(S.texto||'Cada semana, abrimos el ticket de algo que pagas todos los días.')+'</div>');
  c.append(img); c.append(h); c.append(s); document.body.append(c);
  pintar=(t)=>{ const p=P(t,0,.7); img.style.opacity=p; img.style.transform='scale('+(0.7+0.3*p)+') rotate('+((1-p)*-20)+'deg)'; fade(h,P(t,.4,.6),40); fade(s,P(t,.9,.6)); };
  window.FIN=2;
}
window.pintar=pintar;
`;

function html(spec) {
  return `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800;900&family=JetBrains+Mono:wght@500;700&display=swap">
<style>${CSS}</style></head><body>
<script>window.SPEC=${JSON.stringify(spec).replace(/</g, '\\u003c')};</script>
<script>document.fonts.ready.then(()=>{${MOTOR}; window.LISTO=true;});</script>
</body></html>`;
}

async function main() {
  const [, , specPath, outDir, ...solo] = process.argv;
  if (!specPath || !outDir) { console.log('Uso: node graficos.js graficos.json CARPETA_SALIDA [ids]'); process.exit(1); }
  const tarjetas = JSON.parse(fs.readFileSync(specPath, 'utf8'));
  fs.mkdirSync(outDir, { recursive: true });
  const FF = ffmpegPath();
  const browser = await puppeteer.launch({ executablePath: EDGE, headless: 'shell', userDataDir: fs.mkdtempSync(path.join(os.tmpdir(), 'tm_edge_')), args: ['--hide-scrollbars', '--allow-file-access-from-files', '--no-first-run', '--disable-extensions'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  const tmp = path.join(os.tmpdir(), 'tm_grafico.html');
  for (const spec of tarjetas) {
    if (solo.length && !solo.includes(spec.id)) continue;
    const salida = path.join(outDir, `g_${spec.id}.mp4`);
    fs.writeFileSync(tmp, html(spec), 'utf8');
    await page.goto('file:///' + tmp.replace(/\\/g, '/'), { waitUntil: 'networkidle0' });
    await page.waitForFunction('window.LISTO===true', { timeout: 20000 });
    const fin = await page.evaluate('window.FIN');
    const dur = spec.duracion || Math.max(fin + 1.5, 4);
    const n = Math.round(dur * FPS);
    const ff = spawn(FF, ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
      '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-pix_fmt', 'yuv420p', '-r', String(FPS), salida]);
    let ultimo = null;
    for (let i = 0; i < n; i++) {
      const t = i / FPS;
      if (t <= fin + 0.1 || !ultimo) {
        await page.evaluate((tt) => window.pintar(tt), t);
        ultimo = await page.screenshot({ type: 'jpeg', quality: 92 });
      }
      if (!ff.stdin.write(ultimo)) await new Promise((r) => ff.stdin.once('drain', r));
    }
    ff.stdin.end();
    await new Promise((r) => ff.on('close', r));
    console.log(`✓ g_${spec.id}.mp4 (${dur.toFixed(1)} s)`);
  }
  await browser.close();
}

main().catch((e) => { console.error(e); process.exit(1); });
