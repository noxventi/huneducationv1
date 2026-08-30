# -*- coding: utf-8 -*-
"""Em-dash temizligi.

Tasarim standardi (DESIGN.md, "Do's and Don'ts") uzun tireyi yasakliyor:
yapay zeka metinlerinin en belirgin izlerinden biri ve Turkce'de de
noktalama olarak yerlesik degil. Yerine baglama gore iki nokta, virgul
veya nokta konur.

Kod baglamindaki '—' (sehir sentinel degeri) korunur.
"""
import io, os, re, sys

TOOLS = sys.argv[1] if len(sys.argv) > 1 else 'tools'
D = '—'

# Once ozel durumlar, sonra genel kurallar
OZEL = [
    # kod sentinel: dokunma (asagidaki genel kurallar bunlari atlasin diye
    # gecici bir isaretle korunur)
    ("== '%s'" % D, '@@SENTINEL_A@@'),
    ("'%s'," % D, '@@SENTINEL_B@@'),
    ("or '%s'" % D, '@@SENTINEL_C@@'),

    # basliklarda: iki nokta daha net
    ('About Us %s Hungary-Focused' % D, 'About Us: Hungary-Focused'),
    ('Contact %s Free Consultation' % D, 'Contact: Free Consultation'),

    # parantez ici aciklama
    ('education and %s where required %s financial data' % (D, D),
     'education and, where required, financial data'),
    ('one country %s Hungary %s since 1999' % (D, D), 'one country, Hungary, since 1999'),
    ('student stories section %s with your initial or full name, your university and your programme %s happens' % (D, D),
     'student stories section, with your initial or full name, your university and your programme, happens'),
    ('ogrenci hikayeleri bolumunde', 'ogrenci hikayeleri bolumunde'),
]

# <b>Etiket</b> — aciklama   ->   <b>Etiket</b>: aciklama
GENEL = [
    (re.compile(r'</b>\s*%s\s*' % D), '</b>: '),
    (re.compile(r'</td><td>([^<]{1,60}?)\s*%s\s*' % D), r'</td><td>\1, '),
    # cumle ici: sonrasi kucuk harfle basliyorsa virgul
    (re.compile(r'\s*%s\s+(?=[a-zçğıöşü])' % D), ', '),
    # sonrasi buyuk harfle basliyorsa nokta
    (re.compile(r'\s*%s\s+(?=[A-ZÇĞİÖŞÜ“"])' % D), '. '),
    # sayi araliklarinda kalan (6—10) -> en dash
    (re.compile(r'(\d)\s*%s\s*(\d)' % D), r'\1–\2'),
]

DOSYALAR = ['en_content.py', 'en_content2.py', 'en_content3.py', 'en_content4.py',
            'en_content5.py', 'en_content6.py', 'en_content7.py',
            'pages_content.py', 'pages_content2.py', 'pages_content3.py',
            'pages_content4.py', 'pages_content5.py', 'pages_content6.py',
            'pages_content7.py', 'gen_pages.py']

toplam = 0
for f in DOSYALAR:
    p = os.path.join(TOOLS, f)
    if not os.path.exists(p):
        continue
    s = io.open(p, encoding='utf-8').read()
    once = s.count(D)
    if not once:
        continue
    for a, b in OZEL:
        s = s.replace(a, b)
    for rx, rep in GENEL:
        s = rx.sub(rep, s)
    # sentinel geri
    s = s.replace('@@SENTINEL_A@@', "== '%s'" % D)
    s = s.replace('@@SENTINEL_B@@', "'%s'," % D)
    s = s.replace('@@SENTINEL_C@@', "or '%s'" % D)
    sonra = s.count(D)
    io.open(p, 'w', encoding='utf-8').write(s)
    toplam += once - sonra
    print('%-22s %3d -> %d' % (f, once, sonra))

print('temizlenen:', toplam)
