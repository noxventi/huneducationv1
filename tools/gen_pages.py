# -*- coding: utf-8 -*-
"""
Hun Education, iki dilli içerik sayfası üreticisi.

    python gen_pages.py <SITE_KOKU> <tr|en>

Neden bir üretici? Header, footer ve mobil menü altı sayfada birebir aynı ve
crawlable <a href> olarak HTML'de bulunmalı (PRD §11.7). Elle kopyalamak
kaçınılmaz olarak sürüklenmeye yol açar. İki dil devreye girince bu risk
ikiye katlanıyor: aynı düzeltmeyi 24 dosyada yapmak yerine burada bir kez
yapılır. Üretimde bunun karşılığı WordPress Theme Builder şablonudur.

DİZİN DÜZENİ
    site/            → İngilizce (varsayılan, kök)
    site/tr/         → Türkçe

Bu düzen hem `huneducation.com/tr/` hem de `tr.huneducation.com` ile
çalışır; ikisi arasındaki tek fark mutlak URL'ler, o da DOMAIN/PREFIX
sabitlerinden geliyor.

Üniversite tablosu tek kaynaktan, assets/data/catalog.js, okunur.
"""
import io, os, re, sys, json

ROOT = os.path.abspath(os.path.dirname(__file__))
SITE = sys.argv[1]
LANG = (sys.argv[2] if len(sys.argv) > 2 else 'tr').lower()
TR = LANG == 'tr'

# --------------------------------------------------------------- URL şeması
#
# CANLI YAPI KORUNUR. Bu dosyadaki slug'lar uydurulmuş değil, huneducation.com
# üzerinde hâlihazırda yayında ve sıralaması olan adreslerdir. Hiçbiri
# değiştirilmez; yeni tasarım AYNI URL'lerin üzerine gelir. Böylece taşıma bir
# "site migrasyonu" değil, sadece içerik/tasarım tazelemesi olur ve 301
# yönlendirmeye ihtiyaç kalmaz.
#
# Diller ayrı alan adlarında (WPML domain başına dil):
#   İngilizce  → huneducation.com
#   Türkçe     → tr.huneducation.com
DOMAIN = 'https://huneducation.com'
EN_BASE = 'https://huneducation.com/'
TR_BASE = 'https://tr.huneducation.com/'
BASE = TR_BASE if TR else EN_BASE

# Yereldeki klasör düzeni yalnızca dosyaları ayırmak için; canlıda iki dil de
# tek WordPress kurulumunda durur ve WPML alan adına göre yönlendirir.
OUT = os.path.join(SITE, 'tr') if TR else SITE
A = '../' if TR else ''

if not os.path.isdir(OUT):
    os.makedirs(OUT)

# --------------------------------------------------------------- veri
def load_universities():
    """Universite listesi catalog-index.json'dan gelir.

    Bu dosya build_catalog.py tarafindan, canlidaki gercek `course` ve
    `university` kayitlarindan uretilir. Onceden catalog.js regex ile
    ayristiriliyordu; veri sematik degisince sessizce kiriliyordu.
    """
    p = os.path.join(SITE, 'assets/data/catalog-index.json')
    d = json.loads(io.open(p, encoding='utf-8').read())
    i = 1 if TR else 0
    sehirler = {k: v[i] for k, v in d['sehirler'].items()}
    alanlar = {k: v[i] for k, v in d['alanlar'].items()}
    turler = {k: v[i] for k, v in d['turler'].items()}
    out = []
    for u in d['universiteler']:
        out.append(dict(
            id=u['id'],
            ad=(u['tr'] or u['en']) if TR else u['en'],
            sehir=sehirler.get(u['sehir'], '—'),
            sehir_id=u['sehir'],
            tur=turler.get(u['tur'], u['tur']),
            kurulus=u['kurulus'],
            alanlar=[alanlar.get(a, a) for a in u['alanlar']],
            programSayisi=u['programSayisi'],
        ))
    out.sort(key=lambda x: x['ad'])
    return out

UNIS = load_universities()

