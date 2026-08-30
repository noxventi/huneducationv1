# -*- coding: utf-8 -*-
import urllib.request, urllib.error, re, io, time, html, random, json
UA={'User-Agent':'Mozilla/5.0 (huneducation-desc-kontrol)'}
def al(u):
    r=urllib.request.Request(u,headers=UA)
    for _ in range(3):
        try:
            with urllib.request.urlopen(r,timeout=40) as f: return f.read().decode('utf-8','replace')
        except urllib.error.HTTPError as e:
            if e.code in (503,508,429): time.sleep(18); continue
            return ''
        except Exception: time.sleep(6)
    return ''
random.seed(11)
ozet={}
for host in ('huneducation.com','tr.huneducation.com'):
    urls=[]
    for f in ('course','university'):
        s=al('https://%s/%s-sitemap.xml'%(host,f))
        locs=re.findall(r'<loc>([^<]+)</loc>',s)
        urls += random.sample(locs, min(14 if f=='course' else 6, len(locs)))
        time.sleep(1)
    var=0; yok=0; uzun=[]
    for u in urls:
        s=al(u)
        if not s: continue
        m=re.search(r'<meta name="description" content="([^"]*)"',s)
        d=html.unescape(m.group(1)) if m else ''
        if d.strip(): var+=1; uzun.append(len(d))
        else: yok+=1; print('   ACIKLAMASIZ:',u,flush=True)
        time.sleep(1.2)
    ozet[host]={'olculen':var+yok,'aciklamasi_var':var,'yok':yok,
                'ort_uzunluk':round(sum(uzun)/len(uzun)) if uzun else 0,
                'min':min(uzun) if uzun else 0,'max':max(uzun) if uzun else 0}
    print('%-24s %d/%d sayfada aciklama var | ort %d karakter (%d-%d)' % (
        host, var, var+yok, ozet[host]['ort_uzunluk'], ozet[host]['min'], ozet[host]['max']), flush=True)
io.open('huneducation.com-audit2/desc_kontrol.json','w',encoding='utf-8').write(json.dumps(ozet,ensure_ascii=False,indent=1))
