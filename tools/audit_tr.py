# -*- coding: utf-8 -*-
"""Turkce sayfalarin dil denetimi.

python tools/audit_tr.py site

Dort sey arar:
  1. Turkce sayfada Ingilizce kalinti (govde metni, baglanti etiketi, buton,
     aria-label, alt, placeholder, title/description).
  2. Katalogda cevrilmemis kayit (program adi, universite adi, sinav metni).
  3. Terim sozlugu ihlali (ayni kavram icin iki farkli Turkce karsilik).
  4. Turkce yazim tuzaklari (bogus kesme isareti, egik tirnak eksigi,
     "yapmakta olan" gibi ceviri kokan kaliplar, uzun tire).

Cikis kodu: bulgu varsa 1.
"""
import io, os, re, sys, json, unicodedata

ROOT = sys.argv[1] if len(sys.argv) > 1 else 'site'
TR = os.path.join(ROOT, 'tr')

# ---------------------------------------------------------------- 1) EN kalinti
# Turkce metinde gecmesi olagan olmayan Ingilizce kelimeler. Marka, kisaltma ve
# Turkcede de kullanilan sozcukler (vize, kampus, pilot, plan, IELTS, Erasmus...)
# listede yok; ikisinde de ayni yazilan sozcuk kalinti sayilmaz.
EN_SOZCUK = r"""
about admissions apply back become before below between browse career choose
close contact costs course courses degree discover download during each explore
enrol enroll every field fields filter filters find first following from guide
here home hungary(?!\w) intake language learn life living master masters medicine
menu more next open other overview page pages price prices pricing
programme programmes read requirements results scholarship search see semester
send show start step steps student students study submit support term terms
these those toggle tuition universities university view visa(?=\s|<|$) welcome
what when where which why with year years your
""".split()
EN_RX = re.compile(r'(?<![\w-])(?:%s)(?![\w-])' % '|'.join(EN_SOZCUK), re.I)

# Turkce'de de aynen gecen ya da marka olan diziler: bulunursa yok say
BEYAZ = [
    'Hun Education', 'HUN EDUCATION', 'huneducation', 'Erasmus', 'IELTS', 'TOEFL',
    'Stipendium Hungaricum', 'Class 1', 'Semmelweis', 'Budapest', 'utca',
    'University', 'College', 'Institute', 'Business School',  # resmi uni adlari
    'of Technology', 'of Economics', 'and Economics', 'of Veterinary',
    'Doctors', 'Medicine', 'Pharmacy', 'Dentistry',           # uni adi icinde
    'WhatsApp', 'Google', 'Apostille', 'apostille',
    # resmi program adlari: cevrilmez
    'Professional Pilot', 'Pilot Training (0 to ATPL)',
]

TAG_RX = re.compile(r'<(script|style)[^>]*>.*?</\1>', re.S | re.I)
# Satir ici etiketler bosluk birakmadan silinir; yoksa "<b>Ön Kabul</b>, ödeme"
# metne "Ön Kabul , ödeme" diye dusup sahte "noktalama oncesi bosluk" uretir.
SATIRICI = re.compile(r'</?(?:b|strong|i|em|span|a|small|sup|sub|abbr|code|u|mark|time)(?:\s[^>]*)?>', re.I)
ETIKET = re.compile(r'<[^>]+>')
NITEL = re.compile(r'\b(?:aria-label|alt|placeholder)="([^"]{2,})"')
# URL'ler noktalama kurallarindan muaf
URL = re.compile(r'https?://\S+')


def govde(html):
    """Gorunur metin + kullaniciya donen nitelik degerleri."""
    s = TAG_RX.sub(' ', html)
    nitelikler = NITEL.findall(s)
    s = SATIRICI.sub('', s)
    s = ETIKET.sub(' ', s)
    s = s.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&middot;', '·')
    s = re.sub(r'&[a-z]+;', ' ', s)
    s = URL.sub(' ', s)
    return s + '\n' + '\n'.join(nitelikler)


def maskele(s):
    for b in BEYAZ:
        s = s.replace(b, ' ' * len(b))
    # <html lang="tr"> disi bloklar: lang="en" isaretli her sey mesru
    return s


# --------------------------------------------------------------- 3) terim birligi
# Ayni kavramin tek bir karsiligi olmali. Solda tercih, sagda yasak esanlamlilar.
SOZLUK = [
    ('öğrenim ücreti', ['eğitim ücreti', 'okul ücreti', 'tuition ücreti']),
    ('başvuru',        ['aplikasyon']),
    ('dönem',          ['sömestr', 'semester']),
    ('lisans',         ['bachelor', 'bachelors']),
    ('yüksek lisans',  ['master programı', 'master derecesi']),
    # not: "ikamet karti" fiziksel kartin dogru adi, izinle karistirilmamali
    ('oturum izni',    ['residence permit']),
    ('kabul mektubu',  ['acceptance letter', 'kabul yazısı']),
    ('danışman',       ['konsültan', 'advisor']),
    ('konaklama',      ['akomodasyon']),
    ('yurt',           ['dormitory', 'dorm']),
]

