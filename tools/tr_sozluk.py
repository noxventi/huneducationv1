# -*- coding: utf-8 -*-
"""Turkce yerellestirme sozlugu.

Canlida bazi kurs ve universite kayitlarinin Turkce cevirisi yok; TR
sayfasinda Ingilizce adiyla gorunuyorlar. Bu dosya YALNIZCA BOSLUK
DOLDURUR: canlida Turkcesi varsa o kazanir, yoksa buradaki kullanilir.
Boylece musteri canlida bir ceviri girdiginde burasi otomatik devre disi
kalir ve iki kaynak catismaz.

Adlandirma, canlidaki mevcut Turkce basliklarin kendi kurallarini izler:
    "Kentsel Sistemler Muhendisligi MSc - DE"
    "Makine Muhendisligi YL - ELTE"
    "Tip - SZTE"
yani  <Turkce ad> [derece kodu] – <universite kisaltmasi>
ayirac olarak uzun tire (en dash) kullanilir.
"""

TIRE = '–'  # en dash: canlidaki basliklarda kullanilan ayirac


def _t(ad, kisaltma=None):
    return '%s %s %s' % (ad, TIRE, kisaltma) if kisaltma else ad


# Ingilizce baslik -> Turkce baslik
KURS_TR = {
    # --- Nyiregyhaza ---
    'Agricultural Engineering - NYE':               _t('Ziraat Mühendisliği', 'NYE'),
    'Business Administration and Management - NYE': _t('İşletme ve Yönetim', 'NYE'),
    'Chemistry - NYE':                              _t('Kimya', 'NYE'),
    'Mechanical Engineering - NYE':                 _t('Makine Mühendisliği', 'NYE'),
    'MSc Environmentral Science - NYE':             _t('Çevre Bilimleri MSc', 'NYE'),
    'MA Social Pedagogy - NYE':                     _t('Sosyal Pedagoji MA', 'NYE'),

    # --- Pecs ---
    'Dietetics BSc - PTE':                          _t('Diyetetik', 'PTE'),
    'Midwifery BSc​':                          _t('Ebelik'),
    'Physiotherapy BSc - PTE':                      _t('Fizyoterapi', 'PTE'),
    'Social Work MA - PTE':                         _t('Sosyal Hizmet MA', 'PTE'),
    'Biotechnology MSc - PTE':                      _t('Biyoteknoloji MSc', 'PTE'),
    'Physiotherapy MSc - PTE':                      _t('Fizyoterapi MSc', 'PTE'),

    # --- Semmelweis ---
    'Physiotherapy - SOTE':                         _t('Fizyoterapi', 'SOTE'),
    'Nursing BSc - SOTE':                           _t('Hemşirelik', 'SOTE'),
    'Medical Diagnostic Analysis (Optometry) - SOTE': _t('Tıbbi Tanı Analizi (Optometri)', 'SOTE'),
    'Physiotherapy MSc - SOTE':                     _t('Fizyoterapi MSc', 'SOTE'),
    'Nursing MSc - SOTE':                           _t('Hemşirelik MSc', 'SOTE'),

    # --- Veteriner ---
    'Veterinary Medicine':                          _t('Veteriner Hekimliği', 'UNIVET'),

    # --- ELTE ---
    'Kindergarten Education - ELTE':                _t('Okul Öncesi Öğretmenliği', 'ELTE'),

    # --- John von Neumann ---
    'Computer Science Engineering BSc - NJE':       _t('Bilgisayar Mühendisliği', 'NJE'),

    # --- Metropolitan ---
    'Marketing - METU':                             _t('Pazarlama MA', 'METU'),
    'Commerce and Marketing - METU':                _t('Ticaret ve Pazarlama', 'METU'),
    'Business Administration - METU':               _t('İşletme MA', 'METU'),
    'Business Administration and Management - METU': _t('İşletme ve Yönetim', 'METU'),

    # --- IBS ---
    'Business Management IBS':                      _t('İşletme Yönetimi', 'IBS'),
    'International Business Economics IBS':         _t('Uluslararası İşletme ve Ekonomi', 'IBS'),
    'Corporate Finance IBS':                        _t('Kurumsal Finans', 'IBS'),

    # --- Hazirlik ---
    'Foundation Year for Business Studies':         'İşletme Bölüm Hazırlık Yılı',
    'Foundation Year for Business Informatics':     'İşletme Bilişimi Bölüm Hazırlık Yılı',
    'Foundation Year for Business Studies (Delivered In German)': 'İşletme Bölüm Hazırlık Yılı (Almanca)',
    'General English Course':                       'Genel İngilizce Kursu',

    # --- Kodolanyi ---
    'Tourism and Catering - KJU':                   _t('Turizm ve Otelcilik', 'KJU'),

    # --- Cesitli yuksek lisans ---
    'MSc Business Informatics':                     'İşletme Bilişimi MSc',
    'MSc Computer Science':                         'Bilgisayar Bilimleri MSc',
    'MSc Food Safety and Quality Engineering':      'Gıda Güvenliği ve Kalite Mühendisliği MSc',
    'Interior and Spatial Design MA':               'İç Mimarlık ve Mekân Tasarımı MA',
    'Social Policy MA':                             'Sosyal Politika MA',
    'Kimya - Master':                               'Kimya MSc',

    # --- BME / Obuda ---
    'Civil Engineering - BME':                      _t('İnşaat Mühendisliği', 'BME'),
    'Geoinformatics - OE':                          _t('Jeoinformatik MSc', 'OE'),

    # --- Szeged ---
    'Applied Mathematics MSc - SZTE':               _t('Uygulamalı Matematik MSc', 'SZTE'),
    'Classical Musical Instrumental Performance (Viola) MA - SZTE':
        _t('Klasik Enstrüman İcracılığı (Viyola) MA', 'SZTE'),

    # --- Miskolc ---
    'Performance - Miskolc':                        _t('Sahne Sanatları', 'Miskolc'),
    'Nursing and Patient Care (Nurse) - Miskolc':   _t('Hemşirelik ve Hasta Bakımı', 'Miskolc'),
    'BSc in Mechanical Engineering - Miskolc':      _t('Makine Mühendisliği', 'Miskolc'),
    'Materials Engineering - Miskolc':              _t('Malzeme Mühendisliği', 'Miskolc'),
    'BSc in Logistics Engineering - Miskolc':       _t('Lojistik Mühendisliği', 'Miskolc'),
    'English and American Studies - Miskolc':       _t('İngiliz Dili ve Amerikan Çalışmaları', 'Miskolc'),
    'Computer Science Engineering - Miskolc':       _t('Bilgisayar Mühendisliği', 'Miskolc'),
    'Business Administration and Management BSc - Miskolc': _t('İşletme ve Yönetim', 'Miskolc'),

    # --- Spor Bilimleri ---
    'Sport and Exercise Science On Campus -TF':     _t('Spor ve Egzersiz Bilimleri (Yüz Yüze)', 'TF'),
    'International Sports Diplomacy MA On Campus - TF': _t('Uluslararası Spor Diplomasisi MA (Yüz Yüze)', 'TF'),
    'International Sports Diplomacy MA Hybrid - TF': _t('Uluslararası Spor Diplomasisi MA (Hibrit)', 'TF'),
    'Sports Coaching Hybrid MA - TF':               _t('Spor Antrenörlüğü MA (Hibrit)', 'TF'),
}

