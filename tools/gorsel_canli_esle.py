# -*- coding: utf-8 -*-
"""Tıp ve pilotaj sayfalarını canlıdaki kare kümesiyle birebir eşler.

Canlı sayfalardaki Elementor karuselinden çıkarılan sıra:

  tıp      : edward-jenner (mikroskop) · mart-production (görüntüleme) ·
             chokniti (laboratuvar) · macaristanda_tip_okumak (öğrenci grubu)
  pilotaj  : IMG_4757 · IMG_0641 · 18f73a81 (derslik) · tanathip (apron) ·
             IMG_4908 · IMG_5913 · IMG_8095 · ahmed-muntasir (motor)

Bu iki sayfadaki eski yerleşimler tamamen silinir, yerine yalnızca bu
kareler konur. Üniversite bina fotoğrafları başka sayfalarda duruyor.
"""
import io, re

HEDEF = ('tools/pages_content6.py', 'tools/en_content6.py')


def bloklari_sil(s):
    """{figure(...)}, {strip(...)}, {galeri(...)} çağrılarını süpürür."""
    n = 0
    while True:
        m = re.search(r'\{(figure|strip|galeri)\(', s)
        if not m:
            return s, n
        i, derinlik = m.start(), 0
        while i < len(s):
            if s[i] == '{':
                derinlik += 1
            elif s[i] == '}':
                derinlik -= 1
                if derinlik == 0:
                    break
            i += 1
        bas, son = m.start(), i + 1
        # blok kendi satırındaysa, arkasındaki boş satırı da al
        while son < len(s) and s[son] == '\n':
            son += 1
        while bas > 0 and s[bas - 1] == '\n' and s[bas - 2:bas - 1] == '\n':
            bas -= 1
        s = s[:bas] + s[son:]
        n += 1


TR = [
 # --- pilotaj ---
 ('<h2 id="neden">Neden Macaristan?</h2>',
  """{figure('pilotaj-hangar-egitim-ucagi',
        'Uçuş üniforması ve reflektif yelek giymiş öğrenci, hangarda çift motorlu eğitim uçağının önünde',
        'Macaristan’da pilotaj eğitimi alan öğrencimiz, eğitim uçağının önünde.',
        oncelik=True)}

<h2 id="neden">Neden Macaristan?</h2>"""),
 ('<h2 id="nerede">Hangi üniversitelerde okutulur?</h2>',
  """{strip('Pilotaj eğitiminden kareler', [
 ('pilotaj-ogrenci-pervane',
  'Pilot üniformalı öğrenci, tek motorlu eğitim uçağının pervanesinin yanında',
  'Tek motorlu eğitim uçağıyla ilk saatler.'),
 ('pilotaj-ogrenciler-hangara-giderken',
  'Reflektif yelekli öğrenci grubu, çimenlikten uçak hangarına doğru yürürken',
  'Uçuş günü: öğrenciler hangara giderken.'),
 ('pilotaj-derslik-uniformali',
  'Pilot üniformalı öğrenci grubu, derslikte sıraların başında',
  'Teorik ders saati.'),
 ('pilotaj-apron-gun-batimi',
  'Gün batımında havalimanı apronu, körüğe yanaşmış yolcu uçağı',
  'Ticari havacılık: lisans sonrası hedef.'),
 ('pilotaj-ogrenciler-pist',
  'Pilot gömlekli üç öğrenci, uçuş alanında birlikte',
  'Uçuş alanında öğrencilerimiz.'),
])}

<h2 id="nerede">Hangi üniversitelerde okutulur?</h2>"""),
 ('<h2 id="ucret">Ücretler ve neyi kapsar</h2>',
  """<h2 id="ucret">Ücretler ve neyi kapsar</h2>
{figure('pilotaj-ucak-motoru',
        'Apronda bir yolcu uçağının motoru ve kanadı, bulutlu gökyüzü',
        'Uçuş saati, ücretin en belirleyici kalemi.')}"""),
 ('<h2 id="sartlar">Başvurmadan önce hazırlamanız gerekenler</h2>',
  """<h2 id="sartlar">Başvurmadan önce hazırlamanız gerekenler</h2>
{figure('budapeste-koprude-ogrenciler',
        'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci',
        'Özgürlük Köprüsü’nde öğrencilerimiz.')}"""),
 # --- tıp ---
 ('<h2 id="sinav">Giriş sınavı ve hazırlık</h2>',
  """<h2 id="sinav">Giriş sınavı ve hazırlık</h2>
{figure('tip-ogrenci-calisma-grubu',
        'Derslikte masa başında birlikte çalışan öğrenci grubu',
        'Hazırlık ortalama 6–10 hafta sürüyor.')}"""),
 ('<h2 id="yapi">Altı yıl nasıl ilerler?</h2>',
  """<h2 id="yapi">Altı yıl nasıl ilerler?</h2>
{strip('Tıp eğitiminden kareler', [
 ('tip-mikroskop-laboratuvar',
  'Laboratuvarda önlüklü bir araştırmacı mikroskop başında; tezgâhta kan tüpleri',
  'İlk iki yıl: temel bilimler ve laboratuvar.'),
 ('tip-goruntuleme-ekranlari',
  'Radyoloji odasında ekranlarda beyin görüntüleme kesitleri',
  'Klinik yıllar: tanı ve görüntüleme.'),
 ('tip-laboratuvar-tup',
  'Bone ve gözlük takmış laboratuvar çalışanı, mavi deney tüplerine pipetle sıvı aktarıyor',
  'Laboratuvar uygulamaları eğitim boyunca sürüyor.'),
])}"""),
]

