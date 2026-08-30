/* ============================================================
   main.js — orkestrasyon
   Tüm modüller aynı rAF kalbine ve aynı scroll motoruna bağlanır.
   ============================================================ */

import { $$, splitWords, env } from './core/util.js';
import { scroller, initReveal } from './core/scroll.js';

import { initCurtain } from './modules/curtain.js';
import { initCursor } from './modules/cursor.js';
import { initHeader } from './modules/header.js';
import { initDropdowns } from './modules/dropdown.js';
import { initMarquee } from './modules/marquee.js';
import { initFields } from './modules/fields.js';
import { initProcess } from './modules/process.js';
import { initScrub } from './modules/scrub.js';
import { initWhy } from './modules/why.js';
import { initMap } from './modules/map.js';
import { initCost } from './modules/cost.js';
import { initAccordion } from './modules/accordion.js';
import { initForm } from './modules/form.js';
import { initWhatsApp } from './modules/whatsapp.js';

/* JS çalışıyor işareti — reveal stilleri ancak bundan sonra devreye girer,
   böylece JS yoksa/çökerse içerik %100 görünür kalır. */
document.documentElement.classList.add('js-on');

/* Hero giriş dizisini başlatır. Perde varsa animasyon perdenin ardında
   harcanmasın diye perde kalkınca, yoksa hemen tetiklenir. */
function initHero() {
  const start = () => document.body.classList.add('hero-in');
  if (document.documentElement.classList.contains('no-curtain') || !document.getElementById('curtain')) {
    requestAnimationFrame(start);
  } else {
    document.body.addEventListener('curtain:done', start, { once: true });
    setTimeout(start, 2800); // perde beklenmedik şekilde takılırsa emniyet
  }
}

function boot() {
  /* Başlık kelimelerini animasyon için sar */
  $$('[data-split]').forEach((el) => {
    splitWords(el);
    el.setAttribute('data-reveal', 'none');
  });

  initCurtain();
  initHero();

  /* Hero fotoğrafı parallax'ı: bölümün kaydırma ilerlemesi --hp olarak
     yazılır, görsel CSS'te bu değerle içerikten yavaş akar. */
  const hero = document.querySelector('.hero');
  if (hero) scroller.track(hero, { start: 'top top', end: 'bottom top', var: '--hp' });
  initHeader(scroller);
  initDropdowns();
  initMarquee(scroller);
  initFields(scroller);
  initProcess(scroller);
  initScrub(scroller);
  initWhy(scroller);
  initMap();
  initCost();
  initAccordion();
  initForm();
  initWhatsApp();

  if (!env.touch && !env.reduce) initCursor();

  initReveal();

  /* split-mask başlıkları da IntersectionObserver ile açılır */
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in');
        io.unobserve(e.target);
      });
    },
    { threshold: 0.15 }
  );
  $$('.split-mask').forEach((el) => (env.reduce ? el.classList.add('is-in') : io.observe(el)));

  /* Footer mega logotype parallax */
  const mega = document.querySelector('.ftr__mega');
  if (mega) scroller.track(mega, { start: 'top bottom', end: 'bottom bottom', var: '--ftp', smooth: 0.12 });

  /* Final bölüm arkaplanı */
  const final = document.querySelector('.final');
  if (final) scroller.track(final, { start: 'top bottom', end: 'bottom top', var: '--fnp', smooth: 0.1 });

  /* Sayfa ilerleme çubuğu */
  scroller.onFrame((s) => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    document.documentElement.style.setProperty('--page-p', max > 0 ? (s.y / max).toFixed(4) : 0);
  });

  /* Yıl */
  const y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();

  /* Sayfa içi bağlantılar: sabit header'ı hesaba kat */
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href^="#"]');
    if (!a) return;
    const id = a.getAttribute('href');
    if (id.length < 2) return;
    const target = document.querySelector(id);
    if (!target) return;
    e.preventDefault();
    document.body.classList.remove('nav-open');
    scroller.scrollTo(target, -70);
    history.replaceState(null, '', id);
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', boot, { once: true });
} else {
  boot();
}
