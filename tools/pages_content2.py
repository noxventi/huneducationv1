# -*- coding: utf-8 -*-
# Kalan sayfalar. gen_pages.py'nin sonundan exec edilir.



# =====================================================================
# 3) MACARİSTAN'DA EĞİTİM (pillar)
# =====================================================================
qa_pillar = [
    ("Macaristan'da eğitim dili nedir?",
     "<p>Uluslararası öğrencilere yönelik programların büyük çoğunluğu <b>İngilizce</b> yürütülür. "
     "Macarca bilmek başvuru için şart değildir; günlük hayatta işe yarar ama derslerin gereği değildir.</p>"),
    ("Diplomam Türkiye'de geçerli olur mu?",
     "<p>Yurt dışında alınan diplomaların Türkiye'de kullanılabilmesi için YÖK denklik değerlendirmesi "
     "gerekir. Denklik; üniversitenin tanınırlığı, program içeriği, eğitim süresi ve mezuniyet "
     "koşullarına göre değerlendirilir ve bazı alanlarda ek sınav istenebilir. Kurallar değişebildiği "
     "için başvurudan önce YÖK'ün güncel mevzuatını doğrudan incelemenizi öneririz. "
     "<b>Otomatik veya garantili denklik iddiasında bulunmuyoruz.</b></p>"),
    ("Öğrenciyken çalışabilir miyim?",
     "<p>Öğrenci ikametiyle çalışma hakkı, süresi ve koşulları Macaristan mevzuatına tabidir ve "
     "değişebilir. Planlarınızı çalışma geliri üzerine kurmadan önce güncel düzenlemeyi resmî "
     "kaynaktan teyit edin.</p>"),
    ("Hangi şehir öğrenci için daha uygun?",
     "<p>Budapeşte en geniş program çeşitliliğini ve en büyük uluslararası topluluğu sunar ama yaşam "
     "maliyeti en yüksek şehirdir. Debrecen, Szeged ve Pécs benzer akademik kalitede daha düşük "
     "yaşam maliyetiyle öne çıkar. Seçim; bölümünüzün hangi şehirde açıldığına ve bütçenize bağlıdır.</p>"),
]

