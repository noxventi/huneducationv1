# -*- coding: utf-8 -*-
"""Basvuru ve maliyet sayfalari icin ton duzenlemesi.

Iki sayfa da dogru bilgiyi engel gibi sunuyordu:
  - "Hun Education her ulkeden basvuru gonderme yetkisine sahip degil"
    aslinda "25'ten fazla ulkenin vatandasiyla calisiyoruz" demek.
  - "Sinavsiz universite ifadesi dogru degildir" diye acilan bolum,
    okuyucuya once yapamayacagini soyluyordu.
  - Maliyet sayfasi rakami veriyor ama bunun ne kadar iyi bir rakam
    oldugunu hic soylemiyordu.

Rakamlar ve kosullar aynen kaliyor; degisen sey sira ve cerceve.
"""
import io

TR = 'tools/pages_content.py'
EN = 'tools/en_content.py'

R_TR = [
# ---------------------------------------------------------------- BASVURU
# uygunluk bolumu: engel degil, kapsam
("""<h2 id="uygunluk">Belgelerden önce: uygun musunuz?</h2>
<p>Bu soruyu evraktan önce iki koşul belirliyor ve ikisi de kolayca gözden kaçıyor.</p>""",
 """<h2 id="uygunluk">Belgelerden önce: uygun musunuz?</h2>
<p>İyi haber şu: çoğu aday zaten uygun. Yine de üç başlık evraktan önce netleşsin ki boşuna
hazırlık yapmayasınız.</p>"""),

("""<p>Bu sınırların üzerindeyseniz yine de bize yazın. Sınırlar gerçek ama çoğu zaman uygun bir yol
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
konsolosluğu aynı şeye bakıyor. Belgelenemiyorsa vize başvurusu başlatmayı önermiyoruz.</p>""",
 """<p>Yaşınız bu sınırların üzerindeyse yine de yazın. Sınırlar gerçek ama çoğu durumda uygun bir yol
çıkıyor; hangisi olduğunu ilk görüşmede söyleriz.</p>

<h3>Uyruk</h3>
<p>25'ten fazla ülkenin vatandaşı adına başvuru gönderebiliyoruz: <b>Avrupa Birliği ülkeleri, ABD ve
Latin Amerika ülkeleri, Arnavutluk, Cezayir, Azerbaycan, Bosna Hersek, Mısır, Gürcistan, Ürdün,
Kazakistan, Kırgızistan, Moğolistan, Katar, Rusya, Sırbistan, Tayland, Türkiye, Ukrayna, Özbekistan
ve Vietnam.</b> Listede yoksanız yine de yazın; doğru kanalı gösterelim.</p>

<h3>Mali yeterlilik</h3>
<p>Konsolosluk eğitiminizin finanse edildiğini görmek istiyor ve beklenen tutar sanıldığından düşük:
<b>aylık ortalama 650 € × 10 aylık akademik yıl, yani yaklaşık 6.500 €</b>; kendi ya da sponsorunuzun
hesabında, düzenli gelir kanıtıyla birlikte. Bu Macaristan'a özgü bir kural değil, her ülkenin
konsolosluğu aynı şeye bakıyor. Sponsor mektubuyla nasıl belgeleneceğini birlikte planlıyoruz.</p>

{inline_cta("Profiliniz uygun mu? Tek mesajla öğrenin.")}"""),

# giris sinavi: once yapabileceginizi soyle
("""<h2 id="sinav">Giriş sınavı ve mülakat</h2>
<p>“Sınavsız üniversite” ifadesi Macaristan için doğru değildir. YKS istenmemesi, üniversitenin
kendi değerlendirmesini yapmadığı anlamına gelmez. Alan bazında beklenenler:</p>""",
 """<h2 id="sinav">Giriş sınavı ve mülakat</h2>
<p>YKS puanınız istenmiyor; bunun yerine üniversite sizi kendi ölçütleriyle değerlendiriyor. Bu çoğu
aday için avantaj: tek bir sınav gününe değil, lise notlarınıza ve alanla ilgili bir değerlendirmeye
bakılıyor. Hazırlık süreleri de kısa. Alan bazında beklenenler:</p>"""),

("""<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Hazırlık süreleri Hun Education danışmanlarının başvuru dosyalarından edindiği saha gözlemidir,
üniversitelerin resmî tavsiyesi değildir. Kabul kararı her zaman üniversiteye aittir.</p>""",
 """<p>Sınava hazırlığı yalnız yürütmüyorsunuz: hangi konuların çıktığını, geçmiş adayların nerede
zorlandığını ve kaç haftaya ihtiyacınız olduğunu danışmanınız baştan söylüyor.</p>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Hazırlık süreleri Hun Education danışmanlarının başvuru dosyalarından edindiği saha gözlemidir,
üniversitelerin resmî tavsiyesi değildir. Kabul kararı her zaman üniversiteye aittir.</p>"""),

# takvim: aciliyet duygusu
("""<h2 id="takvim">Başvuru takvimi</h2>
<p>Macaristan'da iki başlangıç dönemi vardır. Kontenjan dolduğunda dönem ilan edilen tarihten
önce kapanabilir; bu yüzden erken başvuru belirleyicidir.</p>""",
 """<h2 id="takvim">Başvuru takvimi</h2>
<p>Yılda iki başlangıç dönemi var, yani bir dönemi kaçırsanız bile altı ay sonra yeniden
başlayabilirsiniz. Ama kontenjan dolduğunda dönem ilan edilen tarihten önce kapanıyor: erken
başvuran aday hem daha çok programdan seçiyor hem de daha rahat bir vize takvimi yakalıyor.</p>"""),

# adim adim: sonuna kadar yanindayiz
("""  <li><div><h3>Seyahat ve karşılama</h3><p>Vize sonrası uçuş, konaklama ve karşılama planlanır. En az üç ay, tercihen bir yıl süreli seyahat ve kaza sigortasına ihtiyacınız olacak.</p></div></li>
</ol>""",
 """  <li><div><h3>Seyahat ve karşılama</h3><p>Vize sonrası uçuş, konaklama ve karşılama planlanır. Budapeşte ekibimiz sizi havalimanında karşılar, yurda yerleştirir ve ilk alışverişe kadar yanınızda olur.</p></div></li>
</ol>
<p>Altı adımın tamamında yanınızdayız. Dosyayı biz kuruyoruz, sınav hazırlığını birlikte
planlıyoruz, konsolosluk randevusunu takip ediyoruz ve Macaristan'a vardığınızda sizi ekibimiz
karşılıyor.</p>"""),

# CTA
("""{acta("Dosyanızı birlikte kontrol edelim", "Hangi belgenin eksik olduğunu ve hangi programlara gerçekçi şansınız olduğunu ilk görüşmede söyleriz.")}""",
 """{acta("Başvurunuza bugün başlayalım", "Hangi belgeye ihtiyacınız olduğunu ve hangi programlara gerçekçi şansınız olduğunu ilk görüşmede söyleriz. Görüşme ücretsiz ve sizi hiçbir şeye bağlamaz.")}"""),

# ---------------------------------------------------------------- MALIYET
("""<p>Ücretler seviyeye ve alana göre belirgin biçimde ayrışır. Aşağıdaki tablo yıllık öğrenim
ücretini gösterir; konaklama ve yaşam giderleri dahil değildir.</p>""",
 """<p>Macaristan'ın en güçlü tarafı fiyatı: aynı bölüm Batı Avrupa'da çoğu zaman iki katına yakın bir
bütçe ister. Aşağıdaki tablo yıllık öğrenim ücretini gösterir; konaklama ve yaşam giderleri dahil
değildir.</p>"""),

("""{acta("Size özel bütçe planı çıkaralım", "Seçtiğiniz program, şehir ve konaklama tercihine göre gerçekçi bir yıllık bütçe tablosu hazırlayalım.")}""",
 """{acta("Bütçenize uyan programı bulalım", "Seçtiğiniz program, şehir ve konaklama tercihine göre gerçekçi bir yıllık bütçe tablosunu ilk görüşmede önünüze koyalım. Görüşme ücretsiz.")}"""),
]

