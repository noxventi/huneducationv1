# -*- coding: utf-8 -*-
# Canlida yayinda olan son iki sayfa cifti (3/3).

# =====================================================================
# YAŞAM  ->  /macaristanda-yasam-ve-universite-egitimi-bilinmesi-gerekenler/
# =====================================================================
qa_yasam = [
    ("Ayda ne kadar paraya ihtiyacım var?",
     "<p>Nerede ve nasıl yaşadığınıza göre aylık yaklaşık <b>480 – 1.000 €</b>. Belirleyici kalem "
     "konaklama: yurt yeri 60 €'ya kadar inebilirken stüdyo daire 550 € civarında. Market ve faturalar "
     "yaklaşık 300 €, ulaşım kartı 120 €.</p>"),
    ("Vardıktan sonra ilk ay ne yapılması gerekir?",
     "<p>İkamet kaydı, üniversite kaydı, banka hesabı ve ulaşım kartı; kabaca bu sırayla. Hiçbiri tek "
     "başına zor değil; zor olan birbirine bağlı olmaları ve süreleri. Budapeşte ekibimiz tam olarak "
     "bunun için var.</p>"),
    ("Yurt mu kiralık daire mi?",
     "<p>Yurt daha ucuz, daha yakın ve daha sosyal; buna karşılık sayısı sınırlı ve çoğu zaman "
     "paylaşımlı ve kontenjan erken dolar. Önerimiz şu: yurda başvurun, kiralık daireyi de yedek "
     "olarak ayarlayın. Budapeşte ekibimiz iki seçeneği de sizin için takip eder.</p>"),
]

