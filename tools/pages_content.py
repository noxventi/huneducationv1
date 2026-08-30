# -*- coding: utf-8 -*-
# gen_pages.py tarafından exec edilir. İçerik huneducation.com verisinden
# yeniden yazılmıştır, birebir kopya değildir.



# =====================================================================
# 1) BAŞVURU ŞARTLARI
# =====================================================================
qa_basvuru = [
    ("Macaristan'da üniversite okumak için YKS gerekli mi?",
     "<p>Hayır, <b>YKS puanı istenmez</b>. Üniversiteler kendi kabul sürecini yürütür: lise "
     "notlarınıza bakar, sağlık, mühendislik, mimarlık ve sanat programlarında ise kendi giriş "
     "sınavını ya da mülakatını yapar. Yani tek bir sınav gününe değil, konusu belli ve "
     "hazırlanabilir bir değerlendirmeye giriyorsunuz.</p>"),
    ("Dil belgem yoksa başvurabilir miyim?",
     "<p>Evet. Üniversitelerin çoğu zaten dil belgesi istemez, kendi mülakatını yapar. B2 "
     "seviyesinde değilseniz üniversite bünyesindeki İngilizce Dil Hazırlık programına "
     "başvurabilirsiniz; ücretler yıllık 2.500 €'dan başlar ve program başarıyla tamamlandığında "
     "bölüme geçiş yapılır.</p>"),
    ("Vize alamazsam ödediğim ücret ne olur?",
     "<p>Konsolosluğun verdiği yazılı ret gerekçesini üniversiteye ilettikten sonra öğrenim ücreti "
     "genellikle 30 iş günü içinde iade edilir. Başvuru, sınav ve kayıt ücretleri iade kapsamı "
     "dışındadır. Kesin koşullar hizmet sözleşmenizde yer alır.</p>"),
    ("Diploma ve transkriptimin çevirisi nasıl olmalı?",
     "<p>Belgeler İngilizce olmalı ya da yeminli tercüme ile İngilizceye çevrilmelidir. "
     "Diplomanın ayrıca apostil şerhi taşıması gerekir. Apostil, belgenin düzenlendiği ülkedeki "
     "yetkili makamdan alınır ve çeviriden önce yapılması zaman kazandırır.</p>"),
]

