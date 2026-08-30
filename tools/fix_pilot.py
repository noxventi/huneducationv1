# -*- coding: utf-8 -*-
"""Pilotaj sayfasini canli veriye gore duzeltir.

Yanlis olan neydi:
  - Universite  : "Dunaujvaros Universitesi" tek basina  ->  BME ve UOD
  - Ucret       : "7.500 - 13.500 $ / donem"             ->  BME 29.500 EUR/yil
                                                             UOD 66.800 EUR/yil
  - Ucret birimi: donemlik saniliyordu                   ->  course_price YILLIK

Kaynak: huneducation.com `course` kayitlari
  Professional Pilot - BME .......................... 29 500 EUR, 7 donem
  Pilot Training (0 to ATPL) + Mechanical Eng - UOD .. 66 800 EUR, 7 donem
"""
import io, sys

TOOLS = sys.argv[1] if len(sys.argv) > 1 else 'tools'

EN = [
# --- kisa cevap ---
("""  <p>Professional pilot training in Hungary runs as a three-and-a-half year BSc at the University of
  Dunaújváros, taught in English. The fee is quoted per term at $7,500 to $13,500 because flight hours,
  not tuition, drive the cost. Admission requires a Class 1 aeromedical certificate, an English
  assessment and an aptitude evaluation.</p>""",
 """  <p>Two Hungarian universities run pilot training in English, and they are priced very differently.
  The Budapest University of Technology and Economics offers a <b>Professional Pilot</b> programme at
  <b>€29,500 a year</b> over 7 semesters. The University of Dunaújváros combines pilot training to ATPL
  with mechanical engineering at <b>€66,800 a year</b>, also over 7 semesters. Both figures are annual
  tuition, and both include the flight training that makes this the most expensive programme in the
  catalogue.</p>"""),

# --- nerede okutuluyor ---
("""<h2 id="where">Where it is taught</h2>
<p>The <b>University of Dunaújváros (UOD)</b> runs the professional pilot programme, alongside an
aeronautical engineering degree for applicants drawn to aviation without the flight deck. Dunaújváros
sits south of Budapest on the Danube, a small campus city with a low cost of living, which matters when
the training itself is this expensive.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Aviation programmes</caption>
  <thead><tr><th>Programme</th><th>Duration</th><th>Fee</th><th>Assessment</th></tr></thead>
  <tbody>
    <tr><td><b>Aircraft Pilot BSc</b></td><td>3.5 years</td><td class="num">$7,500 – $13,500 / term</td><td>Medical, language and aptitude</td></tr>
    <tr><td><b>Aeronautical Engineering</b></td><td>3.5 years</td><td class="num">€3,000 – €5,000 / year</td><td>Online physics and mathematics exam</td></tr>
  </tbody>
</table>
</div>""",
 """<h2 id="where">Where it is taught</h2>
<p>Two universities, two different propositions. <b>BME</b> in Budapest runs a Professional Pilot
programme; the <b>University of Dunaújváros (UOD)</b> runs a combined track that takes you from zero to
an ATPL alongside a mechanical engineering degree, which is why its fee is more than double. UOD sits
south of Budapest on the Danube and has a markedly lower cost of living than the capital.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Aviation programmes and their annual tuition</caption>
  <thead><tr><th>Programme</th><th>University</th><th>Duration</th><th>Annual fee</th></tr></thead>
  <tbody>
    <tr><td><b>Professional Pilot</b></td><td>BME, Budapest</td><td>7 semesters</td><td class="num">€29,500</td></tr>
    <tr><td><b>Pilot Training (0 to ATPL) + Mechanical Engineering</b></td><td>UOD, Dunaújváros</td><td>7 semesters</td><td class="num">€66,800</td></tr>
    <tr><td>BSc Mechanical Engineering <i>(no flight training)</i></td><td>UOD, Dunaújváros</td><td>7 semesters</td><td class="num">€3,950</td></tr>
  </tbody>
</table>
</div>
<p>The third row is there for scale: the same engineering degree without flight training costs €3,950 a
year. The difference is the flying.</p>"""),

# --- maliyet nasil olusuyor ---
("""    <tr><td><b>Ground school</b></td><td>Academic tuition, per term</td><td>Theory, simulators, examinations</td></tr>
    <tr><td><b>Flight hours</b></td><td>By the hour, consumed unevenly</td><td>The dominant and most variable cost</td></tr>""",
 """    <tr><td><b>Ground school</b></td><td>Included in the annual tuition</td><td>Theory, simulators, examinations</td></tr>
    <tr><td><b>Flight hours</b></td><td>Included in the annual tuition</td><td>The reason the fee is 7 to 17 times a normal engineering degree</td></tr>"""),

("""<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Because flight hours are billed as flown, the total for the programme varies between students. Ask the
university for a written breakdown of the expected hour count before you commit, and plan the currency
risk: this programme is priced in dollars while your living costs are in euros.</p>""",
 """<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Ask the university for a written breakdown of what the fee covers before you commit: how many flight
hours are included, what happens if you need more, and whether the aeromedical certificate and its
renewals are inside or outside the tuition.</p>"""),

("""<p>Because it is not a tuition figure in the ordinary sense.""", """<p>Because it is not a tuition figure in the ordinary sense."""),

# --- ozet metinleri ---
("""    'Professional pilot training in Hungary: a three-and-a-half year BSc at the University of '
    'Dunaújváros, $7,500 to $13,500 per term, the Class 1 medical and the aptitude assessment.',""",
 """    'Pilot training in Hungary at BME and the University of Dunaújváros: €29,500 and €66,800 a year, '
    'what the fee covers, and the Class 1 aeromedical certificate you need first.',"""),
("""    'A BSc that combines ground school with flight hours. How the cost is actually built and what you '
    'need to arrange before you apply.',""",
 """    'Two universities, two very different price tags. What the fee covers and what you need to arrange '
    'before you apply.',"""),
]

