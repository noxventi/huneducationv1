# -*- coding: utf-8 -*-
"""Görselleri sayfalara dağıtır: tek bölüme yığmadan, ilgili metnin yanına.

YERLEŞİM İLKESİ
  - Her sayfada birden çok görsel, farklı bölümlerde.
  - Kaydırılabilir şerit (strip) çok fotoğraflı yerlerde; tek figure ise
    bir bölümü tek kareyle destekleyeceği yerde.
  - Alt yazı görselde görüneni söyler, metindeki iddiayı tekrarlamaz.

Betik iki kez çalıştırılırsa tekrar eklemez: her ekleme öncesi görsel
adının dosyada olup olmadığına bakılır.
"""
import io

TR = {
# =====================================================================
# PİLOTAJ — gerçek öğrenci fotoğrafları, üç ayrı bölümde
# =====================================================================
'tools/pages_content6.py': [
 ('<h2 id="neden">Neden Macaristan?</h2>',
  '''{figure('pilotaj-hangar-egitim-ucagi',
        'Uçuş üniforması ve reflektif yelek giymiş öğrenci, hangarda çift motorlu eğitim uçağının önünde',
        'Macaristan’da pilotaj eğitimi alan öğrencimiz, eğitim uçağının önünde.',
        1008, 1344, oncelik=True)}

<h2 id="neden">Neden Macaristan?</h2>'''),
 ('<h2 id="nerede">Hangi üniversitelerde okutulur?</h2>',
  '''{strip('Pilotaj eğitiminden kareler', [
 ('pilotaj-ogrenciler-hangara-giderken',
  'Reflektif yelekli öğrenci grubu, çimenlikten uçak hangarına doğru yürürken',
  'Uçuş günü: öğrenciler hangara giderken.'),
 ('pilotaj-egitim-ucaklari-apron',
  'Apronda yan yana dizilmiş tek motorlu eğitim uçakları',
  'Eğitim filosu apronda.'),
 ('pilotaj-ogrenci-pervane',
  'Pilot üniformalı öğrenci, tek motorlu eğitim uçağının pervanesinin yanında',
  'Tek motorlu eğitim uçağıyla ilk saatler.'),
 ('pilotaj-ogrenciler-pist',
  'Pilot gömlekli üç öğrenci, uçuş alanında birlikte',
  'Uçuş alanında öğrencilerimiz.'),
 ('pilotaj-fuar-standi',
  'Üniformalı iki öğrenci, bir pilot akademisi fuar standının önünde',
  'Havacılık fuarında öğrencilerimiz.'),
])}

<h2 id="nerede">Hangi üniversitelerde okutulur?</h2>'''),
 ('<h2 id="sartlar">Başvurmadan önce hazırlamanız gerekenler</h2>',
  '''<h2 id="sartlar">Başvurmadan önce hazırlamanız gerekenler</h2>
{figure('pilotaj-ogrenciler-hangara-giderken',
        'Reflektif yelekli öğrenci grubu, çimenlikten uçak hangarına doğru yürürken',
        'Uçuş eğitimi, teorik derslerle aynı dönemde başlar.',
        1280, 720)}'''),

 # ---------------- TIP ----------------
 ('<h2 id="universiteler">Hangi üniversitelerde okutulur?</h2>',
  '''<h2 id="universiteler">Hangi üniversitelerde okutulur?</h2>
{strip('Tıp eğitimi veren üniversitelerden kareler', [
 ('semmelweis-tarihi-bina',
  'Semmelweis Üniversitesi’nin tarihi tuğla ve taş cepheli binası',
  'Semmelweis Üniversitesi, Budapeşte.'),
 ('semmelweis-modern-bina',
  'Semmelweis Üniversitesi’nin akşam ışıklandırılmış modern binası',
  'Semmelweis’in yeni eğitim binası.'),
 ('semmelweis-vitray',
  'Semmelweis Üniversitesi binasındaki renkli vitray pencere',
  'Tarihi binadan bir ayrıntı.'),
 ('pecs-kampus-hava',
  'Pécs Üniversitesi kampüsünün havadan görünümü',
  'Pécs Üniversitesi kampüsü.'),
 ('pecs-universitesi-tabela',
  'Pécs Üniversitesi binası; girişte “University of Pécs” tabelası',
  'Pécs’te fakülte girişi.'),
])}'''),
 ('<h2 id="sinav">Giriş sınavı ve hazırlık</h2>',
  '''<h2 id="sinav">Giriş sınavı ve hazırlık</h2>
{figure('bme-tarihi-salon',
        'Kemerli pencereleri olan tarihi çalışma salonu ve sıralar',
        'Giriş sınavı hazırlığı ortalama 6–10 hafta sürüyor.',
        1280, 720)}'''),
],

# =====================================================================
# ÜNİVERSİTELER + ANA REHBER
# =====================================================================
'tools/pages_content2.py': [
 # --- ana rehber: neden bölümü ---
 ('<h2 id="sistem">Eğitim sistemi ve dereceler</h2>',
  '''{strip('Macaristan üniversitelerinden kareler', [
 ('elte-tarihi-bina', 'ELTE’nin tarihi taş cepheli binası',
  'ELTE, Budapeşte.'),
 ('debrecen-ana-bina', 'Debrecen Üniversitesi’nin sütunlu ana binası ve önündeki havuz',
  'Debrecen Üniversitesi ana binası.'),
 ('szeged-ana-bina', 'Szeged Üniversitesi’nin sarı cepheli ana binası',
  'Szeged Üniversitesi.'),
 ('pecs-tas-kemer-giris', 'Pécs Üniversitesi’nin taş kemerli avlu girişi',
  'Pécs’te avlu girişi.'),
 ('bme-tuna-kiyisi', 'Tuna kıyısındaki tarihi üniversite binası ve nehirde bir gemi',
  'Tuna kıyısında üniversite binası.'),
])}

<h2 id="sistem">Eğitim sistemi ve dereceler</h2>'''),
 ('<h2 id="sehirler">Hangi şehirde okumalı?</h2>',
  '''<h2 id="sehirler">Hangi şehirde okumalı?</h2>
{figure('pecs-sehir-hava',
        'Pécs şehir merkezinin kırmızı çatılı havadan görünümü',
        'Pécs. Budapeşte dışındaki şehirlerde yaşam maliyeti belirgin şekilde düşük.',
        1280, 720)}'''),

 # --- üniversiteler sayfası ---
 ('<h2 id="liste">Üniversite listesi</h2>',
  '''<h2 id="liste">Üniversite listesi</h2>
{galeri([
 ('pecs-universitesi-tabela',
  'Pécs Üniversitesi binası; girişte “University of Pécs” tabelası',
  'Pécs Üniversitesi', 'Ülkenin en eski üniversitesi; tıp, diş hekimliği ve eczacılık.'),
 ('debrecen-cam-bina',
  'Debrecen Üniversitesi’nin cam cepheli modern binası',
  'Debrecen Üniversitesi', 'Sağlık ve mühendislikte köklü gelenek.'),
 ('elte-avlu',
  'ELTE’nin kemerli iç avlusu',
  'ELTE', 'Beşeri bilimler, sosyal bilimler ve psikoloji.'),
 ('szeged-modern-bina',
  'Szeged Üniversitesi’nin cam cepheli modern binası',
  'Szeged Üniversitesi', 'Tıp ve fen bilimleri; düşük yaşam maliyeti.'),
 ('miskolc-cam-bina',
  'Miskolc Üniversitesi’nin cam cepheli binası ve önündeki meydan',
  'Miskolc Üniversitesi', 'Mühendislik ve yer bilimleri.'),
 ('obuda-sari-bina',
  'Óbuda Üniversitesi’nin sarı cepheli tarihi binası',
  'Óbuda Üniversitesi', 'Budapeşte’de mühendislik ve bilişim.'),
 ('metu-bina-tabela',
  '“Budapesti Metropolitan Egyetem” yazılı yuvarlak kampüs binası',
  'Budapeşte Metropolitan', 'Tasarım, medya ve işletme.'),
 ('univet-avlu-heykeller',
  'Veteriner Üniversitesi’nin avlusu; iki yanda köpek heykelleri',
  'Veteriner Üniversitesi', 'Budapeşte’de veterinerlik eğitimi.'),
 ('corvinus-bina',
  'Corvinus Üniversitesi’nin modern cam ve taş cepheli binası',
  'Corvinus Üniversitesi', 'İşletme ve ekonomi.'),
])}'''),
 ('<h2 id="sehir">Şehre göre dağılım</h2>',
  '''<h2 id="sehir">Şehre göre dağılım</h2>
{strip('Üniversite şehirlerinden kareler', [
 ('miskolc-kampus-hava', 'Sonbaharda Miskolc Üniversitesi kampüsünün havadan panoraması',
  'Miskolc kampüsü sonbaharda.'),
 ('debrecen-kuleli-bina', 'Debrecen Üniversitesi’nin kuleli binası',
  'Debrecen’de kampüs.'),
 ('pecs-sonbahar-kampus', 'Sonbaharda Pécs Üniversitesi binası ve önündeki ağaçlar',
  'Pécs’te sonbahar.'),
 ('elte-gece-cephe', 'ELTE binasının gece ışıklandırılmış cephesi',
  'Budapeşte’de akşam.'),
])}'''),
],

# =====================================================================
# YAŞAM + ÖĞRENCİ GÖRÜŞLERİ
# =====================================================================
'tools/pages_content7.py': [
 ('<h2 id="konaklama">Öğrenciler nerede yaşar?</h2>',
  '''<h2 id="konaklama">Öğrenciler nerede yaşar?</h2>
{figure('szeged-yurt-binasi',
        'Szeged’de bir öğrenci yurdu binası ve önünden geçen yayalar',
        'Üniversite yurdu. Aylık 60 €’dan başlıyor.',
        1280, 720)}'''),
 ('<h2 id="sehir">Kampüs dışında hayat</h2>',
  '''<h2 id="sehir">Kampüs dışında hayat</h2>
{strip('Macaristan’da öğrenci hayatından kareler', [
 ('budapeste-balikci-tabyasi',
  'Balıkçı Tabyası’nın kemerinden gün doğumunda Budapeşte manzarası',
  'Balıkçı Tabyası, Budapeşte.'),
 ('budapeste-koprude-ogrenciler',
  'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci',
  'Özgürlük Köprüsü’nde öğrencilerimiz.'),
 ('obuda-yemekhane',
  'Óbuda Üniversitesi’nin geniş, aydınlık yemekhanesi',
  'Kampüs yemekhanesi.'),
 ('obuda-ogrenciler',
  'Óbuda Üniversitesi tabelası altında bankta oturan öğrenci grubu',
  'Ders arası.'),
 ('pecs-sehir-hava',
  'Pécs şehir merkezinin kırmızı çatılı havadan görünümü',
  'Pécs: yürünebilir bir üniversite şehri.'),
])}'''),

 # --- öğrenci görüşleri ---
 ('<h2 id="sesler">Kendi cümleleriyle</h2>',
  '''<h2 id="sesler">Kendi cümleleriyle</h2>
{strip('Öğrencilerimizden kareler', [
 ('metu-ogrenci-grubu', 'Kampüs bahçesinde toplanmış uluslararası öğrenci grubu',
  'Kampüste uluslararası öğrenciler.'),
 ('pilotaj-ogrenciler-pist', 'Pilot gömlekli üç öğrenci, uçuş alanında birlikte',
  'Pilotaj öğrencilerimiz uçuş alanında.'),
 ('budapeste-koprude-ogrenciler', 'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci',
  'Budapeşte’de bir hafta sonu.'),
 ('metu-ogrenci-portre', 'Kampüs koridorunda, cam cephenin önünde duran bir öğrenci',
  'Budapeşte Metropolitan kampüsü.'),
])}'''),
 ('<h2 id="temalar">Tekrar eden başlıklar</h2>',
  '''<h2 id="temalar">Tekrar eden başlıklar</h2>
{figure('metu-derslik',
        'Amfi dersliğinde dizüstü bilgisayar başında çalışan öğrenciler',
        'Dersler İngilizce; sınıflar uluslararası.',
        1280, 720)}'''),
],

# =====================================================================
# NEDEN MACARİSTAN + YÜKSEK LİSANS
# =====================================================================
'tools/pages_content5.py': [
 ('<h2 id="neden">Macaristan neden öne çıkar?</h2>',
  '''<h2 id="neden">Macaristan neden öne çıkar?</h2>
{strip('Macaristan’ın köklü üniversitelerinden kareler', [
 ('pecs-tas-kemer-giris', 'Pécs Üniversitesi’nin taş kemerli avlu girişi',
  'Pécs Üniversitesi, 1367’de kuruldu.'),
 ('semmelweis-tarihi-bina', 'Semmelweis Üniversitesi’nin tarihi tuğla ve taş cepheli binası',
  'Semmelweis’te tıp eğitimi 1769’a dayanıyor.'),
 ('elte-kutuphane', 'ELTE’nin ahşap raflı, iki katlı tarihi kütüphane salonu',
  'ELTE’nin tarihi kütüphanesi.'),
 ('bme-tuna-kiyisi', 'Tuna kıyısındaki tarihi üniversite binası ve nehirde bir gemi',
  'Tuna kıyısında üniversite binası.'),
])}'''),
 ("<h2 id=\"hayat\">Avrupa'nın ortasında bir öğrencilik</h2>",
  """<h2 id="hayat">Avrupa'nın ortasında bir öğrencilik</h2>
{figure('budapeste-balikci-tabyasi',
        'Balıkçı Tabyası’nın kemerinden gün doğumunda Budapeşte manzarası',
        'Buda Kalesi ve Tuna kıyısı UNESCO listesinde.',
        1280, 854)}"""),

 # --- yüksek lisans ---
 ('<h2 id="alanlar">Alanlar, ücretler ve süre</h2>',
  '''<h2 id="alanlar">Alanlar, ücretler ve süre</h2>
{strip('Yüksek lisans programlarından kareler', [
 ('corvinus-bina', 'Corvinus Üniversitesi’nin modern cam ve taş cepheli binası',
  'İşletme ve ekonomi: Corvinus.'),
 ('bme-kampus-ogrenciler', 'Kampüs çimenliğinde birlikte proje kuran öğrenci grubu',
  'Mühendislikte proje çalışması.'),
 ('metu-tasarim-atolye', 'Tasarım atölyesinde yere serilmiş baskı çalışmaları ve bir öğrenci',
  'Tasarım atölyesi.'),
 ('elte-kutuphane', 'ELTE’nin ahşap raflı, iki katlı tarihi kütüphane salonu',
  'Tez dönemi: ELTE kütüphanesi.'),
])}'''),
],

# =====================================================================
# BAŞVURU + MALİYET
# =====================================================================
'tools/pages_content.py': [
 ('<h2 id="sinav">Giriş sınavı ve mülakat</h2>',
  '''<h2 id="sinav">Giriş sınavı ve mülakat</h2>
{figure('metu-derslik',
        'Amfi dersliğinde dizüstü bilgisayar başında çalışan öğrenciler',
        'Değerlendirme, tek bir sınav gününe değil lise notlarınıza ve alan sınavına bakar.',
        1280, 720)}'''),
 ('<h2 id="takvim">Başvuru takvimi ve süreç</h2>',
  '''<h2 id="takvim">Başvuru takvimi ve süreç</h2>
{strip('Kampüslerden kareler', [
 ('debrecen-cam-bina', 'Debrecen Üniversitesi’nin cam cepheli modern binası',
  'Debrecen Üniversitesi.'),
 ('szeged-ana-bina', 'Szeged Üniversitesi’nin sarı cepheli ana binası',
  'Szeged Üniversitesi.'),
 ('obuda-sari-bina', 'Óbuda Üniversitesi’nin sarı cepheli tarihi binası',
  'Óbuda Üniversitesi, Budapeşte.'),
 ('metu-bina-tabela', '“Budapesti Metropolitan Egyetem” yazılı yuvarlak kampüs binası',
  'Budapeşte Metropolitan.'),
])}'''),
 # --- maliyet sayfası ---
 ('<h2 id="yasam">Yaşam giderleri</h2>',
  '''<h2 id="yasam">Yaşam giderleri</h2>
{figure('szeged-yurt-binasi',
        'Szeged’de bir öğrenci yurdu binası ve önünden geçen yayalar',
        'Yurt, bütçeyi en çok etkileyen tercih.',
        1280, 720)}'''),
],
}

