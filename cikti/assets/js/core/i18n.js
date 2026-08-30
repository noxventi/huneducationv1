/* ============================================================
   i18n.js — arayüz metinlerinin dil katmanı

   Site iki dilde yayınlanıyor: İngilizce kök dizinde, Türkçe /tr/
   altında. Her dil için ayrı bir JS kopyası tutmak yerine tek kaynak
   var; dil `<html lang>` niteliğinden okunuyor. Böylece bir metin
   düzeltmesi tek yerde yapılır ve iki dil sürüklenemez.

   Neden sözlük dosyası, neden `data-i18n` değil:
   HTML'deki metinler statik olarak üretiliyor (gen_pages.py) ve
   crawlable olmak zorunda; JS ile yerine koyulan metin SEO için
   risklidir. Burası yalnız JS'in RUNTIME'da ürettiği arayüz
   metinlerini (filtre etiketleri, form hataları, kart alanları)
   kapsar — sayfa içeriğini değil.
   ============================================================ */

export const LANG = document.documentElement.lang?.toLowerCase().startsWith('tr') ? 'tr' : 'en';
export const IS_TR = LANG === 'tr';

/* Sıralama ve karşılaştırma için BCP-47 etiketi. Türkçe'de i/ı ayrımı
   ve ö/ü sıralaması İngilizce collation'dan farklı; localeCompare ve
   toLocaleLowerCase bu etikete bağlı. */
export const LOCALE = IS_TR ? 'tr-TR' : 'en-GB';

/* Dosya adları dile göre değişiyor (İngilizce slug SEO'da anahtar kelime
   taşır). İki dil ağacı da kendi dizininde kapalı olduğu için göreli
   dosya adı yeterli; yalnız temel ad farklı. JS'in ürettiği bağlantılar
   buradan okunur, elle yazılmaz. */
export const ROUTES = IS_TR
  ? { home: 'index.html', programs: 'kurslar.html', universities: 'macaristan-universiteleri.html' }
  : { home: 'index.html', programs: 'courses.html', universities: 'universities.html' };

const DICT = {
  /* ---------- Program kataloğu (catalog.js) ---------- */
  'facet.seviye': { en: 'Level', tr: 'Seviye' },
  'facet.alan': { en: 'Field', tr: 'Alan' },
  'facet.sehir': { en: 'City', tr: 'Şehir' },
  'facet.uni': { en: 'University', tr: 'Üniversite' },
  'facet.dil': { en: 'Language', tr: 'Dil' },
  'facet.butce': { en: 'Annual budget', tr: 'Yıllık bütçe' },

  'lang.en': { en: 'English', tr: 'İngilizce' },
  'lang.hu': { en: 'Hungarian', tr: 'Macarca' },

  'budget.low': { en: 'Under €5,000', tr: '5.000 € altı' },
  'budget.mid': { en: '€5,000 – €10,000', tr: '5.000 – 10.000 €' },
  'budget.high': { en: 'Over €10,000', tr: '10.000 € üzeri' },

  'card.lang': { en: 'Language of instruction', tr: 'Eğitim dili' },
  'card.duration': { en: 'Duration', tr: 'Süre' },
  'card.intake': { en: 'Intake', tr: 'Başlangıç dönemi' },
  'card.deadline': { en: 'Application deadline', tr: 'Son başvuru' },
  'card.fee': { en: 'Annual tuition', tr: 'Yıllık ücret' },
  'card.exam': { en: 'Entrance exam / interview:', tr: 'Sınav/mülakat:' },
  'card.cta': { en: 'Check My Eligibility', tr: 'Uygunluğumu Değerlendirin' },
  'card.ask': { en: 'ask an adviser', tr: 'danışmana sorun' },

  'results.filtered': { en: 'filtered from {n} records', tr: '{n} kayıt içinde filtrelendi' },
  'results.all': { en: 'verified catalogue records', tr: 'doğrulanmış katalog kaydı' },
  'results.remove': { en: 'Remove {label} filter', tr: '{label} filtresini kaldır' },

  /* ---------- Program bulucu (finder.js) ---------- */
  'finder.start': { en: 'Start by choosing the first step.', tr: 'İlk adımı seçerek başlayın.' },

  /* ---------- Harita (map.js) ---------- */
  'map.cityCta': { en: 'See programmes in {city}', tr: '{city} programlarını gör' },

  /* ---------- Form (form.js) ---------- */
  'form.name': { en: 'Please enter your full name.', tr: 'Lütfen ad ve soyadınızı yazın.' },
  'form.tel': {
    en: 'Enter your phone number with the country code. Example: +44 7700 900000',
    tr: 'Telefonu ülke koduyla yazın. Örnek: +90 532 000 00 00',
  },
  'form.mail': { en: 'Enter a valid email address.', tr: 'Geçerli bir e-posta adresi girin.' },
  'form.consent': {
    en: 'You need to accept the privacy notice to continue.',
    tr: 'Devam etmek için aydınlatma metnini onaylamanız gerekiyor.',
  },

  /* ---------- Başlık (header.js) ---------- */
  'nav.close': { en: 'Close menu', tr: 'Menüyü kapat' },
  'nav.open': { en: 'Open menu', tr: 'Menüyü aç' },

  /* ---------- Maliyet kartı (cost.js) ---------- */
  'cost.level': { en: 'Study level', tr: 'Eğitim seviyesi' },
  'cost.stay': { en: 'Accommodation', tr: 'Konaklama' },
  'cost.bachelor': { en: 'Bachelor', tr: 'Lisans' },
  'cost.master': { en: "Master's", tr: 'Yüksek lisans' },
  /* Segment butonu dar; "Medicine & Dentistry" 126px kutuda iki satıra
     bölünüp diziyi yamultuyordu. Butonda kısa ad, senaryo ve döküm
     satırında tam ad kullanılır. */
  'cost.medical': { en: 'Medicine', tr: 'Tıp & Diş' },
  'cost.medicalFull': { en: 'Medicine & Dentistry', tr: 'Tıp & Diş' },
  'cost.dorm': { en: 'Dormitory', tr: 'Yurt' },
  'cost.shared': { en: 'Shared flat', tr: 'Paylaşımlı oda' },
  'cost.studio': { en: 'Studio flat', tr: 'Stüdyo daire' },
  'cost.tuition': { en: 'Tuition fee', tr: 'Öğrenim ücreti' },
  'cost.tuitionAlt': { en: '{level} · per year', tr: '{level} · yıllık' },
  'cost.stayAlt': { en: '{type} · €{min}–{max} / month', tr: '{type} · aylık {min}–{max} €' },
  'cost.living': { en: 'Living expenses', tr: 'Yaşam giderleri' },
  'cost.livingAlt': { en: 'groceries, bills · €300 / month', tr: 'market, fatura · aylık 300 €' },
  'cost.transport': { en: 'Transport', tr: 'Ulaşım' },
  'cost.transportAlt': { en: 'public transport · €120 / month', tr: 'toplu taşıma · aylık 120 €' },
  'cost.health': { en: 'Health insurance', tr: 'Sağlık sigortası' },
  'cost.healthAlt': { en: 'required for enrolment', tr: 'kayıt için zorunlu' },
  'cost.first': { en: 'First-year fees', tr: 'İlk yıl ücretleri' },
  'cost.firstAlt': {
    en: 'visa €95–145 · application €140 · deposit €120',
    tr: 'vize 95–145 € · başvuru 140 € · depozito 120 €',
  },
  'cost.scenario': { en: '{level} · {stay} · {m}-month academic year', tr: '{level} · {stay} · {m} aylık akademik yıl' },
  'cost.share': { en: '{p}% of total', tr: 'payı %{p}' },
  'cost.note': {
    en: '<b>{sum}</b> of this is paid in the first year only. The consultancy fee is separate from university fees and is agreed during your consultation.',
    tr: 'Bu tutarın <b>{sum}</b> kadarı yalnız ilk yıl ödenir. Danışmanlık hizmet bedeli üniversite ücretinden ayrıdır ve görüşmede belirlenir.',
  },
  'cost.match': {
    en: 'Published bachelor + dormitory range: €8,500 – €14,000.',
    tr: 'Yayınlanan lisans + yurt aralığı: 8.500 – 14.000 €.',
  },
};

