# -*- coding: utf-8 -*-
"""Tip sayfasini canli veriye gore duzeltir.

Yanlis olan neydi:
  - "Dort universite: Semmelweis, Debrecen, Szeged, Pecs"
        -> Katalogda tip UC universitede: SOTE, PTE, SZTE. Debrecen'de YOK.
  - "16.000 EUR/yil" tek rakam
        -> SOTE 19.900 USD | PTE 18.000 USD | SZTE 15.800 EUR (hepsi yillik)
  - "Dis hekimligi 17.350 EUR'dan"
        -> Dis PTE 18.600 EUR; SOTE'de dis Almanca yurutuluyor (18.300 EUR)
  - "Tip Hazirlik Szeged'de, donemlik 2.500 EUR'dan"
        -> Pre-Medical McDaniel (7.230 / 7.800 EUR) ve PTE (5.850 EUR), YILLIK

Kaynak: huneducation.com `course` kayitlari + macaristan-universite-fiyatlari
sayfasi (tip+dis icin yillik toplam ~26.000 EUR).
"""
import io, sys

TOOLS = sys.argv[1] if len(sys.argv) > 1 else 'tools'

EN = [
("""    ("What does medicine cost per year?",
     "<p>€16,000 a year for general medicine and from €17,350 for dentistry. Living costs are on top, so "
     "a realistic total is roughly €21,000 to €26,000 a year.</p>"),""",
 """    ("What does medicine cost per year?",
     "<p>It depends on the university and the currency it charges in: Semmelweis $19,900, Pécs $18,000 "
     "and Szeged €15,800 a year. Dentistry at Pécs is €18,600. Hun Education's published figure for "
     "medicine and dentistry including living costs is about €26,000 a year.</p>"),"""),

("""  <p>Medicine in Hungary is a six-year integrated programme taught in English, costing €16,000 a year;
  dentistry runs five years from €17,350. Admission turns on a chemistry and biology entrance exam set
  by the faculty itself. Four universities teach it: Semmelweis, Debrecen, Szeged and Pécs. Practising
  afterwards depends on recognition in the country where you intend to work.</p>""",
 """  <p>Medicine in Hungary is a six-year integrated programme taught in English at
  <b>three universities</b>: Semmelweis in Budapest, Pécs and Szeged. Annual tuition runs $19,900,
  $18,000 and €15,800 respectively; dentistry at Pécs is €18,600 over five years. Admission turns on a
  chemistry and biology assessment set by the faculty itself. Practising afterwards depends on
  recognition in the country where you intend to work.</p>"""),

("""    <tr><td><b>Semmelweis University (SOTE)</b></td><td>Budapest</td><td>Medicine, Dentistry, Pharmacy</td><td class="num">€16,000 – €17,350</td></tr>
    <tr><td><b>University of Debrecen</b></td><td>Debrecen</td><td>Medicine, Dentistry</td><td class="num">€16,000 – €17,350</td></tr>
    <tr><td><b>University of Szeged (SZTE)</b></td><td>Szeged</td><td>Medicine, Pre-Medical Course</td><td class="num">€16,000</td></tr>
    <tr><td><b>University of Pécs (PTE)</b></td><td>Pécs</td><td>Medicine, Nursing</td><td class="num">€16,000</td></tr>""",
 """    <tr><td><b>Semmelweis University (SOTE)</b></td><td>Budapest</td><td>Medicine (6 yrs)</td><td class="num">$19,900 / year</td></tr>
    <tr><td><b>University of Pécs (PTE)</b></td><td>Pécs</td><td>Medicine (6 yrs)</td><td class="num">$18,000 / year</td></tr>
    <tr><td><b>University of Szeged (SZTE)</b></td><td>Szeged</td><td>Medicine (6 yrs)</td><td class="num">€15,800 / year</td></tr>
    <tr><td><b>University of Pécs (PTE)</b></td><td>Pécs</td><td>Dentistry (5 yrs)</td><td class="num">€18,600 / year</td></tr>
    <tr><td><b>Semmelweis University (SOTE)</b></td><td>Budapest</td><td>Pharmacy (5 yrs)</td><td class="num">€12,600 / year</td></tr>
    <tr><td><b>University of Pécs (PTE)</b></td><td>Pécs</td><td>Pharmacy (5 yrs)</td><td class="num">€8,800 / year</td></tr>"""),

("""<h2 id="universities">Where medicine is taught</h2>""",
 """<h2 id="universities">Where medicine is taught</h2>
<p>Note what is <b>not</b> on this list. Debrecen is one of Hungary's best-known medical faculties, but
it is not in the programmes we can currently submit applications to. Dentistry at Semmelweis is taught
in German rather than English. Two of the three medicine programmes are priced in <b>US dollars</b>,
which matters when your living costs are in euros.</p>"""),

("""    <tr><td><b>Subjects</b></td><td>Chemistry and biology</td></tr>
    <tr><td><b>Format</b></td><td>Written or oral, set by the university; some run it online</td></tr>""",
 """    <tr><td><b>Subjects</b></td><td>Chemistry and biology</td></tr>
    <tr><td><b>Format</b></td><td>Set by the university. Semmelweis records its assessment as an interview; Szeged runs a written and oral exam online.</td></tr>"""),

("""  <p><b>€21,000 – €26,000</b> including living costs, on a dormitory-to-studio range. Tuition alone is
  €16,000 for medicine and from €17,350 for dentistry, which is why the medical budget sits so far above
  the €8,500 to €14,000 typical of other programmes.</p>
</div>
<p>Two costs are easy to forget. The programme runs six years rather than three or four, so the total
commitment is roughly €130,000 to €150,000; and the first year carries the one-off application, visa
and deposit charges on top.</p>""",
 """  <p><b>About €26,000</b> including living costs. That is Hun Education's own published figure for
  medicine and dentistry, and it sits far above the €8,500 to €14,000 typical of other programmes
  because tuition alone is €15,800 to $19,900.</p>
</div>
<p>Two costs are easy to forget. The programme runs six years rather than three or four, so the total
commitment is well over €100,000; and the first year carries the one-off application, visa and deposit
charges on top. If your programme is priced in dollars, budget for currency movement across six years.</p>"""),

("""<p>Two routes exist for applicants who are not yet at the required level. The <b>Pre-Medical Course</b>
at Szeged is a one-year foundation in chemistry and biology aimed directly at the entrance exam, from
€2,500 per term. The <b>English Language Foundation</b> programmes cover the language requirement for
applicants below B2. Both are in the <a href="{S['progs']}">catalogue</a>.</p>""",
 """<p>Two routes exist for applicants who are not yet at the required level.</p>
<div class="tablewrap">
<table class="dtable">
  <caption>Pre-medical and language routes</caption>
  <thead><tr><th>Programme</th><th>University</th><th>Annual fee</th></tr></thead>
  <tbody>
    <tr><td><b>PreMedical / PreEngineering / PreBusiness</b></td><td>University of Pécs (PTE)</td><td class="num">€5,850</td></tr>
    <tr><td><b>Two-semester Pre-Medical Track</b></td><td>McDaniel College Budapest</td><td class="num">€7,230</td></tr>
    <tr><td><b>Pre-Medical (Intensive)</b></td><td>McDaniel College Budapest</td><td class="num">€7,800</td></tr>
    <tr><td>English Language Preparatory</td><td>Several universities</td><td class="num">from €2,500</td></tr>
  </tbody>
</table>
</div>
<p>All of these are in the <a href="{S['progs']}">catalogue</a> with their current fees and deadlines.</p>"""),

("""    'Medicine in Hungary for international students: the chemistry and biology entrance exam, the '
    'six-year structure, €16,000 a year tuition, and what recognition requires afterwards.',""",
 """    'Medicine in Hungary for international students: the three universities that teach it, real annual '
    'fees from €15,800 to $19,900, the entrance assessment and what recognition requires afterwards.',"""),
("""    'Six years, taught in English, at four universities. What the entrance exam asks, how the years are '
    'structured and what the whole thing costs.',""",
 """    'Six years, taught in English, at three universities. What the entrance assessment asks, how the '
    'years are structured and what the whole thing really costs.',"""),
("""          (S['unis'],"Universities","Medical faculties","Semmelweis, Debrecen, Szeged and Pécs.")""",
 """          (S['unis'],"Universities","Medical faculties","Semmelweis, Pécs and Szeged.")"""),
]

