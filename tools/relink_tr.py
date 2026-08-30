# -*- coding: utf-8 -*-
"""Turkce elle yazilmis sayfalardaki INGILIZCE slug'lari Turkcesine cevirir.

    python tools/relink_tr.py site

Neden gerekli: tr/index.html ve tr/kurslar.html, Ingilizce surumden ters
cevirilerek geri uretildi. Metin Turkcelesti ama href'ler Ingilizce canli
slug'larda kaldi. Bu script yalnizca o eslemeyi yapar.
"""
import io, os, sys

SITE = sys.argv[1]

# Ingilizce canli slug -> Turkce canli slug
EN2TR = {
    'why-hungary.html': 'neden-macaristanda-egitim.html',
    'education-in-hungary.html': 'macaristanda-universite-okumak.html',
    'universities.html': 'macaristan-universiteleri.html',
    'courses.html': 'kurslar.html',
    'admission.html': 'macaristan-universite-basvuru-sartlari.html',
    'costs.html': 'macaristan-universite-fiyatlari.html',
    'masters-education-in-hungary.html': 'macaristan-yuksek-lisans.html',
    'studying-medicine-in-hungary-and-pursuing-a-medical-degree-in-hungary.html':
        'macaristanda-tip-egitimi-ve-macaristanda-tip-okumak.html',
    'pilot-training-at-hungarian-universities.html':
        'macaristan-universiteleri-pilotluk-egitimi.html',
    'university-education-and-life-in-hungary-what-you-need-to-know.html':
        'macaristanda-yasam-ve-universite-egitimi-bilinmesi-gerekenler.html',
    'student-perspectives.html': 'macaristan-universiteleri-ogrenci-gorusleri.html',
    'about-us.html': 'hakkimizda.html',
    'contact.html': 'iletisim.html',
    'privacy-notice.html': 'kvkk-aydinlatma.html',
    'consent.html': 'acik-riza.html',
    'cookie-policy.html': 'gizlilik-cerez.html',
    'terms-of-use.html': 'kullanim-kosullari.html',
}

# Uzun slug'lar once degistirilmeli, yoksa kisa olan uzunun icinde eslesir
SIRALI = sorted(EN2TR.items(), key=lambda kv: -len(kv[0]))

for dosya in ('index.html', 'kurslar.html'):
    p = os.path.join(SITE, 'tr', dosya)
    if not os.path.exists(p):
        print('YOK:', p)
        continue
    s = io.open(p, encoding='utf-8').read()
    n = 0
    for en, tr in SIRALI:
        for a, b in ((u'href="%s"' % en, u'href="%s"' % tr),
                     (u'href="%s?' % en, u'href="%s?' % tr),
                     (u'href="%s#' % en, u'href="%s#' % tr)):
            n += s.count(a)
            s = s.replace(a, b)
    # Dil degistirici karsi dile (Ingilizceye) gitmeli: geri cevrilmemeli
    s = s.replace('href="../kurslar.html" hreflang="en"', 'href="../courses.html" hreflang="en"')
    s = s.replace('href="../iletisim.html" hreflang="en"', 'href="../contact.html" hreflang="en"')
    io.open(p, 'w', encoding='utf-8').write(s)
    print('tr/%s : %d baglanti Turkcelestirildi' % (dosya, n))
