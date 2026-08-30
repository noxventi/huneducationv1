# -*- coding: utf-8 -*-
"""Ana sayfadaki "Kısaca" bölümünü yeniden yazar.

ANAHTAR KELİME STRATEJİSİ
  Hedef terimler tahminle değil, canlı sitenin kendi slug'larından
  alındı: "Macaristan'da üniversite okumak", "Macaristan üniversiteleri",
  "Macaristan üniversite fiyatları", "Macaristan üniversite başvuru
  şartları", "Macaristan'da tıp eğitimi", "Macaristan pilotluk eğitimi",
  "Macaristan yüksek lisans". Başlık, birincil terimi soru biçiminde
  taşır; cevap motorları soru-cevap eşleşmesini bu biçimde çıkarır.

GEO (cevap motoru) GEREKLERİ
  - İlk cümle soruyu doğrudan cevaplar, bağlam cümlesiyle başlamaz.
  - Paragraf ~70 kelime: alıntılanabilir uzunluk.
  - Adlandırılmış varlıklar geçer (Semmelweis, Debrecen, Pécs, Szeged,
    Budapeşte, YÖK, Bologna, AKTS) çünkü varlık bağlantısı alıntılanma
    olasılığını artırır.
  - Her rakam kendi satırında, terim/değer/açıklama üçlüsü olarak durur;
    tanım listesi bu üçlünün en net taşıyıcısıdır.
  - Güncelleme tarihi görünür: tazelik sinyali.

GÖRSEL
  Her bilgi satırı ayrı bir kart; değer görsel olarak öne çıkar, açıklama
  arkasında durur. Satırlar kademeli olarak belirir (reveal altyapısının
  --i değişkeni). Rakamlar tabular-nums ile hizalanır.
"""
import io, re, sys

SITE = sys.argv[1] if len(sys.argv) > 1 else 'site'

TR = '''<div class="shell brief">
    <div class="brief__head">
      <p class="eyebrow" data-reveal="up-sm">Kısaca</p>
      <h2 class="h-md display" id="ozet-h" data-reveal="up">Macaristan&rsquo;da üniversite<br>okumak nasıl işler?</h2>
    </div>

    <div class="brief__body">
      <p class="brief__lead" data-reveal="up">
        <b>Macaristan&rsquo;da üniversite okumak</b>, İngilizce eğitim alarak Avrupa Birliği üyesi bir
        ülkeden diploma edinmenin en erişilebilir yollarından biridir. Üniversiteler YKS puanı istemez;
        her fakülte kendi giriş değerlendirmesini yapar. Bir akademik yılın öğrenim ve yaşam gideri
        birlikte <b>8.500 – 14.000 €</b> aralığında kalır. Semmelweis, Debrecen, Pécs ve Szeged gibi
        köklü üniversitelerde tıp, mühendislik, işletme ve pilotaj programları İngilizce yürütülür.
      </p>
      <p class="brief__sub" data-reveal="up" data-reveal-delay="90">
        Hun Education olarak 1999&rsquo;dan bu yana yalnızca Macaristan&rsquo;da eğitim alanına
        odaklanıyor, <a class="link" href="macaristan-universiteleri.html">20 üniversitede</a> sunulan
        <a class="link" href="kurslar.html">490 İngilizce program</a> arasından öğrencilerimize uygun
        olanı belirliyoruz.
      </p>
    </div>

    <dl class="brief__facts">
      <div data-reveal="up">
        <dt>Eğitim dili</dt>
        <dd><b>İngilizce</b><span>Kataloğumuzdaki 490 programın tamamı İngilizce yürütülür; başvuru için Macarca gerekmez.</span></dd>
      </div>
      <div data-reveal="up">
        <dt>Giriş şartı</dt>
        <dd><b>YKS puanı istenmez</b><span>Tıp, mühendislik, mimarlık ve sanat programlarında üniversitenin kendi giriş sınavı uygulanır.</span></dd>
      </div>
      <div data-reveal="up">
        <dt>Yıllık öğrenim ücreti</dt>
        <dd><b class="num-mono">3.000 – 5.000 €</b><span>Lisans seviyesinde. Tıpta 15.800 € ile 19.900 $, yüksek lisansta 4.000 – 6.000 € arasındadır.</span></dd>
      </div>
      <div data-reveal="up">
        <dt>Yıllık yaşam gideri</dt>
        <dd><b class="num-mono">4.000 – 8.000 €</b><span>Konaklama tercihi belirleyicidir; Budapeşte dışındaki şehirlerde belirgin şekilde düşer.</span></dd>
      </div>
      <div data-reveal="up">
        <dt>Üniversite ve program</dt>
        <dd><b class="num-mono">20 üniversite · 490 program</b><span>Budapeşte, Debrecen, Szeged ve Pécs başta olmak üzere sekiz şehirde.</span></dd>
      </div>
      <div data-reveal="up">
        <dt>Başvuru dönemleri</dt>
        <dd><b>Eylül ve Şubat</b><span>Eylül dönemi Nisan–Haziran, Şubat dönemi Ekim sonu–Kasım arasında kapanır.</span></dd>
      </div>
      <div data-reveal="up">
        <dt>Diploma</dt>
        <dd><b>Bologna · AKTS</b><span>Programlar Avrupa Yükseköğretim Alanı yapısındadır. Türkiye&rsquo;de kullanım için YÖK denkliği gerekir.</span></dd>
      </div>
      <div class="brief__cta" data-reveal="up">
        <p>Hangi programa gerçekçi şansınız olduğunu ilk görüşmede söyleriz.</p>
        <a class="btn btn--primary btn--sm" href="iletisim.html" data-magnetic><span class="btn__label"><span data-t="Ücretsiz Ön Görüşme">Ücretsiz Ön Görüşme</span></span></a>
      </div>
    </dl>

    <p class="brief__meta">
      Ücret, takvim ve kabul koşulları üniversitelerin güncel yayınlarından derlenir.
      <time datetime="2026-08-09">Son güncelleme: 9 Ağustos 2026</time>
    </p>
  </div>'''

