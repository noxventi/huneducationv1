# -*- coding: utf-8 -*-
"""Neden Macaristan sayfasi: 11 bolumden 5'e, Turkce yeniden yazim.

Akademik gecmis, Turkiye bagi ve Ingilizce egitim tek bolumde birlesti;
konum ile ogrenci hayati tek bolumde birlesti. Anlatim canlidaki gibi
akici cumlelerle ve "Hun Education olarak" sesiyle kuruldu.
"""
import io

p = 'tools/pages_content5.py'
s = io.open(p, encoding='utf-8').read()

BAS = "body_neden = f'''"
SON = '<h2 id="sss">Sık sorulan sorular</h2>'
i, j = s.index(BAS), s.index(SON)

YENI = BAS + '''<div class="alayout">
{toc([('rakamlar','Rakamlarla Macaristan'),
      ('neden','Macaristan neden öne çıkıyor?'),
      ('maliyet','Eğitim ve yaşam maliyetleri'),
      ('hayat',"Avrupa'nın ortasında bir öğrencilik"),
      ('gorusme','Başvurudan önce konuştuklarımız'),
      ('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}

<article class="prose">

<section id="giris" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Yurt dışında okumaya karar veren öğrencilerin önündeki en büyük soru genellikle şu oluyor: kaliteli
  bir eğitimi makul bir bütçeyle nerede alabilirim? Macaristan son yıllarda bu sorunun en güçlü
  cevaplarından biri hâline geldi. Eğitim baştan sona İngilizce yürüyor, YKS puanı istenmiyor ve bir
  akademik yılın toplam maliyeti Batı Avrupa'da ödeyeceğinizin yaklaşık yarısı kadar. <b>Hun Education
  olarak</b> 1999'dan bu yana yalnızca bu ülkeye odaklandık; kataloğumuzda 20 üniversitede
  <b>490 İngilizce program</b> bulunuyor.</p>
</section>

<h2 id="rakamlar">Rakamlarla Macaristan</h2>
{stats([('1367', "Pécs Üniversitesi'nin kuruluş yılı"),
        ('40.000', "Macaristan'daki uluslararası öğrenci"),
        ('490', 'Başvurabileceğiniz İngilizce program'),
        ('1999', "Hun Education'ın ilk yılı")])}

<h2 id="neden">Macaristan neden öne çıkıyor?</h2>
<p>Macaristan üniversiteleri yeni kurulmuş kurumlar değil. Pécs Üniversitesi 1367'de kuruldu,
Semmelweis'te tıp eğitimi 1769'a dayanıyor ve Budapeşte Teknoloji ve Ekonomi Üniversitesi dünyanın en
eski teknik üniversiteleri arasında sayılıyor. Bu köklü gelenek bilimde de karşılığını buldu: Macar
asıllı bilim insanları bugüne kadar 16 Nobel Ödülü kazandı, Szent-Györgyi Albert 1937'de C vitamini
üzerine yaptığı çalışmayla ödüle layık görüldü. Tükenmez kalem de Rubik küpü de bu ülkeden çıktı.</p>

<p>Sizin açınızdan tarihten daha önemlisi ise şu: bu fakülteler uluslararası öğrenciyle çalışmaya
alışkın. Tıp, diş hekimliği ve mühendislikte İngilizce programlar onlarca yıldır yürütülüyor; dersler,
sınavlar ve idari süreçlerin tamamı Macarca bilmeden gelen öğrenciye göre kurulmuş durumda. Yani yolu
ilk açan siz olmayacaksınız.</p>

<p>Türk öğrencilerin Macaristan'da okuması da yeni bir eğilim değil. Osmanlı'nın son döneminden
Cumhuriyet'in ilk yıllarına uzanan bir geçmiş var ve bugün ülkede her yıl büyüyen bir Türk öğrenci
topluluğu bulunuyor. Macaristan genelinde 40 bine yakın uluslararası öğrenci okuyor; gittiğinizde
sizden önce gelmiş, aynı yollardan geçmiş arkadaşlar buluyorsunuz.</p>

<p>Dil konusunda ise kafanızın rahat olmasını isteriz. Kataloğumuzdaki her program hazırlık yılından
yüksek lisansa kadar İngilizce yürüyor ve üniversitelerin çoğu dil belgesi bile istemiyor, kendi
mülakatını ya da çevrim içi sınavını yapıyor. Belge isteyen okullarda IELTS 5, 6 veya 6,5 görülüyor.
Seviyeniz henüz yeterli değilse endişelenmeyin; üniversitenin kendi İngilizce hazırlık yılından girip
programa oradan geçebiliyorsunuz.</p>

<h2 id="maliyet">Eğitim ve yaşam maliyetleri</h2>
<p>Macaristan'ı öne çıkaran en somut sebep bütçe. Aşağıdaki rakamlar lisans seviyesinde, yaşam
giderleri dahil, tam ücret ödeyen bir uluslararası öğrencinin yıllık toplam bütçesini gösteriyor. Aynı
diplomayı Batı Avrupa'da almak çoğu durumda bunun iki katına yakın bir bütçe gerektiriyor.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Macaristan'da lisans seviyesinde yıllık bütçe</caption>
  <thead><tr><th>Kalem</th><th>Tutar</th></tr></thead>
  <tbody>
    <tr><td><b>Öğrenim ücreti</b></td><td class="num">3.000 – 5.000 €</td></tr>
    <tr><td><b>Yaşam giderleri</b></td><td class="num">4.000 – 8.000 €</td></tr>
    <tr><td><b>Yıllık toplam</b></td><td class="num">8.500 – 14.000 €</td></tr>
  </tbody>
</table>
</div>
<p>Aralığın alt ucu, Budapeşte dışında okuyan ve yurtta kalan bir öğrenciye karşılık geliyor; üst ucu
ise başkentte stüdyo dairede yaşayan bir öğrenciye. Yani bütçenizi büyük ölçüde kendi tercihleriniz
belirliyor. Bu rakamları üniversite tarifelerinden ve öğrencilerimizin gerçek harcamalarından
derliyor, her akademik yıl yeniden doğruluyoruz.</p>

{inline_cta("Bütçenizi paylaşın, hangi programlara girebileceğinizi ilk görüşmede söyleyelim.")}

<h2 id="hayat">Avrupa'nın ortasında bir öğrencilik</h2>
<p>Macaristan'da okumak yalnızca bir diploma almak anlamına gelmiyor. Budapeşte'den Viyana,
Bratislava, Zagreb ve Belgrad kara ya da tren yoluyla birkaç saat uzaklıkta; çoğu Avrupa başkentine
kısa bir uçuşla varıyorsunuz. Ülke AB ve Schengen üyesi olduğu için öğrenci ikametinizle bölgede
seyahat etmek son derece kolay. Uzun yaz tatilleri ve öğrenci bütçesine uygun tren bağlantıları,
diploma yıllarınızı aynı zamanda bir Avrupa deneyimine dönüştürüyor.</p>

<p>Şehirlerin kendisi de bu deneyimin bir parçası. Buda Kalesi ve Tuna kıyısı UNESCO listesinde yer
alıyor, Sziget her yaz Budapeşte'de Avrupa'nın en büyük müzik festivallerinden biri olarak
düzenleniyor ve Balaton Gölü yaz aylarında öğrencilerin buluşma noktasına dönüşüyor. Günlük hayata
gelirsek, bir öğrencinin yılı kabaca şöyle geçiyor:</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Bir öğrenci yılının pratik dokusu</caption>
  <thead><tr><th>Başlık</th><th>Ne bekleyin</th></tr></thead>
  <tbody>
    <tr><td><b>Konaklama</b></td><td>Üniversite yurdu aylık 60 €'dan başlar; paylaşımlı dairede oda ≈350 €; stüdyo ≈550 €</td></tr>
    <tr><td><b>Ulaşım</b></td><td>Budapeşte'de yoğun metro, tramvay ve otobüs ağı; öğrenci kartı aylık ≈120 €</td></tr>
    <tr><td><b>Sağlık</b></td><td>Sağlık sigortası kayıt için zorunlu, yıllık ≈300 €</td></tr>
    <tr><td><b>Topluluk</b></td><td>Budapeşte, Debrecen ve Pécs'te kalabalık uluslararası öğrenci nüfusu</td></tr>
  </tbody>
</table>
</div>

<h2 id="gorusme">Başvurudan önce konuştuklarımız</h2>
<p>Kararınızı sağlam vermeniz için dört konuyu başvuru öncesinde birlikte netleştiriyoruz. Hiçbiri
engel değil; sadece doğru sırayla ele alındığında sonradan sürpriz çıkarmayan başlıklar.</p>
<ul>
  <li><b>Mezuniyetten sonra Macaristan'da kalmayı düşünüyorsanız</b> Macarcaya diploma sürecinde
  başlamak işinizi çok kolaylaştırıyor. Uluslararası şirketlerde İngilizce yeterli oluyor ama yerel iş
  piyasasında dil fark yaratıyor. Üniversitelerin çoğu başlangıç seviyesi Macarcayı ücretsiz veriyor.</li>
  <li><b>Alanınız düzenlenmiş bir meslekse</b> (tıp, diş hekimliği, eczacılık, mimarlık, hukuk)
  mezuniyet sonrası denklik yolunu daha program seçerken birlikte kontrol ediyoruz.</li>
  <li><b>Bütçenizi</b> burs beklentisi üzerine değil, ücretlerin kendisi üzerine kuruyoruz.
  Macaristan'ın avantajı zaten fiyatın kendisinde; burs çıkarsa ek kazanç oluyor.</li>
  <li><b>Şehir tercihinizi</b> program listesiyle birlikte yapıyoruz. Budapeşte en kalabalık seçenek
  ama Debrecen, Szeged ve Pécs hem güçlü programlar hem belirgin şekilde düşük yaşam maliyeti
  sunuyor.</li>
</ul>

'''

io.open(p, 'w', encoding='utf-8').write(s[:i] + YENI + s[j:])
print('neden sayfasi yeniden yazildi')
