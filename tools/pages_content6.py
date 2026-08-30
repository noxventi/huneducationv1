# -*- coding: utf-8 -*-
# Canlida yayinda olup yeni tasarimda karsiligi olmayan sayfalar (2/3).

# =====================================================================
# TIP  ->  /macaristanda-tip-egitimi-ve-macaristanda-tip-okumak/
# =====================================================================
qa_tip = [
    ("Macaristan'da tıp için giriş sınavı var mı?",
     "<p>Evet, her tıp fakültesi kendi giriş değerlendirmesini uygular: kimya ve biyoloji, "
     "üniversiteye göre sözlü ya da yazılı. YKS puanı istenmez; konusu belli olduğu için "
     "ortalama 6–10 haftalık bir çalışmayla hazırlanılır.</p>"),
    ("Tıp kaç yıl ve hangi dereceyi verir?",
     "<p>Tıp altı yıl, diş hekimliği beş yıl; ikisi de bütünleşik (tek aşamalı) program. Verilen derece "
     "doktora düzeyinde bir meslek diplomasıdır (MD / DMD), lisans artı yüksek lisans değil.</p>"),
    ("Tıp yıllık ne kadar tutar?",
     "<p>Üniversiteye ve ücretin alındığı para birimine göre değişir: Semmelweis 19.900 $, Pécs "
     "18.000 $, Szeged 15.800 €. Pécs'te diş hekimliği 18.600 €. Hun Education'ın tıp ve diş için "
     "yayınladığı yaşam gideri dahil rakam yıllık yaklaşık 26.000 €.</p>"),
    ("Macaristan tıp diplomasıyla Türkiye'de hekimlik yapabilir miyim?",
     "<p>Tıp her ülkede düzenlenmiş bir meslek. Hekimlik yapmak, çalışacağınız ülkedeki yetkili kurumun "
     "denklik değerlendirmesini ve çoğu durumda bir yeterlilik sınavını gerektirir. Başvurmadan önce "
     "yetkili kurumun güncel kurallarını inceleyin. <b>Denklik vaadinde bulunmuyoruz.</b></p>"),
]

