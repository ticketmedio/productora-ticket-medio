// Motor de escenas ilustradas de Ticket Medio (desde el vídeo 2).
// La mascota se mueve por escenarios dibujados; textos, cifras, monedas y flechas aparecen
// sincronizados con la locución (se anclan a frases del SRT con "en": "trozo de frase").
//
// Uso: node herramientas/escenas.js CARPETA_VIDEO [id1 id2 ...]
//   Lee CARPETA_VIDEO/escenas_v2.json y CARPETA_VIDEO/audio/subtitulos.srt
//   Escribe CARPETA_VIDEO/clips/s_ID.mp4 y CARPETA_VIDEO/montaje.json (para montaje.py)
//
// escenas_v2.json:
// { "musica": "...", "cola": 3,
//   "escenas": [ { "id": "01", "desde": "frase con la que empieza", "fondo": "super_pasillo" | "#F4E9D0",
//                  "zoom": [1, 1.06], "capas": [ {tipo, ...}, ... ] } ] }
// Tiempos de cada capa: "t" (segundos desde el inicio de la escena) o "en" (trozo de una frase del SRT).
// Tipos: mascota, texto, cifra, moneda, flecha, rect, sello, bocadillo, tarta, hud, imagen.
const fs = require('fs');
const path = require('path');
const os = require('os');
const { spawn, execFileSync } = require('child_process');
const puppeteer = require('puppeteer-core');

const FPS = 30;
const RAIZ = path.join(__dirname, '..');

function navegador() {
  const base = path.join(__dirname, 'navegador', 'chrome-headless-shell');
  if (process.platform === 'win32' && fs.existsSync(base)) {
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
const FF = ffmpegPath();
const FFPROBE = FF.replace(/ffmpeg(\.exe)?$/i, 'ffprobe$1');
const url = (p) => (p.startsWith('/') ? 'file://' : 'file:///') + p.replace(/\\/g, '/');

// ---------- SRT y anclajes ----------
function leerSRT(ruta) {
  const aSeg = (s) => { const [h, m, r] = s.split(':'); const [sec, ms] = r.split(','); return +h * 3600 + +m * 60 + +sec + +ms / 1000; };
  return fs.readFileSync(ruta, 'utf8').trim().split(/\r?\n\r?\n/).map((b) => {
    const l = b.split(/\r?\n/); const [a, z] = l[1].split(' --> ');
    return { ini: aSeg(a.trim()), fin: aSeg(z.trim()), texto: l.slice(2).join(' ') };
  });
}
const norm = (s) => s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9ñ ]/g, ' ').replace(/\s+/g, ' ').trim();
function buscar(srt, trozo, desde = 0) {
  const n = norm(trozo);
  for (const f of srt) {
    if (f.fin < desde - 0.01) continue;
    const nf = norm(f.texto); const i = nf.indexOf(n);
    if (i >= 0) {
      // interpolación dentro de la frase según la posición del trozo
      return f.ini + (f.fin - f.ini) * (i / Math.max(nf.length, 1));
    }
  }
  throw new Error('No encuentro en el SRT: «' + trozo + '»');
}

// ---------- página ----------
const CSS = `
*{box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#F4E9D0}
#fondo{position:absolute;inset:-40px;background-size:cover;background-position:center;transform-origin:50% 55%}
#velo{position:absolute;inset:0;background:rgba(255,251,240,.36)}
#capas{position:absolute;inset:0}
.abs{position:absolute;will-change:transform,opacity}
.mano{font-family:"Patrick Hand","Comic Sans MS",cursive}
.marker{font-family:"Permanent Marker","Patrick Hand",cursive}
.papel{background:#FFFDF6;border:5px solid #1b1b1b;border-radius:14px 22px 12px 18px;padding:14px 26px;box-shadow:6px 8px 0 rgba(0,0,0,.18)}
.sombra{filter:drop-shadow(0 14px 10px rgba(0,0,0,.22))}
.contorno{text-shadow:-4px -4px 0 #FFFDF6,4px -4px 0 #FFFDF6,-4px 4px 0 #FFFDF6,4px 4px 0 #FFFDF6,0 -5px 0 #FFFDF6,0 5px 0 #FFFDF6,-5px 0 0 #FFFDF6,5px 0 0 #FFFDF6,6px 9px 0 rgba(0,0,0,.25)}
.stripe{position:absolute;left:0;right:0;bottom:0;height:12px;background:repeating-linear-gradient(-45deg,#F5B301 0 18px,#1b1b1b 18px 36px);z-index:50}
.marca{position:absolute;right:38px;top:30px;z-index:50;font-family:"Permanent Marker",cursive;font-size:26px;color:#1b1b1b;background:#F5B301;padding:4px 14px;border:3px solid #1b1b1b;border-radius:8px;transform:rotate(2deg)}
.fuente{position:absolute;left:36px;bottom:24px;z-index:50;font-family:"Patrick Hand",cursive;font-size:24px;color:#1b1b1b;background:rgba(255,253,246,.85);padding:2px 12px;border-radius:6px}
`;