# --------------------------------------------------------------- dosya adları
#
# İlk 14 çift CANLIDA YAYINDA olan sayfalardır; slug'lara dokunulmaz.
# Türkçe slug'lar anahtar kelimeyi zaten taşıyor (macaristan-universite-fiyatlari
# gibi) ve sıralaması var, kısaltmak kayıp olurdu.
#
# Son 4 çift yalnızca yeni tasarımla gelen hukuki sayfalardır: canlıda karşılığı
# yok, yeni URL olarak eklenirler. Yeni URL eklemek risksizdir; mevcut URL
# değiştirmek değildir.
SLUG = {
    # anahtar        İngilizce (huneducation.com)                              Türkçe (tr.huneducation.com)
    'home':      ('index.html',                                                'index.html'),
    'why':       ('why-hungary.html',                                          'neden-macaristanda-egitim.html'),
    'edu':       ('education-in-hungary.html',                                 'macaristanda-universite-okumak.html'),
    'unis':      ('universities.html',                                         'macaristan-universiteleri.html'),
    'progs':     ('courses.html',                                              'kurslar.html'),
    'apply':     ('admission.html',                                            'macaristan-universite-basvuru-sartlari.html'),
    'costs':     ('costs.html',                                                'macaristan-universite-fiyatlari.html'),
    'masters':   ('masters-education-in-hungary.html',                         'macaristan-yuksek-lisans.html'),
    'medicine':  ('studying-medicine-in-hungary-and-pursuing-a-medical-degree-in-hungary.html',
                                                                               'macaristanda-tip-egitimi-ve-macaristanda-tip-okumak.html'),
    'pilot':     ('pilot-training-at-hungarian-universities.html',             'macaristan-universiteleri-pilotluk-egitimi.html'),
    'life':      ('university-education-and-life-in-hungary-what-you-need-to-know.html',
                                                                               'macaristanda-yasam-ve-universite-egitimi-bilinmesi-gerekenler.html'),
    'stories':   ('student-perspectives.html',                                 'macaristan-universiteleri-ogrenci-gorusleri.html'),
    'about':     ('about-us.html',                                             'hakkimizda.html'),
    'contact':   ('contact.html',                                              'iletisim.html'),
    # --- yeni (canlıda yok) ---
    'privacy':   ('privacy-notice.html',                                       'kvkk-aydinlatma.html'),
    'consent':   ('consent.html',                                              'acik-riza.html'),
    'cookies':   ('cookie-policy.html',                                        'gizlilik-cerez.html'),
    'terms':     ('terms-of-use.html',                                         'kullanim-kosullari.html'),
}
# Canlıda hâlihazırda yayında olan anahtarlar (taşımada URL'si korunacaklar)
CANLI = ('home','why','edu','unis','progs','apply','costs','masters',
         'medicine','pilot','life','stories','about','contact')
S = {k: (v[1] if TR else v[0]) for k, v in SLUG.items()}
# Dil değiştirici için karşı dildeki eş sayfa
S_OTHER = {k: (v[0] if TR else v[1]) for k, v in SLUG.items()}
SLUG_KEY = {v: k for k, v in S.items()}

# --------------------------------------------------------------- sabit metinler
if TR:
    W = dict(
        skip='İçeriğe geç', homeAria='Hun Education ana sayfa', mainMenu='Ana menü',
        langGroup='Dil seçimi', wa="WhatsApp'tan yazın", mobileMenu='Mobil menü',
        openMenu='Menüyü aç', cta='Ücretsiz Ön Görüşme', ctaLong='Ücretsiz Ön Görüşme Al',
        ctaShort='Ön Görüşme Al', waAsk="WhatsApp'tan Sor", contact='İletişim',
        ftrH='Site alt bilgisi', quick='Hızlı bağlantılar', popular='Popüler programlar',
        legal='Yasal', crumbsAria='Site yolu', toc='İçindekiler', related='İlgili sayfalar',
        breadHome='Ana sayfa',
        ftrAbout="1999'dan beri Macaristan odaklı akademik danışmanlık. Program seçiminden başvuruya, "
                 "vizeden konaklama ve şehir oryantasyonuna kadar uçtan uca destek.",
        navEdu="Macaristan'da Eğitim", navUnis='Üniversiteler', navProgs='Programlar',
        navApply='Başvuru', navCosts='Maliyetler', navAbout='Kurumsal',
        # açılır menü kalemleri
        navWhy='Neden Macaristan?', navEduGuide='Üniversite eğitimi rehberi',
        navLife="Macaristan'da yaşam", navStories='Öğrenci görüşleri',
        navCatalog='Tüm programlar', navMed='Tıp eğitimi',
        navPilot='Pilotluk eğitimi', navMaster='Yüksek lisans',
        navApplyReq='Başvuru şartları', navAboutUs='Hakkımızda',
        navContact='İletişim', navMenu='menüsü',
        popMed='Tıp', popDent='Diş Hekimliği', popEng='Mühendislik', popBus='İşletme',
        popPsy='Psikoloji', popPilot='Pilotaj',
        offHQ='Budapeşte merkez', offTR='Türkiye',
        offTRList='Ankara · İstanbul (Kadıköy) · İzmir · Bursa',
        waLink="WhatsApp'tan yazın", hours='Pazartesi – Cuma · 09:00 – 18:00',
        tel='TEL', mail='E-POSTA',
        disclaimer='Sitede yer alan öğrenim ücretleri, başvuru tarihleri ve kabul koşulları üniversiteler '
                   'tarafından değiştirilebilir. Vize ve denklik kararları ilgili resmî kurumlara aittir. '
                   'Nihai bilgi için üniversitenin resmî sayfasını ve güncel mevzuatı esas alınız.',
        rights='Tüm hakları saklıdır.',
        lPrivacy='KVKK Aydınlatma Metni', lConsent='Açık Rıza Metni',
        lCookies='Gizlilik ve Çerez Politikası', lTerms='Kullanım Koşulları',
        byAuthor='Hazırlayan', byTeam='Hun Education akademik danışmanlık ekibi',
        byUpdated='Son güncelleme', byUpdatedVal='5 Ağustos 2026',
        byNext='Sonraki kontrol', byNextVal='Ocak 2027',
        changelog='Değişiklik günlüğü',
        chg1='İçerik editoryal ve SEO denetiminden geçirildi; kaynak beyanları güncellendi.',
        chg2='Sayfa yayına alındı; ücret aralıkları, başvuru takvimi ve giriş sınavı şartları güncel veriyle yazıldı.',
        locale='tr_TR', inLang='tr-TR',
    )
