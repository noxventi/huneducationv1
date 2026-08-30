# -*- coding: utf-8 -*-
"""sadelestir.py'nin Ingilizce karsiligi: iki dil ayni yapida kalsin."""
import io, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sade_ortak import basvuru, maliyet

basvuru(
    'tools/en_content.py',
    """{toc([('short-answer','Short answer'),('documents','Required documents'),('language','English requirement'),
      ('eligibility','Are you eligible?'),
      ('exam','Entrance exams and interviews'),('calendar','Application calendar'),('process','The process step by step'),
      ('mistakes','Exceptions and common mistakes'),('faq','Frequently asked questions'),('sources','Sources')])}""",
    """{toc([('eligibility','Who can apply?'),('documents','Documents and English'),
      ('exam','Entrance exams and interviews'),('calendar','Calendar and process'),
      ('faq','Frequently asked questions'),('sources','Sources')])}""",
    {'uygunluk': 'eligibility', 'belgeler': 'documents', 'dil': 'language',
     'surec': 'process', 'istisna': 'mistakes'},
    {'dil': 'The English requirement', 'surec': 'The process step by step',
     'istisna': 'Common mistakes'},
)

maliyet(
    'tools/en_content.py',
    """{toc([('short-answer','Short answer'),('tuition','Tuition fees'),('by-university','By university'),
      ('living','Living costs'),('one-off','One-off fees'),('total','Annual total'),
      ('planning','How to build your budget'),('faq','Frequently asked questions'),('sources','Sources')])}""",
    """{toc([('tuition','Tuition fees'),('living','Living costs'),
      ('total','Your annual total'),
      ('faq','Frequently asked questions'),('sources','Sources')])}""",
    {'universite': 'by-university', 'tekseferlik': 'one-off', 'plan': 'planning'},
    {'universite': 'Differences between universities', 'tekseferlik': 'One-off fees',
     'plan': 'How we build your budget'},
)

# baslik metinleri icindekilerle ayni olsun
p = 'tools/en_content.py'
s = io.open(p, encoding='utf-8').read()
for a, b in [
    ('<h2 id="eligibility">Before the documents: are you eligible?</h2>',
     '<h2 id="eligibility">Who can apply?</h2>'),
    ('<h2 id="documents">Required documents</h2>',
     '<h2 id="documents">Documents and English</h2>'),
    ('<h2 id="calendar">Application calendar</h2>',
     '<h2 id="calendar">Calendar and process</h2>'),
    ('<h2 id="total">Annual total</h2>',
     '<h2 id="total">Your annual total</h2>'),
]:
    if a in s:
        s = s.replace(a, b)
    else:
        print('  ! baslik eslesmedi:', a[:60])
io.open(p, 'w', encoding='utf-8').write(s)
print('en basliklar hizalandi')
