# -*- coding: utf-8 -*-
# Yasal sayfalar. Kaynak sitede bu metinler yayınlanmadığı için içerik,
# şirketin doğrulanmış bilgileri + BU sitenin fiilî veri işlemleri
# (form alanları, UTM/localStorage, WhatsApp yönlendirmesi) üzerine yazıldı.
# Yayın öncesi hukuk danışmanı onayı gerekir (README'de işaretli).

# legal_page(), LEGAL_BYLINE ve HOME artik gen_pages.py tarafindan
# dile gore uretiliyor; burada yalnizca icerik kaliyor.

# =====================================================================
# 1) KVKK AYDINLATMA METNİ
# =====================================================================
body_kvkk = f'''<div class="alayout">
{toc([('sorumlu','Veri sorumlusu'),('veriler','İşlenen kişisel veriler'),('amaclar','İşleme amaçları'),
      ('hukuki','Hukuki sebepler'),('yontem','Toplama yöntemi'),('aktarim','Verilerin aktarılması'),
      ('saklama','Saklama süreleri'),('haklar','Haklarınız'),('basvuru','Başvuru yöntemi')])}

<article class="prose">

<p>Bu aydınlatma metni, 6698 sayılı Kişisel Verilerin Korunması Kanunu (“KVKK”) m.10 ve
Avrupa Birliği Genel Veri Koruma Tüzüğü (“GDPR”) m.13 uyarınca, kişisel verilerinizin
hangi amaçla, hangi hukuki sebeple işlendiğini ve haklarınızı açıklamak için hazırlanmıştır.
Şirketimiz Macaristan'da yerleşik olduğundan verileriniz hem KVKK hem GDPR kapsamında korunur.</p>

<h2 id="sorumlu">Veri sorumlusu</h2>
<div class="tablewrap">
<table class="dtable">
  <tbody>
    <tr><td><b>Unvan</b></td><td>HUN EDUCATION KFT.</td></tr>
    <tr><td><b>Adres</b></td><td>1204 Budapest, Bethlen utca 17, Macaristan</td></tr>
    <tr><td><b>E-posta</b></td><td>info@huneducation.com</td></tr>
    <tr><td><b>Telefon</b></td><td class="num">+36 70 296 35 31</td></tr>
  </tbody>
</table>
</div>

<h2 id="veriler">İşlenen kişisel veriler</h2>
<div class="tablewrap">
<table class="dtable">
  <thead><tr><th>Kategori</th><th>Örnekler</th><th>Ne zaman toplanır</th></tr></thead>
  <tbody>
    <tr><td><b>Kimlik</b></td><td>Ad, soyad, doğum tarihi, pasaport bilgileri</td><td>Ön görüşme ve başvuru</td></tr>
    <tr><td><b>İletişim</b></td><td>Telefon, e-posta, adres</td><td>Form gönderimi</td></tr>
    <tr><td><b>Eğitim</b></td><td>Diploma, transkript, dil belgesi, özgeçmiş</td><td>Başvuru dosyası hazırlığı</td></tr>
    <tr><td><b>Finansal</b></td><td>Banka hesap dökümü (yalnız vize dosyası için)</td><td>Vize hazırlığı</td></tr>
    <tr><td><b>Sağlık</b><i> (özel nitelikli)</i></td><td>Sağlık raporu (yalnız pilotaj ve sigorta işlemleri gerektirdiğinde, açık rızayla)</td><td>İlgili başvuru aşaması</td></tr>
    <tr><td><b>İşlem güvenliği</b></td><td>Form gönderim kaydı, sitede ilk geliş kaynağı (UTM)</td><td>Site kullanımı</td></tr>
    <tr><td><b>Görsel/işitsel</b></td><td>Fotoğraf, video (yalnız ayrı yazılı izinle)</td><td>Öğrenci hikâyesi yayını</td></tr>
  </tbody>
</table>
</div>

<h2 id="amaclar">İşleme amaçları</h2>
<ul>
  <li>Ücretsiz ön görüşme talebinizin değerlendirilmesi ve size dönüş yapılması</li>
  <li>Uygun üniversite ve programların belirlenmesi, başvuru dosyanızın hazırlanması ve iletilmesi</li>
  <li>Kabul, kayıt, vize ve konaklama süreçlerinin yürütülmesi ve takibi</li>
  <li>Macaristan'a varış sonrası karşılama, ikamet ve kayıt desteğinin sağlanması</li>
  <li>Yasal yükümlülüklerin yerine getirilmesi ve olası uyuşmazlıklarda ispat</li>
  <li>Açık rızanız olması hâlinde tanıtım ve bilgilendirme iletişimi</li>
</ul>

<h2 id="hukuki">Hukuki sebepler</h2>
<div class="tablewrap">
<table class="dtable">
  <thead><tr><th>Sebep</th><th>Dayanak</th><th>Kapsam</th></tr></thead>
  <tbody>
    <tr><td><b>Sözleşmenin kurulması ve ifası</b></td><td>KVKK m.5/2-c · GDPR m.6/1-b</td><td>Danışmanlık hizmetinin sunulması, başvuru ve vize süreçleri</td></tr>
    <tr><td><b>Hukuki yükümlülük</b></td><td>KVKK m.5/2-ç · GDPR m.6/1-c</td><td>Muhasebe ve mevzuat kayıtları</td></tr>
    <tr><td><b>Meşru menfaat</b></td><td>KVKK m.5/2-f · GDPR m.6/1-f</td><td>Hizmet kalitesi, iletişim kayıtları, dolandırıcılık önleme</td></tr>
    <tr><td><b>Açık rıza</b></td><td>KVKK m.5/1, m.6, m.9 · GDPR m.6/1-a, m.9/2-a</td><td>Sağlık verisi, yurt dışına aktarım, pazarlama iletişimi, fotoğraf/video yayını</td></tr>
  </tbody>
</table>
</div>

<h2 id="yontem">Toplama yöntemi</h2>
<p>Verileriniz; web sitemizdeki formlar, e-posta, telefon, WhatsApp yazışmaları, ofislerimizde
yüz yüze görüşmeler ve tarafınızca iletilen belgeler aracılığıyla, kısmen otomatik ve otomatik
olmayan yollarla toplanır. Sitenin kullandığı depolama teknolojileri
<a href=S['cookies']>Gizlilik ve Çerez Politikası</a>'nda açıklanmıştır.</p>

<h2 id="aktarim">Verilerin aktarılması</h2>
<p>Kişisel verileriniz, yalnız yukarıdaki amaçlar için gerekli olduğu ölçüde şu alıcılara aktarılır:</p>
<ul>
  <li><b>Başvurduğunuz Macaristan üniversiteleri</b>: başvuru dosyanızın iletilmesi</li>
  <li><b>Macaristan konsoloslukları ve resmî makamlar</b>: vize ve ikamet işlemleri</li>
  <li><b>Konaklama sağlayıcıları</b>: yurt/kiralık daire başvurusu, talebiniz hâlinde</li>
  <li><b>Hizmet sağlayıcılarımız</b>: barındırma, e-posta ve CRM altyapısı (veri işleyen sıfatıyla)</li>
</ul>
<p>Türkiye'den Macaristan'a veri aktarımı KVKK m.9 kapsamındadır ve
<a href=S['consent']>Açık Rıza Metni</a> ile onayınıza sunulur. Macaristan AB üyesi
olduğundan aktarılan veriler GDPR güvencesi altındadır.</p>

<h2 id="saklama">Saklama süreleri</h2>
<div class="tablewrap">
<table class="dtable">
  <thead><tr><th>Veri</th><th>Süre</th></tr></thead>
  <tbody>
    <tr><td>Hizmet sözleşmesi ve başvuru dosyası</td><td>Sözleşme ilişkisinin sona ermesinden itibaren ilgili mevzuattaki zamanaşımı süresince</td></tr>
    <tr><td>Sonuçlanmayan ön görüşme talepleri</td><td>Son temastan itibaren en fazla 2 yıl</td></tr>
    <tr><td>Muhasebe kayıtları</td><td>İlgili mevzuatın öngördüğü asgari süre</td></tr>
    <tr><td>Pazarlama izinleri</td><td>Rıza geri alınana kadar</td></tr>
  </tbody>
</table>
</div>
<p>Süresi dolan veriler silinir, yok edilir veya anonim hâle getirilir.</p>

<h2 id="haklar">Haklarınız (KVKK m.11 · GDPR m.15-21)</h2>
<ul>
  <li>Kişisel verinizin işlenip işlenmediğini öğrenme ve buna ilişkin bilgi talep etme</li>
  <li>İşleme amacını ve amacına uygun kullanılıp kullanılmadığını öğrenme</li>
  <li>Yurt içinde veya yurt dışında verilerin aktarıldığı üçüncü kişileri öğrenme</li>
  <li>Eksik veya yanlış işlenmiş verilerin düzeltilmesini isteme</li>
  <li>Silme veya yok edilmesini isteme; bu işlemlerin aktarılan üçüncü kişilere bildirilmesini isteme</li>
  <li>Münhasıran otomatik sistemlerle analiz sonucu aleyhinize çıkan sonuca itiraz etme</li>
  <li>Kanuna aykırı işleme sebebiyle zarara uğramanız hâlinde zararın giderilmesini talep etme</li>
  <li>Verdiğiniz açık rızaları dilediğiniz zaman geri alma</li>
</ul>

<h2 id="basvuru">Başvuru yöntemi</h2>
<p>Haklarınıza ilişkin taleplerinizi <b>info@huneducation.com</b> adresine e-posta ile veya
<b>1204 Budapest, Bethlen utca 17, Macaristan</b> adresine yazılı olarak iletebilirsiniz.
Başvurunuz en geç 30 gün içinde ücretsiz olarak sonuçlandırılır. Ayrıca Türkiye'de Kişisel
Verileri Koruma Kurulu'na, Macaristan'da NAIH'e (Nemzeti Adatvédelmi és Információszabadság
Hatóság) şikâyette bulunma hakkınız saklıdır.</p>

{related([(S['consent'],"Yasal","Açık Rıza Metni","Yurt dışına aktarım, sağlık verisi ve pazarlama izinleri."),
          (S['cookies'],"Yasal","Gizlilik ve Çerez Politikası","Sitenin kullandığı depolama teknolojileri."),
          (S['terms'],"Yasal","Kullanım Koşulları","Hizmetin kapsamı ve sorumluluk sınırları.")])}
</article>
</div>'''

