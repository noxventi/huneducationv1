/* Özel imleç + manyetik butonlar.
   Yalnız hassas işaretleyicide ve hareket azaltma kapalıyken çalışır. */

import { ticker, damp, $$ } from '../core/util.js';

export function initCursor() {
  const el = document.getElementById('cursor');
  if (!el) return;

  const ring = el.querySelector('.cursor__ring');
  const dot = el.querySelector('.cursor__dot');
  const label = el.querySelector('.cursor__label');

  const m = { x: innerWidth / 2, y: innerHeight / 2 };
  const ringPos = { ...m };
  const dotPos = { ...m };
  let live = false;

  addEventListener(
    'pointermove',
    (e) => {
      if (e.pointerType !== 'mouse') return;
      m.x = e.clientX;
      m.y = e.clientY;
      if (!live) {
        live = true;
        ringPos.x = dotPos.x = m.x;
        ringPos.y = dotPos.y = m.y;
        el.classList.add('is-live');
      }
    },
    { passive: true }
  );

  addEventListener('pointerdown', () => el.classList.add('is-down'));
  addEventListener('pointerup', () => el.classList.remove('is-down'));
  document.addEventListener('mouseleave', () => el.classList.remove('is-live'));
  document.addEventListener('mouseenter', () => live && el.classList.add('is-live'));

  /* Etkileşimli hedefler: halka büyür, isteğe bağlı etiket gösterir */
  const HOT = 'a, button, [data-cursor], input, select, textarea, .pin, .citem, .fopt';
  document.addEventListener('pointerover', (e) => {
    const hot = e.target.closest(HOT);
    if (!hot) return;
    el.classList.add('is-hot');
    const txt = hot.dataset.cursor || hot.closest('[data-cursor]')?.dataset.cursor;
    if (txt) {
      label.textContent = txt;
      el.classList.add('has-label');
    }
  });
  document.addEventListener('pointerout', (e) => {
    if (e.relatedTarget && e.relatedTarget.closest?.(HOT)) return;
    el.classList.remove('is-hot', 'has-label');
  });

  /* Halka gecikmeli, nokta anlık → derinlik hissi */
  ticker.add((dt) => {
    if (!live) return;
    ringPos.x = damp(ringPos.x, m.x, 0.18, dt);
    ringPos.y = damp(ringPos.y, m.y, 0.18, dt);
    dotPos.x = damp(dotPos.x, m.x, 0.55, dt);
    dotPos.y = damp(dotPos.y, m.y, 0.55, dt);

    ring.style.transform = `translate3d(${ringPos.x}px, ${ringPos.y}px, 0) translate(-50%, -50%)`;
    label.style.transform = `translate3d(${ringPos.x}px, ${ringPos.y}px, 0) translate(-50%, -50%) scale(${
      el.classList.contains('has-label') ? 1 : 0.6
    })`;
    dot.style.transform = `translate3d(${dotPos.x}px, ${dotPos.y}px, 0) translate(-50%, -50%)`;
  });

  initMagnetic();
}

/* Manyetik butonlar: imleç yaklaşınca buton ona doğru esner. */
function initMagnetic() {
  const items = $$('[data-magnetic]');
  if (!items.length) return;

  const state = items.map((el) => ({ el, x: 0, y: 0, tx: 0, ty: 0, active: false, r: null }));

  const measure = () => state.forEach((s) => (s.r = s.el.getBoundingClientRect()));
  measure();
  addEventListener('resize', measure, { passive: true });
  addEventListener('scroll', measure, { passive: true });

  addEventListener(
    'pointermove',
    (e) => {
      if (e.pointerType !== 'mouse') return;
      for (const s of state) {
        if (!s.r) continue;
        const cx = s.r.left + s.r.width / 2;
        const cy = s.r.top + s.r.height / 2;
        const dx = e.clientX - cx;
        const dy = e.clientY - cy;
        const radius = Math.max(s.r.width, s.r.height) * 0.85 + 40;
        const dist = Math.hypot(dx, dy);
        if (dist < radius) {
          const pull = 1 - dist / radius;
          s.tx = dx * 0.32 * pull;
          s.ty = dy * 0.42 * pull;
          s.active = true;
        } else if (s.active) {
          s.tx = 0;
          s.ty = 0;
          s.active = false;
        }
      }
    },
    { passive: true }
  );

  ticker.add((dt) => {
    for (const s of state) {
      const nx = damp(s.x, s.tx, 0.16, dt);
      const ny = damp(s.y, s.ty, 0.16, dt);
      if (Math.abs(nx - s.x) < 0.01 && Math.abs(ny - s.y) < 0.01 && s.tx === 0) continue;
      s.x = nx;
      s.y = ny;
      s.el.style.setProperty('--mx', s.x.toFixed(2) + 'px');
      s.el.style.setProperty('--my', s.y.toFixed(2) + 'px');
    }
  });
}
