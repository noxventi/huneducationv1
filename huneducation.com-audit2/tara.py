# -*- coding: utf-8 -*-
"""Sitemap'ten temsili ornek cekip sayfa sinyallerini olcer. Tek is parcacigi,
gecikmeli: barindirma bugun iki kez 508 dondu."""
import urllib.request, urllib.error, re, json, io, time, html, random

UA = {'User-Agent': 'Mozilla/5.0 (huneducation-denetim2)'}

def al(u, timeout=45):
    r = urllib.request.Request(u, headers=UA)
    for _ in range(3):
        try:
            with urllib.request.urlopen(r, timeout=timeout) as f:
                return f.getcode(), f.read().decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            if e.code in (429, 508, 503):
                time.sleep(15); continue
            return e.code, ''
        except Exception:
            time.sleep(5)
    return 0, ''

def sitemap_urls(host):
    out = {}
    for f in ('page', 'course', 'university', 'course-city', 'course-level', 'course-category'):
        k, s = al('https://%s/%s-sitemap.xml' % (host, f))
        locs = re.findall(r'<loc>([^<]+)</loc>', s)
        out[f] = locs
        time.sleep(0.8)
    return out

def olc(u):
    kod, s = al(u)
    if not s:
        return {'url': u, 'kod': kod, 'hata': True}
    def bul(p, g=1):
        m = re.search(p, s, re.S | re.I)
        return html.unescape(m.group(g)).strip() if m else ''
    govde = re.sub(r'<(script|style|noscript)[^>]*>.*?</\1>', ' ', s, flags=re.S | re.I)
    govde = re.sub(r'<[^>]+>', ' ', govde)
    kelime = len(re.sub(r'\s+', ' ', html.unescape(govde)).split())
    h = {}
    for n in (1, 2, 3):
        h['h%d' % n] = len(re.findall(r'<h%d[\b >]' % n, s, re.I))
    ic = len(set(re.findall(r'href="(https://(?:tr\.)?huneducation\.com/[^"#?]*)"', s)))
    dis = len(set(re.findall(r'href="https?://(?!(?:tr\.)?huneducation\.com)[^"]+"', s)))
    tipler = sorted(set(re.findall(r'"@type"\s*:\s*"([^"]+)"', s)))
    return {
        'url': u, 'kod': kod, 'bayt': len(s.encode('utf-8')),
        'title': bul(r'<title[^>]*>(.*?)</title>'),
        'desc': bul(r'<meta name="description" content="([^"]*)"'),
        'h1': bul(r'<h1[^>]*>(.*?)</h1>').replace('\n', ' ')[:90],
        'basliklar': h, 'kelime': kelime,
        'ic_baglanti': ic, 'dis_baglanti': dis,
        'robots': bul(r'name=["\']robots["\'][^>]*content=["\']([^"\']*)'),
        'canonical': bul(r'rel=["\']canonical["\'] href=["\']([^"\']+)'),
        'hreflang': len(re.findall(r'rel="alternate" hreflang=', s)),
        'schema': tipler,
        'gorsel': len(re.findall(r'<img\b', s, re.I)),
    }

random.seed(7)
sonuc = {}
for host in ('huneducation.com', 'tr.huneducation.com'):
    sm = sitemap_urls(host)
    sec = []
    sec += sm['page'][:14]
    sec += random.sample(sm['course'], min(18, len(sm['course'])))
    sec += random.sample(sm['university'], min(6, len(sm['university'])))
    for t in ('course-city', 'course-level', 'course-category'):
        sec += random.sample(sm[t], min(3, len(sm[t])))
    sonuc[host] = {'sitemap_sayilari': {k: len(v) for k, v in sm.items()}, 'sayfalar': []}
    print('%s: %d URL secildi' % (host, len(sec)), flush=True)
    for i, u in enumerate(sec, 1):
        sonuc[host]['sayfalar'].append(olc(u))
        if i % 10 == 0:
            print('  %d/%d' % (i, len(sec)), flush=True)
        time.sleep(1.1)

io.open('huneducation.com-audit2/crawl2.json', 'w', encoding='utf-8').write(
    json.dumps(sonuc, ensure_ascii=False, indent=1))
n = sum(len(v['sayfalar']) for v in sonuc.values())
print('bitti: %d sayfa -> crawl2.json' % n)