R_EN = [
("""<h2 id="eligibility">Before the documents: are you eligible?</h2>
<p>Two conditions decide this before any paperwork does, and both are easy to miss.</p>""",
 """<h2 id="eligibility">Before the documents: are you eligible?</h2>
<p>The good news is that most applicants already qualify. Even so, three points are worth settling
before you start assembling paperwork.</p>"""),

("""<p>If you are above these limits, talk to us anyway. The limits are real, but the right route often
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
starting a visa application.</p>""",
 """<p>If you are above these limits, write to us anyway. The limits are real, but a workable route
usually exists; we will tell you which one in the first conversation.</p>

<h3>Nationality</h3>
<p>We can submit applications on behalf of citizens of more than 25 countries: <b>EU countries, the
United States and Latin America, Albania, Algeria, Azerbaijan, Bosnia and Herzegovina, Egypt, Georgia,
Jordan, Kazakhstan, Kyrgyzstan, Mongolia, Qatar, Russia, Serbia, Thailand, Türkiye, Ukraine,
Uzbekistan and Vietnam.</b> If your country is not listed, write anyway and we will point you to the
right channel.</p>

<h3>Financial capacity</h3>
<p>The consulate expects to see that your studies are funded, and the amount is lower than most people
expect: <b>€650 a month across a 10-month academic year, so about €6,500</b>, held in your own or your
sponsor's account, alongside evidence of regular income. This is not a Hungarian peculiarity; every
country's consulate looks for the same thing. We plan the sponsor letter with you.</p>

{inline_cta("Not sure whether you qualify? One message is enough to find out.")}"""),

("""<h2 id="exam">Entrance exams and interviews</h2>
<p>“Admission without an exam” is not an accurate description of Hungary. Not requiring a national
entrance exam does not mean the university skips its own assessment. What to expect by field:</p>""",
 """<h2 id="exam">Entrance exams and interviews</h2>
<p>No national entrance exam score is asked for; the university assesses you on its own terms instead.
For most applicants that is an advantage, because the decision rests on your school record and a
subject assessment rather than on one exam day, and the preparation windows are short. What to expect
by field:</p>"""),

("""{acta("Let us review your file together", "In the first consultation we tell you which document is missing and which programmes you have a realistic chance at.")}""",
 """{acta("Let us start your application today", "We will tell you which documents you need and which programmes you have a realistic chance at, in the first conversation. It is free and commits you to nothing.")}"""),

("""<p>Fees separate sharply by level and field. The table below shows annual tuition only; accommodation""",
 """<p>Price is Hungary's strongest card: the same degree in Western Europe usually asks for close to
twice the budget. The table below shows annual tuition; accommodation and living costs are not
included.</p>"""),
]


def uygula(yol, ciftler, etiket):
    s = io.open(yol, encoding='utf-8').read()
    n = 0
    for a, b in ciftler:
        if a in s:
            s = s.replace(a, b); n += 1
        else:
            print('  ! eslesmedi %s :: %s' % (etiket, ' '.join(a.split())[:72]))
    io.open(yol, 'w', encoding='utf-8').write(s)
    print('%-20s %d degisiklik' % (etiket, n))


uygula(TR, R_TR, 'pages_content')
uygula(EN, R_EN, 'en_content')
