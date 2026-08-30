/* Hız duyarlı marquee: sürekli akar, scroll hızıyla hızlanır,
   scroll yönü değişince yön değiştirir. Klasik "ödül sitesi" hissi
   ama tek bir transform ile — DOM'da tek satır klonlanır. */

import { ticker, env } from '../core/util.js';

export function initMarquee(scroller) {
  const rows = document.querySelectorAll('[data-mq]');
  if (!rows.length) return;

  rows.forEach((row) => {
    const wrap = row.parentElement;
    const base = parseFloat(row.dataset.mqSpeed || 60); // px/sn

    /* Kesintisiz akış için satırı dolduracak kadar klonla */
    const original = row.innerHTML;
    let unit = row.scrollWidth;
    const fill = () => {
      row.innerHTML = original;
      unit = row.scrollWidth;
      const need = Math.ceil((wrap.offsetWidth * 2) / Math.max(unit, 1)) + 1;
      for (let i = 0; i < need; i++) row.insertAdjacentHTML('beforeend', original);
    };
    fill();
    addEventListener('resize', fill, { passive: true });

    if (env.reduce) return;

    let x = 0;
    ticker.add((dt) => {
      const boost = 1 + Math.abs(scroller.vel) * 7;
      const dir = scroller.dir >= 0 ? -1 : 1;
      x += dir * base * boost * dt;
      /* modulo ile sonsuz döngü */
      if (x <= -unit) x += unit;
      if (x >= 0) x -= unit;
      row.style.transform = `translate3d(${x.toFixed(2)}px,0,0)`;
    });
  });
}