body_tip = f'''<div class="alayout">
{toc([('universiteler','Hangi üniversitelerde okutulur?'),
      ('sinav','Giriş sınavı ve hazırlık'),('yapi','Altı yıl nasıl ilerler?'),
      ('maliyet','Eğitim ücretleri'),
      ('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}

<article class="prose">

<section id="giris" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Macaristan, İngilizce tıp eğitimi almak isteyen öğrenciler için Avrupa'nın öne çıkan
  ülkelerinden biri. YKS puanı gerektirmeyen altı yıllık bütünleşik tıp programları; Budapeşte'deki
  Semmelweis Üniversitesi ile Pécs ve Szeged Üniversitelerinde sunulur.</p>

  <p><b>Hun Education olarak,</b> Macaristan'daki tıp eğitimi başvurularında yıllara dayanan
  deneyimimizle öğrencilerimizin yanındayız. Üniversite seçiminden giriş sınavına hazırlığa, başvuru
  belgelerinden vize sürecine kadar her aşamayı planlıyor ve öğrencilerimize hedeflerine giden yolda
  profesyonel danışmanlık sağlıyoruz.</p>
</section>

<p>Bu sayfada Macaristan'da tıp okumanın nasıl işlediğini, hangi üniversitelerde okutulduğunu, giriş
sınavının neyi ölçtüğünü ve gerçekçi bir bütçenin ne kadar olduğunu anlatıyoruz.</p>

<h2 id="universiteler">Hangi üniversitelerde okutulur?</h2>
<p>Uluslararası öğrencilere tıp eğitimi veren üç üniversite var ve üçü de köklü kurumlar. Semmelweis
Üniversitesi 1769'dan bu yana hekim yetiştirir ve Avrupa'nın en tanınmış tıp fakülteleri arasında
sayılır. Pécs Üniversitesi ülkenin en eski üniversitesi; geniş araştırma altyapısıyla öne çıkar.
Szeged Üniversitesi ise euro cinsinden en uygun tıp ücretini sunar.</p>
<p>Diş hekimliği ve eczacılık da aynı fakültelerde okutulur. Yani tercih listenizi tek bir şehre
sıkıştırmak zorunda değil, hem alanınıza hem bütçenize göre birden fazla seçenekle ilerleyebiliyorsunuz.</p>
<div class="tablewrap">
<table class="dtable">
  <caption>Uluslararası öğrenciye açık tıp fakülteleri</caption>
  <thead><tr><th>Üniversite</th><th>Şehir</th><th>Programlar</th><th>Yıllık ücret</th></tr></thead>
  <tbody>
    <tr><td><b>Semmelweis Üniversitesi (SOTE)</b></td><td>Budapeşte</td><td>Tıp (6 yıl)</td><td class="num">19.900 $</td></tr>
    <tr><td><b>Pécs Üniversitesi (PTE)</b></td><td>Pécs</td><td>Tıp (6 yıl)</td><td class="num">18.000 $</td></tr>
    <tr><td><b>Szeged Üniversitesi (SZTE)</b></td><td>Szeged</td><td>Tıp (6 yıl)</td><td class="num">15.800 €</td></tr>
    <tr><td><b>Pécs Üniversitesi (PTE)</b></td><td>Pécs</td><td>Diş Hekimliği (5 yıl)</td><td class="num">18.600 €</td></tr>
    <tr><td><b>Semmelweis Üniversitesi (SOTE)</b></td><td>Budapeşte</td><td>Eczacılık (5 yıl)</td><td class="num">12.600 €</td></tr>
    <tr><td><b>Pécs Üniversitesi (PTE)</b></td><td>Pécs</td><td>Eczacılık (5 yıl)</td><td class="num">8.800 €</td></tr>
  </tbody>
</table>
</div>

<h2 id="sinav">Giriş sınavı ve hazırlık</h2>
{figure('tip-ogrenci-calisma-grubu',
        'Derslikte masa başında birlikte çalışan öğrenci grubu',
        'Hazırlık ortalama 6–10 hafta sürüyor.')}
<p>Macaristan'da tıp okumak için YKS puanına ihtiyacınız yok; bunun yerine fakülte sizi kendi giriş
değerlendirmesine tabi tutar. Bu değerlendirme kimya ve biyoloji üzerine kurulu ve üniversiteye göre
sözlü ya da yazılı yapılır. Üniversite giriş sınavları kadar yıpratıcı olmadığını, konusunun belli
olduğu için çalışılabilir bir sınav olduğunu rahatlıkla söyleyebiliriz. Lisede fen ve matematik ağırlıklı
bir program okuduysanız bu aşamada önemli bir avantajınız olur.</p>
<div class="tablewrap">
<table class="dtable">
  <caption>Değerlendirme neyi kapsar</caption>
  <thead><tr><th>Öge</th><th>Ayrıntı</th></tr></thead>
  <tbody>
    <tr><td><b>Dersler</b></td><td>Kimya ve biyoloji</td></tr>
    <tr><td><b>Biçim</b></td><td>Üniversiteye göre değişir. Semmelweis değerlendirmesini mülakat olarak kaydeder; Szeged çevrim içi yazılı ve sözlü sınav yapar.</td></tr>
    <tr><td><b>Dil</b></td><td>İngilizce; ayrıca İngilizceniz de değerlendirilir</td></tr>
    <tr><td><b>Hazırlık</b></td><td>Yürüttüğümüz dosyalarda gözlemlediğimiz aralık 6–10 hafta</td></tr>
    <tr><td><b>Tekrar hakkı</b></td><td>Üniversiteye ve döneme göre değişir</td></tr>
  </tbody>
</table>
</div>
<p>Hazırlığı yalnız yürütmüyorsunuz: hangi fakültenin neyi sorduğunu, geçmiş adayların nerede
zorlandığını ve size kaç hafta gerektiğini danışmanınız baştan çıkarır.</p>
{inline_cta("Kimya ve biyoloji altyapınıza bakalım, hazırlık takviminizi birlikte kuralım.")}
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Hazırlık süresi kendi başvuru dosyalarımızdan edinilmiş saha gözlemidir, üniversitenin resmî tavsiyesi
değildir. Kabul kararı tamamen fakülteye aittir.</p>

<h2 id="yapi">Altı yıl nasıl ilerler?</h2>
{strip('Tıp eğitiminden kareler', [
 ('tip-mikroskop-laboratuvar',
  'Laboratuvarda önlüklü bir araştırmacı mikroskop başında; tezgâhta kan tüpleri',
  'İlk iki yıl: temel bilimler ve laboratuvar.'),
 ('tip-goruntuleme-ekranlari',
  'Radyoloji odasında ekranlarda beyin görüntüleme kesitleri',
  'Klinik yıllar: tanı ve görüntüleme.'),
 ('tip-laboratuvar-tup',
  'Bone ve gözlük takmış laboratuvar çalışanı, mavi deney tüplerine pipetle sıvı aktarıyor',
  'Laboratuvar uygulamaları eğitim boyunca sürüyor.'),
])}
<p>Program klasik tıp eğitimi kurgusunu izler: önce temel bilimler, ardından klinik dersler ve
son yıl hastanede uygulama. Aşağıdaki dört adım altı yılın tamamını özetler.</p>
<ol class="steps">
  <li><div><h3>1–2. yıl · Temel bilimler</h3><p>Anatomi, biyokimya, fizyoloji. Programın en yoğun iki yılı; buradan sonrası belirgin şekilde rahatlar.</p></div></li>
  <li><div><h3>3–4. yıl · Preklinik ve klinik</h3><p>Patoloji, farmakoloji ve klinik derslere geçiş; hastane teması başlar.</p></div></li>
  <li><div><h3>5. yıl · Klinik rotasyonlar</h3><p>Eğitim hastanelerinde ana branşlar arasında rotasyon.</p></div></li>
  <li><div><h3>6. yıl · İntörnlük</h3><p>Bir yıl süreyle gözetim altında klinik uygulama, ardından bitirme sınavları ve diploma.</p></div></li>
</ol>

<h2 id="maliyet">Eğitim ücretleri</h2>
<div class="answer">
  <span class="answer__label">Gerçekçi yıllık toplam</span>
  <p><b>Yaklaşık 26.000 €</b>, yaşam giderleri dahil. Bu Hun Education'ın tıp ve diş hekimliği için
  kendi yayınladığı rakam ve diğer programların 8.500 – 14.000 € bandının çok üstünde; çünkü yalnız
  öğrenim ücreti 15.800 € ile 19.900 $ arasında.</p>
</div>
<p>Bu rakam Batı Avrupa ve Kuzey Amerika'daki tıp fakültelerinin belirgin şekilde altında; Macaristan'ı
uluslararası öğrenciler için çekici kılan da bu. Planlamayı altı yıl üzerinden yapın: ilk yıl başvuru,
vize ve depozito gibi tek seferlik kalemleri de taşır, dolar cinsinden bir programda ise kur
hareketini hesaba katmak gerekir. Ödeme takvimini birlikte çıkarıyoruz.</p>

<h3>Henüz hazır hissetmiyorsanız</h3>
<p>Dil seviyeniz ya da fen altyapınız henüz yeterli değilse endişelenmenize gerek yok. Bir yıllık
hazırlık programlarıyla hem İngilizcenizi hem tıp öncesi derslerinizi tamamlayıp bir sonraki dönem
bölüme geçebiliyorsunuz.</p>
<div class="tablewrap">
<table class="dtable">
  <caption>Tıp hazırlık ve dil hazırlık seçenekleri</caption>
  <thead><tr><th>Program</th><th>Üniversite</th><th>Yıllık ücret</th></tr></thead>
  <tbody>
    <tr><td><b>PreMedical / PreEngineering / PreBusiness</b></td><td>Pécs Üniversitesi (PTE)</td><td class="num">5.850 €</td></tr>
    <tr><td><b>Two-semester Pre-Medical Track</b></td><td>McDaniel College Budapest</td><td class="num">7.230 €</td></tr>
    <tr><td><b>Pre-Medical (Intensive)</b></td><td>McDaniel College Budapest</td><td class="num">7.800 €</td></tr>
    <tr><td>İngilizce Dil Hazırlık</td><td>Birden çok üniversite</td><td class="num">2.500 €'dan</td></tr>
  </tbody>
</table>
</div>
<p>Hepsi güncel ücret ve son başvuru tarihleriyle <a href="{S['progs']}">katalogda</a>.</p>

<h3>Mezuniyetten sonra</h3>
<p>Tıp düzenlenmiş bir meslek; diplomanızı hangi ülkede kullanacaksanız o ülkenin yetkili kurumundan
denklik almanız gerekir. Değerlendirme genellikle üniversitenin tanınırlığı, programın içeriği,
süresi ve tamamladığınız klinik eğitim üzerinden yapılır ve birçok ülke buna bir yeterlilik sınavı
ekler.</p>
<p>Bu konuyu son sınıfa bırakmıyoruz. Hangi ülkede hekimlik yapmayı düşündüğünüzü daha başvuru
aşamasında konuşuyor, bilinen şartları birlikte gözden geçiriyoruz. Kararı yetkili kurum verdiği için
sonuç hakkında taahhüt vermiyoruz; ama yolun nereye çıktığını baştan biliyorsunuz.</p>

<h2 id="sss">Sık sorulan sorular</h2>
{faq_block(qa_tip)}

<section id="kaynak" class="sources">
  <h2>Kaynaklar ve doğrulama</h2>
  <ol>
    <li>Ücret, program yapısı ve giriş sınavı şartları fakültelerin güncel yayınlarından derlenir ve her akademik yıl gözden geçirilir.</li>
    <li>Hazırlık süreleri danışmanlarımızın yürüttüğü başvuru dosyalarından edinilmiş saha gözlemidir.</li>
    <li>Denklik ve yeterlilik ülkenizdeki yetkili kurumun kararıdır; güncel mevzuatı esas alınız.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Tıp hayaliniz için ilk adımı atın", "Bu başvuruyu giriş sınavı belirler ve hazırlık ortalama 6–10 hafta sürer. Kimya ve biyoloji altyapınıza bakalım, size özel bir hazırlık takvimi çıkaralım. Görüşme ücretsiz.")}

{related([(S['apply'],"Başvuru","Başvuru şartları","Belgeler, dil şartı ve takvim."),
          (S['costs'],"Maliyet","Ücretler ve yaşam gideri","Tıp neden bandın üstünde."),
          (S['unis'],"Üniversite","Tıp fakülteleri","Semmelweis, Pécs ve Szeged.")])}
</article>
</div>'''