body_pillar = f'''<div class="alayout">
{toc([('neden','Neden Macaristan?'),('sistem','Eğitim sistemi ve dereceler'),
      ('sehirler','Hangi şehirde okumalı?'),('vize','Vize, oturum ve denklik'),
      ('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}

<article class="prose">

<section id="giris" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Macaristan, Avrupa Birliği üyesi bir ülkede İngilizce eğitim alarak uluslararası geçerliliğe
  sahip bir diploma edinmek isteyen öğrenciler için güçlü bir seçenek sunar. Üniversiteler YKS puanı
  talep etmez; başvuruları kendi kabul süreçleri üzerinden değerlendirir. Lisans programları 3–4
  yıl, <a class="link" href="{S['masters']}">yüksek lisans programları</a> 2 yıl, <a class="link" href="{S['medicine']}">tıp</a> ve diş hekimliği gibi bütünleşik programlar ise 5–6 yıl sürer. Eğitim ve yaşam giderleri birlikte yıllık 8.500 – 14.000 € aralığında kalır.</p>

  <p><b>Hun Education olarak,</b> 20 seçkin üniversitede sunulan 490 İngilizce program arasından
  öğrencilerimizin hedeflerine en uygun seçeneği belirliyor; başvurudan kabul ve vize sürecine kadar
  her adımda yanlarında oluyoruz.</p>
</section>

<p>Bu sayfada Macaristan'daki eğitim sisteminin nasıl işlediğini, hangi şehirde neyin öne çıktığını,
öğrenci vizesinin nasıl alındığını ve diplomanızın Türkiye'de ne anlama geldiğini anlatıyoruz.</p>

<h2 id="neden">Neden Macaristan?</h2>
{figure('budapeste-balikci-tabyasi',
        'Balıkçı Tabyası’nın kemerinden gün doğumunda Budapeşte manzarası',
        'Balıkçı Tabyası’ndan Budapeşte.')}
<p>Macaristan'ı Türk öğrenciler için öne çıkaran şey tek bir avantaj değil, birkaç etkenin bir arada
çalışması. Bunların başında bütçe gelir: öğrenim ücretleri de yaşam giderleri de Batı Avrupa'nın
belirgin şekilde altında seyreder ve bir akademik yılı toplamda 8.500 – 14.000 € bandında tutar.</p>

<p>İkinci etken program çeşitliliği. <a class="link" href="{S['medicine']}">Tıptan</a> <a class="link" href="{S['pilot']}">pilotaja</a>, mühendislikten sanata kadar uluslararası
öğrenciye açık geniş bir yelpaze var ve bunların tamamı İngilizce yürür. Üstelik bu programlar yeni
kurulmuş değil; Pécs Üniversitesi 1367'de kuruldu, Semmelweis'te tıp eğitimi 1769'a dayanır ve Macar
asıllı bilim insanları bugüne kadar 16 Nobel Ödülü kazandı.</p>

<p>Üçüncüsü ise konum ve topluluk. Viyana, Bratislava ve Prag kara yoluyla birkaç saat uzaklıkta;
ülkede 40 bine yakın uluslararası öğrenci okur ve Budapeşte, Debrecen ile Pécs'te yerleşmiş bir Türk
öğrenci ağı sizi bekler. Yani gittiğinizde yalnız kalmıyorsunuz.</p>
{inline_cta("Bu programlardan hangisine gerçekçi şansınız var? İlk görüşmede söyleyelim.")}

{strip('Macaristan üniversitelerinden kareler', [
 ('elte-tarihi-bina', 'ELTE’nin tarihi taş cepheli binası',
  'ELTE, Budapeşte.'),
 ('debrecen-ana-bina', 'Debrecen Üniversitesi’nin sütunlu ana binası ve önündeki havuz',
  'Debrecen Üniversitesi ana binası.'),
 ('szeged-ana-bina', 'Szeged Üniversitesi’nin sarı cepheli ana binası',
  'Szeged Üniversitesi.'),
 ('pecs-tas-kemer-giris', 'Pécs Üniversitesi’nin taş kemerli avlu girişi',
  'Pécs’te avlu girişi.'),
 ('bme-tuna-kiyisi', 'Tuna kıyısındaki tarihi üniversite binası ve nehirde bir gemi',
  'Tuna kıyısında üniversite binası.'),
])}

<h2 id="sistem">Eğitim sistemi ve dereceler</h2>
<p>Macaristan, Bologna sistemine uyumlu üç kademeli bir yapı kullanır. Tıp, diş hekimliği,
eczacılık ve mimarlık gibi alanlar ise bütünleşik (tek aşamalı) programlarla yürütülür.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Derece seviyeleri, süreleri ve yıllık ücret aralıkları</caption>
  <thead><tr><th>Seviye</th><th>Süre</th><th>Yıllık ücret</th><th>Giriş şartı</th></tr></thead>
  <tbody>
    <tr><td><b>Hazırlık</b></td><td>1 yıl</td><td class="num">yıllık 2.500 €'dan</td><td>Üniversitenin kendi sınavı</td></tr>
    <tr><td><b>Lisans</b></td><td>3 – 4 yıl</td><td class="num">3.000 – 5.000 €</td><td>Lise diploması · B2 düzeyi İngilizce</td></tr>
    <tr><td><b>Yüksek lisans</b></td><td>2 yıl</td><td class="num">4.000 – 6.000 €</td><td>Lisans diploması · üniversitenin değerlendirmesi</td></tr>
    <tr><td><b>Doktora</b></td><td>3 – 4 yıl</td><td class="num">6.000 – 8.000 €</td><td>Yüksek lisans diploması</td></tr>
    <tr><td><b>Bütünleşik (tıp, diş)</b></td><td>5 – 6 yıl</td><td class="num">15.800 € – 19.900 $</td><td>Kimya ve biyoloji giriş sınavı</td></tr>
  </tbody>
</table>
</div>

<h3>Eğitim dili</h3>
<p>Uluslararası programların tamamı İngilizce yürütülür ve başvuru için Macarca bilmenize gerek yok.
Lisansta pratikte B2 seviyesi beklenir, yüksek lisansta IELTS 6,5 isteyen üniversiteler var; ancak
okulların çoğu belge yerine kendi mülakatını yapar. Seviyeniz yetmiyorsa üniversitelerin İngilizce
hazırlık programlarına başvurabilirsiniz. Macarca ise günlük hayat ve staj olanakları açısından
avantaj sağlar; birçok üniversite başlangıç seviyesi Macarcayı ücretsiz veya çok düşük ücretle
verir.</p>

<h2 id="sehirler">Hangi şehirde okumalı?</h2>
{figure('pecs-sehir-hava',
        'Pécs şehir merkezinin kırmızı çatılı havadan görünümü',
        'Pécs. Budapeşte dışındaki şehirlerde yaşam maliyeti belirgin şekilde düşük.',
        1280, 720)}
<p>Şehir seçimi en az üniversite seçimi kadar belirleyici olur; çünkü yaşam maliyeti, ulaşım ve öğrenci
topluluğu şehre göre değişir.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Program sunulan başlıca şehirler</caption>
  <thead><tr><th>Şehir</th><th>Bölge</th><th>Öne çıkan</th></tr></thead>
  <tbody>
    <tr><td><b>Budapeşte</b></td><td>Orta Macaristan</td><td>En geniş program çeşitliliği · en yüksek yaşam maliyeti</td></tr>
    <tr><td><b>Debrecen</b></td><td>Doğu Macaristan</td><td>Sağlık ve mühendislikte köklü gelenek · katalogda 130'dan fazla program</td></tr>
    <tr><td><b>Szeged</b></td><td>Güney Macaristan</td><td>Kampüs ile şehir iç içe · daha düşük maliyet</td></tr>
    <tr><td><b>Pécs</b></td><td>Güneybatı</td><td>Ülkenin en eski üniversitesi · yürünebilir şehir</td></tr>
    <tr><td><b>Miskolc</b></td><td>Kuzeydoğu</td><td>Mühendislik ve yer bilimleri</td></tr>
    <tr><td><b>Dunaújváros</b></td><td>Orta Macaristan</td><td>Pilotluk ve makine mühendisliğini birleştiren program</td></tr>
    <tr><td><b>Nyíregyháza</b></td><td>Kuzeydoğu</td><td>Düşük yaşam maliyeti</td></tr>
    <tr><td><b>Kecskemét</b></td><td>Orta Macaristan</td><td>Sanayi bağlantılı mühendislik</td></tr>
  </tbody>
</table>
</div>

<h2 id="vize">Vize, oturum ve denklik</h2>
<p>Türk vatandaşları Macaristan'da öğrenim için <b>D tipi öğrenci vizesi</b> ile giriş yapar.
Vize başvurusunun temel belgesi üniversiteden gelen Nihai Kabul Mektubudur; ayrıca son 6 aylık
banka hesap dökümü, konaklama kanıtı ve sağlık sigortası istenir.</p>
<ol class="steps">
  <li><div><h3>Kabul mektubu</h3><p>Üniversiteden nihai kabul alınır.</p></div></li>
  <li><div><h3>Konsolosluk başvurusu</h3><p>En yakın Macaristan Konsolosluğuna randevu alınarak dosya sunulur.</p></div></li>
  <li><div><h3>Ülkeye giriş</h3><p>Vize onaylandıktan sonra seyahat planlanır.</p></div></li>
  <li><div><h3>İkamet kaydı</h3><p>Varıştan sonra ikamet izni işlemleri tamamlanır.</p></div></li>
</ol>
<p>Vize dosyasını sizin yerinize biz kuruyoruz: hangi belgenin hangi sırayla hazırlanacağını,
randevu takvimini ve konsolosluğun beklediği formatı biliyoruz. Kararı elbette konsolosluk verir,
ama dosyanın eksiksiz gitmesi bizim işimiz.</p>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Güvenceniz şu: vize çıkmazsa, konsolosluğun yazılı ret gerekçesi üniversiteye iletildikten sonra
öğrenim ücreti genellikle 30 iş günü içinde iade edilir. Vize kararı resmî makama ait olduğu için
hiçbir danışmanlık şirketi garanti veremez; size garanti sözü veren bir kaynağa temkinli yaklaşın.</p>

<h3>Denklik ve mezuniyet sonrası</h3>
<p>Diplomanızı Türkiye'de kullanmak istiyorsanız YÖK denklik sürecinden geçmeniz gerekir. Denklik;
üniversitenin tanınırlığı, programın içeriği, eğitim süresi ve mezuniyet koşulları üzerinden
değerlendirilir ve bazı alanlarda ek sınav istenebilir.</p>
<p>Bu adımı sonraya bırakmıyoruz: program seçerken denklik açısından dikkat edilmesi gereken
noktaları birlikte gözden geçiriyoruz, böylece mezuniyette sürprizle karşılaşmıyorsunuz. Mevzuat
değişebildiği için başvurudan önce YÖK'ün güncel kurallarını da doğrudan incelemenizi öneririz;
kararı veren kurum YÖK olduğu için sonuç hakkında taahhüt vermiyoruz.</p>

<h2 id="sss">Sık sorulan sorular</h2>
{faq_block(qa_pillar)}

<section id="kaynak" class="sources">
  <h2>Kaynaklar ve doğrulama</h2>
  <ol>
    <li>Derece süreleri ve ücret aralıkları üniversitelerin resmî yayınlarından, şehir bilgileri Budapeşte ve Pécs'teki ekibimizin saha deneyiminden derlenir.</li>
    <li>Denklik konusunda bağlayıcı kaynak YÖK'ün güncel mevzuatıdır; vize konusunda ilgili konsolosluktur.</li>
    <li>Öğrenci çalışma hakkı Macaristan mevzuatına tabidir ve değişebilir.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Macaristan'da okumaya bugün başlayın", "Akademik geçmişinizi ve hedefinizi konuşalım; size uygun 3–5 gerçekçi programı ilk görüşmede önerelim. Görüşme ücretsiz, sonrası size kalmış.")}

{related([(S['unis'],"Üniversite","20 üniversite","Şehir, tür ve alanlarıyla tam liste."),
          (S['apply'],"Başvuru","Başvuru şartları","Belgeler, dil şartı, giriş sınavı ve takvim."),
          (S['costs'],"Maliyet","Ücretler ve yaşam gideri","Yıllık toplam bütçe aralığı.")])}
</article>
</div>'''