# Ingilizce universite adi -> Turkce
UNI_TR = {
    'University of Miskolc':                    'Miskolc Üniversitesi',
    'University of Veterinary Medicine (UNIVET)': 'Veteriner Hekimliği Üniversitesi (UNIVET)',
    # Okul adi ozel isim; Turkce sayfada da kendi adiyla anilir
    'Wekerle Business School (WBS)':            'Wekerle Business School (WBS)',
}

# Canlidaki Turkce metinde gecen yazim hatalari.
# Musterinin verisini yeniden yazmiyoruz; yalnizca acik yazim hatalari
# duzeltilir, cunku bunlar sayfada oldugu gibi gorunuyor.
YAZIM = [
    ('Uluslarası', 'Uluslararası'),
    ('Msc ', 'MSc '),
    ('Bsc ', 'BSc '),
    # Canlida ayni kavram uc farkli terimle yazilmis ("1 Yariyil", "1 Donemlik",
    # "1 Sömestr"). Sitenin geri kalani "dönem" kullandigi icin hepsi ona
    # cekiliyor; okuyucu ayni sayfada uc esanlamli terim gormemeli.
    ('Yarıyıl ', 'Dönemlik '),
    ('Yarıyıllık ', 'Dönemlik '),
    ('Sömestr ', 'Dönemlik '),
    ('Sömestir ', 'Dönemlik '),
    ('  ', ' '),
]