EN = '''<div class="shell brief">
    <div class="brief__head">
      <p class="eyebrow" data-reveal="up-sm">In brief</p>
      <h2 class="h-md display" id="ozet-h" data-reveal="up">How does studying at a<br>Hungarian university work?</h2>
    </div>

    <div class="brief__body">
      <p class="brief__lead" data-reveal="up">
        <b>Studying at a university in Hungary</b> is one of the most accessible routes to a degree from
        an EU member state, taught entirely in English. Universities do not ask for a national entrance
        exam score; each faculty runs its own assessment. Tuition and living costs together come to
        <b>&euro;8,500 &ndash; &euro;14,000</b> for an academic year. Long-established universities such as
        Semmelweis, Debrecen, P&eacute;cs and Szeged teach medicine, engineering, business and pilot
        training in English.
      </p>
      <p class="brief__sub" data-reveal="up" data-reveal-delay="90">
        Hun Education has focused on this one country since 1999. We match students to the right option
        among <a class="link" href="universities.html">20 universities</a> and
        <a class="link" href="courses.html">490 English-taught programmes</a>.
      </p>
    </div>

    <dl class="brief__facts">
      <div data-reveal="up">
        <dt>Language</dt>
        <dd><b>English</b><span>All 490 programmes in our catalogue are taught in English; Hungarian is not required to apply.</span></dd>
      </div>
      <div data-reveal="up">
        <dt>Admission</dt>
        <dd><b>No entrance exam score</b><span>Medicine, engineering, architecture and arts programmes set their own entrance exam.</span></dd>
      </div>
      <div data-reveal="up">
        <dt>Annual tuition</dt>
        <dd><b class="num-mono">&euro;3,000 &ndash; &euro;5,000</b><span>At bachelor&rsquo;s level. Medicine runs &euro;15,800 to $19,900 and master&rsquo;s &euro;4,000 &ndash; &euro;6,000.</span></dd>
      </div>
      <div data-reveal="up">
        <dt>Annual living costs</dt>
        <dd><b class="num-mono">&euro;4,000 &ndash; &euro;8,000</b><span>Accommodation is the deciding factor; cities outside Budapest are noticeably cheaper.</span></dd>
      </div>
      <div data-reveal="up">
        <dt>Universities and programmes</dt>
        <dd><b class="num-mono">20 universities &middot; 490 programmes</b><span>Across eight cities, led by Budapest, Debrecen, Szeged and P&eacute;cs.</span></dd>
      </div>
      <div data-reveal="up">
        <dt>Intakes</dt>
        <dd><b>September and February</b><span>September applications close April&ndash;June; February applications close late October&ndash;November.</span></dd>
      </div>
      <div data-reveal="up">
        <dt>The degree</dt>
        <dd><b>Bologna &middot; ECTS</b><span>Programmes sit inside the European Higher Education Area. Using the degree at home goes through your national authority.</span></dd>
      </div>
      <div class="brief__cta" data-reveal="up">
        <p>We will tell you which programmes are realistically within reach in the first conversation.</p>
        <a class="btn btn--primary btn--sm" href="contact.html" data-magnetic><span class="btn__label"><span data-t="Free Consultation">Free Consultation</span></span></a>
      </div>
    </dl>

    <p class="brief__meta">
      Fees, dates and admission conditions are compiled from the universities&rsquo; current publications.
      <time datetime="2026-08-09">Last updated: 9 August 2026</time>
    </p>
  </div>'''

BLOK = re.compile(r'<div class="shell brief"[^>]*>.*?\n  </div>', re.S)

for yol, yeni in ((SITE + '/tr/index.html', TR), (SITE + '/index.html', EN)):
    s = io.open(yol, encoding='utf-8').read()
    if not BLOK.search(s):
        print('  ! blok bulunamadı:', yol); continue
    s2 = BLOK.sub(lambda m: yeni, s, count=1)
    for zorunlu in ('<header class="hdr', '<main', '</main>', '<footer', 'id="ozet-h"'):
        if zorunlu not in s2:
            print('  ! %s kayboldu, yazma iptal: %s' % (zorunlu, yol)); break
    else:
        io.open(yol, 'w', encoding='utf-8').write(s2)
        print('%-22s özet bölümü yenilendi' % yol)
