# -*- coding: utf-8 -*-
import urllib.request, re, time, html, sys

URLS = [
 ('anasayfa EN',   'https://huneducation.com/'),
 ('sayfa EN',      'https://huneducation.com/costs/'),
 ('katalog EN',    'https://huneducation.com/courses/'),
 ('katalog s.2',   'https://huneducation.com/courses/2/'),
 ('program EN',    'https://huneducation.com/course/architecture-pte/'),
 ('universite EN', 'https://huneducation.com/university/university-of-pecs/'),
 ('alan arsivi',   'https://huneducation.com/course-category/engineering-architecture/'),
 ('sehir arsivi',  'https://huneducation.com/course-city/debrecen/'),
 ('ince arsiv',    'https://huneducation.com/course-category/law/'),
 ('yil arsivi',    'https://huneducation.com/course-year/2025/'),
 ('anasayfa TR',   'https://tr.huneducation.com/'),
 ('program TR',    'https://tr.huneducation.com/kurs/mimarlik-pte/'),
 ('404 testi',     'https://huneducation.com/bu-sayfa-yok-12345/'),
]

def al(u):
    r = urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0 (teknik-denetim)'})
    try:
        with urllib.request.urlopen(r, timeout=45) as f:
            return f.getcode(), f.read().decode('utf-8','replace')
    except urllib.error.HTTPError as e:
        return e.code, ''
    except Exception as e:
        return 0, ''

print('%-15s %-4s %-26s %-9s %-4s %-3s' % ('TIP','KOD','ROBOTS','CANONICAL','HREF','H1'))
print('-'*78)
for ad, u in URLS:
    kod, s = al(u)
    rob = re.search(r'name=["\']robots["\'][^>]*content=["\']([^"\']*)', s)
    rob = rob.group(1) if rob else '(yok = index)'
    can = re.search(r'rel=["\']canonical["\'] href=["\']([^"\']+)', s)
    kendi = 'kendine' if (can and can.group(1).rstrip('/') == u.rstrip('/')) else (can.group(1)[:34] if can else 'YOK')
    hl = len(re.findall(r'rel=["\']alternate["\'] hreflang=', s))
    h1 = len(re.findall(r'<h1[^>]*>', s))
    print('%-15s %-4s %-26s %-9s %-4d %-3d' % (ad, kod, rob[:26], kendi, hl, h1))
    time.sleep(1.4)
