# -*- coding: utf-8 -*-
"""Sema kapsamini ornekleyerek dogrular: her sayfa tipinden rastgele URL cekip
beklenen dugumlerin varligina bakar. Tek sayfa dogrulamasi yeterli degil."""
import io, json, re, random, time, urllib.request
H = {'User-Agent': 'Mozilla/5.0 (compatible; SEOCheck/1.0)'}

def cek(u):
    try:
        r = urllib.request.Request(u, headers=H)
        with urllib.request.urlopen(r, timeout=40) as f:
            return f.getcode(), f.read(600000).decode('utf-8', 'replace')
    except Exception as e:
        return getattr(e, 'code', 0), ''

def dugumler(s):
    m = re.search(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', s, re.S)
    if not m: return []
    try: d = json.loads(m.group(1))
    except Exception: return ['BOZUK-JSON']
    out = []
    for n in d.get('@graph', [d]):
        t = n.get('@type')
        out.append('+'.join(t) if isinstance(t, list) else str(t))
    return out

def sitemapten(url, n, seed):
    kod, s = cek(url)
    u = re.findall(r'<loc>([^<]+)</loc>', s)
    u = [x for x in u if x.rstrip('/').count('/') > 3]
    random.seed(seed)
    return random.sample(u, min(n, len(u)))

hedef = []
hedef += [('program-EN', x) for x in sitemapten('https://huneducation.com/course-sitemap.xml', 6, 11)]
hedef += [('program-TR', x) for x in sitemapten('https://tr.huneducation.com/course-sitemap.xml', 5, 12)]
hedef += [('uni-EN', x) for x in sitemapten('https://huneducation.com/university-sitemap.xml', 3, 13)]
hedef += [('uni-TR', x) for x in sitemapten('https://tr.huneducation.com/university-sitemap.xml', 2, 14)]
hedef += [('sayfa-EN', x) for x in sitemapten('https://huneducation.com/page-sitemap.xml', 3, 15)]
hedef += [('sayfa-TR', x) for x in sitemapten('https://tr.huneducation.com/page-sitemap.xml', 3, 16)]

print('%-11s %-5s %-9s %-9s %s' % ('tip', 'kod', 'hreflang', 'canonical', 'sema dugumleri'))
sorun = []
for tip, u in hedef:
    kod, s = cek(u)
    if kod != 200:
        sorun.append((u, kod)); print('%-11s %-5s  !!! erisilemedi' % (tip, kod)); continue
    d = dugumler(s)
    hl = len(re.findall(r'hreflang=', s))
    can = 'var' if re.search(r'rel=["\']canonical', s) else 'YOK'
    bekle = {'program': 'Course', 'uni': 'CollegeOrUniversity'}.get(tip.split('-')[0])
    isaret = '' if (not bekle or bekle in d) else '   <<< EKSIK: %s' % bekle
    if isaret: sorun.append((u, 'sema eksik'))
    print('%-11s %-5s %-9d %-9s %s%s' % (tip, kod, hl, can, ','.join(d)[:58], isaret))
    time.sleep(1.5)
print()
print('SORUN: %s' % (sorun or 'yok'))