body_basvuru = f'''<div class="alayout">
{toc([('uygunluk','Kimler başvurabilir?'),('belgeler','Gerekli belgeler ve dil şartı'),
      ('sinav','Giriş sınavı ve mülakat'),('takvim','Başvuru takvimi ve süreç'),
      ('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}

<article class="prose">

<section id="giris" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Macaristan üniversitelerine başvuru süreci, birçok öğrencinin düşündüğünden çok daha sade
  ilerler. Başvuru dosyası; apostilli diploma, İngilizce transkript, pasaport fotokopisi ve İngilizce
  özgeçmişten oluşur. Banka dökümü ise başvuru aşamasında değil, vize başvurusu sırasında istenir.
  Lisans programlarında B2 düzeyinde İngilizce beklenir; ancak üniversitelerin büyük bölümü dil
  belgesi yerine kendi mülakatını uygular.</p>

  <p><b>Hun Education olarak,</b> başvuru dosyanızı sizin adınıza hazırlıyor ve eksik kalan noktaları
  başvurudan önce tamamlıyoruz. Belge hazırlığından üniversite yazışmalarına kadar sürecin tamamını
  öğrencilerimiz adına yürütüyoruz.</p>
</section>

<p>Bu sayfada hangi belgelerin istendiğini, dil şartının gerçekte ne olduğunu, giriş sınavı olan
bölümleri ve başvuru takvimini adım adım anlatıyoruz.</p>

<h2 id="uygunluk">Kimler başvurabilir?</h2>
{strip('Öğrencilerimizden kareler', [
 ('metu-ogrenci-grubu', 'Kampüs bahçesinde toplanmış uluslararası öğrenci grubu',
  'Kampüste uluslararası öğrenciler.'),
 ('obuda-ogrenciler', 'Óbuda Üniversitesi tabelası altında bankta oturan öğrenci grubu',
  'Ders arası.'),
 ('budapeste-koprude-ogrenciler', 'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci',
  'Özgürlük Köprüsü’nde öğrencilerimiz.'),
 ('pilotaj-ogrenciler-pist', 'Pilot gömlekli üç öğrenci, uçuş alanında birlikte',
  'Pilotaj öğrencilerimiz uçuş alanında.'),
])}
<p>İyi haber şu ki adayların büyük çoğunluğu zaten uygun. Yine de üç başlığı evrak hazırlığına
başlamadan netleştirmenizde fayda var; böylece boşuna zaman kaybetmiyorsunuz.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Program türüne göre yaş sınırı</caption>
  <thead><tr><th>Program</th><th>Üst yaş sınırı</th></tr></thead>
  <tbody>
    <tr><td>Hazırlık programları</td><td class="num">25</td></tr>
    <tr><td>Lisans</td><td class="num">25</td></tr>
    <tr><td>Yüksek lisans</td><td class="num">28</td></tr>
    <tr><td>Tıp, diş hekimliği, eczacılık</td><td>Yaş sınırı yok</td></tr>
  </tbody>
</table>
</div>
<p>Yaşınız bu sınırların üzerindeyse yine de yazın. Sınırlar gerçek ama çoğu durumda uygun bir yol
çıkar; hangisi olduğunu ilk görüşmede söyleriz.</p>

<h3>Uyruk</h3>
<p>25'ten fazla ülkenin vatandaşı adına başvuru gönderebiliyoruz: <b>Avrupa Birliği ülkeleri, ABD ve
Latin Amerika ülkeleri, Arnavutluk, Cezayir, Azerbaycan, Bosna Hersek, Mısır, Gürcistan, Ürdün,
Kazakistan, Kırgızistan, Moğolistan, Katar, Rusya, Sırbistan, Tayland, Türkiye, Ukrayna, Özbekistan
ve Vietnam.</b> Listede yoksanız yine de yazın; doğru kanalı gösterelim.</p>

<h3>Mali yeterlilik</h3>
<p>Konsolosluk eğitiminizin finanse edildiğini görmek ister ve beklenen tutar sanıldığından düşük:
<b>aylık ortalama 650 € × 10 aylık akademik yıl, yani yaklaşık 6.500 €</b>; kendi ya da sponsorunuzun
hesabında, düzenli gelir kanıtıyla birlikte. Bu Macaristan'a özgü bir kural değil, her ülkenin
konsolosluğu aynı şeye bakar. Sponsor mektubuyla nasıl belgeleneceğini birlikte planlıyoruz.</p>

{inline_cta("Profiliniz uygun mu? Tek mesajla öğrenin.")}

<h2 id="belgeler">Gerekli belgeler ve dil şartı</h2>
<p>Aşağıdaki belgeler her başvuruda istenir. Programa göre ek belge çıkabiliyor; kabul şartlarını
başvurudan önce birlikte gözden geçirdiğimiz için eksik bir dosyayla yola çıkmıyorsunuz.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Başvuru dosyasının çekirdek belgeleri</caption>
  <thead><tr><th>Belge</th><th>Biçim şartı</th><th>Not</th></tr></thead>
  <tbody>
    <tr><td><b>Başvuru formu</b></td><td>Üniversitenin kendi sistemi</td><td>Her üniversite ayrı form ister</td></tr>
    <tr><td><b>Pasaport fotokopisi</b></td><td>Fotoğraflı sayfa</td><td>Pasaportun geçerlilik süresi eğitim süresini kapsamalı</td></tr>
    <tr><td><b>Diploma</b></td><td>Apostilli</td><td>Mezun değilseniz öğrenci belgesi ile ön başvuru yapılabilir</td></tr>
    <tr><td><b>Transkript</b></td><td>İngilizce veya yeminli tercüme</td><td>Lise ya da lisans not dökümü</td></tr>
    <tr><td><b>İngilizce özgeçmiş</b></td><td>Tercihen Europass, fotoğraflı</td><td>Yüksek lisansta ağırlığı artar</td></tr>
    <tr><td><b>Banka hesap dökümü</b></td><td>Son 6 ay, veli/sponsor hesabı</td><td><b>Başvuru için zorunlu değil.</b> Vize aşamasında gerekir; eğitiminizi başkası finanse ediyorsa sponsor mektubu ekleyin</td></tr>
    <tr><td><b>Dil belgesi</b></td><td>IELTS veya eşdeğeri</td><td>Çoğu zaman <b>istenmez</b>: üniversitelerin çoğu kendi mülakatını yapar</td></tr>
  </tbody>
</table>
</div>

<h3>Dil yeterliliği</h3>
<p>Kataloğumuzdaki neredeyse her program İngilizce yürür, dolayısıyla dil bu başvurunun temel
konusu. Ancak burada adayların çoğunun bilmediği bir kolaylık var: <b>Macaristan'da üniversitelerin
büyük bölümü dil belgesi istemez</b>, bunun yerine kendi mülakatını ya da çevrim içi sınavını
yapar. Belge isteyen okullarda ise üniversiteye ve bölüme göre IELTS 5, 6 veya 6,5 aranır.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Seviyeye göre beklenen dil yeterliliği</caption>
  <thead><tr><th>Seviye</th><th>Beklenen</th><th>Belgesi olmayanlar için</th></tr></thead>
  <tbody>
    <tr><td><b>Lisans</b></td><td class="num">Pratikte B2 · istenirse IELTS 5, 6 veya 6,5</td><td>İngilizce Dil Hazırlık programı</td></tr>
    <tr><td><b>Yüksek lisans</b></td><td class="num">İstenirse IELTS 6,5 veya eşdeğeri</td><td>Hazırlık + yeniden başvuru</td></tr>
    <tr><td><b>Hazırlık</b></td><td>Üniversitenin kendi seviye tespit sınavı</td><td>Belge şartı yok</td></tr>
  </tbody>
</table>
</div>

<h2 id="sinav">Giriş sınavı ve mülakat</h2>
{figure('metu-derslik',
        'Amfi dersliğinde dizüstü bilgisayar başında çalışan öğrenciler',
        'Değerlendirme, tek bir sınav gününe değil lise notlarınıza ve alan sınavına bakar.',
        1280, 720)}
<p>YKS puanınız istenmez; bunun yerine üniversite sizi kendi ölçütleriyle değerlendirir. Bu çoğu
aday için avantaj: tek bir sınav gününe değil, lise notlarınıza ve alanla ilgili bir değerlendirmeye
bakılır. Hazırlık süreleri de kısa. Alan bazında beklenenler:</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Alana göre giriş değerlendirmesi</caption>
  <thead><tr><th>Alan</th><th>Değerlendirme</th><th>Hazırlık süresi</th></tr></thead>
  <tbody>
    <tr><td><b>Tıp, diş hekimliği, eczacılık</b></td><td>Kimya ve biyoloji sınavı, sözlü ya da yazılı</td><td>6–10 hafta</td></tr>
    <tr><td><b>Mühendislik</b></td><td>Çevrim içi fizik ve matematik sınavı</td><td>4–6 hafta</td></tr>
    <tr><td><b>Mimarlık</b></td><td>Fizik, matematik ve portfolyo</td><td>8–12 hafta</td></tr>
    <tr><td><b>Film, tasarım, sanat</b></td><td>Portfolyo ve/veya film sunumu</td><td>Portfolyo birikimine bağlı</td></tr>
    <tr><td><b>İşletme, sosyal bilimler</b></td><td>Yazılı test ve/veya mülakat uygulanabilir</td><td>2–4 hafta</td></tr>
  </tbody>
</table>
</div>
<p>Sınava hazırlığı yalnız yürütmüyorsunuz: hangi konuların çıktığını, geçmiş adayların nerede
zorlandığını ve kaç haftaya ihtiyacınız olduğunu danışmanınız baştan söyler.</p>
<p>Sınava hazırlığı yalnız yürütmüyorsunuz: hangi konuların çıktığını, geçmiş adayların nerede
zorlandığını ve kaç haftaya ihtiyacınız olduğunu danışmanınız baştan söyler.</p>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Hazırlık süreleri Hun Education danışmanlarının başvuru dosyalarından edindiği saha gözlemidir,
üniversitelerin resmî tavsiyesi değildir. Kabul kararı her zaman üniversiteye aittir.</p>

<h2 id="takvim">Başvuru takvimi ve süreç</h2>
{strip('Kampüslerden kareler', [
 ('debrecen-cam-bina', 'Debrecen Üniversitesi’nin cam cepheli modern binası',
  'Debrecen Üniversitesi.'),
 ('szeged-ana-bina', 'Szeged Üniversitesi’nin sarı cepheli ana binası',
  'Szeged Üniversitesi.'),
 ('obuda-sari-bina', 'Óbuda Üniversitesi’nin sarı cepheli tarihi binası',
  'Óbuda Üniversitesi, Budapeşte.'),
 ('metu-bina-tabela', '“Budapesti Metropolitan Egyetem” yazılı yuvarlak kampüs binası',
  'Budapeşte Metropolitan.'),
])}
<p>Macaristan'da yılda iki başlangıç dönemi bulunur; yani bir dönemi kaçırsanız bile altı ay sonra
yeniden başlayabiliyorsunuz. Yine de erken başvurmanızı öneriyoruz, çünkü kontenjan dolduğunda dönem
ilan edilen tarihten önce kapanabilir. Erken başvuran aday hem daha geniş bir program listesinden
seçer hem de vize takvimini rahat rahat planlar.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Dönemlere göre başvuru penceresi</caption>
  <thead><tr><th>Dönem</th><th>Eğitim başlangıcı</th><th>Son başvuru</th><th>Dosyayı hazırlamaya başlama</th></tr></thead>
  <tbody>
    <tr><td><b>Güz</b></td><td class="num">Eylül</td><td class="num">Nisan – Haziran (bazı okullar Temmuz sonuna kadar)</td><td class="num">Ocak – Şubat</td></tr>
    <tr><td><b>Bahar</b></td><td class="num">Şubat</td><td class="num">Ekim sonu – Kasım</td><td class="num">Ağustos – Eylül</td></tr>
  </tbody>
</table>
</div>

<h3>Adım adım süreç</h3>
<ol class="steps">
  <li><div><h3>Dosya incelemesi</h3><p>Belgeleriniz ve akademik geçmişiniz değerlendirilir, hangi programlara gerçekçi şansınız olduğu belirlenir.</p></div></li>
  <li><div><h3>Ön Kabul Mektubu</h3><p>Başvuru üniversiteye iletilir ve olumlu değerlendirme sonrası Ön Kabul Mektubu düzenlenir.</p></div></li>
  <li><div><h3>Ödeme ve kayıt</h3><p>Üniversitenin talep ettiği ödeme yapılır; dekont başvuru dosyasına eklenir.</p></div></li>
  <li><div><h3>Nihai Kabul Mektubu</h3><p>Resmî beyan niteliğindeki Kabul Mektubu e-posta ile iletilir. Vize başvurusunun temel belgesidir.</p></div></li>
  <li><div><h3>Vize başvurusu</h3><p>Kabul Mektubuyla en yakın Macaristan Konsolosluğuna başvurulur. Karar tamamen konsolosluğa aittir.</p></div></li>
  <li><div><h3>Seyahat ve karşılama</h3><p>Vize sonrası uçuş, konaklama ve karşılama planlanır. Budapeşte ekibimiz sizi havalimanında karşılar, yurda yerleştirir ve ilk alışverişe kadar yanınızda olur.</p></div></li>
</ol>
<p>Altı adımın tamamında yanınızdayız. Dosyayı biz kuruyoruz, sınav hazırlığını birlikte
planlıyoruz, konsolosluk randevusunu takip ediyoruz ve Macaristan'a vardığınızda sizi ekibimiz
karşılar.</p>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><b>Apostili sona bırakmak.</b> En sık kaybedilen zaman burada. Apostil çeviriden önce alınmalıdır.</li>
  <li><b>Banka dökümünü başvuru anında hazırlamamak.</b> Son 6 ayı kapsaması gerektiği için geriye dönük düzeltilemez.</li>
  <li><b>Tek üniversiteye başvurmak.</b> Kontenjanlar dönem içinde kapanabildiği için birden fazla seçenekle ilerlemek riski azaltır.</li>
  <li><b>Mezun olmadan başvurulamayacağını sanmak.</b> Son sınıf öğrencileri öğrenci belgesiyle ön başvuru yapabilir; diploma sonradan tamamlanır.</li>
</ul>

<h2 id="sss">Sık sorulan sorular</h2>
{faq_block(qa_basvuru)}

<section id="kaynak" class="sources">
  <h2>Kaynaklar ve doğrulama</h2>
  <ol>
    <li>Belge, dil şartı, giriş sınavı ve takvim bilgileri danışmanlık ekibimiz tarafından üniversitelerin güncel başvuru koşullarına göre derlenir ve her başvuru dönemi öncesinde gözden geçirilir.</li>
    <li>Hazırlık süreleri, danışmanlarımızın yürüttüğü başvuru dosyalarından edinilmiş saha gözlemidir; üniversitelerin resmî tavsiyesi değildir.</li>
    <li>Kabul kararı üniversiteye, vize kararı ilgili konsolosluğa aittir. Nihai koşullar için üniversitenin resmî başvuru sayfasını esas alınız.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Başvurunuza bugün başlayalım", "Hangi belgeye ihtiyacınız olduğunu ve hangi programlara gerçekçi şansınız olduğunu ilk görüşmede söyleriz. Görüşme ücretsiz ve sizi hiçbir şeye bağlamaz.")}

{related([(S['costs'],"Maliyet","Eğitim ve yaşam maliyetleri","Öğrenim ücretleri, konaklama ve tek seferlik harçlar."),
          (S['progs'],"Katalog","Programları filtreleyin","490 program; seviye, alan, şehir ve bütçeye göre."),
          (S['unis'],"Üniversite","20 üniversite","Şehir, tür ve öne çıkan alanlarıyla karşılaştırın.")])}
</article>
</div>'''