write(S['edu'], page(
    S['edu'],
    "Macaristan'da Üniversite Okumak: YKS'siz Kabul ve Ücretler | Hun Education",
    "Macaristan'da üniversite eğitimi rehberi: YKS'siz kabul, yıllık 8.500 – 14.000 € bütçe, "
    "İngilizce programlar, şehirler, D tipi öğrenci vizesi ve YÖK denklik süreci.",
    'Ana rehber',
    "Macaristan'da üniversite eğitimi",
    'YKS’siz kabul, baştan sona İngilizce eğitim ve Avrupa’da geçerli bir diploma. Sistem nasıl '
    'işler, hangi şehirde ne var ve süreç sizin için nasıl yürür?',
    body_pillar, S['edu'],
    [HOME, ("Macaristan'da Eğitim", url_of('edu'))],
    qa_pillar))

# =====================================================================
# 4) ÜNİVERSİTELER
# =====================================================================
rows = '\n'.join(
    '    <tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td><td><a href="%s?uni=%s">Programlar</a></td></tr>'
    % (u['ad'], u['sehir'], u['tur'], ' · '.join(u['alanlar'][:3]), S['progs'], u['id'])
    for u in sorted(UNIS, key=lambda x: (x['sehir'] == '—', x['sehir'], x['ad'])))

