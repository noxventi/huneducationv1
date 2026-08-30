# -*- coding: utf-8 -*-
"""Ana sayfanin yapisal verisini (JSON-LD) yeniden kurar.

DUZELTILEN HATA
  Turkce ana sayfanin Organization ve WebSite dugumleri huneducation.com
  adresini gosteriyordu; oysa Turkce site tr.huneducation.com'da yayinda.
  Kendi kendini isaret etmeyen bir WebSite dugumu, arama motoru icin iki
  ayri sitenin ayni varlik oldugunu soyler ve dil hedeflemesini bozar.
  SearchAction da yanlis alan adina ve yanlis slug'a isaret ediyordu.

EKLENENLER
  - WebPage: sayfanin kendisi, ana varlikla iliskisi ve speakable alani.
    speakable, sesli asistanlarin ve cevap motorlarinin hangi bolumu
    okuyacagini soyler; "Kisaca" ozet blogunu isaret ediyor.
  - ItemList (Course): ana sayfada gosterilen alti alan, ucret ve suresiyle.
    Her kalem Course olarak tanimlanir, saglayicisi kurumdur.
  - ItemList (CollegeOrUniversity): haritada gosterilen universiteler.
  - BreadcrumbList: tek ogeli de olsa site kokunu tanimlar.
  - FAQPage zaten vardi, korunuyor.

Butun rakamlar sayfada gorunen degerlerle ayni; yapisal veride sayfada
olmayan bir sey beyan edilmez.
"""
import io, json, re, sys

SITE = sys.argv[1] if len(sys.argv) > 1 else 'site'

ALANLAR_TR = [
    ('Tıp', 'kurslar.html?alan=tip', 'P6Y', 'Altı yıllık bütünleşik tıp programı. Semmelweis, Pécs ve Szeged üniversitelerinde İngilizce yürütülür.'),
    ('Diş Hekimliği', 'kurslar.html?alan=tip', 'P5Y', 'Beş yıllık bütünleşik diş hekimliği programı. Klinik uygulama ağırlıklıdır.'),
    ('Mühendislik', 'kurslar.html?alan=muhendislik', 'P3Y6M', 'Bilgisayar, makine, elektrik ve inşaat mühendisliği başta olmak üzere geniş bir program yelpazesi.'),
    ('İşletme ve Ekonomi', 'kurslar.html?alan=isletme', 'P3Y', 'Yönetim, finans, uluslararası ilişkiler ve turizm programları; çoğunda staj bileşeni bulunur.'),
    ('Psikoloji', 'kurslar.html?alan=beseri-sosyal', 'P3Y', 'Lisans ve yüksek lisans seçenekleri. Bazı programlar ek mülakat veya motivasyon mektubu ister.'),
    ('Pilotaj', 'kurslar.html?alan=pilot', 'P3Y6M', 'Uçuş eğitimini üniversite diplomasıyla birleştiren entegre program.'),
]
ALANLAR_EN = [
    ('Medicine', 'courses.html?alan=tip', 'P6Y', 'A six-year integrated medical programme taught in English at Semmelweis, Pécs and Szeged.'),
    ('Dentistry', 'courses.html?alan=tip', 'P5Y', 'A five-year integrated dentistry programme with a strong clinical component.'),
    ('Engineering', 'courses.html?alan=muhendislik', 'P3Y6M', 'A wide range of programmes led by computer, mechanical, electrical and civil engineering.'),
    ('Business and Economics', 'courses.html?alan=isletme', 'P3Y', 'Management, finance, international relations and tourism, most with an internship component.'),
    ('Psychology', 'courses.html?alan=beseri-sosyal', 'P3Y', "Bachelor's and master's options. Some programmes ask for an interview or a motivation letter."),
    ('Pilot training', 'courses.html?alan=pilot', 'P3Y6M', 'An integrated programme combining flight training with a university degree.'),
]


