# -*- coding: utf-8 -*-
"""Canli sitenin SEO sinyallerinin anlik goruntusunu alir.

Her degisiklikten ONCE ve SONRA calistirilir; fark alinarak hicbir mevcut
siralama sinyalinin (baslik, canonical, H1) istemeden degismedigi kanitlanir.
Bu, "siralamada geriye gitme" korkusuna karsi somut guvence.
"""
import io, json, re, sys, urllib.request, time
from concurrent.futures import ThreadPoolExecutor

H = {'User-Agent': 'Mozilla/5.0 (compatible; SEOBaseline/1.0)'}

URL = [
 # --- EN editoryal (14) ---
 'https://huneducation.com/', 'https://huneducation.com/why-hungary/',
 'https://huneducation.com/education-in-hungary/', 'https://huneducation.com/universities/',
 'https://huneducation.com/courses/', 'https://huneducation.com/admission/',
 'https://huneducation.com/costs/', 'https://huneducation.com/masters-education-in-hungary/',
 'https://huneducation.com/studying-medicine-in-hungary-and-pursuing-a-medical-degree-in-hungary/',
 'https://huneducation.com/pilot-training-at-hungarian-universities/',
 'https://huneducation.com/university-education-and-life-in-hungary-what-you-need-to-know/',
 'https://huneducation.com/student-perspectives/', 'https://huneducation.com/about-us/',
 'https://huneducation.com/contact/',
 # --- TR editoryal (14) ---
 'https://tr.huneducation.com/', 'https://tr.huneducation.com/neden-macaristanda-egitim/',
 'https://tr.huneducation.com/macaristanda-universite-okumak/',
 'https://tr.huneducation.com/macaristan-universiteleri/', 'https://tr.huneducation.com/kurslar/',
 'https://tr.huneducation.com/macaristan-universite-basvuru-sartlari/',
 'https://tr.huneducation.com/macaristan-universite-fiyatlari/',
 'https://tr.huneducation.com/macaristan-yuksek-lisans/',
 'https://tr.huneducation.com/macaristanda-tip-egitimi-ve-macaristanda-tip-okumak/',
 'https://tr.huneducation.com/macaristan-universiteleri-pilotluk-egitimi/',
 'https://tr.huneducation.com/macaristanda-yasam-ve-universite-egitimi-bilinmesi-gerekenler/',
 'https://tr.huneducation.com/macaristan-universiteleri-ogrenci-gorusleri/',
 'https://tr.huneducation.com/hakkimizda/', 'https://tr.huneducation.com/iletisim/',
 # --- ornek program + universite (her iki dil) ---
 'https://huneducation.com/course/biology-bsc-pte/',
 'https://huneducation.com/course/pharmacy/',
 'https://huneducation.com/course/marketing-masters-2/',
 'https://tr.huneducation.com/course/mimarlik-pte/',
 'https://tr.huneducation.com/course/meteoroloji-yl-elte/',
 'https://huneducation.com/university/university-of-pecs/',
 'https://huneducation.com/university/semmelweis-university/',
 'https://tr.huneducation.com/university/szeged-universitesi-szte/',
 # --- sayfalama ---
 'https://huneducation.com/courses/2/',
 # --- sitemap / robots ---
 'https://huneducation.com/sitemap.xml', 'https://tr.huneducation.com/sitemap.xml',
 'https://huneducation.com/robots.txt', 'https://tr.huneducation.com/robots.txt',
]


def cek(u):
    try:
        r = urllib.request.Request(u, headers=H)
        with urllib.request.urlopen(r, timeout=40) as f:
            s = f.read(700000).decode('utf-8', 'replace')
            kod, basliklar = f.getcode(), dict(f.getheaders())
    except urllib.error.HTTPError as e:
        try: s = e.read(300000).decode('utf-8', 'replace')
        except Exception: s = ''
        kod, basliklar = e.code, {}
    except Exception as e:
        return {'url': u, 'hata': str(e)[:70]}
    if u.endswith('.xml') or u.endswith('.txt'):
        return {'url': u, 'kod': kod, 'loc': len(re.findall(r'<loc>', s)),
                'bayt': len(s), 'ozet': s[:200]}
    g = lambda p: (re.search(p, s, re.S | re.I).group(1).strip()
                   if re.search(p, s, re.S | re.I) else None)
    return {
        'url': u, 'kod': kod,
        'title': re.sub(r'\s+', ' ', g(r'<title[^>]*>(.*?)</title>') or ''),
        'desc': g(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)'),
        'canonical': g(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']*)'),
        'robots': g(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']*)'),
        'h1': [re.sub(r'<[^>]+>|\s+', ' ', x).strip()
               for x in re.findall(r'<h1[^>]*>(.*?)</h1>', s, re.S | re.I)],
        'og_title': g(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']*)'),
        'hreflang': len(re.findall(r'hreflang=', s, re.I)),
        'jsonld': len(re.findall(r'application/ld\+json', s, re.I)),
        'bayt': len(s),
    }


def al(cikti):
    # Barindirma 4 escamanli istekte 508 donuyor; tek tek ve araliklarla
    # cekilir. Yavas ama sunucuyu zorlamaz ve veri eksiksiz gelir.
    d = []
    for i, u in enumerate(URL):
        r = cek(u)
        if r.get('kod') == 508 or 'hata' in r:
            time.sleep(4); r = cek(u)          # bir kez daha dene
        d.append(r)
        if (i + 1) % 10 == 0:
            print('   %d/%d' % (i + 1, len(URL)), flush=True)
        time.sleep(1.2)
    io.open(cikti, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
    hata = [x for x in d if 'hata' in x or x.get('kod', 0) >= 400]
    print('%d URL yakalandi -> %s  (hatali: %d)' % (len(d), cikti, len(hata)))
    for x in hata[:5]:
        print('   !', x['url'], x.get('hata') or x.get('kod'))
    return d


if __name__ == '__main__':
    al(sys.argv[1] if len(sys.argv) > 1 else 'baseline.json')
