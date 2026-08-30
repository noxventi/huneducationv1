# -*- coding: utf-8 -*-
"""canli.json -> site/assets/data/catalog.js

Veri kaynagi ARTIK ELLE YAZILMIS DEGIL: huneducation.com uzerindeki gercek
`course` ve `university` kayitlarindan disa aktarilmistir. Onceki surumde
46 kayit elle derlenmisti ve ucretlerin bir kismi canlidaki gercek
rakamlarla ortusmuyordu; bu surumde 498 kurs ve 20 universite oldugu gibi
aktarilir.

Onemli tespitler (canlidan dogrulanmistir):
  * course_price YILLIKTIR (kurs sayfasinda "usd/year (2 semesters)" yazar)
  * Ucretlerin ~%15'i USD, gerisi EUR
  * Tip yalniz UC universitede: SOTE, PTE, SZTE (Debrecen'de yok)
  * Pilotaj BME'de, 29.500 EUR (Dunaujvaros'ta degil)
"""
import io, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tr_sozluk import kurs_tr, uni_tr, sinav_bilesenleri, dil_seviye_kod, DIL_SEVIYE

SRC = sys.argv[1]
OUT = sys.argv[2]
d = json.load(io.open(SRC, encoding='utf-8'))

# ---------------------------------------------------------------- sehirler
# Canlida sehir terimi "Miscolc" yazilmis (yazim hatasi); dogru yazimi
# gosteriyoruz, anahtar eslesmesi bozulmasin diye ikisi de tutuluyor.
SEHIR = {
    'Budapest':    ('budapest',    'Budapest',    'Budapeşte',    'Central Hungary',      'Orta Macaristan'),
    'Debrecen':    ('debrecen',    'Debrecen',    'Debrecen',     'Eastern Hungary',      'Doğu Macaristan'),
    'Szeged':      ('szeged',      'Szeged',      'Szeged',       'Southern Hungary',     'Güney Macaristan'),
    'Pécs':        ('pecs',        'Pécs',        'Pécs',         'South-western Hungary','Güneybatı Macaristan'),
    # Canlida iki yazim var: kurs taksonomisinde 'Miscolc' (yazim hatasi),
    # universite alaninda 'Miskolc'. Ikisi de ayni sehre eslenir.
    'Miscolc':     ('miskolc',     'Miskolc',     'Miskolc',      'North-eastern Hungary','Kuzeydoğu Macaristan'),
    'Miskolc':     ('miskolc',     'Miskolc',     'Miskolc',      'North-eastern Hungary','Kuzeydoğu Macaristan'),
    'Dunaújváros': ('dunaujvaros', 'Dunaújváros', 'Dunaújváros',  'Central Hungary',      'Orta Macaristan'),
    'Nyíregyháza': ('nyiregyhaza', 'Nyíregyháza', 'Nyíregyháza',  'North-eastern Hungary','Kuzeydoğu Macaristan'),
    'Kecskemét':   ('kecskemet',   'Kecskemét',   'Kecskemét',    'Central Hungary',      'Orta Macaristan'),
}

