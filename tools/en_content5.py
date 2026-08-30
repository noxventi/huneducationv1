# -*- coding: utf-8 -*-
# Canlida yayinda olup yeni tasarimda karsiligi olmayan sayfalar (1/2).
# Slug'lar canlidan alinmistir, degistirilmez.

# =====================================================================
# WHY HUNGARY  ->  /why-hungary/
# =====================================================================
qa_why = [
    ("Is a Hungarian degree recognised across Europe?",
     "<p>Hungary is an EU member state and part of the European Higher Education Area, so degrees "
     "follow the Bologna structure and carry ECTS credits. What that guarantees is comparability, not "
     "automatic recognition: using the degree in a regulated profession still goes through the "
     "competent authority in the country where you want to practise.</p>"),
    ("Why is Hungary cheaper than Western Europe?",
     "<p>Two things stack up. Tuition at Hungarian universities is set lower than in Western Europe for "
     "comparable programmes, and the cost of living outside Budapest is markedly lower again. Together "
     "they put a full academic year in the €8,500 to €14,000 band rather than double that.</p>"),
    ("Do I need to speak Hungarian?",
     "<p>Not to study. International programmes run entirely in English and admission does not test "
     "Hungarian. It helps in daily life and for part-time work, and most universities offer beginner "
     "classes free or at low cost.</p>"),
]

