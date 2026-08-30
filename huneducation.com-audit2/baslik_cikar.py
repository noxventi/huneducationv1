# -*- coding: utf-8 -*-
"""Rakip sayfalarin H2/H3 yapisini cikarir. Konu bosluklarini tahminle degil,
gercekten ne yazdiklarina bakarak bulmak icin."""
import urllib.request, urllib.error, re, json, io, time, html

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36'}
SAYFALAR = [
 ('BIZ',        'https://tr.huneducation.com/macaristanda-universite-okumak/'),
 ('academix',   'https://www.academix.com.tr/yurtdisinda-universite/macaristanda-universite'),
 ('icesturkey', 'https://www.icesturkey.com/macaristan-universiteleri'),
 ('elt',        'https://www.elt.com.tr/macaristanda-universite-egitim'),
 ('gedu',       'https://gedu.com.tr/macaristan-universiteleri/'),
 ('iecc',       'https://www.iecc.com.tr/macaristan-universite-egitimi'),
]

def al(u):
    r = urllib.request.Request(u, headers=UA)
    for _ in range(3):
        try:
            with urllib.request.urlopen(r, timeout=45) as f:
                return f.read().decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            if e.code in (503, 508, 429):
                time.sleep(20); continue
            return ''
        except Exception:
            time.sleep(6)
    return ''

def temizle(t):
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()

out = {}
for ad, u in SAYFALAR:
    s = al(u)
    if not s:
        out[ad] = {'hata': True}; print('%-12s alinamadi' % ad, flush=True); continue
    bas = []
    for m in re.finditer(r'<h([23])[^>]*>(.*?)</h\1>', s, re.S | re.I):
        t = temizle(m.group(2))
        if 3 <= len(t) <= 110:
            bas.append((int(m.group(1)), t))
    out[ad] = {'url': u, 'basliklar': bas}
    print('%-12s %d baslik' % (ad, len(bas)), flush=True)
    time.sleep(2.5)

io.open('huneducation.com-audit2/basliklar.json', 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
print('\nyazildi')
