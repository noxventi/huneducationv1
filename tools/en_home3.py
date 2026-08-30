# -*- coding: utf-8 -*-
"""index.html ucuncu parti: SSS, final CTA ve footer."""
import io, os, re, sys

SITE = sys.argv[1]
P = os.path.join(SITE, 'index.html')
s = io.open(P, encoding='utf-8').read()

R = [
# ---------------------------------------------------------------- FAQ
('<!-- ==================================================================\n     BÖLÜM 12 — SSS',
 '<!-- ==================================================================\n     SECTION 12 - FAQ'),
('<p class="eyebrow" data-reveal="up-sm">Sık sorulanlar</p>', '<p class="eyebrow" data-reveal="up-sm">Frequently asked</p>'),
('En çok merak edilen<br>altı soru', 'The six questions<br>we hear most'),
('Yanıtlar koşulludur ve mevzuat değiştikçe güncellenir. Kesin bilgi için her zaman\n'
 '        ilgili üniversitenin ve resmî kurumların güncel sayfalarını esas alın.',
 'The answers are conditional and are updated as the rules change. For anything definitive, always\n'
 '        rely on the current pages of the university and the official authorities.'),
('<span data-t="Sorunuz burada yoksa sorun">Sorunuz burada yoksa sorun</span>',
 '<span data-t="Ask us anything not covered here">Ask us anything not covered here</span>'),
('<span class="acc__num">01</span> YKS\'ye girmem gerekiyor mu?',
 '<span class="acc__num">01</span> Do I need a national entrance exam?'),
('<p>Macaristan\'daki üniversiteler kendi başvuru ve kabul süreçlerini uygular; YKS puanı genellikle\n'
 '          bir kabul şartı değildir. Ancak bu "sınavsız kabul" anlamına gelmez — birçok programın kendi\n'
 '          giriş sınavı vardır:</p>',
 '<p>Hungarian universities run their own application and admission process, and a national entrance\n'
 '          exam score is generally not an admission requirement. But that does not mean “admission without\n'
 '          an exam” — many programmes set an entrance exam of their own:</p>'),
('<p><b>Sağlık alanları</b> için kimya ve biyoloji sınavı (sözlü veya yazılı),\n'
 '          <b>mühendislik</b> için online fizik ve matematik sınavı, <b>mimarlık</b> için fizik, matematik ve\n'
 '          portfolyo, <b>film ve tasarım</b> programları için portfolyo istenir.</p>',
 '<p><b>Health programmes</b> set a chemistry and biology exam (oral or written), <b>engineering</b> an\n'
 '          online physics and mathematics exam, <b>architecture</b> physics, mathematics and a portfolio, and\n'
 '          <b>film and design</b> programmes a portfolio.</p>'),
('<p>Gerekli belgeler: başvuru formu, pasaport fotokopisi, İngilizce ya da onaylı çeviri transkript,\n'
 '          apostilli diploma, son 6 aylık banka hesap dökümü ve İngilizce özgeçmiş (tercihen Europass).</p>',
 '<p>Documents required: the application form, a passport copy, a transcript in English or certified\n'
 '          translation, an apostilled diploma, a six-month bank statement and an English CV (Europass preferred).</p>'),
('<p>Türkiye\'de mezuniyet sonrası denklik değerlendirmesi için YÖK\'ün güncel kurallarını ayrıca\n'
 '          incelemeniz gerekir.</p>',
 '<p>For recognition of your degree after graduation you also need to check the current rules of the\n'
 '          competent authority in your own country.</p>'),
('<span class="acc__num">02</span> İngilizce dil belgesi şart mı?',
 '<span class="acc__num">02</span> Do I need an English language certificate?'),
('<p><b>Lisansta</b> en az <b>B2</b> seviyesi beklenir. Bazı okullar IELTS <b>5, 6 veya 6.5</b> puan\n'
 '          belgesi ister. <b>Yüksek lisansta</b> genellikle <b>IELTS 6.5</b> veya eşdeğer bir belge gerekir.</p>',
 '<p><b>Bachelor’s</b> programmes expect at least <b>B2</b>. Some universities ask for an IELTS score of\n'
 '          <b>5, 6 or 6.5</b>. <b>Master’s</b> programmes usually require <b>IELTS 6.5</b> or an equivalent.</p>'),
('<p>B2 seviyesinde değilseniz üniversitelerin bünyesindeki <b>İngilizce Dil Hazırlık</b>\n'
 '          programlarına başvurabilirsiniz; ücreti dönemlik 2.500 €\'dan başlar. Kabul edilen belge türü ve\n'
 '          minimum puan üniversiteye ve programa göre değişir.</p>',
 '<p>If you are not at B2 you can apply to the universities’ own <b>English Language Foundation</b>\n'
 '          programmes, which start from €2,500 per term. The accepted certificate and the minimum score vary\n'
 '          by university and by programme.</p>'),
('<span class="acc__num">03</span> Başvurular ne zaman açılıyor?',
 '<span class="acc__num">03</span> When do applications open?'),
('<p>Macaristan\'da iki başlangıç dönemi vardır:</p>', '<p>Hungary has two intakes a year:</p>'),
('<p><b>Eylül (güz) dönemi</b> — üniversitelerin çoğu Eylül\'de başladığı için başvuruların\n'
 '          <b>Nisan, Mayıs veya Haziran</b> ayına kadar yapılması istenir.<br>\n'
 '          <b>Şubat (bahar) dönemi</b> — <b>Ekim sonuna, en geç Kasım</b> ayına kadar başvurmanız gerekir.</p>',
 '<p><b>September (autumn) intake</b> — most universities start in September, so applications are\n'
 '          expected by <b>April, May or June</b>.<br>\n'
 '          <b>February (spring) intake</b> — you need to apply by <b>the end of October, and November at the latest</b>.</p>'),
('<p>Kesin tarihler her üniversitenin kendi akademik takvimine bağlıdır ve kontenjan dolduğunda\n'
 '          dönem erken kapanabilir.</p>',
 '<p>Exact dates depend on each university’s own academic calendar, and an intake can close early once\n'
 '          places run out.</p>'),
('<span class="acc__num">04</span> Toplam maliyet ne kadar tutar?',
 '<span class="acc__num">04</span> What does it cost in total?'),
('<p>Eğitim ve yaşam giderleri birlikte <b>yıllık 8.500 – 14.000 €</b> aralığındadır.\n'
 '          Öğrenim ücreti lisansta 3.000–5.000 €, yüksek lisansta 4.000–6.000 €, tıp ve diş hekimliğinde\n'
 '          16.000–17.350 €\'dur. Yaşam giderleri tek başına yılda 4.000–8.000 € tutar.</p>',
 '<p>Tuition and living costs together run <b>€8,500 – €14,000 a year</b>. Tuition is €3,000–5,000 for a\n'
 '          bachelor’s, €4,000–6,000 for a master’s and €16,000–17,350 for medicine and dentistry. Living costs\n'
 '          alone come to €4,000–8,000 a year.</p>'),
('<p>Konaklama en oynak kalemdir: üniversite yurtları ayda 60–400 €, kiralık oda ≈350 €,\n'
 '          stüdyo daire ≈550 €\'dur. Buna aylık ≈300 € yaşam gideri, 120 € ulaşım, yıllık 300 € sağlık\n'
 '          sigortası ile tek seferlik 140 € başvuru ve 95–145 € vize ücreti eklenir.</p>',
 '<p>Accommodation is the most volatile item: university dormitories cost €60–400 a month, a rented room\n'
 '          around €350 and a studio flat around €550. On top of that come roughly €300 a month in living costs,\n'
 '          €120 for transport, €300 a year for health insurance, plus a one-off €140 application fee and a\n'
 '          €95–145 visa fee.</p>'),
('<p>Rakamlar üniversiteye, şehre ve yaşam tercihinize göre değişir; üniversiteler tarafından\n'
 '          güncellenebilir. Yukarıdaki maliyet bölümünden kendi kalem listenizi çıkarabilirsiniz.</p>',
 '<p>The figures change with the university, the city and how you live, and universities can update them.\n'
 '          You can build your own breakdown in the cost section above.</p>'),
('<span class="acc__num">05</span> Vize sürecinde destek veriyor musunuz?',
 '<span class="acc__num">05</span> Do you support the visa process?'),
('<p>Evet. Kabul mektubunuz çıktıktan sonra en yakın Macaristan Konsolosluğu için gereken belge\n'
 '          listesini hazırlar, randevu ve dosya düzenini birlikte kontrol ederiz. Başvuru için son 6 aylık\n'
 '          banka hesap dökümü de istenir.</p>',
 '<p>Yes. Once your acceptance letter comes through, we prepare the document list for your nearest\n'
 '          Hungarian consulate and check the appointment and the file with you. A six-month bank statement is\n'
 '          also required for the application.</p>'),
('<p>Vize kararı tamamen ilgili resmî makama aittir; hiçbir danışmanlık şirketi vize garantisi\n'
 '          veremez. Vize alınamaması durumunda ödenen <b>öğrenim ücreti 30 iş günü içinde iade edilir</b>;\n'
 '          başvuru ve sınav ücretleri iade edilmez.</p>',
 '<p>The visa decision rests entirely with the official authority; no consultancy can guarantee a visa.\n'
 '          If the visa is refused, <b>tuition already paid is refunded within 30 working days</b>; application\n'
 '          and entrance exam fees are not refunded.</p>'),
('<span class="acc__num">06</span> Diplomam Türkiye\'de tanınır mı?',
 '<span class="acc__num">06</span> Will my degree be recognised at home?'),
('<p>Yurt dışında alınan diplomaların Türkiye\'de kullanılabilmesi için YÖK\'ün denklik değerlendirmesi\n'
 '          gerekir. Denklik; üniversitenin tanınırlığı, programın içeriği, eğitim süresi ve mezuniyet\n'
 '          koşullarına göre değerlendirilir ve bazı alanlarda ek sınav (ör. seviye tespit sınavı) istenebilir.</p>',
 '<p>Using a degree earned abroad in your own country normally requires a recognition assessment by the\n'
 '          competent national authority. Recognition is judged on the university’s standing, the content of the\n'
 '          programme, the length of study and the graduation conditions, and some fields require an additional\n'
 '          exam (for example a placement test).</p>'),
('<p>Kurallar değişebildiği için başvuru öncesinde YÖK\'ün güncel denklik mevzuatını doğrudan\n'
 '          incelemenizi öneririz. Otomatik veya garantili denklik iddiasında bulunmuyoruz.</p>',
 '<p>Because the rules change, review your national authority’s current recognition regulations before you\n'
 '          apply. We make no claim of automatic or guaranteed recognition.</p>'),

# ---------------------------------------------------------------- final CTA
('<!-- ==================================================================\n     BÖLÜM 13 — FİNAL CTA',
 '<!-- ==================================================================\n     SECTION 13 - FINAL CTA'),
('<p class="eyebrow" data-reveal="up-sm">Son adım</p>', '<p class="eyebrow" data-reveal="up-sm">Last step</p>'),
('<h2 class="display h-xl split-mask" id="final-h" data-split>Hangi programın size uygun olduğundan emin değil misiniz?</h2>',
 '<h2 class="display h-xl split-mask" id="final-h" data-split>Not sure which programme is right for you?</h2>'),
('Akademik geçmişinizi ve hedeflerinizi birlikte değerlendirelim. Ön görüşme ücretsizdir\n'
 '        ve sizi hiçbir şeye bağlamaz.',
 'Let us go through your academic record and your goals together. The consultation is free and\n'
 '        commits you to nothing.'),
('<p class="final__form-title">Ücretsiz ön görüşme talebi</p>',
 '<p class="final__form-title">Request a free consultation</p>'),
('<span class="field__label">Ad soyad <span class="field__req" aria-hidden="true">*</span></span>',
 '<span class="field__label">Full name <span class="field__req" aria-hidden="true">*</span></span>'),
('<span class="field__label">Telefon <span class="field__req" aria-hidden="true">*</span></span>',
 '<span class="field__label">Phone <span class="field__req" aria-hidden="true">*</span></span>'),
('placeholder="+90 5XX XXX XX XX"', 'placeholder="+44 7700 900000"'),
('<span class="field__label">E-posta <span class="field__req" aria-hidden="true">*</span></span>',
 '<span class="field__label">Email <span class="field__req" aria-hidden="true">*</span></span>'),
('<span class="field__label">İlgilendiğiniz seviye</span>', '<span class="field__label">Level you are interested in</span>'),
('<option value="">Seçiniz</option>\n'
 '            <option>Hazırlık</option><option>Lisans</option><option>Yüksek lisans</option><option>Tıp / diş / eczacılık</option><option>Henüz emin değilim</option>',
 '<option value="">Please choose</option>\n'
 '            <option>Foundation</option><option>Bachelor&rsquo;s</option><option>Master&rsquo;s</option><option>Medicine / dentistry / pharmacy</option><option>Not sure yet</option>'),
('<span>Kişisel verilerimin, ön görüşme talebimi değerlendirmek amacıyla işlenmesini kabul ediyorum.\n'
 '          <a href="kvkk-aydinlatma.html" target="_blank" rel="noopener">KVKK Aydınlatma Metni</a></span>',
 '<span>I consent to my personal data being processed in order to assess my consultation request.\n'
 '          <a href="privacy-notice.html" target="_blank" rel="noopener">Privacy Notice</a></span>'),
('<span data-t="Ücretsiz Ön Görüşme Al">Ücretsiz Ön Görüşme Al</span>',
 '<span data-t="Book a Free Consultation">Book a Free Consultation</span>'),
('Yazmayı tercih ederseniz:\n        <a class="link" href="https://wa.me/" data-wa>WhatsApp\'tan sorun</a>',
 'Prefer to write?\n        <a class="link" href="https://wa.me/" data-wa>Ask us on WhatsApp</a>'),
('<!-- Gizli attribution alanları — PRD §13 -->', '<!-- Hidden attribution fields - PRD 13 -->'),
('<h3>Talebiniz alındı</h3>', '<h3>We have your request</h3>'),
('<p>Danışmanımız çalışma saatleri içinde size dönecek. Dilerseniz görüşmeyi hemen WhatsApp\'tan sürdürebilirsiniz.</p>',
 '<p>An adviser will come back to you during working hours. If you prefer, you can carry on the conversation on WhatsApp right away.</p>'),
('<span data-t="WhatsApp\'tan devam et">WhatsApp\'tan devam et</span>',
 '<span data-t="Continue on WhatsApp">Continue on WhatsApp</span>'),

# ---------------------------------------------------------------- footer
('<h2 id="ftr-h" class="sr-only">Site alt bilgisi</h2>', '<h2 id="ftr-h" class="sr-only">Site footer</h2>'),
('<p>1999\'dan beri Macaristan odaklı akademik danışmanlık. Program seçiminden başvuruya,\n'
 '        vizeden konaklama ve şehir oryantasyonuna kadar uçtan uca destek.</p>',
 '<p>Hungary-focused academic consultancy since 1999. End-to-end support from choosing a programme to\n'
 '        applying, and from the student visa to accommodation and settling into your city.</p>'),
('<nav class="ftr__col" aria-label="Hızlı bağlantılar">\n        <h3>Hızlı bağlantılar</h3>\n'
 '        <a href="macaristanda-egitim.html">Macaristan\'da Eğitim</a><a href="universiteler.html">Üniversiteler</a>\n'
 '        <a href="programlar.html">Programlar</a><a href="hakkimizda.html">Hizmetlerimiz</a>\n'
 '        <a href="#hikayeler">Öğrenci Hikâyeleri</a><a href="#rehber">Rehber</a>\n      </nav>',
 '<nav class="ftr__col" aria-label="Quick links">\n        <h3>Quick links</h3>\n'
 '        <a href="study-in-hungary.html">Study in Hungary</a><a href="universities.html">Universities</a>\n'
 '        <a href="programs.html">Programmes</a><a href="about.html">What We Do</a>\n'
 '        <a href="#hikayeler">Student Stories</a><a href="#rehber">Guides</a>\n      </nav>'),
('<nav class="ftr__col" aria-label="Popüler programlar">\n        <h3>Popüler programlar</h3>\n'
 '        <a href="programlar.html?alan=tip">Tıp</a><a href="programlar.html?alan=tip">Diş Hekimliği</a>\n'
 '        <a href="programlar.html?alan=muhendislik">Mühendislik</a><a href="programlar.html?alan=isletme">İşletme</a>\n'
 '        <a href="programlar.html?alan=beseri-sosyal">Psikoloji</a><a href="programlar.html?alan=pilot">Pilotaj</a>\n      </nav>',
 '<nav class="ftr__col" aria-label="Popular programmes">\n        <h3>Popular programmes</h3>\n'
 '        <a href="programs.html?alan=tip">Medicine</a><a href="programs.html?alan=tip">Dentistry</a>\n'
 '        <a href="programs.html?alan=muhendislik">Engineering</a><a href="programs.html?alan=isletme">Business</a>\n'
 '        <a href="programs.html?alan=beseri-sosyal">Psychology</a><a href="programs.html?alan=pilot">Pilot Training</a>\n      </nav>'),
('<h3>İletişim</h3>', '<h3>Contact</h3>'),
('<p class="ftr__office"><b>Budapeşte merkez</b><span>1204 Budapest, Bethlen utca 17, Macaristan</span></p>',
 '<p class="ftr__office"><b>Budapest head office</b><span>1204 Budapest, Bethlen utca 17, Hungary</span></p>'),
('<p class="ftr__office"><b>Türkiye</b><span>Ankara · İstanbul (Kadıköy) · İzmir · Bursa</span></p>',
 '<p class="ftr__office"><b>Türkiye</b><span>Ankara · Istanbul (Kadıköy) · Izmir · Bursa</span></p>'),
('<span class="num-mono">E-POSTA</span>', '<span class="num-mono">EMAIL</span>'),
('<span class="num-mono">WA</span> WhatsApp\'tan yazın', '<span class="num-mono">WA</span> Message us on WhatsApp'),
('<p class="ftr__hours num-mono">Pazartesi – Cuma · 09:00 – 18:00</p>',
 '<p class="ftr__hours num-mono">Monday – Friday · 09:00 – 18:00 CET</p>'),
('Sitede yer alan öğrenim ücretleri, başvuru tarihleri ve kabul koşulları üniversiteler tarafından\n'
 '        değiştirilebilir. Vize ve denklik kararları ilgili resmî kurumlara aittir. Nihai bilgi için\n'
 '        üniversitenin resmî sayfasını ve güncel mevzuatı esas alınız.',
 'Tuition fees, application dates and admission requirements shown on this site may be changed by the\n'
 '        universities. Visa and recognition decisions rest with the relevant official authorities. Always\n'
 '        treat the university’s own page and current legislation as definitive.'),
('<nav class="ftr__links" aria-label="Yasal">\n'
 '        <a href="kvkk-aydinlatma.html">KVKK Aydınlatma Metni</a><a href="acik-riza.html">Açık Rıza Metni</a>\n'
 '        <a href="gizlilik-cerez.html">Gizlilik ve Çerez Politikası</a><a href="kullanim-kosullari.html">Kullanım Koşulları</a>\n'
 '      </nav>',
 '<nav class="ftr__links" aria-label="Legal">\n'
 '        <a href="privacy-notice.html">Privacy Notice</a><a href="consent.html">Consent Statement</a>\n'
 '        <a href="cookie-policy.html">Cookie Policy</a><a href="terms-of-use.html">Terms of Use</a>\n'
 '      </nav>'),
('· Tüm hakları saklıdır.', '· All rights reserved.'),
('<span data-t="Ön Görüşme Al">Ön Görüşme Al</span>', '<span data-t="Book a Consultation">Book a Consultation</span>'),
]

miss = []
for a, b in R:
    if a not in s:
        miss.append(a[:90])
    s = s.replace(a, b)

io.open(P, 'w', encoding='utf-8').write(s)
print('index.html (bolum 12-13 + footer) yazildi:', len(s))
if miss:
    print('ESLESMEYEN:', len(miss))
    for m in miss:
        print('  !', m)
else:
    print('bu partide tum kaliplar eslesti')

# ---- kalinti taramasi: gorunur metinde Turkce karakter kaldi mi?
body = re.sub(r'<script.*?</script>', '', s, flags=re.S)
body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
txt = re.sub(r'<[^>]+>', ' ', body)
hits = sorted(set(re.findall(r'\w*[çğıöşüÇĞİÖŞÜ]\w*', txt)))
print('gorunur metinde TR karakterli kelimeler:', hits)
