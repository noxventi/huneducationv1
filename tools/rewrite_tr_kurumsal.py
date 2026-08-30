# -*- coding: utf-8 -*-
"""Turkce sayfa girisleri: kurumsal danismanlik dili.

Musterinin verdigi ornek metinden cikarilan olcut:

  1. Ilk cumle ulkeyi konumlandirir ("Macaristan, ... icin Avrupa'nin
     one cikan ulkelerinden biri."). Rakamla acilmaz.
  2. "Hun Education olarak," HER ZAMAN virgullu ve KENDI paragrafinda
     baslar. Sirketin ne yaptigi, bilgiyle karistirilmadan anlatilir.
  3. Yuklem zincirleri virgulle birbirine eklenmez. Her cumle tek bir
     is yapar; noktali virgul yalnizca siralama icin kullanilir.
  4. Rakamlar kendi cumlesinde durur, ust uste yigilmaz.
  5. Kurumsal fiiller: planliyoruz, yurutuyoruz, sagliyoruz,
     belirliyoruz, yanlarinda oluyoruz.

Rakamlarin hicbiri degismiyor; degisen yalnizca cumle kurulusu.
"""
import io

R = {
# =====================================================================
'tools/pages_content.py': [
# --- BAŞVURU ---
("""  <p>Macaristan'a başvuru süreci, ilk bakışta göründüğünden çok daha sade ilerliyor. Apostilli
  diplomanız, İngilizce transkriptiniz, pasaport fotokopiniz ve İngilizce özgeçmişiniz dosyanın
  tamamını oluşturuyor; banka dökümü başvuruda değil, vize aşamasında isteniyor. Lisansta pratikte B2
  İngilizce bekleniyor ama üniversitelerin çoğu dil belgesi yerine kendi mülakatını yapıyor.
  <b>Hun Education olarak</b> bu dosyayı sizin adınıza kuruyor, eksik kalan noktaları başvurudan önce
  tamamlıyoruz.</p>""",
 """  <p>Macaristan üniversitelerine başvuru süreci, birçok öğrencinin düşündüğünden çok daha sade
  ilerliyor. Başvuru dosyası; apostilli diploma, İngilizce transkript, pasaport fotokopisi ve İngilizce
  özgeçmişten oluşuyor. Banka dökümü ise başvuru aşamasında değil, vize başvurusu sırasında isteniyor.
  Lisans programlarında B2 düzeyinde İngilizce bekleniyor; ancak üniversitelerin büyük bölümü dil
  belgesi yerine kendi mülakatını uyguluyor.</p>

  <p><b>Hun Education olarak,</b> başvuru dosyanızı sizin adınıza hazırlıyor ve eksik kalan noktaları
  başvurudan önce tamamlıyoruz. Belge hazırlığından üniversite yazışmalarına kadar sürecin tamamını
  öğrencilerimiz adına yürütüyoruz.</p>"""),

# --- MALİYET ---
("""  <p>Yurt dışında okumayı düşünürken aklınıza gelen ilk soru büyük ihtimalle bütçe oluyor. Macaristan
  bu konuda rahatlatıcı bir tablo sunuyor: eğitim ve yaşam giderleri birlikte yıllık
  <b>8.500 – 14.000 €</b> tutuyor. Lisans öğrenim ücretleri 3.000 – 5.000 €, yüksek lisans
  4.000 – 6.000 €, tıp ve diş hekimliği ise 15.800 € ile 19.900 $ arasında değişiyor. Konaklamaya
  aylık 60 – 550 €, günlük yaşam giderlerine yaklaşık 300 € ayırmanız gerekiyor. Bütçenizi en çok
  etkileyecek tercih konaklama olacak; bu yüzden aşağıda her kalemi tek tek açıyoruz.</p>""",
 """  <p>Yurt dışında eğitim planlayan öğrencilerin en çok merak ettiği konuların başında bütçe geliyor.
  Macaristan bu açıdan Avrupa'nın en avantajlı ülkelerinden biri olarak öne çıkıyor. Eğitim ve yaşam
  giderleri birlikte değerlendirildiğinde bir akademik yılın toplam maliyeti
  <b>8.500 – 14.000 €</b> aralığında kalıyor.</p>

  <p>Öğrenim ücretleri programa göre değişiyor. Lisans programlarında yıllık 3.000 – 5.000 €, yüksek
  lisansta 4.000 – 6.000 €, tıp ve diş hekimliğinde ise 15.800 € ile 19.900 $ arasında bir tutar söz
  konusu. Bunlara aylık 60 – 550 € arasında konaklama gideri ve yaklaşık 300 € tutarında günlük yaşam
  gideri ekleniyor.</p>

  <p><b>Hun Education olarak,</b> öğrencilerimiz için gerçekçi bir bütçe planı çıkarıyoruz. Program,
  şehir ve konaklama tercihine göre her kalemi tek tek hesaplıyor; ödeme takvimini başvurudan önce
  netleştiriyoruz.</p>"""),
],

# =====================================================================
'tools/pages_content2.py': [
# --- ANA REHBER ---
("""  <p>Macaristan, Avrupa Birliği üyesi bir ülkede İngilizce okuyup uluslararası geçerliliği olan bir
  diploma almanın en pratik yollarından biri. Üniversiteler YKS puanı istemiyor, kendi kabul sürecini
  yürütüyor; lisans 3–4 yıl, yüksek lisans 2 yıl, tıp ve diş hekimliği gibi bütünleşik programlar ise
  5–6 yıl sürüyor. Eğitim ve yaşam giderleri birlikte yıllık 8.500 – 14.000 € aralığında kalıyor.
  <b>Hun Education olarak</b> 20 üniversitede toplam 490 İngilizce program için başvuru
  yürütüyoruz.</p>""",
 """  <p>Macaristan, Avrupa Birliği üyesi bir ülkede İngilizce eğitim alarak uluslararası geçerliliğe
  sahip bir diploma edinmek isteyen öğrenciler için güçlü bir seçenek sunuyor. Üniversiteler YKS puanı
  talep etmiyor; başvuruları kendi kabul süreçleri üzerinden değerlendiriyor. Lisans programları 3–4
  yıl, yüksek lisans programları 2 yıl, tıp ve diş hekimliği gibi bütünleşik programlar ise 5–6 yıl
  sürüyor. Eğitim ve yaşam giderleri birlikte yıllık 8.500 – 14.000 € aralığında kalıyor.</p>

  <p><b>Hun Education olarak,</b> 20 seçkin üniversitede sunulan 490 İngilizce program arasından
  öğrencilerimizin hedeflerine en uygun seçeneği belirliyor; başvurudan kabul ve vize sürecine kadar
  her adımda yanlarında oluyoruz.</p>"""),

# --- ÜNİVERSİTELER ---
("""  <p>Hun Education aracılığıyla Macaristan'daki <b>{len(UNIS)} üniversiteye</b> başvuru yapılabiliyor;
  sekiz farklı şehre dağılıyorlar. En geniş program çeşitliliği Budapeşte'de; Debrecen, Szeged ve
  Pécs ise benzer akademik kaliteyi daha düşük yaşam maliyetiyle sunuyor. Tüm listede hazırlık
  yılından tıp ve pilotaja <b>{sum(u["programSayisi"] for u in UNIS)} İngilizce program</b>
  bulunuyor.</p>""",
 """  <p>Macaristan'ın sekiz farklı şehrinde, uluslararası öğrencilere kapılarını açan
  <b>{len(UNIS)} üniversite</b> bulunuyor. Program çeşitliliği açısından Budapeşte ilk sırada yer
  alırken Debrecen, Szeged ve Pécs benzer akademik kaliteyi daha uygun yaşam maliyetiyle sunuyor.
  Hazırlık programlarından tıp ve pilotaja uzanan geniş bir yelpazede toplam
  <b>{sum(u["programSayisi"] for u in UNIS)} İngilizce program</b> yer alıyor.</p>

  <p><b>Hun Education olarak,</b> bu üniversitelerin tamamına başvuru gönderiyoruz. Akademik
  geçmişinizi ve hedeflerinizi değerlendirerek profilinize en uygun kurumları belirliyor, tercih
  listenizi birlikte oluşturuyoruz.</p>"""),
],

# =====================================================================
'tools/pages_content3.py': [
# --- HAKKIMIZDA ---
("""  <p>Hun Education, 1999'dan beri yalnızca Macaristan'a odaklanan bir akademik danışmanlık şirketidir
  ve Macaristan'daki ilk Türk eğitim danışmanlığı kurumudur. Merkez ofis Budapeşte'de; Ankara,
  İstanbul, İzmir, Bursa ve Pécs'te temsilcilikler bulunuyor. Hizmet kapsamı program seçiminden
  başvuruya, vizeden konaklama ve şehir oryantasyonuna kadar uzanır.</p>""",
 """  <p>Hun Education, 1999 yılından bu yana yalnızca Macaristan'da eğitim alanına odaklanan bir
  akademik danışmanlık kurumudur. Ülkede faaliyet gösteren ilk Türk eğitim danışmanlığı şirketi olarak
  yirmi beş yılı aşkın bir deneyime sahibiz.</p>

  <p>Merkez ofisimiz Budapeşte'de bulunuyor; Ankara, İstanbul, İzmir, Bursa ve Pécs'te temsilciliklerimiz
  aracılığıyla öğrencilerimize hizmet veriyoruz. Program seçiminden başvuruya, vize sürecinden konaklama
  ve şehir oryantasyonuna kadar her aşamada öğrencilerimizin yanında oluyoruz.</p>"""),
],

# =====================================================================
'tools/pages_content5.py': [
# --- NEDEN MACARİSTAN ---
("""  <p>Yurt dışında okumaya karar veren öğrencilerin önündeki en büyük soru genellikle şu oluyor: kaliteli
  bir eğitimi makul bir bütçeyle nerede alabilirim? Macaristan son yıllarda bu sorunun en güçlü
  cevaplarından biri hâline geldi. Eğitim baştan sona İngilizce yürüyor, YKS puanı istenmiyor ve bir
  akademik yılın toplam maliyeti Batı Avrupa'da ödeyeceğinizin yaklaşık yarısı kadar. <b>Hun Education
  olarak</b> 1999'dan bu yana yalnızca bu ülkeye odaklandık; kataloğumuzda 20 üniversitede
  <b>490 İngilizce program</b> bulunuyor.</p>""",
 """  <p>Yurt dışında eğitim planlayan öğrencilerin en önemli sorularından biri şu: Kaliteli bir eğitimi
  ulaşılabilir bir bütçeyle hangi ülkede alabilirim? Macaristan; İngilizce eğitim seçenekleri, YKS puanı
  gerektirmeyen başvuru süreci ve Batı Avrupa'ya kıyasla çok daha avantajlı eğitim ve yaşam
  maliyetleriyle güçlü bir alternatif sunuyor.</p>

  <p><b>Hun Education olarak</b> 1999'dan bu yana yalnızca Macaristan'da eğitim alanına odaklanıyoruz.
  20 seçkin üniversitede sunulan <b>490 İngilizce program</b> arasından öğrencilerimizin hedeflerine en
  uygun seçeneği belirliyor; başvurudan kabul ve vize sürecine kadar her adımda yanlarında
  oluyoruz.</p>"""),

# --- YÜKSEK LİSANS ---
("""  <p>Lisansını tamamlamış ve kariyerine Avrupa'da devam etmek isteyen öğrenciler için Macaristan
  oldukça pratik bir seçenek sunuyor. Yüksek lisans programları iki yıl sürüyor, 120 AKTS taşıyor ve
  baştan sona İngilizce yürüyor. Ücretler çoğunlukla <b>yıllık 4.000 – 6.000 €</b> bandında; katalog
  genelinde üniversiteye ve alana göre 3.200 € ile 14.000 € arasında değişiyor. Kabul için alanınızla
  ilgili tanınan bir lisans diploması, çoğu üniversitede de IELTS 6,5 isteniyor. Başvurunuzu Eylül
  dönemi için Nisan–Haziran arasında yapabilir, birçok programda Şubat dönemini de
  değerlendirebilirsiniz.</p>""",
 """  <p>Macaristan, lisans eğitimini tamamlamış ve kariyerine Avrupa'da devam etmek isteyen öğrenciler
  için güçlü bir yüksek lisans seçeneği sunuyor. Programlar iki yıl sürüyor, 120 AKTS kredi taşıyor ve
  baştan sona İngilizce yürütülüyor. Öğrenim ücretleri çoğunlukla <b>yıllık 4.000 – 6.000 €</b>
  aralığında; üniversiteye ve alana göre bu tutar 3.200 € ile 14.000 € arasında değişebiliyor.</p>

  <p>Kabul için alanınızla ilgili tanınan bir lisans diploması, çoğu üniversitede ise IELTS 6,5
  düzeyinde İngilizce yeterliliği isteniyor. Eylül dönemi başvuruları Nisan–Haziran aralığında
  tamamlanıyor; birçok program Şubat döneminde de öğrenci kabul ediyor.</p>

  <p><b>Hun Education olarak,</b> transkriptinizi inceleyerek hangi programlara uygun olduğunuzu
  belirliyor ve motivasyon mektubunuzu birlikte hazırlıyoruz. Başvurudan kabule kadar süreci sizin
  adınıza yürütüyoruz.</p>"""),
],

# =====================================================================
'tools/pages_content6.py': [
# --- TIP ---
("""  <p>Macaristan üniversiteleri, tıp eğitimi için Avrupa'daki en güçlü seçenekler arasında yer alıyor ve
  her yıl daha fazla Türk öğrenci bu yolu tercih ediyor. Eğitim baştan sona İngilizce yürüyor, YKS puanı
  istenmiyor ve altı yıllık bütünleşik program <b>üç köklü üniversitede</b> veriliyor: Budapeşte'de
  Semmelweis, ardından Pécs ve Szeged. <b>Hun Education olarak</b> bu başvuruları yıllardır yürütüyor,
  giriş sınavı hazırlığından vize aşamasına kadar öğrencilerimize eşlik ediyoruz.</p>""",
 """  <p>Macaristan, İngilizce tıp eğitimi almak isteyen öğrenciler için Avrupa'nın öne çıkan
  ülkelerinden biri. YKS puanı gerektirmeyen altı yıllık bütünleşik tıp programları; Budapeşte'deki
  Semmelweis Üniversitesi ile Pécs ve Szeged Üniversitelerinde sunuluyor.</p>

  <p><b>Hun Education olarak,</b> Macaristan'daki tıp eğitimi başvurularında yıllara dayanan
  deneyimimizle öğrencilerimizin yanındayız. Üniversite seçiminden giriş sınavına hazırlığa, başvuru
  belgelerinden vize sürecine kadar her aşamayı planlıyor ve öğrencilerimize hedeflerine giden yolda
  profesyonel danışmanlık sağlıyoruz.</p>"""),

# --- PİLOTAJ ---
("""  <p>Macaristan üniversiteleri, uluslararası öğrencilere yüzlerce bölüm seçeneği sunuyor; ancak son
  yıllarda pilotaj eğitimi bunların arasında ayrı bir yere oturdu. Bunun sebebi basit: Macaristan'da
  uçuş eğitimini üniversite diplomasıyla aynı programda alıyor, mezun olduğunuzda hem lisansınızı hem
  diplomanızı birlikte taşıyorsunuz. <b>Hun Education olarak</b> her yıl pilotluk okumak isteyen
  öğrencilerimizin başvurularını yürütüyor, sağlık sertifikasından uçuş saatlerine kadar süreci
  baştan sona birlikte planlıyoruz.</p>""",
 """  <p>Macaristan üniversiteleri, uluslararası öğrencilere yüzlerce İngilizce program sunarken pilotaj
  eğitimi son yılların en çok ilgi gören seçeneklerinden biri olarak öne çıkıyor. Öğrenciler, akademik
  lisans eğitimi ile uygulamalı uçuş eğitimini aynı program kapsamında tamamlayarak mezuniyetlerinde
  hem üniversite diplomasına hem de profesyonel pilotluk kariyerine yönelik gerekli yetkinliklere
  sahip oluyor.</p>

  <p><b>Hun Education olarak,</b> pilotaj eğitimi almak isteyen öğrencilerimizin üniversite
  başvurularını her yıl titizlikle yürütüyoruz. Uygun programın belirlenmesinden sağlık sertifikasına,
  kabul sürecinden uçuş eğitimine kadar tüm aşamaları öğrencilerimizle birlikte planlıyor ve sürecin
  her adımında yanlarında oluyoruz.</p>"""),
],

# =====================================================================
'tools/pages_content7.py': [
# --- YAŞAM ---
("""  <p>Macaristan'da öğrenci olarak yaşamak aylık yaklaşık <b>480 – 1.000 €</b> tutuyor ve bu aralığı
  konaklama belirliyor. İlk ay akademik değil idari: ikamet kaydı, üniversite kaydı, banka hesabı ve
  ulaşım kartı. İngilizce diplomanız ve üniversite şehirlerindeki günlük hayat için yeterli; ötesinde
  Macarca işinizi kolaylaştırıyor.</p>""",
 """  <p>Macaristan'da öğrenci olarak yaşamanın aylık maliyeti yaklaşık <b>480 – 1.000 €</b> arasında
  değişiyor ve bu aralığı belirleyen temel kalem konaklama tercihi oluyor. Ülkeye vardıktan sonraki
  ilk ay ise akademik olmaktan çok idari geçiyor; ikamet kaydı, üniversite kaydı, banka hesabı açılışı
  ve ulaşım kartı bu dönemde tamamlanıyor.</p>

  <p><b>Hun Education olarak,</b> Budapeşte ekibimizle öğrencilerimizi havalimanında karşılıyor ve
  yerleşim sürecinin tamamında yanlarında oluyoruz. Konaklama başvurusundan resmî işlemlere kadar ilk
  ayın her adımını birlikte planlıyoruz.</p>"""),

# --- ÖĞRENCİ GÖRÜŞLERİ ---
("""  <p>Bir ülkeyi anlatan en iyi kaynak, orada okuyan öğrencilerin kendisidir. Aşağıdaki yorumlar
  başvurusunu birlikte yürüttüğümüz öğrencilere ait ve izinleriyle, kendi tercihleri doğrultusunda ad
  ya da baş harfle yayınlanıyor. Budapeşte, Debrecen ve Pécs'te tıp, mühendislik, medya ve dil
  bilimleri okuyan arkadaşlarınızın deneyimlerini burada okuyabilirsiniz.</p>""",
 """  <p>Bir ülkede eğitim almanın nasıl bir deneyim olduğunu en iyi, orada okuyan öğrenciler anlatır.
  Bu sayfada Budapeşte, Debrecen ve Pécs'te tıp, mühendislik, medya ve dil bilimleri okuyan
  öğrencilerimizin kendi cümleleriyle paylaştığı deneyimleri bulacaksınız.</p>

  <p>Aşağıdaki yorumlar, başvuru süreçlerini birlikte yürüttüğümüz öğrencilere ait. Tamamı
  öğrencilerimizin izniyle ve kendi tercihleri doğrultusunda ad ya da baş harf kullanılarak
  yayımlanıyor.</p>"""),
],
}

for yol, ciftler in R.items():
    s = io.open(yol, encoding='utf-8').read()
    n = 0
    for a, b in ciftler:
        if a in s:
            s = s.replace(a, b, 1); n += 1
        else:
            print('  ! eslesmedi %s :: %s' % (yol, ' '.join(a.split())[:70]))
    io.open(yol, 'w', encoding='utf-8').write(s)
    print('%-26s %d giris yeniden yazildi' % (yol, n))
