/* Süreç bölümü — kart destesi.

   Adımlar `position: sticky` ile üst üste toplanır: her kart bir öncekinin
   14px altına yapışır, altta kalanlar hafifçe küçülerek yığına derinlik verir.
   Aktif kart değiştikçe arkadaki fotoğraf, yolculuk çubuğu ve sayaç güncellenir.

   İki incelik:
   1) Aktif adım, kartların EKRANDAKİ konumundan hesaplanamaz — sticky
      hepsini tepeye toplar. Bunun yerine kartların DOĞAL (akıştaki) konumları
      liste başlangıcı + önceki kart yükseklikleri toplamıyla bulunur.
   2) Bir kart viewport'a sığmıyorsa yapışkanlık kapatılır; ekrandan uzun bir
      sticky kartın alt kısmına scroll ile ulaşılamaz.
*/

import { ticker } from '../core/util.js';

const OFFSET_STEP = 14; // kartlar arası deste basamağı (px) — CSS ile aynı
const DEPTH_SCALE = 0.018; // her gömülme kademesinde küçülme
const MAX_DEPTH = 4;

export function initProcess(scroller) {
  const list = document.querySelector('[data-process]');
  if (!list) return;

  const steps = Array.from(list.querySelectorAll('.pstep'));
  if (!steps.length) return;

  const imgs = Array.from(document.querySelectorAll('[data-pimg]'));
  const idxOut = document.querySelector('[data-process-idx]');
  const titleOut = document.querySelector('[data-ptitle]');
  const journey = document.querySelector('.pjourney');
  const endTR = document.querySelector('[data-pend="tr"]');
  const endHU = document.querySelector('[data-pend="hu"]');

  /* Metinler adımların kendisinden okunur: içerik HTML'de tek yerde durur. */
  const meta = steps.map((el) => ({
    phase: el.querySelector('.pstep__phase')?.textContent.trim() ?? '',
    title: el.querySelector('h3')?.textContent.trim() ?? '',
  }));

  let naturalTops = [];
  let stickyTops = [];
  let flat = false;
  let active = -1;

  const remPx = () => parseFloat(getComputedStyle(document.documentElement).fontSize) || 16;

  function measure() {
    /* Sticky kapalıyken ölç: doğal konumlar ancak böyle güvenilir. */
    list.classList.add('is-measuring');

    const headerH = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--header-h')) || 72;
    const small = matchMedia('(max-width: 1000px)').matches;
    const pad = (small ? 0.7 : 1.1) * remPx();
    const stepPx = small ? 8 : OFFSET_STEP;

    const listTop = list.getBoundingClientRect().top + window.scrollY;
    const gap = parseFloat(getComputedStyle(list).rowGap) || 0;

    naturalTops = [];
    stickyTops = [];
    let acc = 0;
    let tallest = 0;
    steps.forEach((el, i) => {
      const h = el.getBoundingClientRect().height;
      naturalTops.push(listTop + acc);
      stickyTops.push(headerH + pad + i * stepPx);
      acc += h + gap;
      tallest = Math.max(tallest, h + headerH + pad + i * stepPx);
    });

    /* Yığının en alt kartı ekrana sığmıyorsa deste kapanır. */
    flat = tallest > window.innerHeight - 16;
    list.classList.toggle('is-flat', flat);
    list.classList.remove('is-measuring');
  }

  function setActive(i) {
    if (i === active) return;
    active = i;

    imgs.forEach((img, n) => img.classList.toggle('is-on', n === i));

    if (journey) journey.style.setProperty('--pj', (i / (steps.length - 1)).toFixed(3));

    const phase = meta[i].phase;
    endTR?.classList.toggle('is-on', phase.startsWith('TÜRKİYE'));
    endHU?.classList.toggle('is-on', phase.includes('MACARİSTAN'));

    if (idxOut) idxOut.textContent = String(i + 1).padStart(2, '0');
    if (titleOut) titleOut.textContent = meta[i].title;

    /* Gömülen kartlar kademeli küçülür → yığın derinliği */
    steps.forEach((el, n) => {
      const depth = flat ? 0 : Math.max(0, Math.min(MAX_DEPTH, i - n));
      el.style.setProperty('--sc', (1 - depth * DEPTH_SCALE).toFixed(4));
      el.classList.toggle('is-live', n === i);
    });
  }

  measure();
  addEventListener('resize', () => {
    measure();
    active = -1;
    scroller.remeasure();
  }, { passive: true });
  if (document.fonts) document.fonts.ready.then(measure);
  addEventListener('load', measure);

  scroller.onFrame((s) => {
    if (!naturalTops.length) return;
    let i = 0;
    if (flat) {
      /* Deste kapalıyken okuma çizgisini geçen son kart aktiftir */
      const line = innerHeight * 0.45;
      for (let n = 0; n < steps.length; n++) {
        if (steps[n].getBoundingClientRect().top <= line) i = n;
        else break;
      }
    } else {
      /* Kart, doğal konumu yapışma noktasına ulaştığında üste geçer */
      for (let n = 0; n < steps.length; n++) {
        if (s.y >= naturalTops[n] - stickyTops[n] - 8) i = n;
        else break;
      }
    }
    setActive(i);
  });

  setActive(0);
  void ticker;
}
