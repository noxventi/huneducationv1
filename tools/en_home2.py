# -*- coding: utf-8 -*-
"""index.html ikinci parti: surec, manifesto, harita, hikayeler, maliyet,
rehber, SSS, final CTA ve footer. en_home.py'den SONRA calistirilir."""
import io, os, re, sys

SITE = sys.argv[1]
P = os.path.join(SITE, 'index.html')
s = io.open(P, encoding='utf-8').read()

R = [
# ---------------------------------------------------------------- process
('<!-- ==================================================================\n     BÖLÜM 6 — SÜREÇ (pinned, 6 adım)',
 '<!-- ==================================================================\n     SECTION 6 - PROCESS (pinned, 6 steps)'),
('alt="Ücretsiz ön görüşmede danışmanla konuşan öğrenci ve ailesi"',
 'alt="A student and their family talking to an adviser during a free consultation"'),
('alt="Üniversite ve program araştırması yapan öğrenci"', 'alt="Student researching universities and programmes"'),
('alt="Üniversite başvurusu için hazırlanan diploma, transkript ve pasaport"',
 'alt="Diploma, transcript and passport prepared for a university application"'),
('alt="Macaristan\'da bir üniversite kampüsünün avlusunda yürüyen öğrenciler"',
 'alt="Students walking through the courtyard of a university campus in Hungary"'),
('alt="Budapeşte\'de aydınlık bir öğrenci konaklaması"', 'alt="A bright student flat in Budapest"'),
('alt="Havalimanında karşılanan uluslararası öğrenci"', 'alt="International student being met at the airport"'),
('<p class="eyebrow">Hun Education ile süreç</p>', '<p class="eyebrow">The process with Hun Education</p>'),
('İlk görüşmeden<br>Budapeşte\'deki<br>ilk haftanıza', 'From the first call<br>to your first week<br>in Budapest'),
('Altı adımın tamamında aynı ekiple çalışırsınız. Her adımda sizden ne beklendiği ve\n'
 '          bizim ne yaptığımız önceden yazılı olarak bellidir.',
 'You work with the same team through all six steps. What is expected of you and what we do at each\n'
 '          step is set out in writing in advance.'),
('<b class="num-mono is-on" data-pend="tr">TÜRKİYE</b>', '<b class="num-mono is-on" data-pend="tr">HOME COUNTRY</b>'),
('<b class="num-mono" data-pend="hu">MACARİSTAN</b>', '<b class="num-mono" data-pend="hu">HUNGARY</b>'),
('<span class="pjourney__now" data-ptitle>Ücretsiz ön görüşme ve hedef analizi</span>',
 '<span class="pjourney__now" data-ptitle>Free consultation and goal analysis</span>'),
('<a class="btn btn--ghost" href="iletisim.html" data-magnetic><span class="btn__label"><span data-t="Süreci Birlikte Planlayalım">Süreci Birlikte Planlayalım</span></span></a>',
 '<a class="btn btn--ghost" href="contact.html" data-magnetic><span class="btn__label"><span data-t="Let Us Plan It Together">Let Us Plan It Together</span></span></a>'),
('<p class="pstep__phase num-mono">TÜRKİYE → MACARİSTAN</p>', '<p class="pstep__phase num-mono">HOME COUNTRY → HUNGARY</p>'),
('<p class="pstep__phase num-mono">TÜRKİYE</p>', '<p class="pstep__phase num-mono">HOME COUNTRY</p>'),
('<p class="pstep__phase num-mono">MACARİSTAN</p>', '<p class="pstep__phase num-mono">HUNGARY</p>'),
('<h3>Ücretsiz ön görüşme ve hedef analizi</h3>', '<h3>Free consultation and goal analysis</h3>'),
('<p class="pstep__desc">Akademik geçmişinizi, dil seviyenizi, bütçenizi ve mezuniyet sonrası hedefinizi konuşuruz. Görüşme sonunda hangi seviyede, hangi alanlarda gerçekçi seçenekleriniz olduğunu söyleriz.</p>',
 '<p class="pstep__desc">We talk through your academic record, your English level, your budget and what you want after graduation. By the end of the call we tell you which levels and which fields are realistic options for you.</p>'),
('<h3>Üniversite ve program eşleştirme</h3>', '<h3>Matching universities and programmes</h3>'),
('<p class="pstep__desc">Profilinize uyan programları kabul şartı, ücret, şehir ve başvuru takvimiyle birlikte karşılaştırmalı bir liste hâlinde sunarız. Hangi programın neden elendiğini de açıklarız.</p>',
 '<p class="pstep__desc">We put the programmes that match your profile side by side with their admission conditions, fees, city and application deadlines. We also explain why any programme was ruled out.</p>'),
('<h3>Evrakların hazırlanması</h3>', '<h3>Preparing the documents</h3>'),
('<p class="pstep__desc">Apostilli diploma, İngilizce transkript, pasaport, İngilizce özgeçmiş ve son 6 aylık banka hesap dökümünü kontrol listesiyle tamamlarız. En sık kaybedilen zaman apostil aşamasında geçer.</p>',
 '<p class="pstep__desc">We work through a checklist: apostilled diploma, English transcript, passport, English CV and a six-month bank statement. The apostille stage is where most time is lost.</p>'),
('<h3>Başvuru, giriş sınavı ve kabul</h3>', '<h3>Application, entrance exam and offer</h3>'),
('<p class="pstep__desc">Başvuruyu üniversitenin kendi sistemi üzerinden yaparız. Sağlıkta kimya–biyoloji, mühendislikte fizik–matematik sınavı varsa hazırlığınızı planlarız. Olumlu sonuçta önce <b>Ön Kabul</b>, ödeme sonrası <b>Nihai Kabul Mektubu</b> düzenlenir.</p>',
 '<p class="pstep__desc">We submit through the university’s own system. Where there is a chemistry–biology exam for health programmes or a physics–mathematics exam for engineering, we plan your preparation. On a positive result you receive a <b>conditional offer</b> first and the <b>final Acceptance Letter</b> after payment.</p>'),
('<h3>Vize, konaklama ve seyahat</h3>', '<h3>Visa, accommodation and travel</h3>'),
('<p class="pstep__desc">Nihai Kabul Mektubuyla en yakın Macaristan Konsolosluğuna başvurulur. Yurt ya da kiralık daire seçeneklerini kabulünüze göre araştırırız. Vize kararı konsolosluğa aittir; vize alınamazsa öğrenim ücreti <b>30 iş günü içinde iade edilir</b>.</p>',
 '<p class="pstep__desc">You apply at your nearest Hungarian consulate with the final Acceptance Letter. We research dormitory and rental options around your offer. The visa decision rests with the consulate; if the visa is refused, tuition is <b>refunded within 30 working days</b>.</p>'),
('<h3>Karşılama ve oryantasyon</h3>', '<h3>Arrival and orientation</h3>'),
('<p class="pstep__desc">Havalimanı karşılama, ikamet kaydı, banka hesabı, ulaşım kartı ve üniversite kaydı için Budapeşte ekibimiz yanınızda olur. Eğitiminiz boyunca da aynı danışmana ulaşırsınız.</p>',
 '<p class="pstep__desc">Our Budapest team is with you for the airport pick-up, residence registration, bank account, transport card and university enrolment. You keep the same adviser throughout your studies.</p>'),
('<div><dt>Bu adımda siz</dt><dd>Transkriptinizi ve dil seviyenizi hazır bulundurun</dd></div>',
 '<div><dt>Your part</dt><dd>Have your transcript and English level ready</dd></div>'),
('<div><dt>Bu adımda biz</dt><dd>Gerçekçi seçenek listesi ve takvim çıkarırız</dd></div>',
 '<div><dt>Our part</dt><dd>We produce a realistic shortlist and a timeline</dd></div>'),
('<div><dt>Bu adımda siz</dt><dd>Şehir ve bütçe tercihinizi netleştirin</dd></div>',
 '<div><dt>Your part</dt><dd>Settle on your city and budget</dd></div>'),
('<div><dt>Bu adımda biz</dt><dd>Karşılaştırma tablosu ve kabul şartı analizi</dd></div>',
 '<div><dt>Our part</dt><dd>A comparison table and an admission-conditions analysis</dd></div>'),
('<div><dt>Bu adımda siz</dt><dd>Apostil ve yeminli çeviri randevularını alın</dd></div>',
 '<div><dt>Your part</dt><dd>Book the apostille and sworn translation appointments</dd></div>'),
('<div><dt>Bu adımda biz</dt><dd>Kontrol listesi ve dosya denetimi yaparız</dd></div>',
 '<div><dt>Our part</dt><dd>We run the checklist and audit the file</dd></div>'),
('<div><dt>Bu adımda siz</dt><dd>Giriş sınavına veya mülakata hazırlanın</dd></div>',
 '<div><dt>Your part</dt><dd>Prepare for the entrance exam or interview</dd></div>'),
('<div><dt>Bu adımda biz</dt><dd>Başvuru, sınav takibi ve kabul yazışması</dd></div>',
 '<div><dt>Our part</dt><dd>The application, exam follow-up and offer correspondence</dd></div>'),
('<div><dt>Bu adımda siz</dt><dd>Konsolosluk randevusuna katılın</dd></div>',
 '<div><dt>Your part</dt><dd>Attend the consulate appointment</dd></div>'),
('<div><dt>Bu adımda biz</dt><dd>Belge dosyası ve konaklama araştırması</dd></div>',
 '<div><dt>Our part</dt><dd>The document file and the accommodation search</dd></div>'),
('<div><dt>Bu adımda siz</dt><dd>Uçuş bilgilerinizi bizimle paylaşın</dd></div>',
 '<div><dt>Your part</dt><dd>Share your flight details with us</dd></div>'),
('<div><dt>Bu adımda biz</dt><dd>Karşılama, ikamet ve kayıt desteği</dd></div>',
 '<div><dt>Our part</dt><dd>Pick-up, residence and enrolment support</dd></div>'),
('<ul class="pstep__tags"><li>30–45 dk</li><li>Online veya ofis</li><li>Ücretsiz</li></ul>',
 '<ul class="pstep__tags"><li>30–45 min</li><li>Online or in office</li><li>Free</li></ul>'),
('<ul class="pstep__tags"><li>Karşılaştırma listesi</li><li>Kabul şartı analizi</li></ul>',
 '<ul class="pstep__tags"><li>Comparison shortlist</li><li>Admission analysis</li></ul>'),
('<ul class="pstep__tags"><li>Kontrol listesi</li><li>Apostil yönlendirmesi</li></ul>',
 '<ul class="pstep__tags"><li>Document checklist</li><li>Apostille guidance</li></ul>'),
('<ul class="pstep__tags"><li>Güz için Nisan–Haziran</li><li>Sınav hazırlığı</li></ul>',
 '<ul class="pstep__tags"><li>April–June for autumn</li><li>Exam preparation</li></ul>'),
('<ul class="pstep__tags"><li>D tipi öğrenci vizesi</li><li>Yurt / kiralık daire</li></ul>',
 '<ul class="pstep__tags"><li>Type D student visa</li><li>Dormitory or rental</li></ul>'),
('<ul class="pstep__tags"><li>Havalimanı karşılama</li><li>İkamet &amp; kayıt</li></ul>',
 '<ul class="pstep__tags"><li>Airport pick-up</li><li>Residence &amp; enrolment</li></ul>'),
('Adımların kapsamı seçilen hizmet paketine göre değişebilir. Kabul kararı üniversiteye,\n'
 '      vize kararı ilgili konsolosluğa, denklik kararı YÖK\'e aittir; Hun Education bu sonuçlar\n'
 '      için garanti vermez.',
 'The scope of each step can vary with the service package you choose. The admission decision rests\n'
 '      with the university, the visa decision with the relevant consulate and the recognition decision\n'
 '      with your national authority; Hun Education does not guarantee those outcomes.'),

# ---------------------------------------------------------------- manifesto
('<!-- ==================================================================\n     BÖLÜM 7 — NEDEN HUN EDUCATION (scroll ile aydınlanan metin)',
 '<!-- ==================================================================\n     SECTION 7 - WHY HUN EDUCATION (text lit by scroll)'),
('<p class="eyebrow" data-reveal="up-sm">Neden Hun Education?</p>', '<p class="eyebrow" data-reveal="up-sm">Why Hun Education?</p>'),
('<h2 class="sr-only" id="manifesto-h">Neden Hun Education?</h2>', '<h2 class="sr-only" id="manifesto-h">Why Hun Education?</h2>'),
('Macaristan&rsquo;da eğitim yolculuğunuzu genel bilgilerle değil, 1999&rsquo;dan beri bu ülkede\n'
 '      edindiğimiz deneyimle planlıyoruz. Hangi üniversitenin size uygun olduğunu, başvuruda sizi\n'
 '      nelerin beklediğini ve öğrenci yaşamına nasıl hazırlanmanız gerektiğini biliyor; sürecin\n'
 '      her aşamasında yanınızda oluyoruz.',
 'We plan your studies in Hungary from experience built in this one country since 1999, not from\n'
 '      general information. We know which university suits you, what awaits you in the application and\n'
 '      how to prepare for student life here — and we stay beside you at every stage of the process.'),
('<h3>Tek ülke, tam odak</h3>', '<h3>One country, full focus</h3>'),
('<p>Danışmanlarımız yalnızca Macaristan sistemini takip eder. Başvuru takvimi ya da kabul şartı değiştiğinde bunu haberden değil, üniversiteden öğreniriz.</p>',
 '<p>Our advisers follow one system only. When an application deadline or an admission condition changes, we hear it from the university, not from the news.</p>'),
('<h3>Türkiye\'den Macaristan\'a kesintisiz</h3>', '<h3>Unbroken from home to Hungary</h3>'),
('<p>Uçağa binince destek bitmiyor. İkamet kaydı, kayıt haftası ve ilk dönem sorunları için Budapeşte\'deki ekibe ulaşırsınız.</p>',
 '<p>Support does not end when you board the plane. For residence registration, enrolment week and first-term problems you reach the team in Budapest.</p>'),
('<h3>Danışmana doğrudan erişim</h3>', '<h3>Direct access to your adviser</h3>'),
('<p>Her aday bir danışmana atanır. Süreç boyunca aynı kişiyle konuşursunuz; her seferinde baştan anlatmak zorunda kalmazsınız.</p>',
 '<p>Every applicant is assigned an adviser. You speak to the same person throughout, so you never have to start the story over.</p>'),
('<h3>Kaynağı belli bilgi</h3>', '<h3>Information with a source</h3>'),
('<p>Ücret, tarih ve kabul şartı paylaştığımızda kaynağını ve son güncelleme tarihini de veririz. Eski veriyi güncelmiş gibi göstermeyiz.</p>',
 '<p>When we give you a fee, a date or an admission condition, we give you its source and its last update. We do not present old data as current.</p>'),

# ---------------------------------------------------------------- map
('<!-- ==================================================================\n     BÖLÜM 8 — ÖNE ÇIKAN ÜNİVERSİTELER (etkileşimli harita)',
 '<!-- ==================================================================\n     SECTION 8 - FEATURED UNIVERSITIES (interactive map)'),
('<p class="eyebrow" data-reveal="up-sm">Üniversiteler</p>', '<p class="eyebrow" data-reveal="up-sm">Universities</p>'),
('Macaristan haritasında<br>nereye bakıyoruz?', 'Where on the map<br>are we looking?'),
('Şehir seçimi, üniversite kadar belirleyicidir: yaşam maliyeti, ulaşım, staj imkânı ve\n'
 '        Türk öğrenci topluluğu şehre göre değişir. Haritadan bir şehir seçin.',
 'Your city matters as much as your university: cost of living, transport, internship opportunities\n'
 '        and the size of the international community all change from one to the next. Pick a city on the map.'),
('aria-label="Macaristan haritası; üniversite şehirleri işaretli"',
 'aria-label="Map of Hungary with university cities marked"'),
('<!-- Macaristan sınırı: gerçek coğrafi koordinatlardan (WGS84) düzlemsel\n'
 '               izdüşümle üretilmiş sadeleştirilmiş poligon. Pin konumları da\n'
 '               aynı izdüşümü kullanır, bu yüzden şehirler doğru yerde durur. -->',
 '<!-- Hungary border: a simplified polygon produced from real WGS84 coordinates\n'
 '               with a planar projection. The pins use the same projection, which is\n'
 '               why the cities land in the right places. -->'),
('aria-label="Budapeşte">', 'aria-label="Budapest">'),
('<text class="pin__t" x="18" y="6">Budapeşte</text>', '<text class="pin__t" x="18" y="6">Budapest</text>'),
('<!-- Etiket batıya bakar: sağdaki Kecskemét ile çakışmasın -->',
 '<!-- Label faces west so it does not collide with Kecskemét to the right -->'),
('<p class="unis__map-hint num-mono" aria-hidden="true">Şehir seçin →</p>',
 '<p class="unis__map-hint num-mono" aria-hidden="true">Pick a city →</p>'),
('<!-- Mobil şehir seçici: harita pinleri küçük ekranda dokunma hedefi\n'
 '           olarak yetersiz kaldığı için seçim buradan yapılır. JS doldurur. -->',
 '<!-- Mobile city picker: map pins are too small to be reliable touch targets,\n'
 '           so the selection happens here. Populated by JS. -->'),
('<div class="unis__chips" data-map-chips role="group" aria-label="Şehir seçin"></div>',
 '<div class="unis__chips" data-map-chips role="group" aria-label="Pick a city"></div>'),
('<!-- İçerik JS ile şehre göre değişir; ilk yükte Budapeşte -->',
 '<!-- Content changes with the city via JS; Budapest on first load -->'),
('<p>Listedeki 19 üniversite, Hun Education aracılığıyla başvuru yapılabilen kurumlardır;\n'
 '      bu bir partnerlik ya da temsilcilik beyanı değildir. Program, ücret ve kabul şartları\n'
 '      üniversiteler tarafından değiştirilebilir; nihai bilgi için ilgili üniversitenin resmî\n'
 '      sayfasını esas alınız.</p>',
 '<p>The 19 universities listed are institutions you can apply to through Hun Education; this is not\n'
 '      a statement of partnership or representation. Programmes, fees and admission conditions may be\n'
 '      changed by the universities — treat the university’s own official page as definitive.</p>'),

# ---------------------------------------------------------------- stories
('<!-- ==================================================================\n     BÖLÜM 9 — ÖĞRENCİ HİKÂYELERİ',
 '<!-- ==================================================================\n     SECTION 9 - STUDENT STORIES'),
('<p class="eyebrow" data-reveal="up-sm">Öğrenci hikâyeleri</p>', '<p class="eyebrow" data-reveal="up-sm">Student stories</p>'),
('Sözü öğrencilere<br>bırakıyoruz', 'We leave the words<br>to our students'),
('Aşağıdaki deneyimler, süreçlerini birlikte yürüttüğümüz öğrencilerin izinli ve\n'
 '        gerçek yorumlarıdır. İsimler, öğrencilerin kendi tercihiyle baş harfle yazılır.',
 'The experiences below are genuine comments from students whose applications we handled, published\n'
 '        with their permission. Surnames appear as initials at the students’ own request.'),
('<p>Tüm işlemlerimde Hun Education danışmanları çok yardımcı oldu. Şimdi Budapeşte\'de,\n'
 '          büyük bir film yapımında Visual Effects departmanında çalışıyorum.</p>',
 '<p>The Hun Education advisers helped me enormously with every step. I now work in Budapest, in the\n'
 '          visual effects department of a major film production.</p>'),
('<span>Budapeşte Metropolitan Üniversitesi</span>', '<span>Budapest Metropolitan University</span>'),
('<p>Haziran 2022 itibarıyla 4. yıl bitmek üzere. Budapeşte\'de ve böyle kaliteli bir okulda\n'
 '          eğitim gördüğüm için kendimi şanslı hissediyorum.</p>',
 '<p>As of June 2022 I am about to finish my fourth year. I feel lucky to be studying in Budapest,\n'
 '          and at a university of this quality.</p>'),
('<span>Semmelweis Üniversitesi</span>', '<span>Semmelweis University</span>'),
('<span class="num-mono">Tıp</span>', '<span class="num-mono">Medicine</span>'),
('<p>Şu an Macaristan Samsung\'da çalışıyorum.</p>', '<p>I am now working at Samsung in Hungary.</p>'),
('<span>Debrecen Üniversitesi</span>', '<span>University of Debrecen</span>'),
('<span class="num-mono">Elektrik Mühendisliği</span>', '<span class="num-mono">Electrical Engineering</span>'),
('<h3 class="story__briefTitle">Daha fazlası</h3>', '<h3 class="story__briefTitle">And more</h3>'),
('<p>Tıp, hemşirelik, mühendislik ve dil yüksek lisansı okuyan öğrencilerin yazılı\n'
 '        deneyimleri ile altı video görüşme öğrenci görüşleri sayfasında yer alıyor.</p>',
 '<p>Written accounts from students in medicine, nursing, engineering and a language master’s, plus\n'
 '        six video interviews, are collected on the student reviews page.</p>'),
('<li><span class="num-mono">1</span> Sude A. · Pécs Üniversitesi · Tıp</li>',
 '<li><span class="num-mono">1</span> Sude A. · University of Pécs · Medicine</li>'),
('<li><span class="num-mono">2</span> Özlem D. · Pécs Üniversitesi · İngiliz Dili YL</li>',
 '<li><span class="num-mono">2</span> Özlem D. · University of Pécs · English Studies MA</li>'),
('<li><span class="num-mono">3</span> Sude · Pécs Üniversitesi · Hemşirelik</li>',
 '<li><span class="num-mono">3</span> Sude · University of Pécs · Nursing</li>'),
('<a class="link" href="#gorusme">Tüm öğrenci hikâyeleri', '<a class="link" href="#gorusme">All student stories'),

# ---------------------------------------------------------------- cost
('<!-- ==================================================================\n     BÖLÜM 10 — MALİYET GÖRÜNÜRLÜĞÜ',
 '<!-- ==================================================================\n     SECTION 10 - COST VISIBILITY'),
('<p class="eyebrow" data-reveal="up-sm">Maliyet görünürlüğü</p>', '<p class="eyebrow" data-reveal="up-sm">Cost visibility</p>'),
('Bütçenizi daha<br>baştan planlayın', 'Plan your budget<br>from the start'),
('Toplam maliyet yalnızca öğrenim ücreti değildir. Eğitim seviyenizi ve konaklama\n'
 '        tercihinizi seçin; yıllık tahmini aralık ve kalem kalem dağılımı anında güncellensin.',
 'The total is not just tuition. Choose your study level and your accommodation, and the estimated\n'
 '        annual range and its item-by-item breakdown update instantly.'),
('<p>Sonuç tek bir rakam değil bir <b>aralıktır</b>: aynı programda yurtta kalan öğrenciyle\n'
 '        stüdyo dairede kalan arasında yılda birkaç bin euro fark oluşur. Aralığın alt ve üst ucu\n'
 '        bu farkı gösterir; kesin tutar üniversiteye ve şehre göre değişir.</p>',
 '<p>The answer is a <b>range</b>, not a single figure: on the same programme, a student in a\n'
 '        dormitory and one in a studio flat are several thousand euros apart each year. The two ends of\n'
 '        the range show that gap; the exact amount depends on the university and the city.</p>'),
('<span data-t="Bana Özel Bütçe Planı İstiyorum">Bana Özel Bütçe Planı İstiyorum</span>',
 '<span data-t="Build My Budget Plan">Build My Budget Plan</span>'),
('<span class="ccard__label">Tahmini yıllık maliyet</span>', '<span class="ccard__label">Estimated annual cost</span>'),

# ---------------------------------------------------------------- guides
('<!-- ==================================================================\n     BÖLÜM 11 — REHBER',
 '<!-- ==================================================================\n     SECTION 11 - GUIDES'),
('<p class="eyebrow" data-reveal="up-sm">Rehber</p>', '<p class="eyebrow" data-reveal="up-sm">Guides</p>'),
('<h2 class="h-md display" id="guides-h" data-reveal="up">Karar vermeden önce okuyun</h2>',
 '<h2 class="h-md display" id="guides-h" data-reveal="up">Read this before you decide</h2>'),
('<a class="link" href="macaristanda-egitim.html" data-reveal="up-sm">Tüm rehber içerikleri',
 '<a class="link" href="study-in-hungary.html" data-reveal="up-sm">All guide content'),
('data-cursor="Oku"', 'data-cursor="Read"'),
('<a class="gcard card" href="basvuru.html"', '<a class="gcard card" href="admission-requirements.html"'),
('alt="Macaristan üniversite başvurusu için hazırlanan belgeler ve pasaport"',
 'alt="Documents and passport prepared for a Hungarian university application"'),
('<span class="chip chip--soft num-mono">Başvuru</span>', '<span class="chip chip--soft num-mono">Admissions</span>'),
('<h3 class="card__title">Macaristan üniversite başvuru şartları ve gerekli belgeler</h3>',
 '<h3 class="card__title">University admission requirements and documents in Hungary</h3>'),
('<p class="gcard__ex">Apostilli diploma, transkript, dil belgesi ve banka dökümü: dosyanın tam kontrol listesi.</p>',
 '<p class="gcard__ex">Apostilled diploma, transcript, language certificate and bank statement: the full checklist.</p>'),
('<span class="chip chip--soft num-mono">Tıp</span>', '<span class="chip chip--soft num-mono">Medicine</span>'),
('<h3 class="card__title">Macaristan\'da tıp eğitimi ve tıp diploması</h3>',
 '<h3 class="card__title">Studying medicine in Hungary and the degree that follows</h3>'),
('<p class="gcard__ex">Giriş sınavı, altı yıllık program yapısı ve mezuniyet sonrası yol haritası.</p>',
 '<p class="gcard__ex">The entrance exam, the structure of the six-year programme and what comes after graduation.</p>'),
('<span class="chip chip--soft num-mono">Pilotaj</span>', '<span class="chip chip--soft num-mono">Pilot training</span>'),
('<h3 class="card__title">Macaristan üniversitelerinde pilotaj eğitimi</h3>',
 '<h3 class="card__title">Pilot training at Hungarian universities</h3>'),
('<p class="gcard__ex">Teorik eğitim ile uçuş saatlerinin ayrı ücretlendirilmesi ve sağlık şartları.</p>',
 '<p class="gcard__ex">How ground school and flight hours are priced separately, and the medical requirements.</p>'),
('<a class="gcard card" href="macaristanda-egitim.html"', '<a class="gcard card" href="study-in-hungary.html"'),
('alt="Budapeşte\'de şehir oryantasyonu turunda öğrenciler"',
 'alt="Students on a city orientation tour in Budapest"'),
('<span class="chip chip--soft num-mono">Yaşam</span>', '<span class="chip chip--soft num-mono">Student life</span>'),
('<h3 class="card__title">Macaristan\'da üniversite eğitimi ve yaşam: bilmeniz gerekenler</h3>',
 '<h3 class="card__title">Studying and living in Hungary: what you need to know</h3>'),
('<p class="gcard__ex">Konaklama, ulaşım, bütçe ve ilk ay yapılacak resmî işlemler.</p>',
 '<p class="gcard__ex">Accommodation, transport, budget and the official steps of your first month.</p>'),
('<span class="chip chip--updated num-mono">güncel: 08.2026</span>',
 '<span class="chip chip--updated num-mono">updated: 08.2026</span>'),
('<span class="chip chip--soft num-mono">8 dk okuma</span>', '<span class="chip chip--soft num-mono">8 min read</span>'),
('<span class="chip chip--soft num-mono">9 dk okuma</span>', '<span class="chip chip--soft num-mono">9 min read</span>'),
('<span class="chip chip--soft num-mono">7 dk okuma</span>', '<span class="chip chip--soft num-mono">7 min read</span>'),
('<span class="chip chip--soft num-mono">6 dk okuma</span>', '<span class="chip chip--soft num-mono">6 min read</span>'),
('href="programlar.html?alan=tip" data-reveal="up"', 'href="programs.html?alan=tip" data-reveal="up"'),
('href="programlar.html?alan=pilot" data-reveal="up"', 'href="programs.html?alan=pilot" data-reveal="up"'),
]

miss = []
for a, b in R:
    if a not in s:
        miss.append(a[:90])
    s = s.replace(a, b)

io.open(P, 'w', encoding='utf-8').write(s)
print('index.html (bolum 6-11) yazildi:', len(s))
if miss:
    print('ESLESMEYEN:', len(miss))
    for m in miss:
        print('  !', m)
else:
    print('bu partide tum kaliplar eslesti')