write(S['medicine'], page(
    S['medicine'],
    'Macaristan’da Tıp Eğitimi: Giriş Sınavı ve Ücretler (2026) | Hun Education',
    "Macaristan'da tıp okumak: tıp okutan üç üniversite, 15.800 € ile 19.900 $ arasındaki gerçek "
    "yıllık ücretler, giriş değerlendirmesi ve mezuniyet sonrası denklik süreci.",
    'Tıp rehberi',
    'Macaristan’da tıp eğitimi',
    'Altı yıl, İngilizce, üç üniversitede. Giriş değerlendirmesi ne sorar, yıllar nasıl kurgulanır '
    've bütün bunun gerçek maliyeti ne?',
    body_tip, S['medicine'],
    [HOME, ('Tıp Eğitimi', url_of('medicine'))],
    qa_tip))

# =====================================================================
# PİLOTAJ  ->  /macaristan-universiteleri-pilotluk-egitimi/
# =====================================================================
qa_pilot = [
    ("Program hangi lisansa götürür?",
     "<p>Profesyonel pilotluk BSc'si akademik dereceyle uçuş eğitimini birleştirip ticari pilot lisansına "
     "yönelir. Lisansın tipi, yetkilendirmeler ve uçuş saati sayısı üniversite ile havacılık otoritesi "
     "tarafından belirlenir ve değişebilir; taahhüt vermeden önce güncel yapıyı üniversiteden teyit "
     "edin.</p>"),
    ("Pilotaj neden bu kadar pahalı?",
     "<p>Çünkü maliyeti öğrenim değil uçuş saatleri belirler. "
     "BME'de yıllık 29.500 €, UOD'nin birleşik programında 66.800 € bunu yansıtır; ücret "
     "yıllık olarak açıklanır ve uçuş eğitimini kapsar.</p>"),
    ("Hangi sağlık raporu gerekir?",
     "<p>Yetkili hekimden alınacak Class 1 uçuş sağlık sertifikası. Bunu başvurudan sonra değil önce "
     "değerlendirin: pilotaj başvurusunun en sık burada durduğunu görüyoruz.</p>"),
]

