# -*- coding: utf-8 -*-
"""Basvuru sayfasini canli icerige gore duzeltir ve EKSIKLERI tamamlar.

Canlida olup bende HIC OLMAYAN sartlar (en onemlisi bunlar):
  * YAS SINIRI      Hazirlik 25 | Lisans 25 | Yuksek lisans 28 | Tip/Dis/Ecz sinirsiz
  * UYRUK KISITI    Hun Education her ulkeden basvuru kabul edemiyor; belirli bir
                    ulke listesi var. Ingilizce sayfada bu kritik.
  * MALI YETERLILIK ~650 EUR/ay x 10 ay = 6.500 EUR gosterilmesi bekleniyor
  * SIGORTA         En az 3 ay, tercihen 1 yil seyahat ve kaza sigortasi

Bende YANLIS/EKSIK olanlar:
  * Banka dokumu "cekirdek belge" olarak yazilmisti; canlida "Zorunlu Degil",
    vize asamasi icin gerekiyor
  * IELTS sarti abartilmisti; canlida "cogu okul kendi mulakatini yaptigi icin
    istemiyor, bazi okullar IELTS 5 / 6 / 6.5 istiyor"
  * Iade kosulu kosulsuz yazilmisti; canlida konsolosluk RET GEREKCESI
    iletildikten sonra ve "genellikle" 30 is gunu; kayit ucreti de iade disi
  * Son basvuru "Nisan-Haziran"di; canlida bazi universiteler Temmuz sonuna
    kadar aliyor

Kaynak: tr.huneducation.com/macaristan-universite-basvuru-sartlari/
"""
import io, sys

TOOLS = sys.argv[1] if len(sys.argv) > 1 else 'tools'

EN = [
# --- belge tablosu: banka dokumu zorunlu degil ---
("""    <tr><td><b>Bank statement</b></td><td>Last 6 months</td><td>Needed at the visa stage</td></tr>""",
 """    <tr><td><b>Bank statement</b></td><td>Last 6 months, sponsor's account</td><td><b>Not required to apply.</b> Needed at the visa stage; add a sponsor letter if someone else funds your studies</td></tr>"""),
("""    <tr><td><b>Language certificate</b></td><td>IELTS or equivalent</td><td>Varies by programme, see below</td></tr>""",
 """    <tr><td><b>Language certificate</b></td><td>IELTS or equivalent</td><td>Often <b>not</b> required: most universities run their own interview instead</td></tr>"""),

# --- dil sarti gercege gore ---
("""<p>Almost every programme in this catalogue is taught in English, which makes language proficiency one
of the decisive steps in admission. The accepted certificate and the minimum score vary by
university; some universities accept their own online language test instead.</p>""",
 """<p>Almost every programme in this catalogue is taught in English. The point applicants most often get
wrong is this: <b>most Hungarian universities do not ask for a language certificate at all</b>, because
they run their own interview or online test instead. Some do ask for IELTS, at 5, 6 or 6.5 depending on
the university and the programme.</p>"""),
("""    <tr><td><b>Bachelor's</b></td><td class="num">B2 minimum · IELTS 5 – 6.5</td><td>English Language Foundation programme</td></tr>
    <tr><td><b>Master's</b></td><td class="num">IELTS 6.5 or equivalent</td><td>Foundation year, then reapply</td></tr>
    <tr><td><b>Foundation</b></td><td>Placement test</td><td>No certificate required</td></tr>""",
 """    <tr><td><b>Bachelor's</b></td><td class="num">B2 in practice · IELTS 5, 6 or 6.5 where asked</td><td>English Language Preparatory programme</td></tr>
    <tr><td><b>Master's</b></td><td class="num">Usually IELTS 6.5 or equivalent</td><td>Preparatory year, then reapply</td></tr>
    <tr><td><b>Preparatory</b></td><td>University's own placement test</td><td>No certificate required</td></tr>"""),

# --- YENI: uygunluk bolumu ---
("""<h2 id="exam">Entrance exams and interviews</h2>""",
 """<h2 id="eligibility">Before the documents: are you eligible?</h2>
<p>Two conditions decide this before any paperwork does, and both are easy to miss.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Age limits by programme type</caption>
  <thead><tr><th>Programme</th><th>Maximum age</th></tr></thead>
  <tbody>
    <tr><td>Preparatory programmes</td><td class="num">25</td></tr>
    <tr><td>Bachelor's</td><td class="num">25</td></tr>
    <tr><td>Master's</td><td class="num">28</td></tr>
    <tr><td>Medicine, dentistry, pharmacy</td><td>No age limit</td></tr>
  </tbody>
</table>
</div>
<p>If you are above these limits, talk to us anyway. The limits are real, but the right route often
exists and we will tell you what it is.</p>

<h3>Nationality</h3>
<p>Hun Education is not authorised to submit applications from every country. We can work with citizens
of: <b>European Union countries, the United States and Latin America, Albania, Algeria, Azerbaijan,
Bosnia and Herzegovina, Egypt, Georgia, Jordan, Kazakhstan, Kyrgyzstan, Mongolia, Qatar, Russia,
Serbia, Thailand, Türkiye, Ukraine, Uzbekistan and Vietnam.</b></p>

<h3>Financial capacity</h3>
<p>The consulate expects to see that your studies are funded. A working estimate is
<b>€650 a month across a 10-month academic year, so about €6,500</b>, held in your own or your
sponsor's account, alongside evidence of regular income. This is not a Hungarian peculiarity; every
country's consulate looks for the same thing. If that cannot be evidenced, we do not recommend
starting a visa application.</p>

<h2 id="exam">Entrance exams and interviews</h2>"""),

# --- takvim: temmuz sonu ---
("""    <tr><td><b>Autumn</b></td><td class="num">September</td><td class="num">April – June</td><td class="num">January – February</td></tr>""",
 """    <tr><td><b>Autumn</b></td><td class="num">September</td><td class="num">April – June (some until end of July)</td><td class="num">January – February</td></tr>"""),

# --- iade kosulu ---
("""    ("What happens to my tuition fee if my visa is refused?",
     "<p>If the student visa is refused, tuition already paid is refunded within 30 working days. "
     "Application and entrance exam fees fall outside the refund.</p>"),""",
 """    ("What happens to my tuition fee if my visa is refused?",
     "<p>You send the university the written refusal issued by the consulate, and the tuition is then "
     "usually refunded within 30 working days. Application, entrance exam and registration fees are "
     "outside the refund. The exact terms are in your service agreement.</p>"),"""),

# --- surec adimi: sigorta ---
("""  <li><div><h3>Travel and arrival</h3><p>After the visa we plan your flight, accommodation and arrival in Budapest.</p></div></li>""",
 """  <li><div><h3>Travel and arrival</h3><p>After the visa we plan your flight, accommodation and arrival. You will need travel and accident insurance covering at least three months, ideally the full year.</p></div></li>"""),

# --- ozet ---
("""    "Documents, English requirement, entrance exams and the application calendar for applying to a "
    "university in Hungary — from the apostille to the student visa, step by step.",""",
 """    "Age limits, eligible nationalities, financial capacity, documents, the English requirement and "
    "entrance exams for applying to a university in Hungary, step by step.","""),

("""      {toc([('short-answer','Short answer'),('documents','Required documents'),('language','English requirement'),""",
 """      {toc([('short-answer','Short answer'),('documents','Required documents'),('language','English requirement'),('eligibility','Are you eligible?'),"""),
]

