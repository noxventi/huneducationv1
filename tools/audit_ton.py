# -*- coding: utf-8 -*-
"""Satis tonu denetimi.

python tools/audit_ton.py site

Sayfalar dogru bilgi verirken ziyaretciyi kararindan cayirmamali. Bu
denetleyici uc seye bakiyor:

  1. CAYDIRICI KALIPLAR. "uygun olmadigi durumlar", "durust cevap",
     "yetkisine sahip degil" gibi ifadeler dogru olabilir ama okuyucuyu
     once yapamayacagi seye odakliyor. Ayni gercek olumlu cerceveyle
     yazilabiliyor, o yuzden bunlar geri sizarsa yakalanmali.
  2. CAGRI KAPSAMI. Her sayfada en az uc donusum noktasi (iletisim
     baglantisi ya da WhatsApp) olmali; okuyucu sayfanin sonunu
     beklemeden geri donebilmeli.
  3. JSON-LD GECERLILIGI. SSS metinleri hem govdede hem yapisal veride
     duruyor; biri duzeltilip digeri unutulursa arama sonucunda eski
     cumle gorunmeye devam eder.

Not: bu denetim "her uyariyi kaldir" demek degil. Vize kararinin resmi
makama ait oldugu, denklikte taahhut verilmedigi gibi ifadeler kalmali;
bunlar listede yok. Listedekiler, ayni bilgiyi caydirici bicimde
soyleyen kaliplar.

Cikis kodu: bulgu varsa 1.
"""
import io, os, re, sys, json, glob

ROOT = sys.argv[1] if len(sys.argv) > 1 else 'site'

CAYDIRICI = [
    # Turkce
    (r'uygun olmadığı durumlar',        'bölüm başlığı okuyucuyu caydırıyor'),
    (r'doğru cevap olmadığı',           'bölüm başlığı okuyucuyu caydırıyor'),
    (r'Dürüst bir rehberde',            'kendi dürüstlüğünü savunan giriş'),
    (r'Dürüst cevap',                   '"dürüst cevap" kalıbı'),
    (r'garanti vermeyiz',               'olumsuz kapanış; "sürprizle karşılaşmazsınız" tercih edilir'),
    (r'yetkisine sahip değil',           'kapsamı eksiklik olarak sunuyor'),
    (r'sınavsız kabul anlamına gelmez',  'önce yapamayacağını söylüyor'),
    (r'değerlendirmesiz kabul de yok',   'önce yapamayacağını söylüyor'),
    (r'Sektör standardının düşük',       'kendi sektörünü eleştiriyor'),
    (r'olmayana</b> dikkat',             'bölüm bir eksikle açılıyor'),
    (r'hafife aldığı',                   'okuyucuyu suçlayan giriş'),
    (r'öğrenci kaybının çoğu',           'korkutucu istatistik'),
    (r'başlatmayı önermiyoruz',          'kapıyı kapatan ifade'),
    # Ingilizce
    (r'not the right answer',            'section framed as a warning'),
    (r'An honest guide',                 'defends its own honesty'),
    (r'the honest answer',               '"honest answer" framing'),
    (r'industry standard is low',        'attacks the industry'),
    (r'Note what is <b>not</b>',         'section opens on an absence'),
    (r'applicants underestimate',        'blames the reader'),
    (r'do not recommend starting',       'closes the door'),
    (r'trade-offs stated plainly',       'leads with trade-offs'),
    (r'no admission without assessment', 'leads with what you cannot do'),
]

TAG = re.compile(r'<[^>]+>')
LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)

bulgu = []
sayfalar = sorted(glob.glob(os.path.join(ROOT, '*.html')) +
                  glob.glob(os.path.join(ROOT, 'tr', '*.html')))

for yol in sayfalar:
    h = io.open(yol, encoding='utf-8').read()
    ad = os.path.relpath(yol, ROOT).replace('\\', '/')

    for rx, aciklama in CAYDIRICI:
        m = re.search(rx, h)
        if m:
            ctx = ' '.join(TAG.sub(' ', h[max(0, m.start() - 60):m.end() + 60]).split())
            bulgu.append((ad, 'ton', aciklama, ctx[:96]))

    cta = len(re.findall(r'href="[^"]*(?:iletisim|contact)\.html"', h))
    wa = len(re.findall(r'wa\.me', h))
    if cta + wa < 3:
        bulgu.append((ad, 'çağrı', 'sayfada yeterli dönüşüm noktası yok',
                      '%d iletişim + %d WhatsApp' % (cta, wa)))

    for m in LD.finditer(h):
        try:
            json.loads(m.group(1))
        except Exception as e:
            bulgu.append((ad, 'json-ld', 'yapısal veri bozuk', str(e)[:70]))

if not bulgu:
    print('Denetlenen sayfa: %d' % len(sayfalar))
    print('Ton denetimi: temiz.')
    sys.exit(0)

son = ''
for ad, tur, aciklama, ornek in bulgu:
    if ad != son:
        print('\n--- %s' % ad); son = ad
    print('  [%-7s] %s' % (tur, aciklama))
    if ornek:
        print('            …%s…' % ornek)
print('\nToplam bulgu: %d (sayfa: %d)' % (len(bulgu), len(sayfalar)))
sys.exit(1)
