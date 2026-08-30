# -*- coding: utf-8 -*-
"""Ana rehber sayfasi (Macaristan'da Egitim) icin ton duzenlemesi.

Bilgiler dogruydu ama cerceve savunmaciydi: vize bolumu "hicbir sirket
garanti veremez" diye aciliyor, denklik bolumu "garanti vermeyiz" diye
bitiyordu. Ayni gercekler kaliyor; okuyucu once ne kazandigini goruyor,
uyarilar ise "bunu sizin yerinize biz takip ediyoruz" cercevesine geciyor.
"""
import io

# --------------------------------------------------------------------- TR
TR = 'tools/pages_content2.py'
tr = io.open(TR, encoding='utf-8').read()

R_TR = [
# icindekiler
("""{toc([('kisa-cevap','Kısa cevap'),('neden','Neden Macaristan?'),('sistem','Eğitim sistemi ve dereceler'),
      ('dil','Eğitim dili'),('sehirler','Şehirler'),('vize','Vize ve oturum'),
      ('denklik','Denklik ve mezuniyet sonrası'),('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}""",
 """{toc([('kisa-cevap','Kısa cevap'),('neden','Neden Macaristan?'),('sistem','Eğitim sistemi ve dereceler'),
      ('dil','Eğitim dili'),('sehirler','Şehirler'),('vize','Vize ve oturum'),
      ('denklik','Denklik ve mezuniyet sonrası'),('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}"""),

# kisa cevap: kazanci one al
("""  <p>Macaristan, Avrupa Birliği üyesi bir ülke olarak İngilizce eğitim veren geniş bir program
  yelpazesi sunar. Lisans 3–4 yıl, yüksek lisans 2 yıl, tıp ve diş hekimliği gibi bütünleşik
  programlar 5–6 yıl sürer. Eğitim ve yaşam giderleri birlikte yıllık 8.500 – 14.000 € aralığındadır.
  YKS şartı yoktur ancak birçok bölümde üniversitenin kendi giriş sınavı uygulanır.</p>""",
 """  <p>Macaristan, AB üyesi bir ülkede İngilizce okuyup Avrupa'da geçerli bir diploma almanın en
  pratik yollarından biri. <b>YKS şartı yok</b>; üniversiteler kendi değerlendirmesini yapıyor.
  Lisans 3–4 yıl, yüksek lisans 2 yıl, tıp ve diş hekimliği gibi bütünleşik programlar 5–6 yıl
  sürüyor ve eğitim ile yaşam giderleri birlikte yıllık 8.500 – 14.000 € aralığında kalıyor.
  Kataloğumuzda 20 üniversitede 490 İngilizce program var.</p>"""),

# "neden" listesi: kanit bandi ekle
("""<h2 id="neden">Neden Macaristan?</h2>
<p>Macaristan'ı Türk öğrenciler için öne çıkaran şey tek bir avantaj değil, birkaç faktörün
birlikte çalışmasıdır:</p>""",
 """<h2 id="neden">Neden Macaristan?</h2>
{stats([('490', 'Başvuru yapabileceğiniz İngilizce program'),
        ('20', 'Kataloğumuzdaki üniversite'),
        ('8.500 €', 'Bir akademik yılın gerçekçi alt bütçesi'),
        ('YKS yok', 'Kabul üniversitenin kendi değerlendirmesiyle')])}
<p>Macaristan'ı Türk öğrenciler için öne çıkaran şey tek bir avantaj değil, birkaç faktörün
birlikte çalışmasıdır:</p>"""),

("""  <li><b>Köklü üniversite geleneği.</b> Ülkedeki üniversitelerin akademik geçmişi yüzyıllara
  dayanıyor.</li>""",
 """  <li><b>Köklü üniversite geleneği.</b> Pécs Üniversitesi 1367'de kuruldu, Semmelweis'te tıp eğitimi
  1769'a dayanıyor; Macar asıllı bilim insanları bugüne kadar 16 Nobel Ödülü kazandı.</li>"""),

("""  <li><b>Yerleşik Türk öğrenci topluluğu.</b> Özellikle Budapeşte, Debrecen ve Pécs'te güçlü bir
  destek ağı bulunuyor.</li>
</ul>""",
 """  <li><b>Yerleşik Türk öğrenci topluluğu.</b> Macaristan'da 40 bine yakın uluslararası öğrenci
  okuyor; Budapeşte, Debrecen ve Pécs'te güçlü bir Türk öğrenci ağı sizi bekliyor.</li>
</ul>
{inline_cta("Bu programlardan hangisine gerçekçi şansınız var? İlk görüşmede söyleyelim.")}"""),

# vize uyarisi: destek cercevesi
("""<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Vize kararı tamamen ilgili resmî makama aittir. Hiçbir danışmanlık şirketi vize garantisi veremez;
böyle bir vaatte bulunan kaynaklara temkinli yaklaşın. Vize alınamazsa, konsolosluğun yazılı ret gerekçesi
üniversiteye iletildikten sonra öğrenim ücreti genellikle 30 iş günü içinde iade edilir.</p>""",
 """<p>Vize dosyasını sizin yerinize biz kuruyoruz: hangi belgenin hangi sırayla hazırlanacağını,
randevu takvimini ve konsolosluğun beklediği formatı biliyoruz. Kararı elbette konsolosluk veriyor,
ama dosyanın eksiksiz gitmesi bizim işimiz.</p>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Güvenceniz şu: vize çıkmazsa, konsolosluğun yazılı ret gerekçesi üniversiteye iletildikten sonra
öğrenim ücreti genellikle 30 iş günü içinde iade edilir. Vize kararı resmî makama ait olduğu için
hiçbir danışmanlık şirketi garanti veremez; size garanti sözü veren bir kaynağa temkinli yaklaşın.</p>"""),

# denklik: destek cercevesi
("""<p>Denklik mevzuatı değişebildiği için <b>başvuru yapmadan önce</b> YÖK'ün güncel kurallarını
doğrudan incelemenizi öneririz. Program seçerken denklik açısından riskli olabilecek noktaları
görüşmede birlikte değerlendiririz, ancak sonuç hakkında garanti vermeyiz.</p>""",
 """<p>Bu adımı sonraya bırakmıyoruz: program seçerken denklik açısından dikkat edilmesi gereken
noktaları birlikte gözden geçiriyoruz, böylece mezuniyette sürprizle karşılaşmıyorsunuz. Mevzuat
değişebildiği için başvurudan önce YÖK'ün güncel kurallarını da doğrudan incelemenizi öneririz;
kararı veren kurum YÖK olduğu için sonuç hakkında taahhüt vermiyoruz.</p>"""),

# CTA
("""{acta("Nereden başlayacağınızdan emin değil misiniz?", "Akademik geçmişinizi ve hedeflerinizi konuşalım; size uygun 3–5 gerçekçi program önerelim.")}""",
 """{acta("Macaristan'da okumaya bugün başlayın", "Akademik geçmişinizi ve hedefinizi konuşalım; size uygun 3–5 gerçekçi programı ilk görüşmede önerelim. Görüşme ücretsiz, sonrası size kalmış.")}"""),

# meta
("""    "Macaristan'da Üniversite Eğitimi: Sistem, Şehirler, Ücretler (2026) | Hun Education",
    "Macaristan'da üniversite eğitimi rehberi: derece seviyeleri ve süreleri, eğitim dili, şehirler, "
    "yıllık maliyet, D tipi öğrenci vizesi ve YÖK denklik süreci.",
    'Ana rehber',
    "Macaristan'da üniversite eğitimi",
    'Sistem nasıl işliyor, hangi şehirde ne var, bütçe ne kadar ve diploma Türkiye’de ne anlama '
    'geliyor? Karar vermeden önce bilmeniz gereken her şey.',""",
 """    "Macaristan'da Üniversite Okumak: YKS'siz Kabul, Ücretler ve Şehirler (2026) | Hun Education",
    "Macaristan'da üniversite eğitimi rehberi: YKS'siz kabul, yıllık 8.500 – 14.000 € bütçe, "
    "İngilizce programlar, şehirler, D tipi öğrenci vizesi ve YÖK denklik süreci.",
    'Ana rehber',
    "Macaristan'da üniversite eğitimi",
    'YKS’siz kabul, baştan sona İngilizce eğitim ve Avrupa’da geçerli bir diploma. Sistem nasıl '
    'işliyor, hangi şehirde ne var ve süreç sizin için nasıl yürüyor?',"""),
]

