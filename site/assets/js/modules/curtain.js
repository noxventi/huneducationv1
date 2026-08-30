/* Açılış perdesi — kısa (≈1.1 sn), atlanabilir, oturumda bir kez.
   İçerik perde ardında hazır bekler; perde yalnız görsel bir katman. */

import { env, ticker, clamp } from '../core/util.js';

export function initCurtain() {
  const curtain = document.getElementById('curtain');
  if (!curtain) return;

  /* Aynı oturumda ikinci kez gösterme + hareket azaltmada hiç gösterme */
  const seen = sessionStorage.getItem('hun_curtain') === '1';
  if (seen || env.reduce) {
    curtain.remove();
    document.documentElement.classList.add('no-curtain');
    return;
  }

  const pct = curtain.querySelector('.curtain__pct');
  const started = performance.now();
  const MIN = 950; // en az bu kadar görünsün; daha fazlası içeriği geciktirir
  let p = 0;
  let done = false;

  const finish = () => {
    if (done) return;
    done = true;
    sessionStorage.setItem('hun_curtain', '1');
    curtain.classList.add('is-done');
    document.body.dispatchEvent(new CustomEvent('curtain:done'));
    setTimeout(() => curtain.remove(), 1200);
  };

  const stop = ticker.add(() => {
    const elapsed = performance.now() - started;
    /* Gerçek yükleme durumu + zaman tabanı: hangisi yavaşsa o belirler */
    const byTime = elapsed / MIN;
    const byLoad = document.readyState === 'complete' ? 1 : 0.82;
    p = clamp(Math.max(p, Math.min(byTime, byLoad)), 0, 1);

    curtain.style.setProperty('--load', p.toFixed(3));
    if (pct) pct.textContent = String(Math.round(p * 100)).padStart(2, '0');

    if (p >= 1) {
      stop();
      finish();
    }
  });

  /* Kaçış yolları: tıklama, klavye veya 2.6 sn tavan */
  curtain.addEventListener('click', finish);
  window.addEventListener('keydown', finish, { once: true });
  setTimeout(finish, 2600);
}
