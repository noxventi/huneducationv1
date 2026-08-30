# -*- coding: utf-8 -*-
"""Turkce akicilik denetimi.

python tools/audit_akicilik.py site

audit_tr.py yazim hatalarina bakiyor; bu denetleyici ise metnin
"cevrilmis" mi yoksa "Turkce yazilmis" mi okundugunu olcuyor. Olcutler
canlidaki huneducation.com metinlerinden cikarildi:

  1. TELGRAF CUMLE. Ust uste iki nokta ve noktali virgulle parcalanmis,
     yuklemi dusmus cumleler Ingilizceden cevrilmis gibi okunuyor.
     Paragraf basina noktalama yogunlugu olculuyor.
  2. CUMLE UZUNLUGU. Canlidaki paragraflar 18-30 kelimelik cumlelerden
     olusuyor. 8 kelimenin altinda kalan cumle dizileri telgraf
     etkisi yaratiyor.
  3. AJANS SESI. Her rehber sayfasinda en az bir kez "Hun Education
     olarak ..." ya da "-yoruz/-iyoruz" birinci cogul sahis gecmeli;
     yoksa metin kimsenin agzindan cikmamis gibi duruyor.
  4. OKURA HITAP. Sayfada en az bir dogrudan hitap ("...siniz",
     "endiselenmeyin", "unutmayin") bulunmali.

Cikis kodu: bulgu varsa 1.
"""
import io, os, re, sys, glob

ROOT = sys.argv[1] if len(sys.argv) > 1 else 'site'
TR = os.path.join(ROOT, 'tr')

# Yasal sayfalar bilerek resmi dilde; olcut disinda
ATLA = {'kvkk-aydinlatma.html', 'gizlilik-cerez.html', 'kullanim-kosullari.html',
        'acik-riza.html', 'kurslar.html', 'index.html'}

BLOK = re.compile(r'<p(?![^>]*class="(?:byline|notice|ftr__|trust__|hero__))[^>]*>(.*?)</p>', re.S)
SATIRICI = re.compile(r'</?(?:b|strong|i|em|span|a|small|sup|sub|abbr|code|u|mark|time)(?:\s[^>]*)?>', re.I)
ETIKET = re.compile(r'<[^>]+>')

AJANS = re.compile(r'Hun Education olarak|\b\w+(?:ıyoruz|iyoruz|uyoruz|üyoruz|yoruz|ıyor|iyor)\b'
                   r'|\b\w+(?:ırız|iriz|uruz|ürüz|arız|eriz)\b')
HITAP = re.compile(r'\b\w+(?:sınız|siniz|sunuz|sünüz|yorsunuz|abilirsiniz|ebilirsiniz)\b'
                   # "ayirmaniz gerekir" kalibi da ikinci cogul sahsa seslenir
                   r'|\b\w+(?:manız|meniz)\s+(?:gerek|gerekir|gerekiyor|yeterli|yeter)'
                   # sart kipi ("bulursaniz", "isterseniz") dogrudan okura seslenir
                   r'|\b\w+(?:sanız|seniz)\b'
                   r'|endişelenmeyin|unutmayın|merak etmeyin|bilin ki|kaçırmayın')

# Birinci cogul sahis: sirketin sesi. Bu cumlelerde simdiki zaman dogrudur.
BIZ = re.compile(r'(?:yoruz|yorsunuz|yorum)(?![\wçğıöşüÇĞİÖŞÜ])')
SIMDIKI = re.compile(r'\b[\wçğıöşüÇĞİÖŞÜ]+(?:ıyor|iyor|uyor|üyor)\b(?!uz|sunuz|um)')


def govde(html):
    parcalar = []
    for m in BLOK.finditer(html):
        t = SATIRICI.sub('', m.group(1))
        t = ETIKET.sub(' ', t)
        t = t.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&middot;', '·')
        t = re.sub(r'&[a-z]+;', ' ', t)
        t = re.sub(r'\s+', ' ', t).strip()
        if len(t) > 70:
            parcalar.append(t)
    return parcalar


bulgu = []
sayfalar = [f for f in sorted(glob.glob(os.path.join(TR, '*.html')))
            if os.path.basename(f) not in ATLA]

for yol in sayfalar:
    ad = os.path.basename(yol)
    h = io.open(yol, encoding='utf-8').read()
    paragraflar = govde(h)
    if not paragraflar:
        continue
    tam = ' '.join(paragraflar)

    # 1) noktalama yogunlugu: paragraf basina ':' ve ';' sayisi
    for p in paragraflar:
        agir = p.count(';') + p.count(':')
        kelime = len(p.split())
        if kelime >= 25 and agir / (kelime / 25.0) > 2.2:
            bulgu.append((ad, 'telgraf', 'paragrafta çok fazla iki nokta/noktalı virgül', p[:96]))
            break

    # 2) ortalama cumle uzunlugu
    cumleler = [c for c in re.split(r'(?<=[.!?])\s+', tam) if len(c.split()) > 2]
    if cumleler:
        ort = sum(len(c.split()) for c in cumleler) / len(cumleler)
        if ort < 11:
            bulgu.append((ad, 'kısa', 'ortalama cümle %.1f kelime (hedef 14+)' % ort, ''))

    # 3) ajans sesi
    if not AJANS.search(tam):
        bulgu.append((ad, 'ses', '"Hun Education olarak" / birinci çoğul şahıs anlatım yok', ''))

    # 3b) genis zaman tutarliligi
    # Bilgi aktaran cumleler genis zamanla kurulur ("ucretler degisir");
    # simdiki zaman yalnizca sirketin kendi eylemini anlatan birlesik
    # yuklem zincirlerinde kalir ("belirliyor ... oluyoruz"). Zincir disinda
    # kalan her "-yor" metni gunluk konusmaya kaydirir.
    for p in paragraflar:
        for c in re.split(r'(?<=[.!?])\s+', p):
            if BIZ.search(c):
                continue
            e = SIMDIKI.search(c)
            if e:
                bulgu.append((ad, 'zaman', 'geniş zaman yerine şimdiki zaman: "%s"' % e.group(0),
                              c[:96]))
                break
        else:
            continue
        break

    # 4) okura hitap
    if not HITAP.search(tam):
        bulgu.append((ad, 'hitap', 'okura doğrudan hitap eden tek cümle yok', ''))

if not bulgu:
    print('Denetlenen sayfa: %d' % len(sayfalar))
    print('Akicilik denetimi: temiz.')
    sys.exit(0)

son = ''
for ad, tur, mesaj, ornek in bulgu:
    if ad != son:
        print('\n--- %s' % ad); son = ad
    print('  [%-7s] %s' % (tur, mesaj))
    if ornek:
        print('            …%s…' % ornek)
print('\nToplam bulgu: %d (sayfa: %d)' % (len(bulgu), len(sayfalar)))
sys.exit(1)
