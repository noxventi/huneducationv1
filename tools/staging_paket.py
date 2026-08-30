# -*- coding: utf-8 -*-
"""Yerel anasayfayı staging'e taşınmak üzere paketler.

NE ÜRETİR
  cikti/hun2026-paket.zip
    parts/en/*.html   parts/tr/*.html   (9 bölüm + header + footer)
    assets/...                          (css, js, fonts, data, img)

NEDEN DİLİM DİLİM
  Staging sayfası Elementor'da her bölümü ayrı bir kapsayıcıda tutuyor;
  müşteri bölümü Elementor'dan taşıyabilsin/kapatabilsin diye. İçerik
  ise sürüm takibi yapılabilen dosyalarda kalır: kapsayıcının içinde
  tek satırlık [hun2026 s="hero"] kısayolu durur.

JETONLAR
  {ASSETS}      -> tema varlık URI'si
  {LINK:slug}   -> o dildeki staging sayfasının kalıcı bağlantısı
  {HOME}        -> o dildeki hun2026 anasayfası
  {LANGSWITCH}  -> WPML'den üretilen dil değiştirici
  Çözümleme sunucuda (hun2026-loader.php) yapılır; böylece slug'lar
  staging'de değişse bile parçalar yeniden üretilmez.
"""
import io, os, re, zipfile, shutil

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIKTI = os.path.join(KOK, 'cikti')
PAKET = os.path.join(CIKTI, 'hun2026-paket.zip')

# (dil, kaynak dosya, varlık öneki)
KAYNAKLAR = [('en', 'site/index.html', 'assets/'),
             ('tr', 'site/tr/index.html', '../assets/')]

BOLUMLER = ['hero', 'ozet', 'alanlar', 'universiteler', 'maliyet',
            'macaristan', 'surec', 'sss', 'gorusme']


def kes(s, bas, son):
    i = s.index(bas)
    j = s.index(son, i) + len(son)
    return s[i:j]


def etiket_kes(s, bas, ad):
    """İç içe aynı etiketleri sayarak kapanışı bulur.

    Düz `index('</div>')` mobil menüde işe yaramıyor: panelin içinde
    alt menüler için birçok <div> var, ilk kapanış paneli değil onları
    kapatıyordu.
    """
    i = s.index(bas)
    ac, kap = '<' + ad, '</' + ad + '>'
    derinlik, j = 0, i
    while True:
        a = s.find(ac, j)
        k = s.find(kap, j)
        if k == -1:
            raise SystemExit('DUR: %s kapanmiyor' % bas)
        if a != -1 and a < k:
            derinlik += 1
            j = a + len(ac)
        else:
            derinlik -= 1
            j = k + len(kap)
            if derinlik == 0:
                return s[i:j]


def jetonla(html, onek):
    """Varlık yollarını ve iç bağlantıları jetona çevirir."""
    # Varlıklar: hem "../assets/" hem "assets/" biçimi
    html = html.replace('"' + onek, '"{ASSETS}/')
    html = html.replace("'" + onek, "'{ASSETS}/")
    html = re.sub(r'(srcset|src|href)="' + re.escape(onek), r'\1="{ASSETS}/', html)
    # srcset içinde virgülle ayrılmış çoklu yollar
    html = html.replace(' ' + onek, ' {ASSETS}/')

    # Ana sayfa bağlantısı
    html = html.replace('href="/"', 'href="{HOME}"')

    # Sayfa bağlantıları:  xxx.html  ->  {LINK:xxx}
    def bag(m):
        slug = m.group(2)
        # 3. grup isteğe bağlı (#çapa ya da ?sorgu); yoksa None gelir ve
        # doğrudan biçimlendirilirse bağlantının sonuna "None" yapışır.
        ek = m.group(3) or ''
        if slug in ('index', '../index'):
            return '%s="{HOME}%s"' % (m.group(1), ek)
        return '%s="{LINK:%s}%s"' % (m.group(1), slug.lstrip('./'), ek)
    html = re.sub(r'(href)="\.?\.?/?([a-z0-9\-]+)\.html(#[a-z0-9\-]*|\?[^"]*)?"', bag, html)

    # Dil değiştirici bloğu tamamen sunucuya bırakılır
    html = re.sub(r'<div class="lang"[^>]*>.*?</div>', '{LANGSWITCH}', html, flags=re.S)
    return html


def uret():
    if os.path.isdir(CIKTI):
        shutil.rmtree(CIKTI)
    os.makedirs(CIKTI)
    ozet = {}

    for dil, yol, onek in KAYNAKLAR:
        s = io.open(os.path.join(KOK, yol), encoding='utf-8').read()
        klasor = os.path.join(CIKTI, 'parts', dil)
        os.makedirs(klasor, exist_ok=True)

        parcalar = {}
        # Header parçası mobil menü panelini de taşır: panel yerelde
        # <header>'ın DIŞINDA, hemen ardında duruyor. Yalnız <header>
        # kesilirse staging'e hamburger düğmesi gidiyor ama açacağı
        # panel gitmiyor ve düğme hiçbir şey yapmıyor.
        parcalar['header'] = (kes(s, '<header', '</header>')
                              + '\n\n'
                              + etiket_kes(s, '<div class="mnav"', 'div'))
        # Sayfa altbilgisi: ilk <footer> DEĞİL — maliyet kartının içinde de
        # bir <footer class="ccard__foot"> var. Sınıfına göre aranır.
        parcalar['footer'] = kes(s, '<footer class="ftr"', '</footer>')
        ana = s[s.index('<main'):s.index('</main>')]
        for b in BOLUMLER:
            i = ana.index('<section', 0)
            m = re.search(r'<section[^>]*id="%s"[^>]*>' % re.escape(b), ana)
            if not m:
                raise SystemExit('DUR: %s bölümü %s içinde yok' % (b, yol))
            # kapanış </section> etiketini iç içe olanları sayarak bul
            i = m.start()
            derinlik, j = 0, i
            while True:
                a = ana.find('<section', j)
                k = ana.find('</section>', j)
                if k == -1:
                    raise SystemExit('DUR: %s kapanmıyor' % b)
                if a != -1 and a < k:
                    derinlik += 1; j = a + 8
                else:
                    derinlik -= 1; j = k + 10
                    if derinlik == 0:
                        break
            parcalar[b] = ana[i:j]

        for ad, html in parcalar.items():
            io.open(os.path.join(klasor, ad + '.html'), 'w', encoding='utf-8') \
              .write(jetonla(html, onek).strip() + '\n')
        ozet[dil] = {a: len(h) for a, h in parcalar.items()}

    # varlıklar
    shutil.copytree(os.path.join(KOK, 'site', 'assets'), os.path.join(CIKTI, 'assets'))

    with zipfile.ZipFile(PAKET, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for kok, _, dosyalar in os.walk(CIKTI):
            for d in dosyalar:
                p = os.path.join(kok, d)
                if p == PAKET:
                    continue
                z.write(p, os.path.relpath(p, CIKTI).replace(os.sep, '/'))

    print('paket: %s  (%.1f MB)' % (PAKET, os.path.getsize(PAKET) / 1024 / 1024))
    for dil, p in ozet.items():
        print('  %s: %s' % (dil, ', '.join('%s=%d' % (a, n) for a, n in p.items())))
    return PAKET


if __name__ == '__main__':
    uret()
