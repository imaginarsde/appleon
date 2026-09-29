from pathlib import Path
import re,sys
root=Path(sys.argv[1])
def R(n): return (root/n).read_text(encoding="utf-8")
def W(n,s): (root/n).write_text(s,encoding="utf-8")

s=R("index.html")
s=s.replace("</head>",'<link rel="stylesheet" href="android7.css?v=1"></head>')
s=s.replace('<script src="content.js','<script src="compat.js?v=1"></script><script src="content.js')
W("index.html",s)

W("compat.js",'''(function(){
if(!window.console)window.console={log:function(){},error:function(){},warn:function(){}};
if(!Array.from)Array.from=function(a){return Array.prototype.slice.call(a);};
if(!Array.prototype.includes)Array.prototype.includes=function(v){return this.indexOf(v)!==-1;};
if(!String.prototype.startsWith)String.prototype.startsWith=function(s){return this.slice(0,s.length)===s;};
if(!Object.assign)Object.assign=function(t){for(var i=1;i<arguments.length;i++){var s=arguments[i]||{};for(var k in s)if(Object.prototype.hasOwnProperty.call(s,k))t[k]=s[k];}return t;};
if(window.NodeList&&!NodeList.prototype.forEach)NodeList.prototype.forEach=Array.prototype.forEach;
if(window.Element&&!Element.prototype.matches)Element.prototype.matches=Element.prototype.msMatchesSelector||Element.prototype.webkitMatchesSelector;
if(window.Element&&!Element.prototype.closest)Element.prototype.closest=function(sel){var e=this;while(e&&e.nodeType===1){if(e.matches(sel))return e;e=e.parentElement||e.parentNode;}return null;};
if(window.Element&&!Element.prototype.remove)Element.prototype.remove=function(){if(this.parentNode)this.parentNode.removeChild(this);};
window.__cloneJson=function(v){return JSON.parse(JSON.stringify(v));};
window.__uuid=function(){return 'q-'+Date.now().toString(36)+'-'+Math.random().toString(36).slice(2,10)+'-'+Math.random().toString(36).slice(2,8);};
window.__readTextFile=function(file){return new Promise(function(resolve,reject){var r=new FileReader();r.onload=function(){resolve(String(r.result||''));};r.onerror=function(){reject(r.error||new Error('No se pudo leer el archivo.'));};r.readAsText(file);});};
})();''')

