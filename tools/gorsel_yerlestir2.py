# -*- coding: utf-8 -*-
"""İkinci yerleştirme turu: boş kalan bölümleri ve sayfaları kapatır.

Birinci tur bazı sayfalara tek bölümde görsel bırakmıştı; hakkımızda,
iletişim ve maliyet sayfalarında hiç görsel yoktu. Burada her sayfa en az
iki ayrı bölümde görsel görüyor, İngilizce ve Türkçe tarafı eşitleniyor.

Aynı blok ikinci kez eklenmez: uygula() bloğun kendisini arar.
"""
import io
from gorsel_yerlestir import uygula

TR = {
# ---------------------------------------------------------------- başvuru + maliyet
'tools/pages_content.py': [
 ('<h2 id="uygunluk">Kimler başvurabilir?</h2>',
  '''<h2 id="uygunluk">Kimler başvurabilir?</h2>
{strip('Öğrencilerimizden kareler', [
 ('metu-ogrenci-grubu', 'Kampüs bahçesinde toplanmış uluslararası öğrenci grubu',
  'Kampüste uluslararası öğrenciler.'),
 ('obuda-ogrenciler', 'Óbuda Üniversitesi tabelası altında bankta oturan öğrenci grubu',
  'Ders arası.'),
 ('budapeste-koprude-ogrenciler', 'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci',
  'Özgürlük Köprüsü’nde öğrencilerimiz.'),
 ('pilotaj-ogrenciler-pist', 'Pilot gömlekli üç öğrenci, uçuş alanında birlikte',
  'Pilotaj öğrencilerimiz uçuş alanında.'),
])}'''),
 # --- maliyet sayfası ---
 ('<h2 id="ogrenim">Öğrenim ücretleri</h2>',
  '''<h2 id="ogrenim">Öğrenim ücretleri</h2>
{strip('Ücretlerin değiştiği üniversitelerden kareler', [
 ('semmelweis-modern-bina', 'Semmelweis Üniversitesi’nin akşam ışıklandırılmış modern binası',
  'Semmelweis Üniversitesi, Budapeşte.'),
 ('debrecen-kuleli-bina', 'Debrecen Üniversitesi’nin kuleli binası',
  'Debrecen Üniversitesi.'),
 ('corvinus-bina', 'Corvinus Üniversitesi’nin modern cam ve taş cepheli binası',
  'Corvinus Üniversitesi.'),
 ('miskolc-cam-bina', 'Miskolc Üniversitesi’nin cam cepheli binası ve önündeki meydan',
  'Miskolc Üniversitesi.'),
 ('elte-tarihi-bina', 'ELTE’nin tarihi taş cepheli binası',
  'ELTE, Budapeşte.'),
])}'''),
 ('<h2 id="toplam">Yıllık toplam bütçe</h2>',
  '''<h2 id="toplam">Yıllık toplam bütçe</h2>
{figure('pecs-sehir-hava',
        'Pécs şehir merkezinin kırmızı çatılı havadan görünümü',
        'Pécs: Budapeşte dışında bir üniversite şehri.')}'''),
],

# ---------------------------------------------------------------- rehber + üniversiteler
'tools/pages_content2.py': [
 ('<h2 id="neden">Neden Macaristan?</h2>',
  '''<h2 id="neden">Neden Macaristan?</h2>
{figure('budapeste-balikci-tabyasi',
        'Balıkçı Tabyası’nın kemerinden gün doğumunda Budapeşte manzarası',
        'Balıkçı Tabyası’ndan Budapeşte.')}'''),
 ('<h2 id="secim">Nasıl seçmeli?</h2>',
  '''<h2 id="secim">Nasıl seçmeli?</h2>
{figure('pecs-kampus-hava',
        'Pécs Üniversitesi kampüsünün havadan görünümü',
        'Pécs Üniversitesi kampüsü, havadan.')}'''),
],

# ---------------------------------------------------------------- hakkımızda + iletişim
'tools/pages_content3.py': [
 ('<h2 id="hikaye">Kuruluş ve bugün</h2>',
  '''<h2 id="hikaye">Kuruluş ve bugün</h2>
{strip('Öğrencilerimizden kareler', [
 ('pilotaj-ogrenciler-pist', 'Pilot gömlekli üç öğrenci, uçuş alanında birlikte',
  'Pilotaj öğrencilerimiz uçuş alanında.'),
 ('budapeste-koprude-ogrenciler', 'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci',
  'Özgürlük Köprüsü’nde öğrencilerimiz.'),
 ('pilotaj-fuar-standi', 'Üniformalı iki öğrenci, bir pilot akademisi fuar standının önünde',
  'Havacılık fuarında öğrencilerimiz.'),
 ('metu-ogrenci-grubu', 'Kampüs bahçesinde toplanmış uluslararası öğrenci grubu',
  'Kampüste uluslararası öğrenciler.'),
 ('obuda-ogrenciler', 'Óbuda Üniversitesi tabelası altında bankta oturan öğrenci grubu',
  'Ders arası.'),
])}'''),
 ('<h2 id="nasil">Nasıl çalışıyoruz</h2>',
  '''<h2 id="nasil">Nasıl çalışıyoruz</h2>
{figure('debrecen-ana-bina',
        'Debrecen Üniversitesi’nin sütunlu ana binası ve önündeki havuz',
        'Debrecen Üniversitesi ana binası.')}'''),
 # --- iletişim ---
 ('<h2 id="kanallar">İletişim kanalları</h2>',
  '''<h2 id="kanallar">İletişim kanalları</h2>
{figure('budapeste-koprude-ogrenciler',
        'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci',
        'Özgürlük Köprüsü’nde öğrencilerimiz.')}'''),
],

# ---------------------------------------------------------------- neden Macaristan + yüksek lisans
'tools/pages_content5.py': [
 ('<h2 id="maliyet">Eğitim ve yaşam maliyetleri</h2>',
  '''<h2 id="maliyet">Eğitim ve yaşam maliyetleri</h2>
{figure('szeged-yurt-binasi',
        'Szeged’de bir öğrenci yurdu binası ve önünden geçen yayalar',
        'Szeged’de bir öğrenci yurdu.')}'''),
 ('<h2 id="kime">Kimler için uygun?</h2>',
  '''<h2 id="kime">Kimler için uygun?</h2>
{figure('metu-ogrenci-portre',
        'Kampüs koridorunda, cam cephenin önünde duran bir öğrenci',
        'Budapeşte Metropolitan kampüsünde bir öğrenci.')}'''),
 ('<h2 id="sartlar">Kabul şartları ve başvuru</h2>',
  '''<h2 id="sartlar">Kabul şartları ve başvuru</h2>
{figure('elte-avlu',
        'ELTE’nin kemerli iç avlusu',
        'ELTE’nin iç avlusu.')}'''),
],

# ---------------------------------------------------------------- tıp + pilotaj
'tools/pages_content6.py': [
 ('<h2 id="yapi">Altı yıl nasıl ilerler?</h2>',
  '''<h2 id="yapi">Altı yıl nasıl ilerler?</h2>
{figure('metu-derslik',
        'Amfi dersliğinde dizüstü bilgisayar başında çalışan öğrenciler',
        'Amfi derslikte ders saati.')}'''),
 ('<h2 id="ucret">Ücretler ve neyi kapsar</h2>',
  '''<h2 id="ucret">Ücretler ve neyi kapsar</h2>
{figure('pilotaj-egitim-ucaklari-apron',
        'Apronda yan yana dizilmiş tek motorlu eğitim uçakları',
        'Eğitim filosu apronda.')}'''),
],

# ---------------------------------------------------------------- yaşam + görüşler
'tools/pages_content7.py': [
 ('<h2 id="aylik">Bir ay ne kadar tutar?</h2>',
  '''<h2 id="aylik">Bir ay ne kadar tutar?</h2>
{figure('obuda-yemekhane',
        'Óbuda Üniversitesi’nin geniş, aydınlık yemekhanesi',
        'Kampüs yemekhanesi.')}'''),
 ('<h2 id="ilkay">İlk ayınız, adım adım</h2>',
  '''<h2 id="ilkay">İlk ayınız, adım adım</h2>
{figure('metu-ogrenci-grubu',
        'Kampüs bahçesinde toplanmış uluslararası öğrenci grubu',
        'Kampüste uluslararası öğrenciler.')}'''),
],
}

