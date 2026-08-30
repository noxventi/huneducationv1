# -*- coding: utf-8 -*-
"""Ana sayfada onceki turda yapilan ton degisikliklerini geri alir.

Geri alinanlar: hero basligi ve girisi, kapanis bolumu basligi ve metni,
sayfa basligi ile aciklamasi, birinci SSS'in govdesi ve JSON-LD karsiligi.
Hem tr/index.html hem index.html icin.
"""
import io

R = {
'site/tr/index.html': [
('<h1 class="hero__title" data-hero="2">Macaristan&rsquo;da İngilizce okuyun, Avrupa&rsquo;da geçerli diploma alın.</h1>',
 '<h1 class="hero__title" data-hero="2">Macaristan&rsquo;da üniversite yolculuğunuzu güvenle planlayın.</h1>'),

("""      <p class="hero__desc" data-hero="3">
        YKS istenmiyor. 20 üniversitede 490 İngilizce program ve yıllık 8.500 &euro;&rsquo;dan
        başlayan toplam bütçe. Başvurudan vizeye, konaklamadan yerleşime kadar 1999&rsquo;dan beri
        yanınızdayız.
      </p>""",
 """      <p class="hero__desc" data-hero="3">
        Hedeflerinize uygun üniversite ve programı birlikte belirleyelim; başvuru ve kabulden
        vize, konaklama ve yerleşime kadar her adımda yanınızda olalım.
      </p>"""),

('<p class="eyebrow" data-reveal="up-sm">İlk adım</p>',
 '<p class="eyebrow" data-reveal="up-sm">Son adım</p>'),

('<h2 class="display h-xl split-mask" id="final-h" data-split>Macaristan&rsquo;da okumaya bugün başlayın.</h2>',
 '<h2 class="display h-xl split-mask" id="final-h" data-split>Hangi programın size uygun olduğundan emin değil misiniz?</h2>'),

("""      <p class="lede" data-reveal="up" data-reveal-delay="500">
        Akademik geçmişinizi paylaşın; hangi üniversitelere gerçekçi şansınız olduğunu ve bütçenizin
        neye yettiğini ilk görüşmede söyleyelim. Ön görüşme ücretsizdir ve sizi hiçbir şeye bağlamaz.
      </p>""",
 """      <p class="lede" data-reveal="up" data-reveal-delay="500">
        Akademik geçmişinizi ve hedeflerinizi birlikte değerlendirelim. Ön görüşme ücretsizdir
        ve sizi hiçbir şeye bağlamaz.
      </p>"""),

("<title>Macaristan'da Üniversite Eğitimi: YKS'siz Kabul, 490 Program | Hun Education</title>",
 "<title>Macaristan'da Üniversite Eğitimi | Hun Education</title>"),

('content="Macaristan\'da İngilizce okuyun, Avrupa\'da geçerli diploma alın. YKS istenmiyor; 20 üniversitede 490 program ve yıllık 8.500 €\'dan başlayan bütçe. 1999\'dan beri başvurudan yerleşime kadar yanınızdayız."',
 'content="1999\'dan beri yalnızca Macaristan\'a odaklanan eğitim danışmanlığı. Program seçiminden başvuruya, vizeden konaklama ve şehir oryantasyonuna kadar Türkiye ve Macaristan\'daki danışmanlarımızla yanınızdayız."'),

("""          <p><b>YKS puanı istenmiyor.</b> Macaristan'daki üniversiteler kendi kabul sürecini yürütüyor:
          lise notlarınıza bakıyor, birçok programda ise konusu belli ve hazırlanabilir bir giriş sınavı
          uyguluyor:</p>""",
 """          <p>Macaristan'daki üniversiteler kendi başvuru ve kabul süreçlerini uygular; YKS puanı genellikle
          bir kabul şartı değildir. Ancak bu &ldquo;sınavsız kabul&rdquo; anlamına gelmez: birçok programın kendi
          giriş sınavı vardır:</p>"""),

("""          <p>Gerekli belgeler: başvuru formu, pasaport fotokopisi, İngilizce ya da onaylı çeviri transkript,
          apostilli diploma ve İngilizce özgeçmiş (tercihen Europass). Banka dökümü başvuruda değil, vize
          aşamasında isteniyor.</p>""",
 """          <p>Gerekli belgeler: başvuru formu, pasaport fotokopisi, İngilizce ya da onaylı çeviri transkript,
          apostilli diploma, son 6 aylık banka hesap dökümü ve İngilizce özgeçmiş (tercihen Europass).</p>"""),

('''    "text": "YKS puanı istenmiyor. Macaristan'daki üniversiteler kendi kabul sürecini yürütür: lise notlarınıza bakar ve birçok programda konusu belli bir giriş sınavı uygular. Sağlık alanlarında kimya-biyoloji, mühendislikte fizik-matematik sınavı, mimarlıkta portfolyo istenir. Türkiye'de denklik için YÖK'ün güncel kurallarını ayrıca incelemeniz gerekir."''',
 '''    "text": "Macaristan'daki üniversiteler kendi başvuru ve kabul süreçlerini uygular; YKS puanı genellikle bir kabul şartı değildir. Ancak bu sınavsız kabul anlamına gelmez: sağlık alanlarında kimya-biyoloji, mühendislikte fizik-matematik sınavı, mimarlıkta portfolyo istenir. Türkiye'de denklik için YÖK'ün güncel kurallarını ayrıca incelemeniz gerekir."'''),
],

'site/index.html': [
('<h1 class="hero__title" data-hero="2">Study in English in Hungary. Graduate with an EU degree.</h1>',
 '<h1 class="hero__title" data-hero="2">Plan your university journey in Hungary with confidence.</h1>'),

("""      <p class="hero__desc" data-hero="3">
        No national entrance exam. 490 English-taught programmes at 20 universities, with a total
        annual budget from &euro;8,500. We have walked students through application, visa,
        accommodation and arrival since 1999.
      </p>""",
 """      <p class="hero__desc" data-hero="3">
        Let us choose the university and programme that match your goals together, and stay with you at
        every step, from the application and offer to your visa, accommodation and arrival.
      </p>"""),

('<p class="eyebrow" data-reveal="up-sm">First step</p>',
 '<p class="eyebrow" data-reveal="up-sm">Last step</p>'),

('<h2 class="display h-xl split-mask" id="final-h" data-split>Start your Hungarian degree today.</h2>',
 '<h2 class="display h-xl split-mask" id="final-h" data-split>Not sure which programme is right for you?</h2>'),

("""      <p class="lede" data-reveal="up" data-reveal-delay="500">
        Send us your academic record and we will tell you in the first conversation which universities
        are realistically within reach and what your budget covers. The consultation is free and
        commits you to nothing.
      </p>""",
 """      <p class="lede" data-reveal="up" data-reveal-delay="500">
        Let us go through your academic record and your goals together. The consultation is free and
        commits you to nothing.
      </p>"""),

("<title>Study at a University in Hungary: 490 English Programmes | Hun Education</title>",
 "<title>Study at a University in Hungary | Hun Education</title>"),

('content="Study in English in Hungary and graduate with an EU degree. No national entrance exam; 490 programmes at 20 universities from €8,500 a year. With you from application to arrival since 1999."',
 'content="Education consultancy focused on one country since 1999. From choosing a programme to applying, and from the student visa to accommodation and settling into your city, our advisers in Hungary are with you at every step."'),

("""          <p><b>No national entrance exam score is required.</b> Hungarian universities run their own
          admission process: they look at your school record, and many programmes set a defined, preparable
          entrance exam of their own:</p>""",
 """          <p>Hungarian universities run their own application and admission process, and a national entrance
          exam score is generally not an admission requirement. But that does not mean “admission without
          an exam”: many programmes set an entrance exam of their own:</p>"""),

("""          <p>Documents required: the application form, a passport copy, a transcript in English or certified
          translation, an apostilled diploma and an English CV (Europass preferred). The bank statement comes
          at the visa stage, not with the application.</p>""",
 """          <p>Documents required: the application form, a passport copy, a transcript in English or certified
          translation, an apostilled diploma, a six-month bank statement and an English CV (Europass preferred).</p>"""),

('''    "text": "No national entrance exam score is required. Hungarian universities run their own admission process: they look at your school record and many programmes set a defined entrance exam. Health programmes set a chemistry and biology exam, engineering a physics and mathematics exam, and architecture asks for a portfolio. For recognition of the degree at home you also need to check your national authority's current rules."''',
 '''    "text": "Hungarian universities run their own application and admission process, and a national entrance exam score is generally not an admission requirement. That does not mean admission without assessment: health programmes set a chemistry and biology exam, engineering a physics and mathematics exam, and architecture asks for a portfolio. For recognition of the degree at home you also need to check your national authority's current rules."'''),
],
}

for yol, ciftler in R.items():
    s = io.open(yol, encoding='utf-8').read()
    n = 0
    for a, b in ciftler:
        if a in s:
            s = s.replace(a, b); n += 1
        else:
            print('  ! zaten geri alinmis ya da eslesmedi: %s :: %s' % (yol, ' '.join(a.split())[:60]))
    io.open(yol, 'w', encoding='utf-8').write(s)
    print('%-20s %d geri alindi' % (yol, n))