/**
 * Sözlükten metin alır ve {yer-tutucu}ları doldurur.
 * Anahtar bulunamazsa anahtarın kendisi döner — sessizce boş metin
 * basmaktansa eksikliğin ekranda görünmesi tercih edilir.
 */
export function t(key, vars) {
  const row = DICT[key];
  let s = row ? row[LANG] ?? row.en : key;
  if (vars) for (const k in vars) s = s.split('{' + k + '}').join(vars[k]);
  return s;
}

/* ---------- Sayı ve para birimi ----------
   Türkçe binlik ayıracı nokta ve simge sondadır (3.000 €); İngilizcede
   virgül ve simge baştadır (€3,000). Bu yüzden tutarlar veride metin
   olarak değil sayı olarak durur, biçim burada verilir. */
const NF = new Intl.NumberFormat(LOCALE, { maximumFractionDigits: 0 });

export const num = (n) => NF.format(Math.round(n));

export const money = (n, cur = 'EUR') => {
  const sym = cur === 'USD' ? '$' : '€';
  return IS_TR ? `${num(n)} ${sym}` : `${sym}${num(n)}`;
};

/** Aralık: tek sayıda tekrar etmemek için simge bir kez yazılır. */
export const moneyRange = (a, b, cur = 'EUR') => {
  if (a === b) return money(a, cur);
  const sym = cur === 'USD' ? '$' : '€';
  return IS_TR
    ? `${num(a)} – ${num(b)} ${sym}`
    : `${sym}${num(a)} – ${sym}${num(b)}`;
};

/** "3,5 yıl" / "3.5 years" — ondalık ayıracı da dile bağlı. */
export const years = (n) => {
  const s = new Intl.NumberFormat(LOCALE, { maximumFractionDigits: 1 }).format(n);
  return IS_TR ? `${s} yıl` : `${s} ${n === 1 ? 'year' : 'years'}`;
};

export const perYear = (s) => (IS_TR ? `${s} / yıl` : `${s} / year`);
export const perTerm = (s) => (IS_TR ? `${s} / dönem` : `${s} / term`);
