# -*- coding: utf-8 -*-
"""programlar.html -> programs.html (Ingilizce).

Sayfa iskeleti aynidir; yalniz metin, slug ve dil nitelikleri degisir.
Eslesmeyen kalip olursa script bunu bildirir — sessizce Turkce kalan
bir blok olmasin diye.
"""
import io, os, sys

SITE = sys.argv[1]
src = os.path.join(SITE, 'tr', 'programlar.html')
s = io.open(src, encoding='utf-8').read()
# /tr/ kopyasindaki ../assets yollari kokte tekrar assets/ olur
s = s.replace('"../assets/', '"assets/')

R = [
 ('<html lang="tr">', '<html lang="en">'),
 ("<title>Macaristan'da Programlar | Hun Education</title>",
  '<title>University Programmes in Hungary: 490 English-Taught Degrees</title>'),
 ('content="Macaristan\'daki lisans, yüksek lisans, bütünleşik ve hazırlık programlarını seviye, alan, şehir, üniversite ve eğitim diline göre filtreleyin."',
  'content="Filter bachelor’s, master’s, integrated and foundation programmes in Hungary by level, field, city, university and language of instruction."'),
 ('<link rel="canonical" href="https://huneducation.com/tr/programlar/">',
  '<link rel="canonical" href="https://huneducation.com/programs/">'),
 ('<link rel="alternate" hreflang="tr" href="https://huneducation.com/tr/programlar/">\n'
  '<link rel="alternate" hreflang="en" href="https://huneducation.com/programs/">\n'
  '<link rel="alternate" hreflang="x-default" href="https://huneducation.com/programs/">',
  '<link rel="alternate" hreflang="en" href="https://huneducation.com/programs/">\n'
  '<link rel="alternate" hreflang="tr" href="https://huneducation.com/tr/programlar/">\n'
  '<link rel="alternate" hreflang="x-default" href="https://huneducation.com/programs/">'),
 ('<meta property="og:locale" content="tr_TR">',
  '<meta property="og:locale" content="en_GB">\n<meta property="og:locale:alternate" content="tr_TR">'),
 ('<meta property="og:title" content="Macaristan\'da Programlar | Hun Education">',
  '<meta property="og:title" content="University Programmes in Hungary | Hun Education">'),
 ('<meta property="og:description" content="Macaristan\'daki lisans, yüksek lisans, bütünleşik ve hazırlık programlarını seviye, alan, şehir ve bütçeye göre filtreleyin.">',
  '<meta property="og:description" content="Filter bachelor’s, master’s, integrated and foundation programmes in Hungary by level, field, city and budget.">'),
 ('<meta property="og:url" content="https://huneducation.com/tr/programlar/">',
  '<meta property="og:url" content="https://huneducation.com/programs/">'),
 ('<!-- Filtre/sıralama varyasyonları indekslenmez (PRD §11.6) -->',
  '<!-- Filter and sort variations are not indexed (PRD 11.6) -->'),
 ('"@id": "https://huneducation.com/tr/programlar/#page",\n   "url": "https://huneducation.com/tr/programlar/",\n'
  '   "name": "Macaristan\'da Üniversite Programları",\n'
  '   "description": "Macaristan\'daki 40\'ın üzerinde İngilizce üniversite programı; seviye, alan, şehir, üniversite ve bütçeye göre filtrelenebilir katalog.",\n'
  '   "inLanguage": "tr-TR",',
  '"@id": "https://huneducation.com/programs/#page",\n   "url": "https://huneducation.com/programs/",\n'
  '   "name": "University Programmes in Hungary",\n'
  '   "description": "More than 40 English-taught university programmes in Hungary; a catalogue filterable by level, field, city, university and budget.",\n'
  '   "inLanguage": "en-GB",'),
 ('"name": "Ana sayfa",\n     "item": "https://huneducation.com/tr/"',
  '"name": "Home",\n     "item": "https://huneducation.com/"'),
 ('"name": "Programlar",\n     "item": "https://huneducation.com/tr/programlar/"',
  '"name": "Programmes",\n     "item": "https://huneducation.com/programs/"'),
 ('<a class="skip-link" href="#icerik">İçeriğe geç</a>',
  '<a class="skip-link" href="#icerik">Skip to content</a>'),
 ('aria-label="Hun Education ana sayfa"', 'aria-label="Hun Education home"'),
 ('aria-label="Ana menü"', 'aria-label="Main menu"'),
 ('<a class="hdr__link" href="macaristanda-egitim.html">Macaristan\'da Eğitim</a>',
  '<a class="hdr__link" href="study-in-hungary.html">Study in Hungary</a>'),
 ('<a class="hdr__link" href="universiteler.html">Üniversiteler</a>',
  '<a class="hdr__link" href="universities.html">Universities</a>'),
 ('<a class="hdr__link" href="programlar.html" aria-current="page">Programlar</a>',
  '<a class="hdr__link" href="programs.html" aria-current="page">Programmes</a>'),
 ('<a class="hdr__link" href="basvuru.html">Başvuru</a>',
  '<a class="hdr__link" href="admission-requirements.html">Admissions</a>'),
 ('<a class="hdr__link" href="maliyetler.html">Maliyetler</a>',
  '<a class="hdr__link" href="tuition-and-living-costs.html">Costs</a>'),
 ('<a class="hdr__link" href="hakkimizda.html">Hakkımızda</a>',
  '<a class="hdr__link" href="about.html">About Us</a>'),
 ('<div class="lang" role="group" aria-label="Dil seçimi">\n'
  '        <a href="../programs.html" hreflang="en" lang="en"><span>EN</span></a>\n'
  '        <a href="programlar.html" hreflang="tr" lang="tr" aria-current="true"><span>TR</span></a>\n'
  '      </div>',
  '<div class="lang" role="group" aria-label="Language">\n'
  '        <a href="programs.html" hreflang="en" lang="en" aria-current="true"><span>EN</span></a>\n'
  '        <a href="tr/programlar.html" hreflang="tr" lang="tr"><span>TR</span></a>\n'
  '      </div>'),
 ('aria-label="WhatsApp\'tan yazın"', 'aria-label="Message us on WhatsApp"'),
 ('<a class="btn btn--primary btn--sm" href="iletisim.html" data-magnetic>\n'
  '        <span class="btn__label"><span data-t="Ücretsiz Ön Görüşme">Ücretsiz Ön Görüşme</span></span>',
  '<a class="btn btn--primary btn--sm" href="contact.html" data-magnetic>\n'
  '        <span class="btn__label"><span data-t="Free Consultation">Free Consultation</span></span>'),
 ('aria-label="Menüyü aç"', 'aria-label="Open menu"'),
 ('aria-label="Mobil menü"', 'aria-label="Mobile menu"'),
 ('<li><a href="macaristanda-egitim.html" style="--i:0">Macaristan\'da Eğitim</a></li>',
  '<li><a href="study-in-hungary.html" style="--i:0">Study in Hungary</a></li>'),
 ('<li><a href="universiteler.html" style="--i:1">Üniversiteler</a></li>',
  '<li><a href="universities.html" style="--i:1">Universities</a></li>'),
 ('<li><a href="programlar.html" style="--i:2">Programlar</a></li>',
  '<li><a href="programs.html" style="--i:2">Programmes</a></li>'),
 ('<li><a href="basvuru.html" style="--i:3">Başvuru</a></li>',
  '<li><a href="admission-requirements.html" style="--i:3">Admissions</a></li>'),
 ('<li><a href="maliyetler.html" style="--i:4">Maliyetler</a></li>',
  '<li><a href="tuition-and-living-costs.html" style="--i:4">Costs</a></li>'),
 ('<li><a href="hakkimizda.html" style="--i:5">Hakkımızda</a></li>',
  '<li><a href="about.html" style="--i:5">About Us</a></li>'),
 ('<a class="btn btn--primary" href="iletisim.html"><span class="btn__label"><span data-t="Ücretsiz Ön Görüşme Al">Ücretsiz Ön Görüşme Al</span></span></a>',
  '<a class="btn btn--primary" href="contact.html"><span class="btn__label"><span data-t="Book a Free Consultation">Book a Free Consultation</span></span></a>'),
 ('<span data-t="WhatsApp\'tan Sor">WhatsApp\'tan Sor</span>',
  '<span data-t="Ask on WhatsApp">Ask on WhatsApp</span>'),
 ('data-wa-context="Programlar"', 'data-wa-context="Programmes"'),
 ('aria-label="Site yolu"', 'aria-label="Breadcrumb"'),
 ('<a href="index.html">Ana sayfa</a>', '<a href="index.html">Home</a>'),
 ('<span aria-current="page">Programlar</span>', '<span aria-current="page">Programmes</span>'),
 ("Macaristan'daki programları filtreleyin", 'Filter the programmes in Hungary'),
 ('Seviye, alan, şehir, üniversite ve eğitim diline göre daraltın. Seçtiğiniz filtreler\n'
  '      adres çubuğuna yazılır; bağlantıyı ailenizle veya danışmanınızla paylaşabilirsiniz.',
  'Narrow by level, field, city, university and language of instruction. Your filters are written\n'
  '      into the address bar, so you can share the link with your family or your adviser.'),
 ('<p><b>Ücretler yıllık öğrenim ücretidir</b> (pilotajda dönemliktir) ve programa göre değişir.\n'
  '      Katalog, danışmanlık ekibimiz tarafından dönemsel olarak güncellenir (son güncelleme: Ağustos 2026).\n'
  '      Üniversiteler bu koşulları değiştirebilir; nihai bilgi için ilgili üniversitenin resmî\n'
  '      sayfasını esas alınız.</p>',
  '<p><b>Fees shown are annual tuition</b> (per term for pilot training) and vary by programme.\n'
  '      The catalogue is updated periodically by our advisory team (last update: August 2026).\n'
  '      Universities may change these conditions; treat the university’s own official page as\n'
  '      definitive.</p>'),
 ('aria-label="Program filtreleri"', 'aria-label="Programme filters"'),
 ('<h2>Filtreler</h2>', '<h2>Filters</h2>'),
 ('aria-label="Filtreleri kapat"', 'aria-label="Close filters"'),
 ('<label class="field__label" for="q">Anahtar kelime</label>',
  '<label class="field__label" for="q">Keyword</label>'),
 ('placeholder="Örn. tıp, computer, psikoloji"', 'placeholder="e.g. medicine, computer, psychology"'),
 ('<legend>Eğitim seviyesi</legend>', '<legend>Study level</legend>'),
 ('<legend>Alan</legend>', '<legend>Field</legend>'),
 ('<legend>Şehir</legend>', '<legend>City</legend>'),
 ('<legend>Üniversite</legend>', '<legend>University</legend>'),
 ('<legend>Eğitim dili</legend>', '<legend>Language of instruction</legend>'),
 ('<legend>Yıllık bütçe</legend>', '<legend>Annual budget</legend>'),
 ('<span data-t="Sonuçları göster">Sonuçları göster</span>', '<span data-t="Show results">Show results</span>'),
 ('<b data-count>0</b> program\n', '<b data-count>0</b> programmes\n'),
 ('<span data-t="Filtreler">Filtreler</span>', '<span data-t="Filters">Filters</span>'),
 ('<span class="sr-only">Sıralama</span>', '<span class="sr-only">Sort</span>'),
 ('<option value="alpha">Alfabetik (A–Z)</option>', '<option value="alpha">Alphabetical (A–Z)</option>'),
 ('<option value="uni">Üniversiteye göre</option>', '<option value="uni">By university</option>'),
 ('<option value="seviye">Seviyeye göre</option>', '<option value="seviye">By level</option>'),
 ('<span class="cat__active-label num-mono">Seçili:</span>',
  '<span class="cat__active-label num-mono">Selected:</span>'),
 ('<button class="cat__clear" type="button" data-clear-all>Tümünü temizle</button>',
  '<button class="cat__clear" type="button" data-clear-all>Clear all</button>'),
 ('<h3>Bu filtrelerle eşleşen program yok</h3>', '<h3>No programmes match these filters</h3>'),
 ('<p>Bu, aradığınız programın Macaristan\'da bulunmadığı anlamına gelmez — kataloğumuz\n'
  '          doğrulanmış kayıtlarla sınırlıdır. Filtreleri gevşetin ya da doğrudan bize sorun.</p>',
  '<p>That does not mean the programme you are looking for does not exist in Hungary — our\n'
  '          catalogue is limited to verified records. Loosen the filters, or just ask us directly.</p>'),
 ('<span data-t="Filtreleri temizle">Filtreleri temizle</span>',
  '<span data-t="Clear filters">Clear filters</span>'),
 ('<a class="btn btn--primary btn--sm" href="iletisim.html">\n'
  '              <span class="btn__label"><span data-t="Danışmana sor">Danışmana sor</span></span>',
  '<a class="btn btn--primary btn--sm" href="contact.html">\n'
  '              <span class="btn__label"><span data-t="Ask an adviser">Ask an adviser</span></span>'),
 ('<h3>Ne arayacağınızdan emin değil misiniz?</h3>', '<h3>Not sure what to look for?</h3>'),
 ('<p>Danışmanımız akademik geçmişinize göre 3–5 gerçekçi program önerir; neden diğerlerinin\n'
  '          elendiğini de açıklar.</p>',
  '<p>Your adviser will suggest 3–5 realistic programmes based on your academic record — and\n'
  '          explain why the others were ruled out.</p>'),
 ('<a class="btn btn--primary" href="iletisim.html" data-magnetic>\n'
  '          <span class="btn__label"><span data-t="Ücretsiz Ön Görüşme Al">Ücretsiz Ön Görüşme Al</span></span>',
  '<a class="btn btn--primary" href="contact.html" data-magnetic>\n'
  '          <span class="btn__label"><span data-t="Book a Free Consultation">Book a Free Consultation</span></span>'),
 ('Sitede yer alan öğrenim ücretleri, başvuru tarihleri ve kabul koşulları üniversiteler tarafından\n'
  '        değiştirilebilir. Vize ve denklik kararları ilgili resmî kurumlara aittir. Nihai bilgi için\n'
  '        üniversitenin resmî sayfasını ve güncel mevzuatı esas alınız.',
  'Tuition fees, application dates and admission requirements shown on this site may be changed by\n'
  '        the universities. Visa and recognition decisions rest with the relevant official authorities.\n'
  '        Always treat the university’s own page and current legislation as definitive.'),
 ('<nav class="ftr__links" aria-label="Yasal">\n'
  '        <a href="kvkk-aydinlatma.html">KVKK Aydınlatma Metni</a><a href="acik-riza.html">Açık Rıza Metni</a>\n'
  '        <a href="gizlilik-cerez.html">Gizlilik ve Çerez Politikası</a><a href="kullanim-kosullari.html">Kullanım Koşulları</a>\n'
  '      </nav>',
  '<nav class="ftr__links" aria-label="Legal">\n'
  '        <a href="privacy-notice.html">Privacy Notice</a><a href="consent.html">Consent Statement</a>\n'
  '        <a href="cookie-policy.html">Cookie Policy</a><a href="terms-of-use.html">Terms of Use</a>\n'
  '      </nav>'),
 ('· Tüm hakları saklıdır.', '· All rights reserved.'),
 ('<a class="btn btn--primary btn--sm" href="iletisim.html"><span class="btn__label"><span data-t="Ön Görüşme Al">Ön Görüşme Al</span></span></a>',
  '<a class="btn btn--primary btn--sm" href="contact.html"><span class="btn__label"><span data-t="Book a Consultation">Book a Consultation</span></span></a>'),
]

miss = []
for a, b in R:
    if a not in s:
        miss.append(a[:80])
    s = s.replace(a, b)

io.open(os.path.join(SITE, 'programs.html'), 'w', encoding='utf-8').write(s)
print('programs.html yazildi:', len(s), 'byte')
if miss:
    print('ESLESMEYEN KALIP:', len(miss))
    for m in miss:
        print('  !', m)
else:
    print('tum kaliplar eslesti')
