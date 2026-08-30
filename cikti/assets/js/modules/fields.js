/* Popüler alanlar: dikey scroll → yatay hareket.
   Pin, position:sticky ile CSS tarafında yapılır; JS yalnız
   kaydırma mesafesini ve konumu hesaplar. Mobilde devre dışı —
   orada doğal yatay kaydırma daha iyi hisseder. */

import { damp, ticker, env } from '../core/util.js';

export function initFields(scroller) {
  const section = document.querySelector('.fields');
  const track = document.querySelector('[data-fields-track]');
  if (!section || !track) return;

  const idxOut = document.querySelector('[data-field-idx]');
  /* Sayaç yalnız gerçek alan kartlarını sayar (son kart CTA'dır) */
  const realCards = Array.from(track.children).filter((c) => !c.classList.contains('fcard--cta'));
  let step = 1;
  let distance = 0;
  let cur = 0;
  let target = 0;

  const isMobile = () => matchMedia('(max-width: 860px)').matches;

  const measure = () => {
    const gap = parseFloat(getComputedStyle(track).columnGap || 0) || 0;
    step = (realCards[0]?.offsetWidth || 320) + gap;

    if (isMobile()) {
      section.style.removeProperty('--fields-h');
      track.style.removeProperty('--fldx');
      distance = 0;
      return;
    }
    /* Yatay kat edilecek mesafe */
    distance = Math.max(0, track.scrollWidth - window.innerWidth + parseFloat(getComputedStyle(track).paddingRight || 0));
    /* Bölüm yüksekliği = 1 ekran + yatay mesafe (1:1 his) */
    section.style.setProperty('--fields-h', `calc(100svh + ${Math.round(distance * 0.92)}px)`);
  };

  measure();
  addEventListener('resize', () => {
    measure();
    scroller.remeasure();
  }, { passive: true });
  if (document.fonts) document.fonts.ready.then(measure);
  addEventListener('load', measure);

  scroller.track(section, {
    start: 'top top',
    end: 'bottom bottom',
    onUpdate: (p) => {
      if (!distance) return;
      target = -p * distance;
      section.style.setProperty('--fldp', p.toFixed(4));
      if (idxOut) {
        /* Ekranın solundaki karta göre: gerçek kaydırma mesafesinden hesapla */
        const n = Math.min(realCards.length, Math.floor((p * distance) / step) + 1);
        const s = String(Math.max(1, n)).padStart(2, '0');
        if (idxOut.textContent !== s) idxOut.textContent = s;
      }
    },
  });

  /* Mobil: pin yok, doğal yatay kaydırma — ilerleme göstergesini ona bağla */
  track.addEventListener(
    'scroll',
    () => {
      if (!isMobile()) return;
      const max = track.scrollWidth - track.clientWidth;
      const p = max > 0 ? track.scrollLeft / max : 0;
      section.style.setProperty('--fldp', p.toFixed(4));
      if (idxOut) {
        const n = Math.min(realCards.length, Math.floor(track.scrollLeft / step) + 1);
        idxOut.textContent = String(Math.max(1, n)).padStart(2, '0');
      }
    },
    { passive: true }
  );

  /* Yumuşatma: scroll durduğunda kartlar hafifçe yerine oturur */
  ticker.add((dt) => {
    if (!distance) return;
    cur = env.reduce ? target : damp(cur, target, 0.18, dt);
    if (Math.abs(cur - target) < 0.15) cur = target;
    track.style.setProperty('--fldx', cur.toFixed(2) + 'px');
  });
}