by_city = {}
for u in UNIS:
    by_city.setdefault(u['sehir'], []).append(u['ad'])
city_list = '\n'.join(
    '  <li><b>%s</b>: %s</li>' % (c, ', '.join(v))
    for c, v in sorted(by_city.items(), key=lambda kv: (kv[0] == '—', -len(kv[1]))))

qa_uni = [
    ("Hangi üniversiteye başvurabilirim?",
     "<p>Başvurabileceğiniz üniversite; mezuniyet dereceniz, dil seviyeniz, seçtiğiniz alan ve "
     "bütçenize göre değişir. Aynı bölüm birden fazla üniversitede açılabilir ve kabul şartları "
     "farklılaşabilir. Program kataloğundan filtreleyerek başlayabilirsiniz.</p>"),
    ("Devlet ve özel üniversite arasındaki fark nedir?",
     "<p>Devlet üniversiteleri genellikle daha köklü ve daha geniş program yelpazesine sahiptir. "
     "Özel ve vakıf üniversiteleri ise daha küçük sınıflar, sektör bağlantılı programlar ve "
     "esnek başlangıç dönemleri sunabilir. Diploma geçerliliği açısından belirleyici olan kurumun "
     "tanınırlığıdır, statüsü değil.</p>"),
    ("Aynı anda birden fazla üniversiteye başvurabilir miyim?",
     "<p>Evet ve öneririz. Kontenjanlar dönem içinde kapanabildiği için birden fazla seçenekle "
     "ilerlemek riski azaltır. Her üniversitenin kendi başvuru ücreti olduğunu hesaba katın.</p>"),
]