else:
    W = dict(
        skip='Skip to content', homeAria='Hun Education home', mainMenu='Main menu',
        langGroup='Language', wa='Message us on WhatsApp', mobileMenu='Mobile menu',
        openMenu='Open menu', cta='Free Consultation', ctaLong='Book a Free Consultation',
        ctaShort='Book a Consultation', waAsk='Ask on WhatsApp', contact='Contact',
        ftrH='Site footer', quick='Quick links', popular='Popular programmes',
        legal='Legal', crumbsAria='Breadcrumb', toc='On this page', related='Related pages',
        breadHome='Home',
        ftrAbout='Hungary-focused academic consultancy since 1999. End-to-end support from choosing a '
                 'programme to applying, and from the student visa to accommodation and settling into '
                 'your city.',
        navEdu='Study in Hungary', navUnis='Universities', navProgs='Programmes',
        navApply='Admissions', navCosts='Costs', navAbout='Company',
        # dropdown items
        navWhy='Why Hungary?', navEduGuide='Guide to studying here',
        navLife='Life in Hungary', navStories='Student stories',
        navCatalog='All programmes', navMed='Medicine',
        navPilot='Pilot training', navMaster="Master's degrees",
        navApplyReq='Admission requirements', navAboutUs='About us',
        navContact='Contact', navMenu='menu',
        popMed='Medicine', popDent='Dentistry', popEng='Engineering', popBus='Business',
        popPsy='Psychology', popPilot='Pilot Training',
        offHQ='Budapest head office', offTR='Türkiye',
        offTRList='Ankara · Istanbul (Kadıköy) · Izmir · Bursa',
        waLink='Message us on WhatsApp', hours='Monday – Friday · 09:00 – 18:00 CET',
        tel='TEL', mail='EMAIL',
        disclaimer='Tuition fees, application dates and admission requirements shown on this site may be '
                   'changed by the universities. Visa and recognition decisions rest with the relevant '
                   'official authorities. Always treat the university’s own page and current legislation '
                   'as definitive.',
        rights='All rights reserved.',
        lPrivacy='Privacy Notice', lConsent='Consent Statement',
        lCookies='Cookie Policy', lTerms='Terms of Use',
        byAuthor='Written by', byTeam='the Hun Education academic advisory team',
        byUpdated='Last updated', byUpdatedVal='5 August 2026',
        byNext='Next review', byNextVal='January 2027',
        changelog='Change log',
        chg1='Content passed editorial and SEO review; source statements updated.',
        chg2='Page published; fee ranges, application calendar and entrance exam requirements written from current data.',
        locale='en_GB', inLang='en-GB',
    )

# Menü ağacı: (üst başlık, alt kalemler). Alt kalemi olmayan başlık
# doğrudan bağlantıdır. Yasal sayfalar dışındaki 14 sayfanın tamamı
# buradan erişilebilir olmalı; audit_i18n.py bunu denetler.
NAV = [
    (W['navEdu'], None, [
        (S['why'], W['navWhy']),
        (S['edu'], W['navEduGuide']),
        (S['life'], W['navLife']),
        (S['stories'], W['navStories']),
    ]),
    (W['navUnis'], S['unis'], []),
    (W['navProgs'], None, [
        (S['progs'], W['navCatalog']),
        (S['medicine'], W['navMed']),
        (S['pilot'], W['navPilot']),
        (S['masters'], W['navMaster']),
    ]),
    (W['navApply'], None, [
        (S['apply'], W['navApplyReq']),
        (S['costs'], W['navCosts']),
    ]),
    (W['navAbout'], None, [
        (S['about'], W['navAboutUs']),
        (S['contact'], W['navContact']),
    ]),
]

CARET = ('<svg class="hdr__caret" width="10" height="10" viewBox="0 0 24 24" fill="none" '
         'stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" '
         'aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>')

WA_SVG = ('<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
 '<path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.9 9.9 0 0 0 4.79 1.22h.01'
 'c5.46 0 9.9-4.45 9.9-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2Zm0 18.15h-.01a8.2 8.2 0 0 1-4.19-1.15'
 'l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.23 8.25-8.23 2.2 0 4.27.86 5.83 2.42a8.18 8.18 0 0 1 2.41 5.82'
 'c0 4.54-3.7 8.23-8.24 8.23Z"/></svg>')

ARROW = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')