write(S['privacy'], legal_page(
    S['privacy'],
    'KVKK Aydınlatma Metni | Hun Education',
    "HUN EDUCATION KFT.'nin kişisel verileri işleme amaçları, hukuki sebepleri, aktarım ve saklama "
    "koşulları ile KVKK m.11 kapsamındaki haklarınız.",
    'KVKK Aydınlatma Metni',
    'Kişisel verilerinizin hangi amaçla, hangi hukuki sebeple işlendiğini ve haklarınızı bu metinde '
    'açıklıyoruz.',
    body_kvkk, 'KVKK Aydınlatma Metni'))

# =====================================================================
# 2) AÇIK RIZA METNİ
# =====================================================================
body_riza = f'''<div class="alayout">
{toc([('kapsam','Rızanın kapsamı'),('yurtdisi','Yurt dışına aktarım'),('saglik','Sağlık verisi'),
      ('pazarlama','Pazarlama iletişimi'),('gorsel','Fotoğraf ve video'),('geri','Rızanın geri alınması')])}

<article class="prose">

<p>Bu metin, <a href=S['privacy']>KVKK Aydınlatma Metni</a>'nde açıklanan işleme
faaliyetlerinden <b>açık rızaya bağlı olanlar</b> için onayınızı almak amacıyla hazırlanmıştır.
Her rıza kalemi birbirinden bağımsızdır; birine onay vermeniz diğerlerini kapsamaz ve
danışmanlık hizmeti almanız pazarlama iletişimine onay vermenize bağlı değildir.</p>

<h2 id="kapsam">Rızanın kapsamı</h2>
<p>Aşağıdaki başlıklarda sayılan işlemler, ancak ilgili kutucuğu işaretlemeniz veya yazılı
onay vermeniz hâlinde gerçekleştirilir. Rıza vermemeniz, açık rıza gerektirmeyen hizmet
adımlarını etkilemez.</p>

<h2 id="yurtdisi">Yurt dışına aktarım (KVKK m.9)</h2>
<p>Üniversite başvurusu, vize ve konaklama işlemlerinin doğası gereği; kimlik, iletişim,
eğitim ve gerektiğinde finansal verilerinizin <b>Macaristan'daki üniversitelere, resmî
makamlara ve konaklama sağlayıcılarına</b> aktarılmasına açık rıza vermeniz gerekir.
Bu aktarım yapılmadan başvuru süreci yürütülemez. Macaristan AB üyesi olduğundan
aktarılan veriler GDPR güvencesi altındadır.</p>

<h2 id="saglik">Sağlık verisi (özel nitelikli)</h2>
<p>Yalnız <b>pilotaj programı başvurularında</b> (uçuş sağlık raporu) ve <b>sağlık sigortası
işlemlerinde</b> sağlık verisi işlenir. Bu veriler açık rızanız olmadan işlenmez, yalnız ilgili
kuruma iletilir ve başka hiçbir amaçla kullanılmaz.</p>

<h2 id="pazarlama">Pazarlama iletişimi</h2>
<p>Yeni programlar, başvuru dönemi hatırlatmaları ve etkinlikler hakkında e-posta, SMS,
telefon veya WhatsApp üzerinden bilgilendirilmeyi kabul etmeniz hâlinde iletişim
bilgileriniz bu amaçla kullanılır. Bu izin, ticari elektronik ileti mevzuatına tabidir ve
her iletide yer alan yöntemle ya da bize yazarak dilediğiniz an iptal edilebilir.</p>

<h2 id="gorsel">Fotoğraf ve video</h2>
<p>Öğrenci hikâyeleri bölümünde deneyiminizin; adınızın baş harfi veya tam adınız,
üniversite ve bölüm bilginizle birlikte yayınlanması yalnız <b>ayrı yazılı izninizle</b>
gerçekleşir. İzni geri aldığınızda içerik makul süre içinde yayından kaldırılır.</p>

<h2 id="geri">Rızanın geri alınması</h2>
<p>Verdiğiniz her açık rızayı <b>info@huneducation.com</b> adresine yazarak dilediğiniz zaman,
gerekçe göstermeksizin geri alabilirsiniz. Geri alma, o ana kadar yapılmış işlemlerin
hukuka uygunluğunu etkilemez. Yurt dışına aktarım rızasının başvuru süreci devam ederken
geri alınması hâlinde sürecin yürütülemeyeceği tarafınıza bildirilir.</p>

{related([(S['privacy'],"Yasal","KVKK Aydınlatma Metni","İşleme amaçları, hukuki sebepler ve haklarınız."),
          (S['cookies'],"Yasal","Gizlilik ve Çerez Politikası","Sitenin kullandığı depolama teknolojileri."),
          (S['contact'],"İletişim","Bize ulaşın","Rıza ve veri talepleriniz için iletişim kanalları.")])}
</article>
</div>'''