EN = {
'tools/en_content6.py': [
 ('<h2 id="why">Why train in Hungary?</h2>',
  '''{figure('pilotaj-hangar-egitim-ucagi',
        'A student in flight uniform and high-visibility vest in front of a twin-engine training aircraft in a hangar',
        'One of our students on the pilot training programme, in front of a training aircraft.',
        1008, 1344, oncelik=True)}

<h2 id="why">Why train in Hungary?</h2>'''),
 ('<h2 id="where">Where it is taught</h2>',
  '''{strip('Scenes from pilot training', [
 ('pilotaj-ogrenciler-hangara-giderken',
  'A group of students in high-visibility vests walking across grass towards an aircraft hangar',
  'Flying day: students heading to the hangar.'),
 ('pilotaj-egitim-ucaklari-apron',
  'Single-engine training aircraft lined up on the apron',
  'The training fleet on the apron.'),
 ('pilotaj-ogrenci-pervane',
  'A student in pilot uniform beside the propeller of a single-engine training aircraft',
  'First hours on a single-engine trainer.'),
 ('pilotaj-ogrenciler-pist',
  'Three students in pilot shirts together at the airfield',
  'Our students at the airfield.'),
 ('pilotaj-fuar-standi',
  'Two students in uniform in front of a pilot academy exhibition stand',
  'Our students at an aviation fair.'),
])}

<h2 id="where">Where it is taught</h2>'''),
 ('<h2 id="universities">Where medicine is taught</h2>',
  '''<h2 id="universities">Where medicine is taught</h2>
{strip('Scenes from the medical universities', [
 ('semmelweis-tarihi-bina',
  'The historic brick and stone facade of Semmelweis University',
  'Semmelweis University, Budapest.'),
 ('semmelweis-modern-bina',
  'The modern Semmelweis University building lit at dusk',
  'Semmelweis’s newer teaching building.'),
 ('semmelweis-vitray',
  'A stained glass window inside the Semmelweis University building',
  'A detail from the historic building.'),
 ('pecs-kampus-hava',
  'An aerial view of the University of Pécs campus',
  'The University of Pécs campus.'),
 ('pecs-universitesi-tabela',
  'A University of Pécs building with the “University of Pécs” sign at the entrance',
  'A faculty entrance in Pécs.'),
])}'''),
],
'tools/en_content2.py': [
 ('<h2 id="system">The system and degrees</h2>',
  '''{strip('Scenes from Hungarian universities', [
 ('elte-tarihi-bina', 'The historic stone facade of ELTE', 'ELTE, Budapest.'),
 ('debrecen-ana-bina', 'The colonnaded main building of the University of Debrecen with its pool',
  'The main building in Debrecen.'),
 ('szeged-ana-bina', 'The yellow facade of the University of Szeged main building',
  'The University of Szeged.'),
 ('pecs-tas-kemer-giris', 'The stone archway entrance to a University of Pécs courtyard',
  'A courtyard entrance in Pécs.'),
 ('bme-tuna-kiyisi', 'A historic university building on the Danube bank with a boat on the river',
  'A university building on the Danube.'),
])}

<h2 id="system">The system and degrees</h2>'''),
 ('<h2 id="list">University list</h2>',
  '''<h2 id="list">University list</h2>
{galeri([
 ('pecs-universitesi-tabela',
  'A University of Pécs building with the “University of Pécs” sign at the entrance',
  'University of Pécs', 'The country’s oldest university; medicine, dentistry and pharmacy.'),
 ('debrecen-cam-bina',
  'A glass-fronted modern building at the University of Debrecen',
  'University of Debrecen', 'A long tradition in health sciences and engineering.'),
 ('elte-avlu', 'The arcaded inner courtyard at ELTE',
  'ELTE', 'Humanities, social sciences and psychology.'),
 ('szeged-modern-bina', 'A glass-fronted modern building at the University of Szeged',
  'University of Szeged', 'Medicine and sciences; low cost of living.'),
 ('miskolc-cam-bina', 'The glass-fronted building and forecourt at the University of Miskolc',
  'University of Miskolc', 'Engineering and earth sciences.'),
 ('obuda-sari-bina', 'The yellow historic building of Óbuda University',
  'Óbuda University', 'Engineering and IT in Budapest.'),
 ('metu-bina-tabela', 'The round campus building signed “Budapesti Metropolitan Egyetem”',
  'Budapest Metropolitan', 'Design, media and business.'),
 ('univet-avlu-heykeller',
  'The courtyard of the University of Veterinary Medicine, with dog statues on either side',
  'Veterinary Medicine', 'Veterinary training in Budapest.'),
 ('corvinus-bina', 'The modern glass and stone facade of Corvinus University',
  'Corvinus University', 'Business and economics.'),
])}'''),
],
'tools/en_content7.py': [
 ('<h2 id="accommodation">Where students live</h2>',
  '''<h2 id="accommodation">Where students live</h2>
{figure('szeged-yurt-binasi',
        'A student dormitory building in Szeged with people walking past',
        'A university dormitory. From €60 a month.',
        1280, 720)}'''),
 ('<h2 id="city">Life outside the campus</h2>',
  '''<h2 id="city">Life outside the campus</h2>
{strip('Scenes from student life in Hungary', [
 ('budapeste-balikci-tabyasi',
  'A view of Budapest at sunrise through an arch of the Fisherman’s Bastion',
  'The Fisherman’s Bastion, Budapest.'),
 ('budapeste-koprude-ogrenciler',
  'Two students on Liberty Bridge in Budapest',
  'Our students on Liberty Bridge.'),
 ('obuda-yemekhane', 'The large, bright canteen at Óbuda University',
  'A campus canteen.'),
 ('obuda-ogrenciler', 'A group of students on a bench under the Óbuda University sign',
  'Between classes.'),
 ('pecs-sehir-hava', 'An aerial view of the red rooftops of central Pécs',
  'Pécs: a walkable university city.'),
])}'''),
 ('<h2 id="voices">In their own words</h2>',
  '''<h2 id="voices">In their own words</h2>
{strip('Scenes from our students', [
 ('metu-ogrenci-grubu', 'A group of international students gathered in a campus garden',
  'International students on campus.'),
 ('pilotaj-ogrenciler-pist', 'Three students in pilot shirts together at the airfield',
  'Our pilot students at the airfield.'),
 ('budapeste-koprude-ogrenciler', 'Two students on Liberty Bridge in Budapest',
  'A weekend in Budapest.'),
 ('metu-ogrenci-portre', 'A student in a campus corridor in front of a glass facade',
  'The Budapest Metropolitan campus.'),
])}'''),
],
'tools/en_content5.py': [
 ('<h2 id="quality">What makes Hungary stand out</h2>',
  '''<h2 id="quality">What makes Hungary stand out</h2>
{strip('Scenes from Hungary’s long-established universities', [
 ('pecs-tas-kemer-giris', 'The stone archway entrance to a University of Pécs courtyard',
  'The University of Pécs was founded in 1367.'),
 ('semmelweis-tarihi-bina', 'The historic brick and stone facade of Semmelweis University',
  'Semmelweis has trained physicians since 1769.'),
 ('elte-kutuphane', 'The two-storey historic library hall at ELTE with wooden shelving',
  'The historic library at ELTE.'),
 ('bme-tuna-kiyisi', 'A historic university building on the Danube bank with a boat on the river',
  'A university building on the Danube.'),
])}'''),
 ('<h2 id="location">Student life in the middle of Europe</h2>',
  '''<h2 id="location">Student life in the middle of Europe</h2>
{figure('budapeste-balikci-tabyasi',
        'A view of Budapest at sunrise through an arch of the Fisherman’s Bastion',
        'Buda Castle and the Danube embankments are UNESCO-listed.',
        1280, 854)}'''),
 ('<h2 id="fields">Fields, fees and duration</h2>',
  '''<h2 id="fields">Fields, fees and duration</h2>
{strip('Scenes from master’s programmes', [
 ('corvinus-bina', 'The modern glass and stone facade of Corvinus University',
  'Business and economics: Corvinus.'),
 ('bme-kampus-ogrenciler', 'A group of students building a project on a campus lawn',
  'Project work in engineering.'),
 ('metu-tasarim-atolye', 'Print work laid out on the floor of a design studio with a student',
  'A design studio.'),
 ('elte-kutuphane', 'The two-storey historic library hall at ELTE with wooden shelving',
  'Thesis season: the ELTE library.'),
])}'''),
],
'tools/en_content.py': [
 ('<h2 id="exam">Entrance exams and interviews</h2>',
  '''<h2 id="exam">Entrance exams and interviews</h2>
{figure('metu-derslik',
        'Students working at laptops in a lecture theatre',
        'The decision rests on your school record and a subject assessment, not one exam day.',
        1280, 720)}'''),
 ('<h2 id="calendar">Calendar and process</h2>',
  '''<h2 id="calendar">Calendar and process</h2>
{strip('Scenes from the campuses', [
 ('debrecen-cam-bina', 'A glass-fronted modern building at the University of Debrecen',
  'University of Debrecen.'),
 ('szeged-ana-bina', 'The yellow facade of the University of Szeged main building',
  'University of Szeged.'),
 ('obuda-sari-bina', 'The yellow historic building of Óbuda University',
  'Óbuda University, Budapest.'),
 ('metu-bina-tabela', 'The round campus building signed “Budapesti Metropolitan Egyetem”',
  'Budapest Metropolitan.'),
])}'''),
 ('<h2 id="living">Living costs</h2>',
  '''<h2 id="living">Living costs</h2>
{figure('szeged-yurt-binasi',
        'A student dormitory building in Szeged with people walking past',
        'Accommodation is the choice that moves your budget most.',
        1280, 720)}'''),
],
}


def uygula(tablo, etiket):
    for yol, ciftler in tablo.items():
        s = io.open(yol, encoding='utf-8').read()
        n = atlanan = 0
        for a, b in ciftler:
            # aynı blok zaten yerleştiyse tekrar ekleme (görsel adı değil,
            # bloğun kendisi bakılır: aynı fotoğraf birden çok sayfada
            # ya da bölümde kullanılabilir)
            if b in s:
                atlanan += 1; continue
            if a in s:
                s = s.replace(a, b, 1); n += 1
            else:
                print('  ! eşleşmedi %s :: %s' % (yol, ' '.join(a.split())[:52]))
        io.open(yol, 'w', encoding='utf-8').write(s)
        print('%-4s %-26s %d eklendi%s' % (etiket, yol, n,
              (', %d atlandı' % atlanan) if atlanan else ''))


if __name__ == '__main__':
    uygula(TR, 'TR')
    uygula(EN, 'EN')
