# -*- coding: utf-8 -*-
"""Son duzeltme paketi: canli icerikle celisen ifadeler.

1. ILETISIM  Danismanlarin dogrudan telefon/e-postasi canlida YAYINDA.
             Ben "yayinlanmiyor, merkezi kanala yonlendiriliyor" yazmisim: yanlis.
             Uzmanlik alani da "Tum seviyeler" degil "Hazirlik, Lisans, Yuksek Lisans".

2. OGRENCI   Alintilar gercek ama asiri kisaltilmisti. Ozellikle Sinan K.'nin
   GORUSLERI  hikayesi tek cumleye indirgenmisti; canlidaki tam metin geri kondu.

3. NEDEN     Hollanda/Almanya/Ingiltere maliyet rakamlari BENIM tahminimdi,
   MACARISTAN kaynagi yok. Kaldirildi; yerine yalnizca Macaristan rakami ve
             nitel bir karsilastirma kondu.

4. YUKSEK    Ucret bandi katalogdaki gercek dagilima gore genisletildi.
   LISANS
"""
import io, sys

TOOLS = sys.argv[1] if len(sys.argv) > 1 else 'tools'

# =====================================================================
# 1) ILETISIM
# =====================================================================
EN3 = [
("""<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
In line with our data protection and operational policy, advisers' direct lines and email addresses
are routed through central channels rather than published. Your request reaches the right adviser.</p>""",
 """<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Each adviser has a direct phone number and email address, so you can reach the right person without
going through a queue. Ask us and we will point you to the adviser who covers your level and your
city.</p>"""),
("""    ('Beyza Kantarcı', 'Budapest · Head office', 'Foundation, bachelor’s, master’s'),
    ('Hacer Çakmak', 'Budapest', 'All levels'),
    ('Veli Çınaroğlu', 'Pécs', 'All levels'),
    ('Çağla Nur Türken', 'Debrecen · Nyíregyháza', 'All levels'),
    ('Nesrin Ertaş', 'Ankara', 'All levels'),
    ('Funda Toksoy', 'Ankara', 'All levels'),
    ('Orkun Tokdemir', 'Istanbul · Kadıköy', 'All levels'),
    ('Nur Alpay', 'Izmir', 'All levels'),
    ('Figen Durmaz', 'Bursa', 'All levels'),
    ('Deniz Hızal', 'Çanakkale', 'All levels'),
    ('Ali Yalçın', 'Denizli', 'All levels'),""",
 """    ('Beyza Kantarcı', 'Budapest · Head office', 'Preparatory, bachelor’s, master’s'),
    ('Veli Çınaroğlu', 'Pécs · Hungary representative', 'Preparatory, bachelor’s, master’s'),
    ('Çağla Nur Türken', 'Debrecen · Nyíregyháza', 'Preparatory, bachelor’s, master’s'),
    ('Hacer Çakmak', 'Budapest', 'Preparatory, bachelor’s, master’s'),
    ('Nesrin Ertaş', 'Ankara', 'Preparatory, bachelor’s, master’s'),
    ('Funda Toksoy', 'Ankara', 'Preparatory, bachelor’s, master’s'),
    ('Orkun Tokdemir', 'Istanbul · Kadıköy', 'Preparatory, bachelor’s, master’s'),
    ('Nur Alpay', 'Izmir', 'Preparatory, bachelor’s, master’s'),
    ('Figen Durmaz', 'Bursa', 'Preparatory, bachelor’s, master’s'),
    ('Deniz Hızal', 'Çanakkale', 'Preparatory, bachelor’s, master’s'),
    ('Ali Yalçın', 'Denizli', 'Preparatory, bachelor’s, master’s'),"""),
]
TR3 = [
("""<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Danışmanlara ait doğrudan hat ve e-posta adresleri, KVKK ve operasyon politikası doğrultusunda
yayınlanmak yerine merkezî kanallar üzerinden yönlendirilmektedir. Talebiniz doğru danışmana
iletilir.</p>""",
 """<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Her danışmanın doğrudan telefonu ve e-posta adresi var; sıraya girmeden doğru kişiye
ulaşabilirsiniz. Bize yazın, seviyenize ve şehrinize bakan danışmana yönlendirelim.</p>"""),
("""    ('Beyza Kantarcı', 'Budapeşte · Merkez ofis', 'Hazırlık, lisans, yüksek lisans'),
    ('Hacer Çakmak', 'Budapeşte', 'Tüm seviyeler'),
    ('Veli Çınaroğlu', 'Pécs', 'Tüm seviyeler'),
    ('Çağla Nur Türken', 'Debrecen · Nyíregyháza', 'Tüm seviyeler'),
    ('Nesrin Ertaş', 'Ankara', 'Tüm seviyeler'),
    ('Funda Toksoy', 'Ankara', 'Tüm seviyeler'),
    ('Orkun Tokdemir', 'İstanbul · Kadıköy', 'Tüm seviyeler'),
    ('Nur Alpay', 'İzmir', 'Tüm seviyeler'),
    ('Figen Durmaz', 'Bursa', 'Tüm seviyeler'),
    ('Deniz Hızal', 'Çanakkale', 'Tüm seviyeler'),
    ('Ali Yalçın', 'Denizli', 'Tüm seviyeler'),""",
 """    ('Beyza Kantarcı', 'Budapeşte · Merkez ofis', 'Hazırlık, lisans, yüksek lisans'),
    ('Veli Çınaroğlu', 'Pécs · Macaristan temsilcisi', 'Hazırlık, lisans, yüksek lisans'),
    ('Çağla Nur Türken', 'Debrecen · Nyíregyháza', 'Hazırlık, lisans, yüksek lisans'),
    ('Hacer Çakmak', 'Budapeşte', 'Hazırlık, lisans, yüksek lisans'),
    ('Nesrin Ertaş', 'Ankara', 'Hazırlık, lisans, yüksek lisans'),
    ('Funda Toksoy', 'Ankara', 'Hazırlık, lisans, yüksek lisans'),
    ('Orkun Tokdemir', 'İstanbul · Kadıköy', 'Hazırlık, lisans, yüksek lisans'),
    ('Nur Alpay', 'İzmir', 'Hazırlık, lisans, yüksek lisans'),
    ('Figen Durmaz', 'Bursa', 'Hazırlık, lisans, yüksek lisans'),
    ('Deniz Hızal', 'Çanakkale', 'Hazırlık, lisans, yüksek lisans'),
    ('Ali Yalçın', 'Denizli', 'Hazırlık, lisans, yüksek lisans'),"""),
]

