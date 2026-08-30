/* ============================================================
   catalog.js — program listeleme sayfası
   • Filtreler URL parametresine yazılır (paylaşılabilir, geri tuşu çalışır)
   • Facet sayıları anlık güncellenir; sonuç üretmeyen seçenek gizlenmez,
     sönümlenir — kullanıcı neyin neden olmadığını görür
   • Boş sonuçta kullanıcı asla çıkmaz sokakta bırakılmaz
   ============================================================ */

import { $, $$, splitWords, env, debounce } from './core/util.js';
import { scroller, initReveal } from './core/scroll.js';
import { initHeader } from './modules/header.js';
import { initDropdowns } from './modules/dropdown.js';
import { initCursor } from './modules/cursor.js';
import { initWhatsApp } from './modules/whatsapp.js';
import { PROGRAMLAR, UNIVERSITELER, SEHIRLER, ALANLAR, SEVIYELER, uniById,
         yillikEur, ucretMetni, sureMetni, baslangicMetni, sonBasvuruMetni,
         sinavMetni, dilMetni, programUrl, universiteUrl } from '../data/catalog.js';
import { t, LOCALE } from './core/i18n.js';

document.documentElement.classList.add('js-on');

/* Bütçe bandı, programın GİRİŞ (alt sınır) ücretinden türetilir; dönemlik
   tutarlar yıllığa çevrilir (×2, bkz. yillikGiris). Bant büyüklüğe göre
   hesaplandığı için filtre "yaklaşık"tır; kesin tutar her zaman kartın
   üzerinde para birimi ve dönemiyle birlikte yazılıdır. */
const BUTCE = {
  dusuk: t('budget.low'),
  orta: t('budget.mid'),
  yuksek: t('budget.high'),
};

function butceBandi(p) {
  // Ucret YILLIKTIR; USD kayitlar yaklasik EUR'ya cevrilir (bkz. yillikEur).
  const y = yillikEur(p);
  if (y == null) return null;
  if (y < 5000) return 'dusuk';
  if (y <= 10000) return 'orta';
  return 'yuksek';
}

const FACETS = {
  seviye: { label: t('facet.seviye'), options: () => Object.entries(SEVIYELER) },
  alan: { label: t('facet.alan'), options: () => Object.entries(ALANLAR) },
  sehir: { label: t('facet.sehir'), options: () => Object.entries(SEHIRLER).map(([k, v]) => [k, v.ad]) },
  uni: { label: t('facet.uni'), options: () => UNIVERSITELER.map((u) => [String(u.id), u.ad]) },
  butce: { label: t('facet.butce'), options: () => Object.entries(BUTCE) },
};

const state = { q: '', sort: 'alpha' };
Object.keys(FACETS).forEach((k) => (state[k] = new Set()));

/* Bir programın facet değeri */
const valueOf = (p, facet) => {
  if (facet === 'sehir') return p.sehir ?? uniById(p.uni)?.sehir;
  if (facet === 'uni') return String(p.uni);
  if (facet === 'butce') return butceBandi(p);
  return p[facet];
};

/* `skip` verilen facet hariç tüm filtreleri uygular → doğru facet sayıları */
function filtered(skip) {
  const q = state.q.trim().toLocaleLowerCase(LOCALE);
  return PROGRAMLAR.filter((p) => {
    if (q) {
      const u = uniById(p.uni);
      /* Arama iki dilde birden yapılır: Türkçe arayüzde "Semmelweis
         University" yazan da bulsun, İngilizce arayüzde "Tıp" yazan da. */
      const hay = `${p.ad} ${u?.ad ?? ''} ${ALANLAR[p.alan] ?? ''} ${SEVIYELER[p.seviye] ?? ''}`.toLocaleLowerCase(LOCALE);
      if (!hay.includes(q)) return false;
    }
    for (const facet of Object.keys(FACETS)) {
      if (facet === skip) continue;
      const sel = state[facet];
      if (sel.size && !sel.has(valueOf(p, facet))) return false;
    }
    return true;
  });
}

/* ------------------------------------------------------------
   URL senkronizasyonu
   ------------------------------------------------------------ */
function readURL() {
  const q = new URLSearchParams(location.search);
  state.q = q.get('q') || '';
  for (const facet of Object.keys(FACETS)) {
    state[facet] = new Set((q.get(facet) || '').split(',').filter(Boolean));
  }
  if (q.get('sirala')) state.sort = q.get('sirala');
}

function writeURL(push = false) {
  const q = new URLSearchParams();
  if (state.q) q.set('q', state.q);
  for (const facet of Object.keys(FACETS)) {
    if (state[facet].size) q.set(facet, [...state[facet]].join(','));
  }
  if (state.sort !== 'alpha') q.set('sirala', state.sort);
  const url = location.pathname + (q.toString() ? '?' + q : '');
  history[push ? 'pushState' : 'replaceState'](null, '', url);
}