const MOTOR = `
const S=window.SPEC; const W=S.W||1920,H=S.H||1080;
const cl=(x)=>Math.max(0,Math.min(1,x)); const ease=(x)=>1-Math.pow(1-cl(x),3);
const easeIO=(x)=>{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;};
const back=(x)=>{x=cl(x);const c1=1.9,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
const P=(t,a,d)=>ease((t-a)/(d||.5));
const esc=(s)=>String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/\\n/g,'<br>');
const fmt=(n,dec)=>n.toLocaleString('es-ES',{minimumFractionDigits:dec||0,maximumFractionDigits:dec||0,useGrouping:'always'});
const $=(h)=>{const d=document.createElement('div');d.innerHTML=h.trim();return d.firstChild;};
const capas=document.getElementById('capas'); const fondo=document.getElementById('fondo');
const NS='http://www.w3.org/2000/svg';
// filtro "dibujado a mano" con temblor (boil)
const defs=document.createElementNS(NS,'svg'); defs.setAttribute('width',0); defs.setAttribute('height',0); defs.style.position='absolute';
defs.innerHTML='<filter id="rough"><feTurbulence id="turb" type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="1"/><feDisplacementMap in="SourceGraphic" scale="4"/></filter>';
document.body.append(defs); const turb=document.getElementById('turb');
if(S.fondo_img){fondo.style.backgroundImage='url("'+S.fondo_img+'")';} else {document.getElementById('velo').style.display='none';} if(!S.fondo_img){fondo.style.background=S.fondo_color||'#F4E9D0';}
if(!S.sin_marca) document.body.append($('<div class="marca">TICKET MEDIO</div>'));
document.body.append($('<div class="stripe"></div>'));
if(S.fuente) document.body.append($('<div class="fuente">Fuente: '+esc(S.fuente)+'</div>'));
const fns=[];
const Z=S.zoom||[1,1.05];

function mascota(c){
  const el=$('<div class="abs sombra"></div>'); const img=document.createElement('img'); el.append(img);
  const h=c.h||520; img.style.height=h+'px'; img.style.display='block';
  const poses=[{t:-1,pose:c.pose||'normal'}].concat(c.poses||[]).sort((a,b)=>a.t-b.t);
  const pre={}; poses.forEach(p=>{if(!pre[p.pose]){const i=new Image();i.src=S.MASC+p.pose+'.png';pre[p.pose]=i;}});
  capas.append(el);
  const ent=c.entra||'pop', t0=c.t||0, sal=c.sale;
  const movs=(c.camina||[]).slice().sort((a,b)=>a.t-b.t);
  return (t)=>{
    let pose=poses[0].pose, tp=-9; for(const p of poses){ if(t>=p.t){pose=p.pose;tp=p.t;} }
    if(img.dataset.p!==pose){img.src=S.MASC+pose+'.png'; img.dataset.p=pose;}
    // posición base (con caminatas)
    let x=c.x, y=c.y; let andando=false;
    for(const m of movs){ const k=easeIO((t-m.t)/(m.dur||1.2)); if(t>=m.t){ const x0=x; x=x0+(m.x-x0)*k; if(m.y!==undefined){y=y+(m.y-y)*k;} if(k<1)andando=true; } }
    let op=1, dx=0, dy=0, sc=1;
    const k=(t-t0)/0.7;
    if(t<t0){op=0;}
    else if(ent==='izq'){dx=-(1-easeIO(k))*(x+400); andando=andando||k<1;}
    else if(ent==='der'){dx=(1-easeIO(k))*(W-x+400); andando=andando||k<1;}
    else if(ent==='abajo'){dy=(1-back(k))*700;}
    else {sc=k<1?back(k):1; op=cl(k*3);}
    if(sal&&t>=sal.t){ const q=easeIO((t-sal.t)/0.7); if(sal.hacia==='izq')dx-=q*(x+400); else if(sal.hacia==='der')dx+=q*(W-x+400); else {op*=1-q; sc*=1-q*.3;} andando=andando||q<1; }
    // cambio de pose: pequeño bote
    const kp=(t-tp)/0.35; const pop=kp>=0&&kp<1?1+Math.sin(kp*Math.PI)*0.06:1;
    // respiración / paso
    const f=andando?3.2:0.9; const bob=Math.abs(Math.sin(t*Math.PI*f))*(andando?16:0)+Math.sin(t*Math.PI*2*0.45)*(andando?0:5);
    const rot=andando?Math.sin(t*Math.PI*f)*4:Math.sin(t*Math.PI*2*0.3)*1.2;
    const flip=c.mira==='izq'?-1:1;
    el.style.opacity=op;
    el.style.left=(x+dx)+'px'; el.style.top=(y+dy-bob)+'px';
    el.style.transform='translate(-50%,-100%) rotate('+rot+'deg) scale('+(sc*pop*flip)+','+(sc*pop)+')';
    el.style.transformOrigin='50% 100%';
  };
}

function aparece(el,c,modo){
  const t0=c.t||0, d=c.dur_entrada||0.5, fin=c.fin;
  return (t)=>{
    const k=(t-t0)/d; let op=cl(k*2), tr='';
    if(modo==='pop'){ tr='scale('+(t<t0?0:(k<1?back(k):1))+')'; }
    else if(modo==='sube'){ tr='translateY('+((1-ease(k))*40)+'px)'; }
    if(fin!==undefined&&t>=fin){ const q=cl((t-fin)/0.35); op*=1-q; }
    el.style.opacity=t<t0?0:op; el.style.transform=(el.dataset.base||'')+' '+tr;
  };
}

function texto(c){
  const cls=(c.fuente==='mano'?'mano':'marker')+(c.papel?' papel':' contorno');
  const el=$('<div class="abs '+cls+'"></div>');
  el.innerHTML=esc(c.texto).replace(/\\*(.+?)\\*/g,'<span style="color:'+(c.acento||'#E0521B')+'">$1</span>');
  Object.assign(el.style,{left:c.x+'px',top:c.y+'px',fontSize:(c.tam||64)+'px',color:c.color||'#1b1b1b',lineHeight:1.1,textAlign:c.align||'center',width:c.ancho?c.ancho+'px':'auto',whiteSpace:c.ancho?'normal':'nowrap'});
  if(c.borde) el.style.webkitTextStroke=c.borde;
  el.dataset.base=(c.ancla==='izq'?'translate(0,-50%)':'translate(-50%,-50%)')+' rotate('+(c.rot||0)+'deg)';
  capas.append(el);
  const t0=c.t||0, d=c.dur||Math.min(1.2,0.25+String(c.texto).length*0.03);
  const ap=aparece(el,c,c.anim==='pop'?'pop':'nada');
  return (t)=>{ ap(t); if(c.anim!=='pop'){ const k=cl((t-t0)/d); el.style.clipPath='inset(-20% '+((1-k)*100)+'% -20% -5%)'; } };
}

function cifra(c){
  const el=$('<div class="abs marker contorno"></div>');
  Object.assign(el.style,{left:c.x+'px',top:c.y+'px',fontSize:(c.tam||150)+'px',color:c.color||'#1b1b1b',whiteSpace:'nowrap'});
  if(c.borde!==false) el.style.webkitTextStroke=c.borde||'0px';
  el.dataset.base='translate(-50%,-50%) rotate('+(c.rot||-2)+'deg)';
  capas.append(el); const ap=aparece(el,c,'pop'); const t0=c.t||0;
  return (t)=>{ ap(t); const k=P(t,t0,c.dur||1.3); const v=(c.desde||0)+(c.hasta-(c.desde||0))*k;
    el.innerHTML='<span style="font-size:.55em">'+esc(c.prefijo||'')+'</span>'+fmt(v,c.dec)+'<span style="font-size:.5em">'+esc(c.sufijo||'')+'</span>'; };
}

function monedaSVG(r,txt,color,fuente){
  const col=color||'#F5B301';
  return '<svg width="'+(2*r+12)+'" height="'+(2*r+12)+'" viewBox="-6 -6 '+(2*r+12)+' '+(2*r+12)+'" style="filter:url(#rough);overflow:visible">'+
   '<circle cx="'+r+'" cy="'+r+'" r="'+r+'" fill="'+col+'" stroke="#1b1b1b" stroke-width="6"/>'+
   '<circle cx="'+r+'" cy="'+r+'" r="'+(r*.78)+'" fill="none" stroke="#1b1b1b" stroke-width="3" stroke-dasharray="4 7" opacity=".5"/>'+
   '<text x="'+r+'" y="'+(r+r*.2)+'" text-anchor="middle" font-family="'+(fuente||'Permanent Marker')+'" font-weight="bold" font-size="'+(r*(String(txt).length>3?0.55:0.75))+'" fill="#1b1b1b">'+esc(txt)+'</text></svg>';
}
function moneda(c){
  const r=c.r||70; const el=$('<div class="abs sombra">'+monedaSVG(r,c.texto||'€',c.color)+'</div>');
  capas.append(el); const t0=c.t||0; const v=c.vuela;
  return (t)=>{
    let x=c.x,y=c.y,sc=t<t0?0:back((t-t0)/0.45),op=t<t0?0:1,rot=Math.sin(t*2)*6;
    if(v&&t>=v.t){ const k=easeIO((t-v.t)/(v.dur||1)); x=c.x+(v.x-c.x)*k; y=c.y+(v.y-c.y)*k-Math.sin(k*Math.PI)*(v.arco||160); rot+=k*360*(v.vueltas||1); if(v.desaparece&&k>=1){op=0;} if(v.escala!==undefined)sc*=1+(v.escala-1)*k; }
    if(c.fin!==undefined&&t>=c.fin){op*=1-cl((t-c.fin)/.35);}
    el.style.opacity=op; el.style.left=x+'px'; el.style.top=y+'px'; el.style.transform='translate(-50%,-50%) rotate('+rot+'deg) scale('+sc+')';
  };
}

function flecha(c){
  const [x1,y1]=c.de,[x2,y2]=c.a; const cu=c.curva===undefined?-120:c.curva;
  const mx=(x1+x2)/2+(y2-y1)*cu/600, my=(y1+y2)/2-(x2-x1)*cu/600;
  const svg=document.createElementNS(NS,'svg'); svg.setAttribute('width',W); svg.setAttribute('height',H); svg.style.position='absolute'; svg.style.left=0; svg.style.top=0; svg.style.filter='url(#rough)';
  const col=c.color||'#E0521B', g=c.grosor||9;
  const p=document.createElementNS(NS,'path'); p.setAttribute('d','M'+x1+' '+y1+' Q'+mx+' '+my+' '+x2+' '+y2);
  Object.entries({fill:'none',stroke:col,'stroke-width':g,'stroke-linecap':'round'}).forEach(([k,v])=>p.setAttribute(k,v));
  const ang=Math.atan2(y2-my,x2-mx), L=g*3.6;
  const head=document.createElementNS(NS,'path');
  head.setAttribute('d','M'+(x2-L*Math.cos(ang-.5))+' '+(y2-L*Math.sin(ang-.5))+' L'+x2+' '+y2+' L'+(x2-L*Math.cos(ang+.5))+' '+(y2-L*Math.sin(ang+.5)));
  Object.entries({fill:'none',stroke:col,'stroke-width':g,'stroke-linecap':'round','stroke-linejoin':'round'}).forEach(([k,v])=>head.setAttribute(k,v));
  svg.append(p,head); capas.append(svg); const len=p.getTotalLength(); p.style.strokeDasharray=len;
  const t0=c.t||0,d=c.dur||0.7;
  return (t)=>{ const k=ease((t-t0)/d); p.style.strokeDashoffset=len*(1-k); head.style.opacity=k>0.95?1:0; svg.style.opacity=t<t0?0:(c.fin!==undefined&&t>=c.fin?1-cl((t-c.fin)/.35):1); };
}

function rect(c){
  const el=$('<div class="abs"></div>');
  Object.assign(el.style,{left:c.x+'px',top:c.y+'px',width:c.w+'px',height:c.h+'px',background:c.color||'#F5B301',border:'5px solid #1b1b1b',borderRadius:'10px 16px 8px 14px',transformOrigin:c.crece==='arriba'?'50% 100%':'0 50%',filter:'url(#rough)'});
  if(c.texto){el.innerHTML='<div class="marker" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:'+(c.tam||44)+'px;color:#1b1b1b;white-space:nowrap">'+esc(c.texto)+'</div>';}
  capas.append(el); const t0=c.t||0;
  return (t)=>{ const k=ease((t-t0)/(c.dur||0.9)); el.style.opacity=t<t0?0:1; el.style.transform=c.crece==='arriba'?'scaleY('+k+')':'scaleX('+k+')';
    if(c.fin!==undefined&&t>=c.fin) el.style.opacity=1-cl((t-c.fin)/.35); };
}

function sello(c){
  const el=$('<div class="abs marker"></div>'); el.textContent=c.texto;
  Object.assign(el.style,{left:c.x+'px',top:c.y+'px',fontSize:(c.tam||80)+'px',color:c.color||'#E0521B',border:'8px solid '+(c.color||'#E0521B'),padding:'4px 26px',borderRadius:'12px',background:'rgba(255,253,246,.85)',whiteSpace:'nowrap'});
  capas.append(el); const t0=c.t||0;
  return (t)=>{ const k=(t-t0)/0.35; const s=t<t0?3:(k<1?3-2*ease(k):1); el.style.opacity=t<t0?0:cl(k*2); el.style.transform='translate(-50%,-50%) rotate('+(c.rot||-8)+'deg) scale('+s+')';
    if(c.fin!==undefined&&t>=c.fin) el.style.opacity=1-cl((t-c.fin)/.35); };
}

function bocadillo(c){
  const piensa=c.piensa;
  const el=$('<div class="abs papel mano"></div>');
  el.innerHTML=esc(c.texto).replace(/\\*(.+?)\\*/g,'<b style="color:#E0521B">$1</b>');
  Object.assign(el.style,{left:c.x+'px',top:c.y+'px',fontSize:(c.tam||46)+'px',maxWidth:(c.ancho||620)+'px',borderRadius:piensa?'60px':'28px',lineHeight:1.2,textAlign:'center'});
  const cola=$('<div style="position:absolute;width:0;height:0;border:22px solid transparent;border-top:34px solid #1b1b1b;bottom:-56px;left:'+(c.cola||30)+'%"></div>');
  if(!piensa) el.append(cola);
  el.dataset.base='translate(-50%,-50%)'; capas.append(el); return aparece(el,c,'pop');
}

function tarta(c){
  // una moneda de 1 € que se reparte en porciones (céntimos)
  const r=c.r||260, cx=c.x, cy=c.y;
  const svg=document.createElementNS(NS,'svg'); svg.setAttribute('width',W); svg.setAttribute('height',H); svg.style.position='absolute'; svg.style.left=0; svg.style.top=0; svg.style.filter='url(#rough)';
  const base=document.createElementNS(NS,'circle'); Object.entries({cx,cy,r,fill:'#FFF3C4',stroke:'#1b1b1b','stroke-width':8}).forEach(([k,v])=>base.setAttribute(k,v)); svg.append(base);
  let a0=-Math.PI/2; const ps=[];
  for(const p of c.porciones){
    const a1=a0+p.v/100*2*Math.PI; const g=document.createElementNS(NS,'g');
    const d='M'+cx+' '+cy+' L'+(cx+r*Math.cos(a0))+' '+(cy+r*Math.sin(a0))+' A'+r+' '+r+' 0 '+(a1-a0>Math.PI?1:0)+' 1 '+(cx+r*Math.cos(a1))+' '+(cy+r*Math.sin(a1))+' Z';
    const path=document.createElementNS(NS,'path'); Object.entries({d,fill:p.color,stroke:'#1b1b1b','stroke-width':6,'stroke-linejoin':'round'}).forEach(([k,v])=>path.setAttribute(k,v));
    g.append(path); svg.append(g);
    const am=(a0+a1)/2; ps.push({g,am,t:p.t,sale:p.sale}); a0=a1;
  }
  capas.append(svg);
  const labs=c.porciones.map((p,i)=>{ if(!p.etiqueta) return null; const am=ps[i].am; const lr=r+(p.dist||120);
    const el=$('<div class="abs marker"></div>'); el.innerHTML=esc(p.etiqueta);
    Object.assign(el.style,{left:(p.lx!==undefined?p.lx:cx+lr*Math.cos(am))+'px',top:(p.ly!==undefined?p.ly:cy+lr*Math.sin(am))+'px',fontSize:(p.tam||44)+'px',color:'#1b1b1b',whiteSpace:'nowrap',textAlign:'center'});
    el.dataset.base='translate(-50%,-50%)'; capas.append(el); return aparece(el,{t:p.t},'pop'); });
  const t0=c.t||0;
  return (t)=>{ svg.style.opacity=t<t0?0:1; base.setAttribute('r',r*back((t-t0)/.5));
    ps.forEach(p=>{ const k=back((t-p.t)/.45); let s=t<p.t?0:k; let tx=0,ty=0;
      if(p.sale!==undefined&&t>=p.sale){ const q=easeIO((t-p.sale)/.6); tx=Math.cos(p.am)*q*60; ty=Math.sin(p.am)*q*60; }
      p.g.setAttribute('transform','translate('+(cx+tx)+' '+(cy+ty)+') scale('+s+') translate('+(-cx)+' '+(-cy)+')'); });
    labs.forEach(f=>f&&f(t)); };
}

function hud(c){
  // contador fijo: «Te quedan: 91 c»
  const el=$('<div class="abs papel marker" style="display:flex;align-items:center;gap:18px;z-index:40"></div>');
  el.innerHTML=monedaSVG(40,'€','#F5B301','Patrick Hand')+'<span class="lab" style="font-size:40px">'+esc(c.etiqueta||'Tu euro')+':</span><span class="v" style="font-size:56px;color:#E0521B"></span>';
  Object.assign(el.style,{left:(c.x||60)+'px',top:(c.y||40)+'px'}); capas.append(el);
  const v=el.querySelector('.v'); const cambios=[{t:-1,valor:c.valor}].concat(c.cambios||[]).sort((a,b)=>a.t-b.t);
  return (t)=>{ let a=cambios[0].valor,b=a,tc=-9; for(const k of cambios){ if(t>=k.t){a=b;b=k.valor;tc=k.t;} }
    const q=P(t,tc,.8); const val=a+(b-a)*q; v.textContent=fmt(val,val%1&&q<1?1:(String(b).includes('.')?1:0))+' c';
    const pul=t-tc<.4&&t>=tc?1+Math.sin((t-tc)/.4*Math.PI)*.12:1; el.style.transform='scale('+pul+')'; el.style.transformOrigin='0 50%'; };
}

function imagen(c){
  const el=$('<div class="abs '+(c.sombra===false?'':'sombra')+'"><img style="height:'+(c.h||300)+'px;display:block"></div>');
  el.querySelector('img').src=c.src; el.dataset.base='translate(-50%,-50%) rotate('+(c.rot||0)+'deg)';
  Object.assign(el.style,{left:c.x+'px',top:c.y+'px'}); capas.append(el); return aparece(el,c,c.anim||'pop');
}

function panel(c){
  const el=$('<div class="abs"></div>');
  Object.assign(el.style,{left:c.x+'px',top:c.y+'px',width:c.w+'px',height:c.h+'px',background:'rgba(255,253,246,'+(c.opacidad||.9)+')',border:'6px solid #1b1b1b',borderRadius:'26px 38px 22px 34px',boxShadow:'10px 12px 0 rgba(0,0,0,.18)',filter:'url(#rough)'});
  capas.append(el); const t0=c.t||0;
  return (t)=>{ const k=ease((t-t0)/.4); el.style.opacity=t<t0?0:k; el.style.transform='scale('+(0.96+0.04*k)+')'; };
}
const TIPOS={panel,mascota,texto,cifra,moneda,flecha,rect,sello,bocadillo,tarta,hud,imagen};
for(const c of S.capas){ if(!TIPOS[c.tipo]) throw new Error('tipo desconocido '+c.tipo); fns.push(TIPOS[c.tipo](c)); }
window.pintar=(t)=>{
  turb.setAttribute('seed',1+Math.floor(t*8)%5);   // temblor de dibujo a 8 fps
  const k=cl(t/S.DUR); const z=Z[0]+(Z[1]-Z[0])*k;
  fondo.style.transform='scale('+z+') translate('+((S.pan||0)*k)+'px,0)';
  fns.forEach(f=>f(t));
};
window.LISTO=true;
`;

