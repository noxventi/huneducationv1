# -*- coding: utf-8 -*-
"""Iki anlik goruntuyu karsilastirir. Amac: hangi siralama sinyalinin
istemeden degistigini gormek. Baslik/canonical/H1 degisimi = RISK,
sema/hreflang/OG eklenmesi = KAZANC."""
import io, json, sys, html

a = json.load(io.open(sys.argv[1], encoding='utf-8'))
b = json.load(io.open(sys.argv[2], encoding='utf-8'))
ha = {x['url']: x for x in a}
hb = {x['url']: x for x in b}

RISK = ['title', 'canonical', 'h1']
KAZANC = ['desc', 'og_title', 'hreflang', 'jsonld', 'robots', 'loc']

risk, kazanc = [], []
for u in ha:
    if u not in hb: continue
    x, y = ha[u], hb[u]
    for k in RISK:
        if x.get(k) != y.get(k):
            risk.append((u, k, x.get(k), y.get(k)))
    for k in KAZANC:
        if x.get(k) != y.get(k):
            kazanc.append((u, k, x.get(k), y.get(k)))

print('=' * 74)
print('RISK: istemeden degisen siralama sinyalleri')
print('=' * 74)
if not risk:
    print('  YOK — hicbir baslik, canonical veya H1 degismedi.')
for u, k, o, n in risk[:25]:
    print('  %s' % u.replace('https://', ''))
    print('    %-10s once : %s' % (k, html.unescape(str(o))[:88]))
    print('    %-10s sonra: %s' % ('', html.unescape(str(n))[:88]))
print('  toplam degisen: %d' % len(risk))

print()
print('=' * 74)
print('KAZANC: eklenen sinyaller')
print('=' * 74)
ozet = {}
for u, k, o, n in kazanc:
    ozet.setdefault(k, []).append((u, o, n))
for k, v in ozet.items():
    print('  %-10s %d URL degisti' % (k, len(v)))
    for u, o, n in v[:3]:
        print('      %-46s %s -> %s' % (u.replace('https://','')[:46],
                                        str(o)[:26], str(n)[:34]))