/* ------------------------------------------------------------
   Çizim
   ------------------------------------------------------------ */
const el = {
  results: $('[data-results]'),
  count: $('[data-count]'),
  countWrap: $('.cat__count'),
  countNote: $('[data-count-note]'),
  active: $('[data-active-filters]'),
  activeList: $('.cat__active-list'),
  emptyTpl: $('[data-empty-template]'),
};

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);

/* Doğrulanmamış alan → gizleme, "sor" göster (PRD §7.4) */
const val = (v) => (v == null || v === '' ? `<span class="ask">${t('card.ask')}</span>` : esc(v));

function programCard(p, i) {
  const u = uniById(p.uni);
  const sehir = SEHIRLER[u?.sehir]?.ad ?? '';
  /* Canlıdaki program/üniversite sayfasına köprü. Katalog bu
     sayfaların hub'ıdır; link yoksa kart düz metin kalır. */
  const purl = programUrl(p);
  const uurl = universiteUrl(u);
  return `
  <li class="pcard" style="--i:${i}">
    <div class="pcard__top">
      <span class="pcard__lvl">${esc(SEVIYELER[p.seviye] ?? p.seviye)}</span>
      <span class="pcard__area">${esc(ALANLAR[p.alan] ?? p.alan)}</span>
    </div>
    <h3 class="pcard__name">${purl
      ? `<a href="${purl}">${esc(p.ad)}</a>`
      : esc(p.ad)}</h3>
    <p class="pcard__uni">${uurl
      ? `<a href="${uurl}">${esc(u?.ad ?? '')}</a>`
      : esc(u?.ad ?? '')} <em>${esc(sehir)}</em></p>

    <dl class="pcard__facts">
      <div><dt>${t('card.lang')}</dt><dd>${val(dilMetni(p))}</dd></div>
      <div><dt>${t('card.duration')}</dt><dd>${val(sureMetni(p))}</dd></div>
      <div><dt>${t('card.intake')}</dt><dd>${val(baslangicMetni(p))}</dd></div>
      <div><dt>${t('card.deadline')}</dt><dd>${val(sonBasvuruMetni(p))}</dd></div>
      <div><dt>${t('card.fee')}</dt><dd>${val(ucretMetni(p))}</dd></div>
    </dl>

    ${sinavMetni(p) ? `<p class="pcard__exam"><b>${t('card.exam')}</b> ${esc(sinavMetni(p))}</p>` : ''}

    <div class="pcard__cta">
      ${purl ? `<a class="link pcard__more" href="${purl}">${t('card.detail')}</a>` : ''}
      <a class="btn btn--dark btn--sm" href="index.html#gorusme">
        <span class="btn__label"><span data-t="${t('card.cta')}">${t('card.cta')}</span></span>
      </a>
    </div>
  </li>`;
}

const SORTERS = {
  alpha: (a, b) => a.ad.localeCompare(b.ad, LOCALE),
  uni: (a, b) => (uniById(a.uni)?.ad ?? '').localeCompare(uniById(b.uni)?.ad ?? '', LOCALE) || a.ad.localeCompare(b.ad, LOCALE),
  ucret: (a, b) => (yillikEur(a) ?? 1e9) - (yillikEur(b) ?? 1e9),
  seviye: (a, b) => Object.keys(SEVIYELER).indexOf(a.seviye) - Object.keys(SEVIYELER).indexOf(b.seviye) || a.ad.localeCompare(b.ad, LOCALE),
};

let lastCount = -1;

function render() {
  const list = filtered().sort(SORTERS[state.sort] || SORTERS.alpha);

  /* Sonuç sayısı — değiştiğinde kısa bir vurgu */
  el.count.textContent = list.length;
  if (lastCount !== -1 && lastCount !== list.length && !env.reduce) {
    el.countWrap.classList.add('is-bump');
    setTimeout(() => el.countWrap.classList.remove('is-bump'), 380);
  }
  lastCount = list.length;

  const anyFilter = state.q || Object.keys(FACETS).some((f) => state[f].size);
  el.countNote.textContent = anyFilter
    ? t('results.filtered', { n: PROGRAMLAR.length })
    : t('results.all');

  el.results.innerHTML = list.length
    ? list.map(programCard).join('')
    : el.emptyTpl.innerHTML;

  renderActive(anyFilter);
  renderFacetCounts();
  bindEmptyActions();
}

function renderActive(anyFilter) {
  el.active.hidden = !anyFilter;
  if (!anyFilter) return;

  const tags = [];
  if (state.q) tags.push({ facet: 'q', value: '', label: `"${state.q}"` });
  for (const [facet, def] of Object.entries(FACETS)) {
    const opts = Object.fromEntries(def.options());
    for (const v of state[facet]) tags.push({ facet, value: v, label: opts[v] ?? v });
  }

  el.activeList.innerHTML = tags
    .map(
      (tag) => `<span class="tagx"><b>${esc(tag.label)}</b>
        <button type="button" data-remove-facet="${tag.facet}" data-remove-value="${esc(tag.value)}"
          aria-label="${esc(t('results.remove', { label: tag.label }))}">
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
        </button></span>`
    )
    .join('');
}