write(S['apply'], page(
    S['apply'],
    'Macaristan Üniversite Başvuru Şartları (2026) | Hun Education',
    "Macaristan üniversite başvurusu: yaş sınırı, kabul edilen uyruklar, mali yeterlilik, belgeler, "
    "dil şartı ve giriş sınavları. Süreç adım adım.",
    'Başvuru rehberi',
    'Macaristan üniversite başvuru şartları',
    'Hangi belgeler istenir, dil şartı ne, hangi bölümde giriş sınavı var ve son başvuru ne zaman? '
    'Süreci baştan sona, koşullarıyla birlikte anlatıyoruz.',
    body_basvuru, S['apply'],
    [HOME, ('Başvuru Şartları', url_of('apply'))],
    qa_basvuru,
    howto=('Macaristan’da üniversiteye nasıl başvurulur?', 'Dosya incelemesinden vizeye ve Budapeşte’ye varışa kadar altı adımlık başvuru süreci.', [('Dosya incelemesi', 'Belgeleriniz ve akademik geçmişiniz değerlendirilir, hangi programlara gerçekçi şansınız olduğu belirlenir.'), ('Ön Kabul Mektubu', 'Başvuru üniversiteye iletilir ve olumlu değerlendirme sonrası Ön Kabul Mektubu düzenlenir.'), ('Ödeme ve kayıt', 'Üniversitenin talep ettiği ödeme yapılır; dekont başvuru dosyasına eklenir.'), ('Nihai Kabul Mektubu', 'Resmî beyan niteliğindeki Kabul Mektubu e-posta ile iletilir. Vize başvurusunun temel belgesidir.'), ('Vize başvurusu', 'Kabul Mektubuyla en yakın Macaristan Konsolosluğuna başvurulur. Karar tamamen konsolosluğa aittir.'), ('Seyahat ve karşılama', 'Vize sonrası uçuş, konaklama ve karşılama planlanır. Budapeşte ekibimiz havalimanında karşılar ve yurda yerleştirir.')])))

