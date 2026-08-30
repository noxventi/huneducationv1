/* ============================================================
   Maliyet kartı

   Tasarım kararı — neden onay kutuları kaldırıldı:
   Önceki sürümde iki farklı etkileşim modeli aynı kartta duruyordu
   (üstte radyo kartları, altta onay kutuları) ve öğrenim/konaklama
   hem kontrolde hem listede tekrar ediyordu. Ayrıca "yaşam giderleri"
   veya "sağlık sigortası" gibi kalemleri kapatmak gerçek bir senaryo
   üretmiyordu — öğrenci bunları zaten ödeyecek. Sahte bir seçim
   sunmak yerine yalnız GERÇEK iki değişken kontrol edilir:
   eğitim seviyesi ve konaklama tercihi.

   Kalan kalemler salt okunur bir döküm olarak listelenir; her satırın
   alt çizgisi aynı zamanda ölçü çubuğudur ve toplam içindeki payı
   kadar dolar, böylece ayrı bir grafik olmadan dağılım görünür.

   Rakamların doğrulanması:
   Aylık kalemler 12 ay yerine ~10 aylık akademik yıl üzerinden
   hesaplanır. Bu varsayımla lisans + yurt senaryosu 8.455–13.905 €
   veriyor ve yayınlanan 8.500–14.000 € aralığıyla %1 içinde örtüşüyor.
   ============================================================ */

import { t, num, money, LANG } from '../core/i18n.js';

const AY = 10; // akademik yıl

const OGRENIM = {
  lisans: { ad: t('cost.bachelor'), deger: [3000, 5000] },
  yl: { ad: t('cost.master'), deger: [4000, 6000] },
  // Canlidaki gercek yillik ucretler: SZTE 15.800 EUR, SOTE 19.900 USD,
  // PTE 18.000 USD, dis (PTE) 18.600 EUR. USD ~0,92 ile EUR'ya cevrildi.
  tip: { ad: t('cost.medical'), adTam: t('cost.medicalFull'), deger: [15800, 18600] },
};

const KONAKLAMA = {
  yurt: { ad: t('cost.dorm'), aylik: [60, 400] },
  oda: { ad: t('cost.shared'), aylik: [320, 380] },
  studyo: { ad: t('cost.studio'), aylik: [520, 580] },
};

/* Her öğrencinin karşılaşacağı sabit kalemler. `bir` = yalnız ilk yıl. */
const SABIT = [
  { ad: t('cost.living'), alt: t('cost.livingAlt'), aylik: [300, 300] },
  { ad: t('cost.transport'), alt: t('cost.transportAlt'), aylik: [120, 120] },
  { ad: t('cost.health'), alt: t('cost.healthAlt'), yillik: [300, 300] },
  { ad: t('cost.first'), alt: t('cost.firstAlt'), yillik: [355, 405], bir: true },
];

/* Sayı ile para simgesi arasında bölünmez boşluk: dar ekranda simge tek
   başına alt satıra düşmesin. Biçim (3.000 € / €3,000) dile bağlı. */
const eur = (n) => money(n).replace(' ', ' ');
const aralik = (a, b) =>
  a === b ? eur(a) : LANG === 'tr' ? `${num(a)} – ${eur(b)}` : `${eur(a)} – ${eur(b)}`;

