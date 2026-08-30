# -*- coding: utf-8 -*-
"""Elle yazilmis sayfalardaki header'i ureticininkiyle esitler.

Ana sayfa ve program katalogu elle yazilmis dosyalar; uretici onlara
dokunmuyor. Header iki yerde ayri ayri durursa menu zamanla ayrisir,
nitekim daha once tam bu yuzden ana sayfada Ingilizce menu kalmisti.

Bu betik gen_pages.py'nin nav_masaustu() ve nav_mobil() ciktisini alip
dort dosyaya basar. Boylece menunun tek kaynagi gen_pages.py'deki NAV
agaci olur.

python tools/sync_header.py site
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else 'site'

NAV_RX = re.compile(r'(<nav class="hdr__nav"[^>]*>).*?(</nav>)', re.S)
MLIST_RX = re.compile(r'(<ul class="mnav__list">).*?(</ul>)', re.S)


def uret(lang):
    """gen_pages.py'yi ilgili dilde calistirip menu parcalarini alir."""
    ortam = {'__name__': '__gen__', '__file__': os.path.join(ROOT, 'gen_pages.py')}
    kaynak = io.open(os.path.join(ROOT, 'gen_pages.py'), encoding='utf-8').read()
    # Sayfa uretim dongusunu calistirmadan yalnizca tanimlari yukle
    kaynak = kaynak.split("print('Sayfalar uretiliyor")[0]
    sys.argv = ['gen_pages.py', OUT, lang]
    exec(compile(kaynak, 'gen_pages.py', 'exec'), ortam)
    return ortam['nav_masaustu'], ortam['nav_mobil'], ortam['S']


def yaz(yol, nav_html, mnav_html):
    s = io.open(yol, encoding='utf-8').read()
    once = s

    def nav_yerine(m):
        return '%s\n      <span class="hdr__glide" aria-hidden="true"></span>\n      %s\n    %s' % (
            m.group(1), nav_html, m.group(2))

    s = NAV_RX.sub(nav_yerine, s, count=1)
    s = MLIST_RX.sub(lambda m: '%s\n      %s\n    %s' % (m.group(1), mnav_html, m.group(2)), s, count=1)
    io.open(yol, 'w', encoding='utf-8').write(s)
    print('%-24s %s' % (os.path.relpath(yol, OUT), 'guncellendi' if s != once else 'degisiklik yok'))


for lang, dosyalar in (('tr', ['tr/index.html', 'tr/kurslar.html']),
                       ('en', ['index.html', 'courses.html'])):
    masaustu, mobil, S = uret(lang)
    mnav_html = mobil()
    for d in dosyalar:
        yol = os.path.join(OUT, d)
        if not os.path.exists(yol):
            print('  ! yok:', yol); continue
        # aktif sayfa: katalog sayfasinda programlar isaretli olsun
        aktif = S['progs'] if d.endswith(('kurslar.html', 'courses.html')) else S['home']
        yaz(yol, masaustu(aktif), mnav_html)
