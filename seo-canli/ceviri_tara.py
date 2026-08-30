# -*- coding: utf-8 -*-
"""TR sayfalarindaki gorunen metni yakalar; oncesi/sonrasi karsilastirmasi icin."""
import io, os, re, sys, json, time, html
import urllib.request

URL = [
 'https://tr.huneducation.com/',
 'https://tr.huneducation.com/kurslar/',
 'https://tr.huneducation.com/macaristan-universite-fiyatlari/',
 'https://tr.huneducation.com/macaristan-universite-basvuru-sartlari/',
 'https://tr.huneducation.com/hakkimizda/',
 'https://tr.huneducation.com/iletisim/',
 'https://tr.huneducation.com/macaristan-universiteleri/',
 'https://tr.huneducation.com/macaristanda-tip-egitimi-ve-macaristanda-tip-okumak/',
 'https://tr.huneducation.com/macaristan-universiteleri-pilotluk-egitimi/',
 'https://tr.huneducation.com/neden-macaristanda-egitim/',
 'https://tr.huneducation.com/course-city/budapest/',
 'https://tr.huneducation.com/course-category/muhendislik-mimarlik/',
 'https://tr.huneducation.com/course-level/lisans-babsc/',
 'https://tr.huneducation.com/kurs/spor-koclugu-hibrid-ma-tf/',
 'https://tr.huneducation.com/kurs/uluslararasi-spor-diplomasisi-hibrid-ma-tf/',
 'https://tr.huneducation.com/universite/szeged-universitesi-szte/',
 'https://tr.huneducation.com/universite/macaristan-spor-bilimleri-universitesi/',
]

def cek(u):
    r = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (huneducation-ceviri-denetimi)'})
    for _ in range(3):
        try:
            with urllib.request.urlopen(r, timeout=45) as f:
                return f.read().decode('utf-8', 'replace')
        except Exception:
            time.sleep(3)
    return ''

def gorunur(s):
    s = re.sub(r'<(script|style|noscript)[^>]*>.*?</\1>', ' ', s, flags=re.S | re.I)
    # buton / baglanti / baslik metinleri ayri toplanir
    ogeler = []
    for etiket in ('a', 'button', 'h1', 'h2', 'h3', 'h4', 'label', 'span', 'p', 'li'):
        for m in re.findall(r'<%s\b[^>]*>(.*?)</%s>' % (etiket, etiket), s, re.S | re.I):
            t = html.unescape(re.sub(r'<[^>]+>', ' ', m))
            t = re.sub(r'\s+', ' ', t).strip()
            if 2 <= len(t) <= 90:
                ogeler.append((etiket, t))
    # input degerleri / placeholder
    for m in re.findall(r'(?:value|placeholder|aria-label)="([^"]{2,90})"', s):
        ogeler.append(('attr', html.unescape(m).strip()))
    return ogeler

# Turkce'ye ozgu harf ya da yaygin Turkce kelime iceriyorsa Turkce say
TR_HARF = set('çğıöşüÇĞİÖŞÜ')
TR_KELIME = re.compile(r'\b(ve|ile|için|bir|bu|daha|olarak|üniversite|program|bölüm|başvuru|tüm|hakkında|iletişim|ana sayfa|devam|gönder|ara)\b', re.I)
# Ingilizce'ye ozgu isaretler
EN_KELIME = re.compile(r'\b(the|and|for|with|your|our|more|all|read|learn|submit|send|search|apply|about|contact|home|next|previous|show|view|click|here|free|now|get|see|find|choose|select|please|required|name|email|message|phone|country|city|price|year|semester|level|category|university|course|program|program(me)?s?)\b', re.I)

def ingilizce_mi(t):
    if any(c in TR_HARF for c in t):
        return False
    if TR_KELIME.search(t):
        return False
    if not EN_KELIME.search(t):
        return False
    # en az iki kelime, ya da bilinen tek kelimelik buton
    return len(t.split()) >= 1

def main(cikti):
    d = {}
    for u in URL:
        s = cek(u)
        if not s:
            d[u] = {'hata': True}
            continue
        og = gorunur(s)
        ing = sorted({t for _, t in og if ingilizce_mi(t)})
        d[u] = {'oge': len(og), 'ingilizce': ing}
        print('%-70s oge=%4d  ingilizce=%3d' % (u.replace('https://tr.huneducation.com', ''), len(og), len(ing)))
        time.sleep(1.2)
    io.open(cikti, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
    top = sorted({x for v in d.values() for x in v.get('ingilizce', [])})
    print('\nBENZERSIZ INGILIZCE DIZE: %d' % len(top))
    return top

if __name__ == '__main__':
    t = main(sys.argv[1] if len(sys.argv) > 1 else 'ceviri/oncesi.json')
    for x in t[:60]:
        print('  ', x)
