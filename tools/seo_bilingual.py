# -*- coding: utf-8 -*-
"""Iki alan adi icin sitemap + robots uretimi ve bag denetimi.

    python tools/seo_bilingual.py site

Diller AYRI ALAN ADINDA yayinlanir (WPML domain basina dil):
    Ingilizce  huneducation.com
    Turkce     tr.huneducation.com

Bu yuzden TEK sitemap degil, alan adi basina BIRER sitemap uretilir; her
URL kendi hreflang alternatif kumesini tasir. Karsilikli olmayan
alternatifleri Google yok sayar, bu yuzden iki taraf da ayni cifti gosterir.
"""
import io, os, re, sys

SITE = sys.argv[1]
EN = 'https://huneducation.com/'
TR = 'https://tr.huneducation.com/'
LASTMOD = '2026-08-08'

# (anahtar, EN dosya, TR dosya, oncelik, sıklık, canlida_var_mi)
PAGES = [
    ('home',     'index.html', 'index.html', '1.0', 'weekly', True),
    ('why',      'why-hungary.html', 'neden-macaristanda-egitim.html', '0.9', 'monthly', True),
    ('edu',      'education-in-hungary.html', 'macaristanda-universite-okumak.html', '0.9', 'monthly', True),
    ('unis',     'universities.html', 'macaristan-universiteleri.html', '0.9', 'monthly', True),
    ('progs',    'courses.html', 'kurslar.html', '0.9', 'weekly', True),
    ('apply',    'admission.html', 'macaristan-universite-basvuru-sartlari.html', '0.9', 'monthly', True),
    ('costs',    'costs.html', 'macaristan-universite-fiyatlari.html', '0.9', 'monthly', True),
    ('masters',  'masters-education-in-hungary.html', 'macaristan-yuksek-lisans.html', '0.8', 'monthly', True),
    ('medicine', 'studying-medicine-in-hungary-and-pursuing-a-medical-degree-in-hungary.html',
                 'macaristanda-tip-egitimi-ve-macaristanda-tip-okumak.html', '0.8', 'monthly', True),
    ('pilot',    'pilot-training-at-hungarian-universities.html',
                 'macaristan-universiteleri-pilotluk-egitimi.html', '0.8', 'monthly', True),
    ('life',     'university-education-and-life-in-hungary-what-you-need-to-know.html',
                 'macaristanda-yasam-ve-universite-egitimi-bilinmesi-gerekenler.html', '0.7', 'monthly', True),
    ('stories',  'student-perspectives.html', 'macaristan-universiteleri-ogrenci-gorusleri.html', '0.7', 'monthly', True),
    ('about',    'about-us.html', 'hakkimizda.html', '0.7', 'yearly', True),
    ('contact',  'contact.html', 'iletisim.html', '0.8', 'yearly', True),
    ('privacy',  'privacy-notice.html', 'kvkk-aydinlatma.html', '0.3', 'yearly', False),
    ('consent',  'consent.html', 'acik-riza.html', '0.3', 'yearly', False),
    ('cookies',  'cookie-policy.html', 'gizlilik-cerez.html', '0.3', 'yearly', False),
    ('terms',    'terms-of-use.html', 'kullanim-kosullari.html', '0.3', 'yearly', False),
]


def url(slug, tr):
    base = TR if tr else EN
    return base if slug == 'index.html' else base + slug.replace('.html', '/')


def sitemap(is_tr):
    rows = []
    for key, en, tr, prio, freq, _ in PAGES:
        alts = ('    <xhtml:link rel="alternate" hreflang="en" href="%s"/>\n'
                '    <xhtml:link rel="alternate" hreflang="tr" href="%s"/>\n'
                '    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>'
                % (url(en, False), url(tr, True), url(en, False)))
        rows.append('  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n'
                    '    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n%s\n  </url>'
                    % (url(tr if is_tr else en, is_tr), LASTMOD, freq, prio, alts))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
            '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + '\n'.join(rows) + '\n</urlset>\n')


def robots(is_tr):
    host = TR if is_tr else EN
    return """# %s
# Bu alan adi yalnizca %s icerigi sunar; diger dil ayri alan adinda.

User-agent: *
Allow: /

# Filtre ve siralama varyasyonlari indekslenmez; kanonik sayfa
# parametresiz surumdur (PRD 11.6).
Disallow: /*?q=
Disallow: /*?sirala=

# Yapay zeka tarayicilari icin acik izin (GEO): iceriklerimizin
# yanitlarda kaynak gosterilerek kullanilmasini istiyoruz.
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: %ssitemap.xml
""" % (host, 'Ingilizce' if not is_tr else 'Turkce', host)


io.open(os.path.join(SITE, 'sitemap.xml'), 'w', encoding='utf-8').write(sitemap(False))
io.open(os.path.join(SITE, 'robots.txt'), 'w', encoding='utf-8').write(robots(False))
io.open(os.path.join(SITE, 'tr', 'sitemap.xml'), 'w', encoding='utf-8').write(sitemap(True))
io.open(os.path.join(SITE, 'tr', 'robots.txt'), 'w', encoding='utf-8').write(robots(True))
print('sitemap.xml + robots.txt : her alan adi icin %d URL' % len(PAGES))

# ---------------------------------------------------------------- bag denetimi
def check(dirpath, label):
    problems = []
    for fn in sorted(os.listdir(dirpath)):
        if not fn.endswith('.html'):
            continue
        p = os.path.join(dirpath, fn)
        s = io.open(p, encoding='utf-8').read()
        for attr in ('href', 'src'):
            for target in re.findall(r'%s="([^"]+)"' % attr, s):
                if target.startswith(('#', 'http', 'tel:', 'mailto:', 'data:')):
                    continue
                t = target.split('#')[0].split('?')[0]
                if not t:
                    continue
                full = os.path.normpath(os.path.join(dirpath, t))
                if os.path.isdir(full) or os.path.exists(full):
                    continue
                problems.append('%s/%s -> %s' % (label, fn, target))
    return problems

probs = check(SITE, 'EN') + check(os.path.join(SITE, 'tr'), 'TR')
if probs:
    print('\nKIRIK BAG (%d):' % len(probs))
    for p in sorted(set(probs)):
        print('  X', p)
else:
    print('Tum ic baglantilar ve varlik yollari cozuluyor.')
