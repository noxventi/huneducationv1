# -*- coding: utf-8 -*-
"""Artık hiçbir sayfada kullanılmayan CSS kurallarını siler.

Bir önceki temizlikte kaba bir regex kullanmış ve ilgisiz bir kuralı
(.brief-sec) da silmiştim. Bu betik onun yerine iki aşamalı çalışır:

  1. Kural bloklarını ayrıştırır (süslü parantez sayarak, @media
     bloklarının içine de girerek).
  2. Bir bloğu YALNIZCA seçicisindeki bütün sınıflar ölüyse siler.
     Seçicide tek bir canlı sınıf varsa bloğa dokunmaz.

Sonunda süslü parantez dengesini ve silinmemesi gereken bir örnek
seçicinin yerinde durduğunu doğrular.
"""
import io, re, sys, glob

CSS = 'site/assets/css/sections.css'
OLU = sys.argv[1:] or [
    'brief__facts', 'brief__cta', 'brief__meta',
    'stories', 'stories__head', 'stories__row',
    'story', 'story__frame', 'story__ph', 'story__meta',
    'story--brief', 'story__briefTitle', 'story__checklist',
]
KORU = '.brief-sec'   # silinmemesi gereken kontrol seçicisi


def bloklar(s):
    """(baslangic, bitis, secici) üçlüleri. @media içindekiler dâhil."""
    out, i, n = [], 0, len(s)
    while i < n:
        a = s.find('{', i)
        if a == -1:
            break
        secici = s[max(0, s.rfind('}', 0, a) + 1):a]
        secici = secici[secici.rfind('*/') + 2:] if '*/' in secici else secici
        secici = secici.strip()
        if secici.startswith('@'):          # @media, @supports: içine gir
            i = a + 1
            continue
        derinlik, j = 1, a + 1
        while j < n and derinlik:
            if s[j] == '{':
                derinlik += 1
            elif s[j] == '}':
                derinlik -= 1
            j += 1
        out.append((a - len(secici) - (len(s[a - len(secici) - 1:a]) - len(secici)), j, secici))
        i = j
    return out


s = io.open(CSS, encoding='utf-8').read()
once = len(s)

# Silinecek blokların aralıklarını topla
sil = []
for a, b, secici in bloklar(s):
    siniflar = re.findall(r'\.([\w-]+)', secici)
    if siniflar and all(c in OLU for c in siniflar):
        bas = s.rfind('\n', 0, a) + 1
        sil.append((bas, b, secici))

for a, b, secici in reversed(sil):
    s = s[:a] + s[b:]

# Arta kalan boş satırları sadeleştir
s = re.sub(r'\n{3,}', '\n\n', s)

denge = s.count('{') - s.count('}')
if denge != 0:
    print('  ! süslü parantez dengesi bozuldu (%d), yazma iptal' % denge); sys.exit(1)
if KORU not in s:
    print('  ! %s silinmiş, yazma iptal' % KORU); sys.exit(1)

io.open(CSS, 'w', encoding='utf-8').write(s)
print('%d kural silindi, %d -> %d byte' % (len(sil), once, len(s)))
for _, _, sec in sil:
    print('   -', ' '.join(sec.split())[:64])