def kurs_tr(en, tr):
    """Canlidaki Turkce varsa o kazanir; yoksa sozlukten doldurulur."""
    ad = tr or KURS_TR.get((en or '').strip())
    if not ad:
        return None
    for a, b in YAZIM:
        ad = ad.replace(a, b)
    return ad.strip()


def uni_tr(en, tr):
    ad = tr or UNI_TR.get((en or '').strip())
    if not ad:
        return None
    for a, b in YAZIM:
        ad = ad.replace(a, b)
    return ad.strip()


# ---------------------------------------------------------------------------
# Giris sinavi ve dil seviyesi alanlari
#
# Canlida bu alanlar SERBEST METIN ve hepsi Ingilizce. TR sayfasinda oldugu
# gibi gorunuyordu ("Interview", "Skype, Zoom, Teams" ...). 52 farkli varyant
# var ama hepsi ayni birkac bilesenden olusuyor. Bu yuzden metni tek tek
# cevirmek yerine BILESENLERINE ayirip iki dilde yeniden uretiyoruz:
# yeni bir varyant eklendiginde de calisir.
# ---------------------------------------------------------------------------

# (arama kalibi, bilesen anahtari) - sira onemli: ozel olan once
SINAV_KALIP = [
    ('bme e-admission',        'bme'),
    ('placement test',         'seviye'),
    ('competency test',        'yeterlilik'),
    ('written',                'yazili'),
    ('oral',                   'sozlu'),
    ('interview',              'mulakat'),
    ('portfolio',              'portfolyo'),
    ('motivation',             'motivasyon'),
    ('motivational',           'motivasyon'),
    ('europass',               'ozgecmis'),
    ('cv',                     'ozgecmis'),
    ('reference work',         'referans'),
    ('math',                   'matematik'),
    ('physic',                 'fizik'),
    ('biology',                'biyoloji'),
    ('english language',       'ingilizce'),
    ('entrance exam',          'girissinavi'),
    ('examination',            'girissinavi'),
    ('skype',                  'online'),
    ('zoom',                   'online'),
    ('teams',                  'online'),
    ('online',                 'online'),
]

# Bilesen sirasi: cikti her zaman ayni duzende okunur
SINAV_SIRA = ['girissinavi', 'yeterlilik', 'yazili', 'sozlu', 'mulakat', 'matematik',
              'fizik', 'biyoloji', 'ingilizce', 'seviye', 'portfolyo', 'ozgecmis',
              'motivasyon', 'referans', 'bme', 'online']


def sinav_bilesenleri(metin):
    """Serbest metni bilesen anahtarlarina cevirir."""
    if not metin:
        return []
    t = metin.lower().replace('&amp;', '&')
    bulunan = set()
    for kalip, anahtar in SINAV_KALIP:
        if kalip in t:
            bulunan.add(anahtar)
    # "mulakat" zaten sozlu bir sinav; ikisi birden varsa sozlu'yu birak
    if 'mulakat' in bulunan and 'sozlu' in bulunan:
        bulunan.discard('sozlu')
    # tek basina "entrance exam" digerleri varken bilgi tasimaz
    if 'girissinavi' in bulunan and len(bulunan) > 1:
        bulunan.discard('girissinavi')
    return [k for k in SINAV_SIRA if k in bulunan]


# Dil seviyesi: CEFR kodlari evrensel, kelimeler cevrilir
DIL_SEVIYE = {
    'b2': ('B2', 'B2'),
    'b1': ('B1', 'B1'),
    'a2': ('A2', 'A2'),
    'c1': ('C1', 'C1'),
    'intermediate': ('Intermediate (B1-B2)', 'Orta düzey (B1-B2)'),
    'upper intermediate': ('Upper intermediate (B2)', 'Orta-üstü (B2)'),
    'english language proficiency': ('Proficiency certificate required', 'Yeterlilik belgesi istenir'),
    'c1 french': ('C1 French', 'C1 Fransızca'),
}


def dil_seviye_kod(metin):
    if not metin:
        return None
    return metin.strip().lower() if metin.strip().lower() in DIL_SEVIYE else None