TR = [
("""  <p>Macaristan'da profesyonel pilotluk, Dunaújváros Üniversitesi'nde üç buçuk yıllık İngilizce bir BSc
  olarak yürüyor. Ücret dönemlik <b>7.500 – 13.500 $</b> olarak açıklanıyor çünkü maliyeti öğrenim değil
  uçuş saatleri belirliyor. Kabul için Class 1 uçuş sağlık sertifikası, dil değerlendirmesi ve yetenek
  sınavı gerekiyor.</p>""",
 """  <p>Macaristan'da iki üniversite İngilizce pilotluk eğitimi veriyor ve fiyatları birbirinden çok
  farklı. Budapeşte Teknoloji ve Ekonomi Üniversitesi'nin <b>Professional Pilot</b> programı 7 dönem
  boyunca <b>yıllık 29.500 €</b>. Dunaújváros Üniversitesi ise ATPL'e kadar pilotluk eğitimini makine
  mühendisliğiyle birleştiriyor ve <b>yıllık 66.800 €</b>, yine 7 dönem. İki rakam da yıllık öğrenim
  ücreti ve ikisi de bu programı katalogdaki en pahalı program yapan uçuş eğitimini kapsıyor.</p>"""),

("""<h2 id="nerede">Nerede okutuluyor</h2>
<p><b>Dunaújváros Üniversitesi (UOD)</b> profesyonel pilotluk programını yürütüyor; havacılığa ilgi
duyup kokpiti hedeflemeyen adaylar için havacılık mühendisliği de aynı kampüste. Dunaújváros
Budapeşte'nin güneyinde, Tuna kıyısında küçük bir kampüs şehri ve yaşam maliyeti düşük; eğitimin
kendisi bu kadar pahalıyken bu önemli bir kalem.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Havacılık programları</caption>
  <thead><tr><th>Program</th><th>Süre</th><th>Ücret</th><th>Değerlendirme</th></tr></thead>
  <tbody>
    <tr><td><b>Profesyonel Pilotluk BSc</b></td><td>3,5 yıl</td><td class="num">7.500 – 13.500 $ / dönem</td><td>Sağlık, dil ve yetenek</td></tr>
    <tr><td><b>Havacılık Mühendisliği</b></td><td>3,5 yıl</td><td class="num">3.000 – 5.000 €</td><td>Online fizik ve matematik sınavı</td></tr>
  </tbody>
</table>
</div>""",
 """<h2 id="nerede">Nerede okutuluyor</h2>
<p>İki üniversite, iki farklı teklif. Budapeşte'deki <b>BME</b> Professional Pilot programını yürütüyor;
<b>Dunaújváros Üniversitesi (UOD)</b> ise sıfırdan ATPL'e uzanan pilotluk eğitimini makine
mühendisliğiyle birleştiren bir program veriyor ve ücreti bu yüzden iki katından fazla. UOD
Budapeşte'nin güneyinde, Tuna kıyısında; yaşam maliyeti başkente göre belirgin şekilde düşük.</p>

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
<p>Üçüncü satır ölçek için: aynı mühendislik diploması uçuş eğitimi olmadan yılda 3.950 €. Aradaki fark
uçmanın kendisi.</p>"""),

("""    <tr><td><b>Teorik eğitim</b></td><td>Dönemlik akademik ücret</td><td>Teori, simülatör, sınavlar</td></tr>
    <tr><td><b>Uçuş saatleri</b></td><td>Saat başına, dönemlere eşit dağılmadan</td><td>Baskın ve en oynak kalem</td></tr>""",
 """    <tr><td><b>Teorik eğitim</b></td><td>Yıllık ücrete dahil</td><td>Teori, simülatör, sınavlar</td></tr>
    <tr><td><b>Uçuş saatleri</b></td><td>Yıllık ücrete dahil</td><td>Ücretin normal bir mühendislik diplomasının 7–17 katı olmasının sebebi</td></tr>"""),

("""Uçuş saatleri uçuldukça faturalandığı için program toplamı öğrenciden öğrenciye değişiyor. Taahhüt
vermeden önce üniversiteden beklenen saat sayısının yazılı dökümünü isteyin ve kur riskini planlayın:
bu program dolar cinsinden fiyatlanırken yaşam gideriniz euro.</p>""",
 """Taahhüt vermeden önce üniversiteden ücretin neyi kapsadığının yazılı dökümünü isteyin: kaç uçuş saati
dahil, fazlası gerekirse ne oluyor ve uçuş sağlık sertifikası ile yenilemeleri ücretin içinde mi
dışında mı.</p>"""),

("""    "Macaristan'da profesyonel pilotluk: Dunaújváros Üniversitesi'nde üç buçuk yıllık BSc, dönemlik "
    "7.500 – 13.500 $, Class 1 sağlık sertifikası ve yetenek değerlendirmesi.",""",
 """    "Macaristan'da pilotluk eğitimi BME ve Dunaújváros Üniversitesi'nde: yıllık 29.500 € ve 66.800 €, "
    "ücretin neyi kapsadığı ve önce almanız gereken Class 1 sağlık sertifikası.","""),
("""    'Teorik eğitimle uçuş saatlerini birleştiren bir BSc. Maliyet gerçekte nasıl oluşuyor ve '
    'başvurmadan önce neyi ayarlamanız gerekiyor?',""",
 """    'İki üniversite, birbirinden çok farklı iki fiyat. Ücret neyi kapsıyor ve başvurmadan önce neyi '
    'ayarlamanız gerekiyor?',"""),
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
    print('%-22s eslesmeyen: %d' % (dosya, len(miss)))
    for m in miss:
        print('   !', m)


uygula('en_content6.py', EN)
uygula('pages_content6.py', TR)
