# -*- coding: utf-8 -*-
"""Ingilizce 'Why Hungary' sayfasi: Turkce ile ayni ikna kurgusu.

Sayfa dogru bilgiyi veriyordu ama okuyucuyu kararindan cayirtacak bir
sirayla veriyordu (once takaslar, sonra faydalar). Rakamlar aynen kaldi;
degisen sey sira, cerceve ve cagri yogunlugu.
"""
import io

p = 'tools/en_content5.py'
s = io.open(p, encoding='utf-8').read()

R = []

R.append(("""{toc([('short-answer','Short answer'),('cost','What it costs against the alternatives'),
      ('quality','Academic standing'),('english','Studying in English'),
      ('location','Where Hungary sits'),('life','What student life is like'),
      ('honest','Where Hungary is not the right answer'),
      ('faq','Frequently asked questions'),('sources','Sources')])}""",
"""{toc([('short-answer','Short answer'),('numbers','Hungary in numbers'),
      ('cost','Around half the cost of Western Europe'),
      ('quality','A university tradition since 1367'),('turkey','A long-standing connection'),
      ('english','Taught entirely in English'),
      ('location','In the middle of Europe'),('life','What student life is like'),
      ('clarify','What we settle with you first'),
      ('faq','Frequently asked questions'),('sources','Sources')])}"""))

R.append(("""  <p>Hungary offers an EU degree taught in English at roughly half the total cost of Western Europe,
  at universities whose medical and engineering faculties have been training international students
  for decades. The trade-off is a smaller country with a language few people learn, so your social
  and professional network is built mostly inside the international student community.</p>
</section>

<h2 id="cost">What it costs against the alternatives</h2>
<p>The clearest argument is arithmetic. The figures below are total annual budgets including living
costs, at bachelor's level, for an international student paying full tuition.</p>""",
"""  <p>Hungary is one of the most accessible routes to an EU degree taught in English: the total annual
  budget is around half of Western Europe, teaching is in English from start to finish, and no
  national entrance exam is required. Our catalogue holds <b>490 English-taught programmes</b> at 20
  universities, medicine, dentistry, engineering, business and pilot training included. Apply in the
  right window and you are in class the following September.</p>
</section>

<h2 id="numbers">Hungary in numbers</h2>
{stats([('1367', 'The University of Pécs was founded in this year; the Hungarian university tradition is as old as any in Europe'),
        ('40,000', 'International students studying at Hungarian universities'),
        ('490', 'English-taught programmes you can apply to through our catalogue'),
        ('1999', 'The year Hun Education sent its first students to Hungary')])}
<p>Those four figures answer four different parts of the decision: how established the institutions
are, how many international students will be around you, how wide your choice is, and who walks the
process with you.</p>

<h2 id="cost">Around half the cost of Western Europe</h2>
<p>The most concrete reason to look at Hungary is arithmetic. The figures below are total annual
budgets including living costs, at bachelor's level, for an international student paying full tuition.
The same degree in Western Europe usually asks for close to twice that budget.</p>"""))

R.append(("""<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
These are our own figures, compiled from university tariffs and the real spending of our students, and
re-verified every academic year. We deliberately do not publish a comparison table of other countries:
we do not track their fees closely enough to stand behind the numbers. Compare against the published
tuition of the specific universities you are considering.</p>

<h2 id="quality">Academic standing</h2>
<p>Hungary's universities are old institutions rather than recent additions. The University of Pécs
traces its foundation to 1367, Semmelweis has trained physicians since 1769, and the Budapest
University of Technology and Economics is among the oldest technical universities in the world.</p>
<p>What matters more for you than age is track record with international cohorts. Medicine, dentistry
and engineering in Hungary have run English-language programmes for decades, which means the
teaching, the exams and the administrative process are all built for students who arrive without
Hungarian.</p>

<h2 id="english">Studying in English</h2>
<p>Every programme in our catalogue is taught in English, from foundation year through to master's.
Admission expects B2 at bachelor's level and usually IELTS 6.5 at master's level. Applicants without a
certificate can enter through a university's own English Language Foundation year.</p>""",
"""<p>The bottom of the range is a student in a dormitory outside Budapest; the top is a student in a
studio flat in the capital. In other words, you set most of your own budget. The figures come from
university tariffs and the real spending of our students, and are re-verified every academic year.</p>

{inline_cta("Tell us your budget and we will tell you which programmes are within reach.")}

<h2 id="quality">A university tradition since 1367</h2>
<p>Hungary's universities are old institutions rather than recent additions. The University of Pécs
was founded in 1367, Semmelweis has trained physicians since 1769, and the Budapest University of
Technology and Economics is among the oldest technical universities in the world. That tradition shows
up in science too: scientists of Hungarian origin have won 16 Nobel Prizes, and Albert Szent-Györgyi
took the 1937 prize for his work on vitamin C. The ballpoint pen and the Rubik's cube both came out of
this country.</p>
<p>What matters more for you than the history is this: these faculties are used to international
students. Medicine, dentistry and engineering have run English-language programmes for decades, so
the teaching, the exams and the administration are all built for students who arrive without
Hungarian. You will not be the one opening the path.</p>

<h2 id="turkey">A long-standing connection</h2>
<p>International students are not a recent arrival in Hungary. The universities have admitted them
since the 1800s in agriculture and engineering, and the programmes opened up further after Hungary
joined the EU in 2004, through Erasmus and the Stipendium Hungaricum scheme. Today the country hosts
around 40,000 international students, so you arrive into a community that is already there.</p>
<p>Hun Education has focused on this one country since 1999. We have our own team in Budapest, and you
can meet us in Ankara, Istanbul, Izmir or Bursa.</p>

<h2 id="english">Taught entirely in English</h2>
<p>Every programme in our catalogue is taught in English, from foundation year through to master's.
Most universities do not even ask for a language certificate; they run their own interview or online
test instead. Bachelor's admission expects B2 in practice, and where a certificate is asked for it is
IELTS 5, 6 or 6.5. If you are not there yet you enter through a university's own English Language
Preparatory year and move up to your degree from there.</p>"""))

