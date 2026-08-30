# -*- coding: utf-8 -*-
"""Anasayfa görsellerini mobilde hafifletir.

SORUN
  Anasayfadaki 13 fotoğraf tek boyutta (1536–1672 px) sunuluyordu ve
  hiçbirinde srcset/width/height yoktu. Telefonda hepsi tam boyutta
  indirilip çözülüyor: 82 MB çözülmüş piksel. Safari bellek baskısında
  sekmeyi düşürüp yeniden yüklüyor — "sayfa durduk yere yenileniyor"
  şikâyetinin en olası kaynağı bu.

ÇÖZÜM
  Her fotoğrafın 760 px'lik bir eşi üretilir; etikete srcset, sizes ve
  gerçek width/height eklenir. Telefon artık 760 px'lik dosyayı indirir:
  çözülmüş bellek ~20 MB'a iner, yer ayırma da baştan doğru yapıldığı
  için yükleme sırasında düzen zıplamaz.
"""
import io, os, re
from PIL import Image

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(KOK, 'site', 'assets', 'img')
KUCUK = 760

SAYFALAR = [('site/index.html', 'assets/img/'), ('site/tr/index.html', '../assets/img/')]


def kucuk_uret(ad):
    """760 px eşi yoksa üretir; gerçek ölçüleri döndürür."""
    p = os.path.join(IMG, ad)
    im = Image.open(p)
    w, h = im.size
    kad = ad[:-5] + '-760.webp'
    kp = os.path.join(IMG, kad)
    if not os.path.exists(kp) and w > KUCUK:
        k = im.convert('RGB').resize((KUCUK, round(h * KUCUK / w)), Image.LANCZOS)
        k.save(kp, 'WEBP', quality=80, method=6)
    kw = Image.open(kp).size[0] if os.path.exists(kp) else w
    return w, h, (kad if os.path.exists(kp) else None), kw


def calis():
    toplam_once = toplam_sonra = 0
    for yol, onek in SAYFALAR:
        tam = os.path.join(KOK, yol)
        s = io.open(tam, encoding='utf-8').read()
        n = 0

        def degistir(m):
            nonlocal n, toplam_once, toplam_sonra
            etiket, ad = m.group(0), m.group(1)
            if 'srcset' in etiket:
                return etiket
            w, h, kad, kw = kucuk_uret(ad)
            toplam_once += w * h * 4 / 1024 / 1024
            toplam_sonra += (kw * round(h * kw / w) if kad else w * h) * 4 / 1024 / 1024
            ek = ' width="%d" height="%d"' % (w, h)
            if kad:
                ek = (' srcset="%s%s %dw, %s%s %dw"'
                      ' sizes="(max-width: 900px) 92vw, 640px"' % (onek, kad, kw, onek, ad, w)) + ek
            # width/height zaten varsa tekrar yazma
            if 'width=' in etiket:
                ek = ek.split(' width=')[0]
            n += 1
            return etiket[:-1] + ek + '>'

        s = re.sub(r'<img[^>]*src="' + re.escape(onek) + r'(\d\d-[^"]+\.webp)"[^>]*>', degistir, s)
        io.open(tam, 'w', encoding='utf-8').write(s)
        print('%-22s %d görsel etiketi yenilendi' % (yol, n))

    print('çözülmüş bellek (mobil): %.0f MB -> %.0f MB'
          % (toplam_once / 2, toplam_sonra / 2))


if __name__ == '__main__':
    calis()
