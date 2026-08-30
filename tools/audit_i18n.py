# -*- coding: utf-8 -*-
"""Iki dilli yayin denetimi.

Kontrol edilenler:
  1. <html lang> dogru mu
  2. canonical kendi URL'sini mi gosteriyor
  3. hreflang en/tr/x-default eksiksiz ve KARSILIKLI mi
  4. dil degistirici karsi dilin es sayfasini mi gosteriyor
  5. Ingilizce sayfalarda gorunur Turkce metin kalmis mi
"""
import io, os, re, sys

SITE = sys.argv[1]
EN_BASE = 'https://huneducation.com/'
TR_BASE = 'https://tr.huneducation.com/'

PAIRS = [
    ('index.html',                    'index.html'),
    ('why-hungary.html',              'neden-macaristanda-egitim.html'),
    ('education-in-hungary.html',     'macaristanda-universite-okumak.html'),
    ('universities.html',             'macaristan-universiteleri.html'),
    ('courses.html',                  'kurslar.html'),
    ('admission.html',                'macaristan-universite-basvuru-sartlari.html'),
    ('costs.html',                    'macaristan-universite-fiyatlari.html'),
    ('masters-education-in-hungary.html', 'macaristan-yuksek-lisans.html'),
    ('studying-medicine-in-hungary-and-pursuing-a-medical-degree-in-hungary.html',
     'macaristanda-tip-egitimi-ve-macaristanda-tip-okumak.html'),
    ('pilot-training-at-hungarian-universities.html',
     'macaristan-universiteleri-pilotluk-egitimi.html'),
    ('university-education-and-life-in-hungary-what-you-need-to-know.html',
     'macaristanda-yasam-ve-universite-egitimi-bilinmesi-gerekenler.html'),
    ('student-perspectives.html',     'macaristan-universiteleri-ogrenci-gorusleri.html'),
    ('about-us.html',                 'hakkimizda.html'),
    ('contact.html',                  'iletisim.html'),
    ('privacy-notice.html',           'kvkk-aydinlatma.html'),
    ('consent.html',                  'acik-riza.html'),
    ('cookie-policy.html',            'gizlilik-cerez.html'),
    ('terms-of-use.html',             'kullanim-kosullari.html'),
]

def canon(slug, tr):
    base = TR_BASE if tr else EN_BASE
    return base if slug == 'index.html' else base + slug.replace('.html', '/')

# Ozel isimler ve marka adlari: Ingilizce sayfada kalmasi normal
ALLOW = {'Türkiye', 'Kadıköy', 'Pécs', 'Işıl', 'Özlem', 'Nyíregyháza', 'Dunaújváros',
         'Kecskemét', 'Eötvös', 'Loránd', 'Óbuda', 'Kodolányi', 'János', 'Kızılay',
         'Menekşe', 'Çankaya', 'Osmanağa', 'Kıbrıs', 'Şehitleri', 'Yücel', 'Özlüce',
         'Öndül', 'Kantarcı', 'Çakmak', 'Çınaroğlu', 'Çağla', 'Türken', 'Ertaş',
         'Yalçın', 'Hızal', 'Çanakkale', 'Nemzeti', 'Adatvédelmi', 'Információszabadság',
         'Hatóság', 'Beyza', 'Şubat', 'Bulvarı', 'Nilüfer', 'ç',
         # Macar bilim insanlari ve yer adlari (Ingilizce sayfada da boyle yazilir)
         'Györgyi', 'Szent', 'Balaton'}

fails = []

def get(s, pat):
    m = re.search(pat, s)
    return m.group(1) if m else None