# ---------------------------------------------------------------- seviye / alan
SEVIYE = {
    # Canlida bir kayitta seviye terimi Turkce girilmis; ikisi de tanınır.
    'Yüksek Lisans (MA&MSc)':                  ('yukseklisans', "Master's (MA/MSc)",               'Yüksek Lisans (MA/MSc)'),
    'Bachelor (BA&BSc)':                       ('lisans',      "Bachelor's (BA/BSc)",              'Lisans (BA/BSc)'),
    'Master (MA&MSc)':                         ('yukseklisans', "Master's (MA/MSc)",               'Yüksek Lisans (MA/MSc)'),
    'Medicine (M.D.)':                         ('tip',          'Medicine (M.D.)',                 'Tıp (M.D.)'),
    'Dentistry (D.M.D.)':                      ('dis',          'Dentistry (D.M.D.)',              'Diş Hekimliği (D.M.D.)'),
    'Pharmacy (PharmD)':                       ('eczacilik',    'Pharmacy (PharmD)',               'Eczacılık (PharmD)'),
    'One-tier Master':                         ('butunlesik',   'One-tier Master',                 'Bütünleşik Program'),
    'Foundation':                              ('hazirlik',     'Foundation',                      'Bölüm Hazırlık'),
    'English Language Preparatory Course':     ('dilhazirlik',  'English Language Preparatory',    'İngilizce Dil Hazırlık'),
    'Combo Preparatory (English+Foundation)':  ('combo',        'Combo Preparatory',               'Combo Hazırlık'),
    'Hungarian Language Preparatory':          ('macarca',      'Hungarian Language Preparatory',  'Macar Dili Hazırlık'),
}
ALAN = {
    'Agricultural and Food Sciences':                       ('tarim',        'Agricultural and Food Sciences', 'Tarım ve Gıda Bilimleri'),
    'Art (Music & Visual Arts)':                            ('sanat',        'Art (Music & Visual Arts)',      'Sanat (Müzik ve Görsel Sanatlar)'),
    'Business and Economics':                               ('isletme',      'Business and Economics',         'İşletme ve Ekonomi'),
    'Communication and Media':                              ('iletisim',     'Communication and Media',        'İletişim ve Medya'),
    'Cultural Sciences, Education and Regional Development': ('kultur',      'Cultural Sciences and Education','Kültür Bilimleri ve Eğitim'),
    'Engineering - Architecture':                           ('muhendislik',  'Engineering and Architecture',   'Mühendislik ve Mimarlık'),
    'Health Sciences':                                      ('saglik',       'Health Sciences',                'Sağlık Bilimleri'),
    'Humanities and Social Sciences':                       ('beseri-sosyal','Humanities and Social Sciences', 'Beşeri ve Sosyal Bilimler'),
    'International Relations, Politics':                    ('uluslararasi', 'International Relations',        'Uluslararası İlişkiler'),
    'IT (Information Technology)':                          ('it',           'IT (Information Technology)',    'IT (Bilgi Teknolojisi)'),
    'Language':                                             ('dil',          'Language Studies',               'Dil Bilimleri'),
    'Law':                                                  ('hukuk',        'Law',                            'Hukuk'),
    'Medicine - Dentistry - Pharmacy':                      ('tipalan',      'Medicine, Dentistry, Pharmacy',  'Tıp, Diş Hekimliği, Eczacılık'),
    'Pilot':                                                ('pilot',        'Pilot Training',                 'Pilotaj'),
    'Preparatory':                                          ('hazirlikalan', 'Preparatory',                    'Hazırlık'),
    'Science (Math,Bio,Che)':                               ('bilim',        'Science (Maths, Biology, Chemistry)', 'Bilim (Matematik, Biyoloji, Kimya)'),
    'Sport':                                                ('spor',         'Sport Sciences',                 'Spor Bilimleri'),
    'Tourism':                                              ('turizm',       'Tourism',                        'Turizm'),
}
TUR = {
    'State': ('devlet', 'State', 'Devlet'),
    'State & Foundation': ('devlet-vakif', 'State and Foundation', 'Devlet ve Vakıf'),
    'Private': ('ozel', 'Private', 'Özel'),
    'Business and Economics': ('ozel', 'Private', 'Özel'),
    '': ('belirtilmemis', 'Not stated', 'Belirtilmemiş'),
}

SINAV_AD = {
    'girissinavi': ('Entrance exam',            'Giriş sınavı'),
    'yeterlilik':  ('Competency test',          'Yeterlilik testi'),
    'yazili':      ('Written exam',             'Yazılı sınav'),
    'sozlu':       ('Oral exam',                'Sözlü sınav'),
    'mulakat':     ('Interview',                'Mülakat'),
    'matematik':   ('Mathematics',              'Matematik'),
    'fizik':       ('Physics',                  'Fizik'),
    'biyoloji':    ('Biology',                  'Biyoloji'),
    'ingilizce':   ('English assessment',       'İngilizce değerlendirmesi'),
    'seviye':      ('Placement test',           'Seviye tespit sınavı'),
    'portfolyo':   ('Portfolio',                'Portfolyo'),
    'ozgecmis':    ('CV',                       'Özgeçmiş'),
    'motivasyon':  ('Motivation letter',        'Motivasyon mektubu'),
    'referans':    ('Reference work',           'Referans çalışma'),
    'bme':         ('BME e-admission system',   'BME e-başvuru sistemi'),
    'online':      ('online',                   'çevrim içi'),
}


def q(s):
    """JS tek tirnakli dizge icin kacis."""
    return (s or '').replace('\\', '\\\\').replace("'", "\\'").replace('\n', ' ').strip()

# ---------------------------------------------------------------- universiteler
# Canlida `course_institute` bazi kayitlarda EN karsiligina normalize
# edilemiyor (UNIVET). Elle koprulenir; kaynak yine canli veridir.
EK_ESLEME = {3534: 1272}   # University of Veterinary Medicine (UNIVET)