# =====================================================================
# 2) OGRENCI GORUSLERI - tam metinler
# =====================================================================
EN7 = [
("""    <blockquote><p>The Hun Education advisers helped me enormously with every step. I now work in
    Budapest, in the visual effects department of a major film production.</p></blockquote>""",
 """    <blockquote><p>The Hun Education advisers helped me enormously with every step. I graduated in Film
    and Media at Budapest Metropolitan University. After my studies and internship I worked with
    production companies including Disney, Marvel, Netflix and Paramount. I now work in Budapest, in the
    visual effects department of a major film production.</p></blockquote>"""),
("""    <blockquote><p>As of June 2022 I am about to finish my fourth year. I feel lucky to be studying in
    Budapest, and at a university of this quality.</p></blockquote>""",
 """    <blockquote><p>I started with Hun Education in the 2017–2018 academic year on the German-language
    pre-medical course at McDaniel College, then moved to Semmelweis University in September 2018. As of
    June 2022 I am about to finish my fourth year, and I feel lucky to be studying in Budapest at a
    university of this quality.</p></blockquote>"""),
("""    <blockquote><p>I am now working at Samsung in Hungary.</p></blockquote>""",
 """    <blockquote><p>I came to Debrecen with Hun Education in September 2008. After finishing Electrical
    Engineering there I completed a master's in mechatronics and a PhD at Óbuda University, then worked
    at Óbuda as an academic. I am now working at Samsung in Hungary.</p></blockquote>"""),
("""    <tr><td><b>Sude A.</b></td><td>University of Pécs</td><td>Medicine</td></tr>
    <tr><td><b>Özlem D.</b></td><td>University of Pécs</td><td>English Studies MA</td></tr>
    <tr><td><b>Sude</b></td><td>University of Pécs</td><td>Nursing</td></tr>""",
 """    <tr><td><b>Sude A.</b></td><td>University of Pécs</td><td>Preparatory year, then Medicine</td></tr>
    <tr><td><b>Özlem D.</b></td><td>University of Pécs</td><td>English Studies MA, now a PhD at Szeged and our Pécs representative</td></tr>
    <tr><td><b>Sude</b></td><td>University of Pécs</td><td>Nursing, first year</td></tr>"""),
]
TR7 = [
("""    <blockquote><p>Tüm işlemlerimde Hun Education danışmanları çok yardımcı oldu. Şimdi Budapeşte'de,
    büyük bir film yapımında Visual Effects departmanında çalışıyorum.</p></blockquote>""",
 """    <blockquote><p>Tüm işlemlerimde Hun Education danışmanları çok yardımcı oldu. Budapeşte Metropolitan
    Üniversitesi Film ve Medya'yı bitirdim. Eğitimim ve stajım sonrasında Disney, Marvel, Netflix ve
    Paramount gibi yapım şirketlerinde çalıştım. Şimdi Budapeşte'de, büyük bir film yapımında Visual
    Effects departmanında çalışıyorum.</p></blockquote>"""),
("""    <blockquote><p>Haziran 2022 itibarıyla 4. yıl bitmek üzere. Budapeşte'de ve böyle kaliteli bir
    okulda eğitim gördüğüm için kendimi şanslı hissediyorum.</p></blockquote>""",
 """    <blockquote><p>Hun Education ile ilk olarak 2017-2018 akademik yılında McDaniel College'da Almanca
    Tıp Öncesi eğitimi aldım ve ardından Eylül 2018'de Semmelweis Üniversitesi'ne yerleştim. Haziran 2022
    itibarıyla 4. yıl bitmek üzere; Budapeşte'de ve böyle kaliteli bir okulda eğitim gördüğüm için
    kendimi şanslı hissediyorum.</p></blockquote>"""),
("""    <blockquote><p>Şu an Macaristan Samsung'da çalışıyorum.</p></blockquote>""",
 """    <blockquote><p>2008 Eylül ayında Hun Education ile Debrecen'e geldim. Elektrik Mühendisliği
    programını Debrecen'de bitirdikten sonra yüksek lisansımı (mekatronik) ve doktoramı Óbuda
    Üniversitesi'nde tamamladım. Daha sonra Óbuda Üniversitesi'nde akademisyen olarak çalıştım. Şu an
    Macaristan Samsung'da çalışıyorum.</p></blockquote>"""),
("""    <tr><td><b>Sude A.</b></td><td>Pécs Üniversitesi</td><td>Tıp</td></tr>
    <tr><td><b>Özlem D.</b></td><td>Pécs Üniversitesi</td><td>İngiliz Dili YL</td></tr>
    <tr><td><b>Sude</b></td><td>Pécs Üniversitesi</td><td>Hemşirelik</td></tr>""",
 """    <tr><td><b>Sude A.</b></td><td>Pécs Üniversitesi</td><td>Hazırlık, ardından Tıp</td></tr>
    <tr><td><b>Özlem D.</b></td><td>Pécs Üniversitesi</td><td>İngiliz Dili YL; şu an Szeged'de doktora ve Pécs temsilcimiz</td></tr>
    <tr><td><b>Sude</b></td><td>Pécs Üniversitesi</td><td>Hemşirelik, 1. sınıf</td></tr>"""),
]