body_why = f'''<div class="alayout">
{toc([('numbers','Hungary in numbers'),
      ('quality','What makes Hungary stand out'),
      ('cost','Tuition and living costs'),
      ('location','Student life in the middle of Europe'),
      ('clarify','What we settle with you first'),
      ('faq','Frequently asked questions'),('sources','Sources')])}

<article class="prose">

<section id="short-answer" class="answer">
  <span class="answer__label">Short answer</span>
  <p>Hungary is one of the most accessible routes to an EU degree taught in English: the total annual
  budget is around half of Western Europe, teaching is in English from start to finish, and no
  national entrance exam is required. Our catalogue holds <b>490 English-taught programmes</b> at 20
  universities, medicine, dentistry, engineering, business and pilot training included. Apply in the
  right window and you are in class the following September.</p>
</section>

<h2 id="numbers">Hungary in numbers</h2>
{stats([('1367', 'The University of Pécs was founded'),
        ('40,000', 'International students in Hungary'),
        ('490', 'English-taught programmes open to you'),
        ('1999', "Hun Education's first year in Hungary")])}
<p>Those four figures answer four different parts of the decision: how established the institutions
are, how many international students will be around you, how wide your choice is, and who walks the
process with you.</p>

<h2 id="cost">Tuition and living costs</h2>
{figure('szeged-yurt-binasi',
        'A student dormitory building in Szeged with people walking past',
        'A student dormitory in Szeged.')}
<p>The most concrete reason to look at Hungary is arithmetic. The figures below are total annual
budgets including living costs, at bachelor's level, for an international student paying full tuition.
The same degree in Western Europe usually asks for close to twice that budget.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Annual budget in Hungary, at bachelor's level</caption>
  <thead><tr><th>Item</th><th>Amount</th></tr></thead>
  <tbody>
    <tr><td><b>Tuition</b></td><td class="num">€3,000 – €5,000</td></tr>
    <tr><td><b>Living costs</b></td><td class="num">€4,000 – €8,000</td></tr>
    <tr><td><b>Total for the year</b></td><td class="num">€8,500 – €14,000</td></tr>
  </tbody>
</table>
</div>
<p>The bottom of the range is a student in a dormitory outside Budapest; the top is a student in a
studio flat in the capital. In other words, you set most of your own budget. The figures come from
university tariffs and the real spending of our students, and are re-verified every academic year.</p>

{inline_cta("Tell us your budget and we will tell you which programmes are within reach.")}

<h2 id="quality">What makes Hungary stand out</h2>
{strip('Scenes from Hungary’s long-established universities', [
 ('pecs-tas-kemer-giris', 'The stone archway entrance to a University of Pécs courtyard',
  'The University of Pécs was founded in 1367.'),
 ('semmelweis-tarihi-bina', 'The historic brick and stone facade of Semmelweis University',
  'Semmelweis has trained physicians since 1769.'),
 ('elte-kutuphane', 'The two-storey historic library hall at ELTE with wooden shelving',
  'The historic library at ELTE.'),
 ('bme-tuna-kiyisi', 'A historic university building on the Danube bank with a boat on the river',
  'A university building on the Danube.'),
])}
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

<h3>A long-standing connection</h3>
<p>International students are not a recent arrival in Hungary. The universities have admitted them
since the 1800s in agriculture and engineering, and the programmes opened up further after Hungary
joined the EU in 2004, through Erasmus and the Stipendium Hungaricum scheme. Today the country hosts
around 40,000 international students, so you arrive into a community that is already there.</p>
<p>Hun Education has focused on this one country since 1999. We have our own team in Budapest, and you
can meet us in Ankara, Istanbul, Izmir or Bursa.</p>

<h3>Taught entirely in English</h3>
<p>Every programme in our catalogue is taught in English, from foundation year through to master's.
Most universities do not even ask for a language certificate; they run their own interview or online
test instead. Bachelor's admission expects B2 in practice, and where a certificate is asked for it is
IELTS 5, 6 or 6.5. If you are not there yet you enter through a university's own English Language
Preparatory year and move up to your degree from there.</p>
<p>This is not a country where English-taught programmes are a small side offering. Hungary hosts one
of the larger international student populations in Central Europe, and in medical faculties the
English-language cohort is often the majority of the intake.</p>

<h2 id="location">Student life in the middle of Europe</h2>
{figure('budapeste-balikci-tabyasi',
        'A view of Budapest at sunrise through an arch of the Fisherman’s Bastion',
        'Buda Castle and the Danube embankments are UNESCO-listed.',
        1280, 854)}
<p>Budapest is within a few hours by road or rail of Vienna, Bratislava, Zagreb and Belgrade, and a
short flight from most European capitals. As an EU and Schengen member, travel across the region on a
Hungarian student residence permit is straightforward. Long summer breaks and rail fares a student can
afford turn your degree years into a European experience as well.</p>
<p>The city itself is part of the offer: Buda Castle and the Danube embankments are UNESCO-listed,
Sziget in Budapest is one of Europe's largest music festivals, and Lake Balaton is where students end
up every summer.</p>

<h3>What student life is like</h3>
<div class="tablewrap">
<table class="dtable">
  <caption>The practical texture of a student year</caption>
  <thead><tr><th>Aspect</th><th>What to expect</th></tr></thead>
  <tbody>
    <tr><td><b>Accommodation</b></td><td>University dormitories from €60 a month; a room in a shared flat around €350; a studio around €550</td></tr>
    <tr><td><b>Transport</b></td><td>Budapest has a dense metro, tram and bus network; a student pass is about €120 a month</td></tr>
    <tr><td><b>Healthcare</b></td><td>Health insurance is compulsory for enrolment, roughly €300 a year</td></tr>
    <tr><td><b>Working</b></td><td>Permitted within the limits set by Hungarian law, which can change; do not build your budget on it</td></tr>
    <tr><td><b>Community</b></td><td>Large international student populations in Budapest, Debrecen and Pécs</td></tr>
  </tbody>
</table>
</div>

<h2 id="clarify">What we settle with you first</h2>
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
</ul>

<h2 id="faq">Frequently asked questions</h2>
{faq_block(qa_why)}

<section id="sources" class="sources">
  <h2>Sources and verification</h2>
  <ol>
    <li>Hungarian tuition and living figures are compiled from university tariffs and the real spending data of our students, and re-verified each academic year.</li>
    <li>Programme and university counts refer to institutions you can apply to through Hun Education, not to the whole Hungarian higher education system.</li>
    <li>The international student count and the Nobel Prize count are widely used public figures for Hungary.</li>
    <li>Recognition and work rights are decided by the competent authorities and can change; treat their current rules as definitive.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("You are one step from studying in Hungary", "Let us go through your field, your budget and your goal, and tell you in the first conversation which universities are realistically within reach. The consultation is free.")}

{related([(S['edu'],"Guide","Study in Hungary","The system, degrees, cities and the student visa."),
          (S['costs'],"Costs","Tuition and living costs","The realistic annual budget, item by item."),
          (S['unis'],"Universities","20 universities","The full list with city, type and fields.")])}
</article>
</div>'''

