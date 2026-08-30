# -*- coding: utf-8 -*-
"""Elle yazilmis sayfalardaki (index.html, katalog) baglantilari CANLI
slug'lara cevirir ve hreflang/canonical'i iki alan adina gore duzeltir.

    python tools/relink.py site

Neden ayri bir script: index.html ve katalog sayfasi uretilmiyor, elle
yazildi. Slug tablosu gen_pages.py'de tek kaynak oldugu icin burada da
ayni tablo kullanilir; iki yerde farkli slug olmasi imkansiz hale gelir.
"""
import io, os, re, sys

SITE = sys.argv[1]
EN = 'https://huneducation.com/'
TR = 'https://tr.huneducation.com/'

# anahtar -> (EN dosya, TR dosya)
SLUG = {
    'home':     ('index.html', 'index.html'),
    'why':      ('why-hungary.html', 'neden-macaristanda-egitim.html'),
    'edu':      ('education-in-hungary.html', 'macaristanda-universite-okumak.html'),
    'unis':     ('universities.html', 'macaristan-universiteleri.html'),
    'progs':    ('courses.html', 'kurslar.html'),
    'apply':    ('admission.html', 'macaristan-universite-basvuru-sartlari.html'),
    'costs':    ('costs.html', 'macaristan-universite-fiyatlari.html'),
    'masters':  ('masters-education-in-hungary.html', 'macaristan-yuksek-lisans.html'),
    'medicine': ('studying-medicine-in-hungary-and-pursuing-a-medical-degree-in-hungary.html',
                 'macaristanda-tip-egitimi-ve-macaristanda-tip-okumak.html'),
    'pilot':    ('pilot-training-at-hungarian-universities.html',
                 'macaristan-universiteleri-pilotluk-egitimi.html'),
    'life':     ('university-education-and-life-in-hungary-what-you-need-to-know.html',
                 'macaristanda-yasam-ve-universite-egitimi-bilinmesi-gerekenler.html'),
    'stories':  ('student-perspectives.html', 'macaristan-universiteleri-ogrenci-gorusleri.html'),
    'about':    ('about-us.html', 'hakkimizda.html'),
    'contact':  ('contact.html', 'iletisim.html'),
    'privacy':  ('privacy-notice.html', 'kvkk-aydinlatma.html'),
    'consent':  ('consent.html', 'acik-riza.html'),
    'cookies':  ('cookie-policy.html', 'gizlilik-cerez.html'),
    'terms':    ('terms-of-use.html', 'kullanim-kosullari.html'),
}

def url(key, tr):
    slug = SLUG[key][1 if tr else 0]
    base = TR if tr else EN
    return base if slug == 'index.html' else base + slug.replace('.html', '/')

# Onceki (uydurma) dosya adlari -> anahtar. Elle yazilmis sayfalarda bu
# adlar geciyor; canli slug'lara cevrilecekler.
ESKI = {
    False: {  # EN
        'study-in-hungary.html': 'edu', 'universities.html': 'unis',
        'programs.html': 'progs', 'admission-requirements.html': 'apply',
        'tuition-and-living-costs.html': 'costs', 'about.html': 'about',
        'contact.html': 'contact', 'privacy-notice.html': 'privacy',
        'consent.html': 'consent', 'cookie-policy.html': 'cookies',
        'terms-of-use.html': 'terms',
    },
    True: {   # TR
        'macaristanda-egitim.html': 'edu', 'universiteler.html': 'unis',
        'programlar.html': 'progs', 'basvuru.html': 'apply',
        'maliyetler.html': 'costs', 'hakkimizda.html': 'about',
        'iletisim.html': 'contact', 'kvkk-aydinlatma.html': 'privacy',
        'acik-riza.html': 'consent', 'gizlilik-cerez.html': 'cookies',
        'kullanim-kosullari.html': 'terms',
    },
}

def relink(path, tr, kendi_anahtari):
    if not os.path.exists(path):
        return path + ' : YOK'
    s = io.open(path, encoding='utf-8').read()
    n = 0
    for eski, key in ESKI[tr].items():
        yeni = SLUG[key][1 if tr else 0]
        if eski == yeni:
            continue
        for a, b in ((u'href="%s"' % eski, u'href="%s"' % yeni),
                     (u'href="%s?' % eski, u'href="%s?' % yeni),
                     (u'href="%s#' % eski, u'href="%s#' % yeni)):
            n += s.count(a)
            s = s.replace(a, b)

    # canonical / hreflang / og:url
    s = re.sub(r'<link rel="canonical" href="[^"]*">',
               '<link rel="canonical" href="%s">' % url(kendi_anahtari, tr), s)
    s = re.sub(r'<link rel="alternate" hreflang="en" href="[^"]*">',
               '<link rel="alternate" hreflang="en" href="%s">' % url(kendi_anahtari, False), s)
    s = re.sub(r'<link rel="alternate" hreflang="tr" href="[^"]*">',
               '<link rel="alternate" hreflang="tr" href="%s">' % url(kendi_anahtari, True), s)
    s = re.sub(r'<link rel="alternate" hreflang="x-default" href="[^"]*">',
               '<link rel="alternate" hreflang="x-default" href="%s">' % url(kendi_anahtari, False), s)
    s = re.sub(r'<meta property="og:url" content="[^"]*">',
               '<meta property="og:url" content="%s">' % url(kendi_anahtari, tr), s)

    # JSON-LD icindeki mutlak adresler
    s = s.replace('https://huneducation.com/tr/programlar/', url('progs', True))
    s = s.replace('https://huneducation.com/programs/', url('progs', False))
    s = s.replace('"https://huneducation.com/tr/"', '"%s"' % TR)

    # dil degistirici: karsi dildeki es sayfa (yerelde goreli, canlida WPML uretir)
    other = SLUG[kendi_anahtari][0 if tr else 1]
    s = re.sub(r'href="(\.\./|tr/)?[^"]*"(\s+hreflang="(?:en|tr)")',
               lambda m: 'href="%s"%s' % (('../' if tr else 'tr/') + other, m.group(2)),
               s)
    io.open(path, 'w', encoding='utf-8').write(s)
    return '%s : %d baglanti' % (os.path.relpath(path, SITE), n)

print(relink(os.path.join(SITE, 'index.html'), False, 'home'))
print(relink(os.path.join(SITE, 'tr', 'index.html'), True, 'home'))
print(relink(os.path.join(SITE, 'courses.html'), False, 'progs'))
print(relink(os.path.join(SITE, 'tr', 'kurslar.html'), True, 'progs'))
