# -*- coding: utf-8 -*-
# Canlida yayinda olan son iki sayfa cifti.

# =====================================================================
# LIFE  ->  /university-education-and-life-in-hungary-what-you-need-to-know/
# =====================================================================
qa_life = [
    ("How much do I need each month to live on?",
     "<p>Around €480 to €1,000 a month depending on where you live and how. Accommodation is the swing "
     "factor: a dormitory place can be €60 while a studio flat is closer to €550. Groceries and bills "
     "run about €300, and a transport pass about €120.</p>"),
    ("What has to be done in the first month after arrival?",
     "<p>Residence registration, university enrolment, a bank account and a transport pass, in roughly "
     "that order. None of them is difficult on its own; the difficulty is that they have dependencies "
     "and deadlines, which is what our Budapest team is for.</p>"),
    ("Is a dormitory better than renting?",
     "<p>Cheaper, closer and more social; also limited in number and often shared. Places go early, so "
     "our advice is to apply for a dormitory and line up a rental as the fallback rather than "
     "choosing one and hoping.</p>"),
]

body_life = f'''<div class="alayout">
{toc([('accommodation','Where students live'),
      ('monthly','What a month costs'),('firstmonth','Your first month, step by step'),
      ('city','Life outside the campus'),('faq','Frequently asked questions'),('sources','Sources')])}

<article class="prose">

<section id="short-answer" class="answer">
  <span class="answer__label">Short answer</span>
  <p>Living in Hungary as a student costs roughly €480 to €1,000 a month, with accommodation the
  variable that moves it. The first month is administrative rather than academic: residence
  registration, enrolment, a bank account and a transport pass. English is enough for your degree and
  for daily life in the university cities; Hungarian helps everywhere else.</p>
</section>

<h2 id="accommodation">Where students live</h2>
{figure('szeged-yurt-binasi',
        'A student dormitory building in Szeged with people walking past',
        'A university dormitory. From €60 a month.',
        1280, 720)}
<div class="tablewrap">
<table class="dtable">
  <caption>Accommodation options compared</caption>
  <thead><tr><th>Option</th><th>Monthly</th><th>Suits</th><th>Watch for</th></tr></thead>
  <tbody>
    <tr><td><b>University dormitory</b></td><td class="num">€60 – €400</td><td>First year, tight budget</td><td>Limited places; apply as early as the offer allows</td></tr>
    <tr><td><b>Room in a shared flat</b></td><td class="num">≈ €350</td><td>Second year onward</td><td>Check whether bills are included</td></tr>
    <tr><td><b>Studio flat</b></td><td class="num">≈ €550</td><td>Couples, privacy</td><td>Deposit plus bills on top</td></tr>
  </tbody>
</table>
</div>
<p>The gap between the cheapest and the most expensive option is several thousand euros a year, which is
why the <a href="{S['costs']}">cost page</a> treats accommodation as the main budget variable rather
than a footnote.</p>

<h2 id="monthly">What a month costs</h2>
{figure('obuda-yemekhane',
        'The large, bright canteen at Óbuda University',
        'A campus canteen.')}
<div class="tablewrap">
<table class="dtable">
  <caption>Typical monthly outgoings</caption>
  <thead><tr><th>Item</th><th>Amount</th><th>Note</th></tr></thead>
  <tbody>
    <tr><td><b>Accommodation</b></td><td class="num">€60 – €550</td><td>The swing factor</td></tr>
    <tr><td><b>Groceries and bills</b></td><td class="num">≈ €300</td><td>Average student spend</td></tr>
    <tr><td><b>Transport pass</b></td><td class="num">€120</td><td>Student discounts vary by city</td></tr>
    <tr><td><b>Health insurance</b></td><td class="num">€25</td><td>≈ €300 a year, compulsory for enrolment</td></tr>
  </tbody>
</table>
</div>
<p>Cities differ. Budapest is the most expensive; Debrecen, Szeged, Pécs and Nyíregyháza run noticeably
lower on both rent and everyday costs.</p>

<h2 id="firstmonth">Your first month, step by step</h2>
{figure('metu-ogrenci-grubu',
        'A group of international students gathered in a campus garden',
        'International students on campus.')}
<ol class="steps">
  <li><div><h3>Arrival and accommodation</h3><p>Airport pick-up, keys, and the first shop. Our Budapest team handles this stretch because it is the part with no safety net.</p></div></li>
  <li><div><h3>Residence registration</h3><p>Completed after arrival within the period the permit allows. Requires the acceptance letter, proof of accommodation and insurance.</p></div></li>
  <li><div><h3>University enrolment</h3><p>Enrolment week, student card, course registration and the timetable.</p></div></li>
  <li><div><h3>Bank account and transport pass</h3><p>Straightforward once the residence card and student card exist, which is why they come fourth rather than first.</p></div></li>
</ol>

<h2 id="city">Life outside the campus</h2>
{strip('Scenes from student life in Hungary', [
 ('budapeste-balikci-tabyasi',
  'A view of Budapest at sunrise through an arch of the Fisherman’s Bastion',
  'The Fisherman’s Bastion, Budapest.'),
 ('budapeste-koprude-ogrenciler',
  'Two students on Liberty Bridge in Budapest',
  'Our students on Liberty Bridge.'),
 ('obuda-ogrenciler', 'A group of students on a bench under the Óbuda University sign',
  'Between classes.'),
 ('pecs-sehir-hava', 'An aerial view of the red rooftops of central Pécs',
  'Pécs: a walkable university city.'),
])}
<p>Hungary's university cities are compact and walkable, and student life concentrates around that.
Budapest has the density and the nightlife; Debrecen and Szeged have large campuses where the student
population sets the tone of the city; Pécs is small enough to cross on foot and has the country's oldest
university at its centre.</p>
<p>Public transport is good and cheap by European standards, and intercity rail makes weekend travel to
Vienna, Bratislava or Kraków realistic on a student budget.</p>

<h3>Getting by without Hungarian</h3>
<p>Your degree is in English, university administration handles international students in English, and
in the university cities you will manage day to day without Hungarian. Outside that, it thins out
quickly: expect Hungarian in local government offices, with landlords and in smaller shops.</p>
<p>Most universities offer beginner Hungarian free or cheaply. It is worth taking, less for fluency than
because it changes how the country responds to you.</p>

<h2 id="faq">Frequently asked questions</h2>
{faq_block(qa_life)}

<section id="sources" class="sources">
  <h2>Sources and verification</h2>
  <ol>
    <li>Living costs come from the real spending data of our students in Hungary and are re-verified each academic year.</li>
    <li>Residence and registration requirements are set by the Hungarian authorities and can change; their current rules are definitive.</li>
    <li>Dormitory availability and pricing are decided by each university.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Planning the practical side?", "Accommodation, arrival and the first month are where plans usually slip. Let us walk through your dates and put an order to it.")}

{related([(S['costs'],"Costs","Tuition and living costs","The full annual budget, item by item."),
          (S['stories'],"Students","Student perspectives","What students say about their own experience."),
          (S['edu'],"Guide","Study in Hungary","The system, the cities and the student visa.")])}
</article>
</div>'''