# --------------------------------------------------------------------- EN
EN = 'tools/en_content2.py'
en = io.open(EN, encoding='utf-8').read()

R_EN = [
("""  <p>As a European Union member state, Hungary offers a wide range of degrees taught in English.
  A bachelor's takes 3–4 years, a master's 2 years, and integrated programmes such as medicine and
  dentistry 5–6 years. Tuition and living costs together run €8,500 – €14,000 a year. There is no
  national entrance exam requirement, but many programmes set an entrance exam of their own.</p>""",
 """  <p>Hungary is one of the most practical ways to study in English inside the EU and graduate with a
  degree that travels. <b>There is no national entrance exam</b>; universities run their own
  assessment. A bachelor's takes 3–4 years, a master's 2 years, and integrated programmes such as
  medicine and dentistry 5–6 years, with tuition and living costs together at €8,500 – €14,000 a year.
  Our catalogue holds 490 English-taught programmes at 20 universities.</p>"""),

("""<h2 id="why">Why Hungary?</h2>
<p>What makes Hungary stand out for international students is not a single advantage but several
factors working together:</p>""",
 """<h2 id="why">Why Hungary?</h2>
{stats([('490', 'English-taught programmes you can apply to'),
        ('20', 'Universities in our catalogue'),
        ('€8,500', 'The realistic lower bound for one academic year'),
        ('No exam', 'Admission runs on the university\\'s own assessment')])}
<p>What makes Hungary stand out for international students is not a single advantage but several
factors working together:</p>"""),

("""{acta("Not sure where to start?", "Let us talk through your academic record and your goals, and put 3–5 realistic programmes in front of you.")}""",
 """{acta("Start your Hungarian degree today", "Tell us about your academic background and your goal, and we will name 3–5 realistic programmes in the first conversation. The consultation is free; what happens next is up to you.")}"""),
]


def uygula(yol, metin, ciftler, etiket):
    n = 0
    for a, b in ciftler:
        if a == b:
            continue
        if a in metin:
            metin = metin.replace(a, b); n += 1
        else:
            print('  ! eslesmedi %s :: %s' % (etiket, ' '.join(a.split())[:72]))
    io.open(yol, 'w', encoding='utf-8').write(metin)
    print('%-22s %d degisiklik' % (etiket, n))


uygula(TR, tr, R_TR, 'pages_content2')
uygula(EN, en, R_EN, 'en_content2')
