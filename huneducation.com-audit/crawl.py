# -*- coding: utf-8 -*-
"""huneducation.com tarayicisi: 500 sayfa, robots.txt'e uyar."""
import json, io, re, sys, time, urllib.request, urllib.parse, urllib.robotparser
from concurrent.futures import ThreadPoolExecutor
from collections import deque, Counter

KOK = 'https://huneducation.com'
UA = 'Mozilla/5.0 (compatible; ClaudeSEOAudit/1.0)'
MAX = 500
H = {'User-Agent': UA}

rp = urllib.robotparser.RobotFileParser()
rp.set_url(KOK + '/robots.txt')
try:
    rp.read()
except Exception:
    pass

def metin(h):
    h = re.sub(r'<(script|style|noscript|svg)[^>]*>.*?</\1>', ' ', h, flags=re.S | re.I)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = re.sub(r'&nbsp;|&#\d+;|&[a-z]+;', ' ', h)
    return re.sub(r'\s+', ' ', h).strip()

def govde(h):
    m = re.search(r'<main\b.*?</main>', h, re.S | re.I)
    if m: return m.group(0)
    m = re.search(r'<div[^>]+class="[^"]*entry-content[^"]*".*?(?=<footer|</body)', h, re.S | re.I)
    return m.group(0) if m else h

def cek(u):
    try:
        r = urllib.request.Request(u, headers=H)
        with urllib.request.urlopen(r, timeout=30) as f:
            son = f.geturl()
            ct = f.getheader('Content-Type', '')
            if 'html' not in ct: return None
            h = f.read(900000).decode('utf-8', 'replace')
            return {'kod': f.getcode(), 'son_url': son, 'html': h,
                    'basliklar': {k.lower(): v for k, v in f.getheaders()}}
    except urllib.error.HTTPError as e:
        return {'kod': e.code, 'son_url': u, 'html': '', 'basliklar': {}}
    except Exception as e:
        return {'kod': 0, 'son_url': u, 'html': '', 'hata': str(e)[:60], 'basliklar': {}}

def coz(u, r):
    h = r['html']
    g = govde(h)
    t = re.search(r'<title[^>]*>(.*?)</title>', h, re.S | re.I)
    d = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)', h, re.I)
    c = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']*)', h, re.I)
    h1 = [metin(x) for x in re.findall(r'<h1[^>]*>(.*?)</h1>', h, re.S | re.I)]
    sema = re.findall(r'"@type"\s*:\s*"([A-Za-z]+)"', h)
    return {
        'url': r['son_url'], 'kod': r['kod'],
        'title': metin(t.group(1)) if t else '',
        'desc': d.group(1) if d else '',
        'canonical': c.group(1) if c else '',
        'h1': h1, 'h1_adet': len(h1),
        'h2': len(re.findall(r'<h2[\s>]', h, re.I)),
        'kelime': len(metin(g).split()),
        'img': len(re.findall(r'<img[\s>]', g, re.I)),
        'img_altsiz': len([x for x in re.findall(r'<img[^>]*>', g, re.I) if not re.search(r'alt=["\'][^"\']+', x)]),
        'sema': sorted(set(sema)),
        'hreflang': len(re.findall(r'hreflang=', h, re.I)),
        'noindex': bool(re.search(r'name=["\']robots["\'][^>]*noindex', h, re.I)),
        'og': bool(re.search(r'property=["\']og:title', h, re.I)),
        'bayt': len(h),
        'ic_bag': len(set(re.findall(r'href="(https://huneducation\.com/[^"#?]*)"', h))),
    }

gorulen, sonuc = set(), []
kuyruk = deque([KOK + '/'])
engelli = []
kilit_sayac = Counter()

def normalize(u):
    u = urllib.parse.urljoin(KOK, u).split('#')[0]
    p = urllib.parse.urlparse(u)
    if p.netloc != 'huneducation.com': return None
    if re.search(r'\.(jpg|jpeg|png|webp|gif|svg|pdf|zip|css|js|ico|xml)$', p.path, re.I): return None
    if p.query: return None
    return p.scheme + '://' + p.netloc + p.path

def isle(u):
    r = cek(u)
    if not r: return None, []
    v = coz(u, r)
    bag = []
    if r['html']:
        for m in re.findall(r'href="([^"]+)"', r['html']):
            n = normalize(m)
            if n: bag.append(n)
    return v, bag

t0 = time.time()
with ThreadPoolExecutor(max_workers=5) as ex:
    while kuyruk and len(sonuc) < MAX:
        parti = []
        while kuyruk and len(parti) < 5 and len(sonuc) + len(parti) < MAX:
            u = kuyruk.popleft()
            if u in gorulen: continue
            if not rp.can_fetch(UA, u):
                engelli.append(u); continue
            gorulen.add(u); parti.append(u)
        if not parti: break
        for v, bag in ex.map(isle, parti):
            if v: sonuc.append(v)
            for b in bag:
                if b not in gorulen and len(gorulen) + len(kuyruk) < MAX * 3:
                    kuyruk.append(b)
        if len(sonuc) % 50 < 5:
            print('  %d sayfa (%.0fs)' % (len(sonuc), time.time() - t0), flush=True)
            io.open('crawl.json', 'w', encoding='utf-8').write(json.dumps(
                {'sayfa': sonuc, 'engelli': engelli, 'sure_sn': round(time.time() - t0),
                 'kismi': True}, ensure_ascii=False))
        time.sleep(0.2)

io.open('crawl.json', 'w', encoding='utf-8').write(json.dumps(
    {'sayfa': sonuc, 'engelli': engelli, 'sure_sn': round(time.time() - t0)},
    ensure_ascii=False))
print('TAMAM: %d sayfa, %.0f sn' % (len(sonuc), time.time() - t0))