function html(spec) {
  return `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Permanent+Marker&family=Patrick+Hand&display=swap">
<style>${CSS}
html,body{width:${spec.W}px;height:${spec.H}px}</style></head><body><div id="fondo"></div><div id="velo"></div><div id="capas"></div>
<script>window.SPEC=${JSON.stringify(spec)};</script>
<script>document.fonts.load('40px "Permanent Marker"').then(()=>document.fonts.load('40px "Patrick Hand"')).then(()=>document.fonts.ready).then(()=>{${MOTOR}}).catch(e=>{window.ERROR=String(e);});</script>
</body></html>`;
}

function duracionAudio(ruta) {
  return parseFloat(execFileSync(FFPROBE, ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', ruta]).toString());
}

async function main() {
  const dir = path.resolve(process.argv[2]);
  const solo = process.argv.slice(3);
  const cfg = JSON.parse(fs.readFileSync(path.join(dir, 'escenas_v2.json'), 'utf8'));
  const srt = leerSRT(path.join(dir, 'audio', 'subtitulos.srt'));
  const total = duracionAudio(path.join(dir, 'audio', 'voz.mp3')) + (cfg.cola || 3);
  // inicio de cada escena
  let prev = 0;
  cfg.escenas.forEach((e, i) => { e._ini = i === 0 ? 0 : buscar(srt, e.desde, prev) - (e.adelanto ?? 0.15); prev = e._ini; });
  cfg.escenas.forEach((e, i) => { e._dur = (i + 1 < cfg.escenas.length ? cfg.escenas[i + 1]._ini : total) - e._ini; });
  const clips = path.join(dir, 'clips'); fs.mkdirSync(clips, { recursive: true });
  const MASC = url(path.join(RAIZ, 'youtube', 'marca', 'mascota', 'recortes')) + '/';

  if (process.env.SOLO_COMPROBAR) { for (const e of cfg.escenas) { const T = (c) => (c.en !== undefined ? buscar(srt, c.en, e._ini - 0.5) - e._ini : (c.t || 0)); for (const c of e.capas || []) { const t = T(c); const fin = typeof c.fin === 'string' ? T({ en: c.fin }) : e._dur; if (c.tipo !== 'panel' && c.tipo !== 'hud' && fin - t < 1.5) console.warn(`⚠ escena ${e.id}: «${c.texto || c.tipo}» solo se ve ${(fin - t).toFixed(1)} s`); } } return; }
  const browser = await puppeteer.launch({ executablePath: navegador(), headless: 'shell', userDataDir: fs.mkdtempSync(path.join(os.tmpdir(), 'tm_esc_')),
    args: ['--hide-scrollbars', '--allow-file-access-from-files', '--no-first-run', '--disable-extensions'] });
  const page = await browser.newPage();
  page.on('pageerror', (e) => console.error('Error en la página:', e.message));
  const VERT = cfg.formato === 'vertical'; const ANCHO = VERT ? 1080 : 1920, ALTO = VERT ? 1920 : 1080;
  await page.setViewport({ width: ANCHO, height: ALTO, deviceScaleFactor: 1 });
  const tmp = path.join(dir, 'clips', '_escena.html');

  for (const e of cfg.escenas) {
    // resolver tiempos relativos
    const T = (c) => (c.en !== undefined ? buscar(srt, c.en, e._ini - 0.5) - e._ini : (c.t || 0));
    const capas = (e.capas || []).map((c) => {
      const o = { ...c, t: T(c) };
      for (const k of ['fin', 'sale', 'vuela']) {
        if (o[k] && typeof o[k] === 'object') o[k] = { ...o[k], t: T(o[k]) };
        else if (k === 'fin' && typeof o[k] === 'string') o[k] = T({ en: o[k] });
      }
      for (const k of ['poses', 'camina', 'cambios', 'porciones']) if (o[k]) o[k] = o[k].map((x) => ({ ...x, t: T(x), ...(x.sale !== undefined ? { sale: typeof x.sale === 'string' ? T({ en: x.sale }) : x.sale } : {}) }));
      return o;
    });
    for (const o of capas) {
      const visible = (typeof o.fin === 'number' ? o.fin : e._dur) - o.t;
      if (o.tipo !== 'panel' && o.tipo !== 'hud' && visible < 1.5)
        console.warn(`⚠ escena ${e.id}: «${o.texto || o.tipo}» solo se ve ${visible.toFixed(1)} s`);
    }
    if (process.env.SOLO_COMPROBAR) continue;
    if (solo.length && !solo.includes(e.id)) continue;
    const fondoImg = (() => {
      if (!e.fondo || e.fondo.startsWith('#')) return null;
      for (const base of [path.join(dir, 'fondos'), cfg.fondos ? path.resolve(dir, cfg.fondos) : null].filter(Boolean))
        for (const ext of ['.png', '.jpg', '.jpeg', '.jfif', '.webp']) { const p = path.join(base, e.fondo + ext); if (fs.existsSync(p)) return url(p); }
      return null;
    })();
    const spec = { W: ANCHO, H: ALTO, capas, DUR: e._dur, MASC, fondo_img: fondoImg, fondo_color: fondoImg ? null : (e.fondo && e.fondo.startsWith('#') ? e.fondo : (e.color_provisional || '#F4E9D0')),
      zoom: e.zoom, pan: e.pan, fuente: e.fuente, sin_marca: e.sin_marca };
    fs.writeFileSync(tmp, html(spec), 'utf8');
    await page.goto(url(tmp), { waitUntil: 'networkidle0' });
    await page.waitForFunction('window.LISTO===true || window.ERROR', { timeout: 30000 });
    const err = await page.evaluate('window.ERROR'); if (err) throw new Error(err);
    const n = Math.round(e._dur * FPS);
    const salida = path.join(clips, `s_${e.id}.mp4`);
    const ff = spawn(FF, ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
      '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', String(FPS), salida]);
    for (let i = 0; i < n; i++) {
      await page.evaluate((tt) => window.pintar(tt), i / FPS);
      const buf = await page.screenshot({ type: 'jpeg', quality: 90 });
      if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once('drain', r));
    }
    ff.stdin.end(); await new Promise((r) => ff.on('close', r));
    console.log(`✓ s_${e.id}.mp4  ${e._ini.toFixed(1)}s → ${e._dur.toFixed(1)} s`);
  }
  await browser.close();
  fs.rmSync(tmp, { force: true });

  const montaje = { salida: cfg.salida || 'output/FINAL_YOUTUBE_1080P.mp4', formato: VERT ? 'vertical' : 'horizontal', voz: 'audio/voz.mp3',
    subtitulos: VERT ? 'audio/subtitulos_cortos.srt' : '06_SUBTITULOS.srt', quemar_subtitulos: VERT, musica: cfg.musica || null, musica_db: cfg.musica_db || -24,
    escenas: cfg.escenas.map((e) => ({ archivo: `clips/s_${e.id}.mp4`, duracion: +e._dur.toFixed(3) })) };
  fs.writeFileSync(path.join(dir, 'montaje.json'), JSON.stringify(montaje, null, 1));
}

main().catch((e) => { console.error(e); process.exit(1); });
