# -*- coding: utf-8 -*-
"""Güven bandını kaldırır, "Kısaca" özetini kendi bölümüne çıkarır.

GEREKÇE
  Banttaki dört rakam sayfanın başka yerlerinde zaten duruyordu:
  1999 hem "Neden Hun Education" bölümünde hem footer'da, ofis listesi
  ve 20 üniversite footer'da. Yani bant, aşağıdaki manifesto bölümünün
  kısaltılmış bir tekrarıydı.

  Ancak bandın içinde "Kısaca" özeti de duruyordu ve bölümün yarısından
  fazlası (3525 byte'ın 1917'si) o bloğa aitti. Özet, arama ve cevap
  motorlarının sayfadan alıntı yaptığı yer; bantla birlikte silinseydi
  bir önceki turda kurulan SEO/GEO yapısı da giderdi.

  Bu yüzden bant kaldırılıyor, özet kendi bölümüne (id="ozet") taşınıyor.
  Marquee, dört rakam hücresi ve alttaki paragraf siliniyor.
"""
import io, re, sys

SITE = sys.argv[1] if len(sys.argv) > 1 else 'site'

TRUST = re.compile(r'<section class="trust section--dark" id="trust"[^>]*>(.*?)\n</section>', re.S)
BRIEF = re.compile(r'<div class="shell brief"[^>]*>.*?\n  </div>', re.S)


def kaldir(yol):
    s = io.open(yol, encoding='utf-8').read()
    m = TRUST.search(s)
    if not m:
        print('  ! güven bandı bulunamadı:', yol); return False
    b = BRIEF.search(m.group(1))
    if not b:
        print('  ! özet bloğu bulunamadı:', yol); return False

    ozet = b.group(0).replace('id="trust-h"', 'id="ozet-h"')
    yeni = ('<section class="brief-sec section--dark" id="ozet" aria-labelledby="ozet-h">\n'
            '%s\n</section>' % ozet)

    s2 = s[:m.start()] + yeni + s[m.end():]
    # bölüm yorumu da güncellensin
    s2 = s2.replace('BÖLÜM 3 — GÜVEN BANDI', 'BÖLÜM 3 — KISACA (özet)')
    s2 = s2.replace('SECTION 3 - TRUST BAND', 'SECTION 3 - IN BRIEF (summary)')

    for zorunlu in ('<header class="hdr', '<main', '</main>', '<footer', 'brief__facts'):
        if zorunlu not in s2:
            print('  ! %s kayboldu, yazma iptal: %s' % (zorunlu, yol)); return False

    io.open(yol, 'w', encoding='utf-8').write(s2)
    print('%-22s güven bandı kaldırıldı (%d -> %d byte)' % (yol, len(m.group(0)), len(yeni)))
    return True


for d in ('tr/index.html', 'index.html'):
    kaldir(SITE + '/' + d)
