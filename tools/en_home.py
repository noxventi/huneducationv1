# -*- coding: utf-8 -*-
"""tr/index.html -> index.html (Ingilizce ana sayfa).

Kaynak olarak /tr/ kopyasi alinir cunku dil degistirici ve hreflang
oradaki yapiyla ayni; yalniz yon tersine cevrilir. Eslesmeyen kalip
kalirsa script bunu bildirir, boylece sessizce Turkce kalan bir blok
olusmaz.

Hero metinleri kullanicinin verdigi Turkce brief'in birebir karsiligidir:
ayni yapisal rol (eyebrow / H1 / aciklama / iki CTA / guven satiri),
Ingilizce'de dogal duracak sekilde yeniden yazilmis hali.
"""
import io, os, re, sys

SITE = sys.argv[1]
s = io.open(os.path.join(SITE, 'tr', 'index.html'), encoding='utf-8').read()
s = s.replace('"../assets/', '"assets/').replace(' ../assets/', ' assets/')

R = [
# ---------------------------------------------------------------- head
('<html lang="tr">', '<html lang="en">'),
("<title>Macaristan'da Üniversite Eğitimi | Hun Education</title>",
 '<title>Study at a University in Hungary | Hun Education</title>'),
('<meta name="description" content="1999\'dan beri yalnızca Macaristan\'a odaklanan eğitim danışmanlığı. Program seçiminden başvuruya, vizeden konaklama ve şehir oryantasyonuna kadar Türkiye ve Macaristan\'daki danışmanlarımızla yanınızdayız.">',
 '<meta name="description" content="Education consultancy focused on one country since 1999. From choosing a programme to applying, and from the student visa to accommodation and settling into your city, our advisers in Hungary are with you at every step.">'),
('<link rel="canonical" href="https://huneducation.com/tr/">',
 '<link rel="canonical" href="https://huneducation.com/">'),
('<link rel="alternate" hreflang="tr" href="https://huneducation.com/tr/">\n'
 '<link rel="alternate" hreflang="en" href="https://huneducation.com/">\n'
 '<link rel="alternate" hreflang="x-default" href="https://huneducation.com/">',
 '<link rel="alternate" hreflang="en" href="https://huneducation.com/">\n'
 '<link rel="alternate" hreflang="tr" href="https://huneducation.com/tr/">\n'
 '<link rel="alternate" hreflang="x-default" href="https://huneducation.com/">'),
('<meta property="og:locale" content="tr_TR">',
 '<meta property="og:locale" content="en_GB">\n<meta property="og:locale:alternate" content="tr_TR">'),
('<meta property="og:title" content="Macaristan\'da Üniversite Eğitimi | Hun Education">',
 '<meta property="og:title" content="Study at a University in Hungary | Hun Education">'),
('<meta property="og:description" content="Macaristan\'daki doğru üniversiteyi birlikte bulalım. 1999\'dan beri tek ülkeye odaklanan akademik danışmanlık.">',
 '<meta property="og:description" content="Let us find the right university in Hungary together. Academic consultancy focused on one country since 1999.">'),
('<meta property="og:url" content="https://huneducation.com/tr/">',
 '<meta property="og:url" content="https://huneducation.com/">'),
('<meta name="twitter:title" content="Macaristan\'da Üniversite Eğitimi | Hun Education">',
 '<meta name="twitter:title" content="Study at a University in Hungary | Hun Education">'),
('<meta name="twitter:description" content="Macaristan\'daki doğru üniversiteyi birlikte bulalım. 1999\'dan beri tek ülkeye odaklanan akademik danışmanlık.">',
 '<meta name="twitter:description" content="Let us find the right university in Hungary together. Academic consultancy focused on one country since 1999.">'),
('<!-- Yapılandırılmış veri: yalnızca sayfada GÖRÜNEN ve doğrulanmış iddialar.\n'
 '     Öğrenci sayısı, partnerlik vb. doğrulanana kadar JSON-LD\'ye eklenmez. -->',
 '<!-- Structured data: only claims that are VISIBLE on the page and verified.\n'
 '     Student numbers, partnerships etc. stay out of the JSON-LD until verified. -->'),
('"description": "1999\'dan beri Macaristan\'da lisans, yüksek lisans ve hazırlık eğitimi konusunda uzmanlaşmış eğitim danışmanlığı."',
 '"description": "Education consultancy specialising in bachelor\'s, master\'s and foundation studies in Hungary since 1999."'),
('"inLanguage": "tr-TR",\n      "publisher"', '"inLanguage": "en-GB",\n      "publisher"'),
('"urlTemplate": "https://huneducation.com/tr/programlar/?q={search_term_string}"',
 '"urlTemplate": "https://huneducation.com/programs/?q={search_term_string}"'),

# ---------------------------------------------------------------- FAQ JSON-LD
('"name": "YKS\'ye girmem gerekiyor mu?"', '"name": "Do I need a national entrance exam?"'),
('"text": "Macaristan\'daki üniversiteler kendi başvuru ve kabul süreçlerini uygular; YKS puanı genellikle bir kabul şartı değildir. Ancak bu sınavsız kabul anlamına gelmez: sağlık alanlarında kimya-biyoloji, mühendislikte fizik-matematik sınavı, mimarlıkta portfolyo istenir. Türkiye\'de denklik için YÖK\'ün güncel kurallarını ayrıca incelemeniz gerekir."',
 '"text": "Hungarian universities run their own application and admission process, and a national entrance exam score is generally not an admission requirement. That does not mean admission without assessment: health programmes set a chemistry and biology exam, engineering a physics and mathematics exam, and architecture asks for a portfolio. For recognition of the degree at home you also need to check your national authority\'s current rules."'),
('"name": "İngilizce dil belgesi şart mı?"', '"name": "Do I need an English language certificate?"'),
('"text": "Lisansta en az B2 seviyesi beklenir; bazı okullar IELTS 5, 6 veya 6.5 puan belgesi ister. Yüksek lisansta genellikle IELTS 6.5 veya eşdeğeri gerekir. B2 seviyesinde değilseniz üniversitelerin İngilizce Dil Hazırlık programlarına başvurabilirsiniz; ücreti dönemlik 2.500 €\'dan başlar."',
 '"text": "Bachelor\'s programmes expect at least B2; some universities ask for an IELTS score of 5, 6 or 6.5. Master\'s programmes usually require IELTS 6.5 or equivalent. If you are not at B2 you can apply to the universities\' English Language Foundation programmes, which start from EUR 2,500 per term."'),
('"name": "Başvurular ne zaman açılıyor?"', '"name": "When do applications open?"'),
('"text": "Macaristan\'da iki başlangıç dönemi vardır. Eylül (güz) dönemi için başvuruların Nisan, Mayıs veya Haziran ayına kadar; Şubat (bahar) dönemi için Ekim sonuna, en geç Kasım ayına kadar yapılması gerekir. Kontenjan dolduğunda dönem erken kapanabilir."',
 '"text": "Hungary has two intakes. For the September (autumn) intake, applications must be in by April, May or June; for the February (spring) intake, by the end of October and at the latest November. An intake can close early once places run out."'),
('"name": "Toplam maliyet ne kadar tutar?"', '"name": "What does it cost in total?"'),
('"text": "Eğitim ve yaşam giderleri birlikte yıllık 8.500 – 14.000 € aralığındadır. Öğrenim ücreti lisansta 3.000–5.000 €, yüksek lisansta 4.000–6.000 €, tıp ve diş hekimliğinde 16.000–17.350 €\'dur. Konaklama tercihi (yurt 60–400 €, kiralık oda ≈350 €, stüdyo ≈550 €/ay) bütçenin en oynak kalemidir."',
 '"text": "Tuition and living costs together run EUR 8,500 to 14,000 a year. Tuition is EUR 3,000-5,000 for a bachelor\'s, 4,000-6,000 for a master\'s and 16,000-17,350 for medicine and dentistry. Accommodation is the most volatile item in the budget: a dormitory is EUR 60-400, a rented room around 350 and a studio flat around 550 a month."'),
('"name": "Vize sürecinde destek veriliyor mu?"', '"name": "Do you support the visa process?"'),
('"text": "Evet; kabul mektubu sonrası konsolosluk için belge listesi hazırlanır, randevu ve dosya birlikte kontrol edilir. Vize kararı tamamen resmî makama aittir; hiçbir danışmanlık şirketi vize garantisi veremez. Vize alınamaması durumunda ödenen öğrenim ücreti 30 iş günü içinde iade edilir."',
 '"text": "Yes. After your acceptance letter we prepare the document list for the consulate and check the appointment and the file with you. The visa decision rests entirely with the official authority; no consultancy can guarantee a visa. If the visa is refused, tuition already paid is refunded within 30 working days."'),
('"name": "Diplomam Türkiye\'de tanınır mı?"', '"name": "Will my degree be recognised at home?"'),
('"text": "Yurt dışı diplomasının Türkiye\'de kullanılması için YÖK denklik değerlendirmesi gerekir. Denklik; üniversitenin tanınırlığı, program içeriği, eğitim süresi ve mezuniyet koşullarına göre değerlendirilir ve bazı alanlarda ek sınav istenebilir. Başvuru öncesinde YÖK\'ün güncel mevzuatını incelemenizi öneririz; otomatik denklik garantisi yoktur."',
 '"text": "Using a foreign degree in your own country normally requires a recognition assessment by the competent national authority. Recognition is judged on the university\'s standing, the content of the programme, the length of study and the graduation conditions, and some fields require an additional exam. Check your national authority\'s current rules before you apply; there is no guarantee of automatic recognition."'),

# ---------------------------------------------------------------- chrome
('<a class="skip-link" href="#icerik">İçeriğe geç</a>', '<a class="skip-link" href="#icerik">Skip to content</a>'),
('<!-- ============ AÇILIŞ PERDESİ ============ -->', '<!-- ============ OPENING CURTAIN ============ -->'),
('<!-- ============ ÖZEL İMLEÇ ============ -->', '<!-- ============ CUSTOM CURSOR ============ -->'),
('<!-- ============ MOBİL MENÜ ============ -->', '<!-- ============ MOBILE MENU ============ -->'),
('<!-- ============ MOBİL SABİT CTA ============ -->', '<!-- ============ STICKY MOBILE CTA ============ -->'),
('aria-label="Hun Education ana sayfa"', 'aria-label="Hun Education home"'),
('aria-label="Ana menü"', 'aria-label="Main menu"'),
('<a class="hdr__link" href="macaristanda-egitim.html">Macaristan\'da Eğitim</a>',
 '<a class="hdr__link" href="study-in-hungary.html">Study in Hungary</a>'),
('<a class="hdr__link" href="universiteler.html">Üniversiteler</a>',
 '<a class="hdr__link" href="universities.html">Universities</a>'),
('<a class="hdr__link" href="programlar.html">Programlar</a>',
 '<a class="hdr__link" href="programs.html">Programmes</a>'),
('<a class="hdr__link" href="basvuru.html">Başvuru</a>',
 '<a class="hdr__link" href="admission-requirements.html">Admissions</a>'),
('<a class="hdr__link" href="maliyetler.html">Maliyetler</a>',
 '<a class="hdr__link" href="tuition-and-living-costs.html">Costs</a>'),
('<a class="hdr__link" href="hakkimizda.html">Hakkımızda</a>',
 '<a class="hdr__link" href="about.html">About Us</a>'),
('<div class="lang" role="group" aria-label="Dil seçimi">\n'
 '        <a href="../index.html" hreflang="en" lang="en"><span>EN</span></a>\n'
 '        <a href="index.html" hreflang="tr" lang="tr" aria-current="true"><span>TR</span></a>\n'
 '      </div>',
 '<div class="lang" role="group" aria-label="Language">\n'
 '        <a href="index.html" hreflang="en" lang="en" aria-current="true"><span>EN</span></a>\n'
 '        <a href="tr/index.html" hreflang="tr" lang="tr"><span>TR</span></a>\n'
 '      </div>'),
('<div class="lang" role="group" aria-label="Dil seçimi" style="width:max-content">\n'
 '      <a href="../index.html" hreflang="en" lang="en"><span>EN</span></a><a href="index.html" hreflang="tr" lang="tr" aria-current="true"><span>TR</span></a>\n'
 '    </div>',
 '<div class="lang" role="group" aria-label="Language" style="width:max-content">\n'
 '      <a href="index.html" hreflang="en" lang="en" aria-current="true"><span>EN</span></a><a href="tr/index.html" hreflang="tr" lang="tr"><span>TR</span></a>\n'
 '    </div>'),
('aria-label="WhatsApp\'tan yazın"', 'aria-label="Message us on WhatsApp"'),
('<a class="btn btn--primary btn--sm" href="iletisim.html" data-magnetic>\n'
 '        <span class="btn__label"><span data-t="Ücretsiz Ön Görüşme">Ücretsiz Ön Görüşme</span></span>',
 '<a class="btn btn--primary btn--sm" href="contact.html" data-magnetic>\n'
 '        <span class="btn__label"><span data-t="Free Consultation">Free Consultation</span></span>'),
('aria-label="Menüyü aç"', 'aria-label="Open menu"'),
('aria-label="Mobil menü"', 'aria-label="Mobile menu"'),
('<li><a href="macaristanda-egitim.html" style="--i:0">Macaristan\'da Eğitim</a>\n'
 '        <div class="mnav__sub">\n'
 '          <a href="macaristanda-egitim.html">Neden Macaristan?</a><a href="hakkimizda.html">Başvuru ve Kabul</a><a href="#maliyet">Maliyetler</a><a href="hakkimizda.html">Vize ve Oturum</a>\n'
 '        </div>\n'
 '      </li>',
 '<li><a href="study-in-hungary.html" style="--i:0">Study in Hungary</a>\n'
 '        <div class="mnav__sub">\n'
 '          <a href="study-in-hungary.html">Why Hungary?</a><a href="admission-requirements.html">Admissions</a><a href="#maliyet">Costs</a><a href="study-in-hungary.html#visa">Visa &amp; Residence</a>\n'
 '        </div>\n'
 '      </li>'),
('<li><a href="universiteler.html" style="--i:1">Üniversiteler</a></li>',
 '<li><a href="universities.html" style="--i:1">Universities</a></li>'),
('<li><a href="programlar.html" style="--i:2">Programlar</a></li>',
 '<li><a href="programs.html" style="--i:2">Programmes</a></li>'),
('<li><a href="hakkimizda.html" style="--i:3">Hizmetlerimiz</a></li>',
 '<li><a href="about.html" style="--i:3">What We Do</a></li>'),
('<li><a href="#hikayeler" style="--i:4">Öğrenci Hikâyeleri</a></li>',
 '<li><a href="#hikayeler" style="--i:4">Student Stories</a></li>'),
('<li><a href="#rehber" style="--i:5">Rehber</a></li>',
 '<li><a href="#rehber" style="--i:5">Guides</a></li>'),
('<li><a href="iletisim.html" style="--i:6">Hakkımızda</a></li>',
 '<li><a href="contact.html" style="--i:6">Contact</a></li>'),
('<a class="btn btn--primary" href="iletisim.html"><span class="btn__label"><span data-t="Ücretsiz Ön Görüşme Al">Ücretsiz Ön Görüşme Al</span></span></a>',
 '<a class="btn btn--primary" href="contact.html"><span class="btn__label"><span data-t="Book a Free Consultation">Book a Free Consultation</span></span></a>'),
('<span data-t="WhatsApp\'tan Sor">WhatsApp\'tan Sor</span>', '<span data-t="Ask on WhatsApp">Ask on WhatsApp</span>'),

# ---------------------------------------------------------------- hero
('<!-- ==================================================================\n     BÖLÜM 2 — HERO',
 '<!-- ==================================================================\n     SECTION 2 - HERO'),
('<p class="hero__eyebrow" data-hero="1">1999&rsquo;dan beri yalnızca Macaristan</p>',
 '<p class="hero__eyebrow" data-hero="1">Hungary only, since 1999</p>'),
('<h1 class="hero__title" data-hero="2">Macaristan&rsquo;da üniversite yolculuğunuzu güvenle planlayın.</h1>',
 '<h1 class="hero__title" data-hero="2">Plan your university journey in Hungary with confidence.</h1>'),
('Hedeflerinize uygun üniversite ve programı birlikte belirleyelim; başvuru ve kabulden\n'
 '        vize, konaklama ve yerleşime kadar her adımda yanınızda olalım.',
 'Let us choose the university and programme that match your goals together, and stay with you at\n'
 '        every step — from the application and offer to your visa, accommodation and arrival.'),
('<a class="hbtn hbtn--primary" href="iletisim.html">Ücretsiz Ön Değerlendirme Al</a>',
 '<a class="hbtn hbtn--primary" href="contact.html">Get a Free Assessment</a>'),
('<a class="hbtn hbtn--ghost" href="programlar.html">\n          Üniversite ve Programları İncele',
 '<a class="hbtn hbtn--ghost" href="programs.html">\n          Explore Universities and Programmes'),
('<span class="hero__trust-full">Budapeşte merkez ofisi &bull; Türkiye ve Macaristan&rsquo;da yerinde destek</span>',
 '<span class="hero__trust-full">Head office in Budapest &bull; On-the-ground support in Hungary and Türkiye</span>'),
('<span class="hero__trust-short">Budapeşte merkez ofisi &bull; Yerinde destek</span>',
 '<span class="hero__trust-short">Budapest head office &bull; On-the-ground support</span>'),

# ---------------------------------------------------------------- trust band
('<!-- ==================================================================\n     BÖLÜM 3 — GÜVEN BANDI',
 '<!-- ==================================================================\n     SECTION 3 - TRUST BAND'),
('<h2 id="trust-h" class="sr-only">Hun Education\'a neden güvenilir?</h2>',
 '<h2 id="trust-h" class="sr-only">Why students trust Hun Education</h2>'),
('<span>Yalnızca Macaristan</span>', '<span>Hungary only</span>'),
('<span>Budapeşte merkez ofis</span>', '<span>Budapest head office</span>'),
('<span>Türkiye &amp; Macaristan danışman ağı</span>', '<span>Adviser network in two countries</span>'),
('<span>Başvurudan yerleşime</span>', '<span>From application to arrival</span>'),
("<span>1999'dan beri</span>", '<span>Since 1999</span>'),
('<p class="trust__label">Macaristan&rsquo;da kesintisiz faaliyet. Ülkedeki ilk Türk eğitim\n      danışmanlığı kurumu.</p>',
 '<p class="trust__label">Operating without interruption in Hungary. The first Turkish education\n      consultancy established in the country.</p>'),
('<span class="trust__num trust__num--word num-mono">Budapeşte</span>',
 '<span class="trust__num trust__num--word num-mono">Budapest</span>'),
('<p class="trust__label">Merkez ofis Macaristan&rsquo;da. Öğrenci ülkeye yerleştikten sonra\n      da aynı ekiple çalışır.</p>',
 '<p class="trust__label">The head office is in Hungary. Students keep working with the same team\n      after they arrive.</p>'),
('<span class="trust__num num-mono">6 <em>ofis</em></span>', '<span class="trust__num num-mono">6 <em>offices</em></span>'),
('<p class="trust__label">Budapeşte, Ankara, İstanbul, İzmir, Bursa ve Pécs. Danışmanlık\n      iki ülkede birden yürütülür.</p>',
 '<p class="trust__label">Budapest, Ankara, Istanbul, Izmir, Bursa and Pécs. The consultancy runs\n      in two countries at once.</p>'),
('<span class="trust__num num-mono">19 <em>üniversite</em></span>',
 '<span class="trust__num num-mono">19 <em>universities</em></span>'),
('<p class="trust__label">Tıp, mühendislik, işletme ve pilotaj dahil 46 İngilizce program\n      için başvuru aracılığı.</p>',
 '<p class="trust__label">Applications handled for 46 English-taught programmes, including medicine,\n      engineering, business and pilot training.</p>'),
('1999&rsquo;dan bu yana binlerce öğrencinin lisans ve yüksek lisans başvurusunu yürüttük.\n'
 '      Program seçiminden vizeye, konaklamadan şehir oryantasyonuna kadar sürecin tamamı\n'
 '      tek ekip tarafından yönetilir.',
 'Since 1999 we have handled the bachelor’s and master’s applications of thousands of students.\n'
 '      From choosing a programme to the visa, and from accommodation to settling into the city, the\n'
 '      whole process is run by one team.'),
('<span class="trust__foot-note">Ücret, takvim ve kabul bilgileri danışmanlık ekibimiz\n      tarafından dönemsel olarak güncellenir.</span>',
 '<span class="trust__foot-note">Fees, dates and admission details are updated periodically by our\n      advisory team.</span>'),

# ---------------------------------------------------------------- finder
('<!-- ==================================================================\n     BÖLÜM 4 — PROGRAM BULUCU (3 adım)',
 '<!-- ==================================================================\n     SECTION 4 - PROGRAMME FINDER (3 steps)'),
('<p class="eyebrow" data-reveal="up-sm">Üç soruda başlayın</p>',
 '<p class="eyebrow" data-reveal="up-sm">Start with three questions</p>'),
('Size uygun program<br>üç adımda belirlensin', 'Find the right programme<br>in three steps'),
('Uzun filtre listeleriyle uğraşmayın. Seviyenizi, ilgi alanınızı ve şehir tercihinizi\n'
 '        seçin; sonuçları filtrelenmiş program listesinde açalım.',
 'No long filter lists. Choose your level, your field of interest and the city you have in mind, and\n'
 '        we will open the results as a filtered programme list.'),
('<h3 class="fstep__q">Hangi seviyede eğitim arıyorsunuz?</h3>', '<h3 class="fstep__q">What level are you looking for?</h3>'),
('<div class="fstep__opts" role="radiogroup" aria-label="Eğitim seviyesi">',
 '<div class="fstep__opts" role="radiogroup" aria-label="Study level">'),
('data-value="hazirlik" data-label="Hazırlık">Hazırlık<em>Dil / bölüm hazırlığı</em>',
 'data-value="hazirlik" data-label="Foundation">Foundation<em>Language or subject preparation</em>'),
('data-value="lisans" data-label="Lisans">Lisans<em>Bachelor</em>',
 'data-value="lisans" data-label="Bachelor’s">Bachelor’s<em>BA / BSc</em>'),
('data-value="yukseklisans" data-label="Yüksek Lisans">Yüksek Lisans<em>Master</em>',
 'data-value="yukseklisans" data-label="Master’s">Master’s<em>MA / MSc</em>'),
('data-value="butunlesik" data-label="Bütünleşik">Bütünleşik<em>Tıp, diş, eczacılık</em>',
 'data-value="butunlesik" data-label="Integrated">Integrated<em>Medicine, dentistry, pharmacy</em>'),
('<h3 class="fstep__q">İlgi alanınız hangisine yakın?</h3>', '<h3 class="fstep__q">Which field is closest to your interest?</h3>'),
('<div class="fstep__opts" role="radiogroup" aria-label="İlgi alanı">',
 '<div class="fstep__opts" role="radiogroup" aria-label="Field of interest">'),
('data-value="tip" data-label="Tıp, Diş, Eczacılık">Tıp, Diş, Eczacılık<em>Bütünleşik sağlık programları</em>',
 'data-value="tip" data-label="Medicine, Dentistry, Pharmacy">Medicine, Dentistry, Pharmacy<em>Integrated health programmes</em>'),
('data-value="muhendislik" data-label="Mühendislik">Mühendislik &amp; Mimarlık<em>Makine, elektrik, inşaat, mimarlık</em>',
 'data-value="muhendislik" data-label="Engineering">Engineering &amp; Architecture<em>Mechanical, electrical, civil, architecture</em>'),
('data-value="it" data-label="IT">IT &amp; Bilgisayar<em>Yazılım, bilgi teknolojileri</em>',
 'data-value="it" data-label="IT">IT &amp; Computing<em>Software, information technology</em>'),
('data-value="isletme" data-label="İşletme">İşletme &amp; Ekonomi<em>Yönetim, finans, uluslararası işletme</em>',
 'data-value="isletme" data-label="Business">Business &amp; Economics<em>Management, finance, international business</em>'),
('data-value="beseri-sosyal" data-label="Beşeri &amp; Sosyal">Beşeri &amp; Sosyal Bilimler<em>Psikoloji, sosyoloji</em>',
 'data-value="beseri-sosyal" data-label="Humanities &amp; Social">Humanities &amp; Social Sciences<em>Psychology, sociology</em>'),
('data-value="pilot" data-label="Pilotaj">Pilotaj<em>Profesyonel pilotluk</em>',
 'data-value="pilot" data-label="Pilot training">Pilot Training<em>Professional pilot licence</em>'),
('<h3 class="fstep__q">Nerede okumak istersiniz?</h3>', '<h3 class="fstep__q">Where would you like to study?</h3>'),
('<div class="fstep__opts" role="radiogroup" aria-label="Şehir tercihi">',
 '<div class="fstep__opts" role="radiogroup" aria-label="City preference">'),
('data-value="budapest" data-label="Budapeşte">Budapeşte<em>Başkent</em>',
 'data-value="budapest" data-label="Budapest">Budapest<em>The capital</em>'),
('data-value="debrecen" data-label="Debrecen">Debrecen<em>Doğu Macaristan</em>',
 'data-value="debrecen" data-label="Debrecen">Debrecen<em>Eastern Hungary</em>'),
('data-value="szeged" data-label="Szeged">Szeged<em>Güney</em>',
 'data-value="szeged" data-label="Szeged">Szeged<em>Southern Hungary</em>'),
('data-value="pecs" data-label="Pécs">Pécs<em>Güneybatı</em>',
 'data-value="pecs" data-label="Pécs">Pécs<em>South-west</em>'),
('data-value="farketmez" data-label="Fark etmez">Fark etmez<em>Tüm şehirleri göster</em>',
 'data-value="farketmez" data-label="No preference">No preference<em>Show every city</em>'),
('<span class="finder__summary-empty">İlk adımı seçerek başlayın.</span>',
 '<span class="finder__summary-empty">Start by choosing the first step.</span>'),
('<span data-t="Sıfırla">Sıfırla</span>', '<span data-t="Reset">Reset</span>'),
('<a class="btn btn--primary" href="programlar.html" data-finder-go data-magnetic aria-disabled="true">\n'
 '            <span class="btn__label"><span data-t="Bana Uygun Programları Göster">Bana Uygun Programları Göster</span></span>',
 '<a class="btn btn--primary" href="programs.html" data-finder-go data-magnetic aria-disabled="true">\n'
 '            <span class="btn__label"><span data-t="Show Programmes That Fit Me">Show Programmes That Fit Me</span></span>'),
('Ne seçeceğinizden emin değil misiniz? Bu tamamen normal —\n'
 '      <a class="link" href="#gorusme">danışmanımız sizinle birlikte belirlesin',
 'Not sure what to choose? That is completely normal —\n'
 '      <a class="link" href="#gorusme">let an adviser work it out with you'),

# ---------------------------------------------------------------- fields
('<!-- ==================================================================\n     BÖLÜM 5 — POPÜLER ALANLAR (yatay pin galerisi)',
 '<!-- ==================================================================\n     SECTION 5 - POPULAR FIELDS (pinned horizontal gallery)'),
('<p class="eyebrow">Popüler alanlar</p>', '<p class="eyebrow">Popular fields</p>'),
('Türk öğrencilerin en çok<br>araştırdığı bölümler', 'The subjects international<br>students ask about most'),
('data-cursor="İncele"', 'data-cursor="View"'),
('alt="Macaristan\'da tıp fakültesi laboratuvarında çalışan öğrenciler"',
 'alt="Students working in a medical school laboratory in Hungary"'),
('<h3 class="fcard__title">Tıp</h3>', '<h3 class="fcard__title">Medicine</h3>'),
('<p class="fcard__desc">İngilizce eğitim veren tıp fakülteleri, giriş sınavı ve mülakat süreçleriyle birlikte değerlendirilir.</p>',
 '<p class="fcard__desc">English-taught medical schools, assessed together with their entrance exam and interview process.</p>'),
('alt="Diş hekimliği eğitiminde klinik uygulama yapan öğrenciler"',
 'alt="Dentistry students during clinical practice"'),
('<h3 class="fcard__title">Diş Hekimliği</h3>', '<h3 class="fcard__title">Dentistry</h3>'),
('<p class="fcard__desc">Klinik uygulama ağırlıklı bütünleşik program. Kontenjanlar sınırlı olduğu için başvuru takvimi kritik.</p>',
 '<p class="fcard__desc">An integrated programme weighted towards clinical practice. Places are limited, so the application calendar is critical.</p>'),
('alt="Mühendislik laboratuvarında proje üzerinde çalışan üniversite öğrencileri"',
 'alt="University students working on a project in an engineering laboratory"'),
('<h3 class="fcard__title">Mühendislik</h3>', '<h3 class="fcard__title">Engineering</h3>'),
('<p class="fcard__desc">Bilgisayar, makine, elektrik ve inşaat mühendisliği başta olmak üzere geniş bir program yelpazesi.</p>',
 '<p class="fcard__desc">A broad catalogue led by computer, mechanical, electrical and civil engineering.</p>'),
('alt="İşletme ve ekonomi dersinde grup çalışması yapan öğrenciler"',
 'alt="Students working in a group during a business and economics class"'),
('<h3 class="fcard__title">İşletme &amp; Ekonomi</h3>', '<h3 class="fcard__title">Business &amp; Economics</h3>'),
('<p class="fcard__desc">Yönetim, finans, uluslararası ilişkiler ve turizm programları; çoğunda staj bileşeni bulunur.</p>',
 '<p class="fcard__desc">Management, finance, international relations and tourism programmes, most with a placement component.</p>'),
('alt="Psikoloji seminerinde tartışan üniversite öğrencileri"',
 'alt="University students in discussion during a psychology seminar"'),
('<h3 class="fcard__title">Psikoloji</h3>', '<h3 class="fcard__title">Psychology</h3>'),
('<p class="fcard__desc">Lisans ve yüksek lisans seçenekleri. Bazı programlar ek mülakat veya motivasyon mektubu ister.</p>',
 '<p class="fcard__desc">Bachelor’s and master’s options. Some programmes ask for an extra interview or a motivation letter.</p>'),
('alt="Pilotaj eğitiminde uçak kokpitinde eğitim alan öğrenci"',
 'alt="Student training in an aircraft cockpit during pilot training"'),
('<h3 class="fcard__title">Pilotaj</h3>', '<h3 class="fcard__title">Pilot Training</h3>'),
('<p class="fcard__desc">Teorik eğitim ve uçuş saatleri ayrı ayrı ücretlendirilir; sağlık raporu ve dil şartı önden planlanmalıdır.</p>',
 '<p class="fcard__desc">Ground school and flight hours are priced separately; the medical certificate and language requirement need planning up front.</p>'),
('<li><span>Süre</span><b>6 yıl</b></li>', '<li><span>Duration</span><b>6 years</b></li>'),
('<li><span>Süre</span><b>5 yıl</b></li>', '<li><span>Duration</span><b>5 years</b></li>'),
('<li><span>Süre</span><b>3,5–4 yıl</b></li>', '<li><span>Duration</span><b>3.5–4 years</b></li>'),
('<li><span>Süre</span><b>3–4 yıl</b></li>', '<li><span>Duration</span><b>3–4 years</b></li>'),
('<li><span>Süre</span><b>3 yıl</b></li>', '<li><span>Duration</span><b>3 years</b></li>'),
('<li><span>Süre</span><b>3,5 yıl</b></li>', '<li><span>Duration</span><b>3.5 years</b></li>'),
('<li><span>Dil</span><b>İngilizce</b></li>', '<li><span>Language</span><b>English</b></li>'),
('<li><span>Yıllık ücret</span><b>16.000 €</b></li>', '<li><span>Annual fee</span><b>€16,000</b></li>'),
('<li><span>Yıllık ücret</span><b>17.350 €<em>\'den</em></b></li>', '<li><span>Annual fee</span><b><em>from </em>€17,350</b></li>'),
('<li><span>Yıllık ücret</span><b>3.000–5.000 €</b></li>', '<li><span>Annual fee</span><b>€3,000–5,000</b></li>'),
('<li><span>Yıllık ücret</span><b>7.800 €<em>\'den</em></b></li>', '<li><span>Annual fee</span><b><em>from </em>€7,800</b></li>'),
('<li><span>Dönemlik ücret</span><b>7.500–13.500 $</b></li>', '<li><span>Fee per term</span><b>$7,500–13,500</b></li>'),
('Programları gör <svg', 'See programmes <svg'),
('<h3 class="fcard__title">Aradığınız<br>alan burada<br>yok mu?</h3>',
 '<h3 class="fcard__title">Not seeing<br>the field you<br>are after?</h3>'),
('<p class="fcard__desc">Macaristan\'da veterinerlik, eczacılık, mimarlık, hukuk ve müzik alanlarında da programlar bulunuyor.</p>',
 '<p class="fcard__desc">Hungary also offers programmes in veterinary medicine, pharmacy, architecture, law and music.</p>'),
('<a class="btn btn--primary" href="programlar.html" data-magnetic><span class="btn__label"><span data-t="Tüm Programlar">Tüm Programlar</span></span></a>',
 '<a class="btn btn--primary" href="programs.html" data-magnetic><span class="btn__label"><span data-t="All Programmes">All Programmes</span></span></a>'),
('Ücretler yıllık öğrenim ücretidir (pilotajda dönemliktir) ve üniversiteye göre değişir;\n'
 '        üniversiteler tarafından değiştirilebilir.',
 'Fees shown are annual tuition (per term for pilot training) and vary by university; universities\n'
 '        may change them.'),
('<span class="chip chip--updated num-mono">Son güncelleme: Ağustos 2026</span>',
 '<span class="chip chip--updated num-mono">Last updated: August 2026</span>'),
]

miss = []
for a, b in R:
    if a not in s:
        miss.append(a[:90])
    s = s.replace(a, b)

io.open(os.path.join(SITE, 'index.html'), 'w', encoding='utf-8').write(s)
print('index.html (bolum 1-5) yazildi:', len(s))
if miss:
    print('ESLESMEYEN:', len(miss))
    for m in miss:
        print('  !', m)
else:
    print('bu partide tum kaliplar eslesti')