def lang_switch(slug):
    """Dil değiştirici: karşı dilin EŞ SAYFASINA gider, ana sayfaya değil.

    Kullanıcı 'Maliyetler' sayfasındayken EN'e basınca 'Costs' sayfasında
    kalmalı; ana sayfaya atmak okuduğu yeri kaybettiriyor. Eşi olmayan bir
    sayfa yok, hepsi çift üretiliyor.
    """
    key = SLUG_KEY.get(slug, 'home')
    other = S_OTHER[key]
    tr_href = ('%s' % other) if not TR else slug
    en_href = ('%s' % other) if TR else slug
    # Türkçe bir alt dizinde: karşı dile giderken bir seviye yukarı/aşağı
    tr_href = tr_href if TR else 'tr/' + tr_href
    en_href = '../' + en_href if TR else en_href
    cur = ' aria-current="true"'
    return (f'<div class="lang" role="group" aria-label="{W["langGroup"]}">'
            f'<a href="{en_href}" hreflang="en" lang="en"{"" if TR else cur}><span>EN</span></a>'
            f'<a href="{tr_href}" hreflang="tr" lang="tr"{cur if TR else ""}><span>TR</span></a>'
            f'</div>')


def nav_masaustu(active):
    """Masaüstü menüsü. Alt kalemi olan başlık <button>, olmayan <a>.

    Başlığın kendisi bir sayfaya gitmez; yalnızca menüyü açar. Böylece
    "tıklarsam gider mi, açılır mı?" belirsizliği kalmaz. Aktif sayfa
    alt listede işaretlenir, üst başlık da is-active alır."""
    parcalar = []
    for i, (baslik, href, alt) in enumerate(NAV):
        if not alt:
            cur = ' aria-current="page"' if href == active else ''
            parcalar.append('<div class="hdr__item">'
                            '<a class="hdr__link" href="%s"%s>%s</a></div>' % (href, cur, baslik))
            continue
        acik = any(h == active for h, _ in alt)
        ogeler = '\n        '.join(
            '<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == active else '', t)
            for h, t in alt)
        parcalar.append(
            '<div class="hdr__item" data-drop>\n'
            '      <button class="hdr__link hdr__link--drop%s" aria-expanded="false" '
            'aria-controls="dd%d" aria-label="%s %s">%s%s</button>\n'
            '      <div class="hdr__menu" id="dd%d" hidden>\n        %s\n      </div>\n'
            '    </div>' % (' is-active' if acik else '', i, baslik, W['navMenu'],
                            baslik, CARET, i, ogeler))
    return '\n    '.join(parcalar)


def nav_mobil():
    """Mobil menü: aynı ağaç, akordiyon olarak."""
    parcalar = []
    for i, (baslik, href, alt) in enumerate(NAV):
        if not alt:
            parcalar.append('<li><a href="%s" style="--i:%d">%s</a></li>' % (href, i, baslik))
            continue
        ogeler = ''.join('<a href="%s">%s</a>' % (h, t) for h, t in alt)
        parcalar.append(
            '<li style="--i:%d"><button class="mnav__toggle" aria-expanded="false" '
            'aria-controls="m%d">%s%s</button>\n'
            '        <div class="mnav__sub" id="m%d" hidden>%s</div>\n      </li>'
            % (i, i, baslik, CARET, i, ogeler))
    return '\n      '.join(parcalar)


def header(active, slug):
    links = nav_masaustu(active)
    mlinks = nav_mobil()
    return f'''<header class="hdr is-solid" id="hdr">
  <div class="hdr__bar">
    <a class="hdr__logo" href="{S['home']}" aria-label="{W['homeAria']}">
      <img src="{A}assets/img/logo2.png" alt="Hun Education" width="250" height="70">
    </a>
    <nav class="hdr__nav" aria-label="{W['mainMenu']}">
      <span class="hdr__glide" aria-hidden="true"></span>
      {links}
    </nav>
    <div class="hdr__side">
      {lang_switch(slug)}
      <a class="icon-btn" href="https://wa.me/" data-wa aria-label="{W['wa']}">{WA_SVG}</a>
      <a class="btn btn--primary btn--sm" href="{S['contact']}" data-magnetic>
        <span class="btn__label"><span data-t="{W['cta']}">{W['cta']}</span></span>
      </a>
      <button class="hdr__burger" id="burger" aria-label="{W['openMenu']}" aria-expanded="false" aria-controls="mnav"><i></i><i></i><i></i></button>
    </div>
    <div class="hdr__progress"></div>
  </div>
</header>

<div class="mnav" id="mnav" hidden>
  <nav aria-label="{W['mobileMenu']}">
    <ul class="mnav__list">
      {mlinks}
    </ul>
  </nav>
  <div class="mnav__foot">
    <a class="btn btn--primary" href="{S['contact']}"><span class="btn__label"><span data-t="{W['ctaLong']}">{W['ctaLong']}</span></span></a>
    <a class="btn btn--wa" href="https://wa.me/" data-wa><span class="btn__label"><span data-t="{W['waAsk']}">{W['waAsk']}</span></span></a>
  </div>
</div>'''

