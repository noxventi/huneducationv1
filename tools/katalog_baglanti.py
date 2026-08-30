# -*- coding: utf-8 -*-
"""Katalog kayıtlarına canlıdaki program ve üniversite slug'larını ekler.

NEDEN
  Yeni katalog sayfası kartları hiçbir yere link vermiyordu. Canlıdaki
  498 EN + 486 TR program ve 20+20 üniversite sayfası, tasarım geçtiği
  anda iç bağlantısız kalacaktı. Katalog bu sayfaların doğal hub'ı.

EŞLEŞTİRME
  1. Program adı canlı başlıkla normalize edilip eşlenir (EN %100).
  2. Türkçe slug önce doğrudan başlıkla, bulunamazsa WPML çeviri
     haritasından (en_id -> tr_slug) alınır.
  3. Hiçbiri tutmazsa program slug'sız kalır; kart o dilde üniversite
     sayfasına düşer. Yanlış sayfaya link vermektense link vermemek.
"""
import io, json, re, unicodedata, os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = ('C:/Users/Burak/AppData/Local/Temp/claude/'
     'C--Users-Burak-Desktop-huneducation/3afbd448-6373-44f8-a61f-d3d8f90a2ebd/scratchpad/')
KAT = os.path.join(KOK, 'site', 'assets', 'data', 'catalog.js')


def norm(t):
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c)).lower()
    t = t.replace('–', '-').replace('—', '-').replace('’', "'")
    t = re.sub(r'\(.*?\)', ' ', t)
    t = re.sub(r'[^a-z0-9]+', ' ', t)
    return ' '.join(t.split())


def calis():
    canli = json.load(io.open(D + 'canli_kayitlar.json', encoding='utf-8'))
    ceviri = json.load(io.open(D + 'ceviri_haritasi.json', encoding='utf-8'))
    kat = io.open(KAT, encoding='utf-8').read()

    en_slug = {norm(x['ad']): x['slug'] for x in canli['course_en']}
    en_id = {norm(x['ad']): x['id'] for x in canli['course_en']}
    tr_slug = {norm(x['ad']): x['slug'] for x in canli['course_tr']}
    id_tr = {int(c['en_id']): c['tr_slug'] for c in ceviri['course']}

    uni_en = {norm(x['ad']): x['slug'] for x in canli['university_en']}
    uni_tr = {norm(x['ad']): x['slug'] for x in canli['university_tr']}
    uid_tr = {c['en_slug']: c['tr_slug'] for c in ceviri['university']}

    # ---- üniversiteler ----
    sayac = {'uni_en': 0, 'uni_tr': 0, 'p_en': 0, 'p_tr': 0, 'p_yok': 0}

    def uni_ekle(m):
        gov, aden, adtr = m.group(0), m.group(3), m.group(4)
        if "sen:" in gov:
            return gov
        se = uni_en.get(norm(aden))
        if not se:
            ilk = norm(aden).split()[0]
            se = next((v for k, v in uni_en.items() if len(ilk) > 4 and ilk in k), None)
        st = uni_tr.get(norm(adtr)) or (uid_tr.get(se) if se else None)
        ek = ''
        if se:
            sayac['uni_en'] += 1; ek += ", sen: '%s'" % se
        if st:
            sayac['uni_tr'] += 1; ek += ", str: '%s'" % st
        return gov.rstrip('}').rstrip() + ek + ' }' if ek else gov

    kat = re.sub(r"\{ id: (\d+), kod: '([^']+)', ad: L\('([^']*)', '([^']*)'\)[^}]*\}",
                 uni_ekle, kat)

    # ---- programlar ----
    def prog_ekle(m):
        gov, aden, adtr = m.group(0), m.group(1), m.group(2)
        if "pen:" in gov:
            return gov
        se = en_slug.get(norm(aden))
        st = tr_slug.get(norm(adtr))
        if not st and se:
            st = id_tr.get(en_id.get(norm(aden)))
        ek = ''
        if se:
            sayac['p_en'] += 1; ek += ", pen: '%s'" % se
        if st:
            sayac['p_tr'] += 1; ek += ", ptr: '%s'" % st
        if not ek:
            sayac['p_yok'] += 1
            return gov
        return gov.rstrip('}').rstrip() + ek + ' }'

    kat = re.sub(r"\{ ad: L\('([^']*)', '([^']*)'\), uni: \d+[^}]*\}", prog_ekle, kat)

    io.open(KAT, 'w', encoding='utf-8').write(kat)
    print('üniversite slug: en=%d tr=%d' % (sayac['uni_en'], sayac['uni_tr']))
    print('program slug   : en=%d tr=%d, eşleşmeyen=%d'
          % (sayac['p_en'], sayac['p_tr'], sayac['p_yok']))


if __name__ == '__main__':
    calis()
