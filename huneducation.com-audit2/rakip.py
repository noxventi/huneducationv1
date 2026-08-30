# -*- coding: utf-8 -*-
import urllib.request, urllib.error, re, json, io, time, html

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36'}

SAYFALAR = [
 ('BIZ  tr.huneducation.com', 'https://tr.huneducation.com/macaristanda-universite-okumak/'),
 ('BIZ  katalog',             'https://tr.huneducation.com/kurslar/'),
 ('elt.com.tr',               'https://www.elt.com.tr/macaristanda-universite-egitim'),
 ('macaristandauniversite',   'https://www.macaristandauniversite.com/'),
 ('gedu.com.tr',              'https://gedu.com.tr/macaristan-universiteleri/'),
 ('iecc.com.tr',              'https://www.iecc.com.tr/macaristan-universite-egitimi'),
 ('unioku.com',               'https://unioku.com/macaristanda-universite'),
 ('icesturkey.com',           'https://www.icesturkey.com/macaristan-universiteleri'),
 ('academix.com.tr',          'https://www.academix.com.tr/yurtdisinda-universite/macaristanda-universite'),
 ('deltaegitim.com.tr',       'https://www.deltaegitim.com.tr/macaristanda-universite-okumak/'),
]

def al(u):
    r = urllib.request.Request(u, headers=UA)
    try:
        with urllib.request.urlopen(r, timeout=40) as f:
            return f.getcode(), f.read().decode('utf-8', 'replace'), dict(f.headers)
    except urllib.error.HTTPError as e:
        return e.code, '', {}
    except Exception as ex:
        return 0, '', {}

def olc(ad, u):
    kod, s, hdr = al(u)
    if not s:
        return {'ad': ad, 'url': u, 'kod': kod, 'hata': True}
    def bul(p, g=1):
        m = re.search(p, s, re.S | re.I)
        return html.unescape(m.group(g)).strip() if m else ''
    govde = re.sub(r'<(script|style|noscript|nav|footer|header)[^>]*>.*?</\1>', ' ', s, flags=re.S | re.I)
    govde = re.sub(r'<[^>]+>', ' ', govde)
    kelime = len(re.sub(r'\s+', ' ', html.unescape(govde)).split())
    tipler = sorted(set(re.findall(r'"@type"\s*:\s*"([^"]+)"', s)))
    return {
        'ad': ad, 'url': u, 'kod': kod,
        'kb': round(len(s.encode('utf-8')) / 1024),
        'kelime': kelime,
        'title': bul(r'<title[^>]*>(.*?)</title>')[:70],
        'title_uz': len(bul(r'<title[^>]*>(.*?)</title>')),
        'desc': 1 if bul(r'<meta name="description" content="([^"]*)"') else 0,
        'h1': len(re.findall(r'<h1[\b >]', s, re.I)),
        'h2': len(re.findall(r'<h2[\b >]', s, re.I)),
        'h3': len(re.findall(r'<h3[\b >]', s, re.I)),
        'gorsel': len(re.findall(r'<img\b', s, re.I)),
        'sema': tipler,
        'sema_n': len(tipler),
        'hreflang': len(re.findall(r'rel="alternate" hreflang=', s)),
        'canonical': 1 if bul(r'rel=["\']canonical["\'] href=["\']([^"\']+)') else 0,
        'og': 1 if 'og:title' in s else 0,
        'https': u.startswith('https'),
    }

out = []
for ad, u in SAYFALAR:
    d = olc(ad, u)
    out.append(d)
    if d.get('hata'):
        print('%-26s HATA kod=%s' % (ad, d['kod']), flush=True)
    else:
        print('%-26s %3s %5d kelime  %2d sema  h1=%d h2=%2d' % (ad, d['kod'], d['kelime'], d['sema_n'], d['h1'], d['h2']), flush=True)
    time.sleep(2.5)

io.open('huneducation.com-audit2/rakipler.json', 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('\nyazildi -> rakipler.json')