function renderFacetCounts() {
  for (const facet of Object.keys(FACETS)) {
    const pool = filtered(facet);
    const counts = new Map();
    for (const p of pool) {
      const v = valueOf(p, facet);
      counts.set(v, (counts.get(v) || 0) + 1);
    }
    $$(`[data-facet="${facet}"] .fchip`).forEach((chip) => {
      const n = counts.get(chip.dataset.value) || 0;
      chip.querySelector('.fchip__n').textContent = n;
      chip.dataset.empty = String(n === 0 && !state[facet].has(chip.dataset.value));
    });
  }
}

function bindEmptyActions() {
  el.results.querySelectorAll('[data-clear-all]').forEach((b) => b.addEventListener('click', clearAll));
}

function clearAll() {
  state.q = '';
  Object.keys(FACETS).forEach((f) => state[f].clear());
  const search = $('#q');
  if (search) search.value = '';
  $$('.fchip').forEach((c) => c.setAttribute('aria-pressed', 'false'));
  writeURL(true);
  render();
}

/* ------------------------------------------------------------
   Kurulum
   ------------------------------------------------------------ */
function buildFacets() {
  for (const [facet, def] of Object.entries(FACETS)) {
    const box = $(`[data-facet="${facet}"] .fchips`);
    if (!box) continue;
    box.innerHTML = def
      .options()
      .map(
        ([value, label]) => `
        <button class="fchip" type="button" data-facet-key="${facet}" data-value="${esc(value)}"
          aria-pressed="${state[facet].has(value)}">
          <span>${esc(label)}</span><span class="fchip__n">0</span>
        </button>`
      )
      .join('');
  }
}

function boot() {
  readURL();
  buildFacets();

  $$('[data-split]').forEach((e) => splitWords(e));
  $$('.split-mask').forEach((e) => e.classList.add('is-in'));

  initHeader(scroller);
  initDropdowns();
  initWhatsApp();
  initReveal();
  if (!env.touch && !env.reduce) initCursor();

  /* Arama */
  const search = $('#q');
  if (search) {
    search.value = state.q;
    search.addEventListener(
      'input',
      debounce(() => {
        state.q = search.value;
        writeURL();
        render();
        pushEvent('program_search', { search_term: state.q });
      }, 180)
    );
  }

  /* Facet çipleri */
  document.addEventListener('click', (e) => {
    const chip = e.target.closest('.fchip');
    if (chip) {
      const facet = chip.dataset.facetKey;
      const value = chip.dataset.value;
      const on = state[facet].has(value);
      on ? state[facet].delete(value) : state[facet].add(value);
      chip.setAttribute('aria-pressed', String(!on));
      writeURL(true);
      render();
      pushEvent('filter_apply', { filter_name: facet, filter_value: value });
      return;
    }

    const rm = e.target.closest('[data-remove-facet]');
    if (rm) {
      const facet = rm.dataset.removeFacet;
      if (facet === 'q') {
        state.q = '';
        if (search) search.value = '';
      } else {
        state[facet].delete(rm.dataset.removeValue);
        const c = document.querySelector(`.fchip[data-facet-key="${facet}"][data-value="${CSS.escape(rm.dataset.removeValue)}"]`);
        c?.setAttribute('aria-pressed', 'false');
      }
      writeURL(true);
      render();
      return;
    }

    if (e.target.closest('[data-clear-all]')) clearAll();
  });

  /* Sıralama */
  const sort = $('[data-sort]');
  if (sort) {
    sort.value = state.sort;
    sort.addEventListener('change', () => {
      state.sort = sort.value;
      writeURL();
      render();
    });
  }

  /* Mobil filtre çekmecesi */
  const setDrawer = (open) => {
    document.body.classList.toggle('filters-open', open);
    document.body.classList.toggle('is-locked', open);
  };
  $('[data-filter-open]')?.addEventListener('click', () => setDrawer(true));
  $('[data-filter-close]')?.addEventListener('click', () => setDrawer(false));
  $('[data-filter-apply]')?.addEventListener('click', () => setDrawer(false));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') setDrawer(false);
  });

  /* Geri/ileri tuşu filtreleri bozmaz */
  addEventListener('popstate', () => {
    readURL();
    if (search) search.value = state.q;
    $$('.fchip').forEach((c) =>
      c.setAttribute('aria-pressed', String(state[c.dataset.facetKey].has(c.dataset.value)))
    );
    if (sort) sort.value = state.sort;
    render();
  });

  const y = $('[data-year]');
  if (y) y.textContent = new Date().getFullYear();

  render();
}

function pushEvent(event, params) {
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({ event, ...params });
}

if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot, { once: true });
else boot();
