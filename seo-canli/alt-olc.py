# -*- coding: utf-8 -*-
"""Alt metnini DOGRU olcer: alt yok (hata) / alt="" (dekoratif, dogru) /
alt dolu (iyi) ayrimi yapar ve izleme pikselleri ile ikonlari haric tutar."""
import re, time, urllib.request, collections
H = {'User-Agent': 'Mozilla/5.0 (compatible; AltCheck/1.0)'}
URL = [
 'https://huneducation.com/', 'https://huneducation.com/why-hungary/',
 'https://huneducation.com/education-in-hungary/', 'https://huneducation.com/universities/',
 'https://huneducation.com/about-us/', 'https://huneducation.com/costs/',
 'https://huneducation.com/course/biology-bsc-pte/',
 'https://huneducation.com/university/university-of-pecs/',
 'https://tr.huneducation.com/', 'https://tr.huneducation.com/hakkimizda/',
 'https://tr.huneducation.com/macaristan-universiteleri/',
]

def dekoratif(t):
    u = (re.search(r'src=["\']([^"\']*)', t) or [None, ''])[1]
    return ('data:image' in u or '/res/flags/' in u or 'facebook.com/tr?' in u
            or re.search(r'width=["\']1["\']', t) or '.svg' in u
            or 'display: ?none' in t)

top = collections.Counter()
sorunlu = []
for u in URL:
    try:
        s = urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=40).read().decode('utf-8', 'replace')
    except Exception as e:
        print('  ! %s %s' % (u, e)); continue
    for t in re.findall(r'<img[^>]*>', s):
        if dekoratif(t):
            top['dekoratif (haric)'] += 1; continue
        m = re.search(r'alt=["\']([^"\']*)["\']', t)
        if m is None:
            top['ALT YOK (hata)'] += 1
            sorunlu.append((u, re.sub(r'\s+', ' ', t)[:110]))
        elif m.group(1).strip() == '':
            top['alt="" (bos)'] += 1
            sorunlu.append((u, re.sub(r'\s+', ' ', t)[:110]))
        else:
            top['alt dolu'] += 1
    time.sleep(1.2)

print('%d sayfa tarandi' % len(URL))
for k, v in top.most_common():
    print('   %-22s %d' % (k, v))
print()
if sorunlu:
    print('duzeltilmesi gerekenler (ilk 10):')
    for u, t in sorunlu[:10]:
        print('  %s' % u.replace('https://', ''))
        print('     %s' % t)
else:
    print('Icerik gorsellerinin tamaminda alt metni dolu.')