for en, tr in PAIRS:
    for slug, is_tr in ((en, False), (tr, True)):
        path = os.path.join(SITE, 'tr', slug) if is_tr else os.path.join(SITE, slug)
        tag = ('TR/' if is_tr else 'EN/') + slug
        if not os.path.exists(path):
            fails.append('%s : DOSYA YOK' % tag)
            continue
        s = io.open(path, encoding='utf-8').read()

        lang = get(s, r'<html lang="([^"]+)"')
        want = 'tr' if is_tr else 'en'
        if lang != want:
            fails.append('%s : lang="%s" olmali "%s"' % (tag, lang, want))

        c = get(s, r'<link rel="canonical" href="([^"]+)"')
        if c != canon(slug, is_tr):
            fails.append('%s : canonical %s != %s' % (tag, c, canon(slug, is_tr)))

        alt_en = get(s, r'hreflang="en" href="([^"]+)"')
        alt_tr = get(s, r'hreflang="tr" href="([^"]+)"')
        alt_x = get(s, r'hreflang="x-default" href="([^"]+)"')
        if alt_en != canon(en, False):
            fails.append('%s : hreflang en %s != %s' % (tag, alt_en, canon(en, False)))
        if alt_tr != canon(tr, True):
            fails.append('%s : hreflang tr %s != %s' % (tag, alt_tr, canon(tr, True)))
        if alt_x != canon(en, False):
            fails.append('%s : x-default %s != %s' % (tag, alt_x, canon(en, False)))

        # dil degistirici: karsi dile giden bag
        block = re.search(r'<div class="lang".*?</div>', s, re.S)
        if not block:
            fails.append('%s : dil degistirici yok' % tag)
        else:
            b = block.group(0)
            want_other = ('../' + en) if is_tr else ('tr/' + tr)
            if 'href="%s"' % want_other not in b:
                fails.append('%s : dil degistirici %s gostermiyor' % (tag, want_other))
            if 'aria-current="true"' not in b:
                fails.append('%s : dil degistiricide aria-current yok' % tag)

        # Icindekiler capalari: h2 bolumleri h3'e indirilince listede
        # kalan girisler bos capa uretiyordu; bu sessiz bir kirilma.
        toc = re.search(r'<nav class="toc".*?</nav>', s, re.S)
        if toc:
            kirik = [h for h in re.findall(r'href="#([^"]+)"', toc.group(0))
                     if ('id="%s"' % h) not in s]
            if kirik:
                fails.append('%s : icindekilerde bos capa -> %s' % (tag, kirik))

        # Ingilizce sayfada gorunur Turkce metin
        if not is_tr:
            body = re.sub(r'<script.*?</script>', '', s, flags=re.S)
            body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
            txt = re.sub(r'<[^>]+>', ' ', body)
            hits = {w for w in re.findall(r'[\wÇĞİÖŞÜçğıöşü]+', txt)
                    if re.search(r'[çğıöşüÇĞİÖŞÜ]', w)} - ALLOW
            if hits:
                fails.append('%s : cevrilmemis olabilir -> %s' % (tag, sorted(hits)[:12]))

# ---------------------------------------------------------------- header
# Yasal sayfalar disindaki her sayfaya header'dan erisilebilmeli. Menu
# elle yazilmis sayfalarda ayri durdugu icin daha once ayrismisti;
# bu kontrol bir daha sessizce eksilmesini engeller.
YASAL = {'privacy-notice.html', 'consent.html', 'cookie-policy.html', 'terms-of-use.html',
         'kvkk-aydinlatma.html', 'acik-riza.html', 'gizlilik-cerez.html',
         'kullanim-kosullari.html'}
HDR_RX = re.compile(r'<header class="hdr.*?</header>|<div class="mnav".*?</div>\s*</div>', re.S)

for en, tr in PAIRS:
    for slug, is_tr in ((en, False), (tr, True)):
        if slug in YASAL or slug == 'index.html':
            continue
        yol = os.path.join(SITE, 'tr', slug) if is_tr else os.path.join(SITE, slug)
        ornek = os.path.join(SITE, 'tr', 'index.html') if is_tr else os.path.join(SITE, 'index.html')
        if not os.path.exists(ornek):
            continue
        s = io.open(ornek, encoding='utf-8').read()
        bas = s.index('<header class="hdr')
        son = s.index('</div>', s.index('mnav__foot'))
        menu = s[bas:son]
        if 'href="%s"' % slug not in menu:
            fails.append('%s/%s : header menusunde yok' % ('TR' if is_tr else 'EN', slug))

print('Denetlenen sayfa: %d' % (len(PAIRS) * 2))
if fails:
    print('\nSORUN (%d):' % len(fails))
    for f in fails:
        print('  X', f)
else:
    print('Tum kontroller gecti.')
