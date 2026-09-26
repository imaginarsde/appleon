(function(){
  'use strict';
  function AudioBank(base){
    this.base=base||'assets/audio/';this.enabled=true;this.volume=.28;this.current=null;
    this.items={tap:new Audio(this.base+'tap.mp3'),open:new Audio(this.base+'open.mp3'),close:new Audio(this.base+'close.mp3')};
    var keys=Object.keys(this.items),i,a;for(i=0;i<keys.length;i++){a=this.items[keys[i]];a.preload='auto';a.volume=this.volume;}
  }
  AudioBank.prototype.play=function(name){if(!this.enabled||!this.items[name])return;if(this.current&&!this.current.paused){this.current.pause();this.current.currentTime=0;}var audio=this.items[name];audio.currentTime=0;this.current=audio;try{var p=audio.play();if(p&&typeof p.catch==='function')p.catch(function(){});}catch(e){}};
  AudioBank.prototype.preload=function(){var keys=Object.keys(this.items),i;for(i=0;i<keys.length;i++){try{this.items[keys[i]].load();}catch(e){}}};
  window.AudioBank=AudioBank;
})();