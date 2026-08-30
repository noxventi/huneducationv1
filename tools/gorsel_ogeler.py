# -*- coding: utf-8 -*-
"""Gorsel bilesenleri: figure, kaydirilabilir serit ve universite izgarasi.

Ayri dosyada: hem sayfa jeneratoru hem de elle bakilan katalog sayfasi
ayni isaretlemeyi uretsin diye. A, varlik yolu onekidir; cagiran taraf
(dil klasorune gore) atar.
"""
import os

A = ''


_OLCU = {}


def olcu(dosya):
    """WebP dosyasinin gercek en/boyunu basliktan okur.

    Elle yazilan width/height'a guvenilmiyor: dikey fotograflar icin
    1280x720 yazilirsa hem yer ayirma yanlis olur hem de srcset'teki
    genislik tanimlayicisi yalan soyler, tarayici yanlis dosyayi secer.
    """
    if dosya in _OLCU:
        return _OLCU[dosya]
    yol = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '..', 'site', 'assets', 'img', dosya)
    with open(yol, 'rb') as f:
        b = f.read(32)
    tur = b[12:16]
    if tur == b'VP8 ':
        w = int.from_bytes(b[26:28], 'little') & 0x3FFF
        h = int.from_bytes(b[28:30], 'little') & 0x3FFF
    elif tur == b'VP8L':
        n = int.from_bytes(b[21:25], 'little')
        w, h = (n & 0x3FFF) + 1, ((n >> 14) & 0x3FFF) + 1
    elif tur == b'VP8X':
        w = int.from_bytes(b[24:27], 'little') + 1
        h = int.from_bytes(b[27:30], 'little') + 1
    else:
        raise ValueError('WebP degil: %s' % dosya)
    _OLCU[dosya] = (w, h)
    return w, h


def kaynak_kumesi(ad):
    """srcset + gercek en/boy. Iki varyantin da olcusu dosyadan gelir.

    Kaynak zaten kucukse iki varyant ayni genislikte cikar; boyle bir
    durumda tek aday yazilir, yoksa srcset ayni genisligi iki kez
    tanimlar ve tarayici icin anlamsiz olur.
    """
    bw, bh = olcu(ad + '.webp')
    kw, _ = olcu(ad + '-760.webp')
    if kw >= bw:
        return '%sassets/img/%s.webp %dw' % (A, ad, bw), bw, bh
    return ('%sassets/img/%s-760.webp %dw, %sassets/img/%s.webp %dw'
            % (A, ad, kw, A, ad, bw), bw, bh)


def figure(ad, alt, caption, w=None, h=None, oncelik=False):
    """Makale içi görsel.

    width/height HTML'de verilir: tarayıcı yeri baştan ayırır, görsel
    yüklenirken metin zıplamaz; olculer dosyadan okunur. Alt metin
    görselde GERÇEKTEN görüneni anlatır; kurum adı ancak doğrulanmışsa
    geçer.
    """
    yukle = 'eager" fetchpriority="high' if oncelik else 'lazy'
    srcset, w, h = kaynak_kumesi(ad)
    return f'''<figure class="figure">
  <img src="{A}assets/img/{ad}.webp"
       srcset="{srcset}"
       sizes="(max-width: 900px) 92vw, 820px"
       width="{w}" height="{h}" alt="{alt}" loading="{yukle}" decoding="async">
  <figcaption>{caption}</figcaption>
</figure>'''


def strip(baslik, ogeler):
    """Yatay kaydirilan gorsel seridi. ogeler: [(ad, alt, altyazi), ...]

    Kaydirilabilir bolge klavyeyle de gezilebilmeli; tabindex ve
    aria-label bu yuzden var. Gorseller 4:3 kirpilir, satirlar hizali
    kalir.
    """
    def kare(ad, alt, altyazi):
        srcset, w, h = kaynak_kumesi(ad)
        return f'''  <figure>
    <img src="{A}assets/img/{ad}.webp"
         srcset="{srcset}"
         sizes="(max-width: 640px) 58vw, 320px" width="{w}" height="{h}"
         alt="{alt}" loading="lazy" decoding="async">
    <figcaption>{altyazi}</figcaption>
  </figure>'''
    kart = '\n'.join(kare(*o) for o in ogeler)
    return ('<div class="strip" role="group" tabindex="0" aria-label="%s">\n%s\n</div>'
            % (baslik, kart))


def galeri(ogeler):
    """Üniversite ızgarası. ogeler: [(ad, alt, baslik, altyazi), ...]"""
    def kare(ad, alt, baslik, altyazi):
        srcset, w, h = kaynak_kumesi(ad)
        return f'''  <figure>
    <img src="{A}assets/img/{ad}.webp"
         srcset="{srcset}"
         sizes="(max-width: 700px) 92vw, 300px"
         width="{w}" height="{h}" alt="{alt}" loading="lazy" decoding="async">
    <figcaption><b>{baslik}</b>{altyazi}</figcaption>
  </figure>'''
    kart = '\n'.join(kare(*o) for o in ogeler)
    return '<div class="ugal">\n%s\n</div>' % kart


