# -*- coding: utf-8 -*-
"""Kalan Ingilizce sayfalari Turkce karsiliklariyla ayni yapiya getirir.

Turkce tarafta bolum sayisi dusuruldu; ayni sayfanin Ingilizcesi eski
yapida kalirsa iki dil birbirinden ayrilir ve dil degistiren ziyaretci
farkli bir sayfa gormus olur. Burada yalnizca yapi degisiyor: hicbir
paragraf silinmiyor, birlestirilen bolumler h3 olarak yerinde kaliyor.
"""
import io, re, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def h2_h3(s, hid, baslik):
    yeni, n = re.subn(r'<h2 id="%s">.*?</h2>' % hid, '<h3>%s</h3>' % baslik,
                      s, count=1, flags=re.S)
    if not n:
        print('  ! bolum bulunamadi:', hid)
    return yeni


def h2_yenile(s, hid, baslik):
    yeni, n = re.subn(r'<h2 id="%s">.*?</h2>' % hid, '<h2 id="%s">%s</h2>' % (hid, baslik),
                      s, count=1, flags=re.S)
    if not n:
        print('  ! baslik bulunamadi:', hid)
    return yeni


def uygula(p, toc_eski, toc_yeni, indir, yenile=()):
    s = io.open(p, encoding='utf-8').read()
    if toc_eski in s:
        s = s.replace(toc_eski, toc_yeni, 1)
    else:
        print('  ! icindekiler eslesmedi:', p)
    for hid, baslik in indir:
        s = h2_h3(s, hid, baslik)
    for hid, baslik in yenile:
        s = h2_yenile(s, hid, baslik)
    io.open(p, 'w', encoding='utf-8').write(s)
    print('%-22s sadelestirildi' % p)


# ----------------------------------------------------------- why-hungary
uygula('tools/en_content5.py',
"""{toc([('short-answer','Short answer'),('numbers','Hungary in numbers'),
      ('cost','Around half the cost of Western Europe'),
      ('quality','A university tradition since 1367'),('turkey','A long-standing connection'),
      ('english','Taught entirely in English'),
      ('location','In the middle of Europe'),('life','What student life is like'),
      ('clarify','What we settle with you first'),
      ('faq','Frequently asked questions'),('sources','Sources')])}""",
"""{toc([('numbers','Hungary in numbers'),
      ('quality','What makes Hungary stand out'),
      ('cost','Tuition and living costs'),
      ('location','Student life in the middle of Europe'),
      ('clarify','What we settle with you first'),
      ('faq','Frequently asked questions'),('sources','Sources')])}""",
       indir=[('turkey', 'A long-standing connection'),
              ('english', 'Taught entirely in English'),
              ('life', 'What student life is like')],
       yenile=[('quality', 'What makes Hungary stand out'),
               ('cost', 'Tuition and living costs'),
               ('location', 'Student life in the middle of Europe')])

# --------------------------------------------------------------- masters
uygula('tools/en_content5.py',
"""{toc([('short-answer','Short answer'),('who','Who a Hungarian master’s suits'),""",
"""{toc([('who','Who a Hungarian master’s suits'),""",
       indir=[('fees', 'Fees and duration'),
              ('process', 'How the application runs')],
       yenile=[('fields', 'Fields, fees and duration'),
               ('requirements', 'Entry requirements and applying')])

# --------------------------------------------------------------- pillar
uygula('tools/en_content2.py',
"""{toc([('short-answer','Short answer'),('why','Why Hungary?'),('system','The system and degrees'),""",
"""{toc([('why','Why Hungary?'),('system','The system and degrees'),""",
       indir=[('language', 'Language of instruction'),
              ('recognition', 'Recognition and after graduation')],
       yenile=[('cities', 'Which city should you choose?'),
               ('visa', 'Visa, residence and recognition')])

# ------------------------------------------------------------- medicine
uygula('tools/en_content6.py',
"""{toc([('short-answer','Short answer'),('universities','Where medicine is taught'),""",
"""{toc([('universities','Where medicine is taught'),""",
       indir=[('foundation', 'If you are not ready yet'),
              ('after', 'After graduation')],
       yenile=[('exam', 'The entrance exam and preparation'),
               ('structure', 'How the six years run'),
               ('cost', 'Tuition fees')])

# ---------------------------------------------------------------- pilot
uygula('tools/en_content6.py',
"""{toc([('short-answer','Short answer'),('where','Where it is taught'),""",
"""{toc([('where','Where it is taught'),""",
       indir=[('structure', 'Ground school and flight training')],
       yenile=[('cost', 'Fees and what they cover'),
               ('requirements', 'What to arrange before you apply')])

# ----------------------------------------------------------------- life
uygula('tools/en_content7.py',
"""{toc([('short-answer','Short answer'),('accommodation','Where students live'),""",
"""{toc([('accommodation','Where students live'),""",
       indir=[('language', 'Getting by without Hungarian')])

# --------------------------------------------------------------- stories
uygula('tools/en_content7.py',
"""{toc([('short-answer','Short answer'),('voices','In their own words'),""",
"""{toc([('voices','In their own words'),""",
       indir=[])

# ---------------------------------------------------------- universities
uygula('tools/en_content2.py',
"""{toc([('short-answer','Short answer'),('list','University list'),('by-city','Distribution by city'),""",
"""{toc([('list','University list'),('by-city','Distribution by city'),""",
       indir=[])