FOOTER = f'''<footer class="ftr" aria-labelledby="ftr-h">
  <h2 id="ftr-h" class="sr-only">{W['ftrH']}</h2>
  <div class="shell">
    <div class="ftr__top">
      <div class="ftr__brand">
        <a class="hdr__logo" href="{S['home']}" aria-label="{W['homeAria']}">
          <img src="{A}assets/img/logo2.png" alt="Hun Education" width="250" height="70">
        </a>
        <p>{W['ftrAbout']}</p>
        <div class="ftr__social">
          <a href="https://www.instagram.com/huneducation/" rel="noopener" target="_blank" aria-label="Instagram">IG</a>
          <a href="https://www.youtube.com/@huneducation" rel="noopener" target="_blank" aria-label="YouTube">YT</a>
          <a href="https://www.facebook.com/HunEducationGLB" rel="noopener" target="_blank" aria-label="Facebook">FB</a>
        </div>
      </div>
      <nav class="ftr__col" aria-label="{W['quick']}">
        <h3>{W['quick']}</h3>
        <a href="{S['edu']}">{W['navEdu']}</a><a href="{S['unis']}">{W['navUnis']}</a>
        <a href="{S['progs']}">{W['navProgs']}</a><a href="{S['apply']}">{W['navApply']}</a>
        <a href="{S['costs']}">{W['navCosts']}</a><a href="{S['about']}">{W['navAbout']}</a>
      </nav>
      <nav class="ftr__col" aria-label="{W['popular']}">
        <h3>{W['popular']}</h3>
        <a href="{S['progs']}?alan=tip">{W['popMed']}</a><a href="{S['progs']}?alan=tip">{W['popDent']}</a>
        <a href="{S['progs']}?alan=muhendislik">{W['popEng']}</a><a href="{S['progs']}?alan=isletme">{W['popBus']}</a>
        <a href="{S['progs']}?alan=beseri-sosyal">{W['popPsy']}</a><a href="{S['progs']}?alan=pilot">{W['popPilot']}</a>
      </nav>
      <div class="ftr__col ftr__col--contact">
        <h3>{W['contact']}</h3>
        <p class="ftr__office"><b>{W['offHQ']}</b><span>1204 Budapest, Bethlen utca 17, {'Macaristan' if TR else 'Hungary'}</span></p>
        <p class="ftr__office"><b>{W['offTR']}</b><span>{W['offTRList']}</span></p>
        <a href="tel:+36702963531" class="ftr__contact"><span class="num-mono">{W['tel']}</span> +36 70 296 35 31</a>
        <a href="mailto:info@huneducation.com" class="ftr__contact"><span class="num-mono">{W['mail']}</span> info@huneducation.com</a>
        <a href="https://wa.me/" data-wa class="ftr__contact"><span class="num-mono">WA</span> {W['waLink']}</a>
        <p class="ftr__hours num-mono">{W['hours']}</p>
      </div>
    </div>
    <div class="ftr__legal">
      <p class="ftr__disclaimer">
        {W['disclaimer']}
      </p>
      <nav class="ftr__links" aria-label="{W['legal']}">
        <a href="{S['privacy']}">{W['lPrivacy']}</a><a href="{S['consent']}">{W['lConsent']}</a>
        <a href="{S['cookies']}">{W['lCookies']}</a><a href="{S['terms']}">{W['lTerms']}</a>
      </nav>
      <p class="ftr__copy num-mono">© <span data-year>2026</span> HUN EDUCATION KFT. · {W['rights']}</p>
    </div>
  </div>
  <div class="ftr__mega" aria-hidden="true"><span>HUN EDUCATION</span></div>
</footer>

<div class="mobile-bar is-up" id="mobileBar">
  <a class="btn btn--primary btn--sm" href="{S['contact']}"><span class="btn__label"><span data-t="{W['ctaShort']}">{W['ctaShort']}</span></span></a>
  <a class="btn btn--wa btn--sm" href="https://wa.me/" data-wa><span class="btn__label"><span data-t="WhatsApp">WhatsApp</span></span></a>
</div>'''

BYLINE = f'''<div class="byline">
  <span class="byline__item"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/></svg>
    <span>{W['byAuthor']} <b>{W['byTeam']}</b></span></span>
  <span class="byline__item"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
    <span>{W['byUpdated']} <b><time datetime="2026-08-05">{W['byUpdatedVal']}</time></b></span></span>
  <span class="byline__item"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M20 6 9 17l-5-5"/></svg>
    <span>{W['byNext']} <b>{W['byNextVal']}</b></span></span>
</div>'''

CHANGELOG = f'''<details class="changelog">
  <summary>{W['changelog']}</summary>
  <ul>
    <li><time datetime="2026-08-05">{'05.08.2026' if TR else '5 Aug 2026'}</time>: {W['chg1']}</li>
    <li><time datetime="2026-08-03">{'03.08.2026' if TR else '3 Aug 2026'}</time>: {W['chg2']}</li>
  </ul>
</details>'''


def acta(title, text):
    return f'''<aside class="acta">
  <div>
    <h2>{title}</h2>
    <p>{text}</p>
  </div>
  <div class="acta__actions">
    <a class="btn btn--primary" href="{S['contact']}" data-magnetic><span class="btn__label"><span data-t="{W['ctaLong']}">{W['ctaLong']}</span></span></a>
    <a class="btn btn--ghost" href="https://wa.me/" data-wa><span class="btn__label"><span data-t="{W['waAsk']}">{W['waAsk']}</span></span></a>
  </div>
</aside>'''


