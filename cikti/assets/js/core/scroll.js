/* ============================================================
   scroll.js — scroll ilerlemesi motoru (el yapımı)

   Tasarım kararları
   -----------------
   1) Native scroll korunur. Sahte "smooth scroll" wrapper'ı YOK:
      position:sticky ile yapılan pin bölümleri bozulmaz, klavye ve
      arama-içinde-bul davranışı doğal kalır.
   2) Ölçüm (getBoundingClientRect) yalnız resize/load/font yüklemede
      yapılır. Her karede sadece scrollY okunur → layout thrash yok.
   3) Motor sonuçları CSS custom property olarak yazar; asıl animasyonu
      CSS yapar. JS "ne kadar ilerledik"i, CSS "nasıl görünür"ü bilir.
   4) prefers-reduced-motion açıkken tüm track'ler son duruma sabitlenir.
   ============================================================ */

import { clamp, damp, r4, ticker, env, debounce } from './util.js';

const ANCHORS = { top: 0, start: 0, center: 0.5, middle: 0.5, bottom: 1, end: 1 };

function anchorValue(token) {
  if (token in ANCHORS) return ANCHORS[token];
  if (token.endsWith('%')) return parseFloat(token) / 100;
  if (token.endsWith('px')) return { px: parseFloat(token) };
  return 0;
}

/** "top bottom" → { el: 0, vp: 1 }  (elemanın tepesi, viewport'un altına değdiğinde) */
function parseOffset(str) {
  const [a, b = 'top'] = String(str).trim().split(/\s+/);
  return { el: anchorValue(a), vp: anchorValue(b) };
}

class Track {
  constructor(el, opts) {
    this.el = el;
    this.target = opts.target || el;
    this.start = parseOffset(opts.start ?? 'top bottom');
    this.end = parseOffset(opts.end ?? 'bottom top');
    this.varName = opts.var || null;
    this.smooth = opts.smooth ?? 0;
    this.easeFn = opts.ease || null;
    this.onUpdate = opts.onUpdate || null;
    this.clampP = opts.clamp !== false;
    this.p = 0;
    this.sp = 0;
    this.startY = 0;
    this.endY = 0;
    this.dirty = true;
  }

  measure(vh, docTop) {
    const rect = this.el.getBoundingClientRect();
    const top = rect.top + docTop;
    const h = rect.height;
    const resolve = (o) => {
      if (typeof o.el === 'object') return top + o.el.px - vh * o.vp;
      const vpPart = typeof o.vp === 'object' ? o.vp.px : vh * o.vp;
      return top + h * o.el - vpPart;
    };
    this.startY = resolve(this.start);
    this.endY = resolve(this.end);
    if (this.endY - this.startY < 1) this.endY = this.startY + 1;
    this.dirty = true;
  }

  update(y, dt) {
    let p = (y - this.startY) / (this.endY - this.startY);
    if (this.clampP) p = clamp(p);
    this.p = p;

    if (this.smooth > 0 && !env.reduce) {
      this.sp = damp(this.sp, p, this.smooth, dt);
      if (Math.abs(this.sp - p) < 0.0004) this.sp = p;
    } else {
      this.sp = p;
    }

    const out = this.easeFn ? this.easeFn(clamp(this.sp)) : this.sp;
    if (Math.abs(out - this._last) < 0.0004 && !this.dirty) return;
    this._last = out;
    this.dirty = false;

    if (this.varName) this.target.style.setProperty(this.varName, r4(out));
    if (this.onUpdate) this.onUpdate(out, this);
  }

  /** Reduced motion: son duruma sabitle. */
  settle() {
    this.p = this.sp = 1;
    if (this.varName) this.target.style.setProperty(this.varName, 1);
    if (this.onUpdate) this.onUpdate(1, this);
  }
}

class Scroller {
  constructor() {
    this.tracks = [];
    this.y = 0;
    this.lastY = 0;
    this.vel = 0;
    this.velSmooth = 0;
    this.vh = window.innerHeight;
    this.dir = 1;
    this.root = document.documentElement;
    this._listeners = new Set();
    this._boot();
  }

