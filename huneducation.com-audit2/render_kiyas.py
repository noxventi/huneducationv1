# -*- coding: utf-8 -*-
"""Tum sayfalari AYNI yontemle render edip olcer. Ham HTML ile render karisimi
kiyaslama yaniltici olurdu: JS ile icerik basan siteler ince gorunuyordu."""
import subprocess, json, io, os, time

SAYFALAR = [
 ('BIZ  macaristanda-universite-okumak', 'https://tr.huneducation.com/macaristanda-universite-okumak/'),
 ('BIZ  kurslar (katalog)',              'https://tr.huneducation.com/kurslar/'),
 ('BIZ  macaristan-universiteleri',      'https://tr.huneducation.com/macaristan-universiteleri/'),
 ('elt.com.tr',              'https://www.elt.com.tr/macaristanda-universite-egitim'),
 ('macaristandauniversite',  'https://www.macaristandauniversite.com/'),
 ('gedu.com.tr',             'https://gedu.com.tr/macaristan-universiteleri/'),
 ('iecc.com.tr',             'https://www.iecc.com.tr/macaristan-universite-egitimi'),
 ('unioku.com',              'https://unioku.com/macaristanda-universite'),
 ('icesturkey.com',          'https://www.icesturkey.com/macaristan-universiteleri'),
 ('academix.com.tr',         'https://www.academix.com.tr/yurtdisinda-universite/macaristanda-universite'),
 ('deltaegitim.com.tr',      'https://www.deltaegitim.com.tr/macaristanda-universite-okumak/'),
]
RUNNER = os.path.expanduser('~/.claude/skills/seo/bin/claude-seo')

out = []
for ad, u in SAYFALAR:
    try:
        p = subprocess.run([RUNNER, 'run', 'render_page.py', u, '--mode', 'always', '--json'],
                           capture_output=True, timeout=180)
        d = json.loads(p.stdout.decode('utf-8', 'replace'))
        t = d.get('text') or d.get('content') or ''
        kelime = len(t.split())
        out.append({'ad': ad, 'url': u, 'render_kelime': kelime})
        print('%-38s %6d kelime' % (ad, kelime), flush=True)
    except Exception as e:
        out.append({'ad': ad, 'url': u, 'render_kelime': None, 'hata': str(e)[:60]})
        print('%-38s HATA %s' % (ad, str(e)[:40]), flush=True)
    time.sleep(3)

io.open('huneducation.com-audit2/render_kiyas.json', 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
print('\nyazildi')