TR = [
("""    <tr><td><b>Banka hesap dökümü</b></td><td>Son 6 ay</td><td>Vize aşaması için gereklidir</td></tr>""",
 """    <tr><td><b>Banka hesap dökümü</b></td><td>Son 6 ay, veli/sponsor hesabı</td><td><b>Başvuru için zorunlu değil.</b> Vize aşamasında gerekir; eğitiminizi başkası finanse ediyorsa sponsor mektubu ekleyin</td></tr>"""),
("""    <tr><td><b>Dil belgesi</b></td><td>IELTS veya eşdeğeri</td><td>Bölüme göre değişir, aşağıya bakınız</td></tr>""",
 """    <tr><td><b>Dil belgesi</b></td><td>IELTS veya eşdeğeri</td><td>Çoğu zaman <b>istenmiyor</b>: üniversitelerin çoğu kendi mülakatını yapıyor</td></tr>"""),

("""<p>Programların büyük çoğunluğu İngilizce eğitim verdiği için dil yeterliliği kabulün belirleyici
adımlarından biridir. Kabul edilen belge türü ve minimum puan üniversiteye göre değişir; bazı
üniversiteler kendi çevrim içi dil sınavını yeterli sayar.</p>""",
 """<p>Kataloğumuzdaki neredeyse her program İngilizce yürüyor. Adayların en çok yanıldığı nokta şu:
<b>Macaristan'da çoğu üniversite dil belgesi istemiyor</b>, çünkü kendi mülakatını ya da çevrim içi
sınavını yapıyor. Bazı okullar IELTS istiyor; üniversiteye ve bölüme göre 5, 6 veya 6,5.</p>"""),
("""    <tr><td><b>Lisans</b></td><td class="num">En az B2 · IELTS 5 – 6.5</td><td>İngilizce Dil Hazırlık programı</td></tr>
    <tr><td><b>Yüksek lisans</b></td><td class="num">IELTS 6.5 veya eşdeğeri</td><td>Hazırlık + yeniden başvuru</td></tr>
    <tr><td><b>Hazırlık</b></td><td>Seviye tespit sınavı</td><td>Belge şartı yok</td></tr>""",
 """    <tr><td><b>Lisans</b></td><td class="num">Pratikte B2 · istenirse IELTS 5, 6 veya 6,5</td><td>İngilizce Dil Hazırlık programı</td></tr>
    <tr><td><b>Yüksek lisans</b></td><td class="num">Genellikle IELTS 6.5 veya eşdeğeri</td><td>Hazırlık + yeniden başvuru</td></tr>
    <tr><td><b>Hazırlık</b></td><td>Üniversitenin kendi seviye tespit sınavı</td><td>Belge şartı yok</td></tr>"""),

("""<h2 id="sinav">Giriş sınavı ve mülakat</h2>""",
 """<h2 id="uygunluk">Belgelerden önce: uygun musunuz?</h2>
<p>Bu soruyu evraktan önce iki koşul belirliyor ve ikisi de kolayca gözden kaçıyor.</p>

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
<p>Bu sınırların üzerindeyseniz yine de bize yazın. Sınırlar gerçek ama çoğu zaman uygun bir yol
bulunuyor; hangisi olduğunu söyleriz.</p>

<h3>Uyruk</h3>
<p>Hun Education her ülkeden başvuru gönderme yetkisine sahip değil. Şu ülkelerin vatandaşlarıyla
çalışabiliyoruz: <b>Avrupa Birliği ülkeleri, ABD ve Latin Amerika ülkeleri, Arnavutluk, Cezayir,
Azerbaycan, Bosna Hersek, Mısır, Gürcistan, Ürdün, Kazakistan, Kırgızistan, Moğolistan, Katar, Rusya,
Sırbistan, Tayland, Türkiye, Ukrayna, Özbekistan ve Vietnam.</b></p>

<h3>Mali yeterlilik</h3>
<p>Konsolosluk eğitiminizin finanse edildiğini görmek istiyor. Çalışma varsayımı şu:
<b>aylık ortalama 650 € × 10 aylık akademik yıl, yani yaklaşık 6.500 €</b>; kendi ya da sponsorunuzun
hesabında, düzenli gelir kanıtıyla birlikte. Bu Macaristan'a özgü bir kural değil; her ülkenin
konsolosluğu aynı şeye bakıyor. Belgelenemiyorsa vize başvurusu başlatmayı önermiyoruz.</p>

<h2 id="sinav">Giriş sınavı ve mülakat</h2>"""),

("""    <tr><td><b>Güz</b></td><td class="num">Eylül</td><td class="num">Nisan – Haziran</td><td class="num">Ocak – Şubat</td></tr>""",
 """    <tr><td><b>Güz</b></td><td class="num">Eylül</td><td class="num">Nisan – Haziran (bazı okullar Temmuz sonuna kadar)</td><td class="num">Ocak – Şubat</td></tr>"""),

("""    ("Vize alamazsam ödediğim ücret ne oluyor?",
     "<p>Vize alınamaması durumunda ödenen öğrenim ücreti 30 iş günü içinde iade edilir. "
     "Başvuru ve sınav ücretleri iade kapsamı dışındadır.</p>"),""",
 """    ("Vize alamazsam ödediğim ücret ne oluyor?",
     "<p>Konsolosluğun verdiği yazılı ret gerekçesini üniversiteye ilettikten sonra öğrenim ücreti "
     "genellikle 30 iş günü içinde iade edilir. Başvuru, sınav ve kayıt ücretleri iade kapsamı "
     "dışındadır. Kesin koşullar hizmet sözleşmenizde yer alır.</p>"),"""),

("""  <li><div><h3>Seyahat ve karşılama</h3><p>Vize sonrası uçuş, konaklama ve Budapeşte'de karşılama planlanır.</p></div></li>""",
 """  <li><div><h3>Seyahat ve karşılama</h3><p>Vize sonrası uçuş, konaklama ve karşılama planlanır. En az üç ay, tercihen bir yıl süreli seyahat ve kaza sigortasına ihtiyacınız olacak.</p></div></li>"""),

("""    "Macaristan'da üniversite başvurusu için gereken belgeler, dil şartı, giriş sınavları ve başvuru "
    "takvimi. Apostilden vize adımına kadar süreç adım adım.",""",
 """    "Macaristan üniversite başvurusu: yaş sınırı, kabul edilen uyruklar, mali yeterlilik, belgeler, "
    "dil şartı ve giriş sınavları. Süreç adım adım.","""),

("""{toc([('kisa-cevap','Kısa cevap'),('belgeler','Gerekli belgeler'),('dil','Dil yeterliliği'),""",
 """{toc([('kisa-cevap','Kısa cevap'),('belgeler','Gerekli belgeler'),('dil','Dil yeterliliği'),('uygunluk','Uygun musunuz?'),"""),
]


def uygula(dosya, ciftler):
    p = TOOLS + '/' + dosya
    s = io.open(p, encoding='utf-8').read()
    miss = []
    for a, b in ciftler:
        if a not in s:
            miss.append(' '.join(a.split())[:70])
            continue
        s = s.replace(a, b)
    io.open(p, 'w', encoding='utf-8').write(s)
    print('%-20s eslesmeyen: %d' % (dosya, len(miss)))
    for m in miss:
        print('   !', m)


uygula('en_content.py', EN)
uygula('pages_content.py', TR)