TR = [
("""    ("Tıp yıllık ne kadar tutuyor?",
     "<p>Tıpta yıllık 16.000 €, diş hekimliğinde 17.350 €'dan başlıyor. Yaşam giderleri bunun üstüne "
     "eklenir; gerçekçi toplam yıllık yaklaşık 21.000 – 26.000 €.</p>"),""",
 """    ("Tıp yıllık ne kadar tutuyor?",
     "<p>Üniversiteye ve ücretin alındığı para birimine göre değişiyor: Semmelweis 19.900 $, Pécs "
     "18.000 $, Szeged 15.800 €. Pécs'te diş hekimliği 18.600 €. Hun Education'ın tıp ve diş için "
     "yayınladığı yaşam gideri dahil rakam yıllık yaklaşık 26.000 €.</p>"),"""),

("""  <p>Macaristan'da tıp, İngilizce yürüyen altı yıllık bütünleşik bir program ve yıllık 16.000 €;
  diş hekimliği beş yıl ve 17.350 €'dan başlıyor. Kabul, fakültenin kendi kimya ve biyoloji giriş
  sınavında düğümleniyor. Dört üniversite okutuyor: Semmelweis, Debrecen, Szeged ve Pécs. Sonrasında
  hekimlik yapmak, çalışacağınız ülkedeki denklik sürecine bağlı.</p>""",
 """  <p>Macaristan'da tıp, İngilizce yürüyen altı yıllık bütünleşik bir program ve <b>üç üniversitede</b>
  okutuluyor: Budapeşte'de Semmelweis, Pécs ve Szeged. Yıllık öğrenim ücretleri sırasıyla 19.900 $,
  18.000 $ ve 15.800 €; Pécs'te beş yıllık diş hekimliği 18.600 €. Kabul, fakültenin kendi kimya ve
  biyoloji değerlendirmesinde düğümleniyor. Sonrasında hekimlik yapmak, çalışacağınız ülkedeki denklik
  sürecine bağlı.</p>"""),

("""    <tr><td><b>Semmelweis Üniversitesi (SOTE)</b></td><td>Budapeşte</td><td>Tıp, Diş Hekimliği, Eczacılık</td><td class="num">16.000 – 17.350 €</td></tr>
    <tr><td><b>Debrecen Üniversitesi</b></td><td>Debrecen</td><td>Tıp, Diş Hekimliği</td><td class="num">16.000 – 17.350 €</td></tr>
    <tr><td><b>Szeged Üniversitesi (SZTE)</b></td><td>Szeged</td><td>Tıp, Tıp Hazırlık</td><td class="num">16.000 €</td></tr>
    <tr><td><b>Pécs Üniversitesi (PTE)</b></td><td>Pécs</td><td>Tıp, Hemşirelik</td><td class="num">16.000 €</td></tr>""",
 """    <tr><td><b>Semmelweis Üniversitesi (SOTE)</b></td><td>Budapeşte</td><td>Tıp (6 yıl)</td><td class="num">19.900 $</td></tr>
    <tr><td><b>Pécs Üniversitesi (PTE)</b></td><td>Pécs</td><td>Tıp (6 yıl)</td><td class="num">18.000 $</td></tr>
    <tr><td><b>Szeged Üniversitesi (SZTE)</b></td><td>Szeged</td><td>Tıp (6 yıl)</td><td class="num">15.800 €</td></tr>
    <tr><td><b>Pécs Üniversitesi (PTE)</b></td><td>Pécs</td><td>Diş Hekimliği (5 yıl)</td><td class="num">18.600 €</td></tr>
    <tr><td><b>Semmelweis Üniversitesi (SOTE)</b></td><td>Budapeşte</td><td>Eczacılık (5 yıl)</td><td class="num">12.600 €</td></tr>
    <tr><td><b>Pécs Üniversitesi (PTE)</b></td><td>Pécs</td><td>Eczacılık (5 yıl)</td><td class="num">8.800 €</td></tr>"""),

("""<h2 id="universiteler">Tıp nerede okutuluyor</h2>""",
 """<h2 id="universiteler">Tıp nerede okutuluyor</h2>
<p>Listede <b>olmayana</b> dikkat edin. Debrecen Macaristan'ın en bilinen tıp fakültelerinden biri ama
şu an başvuru gönderebildiğimiz programlar arasında değil. Semmelweis'te diş hekimliği İngilizce değil
Almanca yürütülüyor. Üç tıp programının ikisi <b>dolar</b> cinsinden fiyatlanıyor; yaşam gideriniz euro
olduğu için bu fark eder.</p>"""),

("""    <tr><td><b>Dersler</b></td><td>Kimya ve biyoloji</td></tr>
    <tr><td><b>Biçim</b></td><td>Üniversiteye göre yazılı veya sözlü; bazıları çevrim içi yapıyor</td></tr>""",
 """    <tr><td><b>Dersler</b></td><td>Kimya ve biyoloji</td></tr>
    <tr><td><b>Biçim</b></td><td>Üniversiteye göre değişir. Semmelweis değerlendirmesini mülakat olarak kaydediyor; Szeged çevrim içi yazılı ve sözlü sınav yapıyor.</td></tr>"""),

("""  <p><b>21.000 – 26.000 €</b>, yaşam giderleri dahil, yurttan stüdyoya uzanan aralıkta. Yalnız öğrenim
  ücreti tıpta 16.000 €, diş hekimliğinde 17.350 €'dan başlıyor; tıp bütçesinin diğer programların
  8.500 – 14.000 € bandının bu kadar üstünde olmasının sebebi bu.</p>
</div>
<p>Kolayca unutulan iki kalem var. Program üç dört yıl değil altı yıl sürüyor, yani toplam taahhüt
kabaca 130.000 – 150.000 €; ve ilk yıl başvuru, vize ve depozito gibi tek seferlik ücretleri ayrıca
taşıyor.</p>""",
 """  <p><b>Yaklaşık 26.000 €</b>, yaşam giderleri dahil. Bu Hun Education'ın tıp ve diş hekimliği için
  kendi yayınladığı rakam ve diğer programların 8.500 – 14.000 € bandının çok üstünde; çünkü yalnız
  öğrenim ücreti 15.800 € ile 19.900 $ arasında.</p>
</div>
<p>Kolayca unutulan iki kalem var. Program üç dört yıl değil altı yıl sürüyor, yani toplam taahhüt
100.000 €'nun belirgin şekilde üstünde; ve ilk yıl başvuru, vize ve depozito gibi tek seferlik
ücretleri ayrıca taşıyor. Programınız dolar cinsindense altı yıl boyunca kur hareketini de hesaba
katın.</p>"""),

("""<p>Şartları henüz karşılamayan adaylar için iki yol var. Szeged'deki <b>Tıp Hazırlık (Pre-Medical
Course)</b> doğrudan giriş sınavına yönelik bir yıllık kimya-biyoloji programı, dönemlik 2.500 €'dan
başlıyor. <b>İngilizce Dil Hazırlık</b> programları ise B2 altındaki adaylar için dil şartını
kapatıyor. İkisi de <a href="{S['progs']}">katalogda</a>.</p>""",
 """<p>Şartları henüz karşılamayan adaylar için iki yol var.</p>
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
<p>Hepsi güncel ücret ve son başvuru tarihleriyle <a href="{S['progs']}">katalogda</a>.</p>"""),

("""    "Macaristan'da tıp okumak: kimya-biyoloji giriş sınavı, altı yıllık program yapısı, yıllık "
    "16.000 € öğrenim ücreti ve mezuniyet sonrası denklik süreci.",""",
 """    "Macaristan'da tıp okumak: tıp okutan üç üniversite, 15.800 € ile 19.900 $ arasındaki gerçek "
    "yıllık ücretler, giriş değerlendirmesi ve mezuniyet sonrası denklik süreci.","""),
("""    'Altı yıl, İngilizce, dört üniversitede. Giriş sınavı ne soruyor, yıllar nasıl kurgulanıyor ve '
    'bütün bunun maliyeti ne?',""",
 """    'Altı yıl, İngilizce, üç üniversitede. Giriş değerlendirmesi ne soruyor, yıllar nasıl kurgulanıyor '
    've bütün bunun gerçek maliyeti ne?',"""),
("""          (S['unis'],"Üniversite","Tıp fakülteleri","Semmelweis, Debrecen, Szeged ve Pécs.")""",
 """          (S['unis'],"Üniversite","Tıp fakülteleri","Semmelweis, Pécs ve Szeged.")"""),
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