# =====================================================================
# 3) NEDEN MACARISTAN - kaynaksiz ulke rakamlari kaldirildi
# =====================================================================
EN5 = [
("""<div class="tablewrap">
<table class="dtable">
  <caption>Indicative annual budget by country (tuition and living costs)</caption>
  <thead><tr><th>Country</th><th>Tuition</th><th>Living</th><th>Total</th></tr></thead>
  <tbody>
    <tr><td><b>Hungary</b></td><td class="num">€3,000 – €6,000</td><td class="num">€4,000 – €8,000</td><td class="num">€8,500 – €14,000</td></tr>
    <tr><td>Netherlands</td><td class="num">from €9,000</td><td class="num">from €11,000</td><td class="num">€20,000+</td></tr>
    <tr><td>Germany (private)</td><td class="num">from €10,000</td><td class="num">from €11,000</td><td class="num">€21,000+</td></tr>
    <tr><td>United Kingdom</td><td class="num">from £16,000</td><td class="num">from £12,000</td><td class="num">£28,000+</td></tr>
  </tbody>
</table>
</div>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
The Hungarian figures are ours and are re-verified every academic year. The comparison rows are
indicative orders of magnitude for international fee payers, not quotes: check each country's own
published tuition before you use them for planning.</p>""",
 """<div class="tablewrap">
<table class="dtable">
  <caption>Annual budget in Hungary, at bachelor's level</caption>
  <thead><tr><th>Item</th><th>Amount</th></tr></thead>
  <tbody>
    <tr><td><b>Tuition</b></td><td class="num">€3,000 – €5,000</td></tr>
    <tr><td><b>Living costs</b></td><td class="num">€4,000 – €8,000</td></tr>
    <tr><td><b>Total for the year</b></td><td class="num">€8,500 – €14,000</td></tr>
  </tbody>
</table>
</div>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
These are our own figures, compiled from university tariffs and the real spending of our students, and
re-verified every academic year. We deliberately do not publish a comparison table of other countries:
we do not track their fees closely enough to stand behind the numbers. Compare against the published
tuition of the specific universities you are considering.</p>"""),
]
TR5 = [
("""<div class="tablewrap">
<table class="dtable">
  <caption>Ülkeye göre gösterge niteliğinde yıllık bütçe (öğrenim + yaşam)</caption>
  <thead><tr><th>Ülke</th><th>Öğrenim</th><th>Yaşam</th><th>Toplam</th></tr></thead>
  <tbody>
    <tr><td><b>Macaristan</b></td><td class="num">3.000 – 6.000 €</td><td class="num">4.000 – 8.000 €</td><td class="num">8.500 – 14.000 €</td></tr>
    <tr><td>Hollanda</td><td class="num">9.000 €'dan</td><td class="num">11.000 €'dan</td><td class="num">20.000 €+</td></tr>
    <tr><td>Almanya (özel)</td><td class="num">10.000 €'dan</td><td class="num">11.000 €'dan</td><td class="num">21.000 €+</td></tr>
    <tr><td>Birleşik Krallık</td><td class="num">16.000 £'dan</td><td class="num">12.000 £'dan</td><td class="num">28.000 £+</td></tr>
  </tbody>
</table>
</div>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Macaristan rakamları bize aittir ve her akademik yıl yeniden doğrulanır. Karşılaştırma satırları
uluslararası öğrenciler için büyüklük mertebesi göstergesidir, teklif değildir; planlama yaparken
ilgili ülkenin kendi yayınladığı ücretleri esas alın.</p>""",
 """<div class="tablewrap">
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
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Bu rakamlar bize ait; üniversite tarifelerinden ve öğrencilerimizin gerçek harcamalarından derleniyor
ve her akademik yıl yeniden doğrulanıyor. Diğer ülkelerin maliyet tablosunu bilerek yayınlamıyoruz:
onların ücretlerini arkasında duracak kadar yakından takip etmiyoruz. Karşılaştırmayı, düşündüğünüz
üniversitelerin kendi yayınladığı ücretler üzerinden yapın.</p>"""),
]