body_pilot = f'''<div class="alayout">
{toc([('neden','Neden Macaristan?'),('nerede','Hangi üniversitelerde okutulur?'),
      ('ucret','Ücretler ve neyi kapsar'),('sartlar','Başvurmadan önce hazırlamanız gerekenler'),
      ('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}

<article class="prose">

<section id="giris" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Macaristan üniversiteleri, uluslararası öğrencilere yüzlerce İngilizce program sunarken pilotaj
  eğitimi son yılların en çok ilgi gören seçeneklerinden biri olarak öne çıkar. Öğrenciler, akademik
  lisans eğitimi ile uygulamalı uçuş eğitimini aynı program kapsamında tamamlayarak mezuniyetlerinde
  hem üniversite diplomasına hem de profesyonel pilotluk kariyerine yönelik gerekli yetkinliklere
  sahip olur.</p>

  <p><b>Hun Education olarak,</b> pilotaj eğitimi almak isteyen öğrencilerimizin üniversite
  başvurularını her yıl titizlikle yürütüyoruz. Uygun programın belirlenmesinden sağlık sertifikasına,
  kabul sürecinden uçuş eğitimine kadar tüm aşamaları öğrencilerimizle birlikte planlıyor ve sürecin
  her adımında yanlarında oluyoruz.</p>
</section>

<p>Bu sayfada Macaristan'da pilotaj eğitiminin neden öne çıktığını, hangi üniversitelerde
okutulduğunu, ücretlerin gerçekte neyi kapsadığını ve başvurudan önce hazırlamanız gerekenleri
anlatıyoruz.</p>
{figure('pilotaj-hangar-egitim-ucagi',
        'Uçuş üniforması ve reflektif yelek giymiş öğrenci, hangarda çift motorlu eğitim uçağının önünde',
        'Macaristan’da pilotaj eğitimi alan öğrencimiz, eğitim uçağının önünde.',
        oncelik=True)}

<h2 id="neden">Neden Macaristan?</h2>
<p>Pilot olmak isteyen bir öğrencinin önünde genellikle üç yol bulunur: havayollarının kadet
programları, üniversitelerin havacılık bölümleri ya da özel uçuş okulları. Bu yolların her birinin
kendine göre bir bedeli var; kadet programları uzun süreli sözleşmeye bağlar, uçuş okulları ise
yüksek ücret karşılığında yalnızca lisans verir, elinizde bir diploma kalmaz.</p>

<p>Macaristan'ın farkı burada ortaya çıkar. Uçuş eğitimi entegre bir lisans programının içinde
verilir; yani teorik dersler ve uçuş saatleri aynı takvim üzerinde ilerler ve mezuniyette elinizde
hem ticari pilot lisansı hem de bir üniversite diploması olur. Sağlık sertifikanızın yenilenmediği
bir durumda bile akademik dereceniz durur, bu da mesleğin doğası gereği önemli bir güvence.</p>

<p>Buna Macaristan'ın Türkiye'ye yakınlığı, eğitimin baştan sona İngilizce yürümesi ve Batı
Avrupa'nın altında seyreden yaşam maliyeti eklenir. Ülke her yıl daha fazla Türk pilot adayını
ağırlıyor ve gittiğinizde sizden önce gelmiş bir topluluk buluyorsunuz.</p>
{strip('Pilotaj eğitiminden kareler', [
 ('pilotaj-ogrenci-pervane',
  'Pilot üniformalı öğrenci, tek motorlu eğitim uçağının pervanesinin yanında',
  'Tek motorlu eğitim uçağıyla ilk saatler.'),
 ('pilotaj-ogrenciler-hangara-giderken',
  'Reflektif yelekli öğrenci grubu, çimenlikten uçak hangarına doğru yürürken',
  'Uçuş günü: öğrenciler hangara giderken.'),
 ('pilotaj-derslik-uniformali',
  'Pilot üniformalı öğrenci grubu, derslikte sıraların başında',
  'Teorik ders saati.'),
 ('pilotaj-apron-gun-batimi',
  'Gün batımında havalimanı apronu, körüğe yanaşmış yolcu uçağı',
  'Ticari havacılık: lisans sonrası hedef.'),
 ('pilotaj-ogrenciler-pist',
  'Pilot gömlekli üç öğrenci, uçuş alanında birlikte',
  'Uçuş alanında öğrencilerimiz.'),
])}

<h2 id="nerede">Hangi üniversitelerde okutulur?</h2>
<p>Hun Education aracılığıyla başvurabileceğiniz iki program var ve ikisi birbirinden oldukça farklı.
Budapeşte Teknoloji ve Ekonomi Üniversitesi (BME), ülkenin en köklü teknik üniversitesi olarak
<b>Professional Pilot</b> programını yürütür. Dunaújváros Üniversitesi (UOD) ise sıfırdan ATPL'e
uzanan uçuş eğitimini makine mühendisliğiyle birleştirir; ücretinin yüksek olmasının sebebi de bu
ikili yapı. UOD, Budapeşte'nin güneyinde Tuna kıyısında yer alır ve yaşam maliyeti başkente göre
belirgin şekilde düşük.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Havacılık programları ve yıllık öğrenim ücretleri</caption>
  <thead><tr><th>Program</th><th>Üniversite</th><th>Süre</th><th>Yıllık ücret</th></tr></thead>
  <tbody>
    <tr><td><b>Professional Pilot</b></td><td>BME, Budapeşte</td><td>7 dönem</td><td class="num">29.500 €</td></tr>
    <tr><td><b>Pilot Training (0 to ATPL) + Makine Mühendisliği</b></td><td>UOD, Dunaújváros</td><td>7 dönem</td><td class="num">66.800 €</td></tr>
    <tr><td>BSc Makine Mühendisliği <i>(uçuş eğitimi yok)</i></td><td>UOD, Dunaújváros</td><td>7 dönem</td><td class="num">3.950 €</td></tr>
  </tbody>
</table>
</div>
<p>Tablodaki üçüncü satırı ölçek vermek için ekledik: aynı mühendislik diploması, uçuş eğitimi
olmadan yılda 3.950 €. Aradaki farkı yaratan şey doğrudan uçmanın kendisi.</p>

{inline_cta("İki programı yan yana koyalım, bütçenize ve hedefinize uyanı birlikte seçelim.")}

<h2 id="ucret">Ücretler ve neyi kapsar</h2>
{figure('pilotaj-ucak-motoru',
        'Apronda bir yolcu uçağının motoru ve kanadı, bulutlu gökyüzü',
        'Uçuş saati, ücretin en belirleyici kalemi.')}
<p>Pilotaj, kataloğumuzda ücretin mutlaka açılması gereken tek program; çünkü buradaki rakam alışıldık
anlamda bir öğrenim ücreti değil. Yıllık ücret hem teorik dersleri hem simülatör çalışmalarını hem de
lisansın gerektirdiği uçuş saatlerini kapsar. Bir mühendislik diplomasının kat kat üzerinde
olmasının sebebi tek başına uçuş saatleri.</p>

<p>Ücretin dışında kalan tek önemli kalem uçuş sağlık sertifikası; bu belge kabulden önce alınır ve
eğitim boyunca periyodik olarak yenilenir. Yaşam giderlerinizi de ayrıca planlamanız gerekir,
Dunaújváros'ta bu kalem Budapeşte'ye göre gözle görülür şekilde düşük.</p>

<p>Ücretin neyi kapsadığına dair yazılı dökümü üniversiteden sizin adınıza biz istiyoruz: kaç uçuş
saati dahil, fazlası gerekirse ne olur, sağlık sertifikası ve yenilemeleri ücretin içinde mi. Böylece
iki üniversiteyi aynı ölçüyle karşılaştırıyor, sonradan sürprizle karşılaşmıyorsunuz.</p>

<h2 id="sartlar">Başvurmadan önce hazırlamanız gerekenler</h2>
{figure('budapeste-koprude-ogrenciler',
        'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci',
        'Özgürlük Köprüsü’nde öğrencilerimiz.')}
<p>Pilotaj başvurusunu diğer bölümlerden ayıran birkaç adım var ve bunları doğru sırayla yapmak
zaman kazandırır. Sıralama şöyle işler:</p>
<ol class="steps">
  <li><div><h3>Class 1 uçuş sağlık sertifikası</h3><p>Yetkili hekimden alınır ve her şeyden önce gelir. Pilotaj başvurusunun en sık durduğu nokta burası olduğu için ilk adımı buraya koyuyoruz.</p></div></li>
  <li><div><h3>İngilizce yeterliliği</h3><p>Hem derece için hem de havacılık telsiz iletişimi için ayrı ayrı değerlendirilir. Seviyeniz henüz yetmiyorsa hazırlık programıyla tamamlıyorsunuz.</p></div></li>
  <li><div><h3>Yetenek değerlendirmesi</h3><p>Üniversitenin uyguladığı, eğitimin varsaydığı koordinasyon ve durumsal muhakemeyi ölçen sınav.</p></div></li>
  <li><div><h3>Akademik dosya</h3><p>Apostilli diploma, transkript, pasaport ve İngilizce özgeçmiş; diğer programlarda olduğu gibi.</p></div></li>
</ol>
<p>Kabulden sonra eğitim iki koldan birlikte ilerler. Akademik tarafta aerodinamik, meteoroloji,
seyrüsefer, hava hukuku ve insan performansı işleniyor; uçuş tarafında ise simülatörden gözetimli
uçuşa geçerek lisansın gerektirdiği saatleri biriktiriyorsunuz. İkisi paralel yürüdüğü için program
üç değil üç buçuk yıl sürüyor, ama derste öğrendiğinizi aynı dönem havada pekiştiriyorsunuz.</p>

<h2 id="sss">Sık sorulan sorular</h2>
{faq_block(qa_pilot)}

<section id="kaynak" class="sources">
  <h2>Kaynaklar ve doğrulama</h2>
  <ol>
    <li>Program yapısı ve ücretler Dunaújváros Üniversitesi'nin yayınlanan koşullarından derlenir ve her akademik yıl gözden geçirilir.</li>
    <li>Lisans yapısı, gerekli uçuş saati ve sağlık standartları havacılık otoritesince belirlenir ve değişebilir; üniversitenin güncel dokümanı esastır.</li>
    <li>Uçuş saatleri uçuldukça faturalandığı için program toplamı öğrenciden öğrenciye değişir.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Pilot olma yolunda ilk adım", "Class 1 sağlık sertifikasıyla başlıyoruz. Hangi işlemi hangi sırayla ayarlamanız gerektiğini, tek kuruş ödemeden önce söyleyelim. Görüşme ücretsiz.")}

{related([(S['progs'],"Katalog","Havacılık programları","Pilotaj ve havacılık mühendisliği."),
          (S['costs'],"Maliyet","Ücretler nasıl alınır","Dönemlik, yıllık ve tek seferlik kalemler."),
          (S['apply'],"Başvuru","Başvuru şartları","Belgeler, dil şartı ve takvim.")])}
</article>
</div>'''

write(S['pilot'], page(
    S['pilot'],
    'Macaristan’da Pilotaj Eğitimi: Ücret, Lisans ve Şartlar | Hun Education',
    "Macaristan'da pilotluk eğitimi BME ve Dunaújváros Üniversitesi'nde: yıllık 29.500 € ve 66.800 €, "
    "ücretin neyi kapsadığı ve önce almanız gereken Class 1 sağlık sertifikası.",
    'Pilotaj rehberi',
    'Macaristan üniversitelerinde pilotluk eğitimi',
    'Uçuş eğitimini üniversite diplomasıyla birlikte alın. Hangi üniversitelerde okutulur, ücret '
    'neyi kapsar ve başvurudan önce neleri hazırlamanız gerekir?',
    body_pilot, S['pilot'],
    [HOME, ('Pilotluk Eğitimi', url_of('pilot'))],
    qa_pilot))