W("android7.css",'''html,body{width:100%;height:100%;margin:0;overflow:hidden}body{position:fixed;left:0;top:0;right:0;bottom:0}
.shell{height:100vh!important;min-height:0!important;max-width:none!important;margin:0!important;padding:8px 24px!important;display:-webkit-flex!important;display:flex!important;-webkit-flex-direction:column!important;flex-direction:column!important;overflow:hidden!important}
header{height:54px!important;min-height:54px!important;-webkit-flex:0 0 54px!important;flex:0 0 54px!important}#stage{display:block!important;-webkit-flex:1 1 auto!important;flex:1 1 auto!important;min-height:0!important;overflow:hidden!important}
.brand-footer{height:86px!important;min-height:86px!important;-webkit-flex:0 0 86px!important;flex:0 0 86px!important;padding:0!important;display:-webkit-flex!important;display:flex!important;justify-content:center!important;align-items:center!important}.brand-footer .footer-youth{width:200px!important;margin-right:64px!important}.brand-footer .municipality-brand{width:195px!important;height:67px!important;overflow:hidden!important}.brand-footer>.footer-youth,.brand-footer>.municipality-brand{transform:none!important}
.bibliodera-brand{position:absolute!important;left:20px!important;top:10px!important;width:310px!important;height:87px!important;max-height:none!important;overflow:hidden!important}.bibliodera-brand img{position:absolute!important;width:389px!important;height:390px!important;left:-39px!important;top:-147px!important;max-width:none!important}
.cover,.split{display:-webkit-flex!important;display:flex!important;-webkit-flex-direction:row!important;flex-direction:row!important;align-items:center!important;width:100%!important;height:100%!important;min-height:0!important;padding:0!important}.cover .copy,.split .copy{width:47%!important}.cover .visual,.split .visual{width:53%!important;height:100%!important;display:-webkit-flex!important;display:flex!important;align-items:center!important;justify-content:center!important}
.cover h1.lettering-title{width:42vw!important;height:11.8vw!important;max-width:none!important;margin:0 auto 20px!important}.cover .lettering-title .brand-art{width:42vw!important;height:11.8vw!important;overflow:hidden!important}.cover .lettering-title .brand-art img{position:absolute!important;width:52.74vw!important;height:52.88vw!important;left:-5.27vw!important;top:-19.86vw!important;max-width:none!important}.cover p{font-size:1.2vw!important;line-height:1.35!important;margin:0 auto 10px!important}
.cover .wheel-wrap,#stage[data-screen=girando] .wheel-wrap{width:58vh!important;height:58vh!important;max-width:720px!important;max-height:720px!important;margin:18px auto 28px!important}.wheel{background:#fff0ce!important}.wheel-svg{position:absolute;left:0;top:0;width:100%;height:100%;border-radius:50%}.wedge-label{z-index:1}.wedge-label strong svg{width:42px!important;height:42px!important}.wedge-label span{width:34%!important;font-size:13px!important;line-height:1.08!important;letter-spacing:0!important;text-align:center!important;margin-top:5px!important}.hub{left:36%!important;right:36%!important;top:36%!important;bottom:36%!important}.hub-action>strong{font-size:30px!important}
#stage[data-screen=girando] h1{font-size:7.8vw!important;line-height:.92!important}.eyebrow{font-size:1vw!important}.category-reveal{display:block!important;text-align:center!important;padding-top:10vh!important}.category-reveal h1{font-size:10vw!important}.question{padding:12px 2vw!important;height:100%!important}.question h1{font-size:4vw!important}.question .answers{display:-webkit-flex!important;display:flex!important;-webkit-flex-wrap:wrap!important;flex-wrap:wrap!important}.question .answer{width:48%!important;margin:1%!important;min-height:92px!important;font-size:1.65vw!important}
.settings{height:100%!important;overflow-y:auto!important;padding:18px 2vw 40px!important;font-size:18px!important}.settings-layout{display:-webkit-flex!important;display:flex!important}.settings-layout>form,.settings-layout>.bank{width:48%!important}.settings-layout>form{margin-right:4%!important}.option-fields,.category-fields{display:-webkit-flex!important;display:flex!important;-webkit-flex-wrap:wrap!important;flex-wrap:wrap!important}.option-fields label,.category-fields label{width:48%!important;margin-right:2%!important}.settings-choices{display:-webkit-flex!important;display:flex!important;max-width:1200px!important;margin:26px auto!important}.settings-choices a{width:48%!important;margin:1%!important;min-height:210px!important}.settings h1{font-size:52px!important}.settings p,.settings input,.settings textarea,.settings select{font-size:18px!important}#stage[data-screen^=configuracion]{padding-top:58px!important;overflow-y:auto!important}
.loop-player{position:fixed!important;left:0!important;top:0!important;right:0!important;bottom:0!important;z-index:9999!important}.loop-player video{width:100%!important;height:100%!important;object-fit:cover!important}
''')

for n in ["content.js","sound.js"]:
    W(n,R(n).replace("catch{}","catch(e){}"))

