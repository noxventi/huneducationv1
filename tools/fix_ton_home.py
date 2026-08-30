# -*- coding: utf-8 -*-
"""Ana sayfa: hero ve kapanis cagrisi sonuc odakli hale getiriliyor.

Onceki metin sureci anlatiyordu ("yolculugunuzu planlayin", "birlikte
belirleyelim"). Ziyaretci once sonucu gormek istiyor: nerede, hangi
dilde, ne kadara okuyacagi. Rakamlar sitedeki diger sayfalarla ayni.

Kapanis basligi da "Son adim / emin degil misiniz?" yerine "Ilk adim /
bugun baslayin" oluyor; ziyaretci icin burasi sonu degil basi.
"""
import io

R = {
'site/tr/index.html': [
('<h1 class="hero__title" data-hero="2">Macaristan&rsquo;da üniversite yolculuğunuzu güvenle planlayın.</h1>',
 '<h1 class="hero__title" data-hero="2">Macaristan&rsquo;da İngilizce okuyun, Avrupa&rsquo;da geçerli diploma alın.</h1>'),

("""      <p class="hero__desc" data-hero="3">
        Hedeflerinize uygun üniversite ve programı birlikte belirleyelim; başvuru ve kabulden
        vize, konaklama ve yerleşime kadar her adımda yanınızda olalım.
      </p>""",
 """      <p class="hero__desc" data-hero="3">
        YKS istenmiyor. 20 üniversitede 490 İngilizce program ve yıllık 8.500 &euro;&rsquo;dan
        başlayan toplam bütçe. Başvurudan vizeye, konaklamadan yerleşime kadar 1999&rsquo;dan beri
        yanınızdayız.
      </p>"""),

('<p class="eyebrow" data-reveal="up-sm">Son adım</p>',
 '<p class="eyebrow" data-reveal="up-sm">İlk adım</p>'),

('<h2 class="display h-xl split-mask" id="final-h" data-split>Hangi programın size uygun olduğundan emin değil misiniz?</h2>',
 '<h2 class="display h-xl split-mask" id="final-h" data-split>Macaristan&rsquo;da okumaya bugün başlayın.</h2>'),

("""      <p class="lede" data-reveal="up" data-reveal-delay="500">
        Akademik geçmişinizi ve hedeflerinizi birlikte değerlendirelim. Ön görüşme ücretsizdir
        ve sizi hiçbir şeye bağlamaz.
      </p>""",
 """      <p class="lede" data-reveal="up" data-reveal-delay="500">
        Akademik geçmişinizi paylaşın; hangi üniversitelere gerçekçi şansınız olduğunu ve bütçenizin
        neye yettiğini ilk görüşmede söyleyelim. Ön görüşme ücretsizdir ve sizi hiçbir şeye bağlamaz.
      </p>"""),
],

'site/index.html': [
('<h1 class="hero__title" data-hero="2">Plan your university journey in Hungary with confidence.</h1>',
 '<h1 class="hero__title" data-hero="2">Study in English in Hungary. Graduate with an EU degree.</h1>'),

("""      <p class="hero__desc" data-hero="3">
        Let us choose the university and programme that match your goals together, and stay with you at
        every step, from the application and offer to your visa, accommodation and arrival.
      </p>""",
 """      <p class="hero__desc" data-hero="3">
        No national entrance exam. 490 English-taught programmes at 20 universities, with a total
        annual budget from &euro;8,500. We have walked students through application, visa,
        accommodation and arrival since 1999.
      </p>"""),

('<p class="eyebrow" data-reveal="up-sm">Last step</p>',
 '<p class="eyebrow" data-reveal="up-sm">First step</p>'),

('<h2 class="display h-xl split-mask" id="final-h" data-split>Not sure which programme is right for you?</h2>',
 '<h2 class="display h-xl split-mask" id="final-h" data-split>Start your Hungarian degree today.</h2>'),

("""      <p class="lede" data-reveal="up" data-reveal-delay="500">
        Let us go through your academic record and your goals together. The consultation is free and
        commits you to nothing.
      </p>""",
 """      <p class="lede" data-reveal="up" data-reveal-delay="500">
        Send us your academic record and we will tell you in the first conversation which universities
        are realistically within reach and what your budget covers. The consultation is free and
        commits you to nothing.
      </p>"""),
],
}

for yol, ciftler in R.items():
    s = io.open(yol, encoding='utf-8').read()
    n = 0
    for a, b in ciftler:
        if a in s:
            s = s.replace(a, b); n += 1
        else:
            print('  ! eslesmedi %s :: %s' % (yol, ' '.join(a.split())[:68]))
    io.open(yol, 'w', encoding='utf-8').write(s)
    print('%-20s %d degisiklik' % (yol, n))