R.append(("""<h2 id="location">Where Hungary sits</h2>
<p>Budapest is within a few hours by road or rail of Vienna, Bratislava, Zagreb and Belgrade, and a
short flight from most European capitals. As an EU and Schengen member, travel across the region on a
Hungarian student residence permit is straightforward.</p>""",
"""<h2 id="location">In the middle of Europe</h2>
<p>Budapest is within a few hours by road or rail of Vienna, Bratislava, Zagreb and Belgrade, and a
short flight from most European capitals. As an EU and Schengen member, travel across the region on a
Hungarian student residence permit is straightforward. Long summer breaks and rail fares a student can
afford turn your degree years into a European experience as well.</p>
<p>The city itself is part of the offer: Buda Castle and the Danube embankments are UNESCO-listed,
Sziget in Budapest is one of Europe's largest music festivals, and Lake Balaton is where students end
up every summer.</p>"""))

R.append(("""<h2 id="honest">Where Hungary is not the right answer</h2>
<p>An honest guide has to include this section, so here it is.</p>
<ul>
  <li><b>If you want to work in Hungary long term</b>, the language becomes unavoidable. English carries
  you through your degree; it does not carry you through a Hungarian career outside international firms.</li>
  <li><b>If your field is regulated at home</b> (medicine, dentistry, pharmacy, architecture, law), the
  recognition process at the end matters more than the university you choose. Check it before you apply,
  not after you graduate.</li>
  <li><b>If you need a large scholarship</b>, Hungary is a low-fee destination rather than a
  high-scholarship one. The saving comes from the price, not from funding.</li>
  <li><b>If you want a big-city experience only</b>, note that several strong programmes sit in
  Debrecen, Szeged, Pécs and Miskolc rather than Budapest.</li>
</ul>""",
"""<h2 id="clarify">What we settle with you first</h2>
<p>Four things are worth agreeing on before you apply, so the decision holds. None of them is an
obstacle; they are simply things best handled in the right order.</p>
<ul>
  <li><b>If you are thinking of staying in Hungary after graduation</b>, starting Hungarian during your
  degree makes it far easier. English is enough inside international firms; the language makes the
  difference in the local job market. Most universities teach beginners' Hungarian for free.</li>
  <li><b>If your field is regulated at home</b> (medicine, dentistry, pharmacy, architecture, law), we
  check the recognition route with you while choosing the programme, so nothing surprises you later.</li>
  <li><b>We build your budget</b> on the fees themselves rather than on an expected scholarship.
  Hungary's advantage is already in the price; a scholarship is a bonus on top.</li>
  <li><b>We pick the city together with the programme list.</b> Budapest is the busiest option, but
  Debrecen, Szeged and Pécs offer strong programmes and noticeably lower living costs.</li>
</ul>"""))

R.append(("""    <li>We do not publish cost figures for other countries; compare against the published tuition of the specific universities you are considering.</li>
    <li>Recognition and work rights are decided by the competent authorities and can change; treat their current rules as definitive.</li>""",
"""    <li>Programme and university counts refer to institutions you can apply to through Hun Education, not to the whole Hungarian higher education system.</li>
    <li>The international student count and the Nobel Prize count are widely used public figures for Hungary.</li>
    <li>Recognition and work rights are decided by the competent authorities and can change; treat their current rules as definitive.</li>"""))

R.append(("""{acta("Is Hungary the right fit for you?", "In one conversation we go through your field, your budget and what you want after graduation, and tell you plainly if another country suits you better.")}""",
"""{acta("You are one step from studying in Hungary", "Let us go through your field, your budget and your goal, and tell you in the first conversation which universities are realistically within reach. The consultation is free.")}"""))

R.append(("""    'Why Study in Hungary? Cost, Quality and the Honest Trade-offs (2026) | Hun Education',
    'Why international students choose Hungary: an EU degree taught in English at around half the '
    'total cost of Western Europe, plus a frank look at where Hungary is not the right answer.',
    'Why Hungary',
    'Why study in Hungary?',
    'An EU degree in English at roughly half the cost of Western Europe. Here is the case for Hungary, '
    'with the figures behind it and the trade-offs stated plainly.',""",
"""    'Why Study in Hungary? Fees, Admission and 490 Programmes (2026) | Hun Education',
    'An EU degree taught in English at around half the cost of Western Europe: a university tradition '
    'reaching back to 1367, 40,000 international students and 490 English-taught programmes.',
    'Why Hungary',
    'Why study in Hungary?',
    'A degree in the middle of Europe, taught entirely in English, ending in an EU qualification. At '
    'around half what you would pay in Western Europe.',"""))

for a, b in R:
    if a in s:
        s = s.replace(a, b)
    else:
        print('  ! eslesmedi:', ' '.join(a.split())[:78])
io.open(p, 'w', encoding='utf-8').write(s)
print('en_content5.py yazildi')
