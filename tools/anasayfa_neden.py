# -*- coding: utf-8 -*-
"""Anasayfadaki "Neden Hun Education?" bölümünü sadeleştirir.

NEDEN
  Bölüm dört düz metin kartından ibaretti: her kartta 25 kelimelik bir
  paragraf, toplamda ~150 kelime. Anasayfada bu kartlar okunmuyor,
  taranıyor; taranırken de hepsi aynı griye karışıyordu.

YENİ KURGU
  Giriş cümlesi kısaldı (kelime kelime aydınlanan efekt kalıyor).
  Dört sebep artık çizgi ikonlu kart: kaydırdıkça ikonun konturu
  soldan sağa ÇİZİLİYOR, kartın üstündeki saç teli çizgi ember rengiyle
  doluyor, kart hafifçe yükseliyor. Dördü sırayla açılır, böylece
  bölüm bir ilerleme çubuğu gibi okunur.

  Çizim JS'te ölçülmüyor: her yol pathLength="1" taşıyor, dolayısıyla
  dash uzunluğu 1 birim ve dashoffset doğrudan (1 - ilerleme).
"""
import io, re

IKONLAR = {
 'odak': '''<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true">
      <circle cx="16" cy="16" r="11" pathLength="1"/>
      <circle cx="16" cy="16" r="4.4" pathLength="1"/>
      <path d="M16 1.6v4.2M16 26.2v4.2M1.6 16h4.2M26.2 16h4.2" pathLength="1"/>
    </svg>''',
 'rota': '''<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M5 25C9 12 20 7 27 6.4" pathLength="1"/>
      <circle cx="5" cy="25" r="2.6" pathLength="1"/>
      <path d="M27 6.4l-4.6 1.1M27 6.4l-1.1 4.6" pathLength="1"/>
    </svg>''',
 'danisman': '''<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M6 6h20a2.4 2.4 0 0 1 2.4 2.4v11.2A2.4 2.4 0 0 1 26 22h-9.6L9.6 27v-5H6a2.4 2.4 0 0 1-2.4-2.4V8.4A2.4 2.4 0 0 1 6 6z" pathLength="1"/>
      <path d="M10.4 11.6h11.2M10.4 16.4h7" pathLength="1"/>
    </svg>''',
 'kaynak': '''<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M8.4 3.4h10.2l6.6 6.6v18.2a2.4 2.4 0 0 1-2.4 2.4H8.4A2.4 2.4 0 0 1 6 28.2V5.8a2.4 2.4 0 0 1 2.4-2.4z" pathLength="1"/>
      <path d="M18.6 3.4v6.8h6.6" pathLength="1"/>
      <path d="M11.4 20.6l3.2 3.2 6.2-6.6" pathLength="1"/>
    </svg>''',
}

TR = dict(
  eyebrow='Nasıl çalışıyoruz?',
  h2='Neden Hun Education?',
  lede=('Macaristan&rsquo;da eğitimi genel bilgilerle değil, 1999&rsquo;dan beri bu ülkede\n'
        '      edindiğimiz deneyimle planlarız.'),
  kartlar=[
    ('odak', 'Tek ülke, tam odak',
     'Kural değişince haberden değil, üniversiteden duyarız.'),
    ('rota', 'Türkiye&rsquo;den Macaristan&rsquo;a kesintisiz',
     'Uçağa binince destek bitmez; Budapeşte ekibi devralır.'),
    ('danisman', 'Danışmana doğrudan erişim',
     'Aynı danışman baştan sona; her seferinde yeniden anlatmazsınız.'),
    ('kaynak', 'Kaynağı belli bilgi',
     'Her ücret ve tarih, kaynağı ve güncelleme tarihiyle gelir.'),
  ])

EN = dict(
  eyebrow='How we work',
  h2='Why Hun Education?',
  lede=('We plan your studies in Hungary from experience built in this one country since\n'
        '      1999, not from general information.'),
  kartlar=[
    ('odak', 'One country, full focus',
     'When a rule changes we hear it from the university, not the news.'),
    ('rota', 'Unbroken from home to Hungary',
     'Support does not end at the airport; the Budapest team takes over.'),
    ('danisman', 'Direct access to your adviser',
     'The same adviser throughout, so you never start the story over.'),
    ('kaynak', 'Information with a source',
     'Every fee and date comes with its source and its last update.'),
  ])


def bolum(m):
    kart = []
    for i, (ikon, baslik, satir) in enumerate(m['kartlar']):
        kart.append('''      <li class="mcard" style="--i:%d">
        <i class="mcard__rule" aria-hidden="true"></i>
        <span class="mcard__icon">%s</span>
        <span class="mcard__k num-mono">%02d</span>
        <h3>%s</h3>
        <p>%s</p>
      </li>''' % (i, IKONLAR[ikon], i + 1, baslik, satir))

    return '''<section class="manifesto section" id="macaristan" aria-labelledby="manifesto-h" data-why>
  <div class="shell">
    <p class="eyebrow" data-reveal="up-sm">%s</p>
    <h2 class="sr-only" id="manifesto-h">%s</h2>
    <p class="manifesto__text display scrub-text" data-scrub>
      %s
    </p>

    <ol class="manifesto__grid">
%s
    </ol>
  </div>
</section>''' % (m['eyebrow'], m['h2'], m['lede'], '\n'.join(kart))


for yol, m in (('site/tr/index.html', TR), ('site/index.html', EN)):
    s = io.open(yol, encoding='utf-8').read()
    bas = s.index('<section class="manifesto section"')
    son = s.index('</section>', s.index('manifesto__grid', bas)) + len('</section>')
    s = s[:bas] + bolum(m) + s[son:]
    for zorunlu in ('<header', '<main', '<footer', 'data-why', 'mcard__icon', 'id="surec"'):
        if zorunlu not in s:
            raise SystemExit('DUR: %s kayboldu (%s)' % (zorunlu, yol))
    io.open(yol, 'w', encoding='utf-8').write(s)
    print('  yenilendi:', yol)