unis = []
uni_by_id = {}
for u in sorted(d['universiteler'], key=lambda x: x['en']):
    sehir = SEHIR.get(u['sehir'], (None,))[0]
    tur = TUR.get((u['tur'] or '').strip(), TUR[''])[0]
    kod = re.sub(r'[^a-z0-9]+', '-', u['en'].lower()).strip('-')[:28]
    rec = dict(id=u['id'], kod=kod, en=u['en'], tr=uni_tr(u['en'], u['tr']) or u['en'],
               sehir=sehir, tur=tur, kurulus=(u['kurulus'] or '').strip())
    unis.append(rec)
    uni_by_id[u['id']] = rec

# ---------------------------------------------------------------- programlar
progs = []
atlanan = 0
for k in d['kurslar']:
    k['uni'] = EK_ESLEME.get(k['uni'], k['uni'])
    if k['uni'] not in uni_by_id:
        atlanan += 1
        continue
    sev = SEVIYE.get(k['seviye'])
    alan = ALAN.get(k['alan'])
    sehir = SEHIR.get(k['sehir'], (None,))[0]
    if not sev or not alan:
        atlanan += 1
        continue
    try:
        fiyat = int(float(k['fiyat']))
    except (TypeError, ValueError):
        fiyat = None
    try:
        donem = int(k['donem'])
    except (TypeError, ValueError):
        donem = None
    progs.append(dict(
        en=k['en'], tr=kurs_tr(k['en'], k['tr']) or k['en'], uni=k['uni'],
        seviye=sev[0], alan=alan[0], sehir=sehir,
        fiyat=fiyat, para=(k['para'] or 'eur').upper(),
        donem=donem, son=(k['son'] or '').strip(),
        dilSeviye=dil_seviye_kod(k['dilSeviye']),
        sinav=sinav_bilesenleri(k['sinav']),
        ay=(k['ay'] or '').strip(),
    ))

progs.sort(key=lambda p: (p['seviye'], p['en']))

# ---------------------------------------------------------------- yaz
L = []
w = L.append
w("/* ============================================================")
w("   catalog.js - program katalogu")
w("")
w("   VERI KAYNAGI")
w("   ------------")
w("   Bu dosya ELLE YAZILMAMISTIR. huneducation.com uzerindeki gercek")
w("   `course` ve `university` kayitlarindan uretilmistir:")
w("       python tools/build_catalog.py canli.json site/assets/data/catalog.js")
w("")
w("   Onceki surumde 46 kayit elle derlenmisti ve ucretlerin bir kismi")
w("   canlidaki gercek rakamlarla ortusmuyordu. Simdi %d kurs ve %d" % (len(progs), len(unis)))
w("   universite oldugu gibi aktariliyor.")
w("")
w("   UCRET SEMANTIGI")
w("   ---------------")
w("   course_price YILLIKTIR. Canli kurs sayfasi bunu acikca yaziyor:")
w("   \"Price: 19 900 usd/year (2 semesters)\". Donem sayisi programin")
w("   TOPLAM uzunlugudur (12 donem = 6 yil), yillik ucretin bolen degil.")
w("   Ucretlerin bir kismi USD cinsindendir; para birimi her kayitta durur.")
w("   ============================================================ */")
w("")
w("import { LANG, t, money, years, perYear } from '../js/core/i18n.js';")
w("")
w("const L = (en, tr) => (LANG === 'tr' ? tr : en);")
w("")
w("export const KAYNAK = {")
w("  ad: 'huneducation.com',")
w("  derlendi: L('8 August 2026', '8 Ağustos 2026'),")
w("};")
w("")

w("export const SEHIRLER = {")
for canli, (kod, en, tr, ben, btr) in SEHIR.items():
    w("  %s: { ad: L('%s', '%s'), bolge: L('%s', '%s') }," % (kod, q(en), q(tr), q(ben), q(btr)))
w("};")
w("")

w("export const TURLER = {")
for _, (kod, en, tr) in sorted({v[0]: v for v in TUR.values()}.items()):
    w("  '%s': L('%s', '%s')," % (kod, q(en), q(tr)))
w("};")
w("")

w("/* Giris sinavi bilesenleri: canlidaki serbest Ingilizce metin")
w("   bilesenlerine ayrilip burada iki dilde yeniden uretiliyor. */")
w("export const SINAV_ADI = {")
for kod, (en, tr) in SINAV_AD.items():
    w("  %s: L('%s', '%s')," % (kod, q(en), q(tr)))