EN = [
 ('<h2 id="why">Why train in Hungary?</h2>',
  """{figure('pilotaj-hangar-egitim-ucagi',
        'A student in flight uniform and high-visibility vest in front of a twin-engine training aircraft in a hangar',
        'One of our students on the pilot training programme, in front of a training aircraft.',
        oncelik=True)}

<h2 id="why">Why train in Hungary?</h2>"""),
 ('<h2 id="where">Where it is taught</h2>',
  """{strip('Scenes from pilot training', [
 ('pilotaj-ogrenci-pervane',
  'A student in pilot uniform beside the propeller of a single-engine training aircraft',
  'First hours on a single-engine trainer.'),
 ('pilotaj-ogrenciler-hangara-giderken',
  'A group of students in high-visibility vests walking across grass towards an aircraft hangar',
  'Flying day: students heading to the hangar.'),
 ('pilotaj-derslik-uniformali',
  'A group of students in pilot uniform at their desks in a classroom',
  'A theory class.'),
 ('pilotaj-apron-gun-batimi',
  'An airport apron at sunset with an airliner at the jet bridge',
  'Commercial aviation: the goal after licensing.'),
 ('pilotaj-ogrenciler-pist',
  'Three students in pilot shirts together at the airfield',
  'Our students at the airfield.'),
])}

<h2 id="where">Where it is taught</h2>"""),
 ('<h2 id="cost">How the cost is built</h2>',
  """<h2 id="cost">How the cost is built</h2>
{figure('pilotaj-ucak-motoru',
        'The engine and wing of an airliner on the apron under a cloudy sky',
        'Flight hours drive the cost more than anything else.')}"""),
 ('<h2 id="requirements">What to arrange before you apply</h2>',
  """<h2 id="requirements">What to arrange before you apply</h2>
{figure('budapeste-koprude-ogrenciler',
        'Two students on Liberty Bridge in Budapest',
        'Our students on Liberty Bridge.')}"""),
 ('<h2 id="exam">The entrance exam and preparation</h2>',
  """<h2 id="exam">The entrance exam and preparation</h2>
{figure('tip-ogrenci-calisma-grubu',
        'A group of students working together at a table in a classroom',
        'Preparation takes 6–10 weeks on average.')}"""),
 ('<h2 id="structure">How the six years run</h2>',
  """<h2 id="structure">How the six years run</h2>
{strip('Scenes from medical training', [
 ('tip-mikroskop-laboratuvar',
  'A researcher in a lab coat at a microscope, with blood sample tubes on the bench',
  'The first two years: basic sciences and the lab.'),
 ('tip-goruntuleme-ekranlari',
  'Brain imaging slices on screens in a radiology room',
  'The clinical years: diagnosis and imaging.'),
 ('tip-laboratuvar-tup',
  'A lab worker in a hairnet and goggles pipetting into blue test tubes',
  'Laboratory work runs through the whole degree.'),
])}"""),
]


for yol, ciftler in (('tools/pages_content6.py', TR), ('tools/en_content6.py', EN)):
    s = io.open(yol, encoding='utf-8').read()
    s, silinen = bloklari_sil(s)
    n = 0
    for a, b in ciftler:
        if a not in s:
            print('  ! eşleşmedi %s :: %s' % (yol, a[:48])); continue
        s = s.replace(a, b, 1); n += 1
    io.open(yol, 'w', encoding='utf-8').write(s)
    print('%-26s %d eski blok silindi, %d yeni blok kondu' % (yol, silinen, n))
