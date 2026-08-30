/* Header: scroll ile kompaktlaşır, aşağı inerken gizlenir,
   yukarı çıkarken geri gelir. Mobil menü, kayan menü göstergesi ve
   mobil CTA barı da burada. */

import { t } from '../core/i18n.js';

/* Kayan menü göstergesi.
   Ölçüm yalnız hover/focus anında ve resize'da yapılır; her karede
   değil. Konum translate + scaleX ile kurulduğu için animasyon
   compositor'da kalır, genişlik animasyonu layout tetiklemez. */
function initNavGlide(hdr) {
  const nav = hdr.querySelector('.hdr__nav');
  const glide = hdr.querySelector('.hdr__glide');
  if (!nav || !glide) return;

  const links = Array.from(nav.querySelectorAll('.hdr__link'));
  if (!links.length) return;

  const BASE = 100; // CSS'teki referans genişlik
  const current = () => nav.querySelector('.hdr__link[aria-current="page"]');

  function place(el) {
    if (!el) {
      glide.style.setProperty('--go', 0);
      return;
    }
    const nr = nav.getBoundingClientRect();
    const r = el.getBoundingClientRect();
    glide.style.setProperty('--gx', (r.left - nr.left).toFixed(2) + 'px');
    glide.style.setProperty('--gs', (r.width / BASE).toFixed(4));
    glide.style.setProperty('--go', 1);
  }

  const reset = () => place(current());

  links.forEach((a) => {
    a.addEventListener('pointerenter', () => place(a));
    a.addEventListener('focus', () => place(a));
  });
  nav.addEventListener('pointerleave', reset);
  nav.addEventListener('focusout', (e) => {
    if (!nav.contains(e.relatedTarget)) reset();
  });

  addEventListener('resize', reset, { passive: true });
  if (document.fonts) document.fonts.ready.then(reset);
  /* Header kompaktlaşınca yükseklik değişir → yeniden ölç */
  hdr.addEventListener('transitionend', (e) => {
    if (e.propertyName === 'height') reset();
  });

  reset();
}

export function initHeader(scroller) {
  const hdr = document.getElementById('hdr');
  const burger = document.getElementById('burger');
  const mnav = document.getElementById('mnav');
  const bar = document.getElementById('mobileBar');
  if (!hdr) return;

  const SOLID_AT = 80;
  const HIDE_AT = 420;
  /* Yalnız koyu hero'lu sayfalarda header şeffaf başlar.
     Diğer sayfalarda kalıcı olarak "solid" kalır — aksi hâlde açık zeminde
     beyaz logo ve beyaz menü metni okunmaz olurdu. */
  const overDark = hdr.classList.contains('hdr--over-dark');
  if (!overDark) hdr.classList.add('is-solid');

  let lastY = 0;
  let hidden = false;

  scroller.onFrame((s) => {
    const y = s.y;

    if (overDark) hdr.classList.toggle('is-solid', y > SOLID_AT);

    /* Menü açıkken header asla saklanmaz */
    if (!document.body.classList.contains('nav-open')) {
      const goingDown = y > lastY + 4;
      const goingUp = y < lastY - 4;
      if (goingDown && y > HIDE_AT && !hidden) {
        hidden = true;
        hdr.classList.add('is-hidden');
      } else if ((goingUp || y < SOLID_AT) && hidden) {
        hidden = false;
        hdr.classList.remove('is-hidden');
      }
    }

    /* Mobil CTA barı: hero geçildikten sonra, final formda gizlenir */
    if (bar) {
      const final = document.getElementById('gorusme');
      const inFinal = final ? final.getBoundingClientRect().top < innerHeight * 0.8 : false;
      bar.classList.toggle('is-up', y > innerHeight * 0.9 && !inFinal);
    }

    lastY = y;
  });

  initNavGlide(hdr);

  /* ---- Mobil menü ---- */
  if (burger && mnav) {
    const setOpen = (open) => {
      document.body.classList.toggle('nav-open', open);
      document.body.classList.toggle('is-locked', open);
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? t('nav.close') : t('nav.open'));
      if (open) {
        mnav.hidden = false;
        hdr.classList.remove('is-hidden');
        hidden = false;
        requestAnimationFrame(() => mnav.querySelector('a')?.focus());
      } else {
        /* Kapanma animasyonu bitmeden hidden'a alma */
        setTimeout(() => {
          if (!document.body.classList.contains('nav-open')) mnav.hidden = true;
        }, 800);
      }
    };

    burger.addEventListener('click', () => setOpen(!document.body.classList.contains('nav-open')));
    mnav.addEventListener('click', (e) => {
      if (e.target.closest('a')) setOpen(false);
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && document.body.classList.contains('nav-open')) {
        setOpen(false);
        burger.focus();
      }
    });

    /* Focus tuzağı — açık menüden sekmeyle çıkılmasın */
    mnav.addEventListener('keydown', (e) => {
      if (e.key !== 'Tab') return;
      const f = mnav.querySelectorAll('a, button');
      if (!f.length) return;
      const first = f[0];
      const last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        burger.focus();
      }
    });
  }
}