# =====================================================================
# 4) YUKSEK LISANS - ucret bandi gercege gore
# =====================================================================
EN5b = [
("""  <p>A master's in Hungary takes two years and 120 ECTS, is taught in English, and costs
  €4,000 to €6,000 a year in tuition.""",
 """  <p>A master's in Hungary takes two years and 120 ECTS and is taught in English. Hun Education's
  published range is €4,000 to €6,000 a year; across the catalogue the actual figures run wider, from
  about €3,200 to €14,000 depending on the university and the field."""),
("""  <p>Tuition runs <b>€4,000 to €6,000 a year</b>, with psychology starting higher at €7,800.
  Adding living costs, a realistic total is <b>€9,000 to €15,000 a year</b>, moving mostly with your
  accommodation choice.</p>""",
 """  <p>The published range is <b>€4,000 to €6,000 a year</b>, and that is where most programmes sit.
  Psychology is higher, from €7,800 at Pécs to €9,400 at ELTE. Adding living costs, a realistic total is
  <b>€9,000 to €15,000 a year</b>, moving mostly with your accommodation choice.</p>"""),
("""    <tr><td><b>Humanities and social sciences</b></td><td>Psychology MA, English Studies MA</td><td class="num">from €7,800 (psychology)</td></tr>""",
 """    <tr><td><b>Humanities and social sciences</b></td><td>Psychology MA, English Studies MA</td><td class="num">€7,800 – €9,400 (psychology)</td></tr>"""),
]
TR5b = [
("""  <p>Macaristan'da yüksek lisans iki yıl ve 120 AKTS, İngilizce yürüyor ve yıllık öğrenim ücreti
  <b>4.000 – 6.000 €</b>.""",
 """  <p>Macaristan'da yüksek lisans iki yıl ve 120 AKTS, İngilizce yürüyor. Hun Education'ın yayınladığı
  aralık <b>yıllık 4.000 – 6.000 €</b>; katalog genelinde gerçek rakamlar daha geniş bir bantta,
  üniversiteye ve alana göre yaklaşık 3.200 € ile 14.000 € arasında."""),
("""  <p>Öğrenim ücreti <b>yıllık 4.000 – 6.000 €</b>; psikoloji 7.800 €'dan başlıyor. Yaşam giderleri
  eklendiğinde gerçekçi toplam <b>yıllık 9.000 – 15.000 €</b> ve bu aralığı esas olarak konaklama
  tercihiniz belirliyor.</p>""",
 """  <p>Yayınlanan aralık <b>yıllık 4.000 – 6.000 €</b> ve programların çoğu bu bantta. Psikoloji daha
  yüksek: Pécs'te 7.800 €, ELTE'de 9.400 €. Yaşam giderleri eklendiğinde gerçekçi toplam
  <b>yıllık 9.000 – 15.000 €</b> ve bu aralığı esas olarak konaklama tercihiniz belirliyor.</p>"""),
("""    <tr><td><b>Beşeri ve sosyal bilimler</b></td><td>Psikoloji MA, İngiliz Dili MA</td><td class="num">7.800 €'dan (psikoloji)</td></tr>""",
 """    <tr><td><b>Beşeri ve sosyal bilimler</b></td><td>Psikoloji MA, İngiliz Dili MA</td><td class="num">7.800 – 9.400 € (psikoloji)</td></tr>"""),
]


def uygula(dosya, ciftler, etiket):
    p = TOOLS + '/' + dosya
    s = io.open(p, encoding='utf-8').read()
    miss = []
    for a, b in ciftler:
        if a not in s:
            miss.append(' '.join(a.split())[:66])
            continue
        s = s.replace(a, b)
    io.open(p, 'w', encoding='utf-8').write(s)
    print('%-18s %-14s eslesmeyen: %d' % (dosya, etiket, len(miss)))
    for m in miss:
        print('   !', m)


uygula('en_content3.py', EN3, 'iletisim')
uygula('pages_content3.py', TR3, 'iletisim')
uygula('en_content7.py', EN7, 'ogrenci')
uygula('pages_content7.py', TR7, 'ogrenci')
uygula('en_content5.py', EN5 + EN5b, 'neden+YL')
uygula('pages_content5.py', TR5 + TR5b, 'neden+YL')