write(S['consent'], legal_page(
    S['consent'],
    'Açık Rıza Metni | Hun Education',
    'Yurt dışına veri aktarımı, sağlık verisi, pazarlama iletişimi ve fotoğraf/video yayını için '
    'açık rıza kapsamı ve rızanın geri alınması.',
    'Açık Rıza Metni',
    'Açık rızaya bağlı işlemler ve her birinin kapsamı. Rıza kalemleri birbirinden bağımsızdır '
    've dilediğiniz an geri alınabilir.',
    body_riza, 'Açık Rıza Metni'))

# =====================================================================
# 3) GİZLİLİK VE ÇEREZ POLİTİKASI
# =====================================================================
body_gizlilik = f'''<div class="alayout">
{toc([('ilkeler','Gizlilik ilkelerimiz'),('guvenlik','Veri güvenliği'),('depolama','Çerezler ve yerel depolama'),
      ('ucuncu','Üçüncü taraf hizmetler'),('analitik','Analitik'),('degisiklik','Politika değişiklikleri')])}

<article class="prose">

<h2 id="ilkeler" style="margin-top:0">Gizlilik ilkelerimiz</h2>
<ul>
  <li>Yalnız hizmetin gerektirdiği veriyi toplarız; “belki lazım olur” diye veri istemeyiz.</li>
  <li>Verilerinizi hiçbir üçüncü tarafa satmayız veya kiralamayız.</li>
  <li>Aktarım yalnız <a href=S['privacy']>Aydınlatma Metni</a>'nde sayılan alıcılarla sınırlıdır.</li>
  <li>Zorunlu olmayan hiçbir izleme teknolojisi, izniniz olmadan çalışmaz.</li>
</ul>

<h2 id="guvenlik">Veri güvenliği</h2>
<p>Web sitemizle iletişiminiz TLS ile şifrelenir. Kişisel verilere erişim, görevi gereği
ihtiyaç duyan personelle sınırlıdır. Başvuru belgeleri yetkisiz erişime karşı korunan
sistemlerde saklanır; saklama süresi dolan veriler silinir veya anonimleştirilir.</p>

<h2 id="depolama">Çerezler ve yerel depolama</h2>
<p>Sitemiz klasik izleme çerezleri yerine tarayıcı depolaması kullanır. Fiilen kullanılan
kayıtların tamamı aşağıdadır:</p>

<div class="tablewrap">
<table class="dtable">
  <thead><tr><th>Kayıt</th><th>Tür</th><th>Amaç</th><th>Süre</th></tr></thead>
  <tbody>
    <tr><td class="num">hun_curtain</td><td>sessionStorage</td><td>Açılış animasyonunun aynı oturumda tekrarlanmaması</td><td>Sekme kapanınca silinir</td></tr>
    <tr><td class="num">hun_first_touch</td><td>localStorage</td><td>Siteye ilk geliş kaynağınızın (ör. arama, reklam) form gönderiminizle eşleştirilmesi, yalnız form gönderirseniz bize ulaşır</td><td>Tarayıcı verisini temizleyene kadar</td></tr>
  </tbody>
</table>
</div>
<p>Bu kayıtlar kimliğinizi tespit etmez ve üçüncü taraflara iletilmez. Tarayıcınızın site
verilerini temizleme özelliğiyle dilediğiniz an silebilirsiniz; sitenin çalışması etkilenmez.</p>

<h2 id="ucuncu">Üçüncü taraf hizmetler</h2>
<div class="tablewrap">
<table class="dtable">
  <thead><tr><th>Hizmet</th><th>Ne zaman devreye girer</th><th>Not</th></tr></thead>
  <tbody>
    <tr><td><b>WhatsApp (Meta)</b></td><td>Yalnız “WhatsApp’tan Sor” bağlantısına tıkladığınızda</td><td>Yazışma WhatsApp'ın kendi gizlilik politikasına tabidir; siteden otomatik veri aktarılmaz</td></tr>
    <tr><td><b>Sosyal medya bağlantıları</b></td><td>Yalnız tıkladığınızda</td><td>Gömülü izleme kodu içermezler</td></tr>
  </tbody>
</table>
</div>

<h2 id="analitik">Analitik</h2>
<p>Analitik ölçüm (ör. Google Analytics) kullanılması hâlinde, zorunlu olmayan bu teknoloji
yalnız <b>izniniz alındıktan sonra</b> etkinleştirilir; izin vermezseniz hiçbir analitik
verisi toplanmaz. Bu bölüm, analitik altyapı devreye alındığında kullanılan araç ve
saklama sürelerini içerecek şekilde güncellenir.</p>

<h2 id="degisiklik">Politika değişiklikleri</h2>
<p>Bu politika ihtiyaç hâlinde güncellenir; yürürlük tarihi sayfanın üstünde belirtilir.
Kapsamlı değişiklikler sitede duyurulur. Sorularınız için:
<b>info@huneducation.com</b></p>

{related([(S['privacy'],"Yasal","KVKK Aydınlatma Metni","İşleme amaçları, hukuki sebepler ve haklarınız."),
          (S['consent'],"Yasal","Açık Rıza Metni","Rızaya bağlı işlemler ve geri alma."),
          (S['terms'],"Yasal","Kullanım Koşulları","Hizmetin kapsamı ve sorumluluk sınırları.")])}
</article>
</div>'''

