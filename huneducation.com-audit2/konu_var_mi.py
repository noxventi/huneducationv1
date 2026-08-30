# -*- coding: utf-8 -*-
import urllib.request, urllib.error, re, io, time, html, json

UA = {'User-Agent': 'Mozilla/5.0 (huneducation-konu-taramasi)'}
SAYFALAR = [
 ('macaristanda-universite-okumak', 'https://tr.huneducation.com/macaristanda-universite-okumak/'),
 ('macaristan-universite-fiyatlari', 'https://tr.huneducation.com/macaristan-universite-fiyatlari/'),
 ('macaristan-universite-basvuru-sartlari', 'https://tr.huneducation.com/macaristan-universite-basvuru-sartlari/'),
 ('macaristan-universiteleri', 'https://tr.huneducation.com/macaristan-universiteleri/'),
 ('neden-macaristanda-egitim', 'https://tr.huneducation.com/neden-macaristanda-egitim/'),
 ('macaristanda-yasam-ve-universite', 'https://tr.huneducation.com/macaristanda-yasam-ve-universite-egitimi-bilinmesi-gerekenler/'),
 ('macaristan-yuksek-lisans', 'https://tr.huneducation.com/macaristan-yuksek-lisans/'),
]
KONULAR = {
 'YÖK denkliği':      r'(YÖK|denklik|denkli)',
 'Ücret / fiyat':     r'(ücret|fiyat|euro|EUR|maliyet)',
 'Başvuru tarihleri': r'(başvuru dönem|başvuru tarih|son başvuru|takvim)',
 'Eğitim sistemi':    r'(eğitim sistemi|bologna|kredi sistemi|ECTS)',
 'Konaklama':         r'(konaklama|yurt|apart|kiralık|rezidans)',
 'Yaşam masrafı':     r'(yaşam masraf|geçim|aylık gider|yaşam mali)',
 'Çalışma izni':      r'(çalışma izni|part.?time|okurken çalış|haftada \d+ saat)',
 'Stipendium bursu':  r'(stipendium|burs)',
 'Vize / oturum':     r'(vize|oturum izni|ikamet)',
 'Popüler bölümler':  r'(popüler bölüm|en çok tercih|öne çıkan bölüm|tercih edilen)',
 'Sıralamalar':       r'(sıralama|ranking|QS|Times Higher)',
 'Eğitim dili/hazırlık': r'(hazırlık|İngilizce eğitim|dil şart|IELTS|TOEFL)',
 'Devlet/özel ayrımı':r'(devlet üniversite|özel üniversite|vakıf üniversite)',
 'SSS':               r'(sık sorulan|S\.S\.S|SSS)',
}

def al(u):
    r = urllib.request.Request(u, headers=UA)
    for _ in range(3):
        try:
            with urllib.request.urlopen(r, timeout=45) as f:
                return f.read().decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            if e.code in (503,508,429): time.sleep(20); continue
            return ''
        except Exception: time.sleep(6)
    return ''

metinler = {}
for ad, u in SAYFALAR:
    s = al(u)
    if not s:
        print('%-40s alinamadi' % ad, flush=True); continue
    g = re.sub(r'<(script|style|noscript|nav|footer|header)[^>]*>.*?</\1>', ' ', s, flags=re.S|re.I)
    g = re.sub(r'<[^>]+>', ' ', g)
    metinler[ad] = re.sub(r'\s+', ' ', html.unescape(g))
    print('%-40s %d kelime' % (ad, len(metinler[ad].split())), flush=True)
    time.sleep(2.5)

print()
print('%-22s %s' % ('KONU', 'HANGI SAYFADA (eslesme sayisi)'))
print('-'*76)
rapor = {}
for konu, desen in KONULAR.items():
    nerede = []
    for ad, t in metinler.items():
        n = len(re.findall(desen, t, re.I))
        if n >= 3:
            nerede.append('%s(%d)' % (ad[:26], n))
    rapor[konu] = nerede
    print('%-22s %s' % (konu, ', '.join(nerede) if nerede else '>>> HICBIR SAYFADA YOK'))
io.open('huneducation.com-audit2/konu_kapsami.json','w',encoding='utf-8').write(json.dumps(rapor, ensure_ascii=False, indent=1))