def stats(items):
    """Sayfa basindaki kanit bandi. items: [(rakam, aciklama), ...]

    Okuyucu uzun metne girmeden once karari destekleyen rakamlari goruyor.
    Buradaki her sayinin sayfa govdesinde ya da Kaynaklar bolumunde
    karsiligi olmali; sustelemek icin rakam eklenmez.
    """
    tek = '\n'.join('  <div><b>%s</b><span>%s</span></div>' % (a, b) for a, b in items)
    return '<div class="stats">\n%s\n</div>' % tek


import gorsel_ogeler
gorsel_ogeler.A = A
from gorsel_ogeler import olcu, kaynak_kumesi, figure, strip, galeri


def inline_cta(text, label=None):
    """Metin ici donusum noktasi. Uzun rehber sayfalarinda okuyucu sonundaki
    CTA'ya varmadan cikabiliyor; bolum aralarina tek satirlik cagri konur."""
    return ('<p class="inline-cta">%s <a class="btn btn--primary btn--sm" href="%s" data-magnetic>'
            '<span class="btn__label"><span data-t="%s">%s</span></span></a></p>'
            % (text, S['contact'], label or W['ctaShort'], label or W['ctaShort']))


def related(items):
    cards = '\n  '.join(
        f'<a class="rcard" href="{h}"><span>{k}</span><b>{t}</b><p>{d}</p></a>' for h, k, t, d in items)
    return f'<nav class="related" aria-label="{W["related"]}">\n  {cards}\n</nav>'


def toc(items):
    links = '\n    '.join(f'<a href="#{i}">{t}</a>' for i, t in items)
    # Mobilde katlanabilir; JS yoksa açık kalır (progressive enhancement)
    return ('<nav class="toc" aria-labelledby="toc-h">\n'
            '  <h2 id="toc-h"><button class="toc__toggle" type="button" aria-expanded="true">'
            f'{W["toc"]}<span class="toc__caret" aria-hidden="true"></span></button></h2>\n'
            f'  <div class="toc__list">\n    {links}\n  </div>\n</nav>')


def faq_block(qa):
    items = ''
    for i, (q, a) in enumerate(qa, 1):
        items += f'''
  <div class="acc__item">
    <h3><button class="acc__btn" aria-expanded="false"><span class="acc__num">{i:02d}</span> {q}<span class="acc__ico"></span></button></h3>
    <div class="acc__panel"><div class="acc__inner"><div>{a}</div></div></div>
  </div>'''
    return f'<div class="acc" data-acc>{items}\n</div>'


def faq_ld(qa):
    return json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "inLanguage": W['inLang'],
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a).strip()}}
                       for q, a in qa]
    }, ensure_ascii=False, indent=2)


def aciklama_kirp(d, sinir=155):
    """meta description SERP'te ~155 karakterden sonra kesilir.

    Kelime ortasindan kesmek yerine son TAM cumlede durulur: yarim
    kalan bir cumle hem SERP'te hem uretken motorlarda kotu alintilanir.
    """
    if len(d) <= sinir:
        return d
    kes = d[:sinir]
    for isaret in ('. ', '; ', ' \u2014 ', ', '):
        i = kes.rfind(isaret)
        if i > sinir * 0.55:
            return kes[:i].rstrip(' ,;\u2014') + '.'
    return kes[:kes.rfind(' ')].rstrip(' ,;\u2014') + '.'


MARKA = ' | Hun Education'


def baslik_kirp(t):
    """<title> 60 karakteri asmasin.

    Google SERP'te yaklasik 60 karakterden sonrasini keser. Marka eki
    16 karakter yiyor ve zaten her sonucta alan adi gorunuyor; baslik
    uzunsa marka DUSER, anahtar kelime kalir. Marka kisa basliklarda
    durur, cunku orada tanınırlık katiyor.
    """
    if len(t) <= 60:
        return t
    if t.endswith(MARKA):
        yalin = t[:-len(MARKA)]
        if len(yalin) <= 60:
            return yalin
        return yalin
    return t


def article_ld(url, title, desc, gorsel=None, konusulabilir=False):
    """Sayfanin Article dugumu.

    headline: Google 110 karakterden sonrasini yok sayar; marka eki
    ve baslikta kalan fazlalik burada kirpilir, <title> ayri kalir.

    image: sayfanin kendi one cikan gorseli. Onsuz Article dugumu bazi
    sonuc turlerinde kucuk resim hakki kazanmaz.

    speakable: cevap blogu olan sayfalarda hangi parcanin CEVAP oldugunu
    acikca isaretler. Sesli asistan ve uretken motorlar once burayi okur.
    """
    d = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": title.split(' | ')[0][:110], "name": title,
        "description": desc,
        "inLanguage": W['inLang'],
        "datePublished": "2026-08-03", "dateModified": GUNCELLEME,
        "author": {"@type": "Organization", "name": "Hun Education",
                   "@id": DOMAIN + "/#org"},
        "publisher": {"@type": "Organization", "name": "Hun Education",
                      "@id": DOMAIN + "/#org",
                      "logo": {"@type": "ImageObject", "url": DOMAIN + "/assets/img/logo2.png"}},
        "isPartOf": {"@type": "WebSite", "@id": BASE + "#website"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url}
    }
    if gorsel:
        d["image"] = {"@type": "ImageObject", "url": gorsel, "width": 1536, "height": 1024}
    if konusulabilir:
        d["speakable"] = {"@type": "SpeakableSpecification",
                          "cssSelector": [".answer", ".lede"]}
    return json.dumps(d, ensure_ascii=False, indent=2)