w("};")
w("")
w("export const DIL_ADI = {")
for kod, (en, tr) in DIL_SEVIYE.items():
    w("  '%s': L('%s', '%s')," % (kod, q(en), q(tr)))
w("};")
w("")
w("export const SEVIYELER = {")
for canli, (kod, en, tr) in SEVIYE.items():
    w("  %s: L('%s', '%s')," % (kod, q(en), q(tr)))
w("};")
w("")

w("export const ALANLAR = {")
for canli, (kod, en, tr) in sorted(ALAN.items(), key=lambda kv: kv[1][1]):
    key = "'%s'" % kod if '-' in kod else kod
    w("  %s: L('%s', '%s')," % (key, q(en), q(tr)))
w("};")
w("")

w("/* Universiteler - canli `university` kayitlarindan. */")
w("export const UNIVERSITELER = [")
for u in unis:
    w("  { id: %d, kod: '%s', ad: L('%s', '%s'), sehir: %s, tur: '%s', kurulus: %s }," % (
        u['id'], u['kod'], q(u['en']), q(u['tr']),
        ("'%s'" % u['sehir']) if u['sehir'] else 'null',
        u['tur'],
        ("'%s'" % u['kurulus']) if u['kurulus'] else 'null'))
w("];")
w("")

w("/* Programlar - canli `course` kayitlarindan. Ucret YILLIKTIR. */")
w("export const PROGRAMLAR = [")
for p in progs:
    parts = [
        "ad: L('%s', '%s')" % (q(p['en']), q(p['tr'])),
        "uni: %d" % p['uni'],
        "seviye: '%s'" % p['seviye'],
        "alan: '%s'" % p['alan'],
        "sehir: %s" % (("'%s'" % p['sehir']) if p['sehir'] else 'null'),
        "fiyat: %s" % (p['fiyat'] if p['fiyat'] is not None else 'null'),
        "para: '%s'" % p['para'],
        "donem: %s" % (p['donem'] if p['donem'] is not None else 'null'),
    ]
    if p['son']:
        parts.append("son: '%s'" % q(p['son']))
    if p['dilSeviye']:
        parts.append("dil: '%s'" % q(p['dilSeviye']))
    if p['sinav']:
        parts.append("sinav: [%s]" % ', '.join("'%s'" % x for x in p['sinav']))
    if p['ay']:
        parts.append("ay: '%s'" % q(p['ay']))
    w("  { %s }," % ', '.join(parts))
w("];")
w("")