export function initCost() {
  const root = document.querySelector('[data-cost]');
  if (!root) return;

  const kontroller = root.querySelector('[data-cost-controls]');
  const liste = root.querySelector('[data-cost-list]');
  const toplamEl = root.querySelector('[data-cost-total]');
  const senaryoEl = root.querySelector('[data-cost-scenario]');
  const notEl = root.querySelector('[data-cost-note]');

  const durum = { seviye: 'lisans', konaklama: 'yurt' };

  /* Kontroller bir kez basılır; seçim değişince yalnız durum nitelikleri
     güncellenir. Yeniden basmak odağı kaybettiriyor ve klavyeyle
     gezinmeyi bozuyordu. */
  function kontrolCiz() {
    const grup = (etiket, alan, veri) => `
      <div class="cpickrow" role="radiogroup" aria-label="${etiket}">
        <span class="cpickrow__label">${etiket}</span>
        <div class="cpickrow__opts">
          ${Object.entries(veri)
            .map(([k, v]) => `<button type="button" role="radio" class="cpick" data-${alan}="${k}">${v.ad}</button>`)
            .join('')}
        </div>
      </div>`;
    kontroller.innerHTML =
      grup(t('cost.level'), 'clevel', OGRENIM) + grup(t('cost.stay'), 'cstay', KONAKLAMA);
  }

  /* Roving tabindex: grup içinde Tab bir kez durur, oklar seçimi taşır. */
  function kontrolSenkron() {
    kontroller.querySelectorAll('.cpick').forEach((b) => {
      const secili = b.dataset.clevel === durum.seviye || b.dataset.cstay === durum.konaklama;
      b.classList.toggle('is-on', secili);
      b.setAttribute('aria-checked', String(secili));
      b.tabIndex = secili ? 0 : -1;
    });
  }

  function kalemler() {
    const kon = KONAKLAMA[durum.konaklama];
    const og = OGRENIM[durum.seviye];
    return [
      { ad: t('cost.tuition'), alt: t('cost.tuitionAlt', { level: og.adTam ?? og.ad }), deger: og.deger },
      {
        ad: t('cost.stay'),
        alt: t('cost.stayAlt', { type: kon.ad, min: kon.aylik[0], max: kon.aylik[1] }),
        deger: [kon.aylik[0] * AY, kon.aylik[1] * AY],
      },
      ...SABIT.map((k) => ({ ...k, deger: k.aylik ? [k.aylik[0] * AY, k.aylik[1] * AY] : k.yillik })),
    ];
  }

  function ciz() {
    kontrolSenkron();
    const rows = kalemler();
    const min = rows.reduce((a, r) => a + r.deger[0], 0);
    const max = rows.reduce((a, r) => a + r.deger[1], 0);
    const toplamOrta = rows.reduce((a, r) => a + (r.deger[0] + r.deger[1]) / 2, 0);

    toplamEl.textContent = aralik(min, max);
    senaryoEl.textContent = t('cost.scenario', {
      level: OGRENIM[durum.seviye].adTam ?? OGRENIM[durum.seviye].ad,
      stay: KONAKLAMA[durum.konaklama].ad,
      m: AY,
    });

    /* Her satırın alt çizgisi toplam içindeki payı kadar dolar; oran ayrıca
       yazıyla da verilir, böylece çubuk açıklama gerektirmez. */
    liste.innerHTML = rows
      .map((r) => {
        const pay = ((r.deger[0] + r.deger[1]) / 2 / toplamOrta) * 100;
        return `
        <li class="crow" style="--pay:${pay.toFixed(1)}%">
          <span class="crow__ad">${r.ad}<em>${r.alt}</em></span>
          <span class="crow__val num-mono">${aralik(r.deger[0], r.deger[1])}<em>${t('cost.share', { p: Math.round(pay) })}</em></span>
        </li>`;
      })
      .join('');

    const ilkYil = rows.filter((r) => r.bir).reduce((a, r) => a + r.deger[1], 0);
    notEl.innerHTML =
      t('cost.note', { sum: eur(ilkYil) }) +
      (durum.seviye === 'lisans' && durum.konaklama === 'yurt'
        ? ` <span class="ccard__match">${t('cost.match')}</span>`
        : '');
  }

  function sec(btn) {
    if (btn.dataset.clevel) durum.seviye = btn.dataset.clevel;
    else if (btn.dataset.cstay) durum.konaklama = btn.dataset.cstay;
    else return false;
    ciz();
    return true;
  }

  kontroller.addEventListener('click', (e) => {
    const btn = e.target.closest('.cpick');
    if (btn) sec(btn);
  });

  kontroller.addEventListener('keydown', (e) => {
    const btn = e.target.closest('.cpick');
    if (!btn) return;
    const yon = { ArrowLeft: -1, ArrowUp: -1, ArrowRight: 1, ArrowDown: 1 }[e.key];
    const hepsi = [...btn.closest('.cpickrow__opts').children];
    let i = null;
    if (yon != null) i = (hepsi.indexOf(btn) + yon + hepsi.length) % hepsi.length;
    else if (e.key === 'Home') i = 0;
    else if (e.key === 'End') i = hepsi.length - 1;
    if (i == null) return;
    e.preventDefault();
    if (sec(hepsi[i])) hepsi[i].focus();
  });

  kontrolCiz();
  ciz();
}
