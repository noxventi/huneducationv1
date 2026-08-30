# -*- coding: utf-8 -*-
"""Kalan Turkce rehber sayfalari: yeniden yazim ve sadelestirme.

Uygulanan olcut, canlidaki huneducation.com metinlerinden cikarildi:
  - Paragraf baglamla acilir, rakamla degil.
  - Cumleler akar; iki nokta ve noktali virgulle parcalanmaz.
  - "Hun Education olarak ..." sesi en az bir kez gecer.
  - Okura dogrudan hitap edilir ("endiselenmeyin", "unutmayin").
  - Her sayfa bir "Sonuc" paragrafiyla toparlanir.

Yapi tarafinda bolum sayisi dusuruluyor; ayni konuyu iki basliga bolen
yerler birlestiriliyor.
"""
import io

R = {
# =====================================================================
# ANA REHBER
# =====================================================================
'tools/pages_content2.py': [
# icindekiler: 9 -> 6
("""{toc([('kisa-cevap','Kısa cevap'),('neden','Neden Macaristan?'),('sistem','Eğitim sistemi ve dereceler'),
      ('dil','Eğitim dili'),('sehirler','Şehirler'),('vize','Vize ve oturum'),
      ('denklik','Denklik ve mezuniyet sonrası'),('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}""",
 """{toc([('neden','Neden Macaristan?'),('sistem','Eğitim sistemi ve dereceler'),
      ('sehirler','Hangi şehirde okumalı?'),('vize','Vize, oturum ve denklik'),
      ('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}"""),

# kisa cevap
("""<section id="kisa-cevap" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Macaristan, AB üyesi bir ülkede İngilizce okuyup Avrupa'da geçerli bir diploma almanın en
  pratik yollarından biri. <b>YKS şartı yok</b>; üniversiteler kendi değerlendirmesini yapıyor.
  Lisans 3–4 yıl, yüksek lisans 2 yıl, tıp ve diş hekimliği gibi bütünleşik programlar 5–6 yıl
  sürüyor ve eğitim ile yaşam giderleri birlikte yıllık 8.500 – 14.000 € aralığında kalıyor.
  Kataloğumuzda 20 üniversitede 490 İngilizce program var.</p>
</section>""",
 """<section id="giris" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Macaristan, Avrupa Birliği üyesi bir ülkede İngilizce okuyup uluslararası geçerliliği olan bir
  diploma almanın en pratik yollarından biri. Üniversiteler YKS puanı istemiyor, kendi kabul sürecini
  yürütüyor; lisans 3–4 yıl, yüksek lisans 2 yıl, tıp ve diş hekimliği gibi bütünleşik programlar ise
  5–6 yıl sürüyor. Eğitim ve yaşam giderleri birlikte yıllık 8.500 – 14.000 € aralığında kalıyor.
  <b>Hun Education olarak</b> 20 üniversitede toplam 490 İngilizce program için başvuru
  yürütüyoruz.</p>
</section>

<p>Bu sayfada Macaristan'daki eğitim sisteminin nasıl işlediğini, hangi şehirde neyin öne çıktığını,
öğrenci vizesinin nasıl alındığını ve diplomanızın Türkiye'de ne anlama geldiğini anlatıyoruz.</p>"""),

# neden bolumu: liste yerine akici anlatim + tek kanit bandi
("""<h2 id="neden">Neden Macaristan?</h2>
{stats([('490', 'İngilizce program'),
        ('20', 'Üniversite'),
        ('8.500 €', 'Bir yılın alt bütçesi'),
        ('YKS yok', 'Üniversite kendi değerlendirmesini yapar')])}
<p>Macaristan'ı Türk öğrenciler için öne çıkaran şey tek bir avantaj değil, birkaç faktörün
birlikte çalışmasıdır:</p>
<ul>
  <li><b>Avrupa'da diploma, ölçülü bütçe.</b> Batı Avrupa'ya kıyasla belirgin şekilde düşük öğrenim
  ücreti ve yaşam maliyeti.</li>
  <li><b>Geniş İngilizce program yelpazesi.</b> Tıptan pilotaja, mühendislikten sanata kadar
  uluslararası öğrenciye açık programlar.</li>
  <li><b>Köklü üniversite geleneği.</b> Pécs Üniversitesi 1367'de kuruldu, Semmelweis'te tıp eğitimi
  1769'a dayanıyor; Macar asıllı bilim insanları bugüne kadar 16 Nobel Ödülü kazandı.</li>
  <li><b>Merkezî konum.</b> Viyana, Bratislava ve Prag'a kara yoluyla birkaç saat mesafe.</li>
  <li><b>Yerleşik Türk öğrenci topluluğu.</b> Macaristan'da 40 bine yakın uluslararası öğrenci
  okuyor; Budapeşte, Debrecen ve Pécs'te güçlü bir Türk öğrenci ağı sizi bekliyor.</li>
</ul>
{inline_cta("Bu programlardan hangisine gerçekçi şansınız var? İlk görüşmede söyleyelim.")}""",
 """<h2 id="neden">Neden Macaristan?</h2>
<p>Macaristan'ı Türk öğrenciler için öne çıkaran şey tek bir avantaj değil, birkaç etkenin bir arada
çalışması. Bunların başında bütçe geliyor: öğrenim ücretleri de yaşam giderleri de Batı Avrupa'nın
belirgin şekilde altında seyrediyor ve bir akademik yılı toplamda 8.500 – 14.000 € bandında tutuyor.</p>

<p>İkinci etken program çeşitliliği. Tıptan pilotaja, mühendislikten sanata kadar uluslararası
öğrenciye açık geniş bir yelpaze var ve bunların tamamı İngilizce yürüyor. Üstelik bu programlar yeni
kurulmuş değil; Pécs Üniversitesi 1367'de kuruldu, Semmelweis'te tıp eğitimi 1769'a dayanıyor ve Macar
asıllı bilim insanları bugüne kadar 16 Nobel Ödülü kazandı.</p>

<p>Üçüncüsü ise konum ve topluluk. Viyana, Bratislava ve Prag kara yoluyla birkaç saat uzaklıkta;
ülkede 40 bine yakın uluslararası öğrenci okuyor ve Budapeşte, Debrecen ile Pécs'te yerleşmiş bir Türk
öğrenci ağı sizi bekliyor. Yani gittiğinizde yalnız kalmıyorsunuz.</p>
{inline_cta("Bu programlardan hangisine gerçekçi şansınız var? İlk görüşmede söyleyelim.")}"""),

# egitim dili bolumunu sistem bolumune tasi
("""<h2 id="dil">Eğitim dili</h2>
<p>Uluslararası programlar İngilizce yürütülür; başvuru için Macarca bilmek gerekmez. Lisansta en az
B2 seviyesi beklenir; yüksek lisansta IELTS 6,5 isteyen üniversiteler var. Belgesi olmayan adaylar
üniversitelerin İngilizce Dil Hazırlık programına başvurabilir.</p>
<p>Macarca, günlük hayat ve staj olanakları açısından avantaj sağlar; birçok üniversite ücretsiz ya da
düşük ücretli başlangıç seviyesi Macarca dersleri sunar.</p>""",
 """<h3>Eğitim dili</h3>
<p>Uluslararası programların tamamı İngilizce yürütülüyor ve başvuru için Macarca bilmenize gerek yok.
Lisansta pratikte B2 seviyesi bekleniyor, yüksek lisansta IELTS 6,5 isteyen üniversiteler var; ancak
okulların çoğu belge yerine kendi mülakatını yapıyor. Seviyeniz yetmiyorsa üniversitelerin İngilizce
hazırlık programlarına başvurabilirsiniz. Macarca ise günlük hayat ve staj olanakları açısından
avantaj sağlıyor; birçok üniversite başlangıç seviyesi Macarcayı ücretsiz veya çok düşük ücretle
veriyor.</p>"""),

# sehirler
("""<h2 id="sehirler">Şehirler</h2>""",
 """<h2 id="sehirler">Hangi şehirde okumalı?</h2>"""),

# vize + denklik birlestirme
("""<h2 id="denklik">Denklik ve mezuniyet sonrası</h2>
<p>Diplomanızı Türkiye'de kullanmak istiyorsanız YÖK denklik sürecinden geçmeniz gerekir. Denklik;
üniversitenin tanınırlığı, programın içeriği, eğitim süresi ve mezuniyet koşullarına göre
değerlendirilir; bazı alanlarda ek sınav istenebilir.</p>""",
 """<h3>Denklik ve mezuniyet sonrası</h3>
<p>Diplomanızı Türkiye'de kullanmak istiyorsanız YÖK denklik sürecinden geçmeniz gerekiyor. Denklik;
üniversitenin tanınırlığı, programın içeriği, eğitim süresi ve mezuniyet koşulları üzerinden
değerlendiriliyor ve bazı alanlarda ek sınav istenebiliyor.</p>"""),

("""<h2 id="vize">Vize ve oturum</h2>""",
 """<h2 id="vize">Vize, oturum ve denklik</h2>"""),
],

# =====================================================================
# BAŞVURU ŞARTLARI
# =====================================================================
'tools/pages_content.py': [
("""<section id="kisa-cevap" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Başvuru için apostilli diploma, İngilizce transkript, pasaport fotokopisi ve İngilizce
  özgeçmiş gerekir; banka dökümü başvuruda değil vize aşamasında istenir. Lisansta pratikte B2
  İngilizce beklenir ama üniversitelerin çoğu dil belgesi yerine kendi mülakatını yapar. Yaş sınırı
  lisansta 25, yüksek lisansta 28; tıpta sınır yok. Eylül dönemi başvuruları Nisan ile Haziran
  arasında, Şubat dönemi başvuruları Ekim sonu ile Kasım arasında kapanır.</p>
</section>""",
 """<section id="giris" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Macaristan'a başvuru süreci, ilk bakışta göründüğünden çok daha sade ilerliyor. Apostilli
  diplomanız, İngilizce transkriptiniz, pasaport fotokopiniz ve İngilizce özgeçmişiniz dosyanın
  tamamını oluşturuyor; banka dökümü başvuruda değil, vize aşamasında isteniyor. Lisansta pratikte B2
  İngilizce bekleniyor ama üniversitelerin çoğu dil belgesi yerine kendi mülakatını yapıyor.
  <b>Hun Education olarak</b> bu dosyayı sizin adınıza kuruyor, eksik kalan noktaları başvurudan önce
  tamamlıyoruz.</p>
</section>

<p>Bu sayfada hangi belgelerin istendiğini, dil şartının gerçekte ne olduğunu, giriş sınavı olan
bölümleri ve başvuru takvimini adım adım anlatıyoruz.</p>"""),

("""<h2 id="belgeler">Gerekli belgeler</h2>
<p>Aşağıdaki belgeler her başvuruda isteniyor. Programa göre ek belge çıkabilir; kabul şartlarını
başvurudan önce birlikte gözden geçiriyoruz.</p>""",
 """<h2 id="belgeler">Gerekli belgeler</h2>
<p>Aşağıdaki belgeler her başvuruda isteniyor. Programa göre ek belge çıkabiliyor; kabul şartlarını
başvurudan önce birlikte gözden geçirdiğimiz için eksik bir dosyayla yola çıkmıyorsunuz.</p>"""),

("""<h2 id="dil">Dil yeterliliği</h2>
<p>Kataloğumuzdaki neredeyse her program İngilizce yürüyor. Adayların en çok yanıldığı nokta şu:
<b>Macaristan'da çoğu üniversite dil belgesi istemiyor</b>, çünkü kendi mülakatını ya da çevrim içi
sınavını yapıyor. Bazı okullar IELTS istiyor; üniversiteye ve bölüme göre 5, 6 veya 6,5.</p>""",
 """<h2 id="dil">Dil yeterliliği</h2>
<p>Kataloğumuzdaki neredeyse her program İngilizce yürüyor, dolayısıyla dil bu başvurunun temel
konusu. Ancak burada adayların çoğunun bilmediği bir kolaylık var: <b>Macaristan'da üniversitelerin
büyük bölümü dil belgesi istemiyor</b>, bunun yerine kendi mülakatını ya da çevrim içi sınavını
yapıyor. Belge isteyen okullarda ise üniversiteye ve bölüme göre IELTS 5, 6 veya 6,5 aranıyor.</p>"""),

("""<h2 id="uygunluk">Belgelerden önce: uygun musunuz?</h2>
<p>İyi haber şu: çoğu aday zaten uygun. Yine de üç başlık evraktan önce netleşsin ki boşuna
hazırlık yapmayasınız.</p>""",
 """<h2 id="uygunluk">Belgelerden önce: uygun musunuz?</h2>
<p>İyi haber şu ki adayların büyük çoğunluğu zaten uygun. Yine de üç başlığı evrak hazırlığına
başlamadan netleştirmenizde fayda var; böylece boşuna zaman kaybetmiyorsunuz.</p>"""),

("""<h2 id="takvim">Başvuru takvimi</h2>
<p>Yılda iki başlangıç dönemi var, yani bir dönemi kaçırsanız bile altı ay sonra yeniden
başlayabilirsiniz. Ama kontenjan dolduğunda dönem ilan edilen tarihten önce kapanıyor: erken
başvuran aday hem daha çok programdan seçiyor hem de daha rahat bir vize takvimi yakalıyor.</p>""",
 """<h2 id="takvim">Başvuru takvimi</h2>
<p>Macaristan'da yılda iki başlangıç dönemi bulunuyor; yani bir dönemi kaçırsanız bile altı ay sonra
yeniden başlayabiliyorsunuz. Yine de erken başvurmanızı öneriyoruz, çünkü kontenjan dolduğunda dönem
ilan edilen tarihten önce kapanabiliyor. Erken başvuran aday hem daha geniş bir program listesinden
seçiyor hem de vize takvimini rahat rahat planlıyor.</p>"""),
],

# =====================================================================
# MALİYET
# =====================================================================
'tools/pages_content.py#2': [
("""<section id="kisa-cevap" class="answer">
  <span class="answer__label">Kısa cevap</span>""",
 """<section id="giris" class="answer">
  <span class="answer__label">Kısa cevap</span>"""),
],

# =====================================================================
# ÜNİVERSİTELER
# =====================================================================
'tools/pages_content2.py#2': [
("""<p>Aşağıdaki tablo şehre göre sıralanmıştır. “Öne çıkan alanlar” sütunu, o üniversitede kataloğumuzda
program bulunan başlıca alanları gösterir; kurumun tüm fakülte yapısı değildir.</p>""",
 """<p>Aşağıdaki tablo şehre göre sıralandı. “Öne çıkan alanlar” sütunu, o üniversitede kataloğumuzda
program bulunan başlıca alanları gösteriyor; kurumun tüm fakülte yapısını değil.</p>"""),
],
}


def uygula():
    for anahtar, ciftler in R.items():
        yol = anahtar.split('#')[0]
        s = io.open(yol, encoding='utf-8').read()
        n = 0
        for a, b in ciftler:
            if a in s:
                s = s.replace(a, b, 1); n += 1
            else:
                print('  ! eslesmedi %s :: %s' % (yol, ' '.join(a.split())[:68]))
        io.open(yol, 'w', encoding='utf-8').write(s)
        print('%-30s %d degisiklik' % (anahtar, n))


uygula()
