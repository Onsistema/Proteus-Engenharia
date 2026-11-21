(()=>{'use strict';
const d=document,b=d.body,top=d.querySelector('.top'),mb=d.querySelector('.menu-btn');
if(mb)mb.addEventListener('click',()=>{const o=b.classList.toggle('menu-open');mb.setAttribute('aria-expanded',String(o))});
d.querySelectorAll('.drop>button').forEach(btn=>{const p=btn.parentElement;
  btn.addEventListener('click',e=>{e.stopPropagation();const o=p.classList.toggle('open');btn.setAttribute('aria-expanded',String(o))});});
d.addEventListener('click',e=>{d.querySelectorAll('.drop.open').forEach(p=>{if(!p.contains(e.target)){p.classList.remove('open');p.querySelector('button').setAttribute('aria-expanded','false')}})});
d.addEventListener('keydown',e=>{if(e.key==='Escape'){d.querySelectorAll('.drop.open').forEach(p=>{p.classList.remove('open');p.querySelector('button').focus()});b.classList.remove('menu-open')}});
const onScroll=()=>top&&top.classList.toggle('scrolled',scrollY>8);addEventListener('scroll',onScroll,{passive:true});onScroll();
// Fios: calcula o comprimento de cada traço e anima uma única vez
d.querySelectorAll('.wires.draw').forEach(svg=>{svg.querySelectorAll('path').forEach(p=>p.style.setProperty('--len',Math.ceil(p.getTotalLength())));
  setTimeout(()=>svg.classList.add('done'),100)});
// Formulário: monta a mensagem e abre o WhatsApp
const f=d.getElementById('quote-form');
if(f)f.addEventListener('submit',e=>{e.preventDefault();if(!f.reportValidity())return;const v=n=>(f.elements.namedItem(n)?.value||'').trim();
  const msg=['Olá, Proteus! Gostaria de um orçamento.','Nome: '+v('name'),v('city')?'Cidade/bairro: '+v('city'):'','Serviço: '+v('service'),v('property')?'Tipo de imóvel: '+v('property'):'',v('details')?'Detalhes: '+v('details'):''].filter(Boolean).join('\n');
  location.assign('https://wa.me/5519971418256?text='+encodeURIComponent(msg))});
})();
