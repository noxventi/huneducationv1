# -*- coding: utf-8 -*-
"""Turkce sayfalarda Ingilizce kalan cerceve metinleri (menu, footer, butonlar).

tr/index.html ve tr/kurslar.html elle yazilmis sayfalar; uretici bunlara
dokunmadigi icin ceviri gecisinde header/footer etiketleri Ingilizce kalmis.
audit_tr.py bunlari yakaladi.
"""
import io, os, sys

SITE = sys.argv[1] if len(sys.argv) > 1 else 'site'

# Her iki sayfada da gecen cerceve metinleri
CERCEVE = [
    ('>Study in Hungary<',  '>Macaristan\'da Eğitim<'),
    ('>Programmes<',        '>Programlar<'),
    ('>Admissions<',        '>Başvuru ve Kabul<'),
    ('>Costs<',             '>Maliyetler<'),
    ('>About Us<',          '>Hakkımızda<'),
    ('>Universities<',      '>Üniversiteler<'),
    ('>What We Do<',        '>Ne Yapıyoruz<'),
    ('>Student Stories<',   '>Öğrenci Hikâyeleri<'),
    ('>Guides<',            '>Rehber<'),
    ('aria-label="Language"', 'aria-label="Dil"'),
    ('aria-label="Quick links"',       'aria-label="Hızlı bağlantılar"'),
    ('<h3>Quick links</h3>',           '<h3>Hızlı bağlantılar</h3>'),
    ('aria-label="Popular programmes"', 'aria-label="Popüler programlar"'),
    ('<h3>Popular programmes</h3>',    '<h3>Popüler programlar</h3>'),
    ('>Medicine<',          '>Tıp<'),
    ('>Dentistry<',         '>Diş Hekimliği<'),
    ('>Engineering<',       '>Mühendislik<'),
    ('>Business<',          '>İşletme<'),
    ('>Psychology<',        '>Psikoloji<'),
    ('>Pilot Training<',    '>Pilotaj<'),
    # butonlar: hem gorunen metin hem data-t degeri
    ('data-t="Show Programmes That Fit Me">Show Programmes That Fit Me<',
     'data-t="Bana Uygun Programları Göster">Bana Uygun Programları Göster<'),
    ('data-t="All Programmes">All Programmes<',
     'data-t="Tüm Programlar">Tüm Programlar<'),
    ('Explore Universities and Programmes',
     'Üniversiteleri ve Programları İnceleyin'),
    ('>All guide content', '>Rehberin tamamı'),
    # program bulucu: Ingilizce alt etiketler
    ('>Lisans<em>Bachelor</em><',        '>Lisans<em>4 yıl, bölüm diploması</em><'),
    ('>Yüksek Lisans<em>Master</em><',   '>Yüksek Lisans<em>2 yıl, lisans üstü</em><'),
]

# Yalnizca tr/index.html: mobil menude iletisim baglantisi yanlis etiketli
SADECE_ANASAYFA = [
    ('<li><a href="iletisim.html" style="--i:6">Hakkımızda</a></li>',
     '<li><a href="iletisim.html" style="--i:6">İletişim</a></li>'),
]

# kurslar.html: JSON-LD icindeki gorunur adlar da Turkce olmali
SADECE_KURSLAR = [
    ('"name": "University Programmes in Hungary"',
     '"name": "Macaristan\'daki Üniversite Programları"'),
    ('"name": "Programmes"', '"name": "Programlar"'),
]

ISLER = [
    ('tr/index.html',   CERCEVE + SADECE_ANASAYFA),
    ('tr/kurslar.html', CERCEVE + SADECE_KURSLAR),
]

for dosya, ciftler in ISLER:
    p = os.path.join(SITE, dosya)
    s = io.open(p, encoding='utf-8').read()
    n = 0
    for a, b in ciftler:
        k = s.count(a)
        if k:
            s = s.replace(a, b); n += k
    io.open(p, 'w', encoding='utf-8').write(s)
    print('%-18s %d degisiklik' % (dosya, n))