body_yasam = f'''<div class="alayout">
{toc([('konaklama','Öğrenciler nerede yaşar?'),
      ('aylik','Bir ay ne kadar tutar?'),('ilkay','İlk ayınız, adım adım'),
      ('sehir','Kampüs dışında hayat'),
      ('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}

<article class="prose">

<section id="kisa-cevap" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Macaristan'da öğrenci olarak yaşamanın aylık maliyeti yaklaşık <b>480 – 1.000 €</b> arasında
  değişir ve bu aralığı belirleyen temel kalem konaklama tercihi olur. Ülkeye vardıktan sonraki
  ilk ay ise akademik olmaktan çok idari geçer; ikamet kaydı, üniversite kaydı, banka hesabı açılışı
  ve ulaşım kartı bu dönemde tamamlanır.</p>

  <p><b>Hun Education olarak,</b> Budapeşte ekibimizle öğrencilerimizi havalimanında karşılıyor ve
  yerleşim sürecinin tamamında yanlarında oluyoruz. Konaklama başvurusundan resmî işlemlere kadar ilk
  ayın her adımını birlikte planlıyoruz.</p>
</section>

<h2 id="konaklama">Öğrenciler nerede yaşar?</h2>
{figure('szeged-yurt-binasi',
        'Szeged’de bir öğrenci yurdu binası ve önünden geçen yayalar',
        'Üniversite yurdu. Aylık 60 €’dan başlıyor.',
        1280, 720)}
<div class="tablewrap">
<table class="dtable">
  <caption>Konaklama seçenekleri karşılaştırması</caption>
  <thead><tr><th>Seçenek</th><th>Aylık</th><th>Kime uygun</th><th>Dikkat</th></tr></thead>
  <tbody>
    <tr><td><b>Üniversite yurdu</b></td><td class="num">60 – 400 €</td><td>İlk yıl, dar bütçe</td><td>Kontenjan sınırlı; kabul gelir gelmez başvurun</td></tr>
    <tr><td><b>Paylaşımlı dairede oda</b></td><td class="num">≈ 350 €</td><td>İkinci yıldan itibaren</td><td>Faturaların dahil olup olmadığını sorun</td></tr>
    <tr><td><b>Stüdyo daire</b></td><td class="num">≈ 550 €</td><td>Çiftler, mahremiyet</td><td>Depozito ve faturalar ayrı</td></tr>
  </tbody>
</table>
</div>
<p>En ucuz ile en pahalı seçenek arasındaki fark yılda birkaç bin euro; <a href="{S['costs']}">maliyet
sayfasında</a> konaklamanın dipnot değil ana bütçe değişkeni olarak ele alınmasının sebebi bu.</p>

<h2 id="aylik">Bir ay ne kadar tutar?</h2>
{figure('obuda-yemekhane',
        'Óbuda Üniversitesi’nin geniş, aydınlık yemekhanesi',
        'Kampüs yemekhanesi.')}
<div class="tablewrap">
<table class="dtable">
  <caption>Tipik aylık giderler</caption>
  <thead><tr><th>Kalem</th><th>Tutar</th><th>Not</th></tr></thead>
  <tbody>
    <tr><td><b>Konaklama</b></td><td class="num">60 – 550 €</td><td>Belirleyici kalem</td></tr>
    <tr><td><b>Market ve faturalar</b></td><td class="num">≈ 300 €</td><td>Ortalama öğrenci harcaması</td></tr>
    <tr><td><b>Ulaşım kartı</b></td><td class="num">120 €</td><td>Öğrenci indirimi şehre göre değişir</td></tr>
    <tr><td><b>Sağlık sigortası</b></td><td class="num">25 €</td><td>Yıllık ≈300 €, kayıt için zorunlu</td></tr>
  </tbody>
</table>
</div>
<p>Şehirler farklı. Budapeşte en pahalısı; Debrecen, Szeged, Pécs ve Nyíregyháza hem kirada hem günlük
giderde belirgin şekilde daha düşük.</p>

<h2 id="ilkay">İlk ayınız, adım adım</h2>
{figure('metu-ogrenci-grubu',
        'Kampüs bahçesinde toplanmış uluslararası öğrenci grubu',
        'Kampüste uluslararası öğrenciler.')}
<ol class="steps">
  <li><div><h3>Varış ve yerleşme</h3><p>Havalimanı karşılama, anahtar teslimi ve ilk alışveriş. Bu bölümü Budapeşte ekibimiz yürütür çünkü emniyet ağı olmayan kısım burası.</p></div></li>
  <li><div><h3>İkamet kaydı</h3><p>Varıştan sonra iznin tanıdığı süre içinde tamamlanır. Kabul mektubu, konaklama kanıtı ve sigorta gerekir.</p></div></li>
  <li><div><h3>Üniversite kaydı</h3><p>Kayıt haftası, öğrenci kartı, ders seçimi ve ders programı.</p></div></li>
  <li><div><h3>Banka hesabı ve ulaşım kartı</h3><p>İkamet kartı ve öğrenci kartı çıktıktan sonra kolay; dördüncü sırada olmasının sebebi bu.</p></div></li>
</ol>

<h2 id="sehir">Kampüs dışında hayat</h2>
{strip('Macaristan’da öğrenci hayatından kareler', [
 ('budapeste-balikci-tabyasi',
  'Balıkçı Tabyası’nın kemerinden gün doğumunda Budapeşte manzarası',
  'Balıkçı Tabyası, Budapeşte.'),
 ('budapeste-koprude-ogrenciler',
  'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci',
  'Özgürlük Köprüsü’nde öğrencilerimiz.'),
 ('obuda-ogrenciler',
  'Óbuda Üniversitesi tabelası altında bankta oturan öğrenci grubu',
  'Ders arası.'),
 ('pecs-sehir-hava',
  'Pécs şehir merkezinin kırmızı çatılı havadan görünümü',
  'Pécs: yürünebilir bir üniversite şehri.'),
])}
<p>Macaristan'ın üniversite şehirleri kompakt ve yürünebilir; öğrenci hayatı da bunun etrafında
yoğunlaşır. Budapeşte'de yoğunluk ve gece hayatı var; Debrecen ve Szeged'de öğrenci nüfusu şehrin
tonunu belirleyecek kadar büyük; Pécs yürüyerek geçilecek kadar küçük ve merkezinde ülkenin en eski
üniversitesi durur.</p>
<p>Toplu taşıma Avrupa ölçeğinde iyi ve ucuz; şehirlerarası tren Viyana, Bratislava ya da Krakov'a hafta
sonu gitmeyi öğrenci bütçesiyle mümkün kılar.</p>

<h3>Macarca bilmeden idare etmek</h3>
<p>Dersleriniz İngilizce, üniversite idaresi uluslararası öğrenciyi İngilizce karşılıyor ve üniversite
şehirlerinde günlük hayatı Macarcasız yürütebiliyorsunuz. Bunun dışında hızla incelir: belediye ve
göç işlemlerinde, ev sahibiyle ve küçük esnafta Macarca bekleyin.</p>
<p>Çoğu üniversite başlangıç seviyesi Macarcayı ücretsiz ya da ucuza verir. Almaya değer; akıcılık
için değil, ülkenin size verdiği karşılığı değiştirdiği için.</p>

<h2 id="sss">Sık sorulan sorular</h2>
{faq_block(qa_yasam)}

<section id="kaynak" class="sources">
  <h2>Kaynaklar ve doğrulama</h2>
  <ol>
    <li>Yaşam giderleri Macaristan'daki öğrencilerimizin gerçek harcama verisinden derlenir ve her akademik yıl yeniden doğrulanır.</li>
    <li>İkamet ve kayıt şartları Macaristan makamlarınca belirlenir ve değişebilir; güncel kuralları esas alınız.</li>
    <li>Yurt kontenjanı ve fiyatı her üniversitenin kendi kararıdır.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Pratik tarafı mı planlıyorsunuz?", "Konaklama, varış ve ilk ay planların en çok kaydığı yer. Tarihlerinizi konuşalım, işlere bir sıra koyalım.")}

{related([(S['costs'],"Maliyet","Ücretler ve yaşam gideri","Kalem kalem yıllık bütçenin tamamı."),
          (S['stories'],"Öğrenci","Öğrenci görüşleri","Öğrenciler kendi deneyimlerini nasıl anlatır."),
          (S['edu'],"Rehber","Macaristan'da eğitim","Sistem, şehirler ve öğrenci vizesi.")])}
</article>
</div>'''