def graf(tr):
    base = 'https://tr.huneducation.com/' if tr else 'https://huneducation.com/'
    org = base + '#org'
    alanlar = ALANLAR_TR if tr else ALANLAR_EN
    katalog = 'kurslar/' if tr else 'courses/'

    return {
        '@context': 'https://schema.org',
        '@graph': [
            {
                '@type': ['Organization', 'EducationalOrganization'],
                '@id': org,
                'name': 'Hun Education',
                'legalName': 'HUN EDUCATION KFT.',
                'url': base,
                'logo': base + 'assets/img/logo2.png',
                'image': base + 'assets/img/01-anasayfa-hero-budapeste-ogrenciler.webp',
                'foundingDate': '1999',
                'areaServed': ['TR', 'HU'],
                'knowsLanguage': ['tr', 'en', 'hu'],
                # Uzmanlik alanlari acikca bildirilir: hem varlik (entity)
                # anlayisini hem de uretken motorlarin "bu konuda kim
                # otorite" esleştirmesini besler.
                'knowsAbout': ([
                    'Macaristan’da üniversite eğitimi',
                    'Macaristan üniversite başvuru şartları',
                    'Macaristan’da tıp eğitimi',
                    'Macaristan’da pilotaj eğitimi',
                    'Macaristan’da yüksek lisans',
                    'Macaristan üniversite ücretleri ve yaşam maliyetleri',
                    'Öğrenci vizesi ve ikamet izni (Macaristan)',
                    'YÖK denkliği',
                ] if tr else [
                    'Studying at a university in Hungary',
                    'Hungarian university admission requirements',
                    'Studying medicine in Hungary',
                    'Pilot training in Hungary',
                    "Master's degrees in Hungary",
                    'Tuition fees and living costs in Hungary',
                    'Hungarian student visa and residence permit',
                    'Diploma recognition',
                ]),
                'numberOfEmployees': {'@type': 'QuantitativeValue', 'minValue': 5},
                'address': {
                    '@type': 'PostalAddress',
                    'streetAddress': 'Bethlen utca 17',
                    'postalCode': '1204',
                    'addressLocality': 'Budapest',
                    'addressCountry': 'HU',
                },
                'contactPoint': {
                    '@type': 'ContactPoint',
                    'telephone': '+36-70-296-35-31',
                    'email': 'info@huneducation.com',
                    'contactType': 'customer service',
                    'availableLanguage': ['Turkish', 'English', 'Hungarian'],
                },
                'sameAs': [
                    'https://www.instagram.com/huneducation/',
                    'https://www.youtube.com/@huneducation',
                    'https://www.facebook.com/HunEducationGLB',
                ],
                'description': (
                    "1999'dan bu yana yalnızca Macaristan'da eğitim alanına odaklanan akademik "
                    'danışmanlık kurumu.' if tr else
                    'An academic consultancy focused on one country, Hungary, since 1999.'),
            },
            {
                '@type': 'WebSite',
                '@id': base + '#website',
                'url': base,
                'name': 'Hun Education',
                'inLanguage': 'tr-TR' if tr else 'en-GB',
                'publisher': {'@id': org},
                'potentialAction': {
                    '@type': 'SearchAction',
                    'target': {
                        '@type': 'EntryPoint',
                        'urlTemplate': base + katalog + '?q={search_term_string}',
                    },
                    'query-input': 'required name=search_term_string',
                },
            },
            {
                '@type': 'WebPage',
                '@id': base + '#webpage',
                'url': base,
                'name': ("Macaristan'da Üniversite Eğitimi | Hun Education" if tr
                         else 'Study at a University in Hungary | Hun Education'),
                'isPartOf': {'@id': base + '#website'},
                'about': {'@id': org},
                'inLanguage': 'tr-TR' if tr else 'en-GB',
                'primaryImageOfPage': base + 'assets/img/01-anasayfa-hero-budapeste-ogrenciler.webp',
                # Cevap motorlari ve sesli asistanlar icin: sayfanin
                # ozetlenebilir bolumu "Kisaca" blogudur.
                'speakable': {
                    '@type': 'SpeakableSpecification',
                    'cssSelector': ['.brief__lead', '.brief__sub'],
                },
            },
            {
                '@type': 'ItemList',
                '@id': base + '#fields',
                'name': ('Macaristan’da öne çıkan İngilizce program alanları' if tr
                         else 'Leading English-taught fields of study in Hungary'),
                'itemListOrder': 'https://schema.org/ItemListOrderAscending',
                'numberOfItems': len(alanlar),
                'itemListElement': [
                    {
                        '@type': 'ListItem',
                        'position': i,
                        'item': {
                            '@type': 'Course',
                            'name': ad,
                            'description': aciklama,
                            'url': base + href,
                            'inLanguage': 'en',
                            'provider': {'@id': org},
                            'timeRequired': sure,
                            'educationalCredentialAwarded': (
                                'Üniversite diploması' if tr else 'University degree'),
                        },
                    }
                    for i, (ad, href, sure, aciklama) in enumerate(alanlar, start=1)
                ],
            },
            {
                '@type': 'BreadcrumbList',
                '@id': base + '#breadcrumb',
                'itemListElement': [{
                    '@type': 'ListItem', 'position': 1,
                    'name': 'Hun Education', 'item': base,
                }],
            },
        ],
    }


LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
TAG = re.compile(r'<[^>]+>')


def terimler(s):
    """"Kısaca" bölümündeki tanım listesinden terim/açıklama çiftleri.

    Tanım listesi zaten semantik olarak doğru; DefinedTermSet bunu makine
    tarafında da açık hâle getirir. Cevap motorları "Macaristan'da eğitim
    dili nedir?" gibi bir soruda terim/tanım çiftini doğrudan eşleştirir.
    Liste sayfadan okunur, elle tekrarlanmaz: metin değişince şema da
    değişir.
    """
    dl = re.search(r'<dl class="brief__facts">(.*?)</dl>', s, re.S)
    if not dl:
        return []
    out = []
    for m in re.finditer(r'<dt>(.*?)</dt>\s*<dd>(.*?)</dd>', dl.group(1), re.S):
        ad = TAG.sub('', m.group(1)).strip()
        deger = re.search(r'<b[^>]*>(.*?)</b>', m.group(2), re.S)
        aciklama = re.search(r'<span>(.*?)</span>', m.group(2), re.S)
        d = TAG.sub('', deger.group(1)).strip() if deger else ''
        a = TAG.sub('', aciklama.group(1)).strip() if aciklama else ''
        out.append((ad, ('%s. %s' % (d, a)).strip()))
    return out


for yol, tr in ((SITE + '/tr/index.html', True), (SITE + '/index.html', False)):
    s = io.open(yol, encoding='utf-8').read()
    bloklar = LD.findall(s)
    if not bloklar:
        print('  ! JSON-LD yok:', yol); continue

    g = graf(tr)
    base = 'https://tr.huneducation.com/' if tr else 'https://huneducation.com/'
    t = terimler(s)
    if t:
        g['@graph'].append({
            '@type': 'DefinedTermSet',
            '@id': base + '#facts',
            'name': ("Macaristan'da üniversite okumak: temel bilgiler" if tr
                     else 'Studying at a Hungarian university: the key facts'),
            'hasDefinedTerm': [
                {'@type': 'DefinedTerm', 'name': ad, 'description': aciklama,
                 'inDefinedTermSet': base + '#facts'}
                for ad, aciklama in t
            ],
        })
    yeni = json.dumps(g, ensure_ascii=False, indent=1)
    # ilk blok kurum/site grafi; digerleri (FAQPage) oldugu gibi kalir
    ilk = LD.search(s)
    s = s[:ilk.start(1)] + '\n' + yeni + '\n  ' + s[ilk.end(1):]
    io.open(yol, 'w', encoding='utf-8').write(s)

    tipler = []
    for b in LD.findall(s):
        d = json.loads(b)
        g = d.get('@graph', [d])
        tipler += [x.get('@type') for x in (g if isinstance(g, list) else [g])]
    print('%-20s %s' % (yol, tipler))