c=R("components.js"); a=c.index(" function wheel("); b=c.index(" const backToGame",a)
wheel=''' function wheel(spinning=false, interactive=false) {
 const cats=BiblioderaContent.categories, slice=360/cats.length;
 function point(angle,r){const a=(angle-90)*Math.PI/180;return [100+r*Math.cos(a),100+r*Math.sin(a)];}
 function sector(i){const center=i*slice,start=center-slice/2,end=center+slice/2,p1=point(start,98),p2=point(end,98);return '<path d="M100 100 L'+p1[0].toFixed(3)+' '+p1[1].toFixed(3)+' A98 98 0 0 1 '+p2[0].toFixed(3)+' '+p2[1].toFixed(3)+' Z" fill="'+cats[i].color+'" stroke="rgba(255,255,255,.36)" stroke-width=".7"/>';}
 const svg='<svg class="wheel-svg" viewBox="0 0 200 200" aria-hidden="true">'+cats.map((c,i)=>sector(i)).join('')+'</svg>';
 return '<div class="wheel-wrap"><div class="pointer"></div><div class="wheel '+(spinning?'spinning':'')+'" style="--spin-duration:'+BiblioderaContent.spinDuration+'ms;--end-rotation:'+(BiblioderaContent.wheelRotation||1440)+'deg">'+svg+cats.map((c,i)=>'<div class="wedge-label" style="--angle:'+(i*slice)+'deg"><strong>'+categoryIcon(c)+'</strong><span>'+escape(c.label)+'</span></div>').join('')+'</div>'+(interactive?'<button class="hub hub-action" data-go="girando" '+(spinning?'disabled':'')+'><strong>GIRAR</strong></button>':'<div class="hub">LA<br><b>B</b></div>')+'<div class="wheel-foot"></div></div>';
 }
'''
W("components.js",c[:a]+wheel+c[b:])

m=R("motion.js")
m=m.replace("stage.querySelector('.wheel-wrap')?.getBoundingClientRect()","(function(e){return e?e.getBoundingClientRect():null;})(stage.querySelector('.wheel-wrap'))")
for x,y in [("exitTween?.kill();","if(exitTween)exitTween.kill();"),("exitDone?.();","if(exitDone)exitDone();"),("context?.revert();","if(context)context.revert();"),("logoTween?.kill();","if(logoTween)logoTween.kill();"),("logo?.remove();","if(logo)logo.remove();"),("inviteTween?.revert();","if(inviteTween)inviteTween.revert();"),("logoTween?.progress(1);","if(logoTween)logoTween.progress(1);"),("spinTimeline?.progress(1);","if(spinTimeline)spinTimeline.progress(1);")]: m=m.replace(x,y)
m=m.replace("window.addEventListener('resize',()=>logoTween?.progress(1));","window.addEventListener('resize',()=>{if(logoTween)logoTween.progress(1);});")
m=m.replace("preference.addEventListener('change',()=>{if(reduced()){if(inviteTween)inviteTween.revert();if(logoTween)logoTween.progress(1);if(spinTimeline)spinTimeline.progress(1);}});","const pc=()=>{if(reduced()){if(inviteTween)inviteTween.revert();if(logoTween)logoTween.progress(1);if(spinTimeline)spinTimeline.progress(1);}};if(preference.addEventListener)preference.addEventListener('change',pc);else if(preference.addListener)preference.addListener(pc);")
W("motion.js",m)