write(S['life'], page(
    S['life'],
    'Macaristan’da Öğrenci Hayatı: Konaklama, Bütçe, İlk Ay | Hun Education',
    "Macaristan'da öğrenci hayatı: konaklama seçenekleri ve fiyatları, aylık gider, varıştan sonraki "
    "ilk ay yapılacak resmî işlemler ve İngilizcenin nereye kadar yettiği.",
    'Öğrenci hayatı',
    'Macaristan’da yaşam ve üniversite eğitimi',
    'Bir ay gerçekte ne tutar, öğrenciler nerede yaşar ve ilk haftalarda kimsenin uyarmadığı '
    'resmî işlemler neler?',
    body_yasam, S['life'],
    [HOME, ('Macaristan’da Yaşam', url_of('life'))],
    qa_yasam))

# =====================================================================
# ÖĞRENCİ GÖRÜŞLERİ  ->  /macaristan-universiteleri-ogrenci-gorusleri/
# =====================================================================
qa_gorus = [
    ("Bu yorumlar gerçek mi?",
     "<p>Evet. Bu sayfadaki her yorum, başvurusunu birlikte yürüttüğümüz bir öğrenciye ait ve izniyle "
     "yayınlanır. Soyadlar öğrencilerin kendi tercihiyle baş harfle yazılır. Anonim ya da kurgulanmış "
     "referans kullanmıyoruz; gerçek öğrenciyi temsil etmek için stok fotoğraf da kullanmıyoruz.</p>"),
    ("Karar vermeden önce bir öğrenciyle konuşabilir miyim?",
     "<p>Çoğu zaman evet. Programa ve yılın hangi döneminde olduğumuza göre, düşündüğünüz bölümde okuyan "
     "bir öğrenciyle sizi buluşturabiliriz. Ön görüşmede isteyin.</p>"),
]