def howto_ld(url, ad, aciklama, adimlar):
    """Adim adim surec icin HowTo dugumu.

    Basvuru sayfasindaki alti adim zaten yazili; makine okunur hali
    "Macaristan'da universiteye nasil basvurulur" tipi sorularda hem
    zengin sonuc hem de uretken motorlarda dogrudan alinti sansi verir.
    """
    return json.dumps({
        "@context": "https://schema.org", "@type": "HowTo",
        "name": ad, "description": aciklama,
        "inLanguage": W['inLang'],
        "totalTime": "P120D",
        "step": [{"@type": "HowToStep", "position": i + 1, "name": b,
                  "text": m, "url": url + "#takvim" if TR else url + "#calendar"}
                 for i, (b, m) in enumerate(adimlar)],
    }, ensure_ascii=False, indent=2)


def crumb_ld(items):
    return json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                            for i, (n, u) in enumerate(items)]
    }, ensure_ascii=False, indent=2)


# Icerik tazeligi tek yerden. Sayfa gövdesi degistiginde burasi da
# guncellenir; JSON-LD ve sitemap ayni tarihi kullanir.
GUNCELLEME = '2026-08-10'

IMG = DOMAIN + '/assets/img/'
OG_IMG = {
 'apply':    IMG + '16-universite-basvuru-belgeleri.webp',
 'costs':    IMG + '12-budapeste-ogrenci-konaklama.webp',
 'edu':      IMG + '04-macaristan-universite-kampusu.webp',
 'why':      IMG + '11-universite-kutuphanesi-ogrenciler.webp',
 'unis':     IMG + '15-debrecen-universite-kampusu.webp',
 'masters':  IMG + '07-isletme-ekonomi-egitimi.webp',
 'medicine': IMG + '05-macaristanda-tip-egitimi.webp',
 'pilot':    IMG + '09-macaristanda-pilotaj-egitimi.webp',
 'life':     IMG + '18-budapeste-sehir-oryantasyonu.webp',
 'stories':  IMG + '14-pecs-ogrenci-hayati.webp',
 'about':    IMG + '02-ucretsiz-on-gorusme-danismanlik.webp',
 'contact':  IMG + '20-mezuniyet-ve-gelecek.webp',
}

def url_of(key):
    """Bir sayfanin AKTIF DILDEKI canli URL'si. Kirinti izleri ve JSON-LD
    buradan beslenir; hicbir yerde mutlak URL elle yazilmaz."""
    slug = S[key]
    return BASE if slug == 'index.html' else BASE + slug.replace('.html', '/')


HOME = (W['breadHome'], BASE)


def page(slug, title, desc, hero_eyebrow, h1, sub, body, active, crumbs, qa=None, extra_css='', howto=None):
    desc = aciklama_kirp(desc)
    key = SLUG_KEY.get(slug, 'home')
    url = BASE + slug.replace('.html', '/')
    alt_en = EN_BASE + (S_OTHER[key] if TR else slug).replace('.html', '/')
    alt_tr = TR_BASE + (slug if TR else S_OTHER[key]).replace('.html', '/')
    if key == 'home':
        alt_en, alt_tr = EN_BASE, TR_BASE

    og = OG_IMG.get(key, IMG + '01-anasayfa-hero-budapeste-ogrenciler.webp')
    ld = [article_ld(url, title, desc, og, konusulabilir='class="answer"' in body),
          crumb_ld(crumbs)]
    if qa:
        ld.append(faq_ld(qa))
    if howto:
        ld.append(howto_ld(url, *howto))
    ld_html = '\n'.join('<script type="application/ld+json">\n%s\n</script>' % j for j in ld)
    crumb_html = ' <span aria-hidden="true">/</span> '.join(
        (f'<a href="{u.replace(BASE, "") or S["home"]}">{n}</a>' if i < len(crumbs) - 1
         else f'<span aria-current="page">{n}</span>')
        for i, (n, u) in enumerate(crumbs))
    return f'''<!DOCTYPE html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{baslik_kirp(title)}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#080c26">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="tr" href="{alt_tr}">
<link rel="alternate" hreflang="x-default" href="{alt_en}">
<meta property="og:type" content="article">
<meta property="og:locale" content="{W['locale']}">
<meta property="og:locale:alternate" content="{'en_GB' if TR else 'tr_TR'}">
<meta property="og:site_name" content="Hun Education">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{og}">
<link rel="icon" href="{A}assets/img/logo2.png">
<link rel="preload" href="{A}assets/fonts/jakarta-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{A}assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{A}assets/css/tokens.css">
<link rel="stylesheet" href="{A}assets/css/base.css">
<link rel="stylesheet" href="{A}assets/css/components.css">
<link rel="stylesheet" href="{A}assets/css/sections.css">
<link rel="stylesheet" href="{A}assets/css/article.css">{extra_css}
{ld_html}
</head>
<body class="page-article">
<a class="skip-link" href="#icerik">{W['skip']}</a>
<div class="cursor" id="cursor" aria-hidden="true"><span class="cursor__ring"></span><span class="cursor__dot"></span><span class="cursor__label"></span></div>

{header(active, slug)}

<main id="icerik">
<section class="ahero">
  <div class="shell">
    <nav class="crumbs" aria-label="{W['crumbsAria']}">{crumb_html}</nav>
    <div class="ahero__inner">
      <p class="eyebrow">{hero_eyebrow}</p>
      <h1>{h1}</h1>
      <p class="ahero__sub">{sub}</p>
      {BYLINE}
    </div>
  </div>
</section>

<div class="shell">
{body}
</div>
</main>

{FOOTER}
<script type="module" src="{A}assets/js/page.js"></script>
</body>
</html>
'''


