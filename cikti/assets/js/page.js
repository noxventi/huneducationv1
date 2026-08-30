/* ============================================================
   page.js — içerik sayfaları (rehber / kurumsal)
   Ana sayfanın ağır scroll sahnelerini yüklemez; yalnız header,
   reveal, imleç, WhatsApp ve içindekiler takibi.
   ============================================================ */

import { $, $$, env } from './core/util.js';
import { scroller, initReveal } from './core/scroll.js';
import { initHeader } from './modules/header.js';
import { initDropdowns } from './modules/dropdown.js';
import { initCursor } from './modules/cursor.js';
import { initWhatsApp } from './modules/whatsapp.js';
import { initAccordion } from './modules/accordion.js';
import { initForm } from './modules/form.js';

document.documentElement.classList.add('js-on');

/* İçindekiler: okunan bölümü işaretler.
   IntersectionObserver yerine scroll motoruna bağlı, çünkü hangi başlığın
   "şu an okunduğu" görünürlükten değil, üst kenara yakınlıktan belirlenir. */
function initToc() {
  const toc = $('.toc');
  if (!toc) return;
  const links = $$('a[href^="#"]', toc);
  if (!links.length) return;

  /* Mobilde katlanır: 9 bağlantılık blok içeriği ekranın altına itiyordu.
     Masaüstünde her zaman açık ve buton pasif davranır. */
  const toggle = $('.toc__toggle', toc);
  const mq = matchMedia('(max-width: 760px)');
  const applyMode = () => {
    if (mq.matches) {
      toc.classList.add('is-collapsed');
      toggle?.setAttribute('aria-expanded', 'false');
    } else {
      toc.classList.remove('is-collapsed');
      toggle?.setAttribute('aria-expanded', 'true');
    }
  };
  mq.addEventListener('change', applyMode);
  applyMode();

  toggle?.addEventListener('click', () => {
    if (!mq.matches) return;
    const open = toc.classList.toggle('is-collapsed') === false;
    toggle.setAttribute('aria-expanded', String(open));
  });
  /* Bir başlığa gidilince liste kendini kapatsın */
  toc.addEventListener('click', (e) => {
    if (mq.matches && e.target.closest('a')) toc.classList.add('is-collapsed');
  });

  const targets = links
    .map((a) => ({ a, el: document.getElementById(decodeURIComponent(a.hash.slice(1))) }))
    .filter((t) => t.el);
  if (!targets.length) return;

  let current = null;
  scroller.onFrame(() => {
    const line = innerHeight * 0.28;
    let found = targets[0];
    for (const t of targets) {
      if (t.el.getBoundingClientRect().top <= line) found = t;
      else break;
    }
    if (found === current) return;
    current?.a.classList.remove('is-current');
    found.a.classList.add('is-current');
    current = found;
  });
}

function boot() {
  initHeader(scroller);
  initDropdowns();
  initWhatsApp();
  initAccordion();
  initForm();
  initToc();
  initReveal();
  if (!env.touch && !env.reduce) initCursor();

  /* Okuma ilerlemesi header çizgisine bağlı */
  scroller.onFrame((s) => {
    const max = document.documentElement.scrollHeight - innerHeight;
    document.documentElement.style.setProperty('--page-p', max > 0 ? (s.y / max).toFixed(4) : 0);
  });

  const y = $('[data-year]');
  if (y) y.textContent = new Date().getFullYear();

  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href^="#"]');
    if (!a || a.getAttribute('href').length < 2) return;
    const target = document.querySelector(a.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    document.body.classList.remove('nav-open');
    scroller.scrollTo(target, -90);
    history.replaceState(null, '', a.getAttribute('href'));
  });
}

if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot, { once: true });
else boot();