w("""/* ---------------------------------------------------------------- turevler */

/* Universitenin turu ve alanlari veriden TUREVDIR: alan listesi o
   universitede fiilen program bulunan kategorilerden hesaplanir, elle
   bakim gerektirmez. */
for (const u of UNIVERSITELER) {
  u.turAdi = TURLER[u.tur] ?? u.tur;
  const say = new Map();
  for (const p of PROGRAMLAR) {
    if (p.uni === u.id) say.set(p.alan, (say.get(p.alan) ?? 0) + 1);
  }
  u.alanlar = [...say.entries()].sort((a, b) => b[1] - a[1]).map(([k]) => k);
  u.programSayisi = [...say.values()].reduce((a, b) => a + b, 0);
}

/** Sinav bilesenlerini okunur bir cumleye cevirir.
 *  "online" bir bilesen degil bir NITELIK: sona parantezle eklenir. */
export const sinavMetni = (p) => {
  if (!p.sinav || !p.sinav.length) return null;
  const online = p.sinav.includes('online');
  const ana = p.sinav.filter((x) => x !== 'online').map((x) => SINAV_ADI[x]).filter(Boolean);
  if (!ana.length) return online ? SINAV_ADI.mulakat + ' (' + SINAV_ADI.online + ')' : null;
  const s = ana.join(' · ');
  return online ? s + ' (' + SINAV_ADI.online + ')' : s;
};

/** Egitim dili her programda Ingilizce; istenen seviye varsa eklenir. */
export const dilMetni = (p) =>
  p.dil ? t('lang.en') + ' · ' + (DIL_ADI[p.dil] ?? p.dil) : t('lang.en');

export const uniById = (id) => UNIVERSITELER.find((u) => u.id === id);
export const sehirAdi = (id) => SEHIRLER[id]?.ad ?? id;

/** "EUR 5,800 / year" - ucret yilliktir, donem sayisi programin toplam uzunlugu. */
export const ucretMetni = (p) =>
  p.fiyat == null ? null : perYear(money(p.fiyat, p.para));

/** Butce filtresi icin yillik EUR karsiligi. USD kayitlari yaklasik cevrilir;
 *  filtre bandi genis oldugu icin kur dalgalanmasi bandi degistirmiyor. */
const USD_EUR = 0.92;
export const yillikEur = (p) =>
  p.fiyat == null ? null : Math.round(p.fiyat * (p.para === 'USD' ? USD_EUR : 1));

/** Programin suresi. Tek donemlik programda "0,5 yil" demek Turkce'de de
 *  Ingilizce'de de tuhaf duruyor; bu durumda donem olarak yazilir. */
export const sureMetni = (p) => {
  if (!p.donem) return null;
  if (p.donem === 1) return L('1 semester', '1 dönem');
  if (p.donem % 2 === 1) return L(p.donem + ' semesters', p.donem + ' dönem');
  return years(p.donem / 2);
};

/** Baslangic donemi ve son basvuru, kaydin kendi verisinden. */
export const AYLAR = {
  September: L('September', 'Eylül'),
  February: L('February', 'Şubat'),
  January: L('January', 'Ocak'),
  October: L('October', 'Ekim'),
};
export const baslangicMetni = (p) => AYLAR[p.ay] ?? p.ay ?? null;

export const sonBasvuruMetni = (p) => {
  if (!p.son) return null;
  const d = new Date(p.son + 'T00:00:00');
  if (isNaN(d)) return p.son;
  return new Intl.DateTimeFormat(LANG === 'tr' ? 'tr-TR' : 'en-GB',
    { day: 'numeric', month: 'long', year: 'numeric' }).format(d);
};

/** Hun Education'in YAYINLADIGI genel aralikar (maliyet sayfasi).
 *  Katalogdaki tek tek ucretlerden ayridir: bunlar kurumun kendi beyani. */
export const UCRET_ARALIKLARI = {
  lisans: L('EUR 3,000 – 5,000 / year', 'yıllık 3.000 – 5.000 €'),
  yukseklisans: L('EUR 4,000 – 6,000 / year', 'yıllık 4.000 – 6.000 €'),
  doktora: L('EUR 6,000 – 8,000 / year', 'yıllık 6.000 – 8.000 €'),
};

export const TAKVIM = {
  guz: { baslangic: L('September', 'Eylül'), sonBasvuru: L('April - June', 'Nisan - Haziran') },
  bahar: { baslangic: L('February', 'Şubat'), sonBasvuru: L('End of October - November', 'Ekim sonu - Kasım') },
};""")

io.open(OUT, 'w', encoding='utf-8').write('\n'.join(L) + '\n')

# --- yan dosya: sayfa ureticisi icin ---
# gen_pages.py once catalog.js'i regex ile ayristiriyordu; format degisince
# kiriliyordu. Artik ayni kaynaktan uretilen bu JSON'u okuyor.
alan_say = {}
for pr in progs:
    alan_say.setdefault(pr['uni'], {})
    alan_say[pr['uni']][pr['alan']] = alan_say[pr['uni']].get(pr['alan'], 0) + 1

yan = {
    'sehirler': {v[0]: (v[1], v[2]) for v in SEHIR.values()},
    'alanlar': {v[0]: (v[1], v[2]) for v in ALAN.values()},
    'turler': {v[0]: (v[1], v[2]) for v in TUR.values()},
    'seviyeler': {v[0]: (v[1], v[2]) for v in SEVIYE.values()},
    'programSayisi': len(progs),
    'universiteler': [],
}
for u in unis:
    say = alan_say.get(u['id'], {})
    yan['universiteler'].append({
        'id': u['id'], 'en': u['en'], 'tr': u['tr'], 'sehir': u['sehir'],
        'tur': u['tur'], 'kurulus': u['kurulus'],
        'alanlar': [k for k, _ in sorted(say.items(), key=lambda kv: -kv[1])],
        'programSayisi': sum(say.values()),
    })
yol = os.path.join(os.path.dirname(OUT) or '.', 'catalog-index.json')
io.open(yol, 'w', encoding='utf-8').write(json.dumps(yan, ensure_ascii=False, indent=1))
print('yan dosya:', yol)
print('yazildi:', OUT)
print('universite:', len(unis), '| program:', len(progs), '| atlanan:', atlanan)
print('boyut KB:', round(os.path.getsize(OUT) / 1024, 1))