# --------------------------------------------------------------- 4) yazim tuzaklari
YAZIM = [
    (re.compile(r'—'),                     'uzun tire (em-dash) kullanilmis'),
    # Ozel ada gelen ek kesme ile ayrilir ("Macaristan'da") - dogru kullanim,
    # kural yalnizca kucuk harfle baslayan sozcuklerdeki hatali kesmeyi arar.
    (re.compile(r'(?<![\w’])[a-zçğıöşü]{2,}\'[a-zçğıöşü]'), 'cins isimde kesme isareti'),
    (re.compile(r'\byapmakta olan\b|\betmekte olan\b|\bolmakta olan\b'),
                                            'ceviri kokan "-makta olan" kalibi'),
    (re.compile(r'\bsize\s+yardımcı\s+olmak\s+için\s+buradayız\b'),
                                            'ceviri kokan "buradayiz" kalibi'),
    (re.compile(r'\bbir\s+çok\b'),          '"birçok" bitisik yazilir'),
    (re.compile(r'\bher\s?hangi\s?bir\b(?!\s)'), 'yazim'),
    (re.compile(r'\bde\s+ki\b|\bki\s+de\b'), 'baglac yazimi'),
    (re.compile(r'\s+([,.;:!?])'),          'noktalama oncesi bosluk'),
    (re.compile(r'([,;:])(?=[^\s\d"”\)])'), 'noktalama sonrasi bosluk yok'),
    (re.compile(r'\bve\s+ve\b|\bbir\s+bir\b|\biçin\s+için\b'), 'tekrar eden kelime'),
    (re.compile(r'\b(\d+)\s*€\s*/\s*yıl\b'), 'para birimi bicimi (yillik ... € tercih edilir)'),
    (re.compile(r'"[^"]{3,}"'),             'duz tirnak (Turkce metinde “ ” tercih edilir)'),
]

bulgu = []


def ekle(dosya, tur, mesaj, ornek=''):
    bulgu.append((dosya, tur, mesaj, ' '.join(ornek.split())[:90]))


# ================================================================= sayfa taramasi
if not os.path.isdir(TR):
    print('tr/ dizini yok:', TR); sys.exit(1)

sayfalar = sorted(f for f in os.listdir(TR) if f.endswith('.html'))
for f in sayfalar:
    yol = os.path.join(TR, f)
    ham = io.open(yol, encoding='utf-8').read()

    if 'lang="tr"' not in ham:
        ekle(f, 'lang', '<html lang="tr"> yok')

    # dil secici baglantisi disindaki blok
    metin = govde(ham)
    # dil secicideki "English" mesru
    metin = metin.replace('English', '        ').replace('Türkçe', '      ')
    m = maskele(metin)

    kalinti = {}
    for eslesme in EN_RX.finditer(m):
        k = eslesme.group(0)
        i = eslesme.start()
        kalinti.setdefault(k.lower(), m[max(0, i - 34):i + 34])
    for k, ctx in sorted(kalinti.items()):
        ekle(f, 'EN', 'Ingilizce kalinti: "%s"' % k, ctx)

    for tercih, yasaklar in SOZLUK:
        for y in yasaklar:
            if re.search(r'(?<![\w-])%s' % re.escape(y), metin, re.I):
                ekle(f, 'terim', '"%s" yerine "%s"' % (y, tercih))

    for rx, aciklama in YAZIM:
        e = rx.search(metin)
        if e:
            ekle(f, 'yazim', aciklama, metin[max(0, e.start() - 34):e.end() + 34])

# ================================================================= katalog
kat = os.path.join(ROOT, 'assets', 'data', 'catalog.js')
if os.path.exists(kat):
    src = io.open(kat, encoding='utf-8').read()
    # tr alanlari: "tr": "..." ciftleri
    ceviri_yok = re.findall(r'tr:\s*(?:""|null)', src)
    if ceviri_yok:
        ekle('catalog.js', 'katalog', '%d kayitta tr karsiligi bos' % len(ceviri_yok))
    # tr degeri Ingilizce mi? (basit isaret: " of " / " and " / " for ")
    for ad in re.findall(r"tr:\s*'([^']{4,})'", src):
        if re.search(r'\b(of|and|for|with|the)\b', ad):
            ekle('catalog.js', 'katalog', 'tr alani Ingilizce gorunuyor', ad)

idx = os.path.join(ROOT, 'assets', 'data', 'catalog-index.json')
if os.path.exists(idx):
    d = json.load(io.open(idx, encoding='utf-8'))
    unis = d.get('universiteler', d) if isinstance(d, dict) else d
    if isinstance(unis, list):
        for u in unis:
            if isinstance(u, dict) and not (u.get('tr') or u.get('ad')):
                ekle('catalog-index.json', 'katalog', 'universite adi bos', str(u)[:60])

# ================================================================= rapor
if not bulgu:
    print('Denetlenen sayfa: %d' % len(sayfalar))
    print('Turkce denetimi: temiz.')
    sys.exit(0)

son = ''
for dosya, tur, mesaj, ornek in bulgu:
    if dosya != son:
        print('\n--- %s' % dosya); son = dosya
    print('  [%-6s] %s' % (tur, mesaj))
    if ornek:
        print('           …%s…' % ornek)
print('\nToplam bulgu: %d (sayfa: %d)' % (len(bulgu), len(sayfalar)))
sys.exit(1)