body_gorus = f'''<div class="alayout">
{toc([('sesler','Kendi cümleleriyle'),
      ('temalar','Tekrar eden başlıklar'),('politika','Referansları nasıl ele alıyoruz'),
      ('sss','Sık sorulan sorular')])}

<article class="prose">

<section id="kisa-cevap" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Bir ülkede eğitim almanın nasıl bir deneyim olduğunu en iyi, orada okuyan öğrenciler anlatır.
  Bu sayfada Budapeşte, Debrecen ve Pécs'te <a class="link" href="{S['medicine']}">tıp</a>, mühendislik, medya ve dil bilimleri okuyan öğrencilerimizin kendi cümleleriyle paylaştığı deneyimleri bulacaksınız.</p>

  <p>Aşağıdaki yorumlar, başvuru süreçlerini birlikte yürüttüğümüz öğrencilere ait. Tamamı
  öğrencilerimizin izniyle ve kendi tercihleri doğrultusunda ad ya da baş harf kullanılarak
  yayımlanır.</p>
</section>

<h2 id="sesler">Kendi cümleleriyle</h2>
{strip('Öğrencilerimizden kareler', [
 ('metu-ogrenci-grubu', 'Kampüs bahçesinde toplanmış uluslararası öğrenci grubu',
  'Kampüste uluslararası öğrenciler.'),
 ('pilotaj-ogrenciler-pist', 'Pilot gömlekli üç öğrenci, uçuş alanında birlikte',
  'Pilotaj öğrencilerimiz uçuş alanında.'),
 ('budapeste-koprude-ogrenciler', 'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci',
  'Budapeşte’de bir hafta sonu.'),
 ('metu-ogrenci-portre', 'Kampüs koridorunda, cam cephenin önünde duran bir öğrenci',
  'Budapeşte Metropolitan kampüsü.'),
])}
<div class="stories__row">
  <figure class="quote">
    <span class="quote__mark" aria-hidden="true">&rdquo;</span>
    <blockquote><p>Tüm işlemlerimde Hun Education danışmanları çok yardımcı oldu. Budapeşte Metropolitan
    Üniversitesi Film ve Medya'yı bitirdim. Eğitimim ve stajım sonrasında Disney, Marvel, Netflix ve
    Paramount gibi yapım şirketlerinde çalıştım. Şimdi Budapeşte'de, büyük bir film yapımında Visual
    Effects departmanında çalışıyorum.</p></blockquote>
    <figcaption class="quote__who"><b>Baturay E.</b><span>Budapeşte Metropolitan Üniversitesi</span>
    <span class="num-mono">Media and Film</span></figcaption>
  </figure>

  <figure class="quote quote--accent">
    <span class="quote__mark" aria-hidden="true">&rdquo;</span>
    <blockquote><p>Hun Education ile ilk olarak 2017-2018 akademik yılında McDaniel College'da Almanca
    Tıp Öncesi eğitimi aldım ve ardından Eylül 2018'de Semmelweis Üniversitesi'ne yerleştim. Haziran 2022
    itibarıyla 4. yıl bitmek üzere; Budapeşte'de ve böyle kaliteli bir okulda eğitim gördüğüm için
    kendimi şanslı hissediyorum.</p></blockquote>
    <figcaption class="quote__who"><b>Işıl A.</b><span>Semmelweis Üniversitesi</span>
    <span class="num-mono">Tıp</span></figcaption>
  </figure>

  <figure class="quote">
    <span class="quote__mark" aria-hidden="true">&rdquo;</span>
    <blockquote><p>2008 Eylül ayında Hun Education ile Debrecen'e geldim. Elektrik Mühendisliği
    programını Debrecen'de bitirdikten sonra yüksek lisansımı (mekatronik) ve doktoramı Óbuda
    Üniversitesi'nde tamamladım. Daha sonra Óbuda Üniversitesi'nde akademisyen olarak çalıştım. Şu an
    Macaristan Samsung'da çalışıyorum.</p></blockquote>
    <figcaption class="quote__who"><b>Sinan K.</b><span>Debrecen Üniversitesi</span>
    <span class="num-mono">Elektrik Mühendisliği</span></figcaption>
  </figure>
</div>

<div class="tablewrap">
<table class="dtable">
  <caption>Diğer yazılı deneyimler</caption>
  <thead><tr><th>Öğrenci</th><th>Üniversite</th><th>Program</th></tr></thead>
  <tbody>
    <tr><td><b>Sude A.</b></td><td>Pécs Üniversitesi</td><td>Hazırlık, ardından Tıp</td></tr>
    <tr><td><b>Özlem D.</b></td><td>Pécs Üniversitesi</td><td>İngiliz Dili YL; şu an Szeged'de doktora ve Pécs temsilcimiz</td></tr>
    <tr><td><b>Sude</b></td><td>Pécs Üniversitesi</td><td>Hemşirelik, 1. sınıf</td></tr>
  </tbody>
</table>
</div>

<h2 id="temalar">Tekrar eden başlıklar</h2>
{figure('metu-derslik',
        'Amfi dersliğinde dizüstü bilgisayar başında çalışan öğrenciler',
        'Dersler İngilizce; sınıflar uluslararası.',
        1280, 720)}
<p>Anlatılara topluca bakınca aynı dört şey öne çıkar. Bunları bilmek işinize yarar, çünkü
öğrencilerin gerçekten zorlandığı ya da iyi bulduğu noktalar bunlar.</p>
<ul>
  <li><b>Ağır olan ilk yıl.</b> Özellikle tıpta temel bilim yılları sınav yükünü ve öğrenci kaybını
  taşır.</li>
  <li><b>İdari ilk ay beklenenden çok önemli.</b> İkamet kaydı ve üniversite kaydı, öğrencilerin
  “yalnız olmadığıma sevindim” dediği aşama.</li>
  <li><b>Şehir seçimi üniversite kadar belirleyici.</b> Budapeşte ile Pécs aynı öğrenci yılının belirgin
  biçimde farklı anlatılarını üretir.</li>
  <li><b>Mezuniyet sonrası istihdam gerçek ama otomatik değil.</b> Macaristan'da mesleki olarak kalan
  öğrenciler uluslararası şirketlerde ve İngilizce çalışılan ortamlarda.</li>
</ul>

<h2 id="politika">Referansları nasıl ele alıyoruz</h2>
<p>Referans sayfaları kolayca güvenilmez hâle geliyor, o yüzden kurallarımızı açıkça yazıyoruz.</p>
<ul>
  <li>Her yorum, başvurusunu yürüttüğümüz bir öğrenciye ait.</li>
  <li>Hiçbir şey öğrencinin izni olmadan yayınlanmaz ve izin geri alınabilir.</li>
  <li>İsimler öğrencinin tercihine göre yazılır; bu genellikle ad ve soyadın baş harfidir.</li>
  <li>Gerçek öğrenciyi temsil etmek için stok fotoğraf kullanılmaz. Fotoğraf yoksa fotoğraf yoktur.</li>
  <li>Kabul oranı, başarı yüzdesi veya memnuniyet puanı yayınlamıyoruz; çünkü belgeleyemeyiz.</li>
</ul>

<h2 id="sss">Sık sorulan sorular</h2>
{faq_block(qa_gorus)}

{acta("Bir öğrenciden dinlemek ister misiniz?", "Programınıza göre çoğu zaman o bölümde okuyan biriyle sizi buluşturabiliyoruz. Ön görüşmede isteyin.")}

{related([(S['life'],"Yaşam","Macaristan'da yaşam","Konaklama, aylık gider ve ilk ay."),
          (S['progs'],"Katalog","Program kataloğu","490 programı filtreleyerek karşılaştırın."),
          (S['about'],"Kurumsal","Hakkımızda","Nasıl çalışıyoruz ve neyi vaat etmiyoruz.")])}
</article>
</div>'''

write(S['stories'], page(
    S['stories'],
    'Macaristan Üniversiteleri Öğrenci Görüşleri | Hun Education',
    "Başvurusunu birlikte yürüttüğümüz öğrencilerin izinli yorumları: Budapeşte, Debrecen ve Pécs'te "
    "tıp, mühendislik, medya ve dil bilimleri.",
    'Öğrenci görüşleri',
    'Macaristan üniversiteleri öğrenci görüşleri',
    'Başvurusunu birlikte yürüttüğümüz öğrencilerin, izinleriyle ve kendi cümleleriyle paylaştıkları '
    'deneyimler.',
    body_gorus, S['stories'],
    [HOME, ('Öğrenci Görüşleri', url_of('stories'))],
    qa_gorus))