write(S['why'], page(
    S['why'],
    'Why Study in Hungary? Fees and Admission (2026) | Hun Education',
    'An EU degree taught in English at around half the cost of Western Europe: a university tradition '
    'reaching back to 1367, 40,000 international students and 490 English-taught programmes.',
    'Why Hungary',
    'Why study in Hungary?',
    'A degree in the middle of Europe, taught entirely in English, ending in an EU qualification. At '
    'around half what you would pay in Western Europe.',
    body_why, S['why'],
    [HOME, ('Why Hungary', url_of('why'))],
    qa_why))

# =====================================================================
# MASTER'S  ->  /masters-education-in-hungary/
# =====================================================================
qa_masters = [
    ("How long is a master's in Hungary?",
     "<p>Two years for most taught master's programmes, worth 120 ECTS. A small number of specialised "
     "programmes run to three semesters.</p>"),
    ("What English level does a master's require?",
     "<p>IELTS 6.5 or an equivalent certificate is the common requirement, above the B2 expected at "
     "bachelor's level. Some universities accept their own online language assessment instead.</p>"),
    ("Can I switch field between my bachelor's and my master's?",
     "<p>Sometimes, and it depends on how far the switch goes. A related move is usually workable with "
     "the right motivation letter; a move into an unrelated technical or health field normally requires "
     "prerequisite credits. We check the specific programme's rules before you apply.</p>"),
    ("Is a thesis required?",
     "<p>Yes. Taught master's programmes in Hungary end in a written thesis and its defence, and the "
     "thesis normally carries a substantial share of the final classification.</p>"),
]