write(S['cookies'], legal_page(
    S['cookies'],
    'Gizlilik ve Çerez Politikası | Hun Education',
    'Hun Education web sitesinin veri güvenliği ilkeleri, kullanılan tarayıcı depolaması, üçüncü '
    'taraf hizmetler ve analitik izin politikası.',
    'Gizlilik ve Çerez Politikası',
    'Sitenin fiilen kullandığı depolama teknolojileri, üçüncü taraf hizmetler ve veri güvenliği '
    'ilkelerimiz, olduğu gibi, eksiksiz.',
    body_gizlilik, 'Gizlilik ve Çerez Politikası'))

# =====================================================================
# 4) KULLANIM KOŞULLARI
# =====================================================================
body_kosullar = f'''<div class="alayout">
{toc([('hizmet','Hizmetin niteliği'),('bilgi','Sitedeki bilgilerin niteliği'),('garanti','Garanti verilmeyen konular'),
      ('iade','Ücretler ve iade'),('fikri','Fikri mülkiyet'),('sorumluluk','Sorumluluğun sınırlandırılması'),
      ('degisiklik','Değişiklikler ve uygulanacak hukuk')])}

<article class="prose">

<h2 id="hizmet" style="margin-top:0">Hizmetin niteliği</h2>
<p>HUN EDUCATION KFT., Macaristan'daki yükseköğretim kurumlarına başvuru sürecinde
<b>akademik danışmanlık ve aracılık</b> hizmeti sunar: hedef analizi, program eşleştirme,
başvuru dosyası hazırlığı, kabul takibi, vize rehberliği, konaklama desteği ve varış sonrası
oryantasyon. Hun Education bir yükseköğretim kurumu değildir; kabul, kayıt, vize ve denklik
kararları ilgili kurumlara aittir.</p>

<h2 id="bilgi">Sitedeki bilgilerin niteliği</h2>
<p>Sitede yer alan öğrenim ücretleri, başvuru tarihleri, kabul şartları ve program bilgileri
danışmanlık ekibimizce dönemsel olarak güncellenir; ancak <b>üniversiteler tarafından her an
değiştirilebilir</b> ve bağlayıcı taahhüt niteliği taşımaz. Nihai koşullar, ilgili
üniversitenin resmî yayınları ve tarafınızla imzalanan hizmet sözleşmesiyle belirlenir.</p>

<h2 id="garanti">Garanti verilmeyen konular</h2>
<ul>
  <li><b>Kabul garantisi verilmez.</b> Kabul kararı münhasıran başvurulan üniversiteye aittir.</li>
  <li><b>Vize garantisi verilmez.</b> Vize kararı münhasıran ilgili konsolosluğa/resmî makama aittir.</li>
  <li><b>Denklik garantisi verilmez.</b> Türkiye'de denklik değerlendirmesi YÖK'ün güncel mevzuatına tabidir.</li>
  <li>Burs, çalışma izni ve mezuniyet sonrası olanaklara ilişkin bilgiler genel bilgilendirmedir; ilgili mevzuat değişebilir.</li>
</ul>

<h2 id="iade">Ücretler ve iade</h2>
<p>Danışmanlık hizmet bedeli, üniversiteye ödenen ücretlerden ayrıdır ve hizmet sözleşmesinde
açıkça belirtilir. Vize başvurunuzun reddedilmesi hâlinde üniversiteye ödenen <b>öğrenim
ücreti 30 iş günü içinde iade edilir</b>; başvuru ve sınav ücretleri iade kapsamı dışındadır.
İade koşullarının ayrıntısı hizmet sözleşmesinde yer alır.</p>

<h2 id="fikri">Fikri mülkiyet</h2>
<p>Bu sitedeki metin, tasarım, logo ve görseller HUN EDUCATION KFT.'ye aittir veya izinle
kullanılmaktadır. Kaynak gösterilerek kısa alıntı yapılabilir; içeriğin izinsiz kopyalanması,
çoğaltılması veya ticari amaçla kullanılması yasaktır. Üniversite adları ilgili kurumlara aittir
ve yalnız bilgilendirme amacıyla anılır.</p>

<h2 id="sorumluluk">Sorumluluğun sınırlandırılması</h2>
<p>Hun Education; üniversitelerin, resmî makamların veya üçüncü taraf hizmet sağlayıcıların
karar ve işlemlerinden, mevzuat değişikliklerinden ve sitenin kesintisiz erişilebilirliğinden
sorumlu tutulamaz. Zorunlu tüketici mevzuatından doğan haklarınız saklıdır.</p>

<h2 id="degisiklik">Değişiklikler ve uygulanacak hukuk</h2>
<p>Bu koşullar gerektiğinde güncellenir; güncel sürüm her zaman bu sayfada yayınlanır ve
yürürlük tarihi üstte belirtilir. Hizmet sözleşmesinden doğan uyuşmazlıklarda sözleşmede
belirlenen hukuk ve yetki kuralları esas alınır; tüketicilerin yerleşim yerindeki başvuru
hakları saklıdır.</p>

{related([(S['privacy'],"Yasal","KVKK Aydınlatma Metni","Kişisel verilerinizin işlenmesi."),
          (S['about'],"Kurumsal","Hakkımızda","1999'dan beri Macaristan odaklı danışmanlık."),
          (S['contact'],"İletişim","Bize ulaşın","Sorularınız için iletişim kanalları.")])}
</article>
</div>'''

write(S['terms'], legal_page(
    S['terms'],
    'Kullanım Koşulları | Hun Education',
    'Hun Education danışmanlık hizmetinin kapsamı, sitedeki bilgilerin niteliği, garanti verilmeyen '
    'konular, iade koşulları ve sorumluluk sınırları.',
    'Kullanım Koşulları',
    'Hizmetimizin ne olduğu ve ne olmadığı; sitedeki bilgilerin niteliği ve tarafların hak ve '
    'sorumlulukları.',
    body_kosullar, 'Kullanım Koşulları'))