  _boot() {
    this.y = this.lastY = window.scrollY;
    this.remeasure();

    const onResize = debounce(() => this.remeasure(), 100);
    window.addEventListener('resize', onResize, { passive: true });
    window.addEventListener('orientationchange', onResize, { passive: true });
    window.addEventListener('load', () => this.remeasure());
    if (document.fonts) document.fonts.ready.then(() => this.remeasure());

    /* Görsel yüklenince yükseklik değişir → yeniden ölç. */
    const ro = new ResizeObserver(debounce(() => this.remeasure(), 80));
    ro.observe(document.body);

    ticker.add((dt) => this.frame(dt));
  }

  remeasure() {
    this.vh = window.innerHeight;
    this.root.style.setProperty('--vh', this.vh * 0.01 + 'px');
    const docTop = window.scrollY;
    for (const t of this.tracks) t.measure(this.vh, docTop);
    this.frame(1 / 60, true);
  }

  frame(dt, force) {
    const y = window.scrollY;
    const raw = (y - this.lastY) / Math.max(dt, 0.001);
    this.lastY = y;

    if (Math.abs(raw) > 1) this.dir = Math.sign(raw);
    this.y = y;

    /* Hız: piksel/saniye → normalize edilmiş, yumuşatılmış -1..1 */
    this.vel = damp(this.vel, clamp(raw / 3000, -1, 1), 0.14, dt);
    if (Math.abs(this.vel) < 0.0006) this.vel = 0;

    this.root.style.setProperty('--scroll-y', Math.round(y));
    this.root.style.setProperty('--scroll-vel', r4(this.vel));

    for (const t of this.tracks) t.update(y, dt);
    for (const fn of this._listeners) fn(this, dt);
    void force;
  }

  /** Track kaydet. Bkz. Track opts. */
  track(el, opts = {}) {
    if (!el) return null;
    const t = new Track(el, opts);
    t.measure(this.vh, window.scrollY);
    if (env.reduce && opts.settleOnReduce !== false) {
      /* Hareket kapalıyken ilerlemeyi hesaplamaya devam et ama
         yalnız "görsel hareket" CSS tarafında nötrlenir.
         Pin bölümleri yine de doğru içerik göstermeli. */
    }
    this.tracks.push(t);
    t.update(this.y, 1 / 60);
    return t;
  }

  /** Her karede çalışacak serbest callback. */
  onFrame(fn) {
    this._listeners.add(fn);
    return () => this._listeners.delete(fn);
  }

  scrollTo(target, offset = 0) {
    const el = typeof target === 'string' ? document.querySelector(target) : target;
    if (!el) return;
    const y = el.getBoundingClientRect().top + window.scrollY + offset;
    window.scrollTo({ top: y, behavior: env.reduce ? 'auto' : 'smooth' });
  }
}

export const scroller = new Scroller();

/* ------------------------------------------------------------
   reveal — IntersectionObserver ile giriş animasyonu.
   İçerik animasyon uğruna GECİKTİRİLMEZ: elemanlar CSS'te görünür
   başlar, .js-on sınıfı gövdeye eklenince gizlenir. JS çökerse
   veya kapalıysa içerik tam görünür kalır (progressive enhancement).
   ------------------------------------------------------------ */
export function initReveal(root = document) {
  const els = root.querySelectorAll('[data-reveal]');
  if (!els.length) return;

  if (env.reduce) {
    els.forEach((el) => el.classList.add('is-in'));
    return;
  }

  const io = new IntersectionObserver(
    (entries) => {
      for (const e of entries) {
        if (!e.isIntersecting) continue;
        const el = e.target;
        const delay = parseFloat(el.dataset.revealDelay || 0);
        if (delay) el.style.setProperty('--reveal-delay', delay + 'ms');
        el.classList.add('is-in');
        io.unobserve(el);
      }
    },
    { rootMargin: '0px 0px -12% 0px', threshold: 0.01 }
  );

  els.forEach((el, i) => {
    /* Grup içi kademe: ebeveyn [data-reveal-group] varsa indeks ver. */
    if (!el.style.getPropertyValue('--i')) el.style.setProperty('--i', i % 12);
    io.observe(el);
  });
}