q=R("settings.js")
q=q.replace("const key='biblodera.questions.v1';let error='';","const key='biblodera.questions.v1';let error='';const clone=v=>window.__cloneJson(v);const uuid=()=>window.__uuid();")
q=q.replace("structuredClone(value)","clone(value)").replace("structuredClone(next)","clone(next)").replace("crypto.randomUUID()","uuid()").replace("stage.focus({preventScroll:true})","stage.focus()")
q=q.replace("stage.querySelector('.settings-layout').after(categoryForm);","const layout=stage.querySelector('.settings-layout');layout.parentNode.insertBefore(categoryForm,layout.nextSibling);")
q=re.sub(r"stage\.querySelector\('#export-bank'\)\.onclick=.*?;\n\s*stage\.querySelector\('#import-bank'\)\.onchange=async e=>\{.*?\};\n\s*if\(selected==='preguntas'\)",'''stage.querySelector('#export-bank').onclick=()=>{const data=JSON.stringify(QuestionStore.get(),null,2);if(window.AndroidBridge&&AndroidBridge.exportJson){AndroidBridge.exportJson('bibliodera-preguntas.json',data);message('Elegí dónde guardar la copia.');return;}};
  stage.querySelector('#import-bank').onchange=e=>{const input=e.target,file=input.files[0];if(!file)return;if(file.size>1000000){message('El archivo supera 1 MB.');input.value='';return;}window.__readTextFile(file).then(text=>{const next=QuestionStore.validate(JSON.parse(text));confirm('¿Reemplazar el banco?','Se cargarán '+next.questions.length+' preguntas y un tiempo de '+next.seconds+' segundos.',()=>{if(save(next,'Copia importada.')){reset();stage.querySelector('[name=seconds]').value=next.seconds;list();}});}).catch(err=>message('No se pudo importar: '+err.message)).then(()=>{input.value='';});};
  if(selected==='preguntas')''',q,flags=re.S)
W("settings.js",q)

a=R("app.js").replace("const category=()=>data.categories[current?.category??0];","const category=()=>data.categories[current&&current.category!=null?current.category:0];").replace("current?.special","current&&current.special").replace("stage.focus({preventScroll:true});","stage.focus();")
mm=re.search(r" async function render\(\)\{([\s\S]*?)\}\n document\.addEventListener",a)
if not mm: raise RuntimeError("render no encontrado")
body=mm.group(1).replace("await motion.exit(id);","return Promise.resolve(motion.exit(id)).then(function(){")
a=a[:mm.start()]+" function render(){"+body+"\n });\n }\n document.addEventListener"+a[mm.end():]
W("app.js",a)

snd=R("sound.js").replace("document.addEventListener('pointerdown',unlock,{capture:true});document.addEventListener('keydown',unlock,{capture:true});","document.addEventListener('touchstart',unlock,true);document.addEventListener('mousedown',unlock,true);document.addEventListener('keydown',unlock,true);")
W("sound.js",snd)