# =====================================================================
# 2) MALİYETLER
# =====================================================================
qa_maliyet = [
    ("Macaristan'da bir yıl okumak toplam ne kadar tutar?",
     "<p>Eğitim ve yaşam giderleri birlikte yıllık <b>8.500 – 14.000 €</b> aralığındadır. "
     "Bu aralık, öğrenim ücreti ile konaklama tercihine göre değişir: yurtta kalan bir öğrenci alt "
     "sınıra, stüdyo dairede kalan üst sınıra yakın bir bütçeyle karşılaşır.</p>"),
    ("Tıp eğitimi neden diğer bölümlerden pahalı?",
     "<p>Tıp ve diş hekimliği laboratuvar, klinik uygulama ve daha uzun eğitim süresi gerektirdiği için "
     "ücretleri yıllık 15.800 € ile 19.900 $ arasındadır. Lisans programlarının çoğu 3.000 – 5.000 € "
     "aralığındadır.</p>"),
    ("Ücretler dönemlik mi yıllık mı ödenir?",
     "<p>Bu sayfadaki öğrenim ücretleri yıllıktır, pilotaj dâhil. Ödeme takvimi üniversiteye göre "
     "değişir; çoğu kurum dönem başında tahsil eder.</p>"),
    ("Burs imkânı var mı?",
     "<p>Burs olanakları üniversiteye, programa ve akademik yıla göre değişir. Güncel burs "
     "koşullarını başvuru öncesinde ilgili üniversitenin resmî sayfasından teyit etmek gerekir; "
     "danışmanınız hangi programlarda başvuru dönemi açık olduğunu paylaşır.</p>"),
]

