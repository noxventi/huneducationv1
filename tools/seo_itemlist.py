# -*- coding: utf-8 -*-
"""Üniversiteler ve katalog sayfalarına ItemList şeması ekler.

NEDEN
  Bu iki sayfa liste sayfası: biri 20 kurumu, diğeri 490 programı
  sayıyor. Liste şeması olmadan arama motoru ve üretken motorlar
  listeyi düz metin olarak görüyor; ItemList ile hangi öğenin nerede
  olduğunu ve hangi sayfaya gittiğini doğrudan okuyabiliyorlar.

  Katalogda 490 öğenin tamamı basılmaz — ilk 60'ı yazılır ve
  numberOfItems gerçek sayıyı bildirir. Tamamını gömmek sayfa ağırlığını
  yüzlerce KB artırır, karşılığında bir şey kazandırmaz.
"""
import io, json, os, re

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def kayitlar():
    """catalog.js'ten üniversite ve program kayıtlarını okur."""
    s = io.open(os.path.join(KOK, 'site', 'assets', 'data', 'catalog.js'),
                encoding='utf-8').read()
    uni = []
    for m in re.finditer(r"\{ id: (\d+), kod: '([^']+)', ad: L\('([^']*)', '([^']*)'\)"
                         r"[^}]*?sehir: '([^']*)'[^}]*?\}", s):
        gov = m.group(0)
        sen = re.search(r"sen: '([^']+)'", gov)
        str_ = re.search(r"str: '([^']+)'", gov)
        uni.append({'en': m.group(3), 'tr': m.group(4), 'sehir': m.group(5),
                    'sen': sen.group(1) if sen else None,
                    'str': str_.group(1) if str_ else None})
    prog = []
    for m in re.finditer(r"\{ ad: L\('([^']*)', '([^']*)'\), uni: \d+[^}]*?\}", s):
        gov = m.group(0)
        pen = re.search(r"pen: '([^']+)'", gov)
        ptr = re.search(r"ptr: '([^']+)'", gov)
        prog.append({'en': m.group(1), 'tr': m.group(2),
                     'pen': pen.group(1) if pen else None,
                     'ptr': ptr.group(1) if ptr else None})
    return uni, prog


def liste_ld(ad, aciklama, ogeler, dil, tur, tam_sayi):
    kok = 'https://tr.huneducation.com' if dil == 'tr' else 'https://huneducation.com'
    ic = []
    for i, o in enumerate(ogeler):
        d = {'@type': 'ListItem', 'position': i + 1, 'name': o['ad']}
        if o.get('url'):
            d['url'] = '%s/%s/%s/' % (kok, tur, o['url'])
        ic.append(d)
    return json.dumps({
        '@context': 'https://schema.org', '@type': 'ItemList',
        'name': ad, 'description': aciklama,
        'itemListOrder': 'https://schema.org/ItemListOrderAscending',
        'numberOfItems': tam_sayi,
        'itemListElement': ic,
    }, ensure_ascii=False, indent=2)


def ekle(yol, ld):
    s = io.open(yol, encoding='utf-8').read()
    if '"ItemList"' in s:
        # onceki surumu degistir
        s = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema\.org",\s*"@type": "ItemList".*?</script>\n?',
                   '', s, flags=re.S)
    blok = '<script type="application/ld+json">\n%s\n</script>\n' % ld
    i = s.index('</head>')
    io.open(yol, 'w', encoding='utf-8').write(s[:i] + blok + s[i:])


def calis():
    uni, prog = kayitlar()
    isler = [
        ('site/universities.html', 'en', 'university',
         'Universities in Hungary that accept international students',
         'Hungarian universities open to international applicants, with their city and type.',
         [{'ad': u['en'], 'url': u['sen']} for u in uni], len(uni)),
        ('site/tr/macaristan-universiteleri.html', 'tr', 'university',
         'Uluslararası öğrenci kabul eden Macaristan üniversiteleri',
         'Başvuru yapılabilen Macaristan üniversiteleri; şehir ve tür bilgisiyle.',
         [{'ad': u['tr'], 'url': u['str']} for u in uni], len(uni)),
        ('site/courses.html', 'en', 'course',
         'English-taught university programmes in Hungary',
         'Bachelor’s, master’s, one-tier and pilot programmes taught in English.',
         [{'ad': p['en'], 'url': p['pen']} for p in prog[:60]], len(prog)),
        ('site/tr/kurslar.html', 'tr', 'course',
         'Macaristan’da İngilizce eğitim veren üniversite programları',
         'Lisans, yüksek lisans, bütünleşik ve pilotaj programları.',
         [{'ad': p['tr'], 'url': p['ptr']} for p in prog[:60]], len(prog)),
    ]
    for yol, dil, tur, ad, acik, ogeler, tam in isler:
        p = os.path.join(KOK, yol)
        ekle(p, liste_ld(ad, acik, ogeler, dil, tur, tam))
        baglantili = sum(1 for o in ogeler if o.get('url'))
        print('  %-42s %d öğe (%d bağlantılı) / toplam %d'
              % (yol.replace('site/', ''), len(ogeler), baglantili, tam))


if __name__ == '__main__':
    calis()
