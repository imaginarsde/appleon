(function(){
  'use strict';
  var ENABLE_AUDIO=true;
  var sections={
    alimentacion:{image:'assets/images/modal_alimentacion.webp',alt:'Alimentación del león: dieta carnívora, presas, caza en grupo y descanso',box:{left:21.833,top:27.725,width:58.333,height:67.536}},
    caracteristicas:{image:'assets/images/modal_caracteristicas.webp',alt:'Características del león: melena, sabana, manadas, sentidos, rugido y descanso',box:{left:23.0,top:21.919,width:53.0,height:73.164}},
    pesoAltura:{image:'assets/images/modal_peso_altura.webp',alt:'Peso y altura del león: medidas corporales, pesos y capacidades físicas',box:{left:23.0,top:21.742,width:53.0,height:73.341}}
  };
  var ui={
    loader:document.getElementById('loader'),backdrop:document.getElementById('backdrop'),modalLayer:document.getElementById('modalLayer'),modalCard:document.getElementById('modalCard'),modalImage:document.getElementById('modalImage'),closeX:document.getElementById('modalCloseX'),closeMain:document.getElementById('modalCloseMain'),topicButtons:document.querySelectorAll('.topic-button'),errorBox:document.getElementById('errorBox')
  };
  var audio=new AudioBank();audio.enabled=ENABLE_AUDIO;
  var activeSection=null,lastTrigger=null,closing=false;
  function pressFeedback(el,ms){if(!el)return;ms=typeof ms==='number'?ms:105;el.classList.add('is-pressed');window.setTimeout(function(){el.classList.remove('is-pressed');},ms);}
  function playSound(name){audio.play(name);}
  function placeModal(section){var b=sections[section].box;ui.modalCard.style.left=b.left+'%';ui.modalCard.style.top=b.top+'%';ui.modalCard.style.width=b.width+'%';ui.modalCard.style.height=b.height+'%';}
  function focusSafe(el){try{if(el&&typeof el.focus==='function')el.focus();}catch(e){}}
  function openModal(section,trigger){
    if(!sections[section]||activeSection||closing)return;
    activeSection=section;lastTrigger=trigger||document.activeElement;pressFeedback(trigger);playSound('tap');placeModal(section);
    ui.modalImage.src=sections[section].image;ui.modalImage.alt=sections[section].alt;ui.modalLayer.hidden=false;ui.modalLayer.setAttribute('aria-hidden','false');ui.backdrop.hidden=false;ui.modalCard.classList.remove('is-closing');
    window.requestAnimationFrame(function(){ui.backdrop.classList.add('is-open');ui.modalCard.classList.add('is-open');});
    window.setTimeout(function(){playSound('open');focusSafe(ui.closeX);},115);
  }
  function closeModal(trigger){
    if(!activeSection||closing)return;closing=true;if(trigger)pressFeedback(trigger,95);playSound('close');ui.modalCard.classList.remove('is-open');ui.modalCard.classList.add('is-closing');ui.backdrop.classList.remove('is-open');
    window.setTimeout(function(){ui.modalLayer.hidden=true;ui.modalLayer.setAttribute('aria-hidden','true');ui.backdrop.hidden=true;ui.modalCard.classList.remove('is-closing');ui.modalImage.src='';activeSection=null;closing=false;focusSafe(lastTrigger);},320);
  }
  function preloadExperience(){
    var images=['assets/images/home.webp','assets/images/button_alimentacion.webp','assets/images/button_caracteristicas.webp','assets/images/button_peso_altura.webp',sections.alimentacion.image,sections.caracteristicas.image,sections.pesoAltura.image];
    var pending=images.length;
    function done(){pending--;if(pending<=0)window.setTimeout(function(){ui.loader.classList.add('is-hidden');},180);}
    audio.preload();
    var i,img;for(i=0;i<images.length;i++){img=new Image();img.onload=done;img.onerror=done;img.src=images[i];}
    window.setTimeout(function(){if(!ui.loader.classList.contains('is-hidden'))ui.loader.classList.add('is-hidden');},4500);
  }
  function bindButton(button){var section=button.getAttribute('data-section');button.addEventListener('click',function(){openModal(section,button);},false);button.addEventListener('touchstart',function(){button.classList.add('is-pressed');},false);button.addEventListener('touchend',function(){button.classList.remove('is-pressed');},false);button.addEventListener('touchcancel',function(){button.classList.remove('is-pressed');},false);}
  var i;for(i=0;i<ui.topicButtons.length;i++)bindButton(ui.topicButtons[i]);
  ui.closeX.addEventListener('click',function(){closeModal(ui.closeX);},false);ui.closeMain.addEventListener('click',function(){closeModal(ui.closeMain);},false);ui.backdrop.addEventListener('click',function(){closeModal();},false);
  document.addEventListener('keydown',function(event){if((event.key==='Escape'||event.keyCode===27)&&activeSection)closeModal();},false);
  window.onerror=function(msg,src,line){if(ui.errorBox){ui.errorBox.style.display='block';ui.errorBox.innerHTML='ERROR JS: '+msg+'\nLínea: '+line;}return false;};
  window.openModal=openModal;window.closeModal=closeModal;window.playSound=playSound;
  preloadExperience();
})();