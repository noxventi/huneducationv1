# -*- coding: utf-8 -*-
"""Program sayfalarına (tıp, pilotaj, yüksek lisans) iç bağlantı verir.

SORUN
  Bu altı sayfa (iki dilde üçer) gövdeden SIFIR iç bağlantı alıyordu;
  yalnızca header açılır menüsünden erişiliyorlardı. Sitenin en yüksek
  niyetli sayfaları bunlar: ilgili pillar sayfalardan bağlantı almazlarsa
  hem tarama önceliği hem konu otoritesi düşük kalır.

YÖNTEM
  Bağlantı, konudan bahseden cümlenin İÇİNE konur — ayrı bir "ilgili
  sayfalar" kutusuna değil. Bağlam içindeki bağlantı hem kullanıcı hem
  arama motoru için daha güçlü sinyaldir. Bağlantı metni hedef sayfanın
  anahtar kelimesidir, "buraya tıklayın" değil.
"""
import io, os, re

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (dosya, aranan, yerine)
EKLER = [
 # ---------------------------- TÜRKÇE ----------------------------
 ('tools/pages_content2.py',
  'yüksek lisans programları 2 yıl, tıp ve diş hekimliği gibi bütünleşik programlar ise 5–6 yıl sürer',
  '<a class="link" href="{S[\'masters\']}">yüksek lisans programları</a> 2 yıl, '
  '<a class="link" href="{S[\'medicine\']}">tıp</a> ve diş hekimliği gibi bütünleşik '
  'programlar ise 5–6 yıl sürer'),

 ('tools/pages_content.py',
  'yüksek lisansta 4.000 – 6.000 €, tıp ve diş hekimliğinde ise 15.800 € ile 19.900 $',
  '<a class="link" href="{S[\'masters\']}">yüksek lisansta</a> 4.000 – 6.000 €, '
  '<a class="link" href="{S[\'medicine\']}">tıp</a> ve diş hekimliğinde ise '
  '15.800 € ile 19.900 $'),

 ('tools/pages_content7.py',
  "Budapeşte, Debrecen ve Pécs'te tıp, mühendislik, medya ve dil bilimleri okuyan öğrencilerimizin",
  "Budapeşte, Debrecen ve Pécs'te <a class=\"link\" href=\"{S['medicine']}\">tıp</a>, "
  "mühendislik, medya ve dil bilimleri okuyan öğrencilerimizin"),

 # ---------------------------- İNGİLİZCE ----------------------------
 ('tools/en_content2.py',
  "master's programmes two years, and one-tier programmes such as medicine and dentistry five to six",
  "<a class=\"link\" href=\"{S['masters']}\">master's programmes</a> two years, and one-tier "
  "programmes such as <a class=\"link\" href=\"{S['medicine']}\">medicine</a> and dentistry "
  "five to six"),

 ('tools/en_content.py',
  "master's, and between €15,800 and $19,900 for medicine and dentistry",
  "<a class=\"link\" href=\"{S['masters']}\">master's</a>, and between €15,800 and $19,900 for "
  "<a class=\"link\" href=\"{S['medicine']}\">medicine</a> and dentistry"),

 ('tools/en_content7.py',
  'medicine, engineering, media and linguistics in Budapest, Debrecen and Pécs',
  '<a class="link" href="{S[\'medicine\']}">medicine</a>, engineering, media and linguistics '
  'in Budapest, Debrecen and Pécs'),
]

# Pilotaj sayfasi: anasayfadaki alan kartindan ve katalog cip seridinden
# zaten "?alan=pilot" filtresine gidiliyor. Ayrica maliyet sayfasindaki
# pilotaj satirindan da dogrudan baglanir.
EKLER += [
 ('tools/pages_content.py', 'Pilotaj eğitimi',
  '<a class="link" href="{S[\'pilot\']}">Pilotaj eğitimi</a>'),
 ('tools/en_content.py', 'Pilot training',
  '<a class="link" href="{S[\'pilot\']}">Pilot training</a>'),
]


def dene(yol, ara, koy):
    """Aranan cümle kaynakta satırlara bölünmüş olabilir; boşluklara
    duyarsız eşleşir. Düz `in` araması bu yüzden çalışmıyordu."""
    p = os.path.join(KOK, yol)
    s = io.open(p, encoding='utf-8').read()
    if koy in s:
        return 'zaten var'
    desen = r'\s+'.join(re.escape(k) for k in ara.split())
    m = re.search(desen, s)
    if not m:
        return '! bulunamadı'
    io.open(p, 'w', encoding='utf-8').write(s[:m.start()] + koy + s[m.end():])
    return 'eklendi'


if __name__ == '__main__':
    for yol, a, k in EKLER:
        print('  %-24s %-14s %s' % (yol.replace('tools/', ''), dene(yol, a, k), a[:44]))
