# -*- coding: utf-8 -*-
"""Program kataloğu sayfalarına (courses / kurslar) görsel şeridi ekler.

Katalog elle bakılan bir sayfa; jeneratörden geçmiyor. Şerit filtrelerin
üstüne, sayfanın girişine konur: öğrenci filtrelemeye başlamadan önce
programların okutulduğu kampüsleri görür.
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

TRLI = [
 ('elte-tarihi-bina', 'ELTE’nin tarihi taş cepheli binası', 'ELTE, Budapeşte.'),
 ('debrecen-cam-bina', 'Debrecen Üniversitesi’nin cam cepheli modern binası',
  'Debrecen Üniversitesi.'),
 ('szeged-ana-bina', 'Szeged Üniversitesi’nin sarı cepheli ana binası', 'Szeged Üniversitesi.'),
 ('pecs-universitesi-tabela',
  'Pécs Üniversitesi binası; girişte “University of Pécs” tabelası', 'Pécs Üniversitesi.'),
 ('obuda-sari-bina', 'Óbuda Üniversitesi’nin sarı cepheli tarihi binası', 'Óbuda Üniversitesi.'),
 ('metu-bina-tabela', '“Budapesti Metropolitan Egyetem” yazılı yuvarlak kampüs binası',
  'Budapeşte Metropolitan.'),
 ('corvinus-bina', 'Corvinus Üniversitesi’nin modern cam ve taş cepheli binası',
  'Corvinus Üniversitesi.'),
 ('miskolc-cam-bina', 'Miskolc Üniversitesi’nin cam cepheli binası ve önündeki meydan',
  'Miskolc Üniversitesi.'),
]
ENLI = [
 ('elte-tarihi-bina', 'The historic stone facade of ELTE', 'ELTE, Budapest.'),
 ('debrecen-cam-bina', 'A glass-fronted modern building at the University of Debrecen',
  'University of Debrecen.'),
 ('szeged-ana-bina', 'The yellow facade of the University of Szeged main building',
  'University of Szeged.'),
 ('pecs-universitesi-tabela',
  'A University of Pécs building with the “University of Pécs” sign at the entrance',
  'University of Pécs.'),
 ('obuda-sari-bina', 'The yellow historic building of Óbuda University', 'Óbuda University.'),
 ('metu-bina-tabela', 'The round campus building signed “Budapesti Metropolitan Egyetem”',
  'Budapest Metropolitan.'),
 ('corvinus-bina', 'The modern glass and stone facade of Corvinus University',
  'Corvinus University.'),
 ('miskolc-cam-bina', 'The glass-fronted building and forecourt at the University of Miskolc',
  'University of Miskolc.'),
]

ISLER = [
    ('site/courses.html', '', ENLI, 'Campuses where these programmes are taught'),
    ('site/tr/kurslar.html', '../', TRLI, 'Programların okutulduğu kampüsler'),
]


def serit(onek, ogeler, etiket):
    import gorsel_ogeler
    gorsel_ogeler.A = onek
    return gorsel_ogeler.strip(etiket, ogeler)


for yol, onek, ogeler, etiket in ISLER:
    s = io.open(yol, encoding='utf-8').read()
    if 'class="strip"' in s:
        print('  zaten var:', yol); continue
    imza = '  </div>\n</section>\n\n<section class="cat">'
    if imza not in s:
        print('  ! kanca bulunamadı:', yol); continue
    blok = serit(onek, ogeler, etiket)
    blok = '\n'.join('    ' + r if r.strip() else r for r in blok.split('\n'))
    s = s.replace(imza, '\n' + blok + '\n' + imza, 1)
    io.open(yol, 'w', encoding='utf-8').write(s)
    print('  şerit eklendi:', yol)
