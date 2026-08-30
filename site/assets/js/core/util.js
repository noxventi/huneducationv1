/* ============================================================
   util.js — matematik, easing ve tek rAF döngüsü
   Harici animasyon kütüphanesi kullanılmaz; her şey burada.
   ============================================================ */

export const clamp = (v, a = 0, b = 1) => (v < a ? a : v > b ? b : v);

export const lerp = (a, b, t) => a + (b - a) * t;

/** Kare hızından bağımsız yumuşatma (60fps'te t katsayısına eşdeğer). */
export const damp = (a, b, t, dt) => lerp(a, b, 1 - Math.pow(1 - t, dt * 60));

/** a..b aralığını 0..1'e taşır. */
export const norm = (v, a, b) => (b - a === 0 ? 0 : (v - a) / (b - a));

/** Bir aralıktan diğerine eşle, sınırlandırılmış. */
export const mapRange = (v, a, b, c, d) => lerp(c, d, clamp(norm(v, a, b)));

/** Girişe/çıkışa yumuşak geçiş penceresi: 0→1→0 */
export const window01 = (p, fadeIn = 0.15, fadeOut = 0.15) =>
  Math.min(clamp(p / fadeIn), clamp((1 - p) / fadeOut));

export const ease = {
  linear: (t) => t,
  outQuad: (t) => 1 - (1 - t) * (1 - t),
  inOutQuad: (t) => (t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2),
  outCubic: (t) => 1 - Math.pow(1 - t, 3),
  inOutCubic: (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
  outQuart: (t) => 1 - Math.pow(1 - t, 4),
  outQuint: (t) => 1 - Math.pow(1 - t, 5),
  /* Uzun scroll mesafelerinde en doğal duran eğri */
  outExpo: (t) => (t === 1 ? 1 : 1 - Math.pow(2, -10 * t)),
  inOutExpo: (t) =>
    t === 0 ? 0 : t === 1 ? 1 : t < 0.5 ? Math.pow(2, 20 * t - 10) / 2 : (2 - Math.pow(2, -20 * t + 10)) / 2,
  outBack: (t) => 1 + 2.7 * Math.pow(t - 1, 3) + 1.7 * Math.pow(t - 1, 2),
  outElastic: (t) =>
    t === 0 ? 0 : t === 1 ? 1 : Math.pow(2, -9 * t) * Math.sin((t * 10 - 0.75) * ((2 * Math.PI) / 3)) + 1,
};

/* ------------------------------------------------------------
   Tek merkezi rAF döngüsü.
   Tüm modüller buraya abone olur → sayfada yalnız bir animasyon
   kalbi çalışır, okuma/yazma sırası kontrol edilebilir.
   ------------------------------------------------------------ */
class Ticker {
  constructor() {
    this.subs = new Set();
    this.running = false;
    this.last = 0;
    this.frame = this.frame.bind(this);
  }
  add(fn) {
    this.subs.add(fn);
    this.start();
    return () => this.subs.delete(fn);
  }
  start() {
    if (this.running) return;
    this.running = true;
    this.last = performance.now();
    requestAnimationFrame(this.frame);
  }
  stop() {
    this.running = false;
  }
  frame(now) {
    if (!this.running) return;
    /* dt'yi sınırla: sekme arkaplandan dönünce sıçrama olmasın */
    const dt = Math.min((now - this.last) / 1000, 1 / 20);
    this.last = now;
    for (const fn of this.subs) fn(dt, now);
    requestAnimationFrame(this.frame);
  }
}
export const ticker = new Ticker();

/* Sekme gizliyken kalbi durdur (pil + CPU). */
document.addEventListener('visibilitychange', () => {
  if (document.hidden) ticker.stop();
  else ticker.start();
});

/* ------------------------------------------------------------
   Ortam
   ------------------------------------------------------------ */
const mqReduce = matchMedia('(prefers-reduced-motion: reduce)');
const mqCoarse = matchMedia('(hover: none), (pointer: coarse)');

export const env = {
  get reduce() {
    return mqReduce.matches;
  },
  get touch() {
    return mqCoarse.matches;
  },
};

export const onReduceChange = (fn) => mqReduce.addEventListener('change', fn);

/* ------------------------------------------------------------
   Küçük yardımcılar
   ------------------------------------------------------------ */
export const $ = (sel, root = document) => root.querySelector(sel);
export const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

export const setVar = (el, name, value) => el.style.setProperty(name, value);

/** Sayıyı CSS'e yazarken 4 hane yeterli — gereksiz reflow metni azalır. */
export const r4 = (n) => Math.round(n * 10000) / 10000;

/** Türkçe sayı biçimi. */
export const fmtTR = (n, opts) => new Intl.NumberFormat('tr-TR', opts).format(n);

/** Basit debounce. */
export function debounce(fn, wait = 120) {
  let t;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), wait);
  };
}

/** Bir metni harflere/kelimelere bölerek animasyon için sarmalar. */
export function splitWords(el, { chars = false } = {}) {
  const source = el.dataset.splitSource || el.textContent;
  el.dataset.splitSource = source;
  const words = source.split(/(\s+)/);
  el.textContent = '';
  const out = [];
  let i = 0;
  for (const w of words) {
    /* Girintili HTML'de kaynak metin boşlukla başlayıp bittiği için
       split() baş ve sonda boş token üretir. Sarmalanırlarsa scrub
       animasyonu ilk ve son adımda hiçbir şeyi aydınlatmaz. */
    if (w === '') continue;
    if (/^\s+$/.test(w)) {
      el.appendChild(document.createTextNode(w));
      continue;
    }
    const wrap = document.createElement('span');
    wrap.className = 'sw';
    const inner = document.createElement('span');
    inner.className = 'sw-i';
    inner.style.setProperty('--i', i++);
    if (chars) {
      for (const c of w) {
        const cs = document.createElement('span');
        cs.className = 'sc';
        cs.textContent = c;
        inner.appendChild(cs);
      }
    } else {
      inner.textContent = w;
    }
    wrap.appendChild(inner);
    el.appendChild(wrap);
    out.push(inner);
  }
  el.style.setProperty('--n', i);
  return out;
}