body_maliyet = f'''<div class="alayout">
{toc([('ogrenim','Öğrenim ücretleri'),('yasam','Yaşam giderleri'),
      ('toplam','Yıllık toplam bütçe'),
      ('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}

<article class="prose">

<section id="giris" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Yurt dışında eğitim planlayan öğrencilerin en çok merak ettiği konuların başında bütçe gelir.
  Macaristan bu açıdan Avrupa'nın en avantajlı ülkelerinden biri olarak öne çıkar. Eğitim ve yaşam
  giderleri birlikte değerlendirildiğinde bir akademik yılın toplam maliyeti
  <b>8.500 – 14.000 €</b> aralığında kalır.</p>

  <p>Öğrenim ücretleri programa göre değişir. Lisans programlarında yıllık 3.000 – 5.000 €, <a class="link" href="{S['masters']}">yüksek lisansta</a> 4.000 – 6.000 €, <a class="link" href="{S['medicine']}">tıp</a> ve diş hekimliğinde ise 15.800 € ile 19.900 $ arasında bir tutar söz
  konusu. Bunlara aylık 60 – 550 € arasında konaklama gideri ve yaklaşık 300 € tutarında günlük yaşam
  gideri eklenir.</p>

  <p><b>Hun Education olarak,</b> öğrencilerimiz için gerçekçi bir bütçe planı çıkarıyoruz. Program,
  şehir ve konaklama tercihine göre her kalemi tek tek hesaplıyor; ödeme takvimini başvurudan önce
  netleştiriyoruz.</p>
</section>

<h2 id="ogrenim">Öğrenim ücretleri</h2>
{strip('Ücretlerin değiştiği üniversitelerden kareler', [
 ('semmelweis-modern-bina', 'Semmelweis Üniversitesi’nin akşam ışıklandırılmış modern binası',
  'Semmelweis Üniversitesi, Budapeşte.'),
 ('debrecen-kuleli-bina', 'Debrecen Üniversitesi’nin kuleli binası',
  'Debrecen Üniversitesi.'),
 ('corvinus-bina', 'Corvinus Üniversitesi’nin modern cam ve taş cepheli binası',
  'Corvinus Üniversitesi.'),
 ('miskolc-cam-bina', 'Miskolc Üniversitesi’nin cam cepheli binası ve önündeki meydan',
  'Miskolc Üniversitesi.'),
 ('elte-tarihi-bina', 'ELTE’nin tarihi taş cepheli binası',
  'ELTE, Budapeşte.'),
])}
<p>Macaristan'ın en güçlü tarafı hiç şüphesiz fiyatı. Aynı bölümü Batı Avrupa'da okumak çoğu zaman
iki katına yakın bir bütçe gerektirir. Aşağıdaki tablo yıllık öğrenim ücretlerini gösterir;
konaklama ve yaşam giderleri bu rakamlara dahil değil.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Seviye ve alana göre yıllık öğrenim ücreti (€)</caption>
  <thead><tr><th>Seviye / alan</th><th>Yıllık ücret</th><th>Süre</th></tr></thead>
  <tbody>
    <tr><td><b>Lisans</b></td><td class="num">3.000 – 5.000 €</td><td>3 – 4 yıl</td></tr>
    <tr><td><b>Yüksek lisans</b></td><td class="num">4.000 – 6.000 €</td><td>2 yıl</td></tr>
    <tr><td><b>Doktora</b></td><td class="num">6.000 – 8.000 €</td><td>3 – 4 yıl</td></tr>
    <tr><td><b>Tıp</b></td><td class="num">15.800 € – 19.900 $</td><td>6 yıl</td></tr>
    <tr><td><b>Diş hekimliği</b></td><td class="num">18.600 €</td><td>5 yıl</td></tr>
    <tr><td><b>Psikoloji</b></td><td class="num">7.800 – 9.400 €</td><td>3 yıl</td></tr>
    <tr><td><b>Pilotaj</b></td><td class="num">29.500 €</td><td>3,5 yıl</td></tr>
    <tr><td><b>İngilizce hazırlık</b></td><td class="num">yıllık 2.500 €'dan</td><td>1 yıl</td></tr>
  </tbody>
</table>
</div>

<h3>Üniversiteye göre farklar</h3>
<p>Aynı seviyedeki programlar üniversiteye göre de farklılaşır:</p>
<div class="tablewrap">
<table class="dtable">
  <caption>Seçili üniversitelerde yıllık ücret aralığı</caption>
  <thead><tr><th>Üniversite</th><th>Şehir</th><th>Yıllık ücret</th></tr></thead>
  <tbody>
    <tr><td><b>Eötvös Loránd Üniversitesi (ELTE)</b></td><td>Budapeşte</td><td class="num">4.000 – 6.000 €</td></tr>
    <tr><td><b>Debrecen Üniversitesi</b></td><td>Debrecen</td><td class="num">3.500 – 5.500 €</td></tr>
    <tr><td><b>Pécs Üniversitesi (PTE)</b></td><td>Pécs</td><td class="num">3.000 – 5.000 €</td></tr>
  </tbody>
</table>
</div>

<h2 id="yasam">Yaşam giderleri</h2>
{figure('szeged-yurt-binasi',
        'Szeged’de bir öğrenci yurdu binası ve önünden geçen yayalar',
        'Yurt, bütçeyi en çok etkileyen tercih.',
        1280, 720)}
<p>Yaşam giderleri tek başına yılda <b>4.000 – 8.000 €</b> tutar. Şehir seçimi burada belirleyicidir:
Budapeşte en yüksek, Szeged, Pécs ve Nyíregyháza gibi şehirler belirgin biçimde daha düşük seyreder.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Aylık yaşam gideri kalemleri</caption>
  <thead><tr><th>Kalem</th><th>Tutar</th><th>Dönem</th><th>Not</th></tr></thead>
  <tbody>
    <tr><td><b>Üniversite yurdu</b></td><td class="num">60 – 400 €</td><td>Aylık</td><td>Kontenjan sınırlı, erken başvuru şart</td></tr>
    <tr><td><b>Kiralık oda</b></td><td class="num">≈ 350 €</td><td>Aylık</td><td>Paylaşımlı daire</td></tr>
    <tr><td><b>Stüdyo daire</b></td><td class="num">≈ 550 €</td><td>Aylık</td><td>Faturalar ayrı olabilir</td></tr>
    <tr><td><b>Market ve faturalar</b></td><td class="num">≈ 300 €</td><td>Aylık</td><td>Ortalama öğrenci harcaması</td></tr>
    <tr><td><b>Toplu taşıma</b></td><td class="num">120 €</td><td>Aylık</td><td>Öğrenci indirimleri değişebilir</td></tr>
    <tr><td><b>Sağlık sigortası</b></td><td class="num">300 €</td><td>Yıllık</td><td>Kayıt için zorunlu</td></tr>
  </tbody>
</table>
</div>

<h3>Tek seferlik ücretler</h3>
<div class="tablewrap">
<table class="dtable">
  <caption>Başvuru ve yerleşim aşamasındaki tek seferlik ödemeler</caption>
  <thead><tr><th>Kalem</th><th>Tutar</th><th>Ne zaman</th></tr></thead>
  <tbody>
    <tr><td><b>Başvuru ücreti</b></td><td class="num">140 €</td><td>Başvuru anında · iade edilmez</td></tr>
    <tr><td><b>Öğrenci vizesi</b></td><td class="num">95 – 145 €</td><td>Kabul mektubu sonrası</td></tr>
    <tr><td><b>Konaklama depozitosu</b></td><td class="num">120 €</td><td>Yerleşim sırasında</td></tr>
  </tbody>
</table>
</div>

<h2 id="toplam">Yıllık toplam bütçe</h2>
{figure('pecs-sehir-hava',
        'Pécs şehir merkezinin kırmızı çatılı havadan görünümü',
        'Pécs: Budapeşte dışında bir üniversite şehri.')}
<p>Kalemleri tek tek toplamak yanıltıcı olur, çünkü konaklama tercihi tek başına yıllık birkaç bin
euroluk fark yaratır. Gerçekçi planlama aralığı şudur:</p>
<div class="answer">
  <span class="answer__label">Yıllık toplam</span>
  <p><b>8.500 – 14.000 €</b>: eğitim ve yaşam giderleri dahil, lisans seviyesi için.
  Tıp ve diş hekimliğinde öğrenim ücreti tek başına 15.800 € ile 19.900 $ arasında olduğu için
  toplam bütçe bu aralığın belirgin şekilde üstündedir.</p>
</div>

<h3>Bütçe planınızı nasıl kuruyoruz</h3>
<p>Bu tablolara bakıp kendi rakamınızı çıkarmakta zorlanabilirsiniz; gayet doğal. Görüşmede dört adımı
birlikte tamamlıyor, size özel bir yıllık bütçe tablosu hazırlıyoruz.</p>
<ol class="steps">
  <li><div><h3>Program ve şehri sabitleyin</h3><p>Öğrenim ücreti ile kira birlikte değişir; ikisini ayrı ayrı değil aynı anda planlıyoruz.</p></div></li>
  <li><div><h3>Konaklama senaryosunu seçin</h3><p>Yurt, paylaşımlı oda ve stüdyo daire arasındaki fark yıllık bütçenin en büyük değişkeni olur.</p></div></li>
  <li><div><h3>İlk yılın tek seferlik ücretlerini ekleyin</h3><p>Başvuru, vize ve depozito yalnızca ilk yıl karşınıza çıkar ama nakit ihtiyacını öne çeker.</p></div></li>
  <li><div><h3>Kur riskini hesaba katın</h3><p>Ücretler euro ve dolar cinsinden; ödeme takvimi boyunca kur hareketi bütçenizi etkileyebilir.</p></div></li>
</ol>

<h2 id="sss">Sık sorulan sorular</h2>
{faq_block(qa_maliyet)}

<section id="kaynak" class="sources">
  <h2>Kaynaklar ve doğrulama</h2>
  <ol>
    <li>Öğrenim ücretleri üniversitelerin ilan ettiği güncel tarifelerden, yaşam giderleri ise Macaristan'da okuyan öğrencilerimizin gerçek harcama verilerinden derlenir.</li>
    <li>Tutarlar her akademik yıl başında danışmanlık ekibimiz tarafından yeniden doğrulanır.</li>
    <li>Ücretler üniversiteler tarafından değiştirilebilir. Nihai tutar için üniversitenin resmî sayfası esastır.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Bütçenize uyan programı bulalım", "Seçtiğiniz program, şehir ve konaklama tercihine göre gerçekçi bir yıllık bütçe tablosunu ilk görüşmede önünüze koyalım. Görüşme ücretsiz.")}

{related([(S['apply'],"Başvuru","Başvuru şartları","Belgeler, dil şartı, giriş sınavı ve takvim."),
          (S['progs'],"Katalog","Bütçeye göre program","Yıllık bütçe filtresiyle listeyi daraltın."),
          (S['edu'],"Rehber","Macaristan'da eğitim","Sistem, şehirler, vize ve denklik.")])}
</article>
</div>'''

write(S['costs'], page(
    S['costs'],
    'Macaristan Üniversite Ücretleri ve Yaşam Maliyetleri (2026) | Hun Education',
    "Macaristan'da lisans, yüksek lisans, tıp ve pilotaj öğrenim ücretleri; konaklama, yaşam gideri, "
    "vize ve sigorta kalemleriyle yıllık toplam bütçe aralığı.",
    'Maliyet rehberi',
    'Macaristan üniversite ücretleri ve yaşam maliyetleri',
    'Öğrenim ücretleri bölüme göre nasıl değişir, aylık yaşam gideri ne kadar ve bir yıl için '
    'gerçekçi toplam bütçe nedir? Kalem kalem açıklıyoruz.',
    body_maliyet, S['costs'],
    [HOME, ('Maliyetler', url_of('costs'))],
    qa_maliyet))
