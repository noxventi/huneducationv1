/* Macaristan haritası: şehir seçimi → o şehirdeki üniversiteler.
   Fare, dokunma ve klavye ile çalışır; harita yolu scroll ile çizilir. */

import { SEHIRLER, UNIVERSITELER, ALANLAR } from '../../data/catalog.js';
import { t, ROUTES } from '../core/i18n.js';
import { scroller } from '../core/scroll.js';

export function initMap() {
  const wrap = document.querySelector('[data-map]');
  const panel = document.querySelector('[data-map-panel]');
  if (!wrap || !panel) return;

  const pins = Array.from(wrap.querySelectorAll('.pin'));

  /* Sınır çizgisi scroll ile çizilir — dash uzunluğu gerçek yol uzunluğundan */
  const shape = wrap.querySelector('.hu-map__shape');
  if (shape) {
    try {
      wrap.style.setProperty('--len', Math.ceil(shape.getTotalLength()));
    } catch {
      /* getTotalLength desteklenmiyorsa CSS varsayılanı kullanılır */
    }
  }
  scroller.track(wrap, { start: 'top 88%', end: 'top 35%', var: '--mp', smooth: 0.14 });

  /* Mobil şehir seçici.
     Haritadaki pinler 375 px genişlikte yaklaşık 20 px'lik dokunma hedefine
     düşüyor — parmakla isabetli seçilemez ve komşu şehirler (Dunaújváros /
     Kecskemét) yan yana. Bu yüzden küçük ekranda harita GÖRSEL kalır,
     seçim bu yatay çip şeridinden yapılır. */
  const chipBar = document.querySelector('[data-map-chips]');
  let chips = [];
  if (chipBar) {
    chipBar.innerHTML = pins
      .map((p) => {
        const c = p.dataset.city;
        return `<button class="mchip" type="button" data-mchip="${c}">${SEHIRLER[c]?.ad ?? c}</button>`;
      })
      .join('');
    chips = Array.from(chipBar.querySelectorAll('.mchip'));
    chips.forEach((b) => b.addEventListener('click', () => select(b.dataset.mchip)));
  }

  /* Çipler devredeyken haritadaki pinler tıklanamaz (pointer-events:none).
     Odaklanabilir ama tıklanamaz bir kontrol bırakmamak için klavye ve
     ekran okuyucu erişimi de çiplere devredilir. */
  const mq = matchMedia('(max-width: 900px)');
  const syncPinA11y = () => {
    const mobil = mq.matches && chips.length > 0;
    pins.forEach((p) => {
      p.setAttribute('tabindex', mobil ? '-1' : '0');
      if (mobil) p.setAttribute('aria-hidden', 'true');
      else p.removeAttribute('aria-hidden');
    });
    wrap.querySelector('.hu-map')?.setAttribute('aria-hidden', mobil ? 'true' : 'false');
  };
  mq.addEventListener('change', syncPinA11y);
  syncPinA11y();

  function select(city, { focus = false } = {}) {
    pins.forEach((p) => p.classList.toggle('is-active', p.dataset.city === city));
    chips.forEach((b) => {
      const on = b.dataset.mchip === city;
      b.classList.toggle('is-on', on);
      b.setAttribute('aria-pressed', String(on));
      /* Seçili çip görünür alana kaysın */
      if (on && chipBar.scrollWidth > chipBar.clientWidth) {
        chipBar.scrollTo({ left: b.offsetLeft - chipBar.clientWidth / 2 + b.offsetWidth / 2, behavior: 'smooth' });
      }
    });
    paint(city);
    if (focus) wrap.querySelector(`.pin[data-city="${city}"]`)?.focus();
  }

  function paint(city) {
    const s = SEHIRLER[city];
    if (!s) return;
    const unis = UNIVERSITELER.filter((u) => u.sehir === city);

    panel.innerHTML = `
      <div class="upanel__city">
        <h3>${s.ad}</h3>
        <span><b class="upanel__count">${unis.length} üniversite</b> · ${s.bolge}</span>
      </div>
      <p class="upanel__note">${s.not}</p>
      <div class="upanel__list">
        ${unis
          .map(
            (u) => `
          <a class="ucard" href="${ROUTES.programs}?uni=${u.id}">
            <span class="ucard__name">${u.ad}</span>
            <span class="ucard__meta">
              <span>${u.turAdi}</span>
              <span>${u.alanlar.map((a) => ALANLAR[a]?.split(' ')[0] ?? a).join(' · ')}</span>
            </span>
          </a>`
          )
          .join('')}
      </div>
      <div class="upanel__cta">
        <a class="btn btn--ghost btn--sm" href="${ROUTES.programs}?sehir=${city}">
          <span class="btn__label"><span data-t="${t('map.cityCta', { city: s.ad })}">${t('map.cityCta', { city: s.ad })}</span></span>
        </a>
      </div>`;

    /* Şehir değişince liste başa dönsün — önceki şehrin kaydırma
       konumu yenisine taşınmasın */
    panel.querySelector('.upanel__list')?.scrollTo?.(0, 0);

    /* Giriş animasyonunu yeniden tetikle */
    panel.classList.remove('upanel-anim');
    void panel.offsetWidth;
    panel.classList.add('upanel-anim');
  }

  pins.forEach((pin) => {
    const city = pin.dataset.city;

    /* Dokunma hedefini büyüt (min 44×44 CSS px karşılığı) — görünmez daire */
    const hit = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    hit.setAttribute('r', '30');
    hit.setAttribute('fill', 'transparent');
    pin.insertBefore(hit, pin.firstChild);

    pin.addEventListener('click', () => select(city));
    pin.addEventListener('mouseenter', () => select(city));
    pin.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        select(city);
      }
      const dir = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
      if (dir) {
        e.preventDefault();
        const i = (pins.indexOf(pin) + dir + pins.length) % pins.length;
        select(pins[i].dataset.city, { focus: true });
      }
    });
  });

  select('budapest');
}