W("video-loop.js",'''window.VideoLoop=(function(){
var generation=0,urls=new Set();
function db(){return new Promise(function(ok,bad){var r=indexedDB.open('bibliodera-media',1);r.onupgradeneeded=function(){r.result.createObjectStore('media');};r.onsuccess=function(){ok(r.result);};r.onerror=function(){bad(r.error);};});}
function storage(value){return db().then(function(d){return new Promise(function(ok,bad){var tx=d.transaction('media',value!==undefined?'readwrite':'readonly'),s=tx.objectStore('media'),r=value===null?s.delete('loop'):value!==undefined?s.put(value,'loop'):s.get('loop');tx.oncomplete=function(){d.close();ok(r.result);};tx.onerror=tx.onabort=function(){d.close();bad(tx.error||Error('No se pudo guardar el video.'));};});});}
function source(f){var u=URL.createObjectURL(f);urls.add(u);return u;}function stop(){generation++;Array.prototype.forEach.call(document.querySelectorAll('video'),function(v){v.pause();v.removeAttribute('src');v.load();});urls.forEach(function(u){URL.revokeObjectURL(u);});urls.clear();}
function validate(f){return new Promise(function(ok,bad){var v=document.createElement('video'),u=URL.createObjectURL(f),t;function end(e){clearTimeout(t);v.removeAttribute('src');v.load();URL.revokeObjectURL(u);e?bad(Error(e)):ok();}v.preload='metadata';v.onloadedmetadata=function(){end(v.videoWidth?'':'Video inválido.');};v.onerror=function(){end('No se puede reproducir este archivo.');};t=setTimeout(function(){end('No se pudo leer el video.');},15000);v.src=u;});}
function settings(p){var token=generation;p.innerHTML='<div class="loop-settings"><h2>Video en loop</h2><div class="loop-actions"><label class="video-upload">Elegir video<input type="file" accept="video/mp4,video/webm,.mp4,.webm"></label><button id="delete-loop" hidden>Eliminar video</button><button class="button" id="start-loop" disabled>Iniciar loop</button></div><p id="loop-status">Buscando video guardado…</p><video class="loop-preview" controls muted playsinline hidden></video></div>';var st=p.querySelector('#loop-status'),inp=p.querySelector('input'),prev=p.querySelector('video'),start=p.querySelector('#start-loop'),del=p.querySelector('#delete-loop'),loaded=false;function active(){return token===generation&&document.documentElement.contains(p);}function show(r){loaded=true;del.hidden=false;prev.src=source(r.file);prev.hidden=false;start.disabled=false;st.textContent='Video guardado: '+r.name;}start.onclick=function(){location.hash='loop';};del.onclick=function(){storage(null).then(function(){stop();location.hash='configuracion-loop';});};inp.onchange=function(){var f=inp.files[0];if(!f)return;if(f.size>500*1024*1024){st.textContent='El video supera 500 MB.';return;}st.textContent='Guardando video…';validate(f).then(function(){return storage({file:f,name:f.name});}).then(function(){if(active())show({file:f,name:f.name});}).catch(function(e){if(active())st.textContent=e.message||'No se pudo guardar.';});};storage().then(function(r){if(active()){if(r)show(r);else st.textContent='Todavía no cargaste un video.';}}).catch(function(){if(active())st.textContent='No se pudo recuperar el video.';});}
function mount(stage,selected){var sec=stage.querySelector('.settings'),head=sec.querySelector('.settings-heading'),p=head.querySelector('p');if(p)p.remove();var q=document.createElement('div');q.id='questions-panel';Array.prototype.slice.call(sec.children).filter(function(e){return e!==head;}).forEach(function(e){q.appendChild(e);});sec.appendChild(q);q.hidden=selected==='loop';if(selected==='loop'){var panel=document.createElement('div');sec.appendChild(panel);settings(panel);}}
function play(stage){var token=generation;stage.innerHTML='<section class="loop-player"><video autoplay muted loop playsinline></video><a class="loop-exit" href="#configuracion-loop">×</a><div class="loop-message">Cargando video…</div><button class="button loop-resume" hidden>Reproducir video</button></section>';var v=stage.querySelector('video'),m=stage.querySelector('.loop-message'),b=stage.querySelector('.loop-resume');function active(){return token===generation&&document.documentElement.contains(v);}function begin(){var p=v.play();if(p&&p.then)p.then(function(){if(active()){m.textContent='';b.hidden=true;}}).catch(function(){if(active()){m.textContent='Tocá para iniciar el video.';b.hidden=false;}});}b.onclick=begin;storage().then(function(r){if(!r){m.textContent='Cargá un video desde Configuración → Loop.';return;}v.src=source(r.file);begin();}).catch(function(){m.textContent='No se pudo recuperar el video.';});}
function menu(stage){stage.innerHTML='<section class="settings settings-menu"><div class="settings-heading"><div><h1>Configuración</h1><p>¿Qué querés preparar?</p></div>'+BiblioderaUI.backToGame()+'</div><nav class="settings-choices"><a href="#configuracion-preguntas"><strong>Preguntas</strong><span>Cargá y editá el contenido</span></a><a href="#configuracion-loop"><strong>Loop</strong><span>Prepará el video del stand</span></a></nav></section>';}
return {mount:mount,play:play,stop:stop,menu:menu};})();''')

for n in ["content.js","components.js","motion.js","settings.js","sound.js","video-loop.js","app.js"]:
    t=R(n).replace("catch{}","catch(e){}")
    if re.search(r"\?\.(?![0-9])|\?\?|\basync\b|\bawait\b",t): raise RuntimeError("Sintaxis moderna remanente en "+n)
    W(n,t)