EN = {
'tools/en_content.py': [
 ('<h2 id="eligibility">Who can apply?</h2>',
  '''<h2 id="eligibility">Who can apply?</h2>
{strip('Scenes from our students', [
 ('metu-ogrenci-grubu', 'A group of international students gathered in a campus garden',
  'International students on campus.'),
 ('obuda-ogrenciler', 'A group of students on a bench under the Óbuda University sign',
  'Between classes.'),
 ('budapeste-koprude-ogrenciler', 'Two students on Liberty Bridge in Budapest',
  'Our students on Liberty Bridge.'),
 ('pilotaj-ogrenciler-pist', 'Three students in pilot shirts together at the airfield',
  'Our pilot students at the airfield.'),
])}'''),
 ('<h2 id="tuition">Tuition fees</h2>',
  '''<h2 id="tuition">Tuition fees</h2>
{strip('Scenes from the universities where fees vary', [
 ('semmelweis-modern-bina', 'The modern Semmelweis University building lit at dusk',
  'Semmelweis University, Budapest.'),
 ('debrecen-kuleli-bina', 'The towered building of the University of Debrecen',
  'University of Debrecen.'),
 ('corvinus-bina', 'The modern glass and stone facade of Corvinus University',
  'Corvinus University.'),
 ('miskolc-cam-bina', 'The glass-fronted building and forecourt at the University of Miskolc',
  'University of Miskolc.'),
 ('elte-tarihi-bina', 'The historic stone facade of ELTE', 'ELTE, Budapest.'),
])}'''),
 ('<h2 id="total">Your annual total</h2>',
  '''<h2 id="total">Your annual total</h2>
{figure('pecs-sehir-hava',
        'An aerial view of the red rooftops of central Pécs',
        'Pécs: a university city outside Budapest.')}'''),
],

'tools/en_content2.py': [
 ('<h2 id="why">Why Hungary?</h2>',
  '''<h2 id="why">Why Hungary?</h2>
{figure('budapeste-balikci-tabyasi',
        'A view of Budapest at sunrise through an arch of the Fisherman’s Bastion',
        'Budapest from the Fisherman’s Bastion.')}'''),
 ('<h2 id="cities">Which city should you choose?</h2>',
  '''<h2 id="cities">Which city should you choose?</h2>
{figure('pecs-sehir-hava',
        'An aerial view of the red rooftops of central Pécs',
        'Pécs. Living costs outside Budapest are markedly lower.')}'''),
 ('<h2 id="by-city">Distribution by city</h2>',
  '''<h2 id="by-city">Distribution by city</h2>
{strip('Scenes from the university cities', [
 ('miskolc-kampus-hava', 'An aerial panorama of the University of Miskolc campus in autumn',
  'The Miskolc campus in autumn.'),
 ('debrecen-kuleli-bina', 'The towered building of the University of Debrecen',
  'A campus in Debrecen.'),
 ('pecs-sonbahar-kampus', 'A University of Pécs building among autumn trees',
  'Autumn in Pécs.'),
 ('elte-gece-cephe', 'The ELTE facade lit at night', 'An evening in Budapest.'),
])}'''),
 ('<h2 id="choosing">How to choose</h2>',
  '''<h2 id="choosing">How to choose</h2>
{figure('pecs-kampus-hava',
        'An aerial view of the University of Pécs campus',
        'The University of Pécs campus from the air.')}'''),
],

'tools/en_content3.py': [
 ('<h2 id="story">Then and now</h2>',
  '''<h2 id="story">Then and now</h2>
{strip('Scenes from our students', [
 ('pilotaj-ogrenciler-pist', 'Three students in pilot shirts together at the airfield',
  'Our pilot students at the airfield.'),
 ('budapeste-koprude-ogrenciler', 'Two students on Liberty Bridge in Budapest',
  'Our students on Liberty Bridge.'),
 ('pilotaj-fuar-standi', 'Two students in uniform in front of a pilot academy exhibition stand',
  'Our students at an aviation fair.'),
 ('metu-ogrenci-grubu', 'A group of international students gathered in a campus garden',
  'International students on campus.'),
 ('obuda-ogrenciler', 'A group of students on a bench under the Óbuda University sign',
  'Between classes.'),
])}'''),
 ('<h2 id="how">How we work</h2>',
  '''<h2 id="how">How we work</h2>
{figure('debrecen-ana-bina',
        'The colonnaded main building of the University of Debrecen with its pool',
        'The main building in Debrecen.')}'''),
 ('<h2 id="channels">Contact channels</h2>',
  '''<h2 id="channels">Contact channels</h2>
{figure('budapeste-koprude-ogrenciler',
        'Two students on Liberty Bridge in Budapest',
        'Our students on Liberty Bridge.')}'''),
],

'tools/en_content5.py': [
 ('<h2 id="cost">Tuition and living costs</h2>',
  '''<h2 id="cost">Tuition and living costs</h2>
{figure('szeged-yurt-binasi',
        'A student dormitory building in Szeged with people walking past',
        'A student dormitory in Szeged.')}'''),
 ('<h2 id="who">Who a Hungarian master\'s suits</h2>',
  '''<h2 id="who">Who a Hungarian master\'s suits</h2>
{figure('metu-ogrenci-portre',
        'A student in a campus corridor in front of a glass facade',
        'A student on the Budapest Metropolitan campus.')}'''),
 ('<h2 id="requirements">Entry requirements and applying</h2>',
  '''<h2 id="requirements">Entry requirements and applying</h2>
{figure('elte-avlu',
        'The arcaded inner courtyard at ELTE',
        'The inner courtyard at ELTE.')}'''),
],

'tools/en_content6.py': [
 ('<h2 id="exam">The entrance exam and preparation</h2>',
  '''<h2 id="exam">The entrance exam and preparation</h2>
{figure('bme-tarihi-salon',
        'A historic study hall with arched windows and rows of desks',
        'Preparation takes 6–10 weeks on average.')}'''),
 ('<h2 id="structure">How the six years run</h2>',
  '''<h2 id="structure">How the six years run</h2>
{figure('metu-derslik',
        'Students working at laptops in a lecture theatre',
        'A teaching hour in the lecture theatre.')}'''),
 ('<h2 id="cost">How the cost is built</h2>',
  '''<h2 id="cost">How the cost is built</h2>
{figure('pilotaj-egitim-ucaklari-apron',
        'Single-engine training aircraft lined up on the apron',
        'The training fleet on the apron.')}'''),
 ('<h2 id="requirements">What to arrange before you apply</h2>',
  '''<h2 id="requirements">What to arrange before you apply</h2>
{figure('pilotaj-ogrenciler-hangara-giderken',
        'A group of students in high-visibility vests walking across grass towards an aircraft hangar',
        'Flight training starts alongside the theory terms.')}'''),
],

'tools/en_content7.py': [
 ('<h2 id="monthly">What a month costs</h2>',
  '''<h2 id="monthly">What a month costs</h2>
{figure('obuda-yemekhane',
        'The large, bright canteen at Óbuda University',
        'A campus canteen.')}'''),
 ('<h2 id="firstmonth">Your first month, step by step</h2>',
  '''<h2 id="firstmonth">Your first month, step by step</h2>
{figure('metu-ogrenci-grubu',
        'A group of international students gathered in a campus garden',
        'International students on campus.')}'''),
 ('<h2 id="themes">What comes up repeatedly</h2>',
  '''<h2 id="themes">What comes up repeatedly</h2>
{figure('metu-derslik',
        'Students working at laptops in a lecture theatre',
        'Teaching is in English; the classes are international.')}'''),
],
}

uygula(TR, 'TR')
uygula(EN, 'EN')
