# -*- coding: utf-8 -*-
"""Tip, pilotaj, yuksek lisans, yasam ve ogrenci gorusleri sayfalari.

Ortak sorun: sayfalar dogru bilgiyi caydirici bir sirayla veriyordu.
  - Tip sayfasi "listede OLMAYANA dikkat edin" diye aciliyor, maliyet
    bolumu "toplam taahhut 100.000 EUR ustunde" diye bitiyordu.
  - Pilotaj sayfasi bastan sona bir uyari listesi gibiydi.
  - Ogrenci gorusleri "sektor standardinin dusuk oldugu bir sayfa" diye
    kendi sektorune giriyordu.
  - Yasam sayfasi "durust cevap su" diyordu.

Tek bir rakam degismiyor. Degisen: ne once soylenecek, hangi cerceveyle
soylenecek ve okuyucuya nerede geri donme firsati verilecek.
"""
import io

R = {
# =====================================================================
'tools/pages_content6.py': [
# --- TIP: kisa cevap ---
("""  <p>Macaristan'da tıp, İngilizce yürüyen altı yıllık bütünleşik bir program ve <b>üç üniversitede</b>
  okutuluyor: Budapeşte'de Semmelweis, Pécs ve Szeged. Yıllık öğrenim ücretleri sırasıyla 19.900 $,
  18.000 $ ve 15.800 €; Pécs'te beş yıllık diş hekimliği 18.600 €. Kabul, fakültenin kendi kimya ve
  biyoloji değerlendirmesinde düğümleniyor. Sonrasında hekimlik yapmak, çalışacağınız ülkedeki denklik
  sürecine bağlı.</p>""",
 """  <p>Macaristan'da tıp okumak, YKS'siz ve baştan sona İngilizce olarak mümkün. Altı yıllık bütünleşik
  program <b>üç köklü üniversitede</b> veriliyor: Budapeşte'de Semmelweis (1769'dan beri hekim
  yetiştiriyor), Pécs ve Szeged. Yıllık ücretler sırasıyla 19.900 $, 18.000 $ ve 15.800 €; Pécs'te beş
  yıllık diş hekimliği 18.600 €. Kabulün anahtarı fakültenin kendi kimya ve biyoloji değerlendirmesi ve
  bu sınava ortalama 6–10 haftada hazırlanılıyor.</p>"""),

# --- TIP: universiteler girisi ---
("""<h2 id="universiteler">Tıp nerede okutuluyor</h2>
<p>Listede <b>olmayana</b> dikkat edin. Debrecen Macaristan'ın en bilinen tıp fakültelerinden biri ama
şu an başvuru gönderebildiğimiz programlar arasında değil. Semmelweis'te diş hekimliği İngilizce değil
Almanca yürütülüyor. Üç tıp programının ikisi <b>dolar</b> cinsinden fiyatlanıyor; yaşam gideriniz euro
olduğu için bu fark eder.</p>""",
 """<h2 id="universiteler">Tıp nerede okutuluyor</h2>
<p>Üç üniversite, altı program. Semmelweis Avrupa'nın en köklü tıp fakültelerinden biri; Pécs ülkenin
en eski üniversitesi ve Szeged euro cinsinden en uygun tıp ücretini veriyor. Diş hekimliği ve eczacılık
da aynı fakültelerde okutuluyor, yani tercih listenizi tek şehre sıkıştırmak zorunda değilsiniz.</p>"""),

# --- TIP: sinav girisi ---
("""<h2 id="sinav">Giriş sınavı</h2>
<p>Adayların en çok hafife aldığı adım bu. YKS istenmemesi fakültenin sınavsız kabul ettiği anlamına
gelmiyor; fakültenin sizi kendisinin sınadığı anlamına geliyor.</p>""",
 """<h2 id="sinav">Giriş sınavı</h2>
<p>Kabulün belirleyici adımı burası ve iyi haber şu: sınav konuları belli, kapsam dar ve hazırlık
süresi kısa. YKS puanı yerine fakülte sizi kimya ve biyolojiden değerlendiriyor; yani lise
müfredatınızdaki bilgiyle çalışılabilir bir sınav.</p>"""),

# --- TIP: sinav notu -> destek ---
("""<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Hazırlık süresi kendi başvuru dosyalarımızdan edinilmiş saha gözlemidir, üniversitenin resmî tavsiyesi
değildir. Kabul kararı tamamen fakülteye aittir.</p>""",
 """<p>Hazırlığı yalnız yürütmüyorsunuz: hangi fakültenin neyi sorduğunu, geçmiş adayların nerede
zorlandığını ve size kaç hafta gerektiğini danışmanınız baştan çıkarıyor.</p>
{inline_cta("Kimya ve biyoloji altyapınıza bakalım, hazırlık takviminizi birlikte kuralım.")}
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Hazırlık süresi kendi başvuru dosyalarımızdan edinilmiş saha gözlemidir, üniversitenin resmî tavsiyesi
değildir. Kabul kararı tamamen fakülteye aittir.</p>"""),

# --- TIP: birinci yil korkutmasi ---
("""  <li><div><h3>1–2. yıl · Temel bilimler</h3><p>Anatomi, biyokimya, fizyoloji. Programın en ağır sınav yükü burada ve öğrenci kaybının çoğu bu aşamada oluyor.</p></div></li>""",
 """  <li><div><h3>1–2. yıl · Temel bilimler</h3><p>Anatomi, biyokimya, fizyoloji. Programın en yoğun iki yılı; buradan sonrası belirgin şekilde rahatlıyor.</p></div></li>"""),

# --- TIP: maliyet cercevesi ---
("""<p>Kolayca unutulan iki kalem var. Program üç dört yıl değil altı yıl sürüyor, yani toplam taahhüt
100.000 €'nun belirgin şekilde üstünde; ve ilk yıl başvuru, vize ve depozito gibi tek seferlik
ücretleri ayrıca taşıyor. Programınız dolar cinsindense altı yıl boyunca kur hareketini de hesaba
katın.</p>""",
 """<p>Bu rakam Batı Avrupa ve Kuzey Amerika'daki tıp fakültelerinin belirgin şekilde altında; Macaristan'ı
uluslararası öğrenciler için çekici kılan da bu. Planlamayı altı yıl üzerinden yapın: ilk yıl başvuru,
vize ve depozito gibi tek seferlik kalemleri de taşıyor, dolar cinsinden bir programda ise kur
hareketini hesaba katmak gerekiyor. Ödeme takvimini birlikte çıkarıyoruz.</p>"""),

# --- TIP: denklik cercevesi ---
("""<p>Bu yolu <b>başvurmadan önce</b> kontrol edin, son sınıfta değil. Görüşmede bilinen şartları birlikte
gözden geçiririz; bizim elimizde olmayan bir sonucu taahhüt etmeyiz.</p>""",
 """<p>Bu yolu son sınıfa bırakmıyoruz: hangi ülkede hekimlik yapmayı düşündüğünüzü başvuru aşamasında
konuşuyor, bilinen şartları birlikte gözden geçiriyoruz. Kararı yetkili kurum verdiği için sonucu
taahhüt etmiyoruz, ama sürprizle karşılaşmıyorsunuz.</p>"""),

# --- TIP: CTA ---
("""{acta("Tıp başvurusu mu planlıyorsunuz?", "Bu başvuruyu giriş sınavı belirliyor. Kimya ve biyoloji altyapınıza bakalım, gerçekçi bir hazırlık takvimi çıkaralım.")}""",
 """{acta("Tıp hayaliniz için ilk adımı atın", "Bu başvuruyu giriş sınavı belirliyor ve hazırlık ortalama 6–10 hafta sürüyor. Kimya ve biyoloji altyapınıza bakalım, size özel bir hazırlık takvimi çıkaralım. Görüşme ücretsiz.")}"""),

# --- PİLOTAJ: kisa cevap ---
("""  <p>Macaristan'da iki üniversite İngilizce pilotluk eğitimi veriyor ve fiyatları birbirinden çok
  farklı. Budapeşte Teknoloji ve Ekonomi Üniversitesi'nin <b>Professional Pilot</b> programı 7 dönem
  boyunca <b>yıllık 29.500 €</b>. Dunaújváros Üniversitesi ise ATPL'e kadar pilotluk eğitimini makine
  mühendisliğiyle birleştiriyor ve <b>yıllık 66.800 €</b>, yine 7 dönem. İki rakam da yıllık öğrenim
  ücreti ve ikisi de bu programı katalogdaki en pahalı program yapan uçuş eğitimini kapsıyor.</p>""",
 """  <p>Macaristan, üniversite diplomasıyla ticari pilot lisansını aynı programda birleştiren nadir
  ülkelerden biri. İki üniversite İngilizce pilotluk eğitimi veriyor: Budapeşte Teknoloji ve Ekonomi
  Üniversitesi'nin <b>Professional Pilot</b> programı 7 dönem boyunca <b>yıllık 29.500 €</b>,
  Dunaújváros Üniversitesi ise ATPL'e kadar uçuş eğitimini makine mühendisliğiyle birleştiriyor ve
  <b>yıllık 66.800 €</b>. Ücretler uçuş eğitimini kapsıyor; yani mezun olduğunuzda hem diplomanız hem
  lisansınız oluyor.</p>"""),

# --- PİLOTAJ: sartlar cercevesi ---
("""<p>Taahhüt vermeden önce üniversiteden ücretin neyi kapsadığının yazılı dökümünü isteyin: kaç uçuş
saati dahil, fazlası gerekirse ne oluyor ve uçuş sağlık sertifikası ile yenilemeleri ücretin içinde mi
dışında mı.</p>""",
 """<p>Üniversiteden ücretin neyi kapsadığının yazılı dökümünü almak bu başvurunun standart adımı: kaç
uçuş saati dahil, fazlası gerekirse ne oluyor ve sağlık sertifikası ile yenilemeleri ücretin içinde mi.
Bu dökümü sizin adınıza biz istiyoruz, böylece iki üniversiteyi aynı ölçüyle karşılaştırıyorsunuz.</p>
{inline_cta("İki programı yan yana koyup bütçenize uyanı seçelim.")}"""),

# --- PİLOTAJ: CTA ---
("""{acta("Pilotaj başvurusu mu düşünüyorsunuz?", "Sağlık sertifikasıyla başlayın. Hangi işlemi hangi sırayla ayarlamanız gerektiğini, tek kuruş ödemeden önce söyleyelim.")}""",
 """{acta("Pilot olma yolunda ilk adım", "Class 1 sağlık sertifikasıyla başlıyoruz. Hangi işlemi hangi sırayla ayarlamanız gerektiğini, tek kuruş ödemeden önce söyleyelim. Görüşme ücretsiz.")}"""),
],

# =====================================================================
'tools/pages_content5.py': [
# --- YÜKSEK LİSANS: CTA ---
("""{acta("Hangi yüksek lisans size uygun?", "Transkriptinizi gönderin; hangi programlara uygun olduğunuzu ve hangi kredi eksiğinin önce kapatılması gerektiğini söyleyelim.")}""",
 """{acta("Yüksek lisansınıza bu dönem başlayın", "Transkriptinizi gönderin; hangi programlara uygun olduğunuzu ve varsa hangi kredi eksiğini önce kapatmanız gerektiğini ilk görüşmede söyleyelim. Görüşme ücretsiz.")}"""),
],

# =====================================================================
'tools/pages_content7.py': [
# --- YAŞAM: "durust cevap" ---
("""Dürüst cevap şu: yurda başvurun ve kiralık daireyi yedek olarak ayarlayın; birini seçip
ummayın.""",
 """Önerimiz şu: yurda başvurun ve kiralık daireyi yedek olarak ayarlayın. Budapeşte ekibimiz iki
seçeneği de sizin için takip ediyor."""),

# --- ÖĞRENCİ GÖRÜŞLERİ: sektor elestirisi ---
("""<p>Sektör standardının düşük olduğu bir sayfa burası, o yüzden kurallarımızı yazmakta fayda var.</p>""",
 """<p>Referans sayfaları kolayca güvenilmez hâle geliyor, o yüzden kurallarımızı açıkça yazıyoruz.</p>"""),
],
}


def uygula():
    for yol, ciftler in R.items():
        s = io.open(yol, encoding='utf-8').read()
        n = 0
        for a, b in ciftler:
            if a in s:
                s = s.replace(a, b); n += 1
            else:
                print('  ! eslesmedi %s :: %s' % (yol, ' '.join(a.split())[:70]))
        io.open(yol, 'w', encoding='utf-8').write(s)
        print('%-28s %d degisiklik' % (yol, n))


uygula()