write(S['life'], page(
    S['life'],
    'University Life in Hungary: Housing, Costs, First Month | Hun Education',
    'Student life in Hungary: accommodation options and prices, what a month costs, the first-month '
    'administrative steps after arrival, and how far English gets you.',
    'Student life',
    'University education and life in Hungary',
    'What a month actually costs, where students live, and the administrative steps nobody warns you '
    'about in your first weeks.',
    body_life, S['life'],
    [HOME, ('Student life', url_of('life'))],
    qa_life))

# =====================================================================
# STUDENT PERSPECTIVES  ->  /student-perspectives/
# =====================================================================
qa_stories = [
    ("Are these reviews real?",
     "<p>Yes. Every comment on this page comes from a student whose application we handled, published "
     "with their permission. Surnames appear as initials at the students' own request. We do not use "
     "anonymous or invented testimonials, and we do not use stock photography to represent real "
     "students.</p>"),
    ("Can I speak to a current student before deciding?",
     "<p>Often, yes. Depending on the programme and the time of year we can put you in touch with a "
     "student on the course you are considering. Ask during your consultation.</p>"),
]

body_stories = f'''<div class="alayout">
{toc([('voices','In their own words'),
      ('themes','What comes up repeatedly'),('policy','How we handle testimonials'),
      ('faq','Frequently asked questions')])}

<article class="prose">

<section id="short-answer" class="answer">
  <span class="answer__label">Short answer</span>
  <p>The comments below are from students whose applications we handled, published with their
  permission and identified by first name and initial at their own request. They cover <a class="link" href="{S['medicine']}">medicine</a>, engineering, media and language studies across Budapest, Debrecen and Pécs.</p>
</section>

<h2 id="voices">In their own words</h2>
{strip('Scenes from our students', [
 ('metu-ogrenci-grubu', 'A group of international students gathered in a campus garden',
  'International students on campus.'),
 ('pilotaj-ogrenciler-pist', 'Three students in pilot shirts together at the airfield',
  'Our pilot students at the airfield.'),
 ('budapeste-koprude-ogrenciler', 'Two students on Liberty Bridge in Budapest',
  'A weekend in Budapest.'),
 ('metu-ogrenci-portre', 'A student in a campus corridor in front of a glass facade',
  'The Budapest Metropolitan campus.'),
])}
<div class="stories__row">
  <figure class="quote">
    <span class="quote__mark" aria-hidden="true">&rdquo;</span>
    <blockquote><p>The Hun Education advisers helped me enormously with every step. I graduated in Film
    and Media at Budapest Metropolitan University. After my studies and internship I worked with
    production companies including Disney, Marvel, Netflix and Paramount. I now work in Budapest, in the
    visual effects department of a major film production.</p></blockquote>
    <figcaption class="quote__who"><b>Baturay E.</b><span>Budapest Metropolitan University</span>
    <span class="num-mono">Media and Film</span></figcaption>
  </figure>

  <figure class="quote quote--accent">
    <span class="quote__mark" aria-hidden="true">&rdquo;</span>
    <blockquote><p>I started with Hun Education in the 2017–2018 academic year on the German-language
    pre-medical course at McDaniel College, then moved to Semmelweis University in September 2018. As of
    June 2022 I am about to finish my fourth year, and I feel lucky to be studying in Budapest at a
    university of this quality.</p></blockquote>
    <figcaption class="quote__who"><b>Işıl A.</b><span>Semmelweis University</span>
    <span class="num-mono">Medicine</span></figcaption>
  </figure>

  <figure class="quote">
    <span class="quote__mark" aria-hidden="true">&rdquo;</span>
    <blockquote><p>I came to Debrecen with Hun Education in September 2008. After finishing Electrical
    Engineering there I completed a master's in mechatronics and a PhD at Óbuda University, then worked
    at Óbuda as an academic. I am now working at Samsung in Hungary.</p></blockquote>
    <figcaption class="quote__who"><b>Sinan K.</b><span>University of Debrecen</span>
    <span class="num-mono">Electrical Engineering</span></figcaption>
  </figure>
</div>

<div class="tablewrap">
<table class="dtable">
  <caption>Further written accounts</caption>
  <thead><tr><th>Student</th><th>University</th><th>Programme</th></tr></thead>
  <tbody>
    <tr><td><b>Sude A.</b></td><td>University of Pécs</td><td>Preparatory year, then Medicine</td></tr>
    <tr><td><b>Özlem D.</b></td><td>University of Pécs</td><td>English Studies MA, now a PhD at Szeged and our Pécs representative</td></tr>
    <tr><td><b>Sude</b></td><td>University of Pécs</td><td>Nursing, first year</td></tr>
  </tbody>
</table>
</div>

<h2 id="themes">What comes up repeatedly</h2>
{figure('metu-derslik',
        'Students working at laptops in a lecture theatre',
        'Teaching is in English; the classes are international.')}
<p>Reading across the accounts, the same four things surface, and they are worth knowing because they
are what students actually found hard or good.</p>
<ul>
  <li><b>The first year is the heavy one.</b> In medicine especially, the basic-science years carry the
  examination load and the attrition.</li>
  <li><b>The administrative first month matters more than expected.</b> Residence registration and
  enrolment are the stretch where students say they were glad not to be alone.</li>
  <li><b>City choice shapes the experience as much as the university.</b> Budapest and Pécs produce
  noticeably different accounts of the same student year.</li>
  <li><b>Employment afterwards is real but not automatic.</b> The students who stayed in Hungary
  professionally are in international firms and English-working environments.</li>
</ul>

<h2 id="policy">How we handle testimonials</h2>
<p>Testimonial pages lose their credibility easily, so we set our rules out in the open.</p>
<ul>
  <li>Every comment comes from a student whose application we handled.</li>
  <li>Nothing is published without the student's permission, and permission can be withdrawn.</li>
  <li>Names appear as the student chooses, which is usually first name and initial.</li>
  <li>No stock photography is used to represent a real student. Where there is no photo, there is no photo.</li>
  <li>We publish no acceptance rate, success percentage or satisfaction score, because we cannot evidence one.</li>
</ul>

<h2 id="faq">Frequently asked questions</h2>
{faq_block(qa_stories)}

{acta("Want to hear it from a student?", "Depending on your programme we can often put you in touch with someone currently on the course. Ask in your consultation.")}

{related([(S['life'],"Student life","Life in Hungary","Accommodation, monthly costs and the first month."),
          (S['progs'],"Catalogue","Programme catalogue","Filter and compare 490 programmes."),
          (S['about'],"Company","About us","How we work, and what we do not promise.")])}
</article>
</div>'''

write(S['stories'], page(
    S['stories'],
    'Student Perspectives: Real Reviews from Students in Hungary | Hun Education',
    'Comments from students whose applications we handled, published with permission: medicine, '
    'engineering, media and language studies in Budapest, Debrecen and Pécs.',
    'Student perspectives',
    'Student perspectives',
    'Comments from students whose applications we handled, published with their permission and in their '
    'own words.',
    body_stories, S['stories'],
    [HOME, ('Student perspectives', url_of('stories'))],
    qa_stories))
