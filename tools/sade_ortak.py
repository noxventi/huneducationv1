# -*- coding: utf-8 -*-
"""sadelestir.py ve sadelestir_en.py'nin paylastigi yardimcilar.

Iki sayfa da ayni konuyu birden fazla basliga bolmustu; okuyucu
icindekilerde 7-8 satir gorup nereye bakacagina karar veremiyordu.
Buradaki islevler bolum tasima ve baslik seviyesi indirme isini yapiyor.
"""
import io, re


def bolum_al(s, hid):
    """<h2 id="hid"> ile bir sonraki <h2 arasindaki blogu dondurur."""
    bas = s.index('<h2 id="%s">' % hid)
    son = s.find('\n<h2 id=', bas + 5)
    if son == -1:
        raise ValueError('bolum sonu bulunamadi: ' + hid)
    return bas, son, s[bas:son]


def h2_h3(blok, baslik):
    """Bolum basligini h3'e indirir; icerik oldugu gibi kalir."""
    return re.sub(r'<h2 id="[^"]+">.*?</h2>', '<h3>%s</h3>' % baslik,
                  blok, count=1, flags=re.S)


def basvuru(p, toc_eski, toc_yeni, ids, basliklar):
    """Uygunluk bolumunu basa tasir, secilen bolumleri h3'e indirir."""
    s = io.open(p, encoding='utf-8').read()
    s = s.replace(toc_eski, toc_yeni, 1)

    b, e, blok = bolum_al(s, ids['uygunluk'])
    s = s[:b] + s[e + 1:]
    hedef = s.index('<h2 id="%s">' % ids['belgeler'])
    s = s[:hedef] + blok + '\n' + s[hedef:]

    for anahtar, baslik in basliklar.items():
        b, e, blok = bolum_al(s, ids[anahtar])
        s = s[:b] + h2_h3(blok, baslik) + s[e:]

    io.open(p, 'w', encoding='utf-8').write(s)
    print('%-26s basvuru sadelestirildi' % p)


def maliyet(p, toc_eski, toc_yeni, ids, basliklar):
    """Alt basliklari ana bolumlerin altina indirir."""
    s = io.open(p, encoding='utf-8').read()
    s = s.replace(toc_eski, toc_yeni, 1)
    for anahtar, baslik in basliklar.items():
        b, e, blok = bolum_al(s, ids[anahtar])
        s = s[:b] + h2_h3(blok, baslik) + s[e:]
    io.open(p, 'w', encoding='utf-8').write(s)
    print('%-26s maliyet sadelestirildi' % p)
