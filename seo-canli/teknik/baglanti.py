# -*- coding: utf-8 -*-
import urllib.request, re, time, html
KAYNAK = 'https://huneducation.com/'
def al(u, method='GET'):
    r = urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0 (teknik-denetim)'}, method=method)
    try:
        with urllib.request.urlopen(r, timeout=40) as f:
            return f.getcode(), f.geturl()
    except urllib.error.HTTPError as e:
        return e.code, u
    except Exception:
        return 0, u

req = urllib.request.Request(KAYNAK, headers={'User-Agent':'Mozilla/5.0'})
s = urllib.request.urlopen(req, timeout=45).read().decode('utf-8','replace')
ham = re.findall(r'<a[^>]+href="(https://(?:tr\.)?huneducation\.com[^"#?]*)"', s)
uniq = []
for u in ham:
    if u not in uniq:
        uniq.append(u)
uniq = uniq[:22]
print('anasayfadan ornek %d ic baglanti kontrol ediliyor\n' % len(uniq))
kotu, yonl = [], []
for u in uniq:
    kod, son = al(u)
    isaret = 'ok'
    if kod >= 400 or kod == 0:
        isaret = 'HATA'; kotu.append((u, kod))
    elif son.rstrip('/') != u.rstrip('/'):
        isaret = 'yonlendirme'; yonl.append((u, son))
    print('  %-3s %-58s %s' % (kod, u.replace('https://','')[:58], isaret))
    time.sleep(1.2)
print()
print('kirik: %d | yonlendirilen: %d | saglam: %d' % (len(kotu), len(yonl), len(uniq)-len(kotu)-len(yonl)))
for u, s2 in yonl: print('  yonlendirme: %s -> %s' % (u, s2))