body_masters = f'''<div class="alayout">
{toc([('who','Who a Hungarian master’s suits'),
      ('fields','Fields and programmes'),('requirements','Entry requirements'),
      ('faq','Frequently asked questions'),('sources','Sources')])}

<article class="prose">

<section id="short-answer" class="answer">
  <span class="answer__label">Short answer</span>
  <p>A master's in Hungary takes two years and 120 ECTS and is taught in English. Hun Education's
  published range is €4,000 to €6,000 a year; across the catalogue the actual figures run wider, from
  about €3,200 to €14,000 depending on the university and the field. Admission expects a recognised bachelor's degree in a related
  field and usually IELTS 6.5. Applications close between April and June for the September intake, and
  several programmes also take a February intake.</p>
</section>

<h2 id="who">Who a Hungarian master's suits</h2>
{figure('metu-ogrenci-portre',
        'A student in a campus corridor in front of a glass facade',
        'A student on the Budapest Metropolitan campus.')}
<p>Three profiles come to us most often, and the answer differs for each.</p>
<ul>
  <li><b>Specialising after a bachelor's at home.</b> The most common case, and the most
  straightforward: a related bachelor's plus IELTS 6.5 is usually the whole requirement.</li>
  <li><b>Adding an EU qualification to an existing career.</b> Works well in business, IT and
  engineering management, where the master's is the credential rather than the training.</li>
  <li><b>Moving toward a doctorate.</b> Hungarian master's programmes are thesis-based, which makes
  the step into a PhD programme a continuation rather than a restart.</li>
</ul>

<h2 id="fields">Fields, fees and duration</h2>
{strip('Scenes from master’s programmes', [
 ('corvinus-bina', 'The modern glass and stone facade of Corvinus University',
  'Business and economics: Corvinus.'),
 ('bme-kampus-ogrenciler', 'A group of students building a project on a campus lawn',
  'Project work in engineering.'),
 ('metu-tasarim-atolye', 'Print work laid out on the floor of a design studio with a student',
  'A design studio.'),
 ('elte-kutuphane', 'The two-storey historic library hall at ELTE with wooden shelving',
  'Thesis season: the ELTE library.'),
])}
<p>Master's-level programmes in our catalogue concentrate in four areas. The full filterable list is in
the <a href="{S['progs']}">course catalogue</a>.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Master's programmes by field</caption>
  <thead><tr><th>Field</th><th>Example programmes</th><th>Annual fee</th></tr></thead>
  <tbody>
    <tr><td><b>IT and engineering</b></td><td>Software Engineering MSc, Engineering Management MSc</td><td class="num">€4,000 – €6,000</td></tr>
    <tr><td><b>Business and finance</b></td><td>Finance MSc, Business MSc</td><td class="num">€4,000 – €6,000</td></tr>
    <tr><td><b>Humanities and social sciences</b></td><td>Psychology MA, English Studies MA</td><td class="num">€7,800 – €9,400 (psychology)</td></tr>
    <tr><td><b>Health sciences</b></td><td>Programme-dependent; entrance assessment applies</td><td class="num">varies</td></tr>
  </tbody>
</table>
</div>

<h2 id="requirements">Entry requirements and applying</h2>
{figure('elte-avlu',
        'The arcaded inner courtyard at ELTE',
        'The inner courtyard at ELTE.')}
<div class="tablewrap">
<table class="dtable">
  <caption>What a master's application file contains</caption>
  <thead><tr><th>Requirement</th><th>Detail</th></tr></thead>
  <tbody>
    <tr><td><b>Bachelor's degree</b></td><td>Apostilled, in a related field; final-year students can pre-apply with a student certificate</td></tr>
    <tr><td><b>Transcript</b></td><td>English or sworn translation, with the credit breakdown</td></tr>
    <tr><td><b>English</b></td><td>IELTS 6.5 or equivalent; some universities accept their own test</td></tr>
    <tr><td><b>CV</b></td><td>English, Europass preferred; weighs more than at bachelor's level</td></tr>
    <tr><td><b>Motivation letter</b></td><td>Required by many programmes, and the piece most often written too late</td></tr>
    <tr><td><b>Interview</b></td><td>Applied by some programmes, usually online</td></tr>
  </tbody>
</table>
</div>

<h3>Fees and duration</h3>
<div class="answer">
  <span class="answer__label">Two years, 120 ECTS</span>
  <p>The published range is <b>€4,000 to €6,000 a year</b>, and that is where most programmes sit.
  Psychology is higher, from €7,800 at Pécs to €9,400 at ELTE. Adding living costs, a realistic total is
  <b>€9,000 to €15,000 a year</b>, moving mostly with your accommodation choice.</p>
</div>

<h3>How the application runs</h3>
<ol class="steps">
  <li><div><h3>Eligibility check</h3><p>We compare your bachelor's content against the programme's prerequisites and tell you where a credit gap would block admission.</p></div></li>
  <li><div><h3>File and motivation letter</h3><p>The letter is prepared with you rather than for you; programmes notice generic text.</p></div></li>
  <li><div><h3>Submission and interview</h3><p>The application goes through the university's own system, and we prepare you for the interview where one applies.</p></div></li>
  <li><div><h3>Offer, payment, visa</h3><p>Conditional offer, then the final Acceptance Letter after payment, which is the core document for the student visa.</p></div></li>
</ol>

<h2 id="faq">Frequently asked questions</h2>
{faq_block(qa_masters)}

<section id="sources" class="sources">
  <h2>Sources and verification</h2>
  <ol>
    <li>Programme, fee and admission details are compiled from the universities' current published conditions and reviewed before each application period.</li>
    <li>Credit equivalence and prerequisite decisions rest with the admitting university.</li>
    <li>Recognition of the completed degree is decided by the competent authority in your own country.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Start your master’s this intake", "Send us your transcript and we will tell you in the first conversation which programmes you qualify for and where a credit gap would need filling first. The consultation is free.")}

{related([(S['apply'],"Admissions","Admission requirements","Documents, language, entrance exams and the calendar."),
          (S['progs'],"Catalogue","Filter by level","Narrow the catalogue to master’s programmes."),
          (S['costs'],"Costs","Tuition and living costs","The realistic annual budget.")])}
</article>
</div>'''

write(S['masters'], page(
    S['masters'],
    "Master's Degrees in Hungary: Fees and Requirements (2026) | Hun Education",
    "English-taught master's programmes in Hungary: two years and 120 ECTS, €4,000 to €6,000 a year, "
    "entry requirements, the motivation letter and the application calendar.",
    "Master's guide",
    "Master's degrees in Hungary",
    'Two years, 120 ECTS, taught in English. What the programmes are, what admission asks for and what '
    'a realistic budget looks like.',
    body_masters, S['masters'],
    [HOME, ("Master's", url_of('masters'))],
    qa_masters))
