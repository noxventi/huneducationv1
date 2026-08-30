# -*- coding: utf-8 -*-
"""Ana sayfayi bir ogrenci adayinin soru sirasina gore yeniden dizer.

SORUN
  13 bolum vardi ve ikisi ayni isi yapiyordu: "Program bulucu" (3 soruluk
  sihirbaz) ile "Populer alanlar" galerisi ziyaretciye ayni soruyu
  soruyordu. "Rehber" bolumu ise header'daki acilir menuyle ayni
  baglantilari veriyordu. Ustelik maliyet, ogrencinin en erken sordugu
  soru olmasina ragmen 10. sirada duruyordu.

COZUM
  Bolumler ziyaretcinin sordugu sirayla diziliyor:
      Ne teklif ediyorsunuz   -> hero
      Kimsiniz                -> guven bandi
      Ne okuyabilirim         -> alanlar
      Ne kadara mal olur      -> maliyet
      Nerede okurum           -> universiteler
      Neden siz               -> manifesto
      Sirada ne var           -> surec
      Aklimdaki sorular       -> SSS
      Ne yapmaliyim           -> iletisim formu

  Iki bolum kaldiriliyor (bulucu, rehber). Hicbir metin silinmiyor;
  kaldirilan iki bolumun isini katalog sayfasi ve header menusu zaten
  yapiyor.
"""
import io, os, re, sys

SITE = sys.argv[1] if len(sys.argv) > 1 else 'site'

# Yeni sira: (section id, yeni baslik yorumu)
SIRA = [
    ('hero',          'HERO',                                   'HERO'),
    ('ozet',          'KISACA (özet)',                          'IN BRIEF (summary)'),
    ('alanlar',       'NE OKUYABİLİRSİNİZ (alan galerisi)',     'WHAT YOU CAN STUDY (field gallery)'),
    ('universiteler', 'NEREDE OKUYABİLİRSİNİZ (harita)',        'WHERE YOU CAN STUDY (map)'),
    ('maliyet',       'NE KADARA MAL OLUR (etkileşimli bütçe)', 'WHAT IT COSTS (interactive budget)'),
    ('macaristan',    'NEDEN HUN EDUCATION',                    'WHY HUN EDUCATION'),
    ('surec',         'SÜREÇ (6 adım)',                         'THE PROCESS (6 steps)'),
    ('sss',           'SIK SORULANLAR',                         'FAQ'),
    ('gorusme',       'İLETİŞİM',                               'CONTACT'),
]
KALDIR = {'bulucu', 'rehber'}

# Türkçe dosyada "BÖLÜM n —", İngilizcede "SECTION n -" yazıyor
BLOK = re.compile(
    r'<!-- ={10,}\s*\n\s*(?:BÖLÜM|SECTION)[^\n]*\n\s*={10,} -->\s*\n(.*?)(?=\n<!-- ={10,}|\n</main>)',
    re.S)

BASLIK = {
    'tr': dict(etiket='BÖLÜM', ayrac='—'),
    'en': dict(etiket='SECTION', ayrac='-'),
}


def bloklari_al(s):
    """id -> gövde. Bölüm yorumları atılır, yenisi yazılır."""
    out = {}
    for m in BLOK.finditer(s):
        govde = m.group(1).rstrip()
        sid = re.search(r'<section[^>]*id="([^"]+)"', govde)
        if sid:
            out[sid.group(1)] = govde
    return out


def yeniden_diz(yol, tr):
    s = io.open(yol, encoding='utf-8').read()
    bloklar = bloklari_al(s)

    eksik = [i for i, _, _ in SIRA if i not in bloklar]
    if eksik:
        print('  ! bölüm bulunamadı: %s (%s)' % (eksik, yol))
        return False

    # Sinir <main> etiketidir. Ilk "<!-- =" yorumuna gore kesmek, sayfanin
    # basindaki perde/imlec/header bloklarini da icine alir ve sayfayi
    # bozar; bu hata bir kez yapildi, bir daha yapilmasin diye burada
    # acikca <main> araniyor.
    ana = re.search(r'<main\b[^>]*>', s)
    if not ana:
        print('  ! <main> bulunamadı:', yol); return False
    bas = ana.end()
    son = s.index('</main>')
    parcalar = []
    for n, (sid, ad_tr, ad_en) in enumerate(SIRA, start=2):
        cizgi = '=' * 66
        b = BASLIK['tr' if tr else 'en']
        parcalar.append('<!-- %s\n     %s %d %s %s\n     %s -->\n%s\n'
                        % (cizgi, b['etiket'], n, b['ayrac'],
                           ad_tr if tr else ad_en, cizgi, bloklar[sid]))

    yeni = s[:bas] + '\n' + '\n'.join(parcalar) + '\n' + s[son:]
    # Emniyet kemeri: sayfanin catisi yerinde mi?
    for zorunlu in ('<header class="hdr', '<main', '</main>', '<footer'):
        if zorunlu not in yeni:
            print('  ! %s kayboldu, yazma iptal: %s' % (zorunlu, yol)); return False
    io.open(yol, 'w', encoding='utf-8').write(yeni)
    atilan = sorted(set(bloklar) - {i for i, _, _ in SIRA})
    print('%-20s %d bölüm dizildi, kaldırılan: %s'
          % (os.path.relpath(yol, SITE), len(SIRA), ', '.join(atilan) or '-'))
    return True


for d, tr in (('tr/index.html', True), ('index.html', False)):
    yeniden_diz(os.path.join(SITE, d), tr)