LEGAL_BYLINE = f'''<div class="byline">
  <span class="byline__item"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
    <span>{'Yürürlük tarihi' if TR else 'Effective from'} <b><time datetime="2026-08-05">{W['byUpdatedVal']}</time></b></span></span>
  <span class="byline__item"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M20 6 9 17l-5-5"/></svg>
    <span>{'Versiyon' if TR else 'Version'} <b>1.0</b></span></span>
  <span class="byline__item"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/></svg>
    <span>{'Veri sorumlusu' if TR else 'Data controller'} <b>HUN EDUCATION KFT.</b></span></span>
</div>'''


def legal_page(slug, title, desc, h1, sub, body, crumb_name):
    desc = aciklama_kirp(desc)
    """Yasal sayfa iskeleti, makale sayfalarından ayrı, çünkü içindekiler
    ve changelog yerine yürürlük tarihi/versiyon künyesi taşıyor."""
    key = SLUG_KEY.get(slug, 'home')
    url = BASE + slug.replace('.html', '/')
    alt_en = EN_BASE + (S_OTHER[key] if TR else slug).replace('.html', '/')
    alt_tr = TR_BASE + (slug if TR else S_OTHER[key]).replace('.html', '/')
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "WebPage",
        "name": h1, "description": desc, "inLanguage": W['inLang'],
        "datePublished": "2026-08-05", "dateModified": "2026-08-05",
        "publisher": {"@id": DOMAIN + "/#org"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url}
    }, ensure_ascii=False, indent=1)
    crumb_ld_s = json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": W['breadHome'], "item": BASE},
            {"@type": "ListItem", "position": 2, "name": crumb_name, "item": url}]
    }, ensure_ascii=False, indent=1)
    return f'''<!DOCTYPE html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{baslik_kirp(title)}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#080c26">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="tr" href="{alt_tr}">
<link rel="alternate" hreflang="x-default" href="{alt_en}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{W['locale']}">
<meta property="og:locale:alternate" content="{'en_GB' if TR else 'tr_TR'}">
<meta property="og:site_name" content="Hun Education">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/img/logo2.png">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{A}assets/img/logo2.png">
<link rel="preload" href="{A}assets/fonts/jakarta-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{A}assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{A}assets/css/tokens.css">
<link rel="stylesheet" href="{A}assets/css/base.css">
<link rel="stylesheet" href="{A}assets/css/components.css">
<link rel="stylesheet" href="{A}assets/css/sections.css">
<link rel="stylesheet" href="{A}assets/css/article.css">
<script type="application/ld+json">
{ld}
</script>
<script type="application/ld+json">
{crumb_ld_s}
</script>
</head>
<body class="page-article">
<a class="skip-link" href="#icerik">{W['skip']}</a>
<div class="cursor" id="cursor" aria-hidden="true"><span class="cursor__ring"></span><span class="cursor__dot"></span><span class="cursor__label"></span></div>

{header(None, slug)}

<main id="icerik">
<section class="ahero">
  <div class="shell">
    <nav class="crumbs" aria-label="{W['crumbsAria']}"><a href="{S['home']}">{W['breadHome']}</a> <span aria-hidden="true">/</span> <span aria-current="page">{crumb_name}</span></nav>
    <div class="ahero__inner">
      <p class="eyebrow">{W['legal']}</p>
      <h1>{h1}</h1>
      <p class="ahero__sub">{sub}</p>
      {LEGAL_BYLINE}
    </div>
  </div>
</section>

<div class="shell">
{body}
</div>
</main>

{FOOTER}
<script type="module" src="{A}assets/js/page.js"></script>
</body>
</html>
'''


def write(slug, html):
    io.open(os.path.join(OUT, slug), 'w', encoding='utf-8').write(html)
    print('  yazildi: %s/%s  %d byte' % (LANG, slug, len(html)))


PARTS = (tuple('pages_content%s.py' % (i or '') for i in ('', 2, 3, 4, 5, 6, 7)) if TR
         else tuple('en_content%s.py' % (i or '') for i in ('', 2, 3, 4, 5, 6, 7)))

print('Sayfalar uretiliyor (%s) -> %s' % (LANG, OUT))
for part in PARTS:
    fp = os.path.join(ROOT, part)
    if os.path.exists(fp):
        exec(io.open(fp, encoding='utf-8').read())
    else:
        print('  ATLANDI (yok):', part)
print('Bitti.')