body_uni = f'''<div class="alayout">
{toc([('liste','Üniversite listesi'),('sehir','Şehre göre dağılım'),
      ('secim','Nasıl seçmeli?'),('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}

<article class="prose">

<section id="kisa-cevap" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Macaristan'ın sekiz farklı şehrinde, uluslararası öğrencilere kapılarını açan
  <b>{len(UNIS)} üniversite</b> bulunur. Program çeşitliliği açısından Budapeşte ilk sırada yer alırken
  Debrecen, Szeged ve Pécs benzer akademik kaliteyi daha uygun yaşam maliyetiyle sunar. Hazırlık
  programlarından tıp ve pilotaja uzanan geniş bir yelpazede toplam
  <b>{sum(u["programSayisi"] for u in UNIS)} İngilizce program</b> yer alır.</p>

  <p><b>Hun Education olarak,</b> bu üniversitelerin tamamına başvuru gönderiyoruz. Akademik
  geçmişinizi ve hedeflerinizi değerlendirerek profilinize en uygun kurumları belirliyor, tercih
  listenizi birlikte oluşturuyoruz.</p>
</section>

<h2 id="liste">Üniversite listesi</h2>
{galeri([
 ('pecs-universitesi-tabela',
  'Pécs Üniversitesi binası; girişte “University of Pécs” tabelası',
  'Pécs Üniversitesi', 'Ülkenin en eski üniversitesi; tıp, diş hekimliği ve eczacılık.'),
 ('debrecen-cam-bina',
  'Debrecen Üniversitesi’nin cam cepheli modern binası',
  'Debrecen Üniversitesi', 'Sağlık ve mühendislikte köklü gelenek.'),
 ('elte-avlu',
  'ELTE’nin kemerli iç avlusu',
  'ELTE', 'Beşeri bilimler, sosyal bilimler ve psikoloji.'),
 ('szeged-modern-bina',
  'Szeged Üniversitesi’nin cam cepheli modern binası',
  'Szeged Üniversitesi', 'Tıp ve fen bilimleri; düşük yaşam maliyeti.'),
 ('miskolc-cam-bina',
  'Miskolc Üniversitesi’nin cam cepheli binası ve önündeki meydan',
  'Miskolc Üniversitesi', 'Mühendislik ve yer bilimleri.'),
 ('obuda-sari-bina',
  'Óbuda Üniversitesi’nin sarı cepheli tarihi binası',
  'Óbuda Üniversitesi', 'Budapeşte’de mühendislik ve bilişim.'),
 ('metu-bina-tabela',
  '“Budapesti Metropolitan Egyetem” yazılı yuvarlak kampüs binası',
  'Budapeşte Metropolitan', 'Tasarım, medya ve işletme.'),
 ('univet-avlu-heykeller',
  'Veteriner Üniversitesi’nin avlusu; iki yanda köpek heykelleri',
  'Veteriner Üniversitesi', 'Budapeşte’de veterinerlik eğitimi.'),
 ('corvinus-bina',
  'Corvinus Üniversitesi’nin modern cam ve taş cepheli binası',
  'Corvinus Üniversitesi', 'İşletme ve ekonomi.'),
])}
<p>Aşağıdaki tablo şehre göre sıralandı. “Öne çıkan alanlar” sütunu, o üniversitede
kataloğumuzda program bulunan başlıca alanları gösterir; kurumun tüm fakülte yapısı değildir.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Hun Education aracılığıyla başvurulabilen üniversiteler</caption>
  <thead><tr><th>Üniversite</th><th>Şehir</th><th>Tür</th><th>Öne çıkan alanlar</th><th>Katalog</th></tr></thead>
  <tbody>
{rows}
  </tbody>
</table>
</div>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Bu liste bir partnerlik ya da temsilcilik beyanı değildir; başvuru yapılabilen kurumları gösterir.</p>

<h2 id="sehir">Şehre göre dağılım</h2>
{strip('Üniversite şehirlerinden kareler', [
 ('miskolc-kampus-hava', 'Sonbaharda Miskolc Üniversitesi kampüsünün havadan panoraması',
  'Miskolc kampüsü sonbaharda.'),
 ('debrecen-kuleli-bina', 'Debrecen Üniversitesi’nin kuleli binası',
  'Debrecen’de kampüs.'),
 ('pecs-sonbahar-kampus', 'Sonbaharda Pécs Üniversitesi binası ve önündeki ağaçlar',
  'Pécs’te sonbahar.'),
 ('elte-gece-cephe', 'ELTE binasının gece ışıklandırılmış cephesi',
  'Budapeşte’de akşam.'),
])}
<ul>
{city_list}
</ul>

<h2 id="secim">Nasıl seçmeli?</h2>
{figure('pecs-kampus-hava',
        'Pécs Üniversitesi kampüsünün havadan görünümü',
        'Pécs Üniversitesi kampüsü, havadan.')}
<ol class="steps">
  <li><div><h3>Önce bölümü sabitleyin</h3><p>Üniversite değil bölüm seçilir. Aynı bölüm birkaç üniversitede açılıyorsa karşılaştırma anlamlı hâle gelir.</p></div></li>
  <li><div><h3>Kabul şartını kontrol edin</h3><p>Giriş sınavı, dil puanı ve portfolyo şartları kurumdan kuruma değişir.</p></div></li>
  <li><div><h3>Şehri bütçeyle birlikte düşünün</h3><p>Öğrenim ücreti düşük ama kirası yüksek bir şehir toplamda daha pahalı olabilir.</p></div></li>
  <li><div><h3>Birden fazla seçenekle ilerleyin</h3><p>Kontenjan kapanma riskine karşı en az iki üniversiteye başvurun.</p></div></li>
</ol>

<h2 id="sss">Sık sorulan sorular</h2>
{faq_block(qa_uni)}

<section id="kaynak" class="sources">
  <h2>Kaynaklar ve doğrulama</h2>
  <ol>
    <li>Liste, aracılık yaptığımız başvuruların güncel kapsamını yansıtır ve her başvuru dönemi öncesinde gözden geçirilir.</li>
    <li>Program, ücret ve kabul şartları üniversiteler tarafından değiştirilebilir.</li>
    <li>Nihai bilgi için ilgili üniversitenin resmî sayfası esastır.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Hangi üniversite size uygun?", "Profilinize uyan üniversiteleri kabul şartı, ücret ve şehir bilgisiyle karşılaştırmalı olarak sunalım.")}

{related([(S['progs'],"Katalog","Program kataloğu","490 programı filtreleyerek karşılaştırın."),
          (S['costs'],"Maliyet","Üniversiteye göre ücret","ELTE, Debrecen ve Pécs karşılaştırması."),
          (S['apply'],"Başvuru","Başvuru şartları","Belgeler, sınavlar ve takvim.")])}
</article>
</div>'''

write(S['unis'], page(
    S['unis'],
    'Macaristan Üniversiteleri: 20 Üniversite, Şehir Şehir | Hun Education',
    "Macaristan'da başvuru yapılabilen üniversiteler; şehir, tür ve öne çıkan alanlarıyla tam liste. "
    "Budapeşte, Debrecen, Szeged, Pécs ve diğer şehirlerdeki seçenekler.",
    'Üniversite rehberi',
    'Macaristan üniversiteleri',
    'Hangi üniversite hangi şehirde, hangi alanlarda program açar? Tam listeyi karşılaştırılabilir '
    'biçimde bir arada topladık.',
    body_uni, S['unis'],
    [HOME, ('Üniversiteler', url_of('unis'))],
    qa_uni))
