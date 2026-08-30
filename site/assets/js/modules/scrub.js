/* Manifesto metni: scroll ilerledikçe kelimeler tek tek aydınlanır.
   Sınıf değişimi kelime bazında ve yalnız gerektiğinde yapılır. */

import { splitWords, env } from '../core/util.js';

export function initScrub(scroller) {
  document.querySelectorAll('[data-scrub]').forEach((el) => {
    const words = splitWords(el);
    if (env.reduce) {
      words.forEach((w) => w.classList.add('lit'));
      return;
    }

    let lit = -1;
    scroller.track(el, {
      start: 'top 78%',
      end: 'bottom 55%',
      onUpdate: (p) => {
        /* Baştan biraz hızlı, sonda yavaş: okuma temposuna yakın */
        const n = Math.round(p * words.length * 1.06);
        if (n === lit) return;
        if (n > lit) {
          for (let i = lit + 1; i <= n && i < words.length; i++) words[i].classList.add('lit');
        } else {
          for (let i = lit; i > n; i--) words[i]?.classList.remove('lit');
        }
        lit = n;
      },
    });
  });
}
