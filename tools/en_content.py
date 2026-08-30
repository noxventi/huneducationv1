# -*- coding: utf-8 -*-
# gen_pages.py tarafindan exec edilir (LANG=en).
# Ingilizce icerik, Turkce sayfanin birebir cevirisi degil: ayni olgular,
# uluslararasi ogrenci okuyucusuna gore yeniden yazilmis metin ve
# Ingilizce aramalara gore secilmis basliklar.

# =====================================================================
# 1) ADMISSION REQUIREMENTS
# =====================================================================
qa_apply = [
    ("Do I need a national university entrance exam to study in Hungary?",
     "<p>No, <b>no national entrance exam score is required</b>. Universities run their own admission "
     "process: they look at your school record, and medicine, engineering, architecture and arts "
     "programmes set their own entrance exam or interview. So the decision rests on a defined, "
     "preparable assessment rather than on one exam day.</p>"),
    ("Can I apply without an English language certificate?",
     "<p>Yes. Most universities do not ask for one anyway; they run their own interview instead. If you "
     "are below B2 you can apply to a university's English Language Preparatory programme, where fees "
     "start from €2,500 a year, and move up to your degree on successful completion.</p>"),
    ("What happens to my tuition fee if my visa is refused?",
     "<p>You send the university the written refusal issued by the consulate, and the tuition is then "
     "usually refunded within 30 working days. Application, entrance exam and registration fees are "
     "outside the refund. The exact terms are in your service agreement.</p>"),
    ("How should my diploma and transcript be translated?",
     "<p>Documents must be in English, or translated into English by a sworn translator. The diploma "
     "also needs an apostille. The apostille is issued by the competent authority in the country "
     "where the document was produced, and getting it before the translation saves time.</p>"),
]

body_apply = f'''<div class="alayout">
{toc([('eligibility','Who can apply?'),('documents','Documents and English'),
      ('exam','Entrance exams and interviews'),('calendar','Calendar and process'),
      ('faq','Frequently asked questions'),('sources','Sources')])}

<article class="prose">

<section id="short-answer" class="answer">
  <span class="answer__label">Short answer</span>
  <p>To apply you need an apostilled diploma, an English transcript, a copy of your passport and an
  English CV; the bank statement comes at the visa stage, not with the application. Bachelor's
  programmes expect B2 in practice, though most universities run their own interview rather than ask
  for a certificate. The age limit is 25 for a bachelor's and 28 for a master's, with no limit for
  medicine. Applications close between April and June for the September intake and between the end of
  October and November for the February intake.</p>
</section>

<h2 id="eligibility">Who can apply?</h2>
{strip('Scenes from our students', [
 ('metu-ogrenci-grubu', 'A group of international students gathered in a campus garden',
  'International students on campus.'),
 ('obuda-ogrenciler', 'A group of students on a bench under the Óbuda University sign',
  'Between classes.'),
 ('budapeste-koprude-ogrenciler', 'Two students on Liberty Bridge in Budapest',
  'Our students on Liberty Bridge.'),
 ('pilotaj-ogrenciler-pist', 'Three students in pilot shirts together at the airfield',
  'Our pilot students at the airfield.'),
])}
<p>The good news is that most applicants already qualify. Even so, three points are worth settling
before you start assembling paperwork.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Age limits by programme type</caption>
  <thead><tr><th>Programme</th><th>Maximum age</th></tr></thead>
  <tbody>
    <tr><td>Preparatory programmes</td><td class="num">25</td></tr>
    <tr><td>Bachelor's</td><td class="num">25</td></tr>
    <tr><td>Master's</td><td class="num">28</td></tr>
    <tr><td>Medicine, dentistry, pharmacy</td><td>No age limit</td></tr>
  </tbody>
</table>
</div>
<p>If you are above these limits, write to us anyway. The limits are real, but a workable route
usually exists; we will tell you which one in the first conversation.</p>

<h3>Nationality</h3>
<p>We can submit applications on behalf of citizens of more than 25 countries: <b>EU countries, the
United States and Latin America, Albania, Algeria, Azerbaijan, Bosnia and Herzegovina, Egypt, Georgia,
Jordan, Kazakhstan, Kyrgyzstan, Mongolia, Qatar, Russia, Serbia, Thailand, Türkiye, Ukraine,
Uzbekistan and Vietnam.</b> If your country is not listed, write anyway and we will point you to the
right channel.</p>

<h3>Financial capacity</h3>
<p>The consulate expects to see that your studies are funded, and the amount is lower than most people
expect: <b>€650 a month across a 10-month academic year, so about €6,500</b>, held in your own or your
sponsor's account, alongside evidence of regular income. This is not a Hungarian peculiarity; every
country's consulate looks for the same thing. We plan the sponsor letter with you.</p>

{inline_cta("Not sure whether you qualify? One message is enough to find out.")}

<h2 id="documents">Documents and English</h2>
<p>These documents are asked for in every application. Individual programmes may want more; we go
through the admission requirements with you before you apply.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Core documents in an application file</caption>
  <thead><tr><th>Document</th><th>Format requirement</th><th>Note</th></tr></thead>
  <tbody>
    <tr><td><b>Application form</b></td><td>The university's own system</td><td>Each university uses a separate form</td></tr>
    <tr><td><b>Passport copy</b></td><td>Photo page</td><td>Validity must cover the length of your studies</td></tr>
    <tr><td><b>Diploma</b></td><td>Apostilled</td><td>Final-year students can pre-apply with a student certificate</td></tr>
    <tr><td><b>Transcript</b></td><td>English or sworn translation</td><td>High school or bachelor's grade record</td></tr>
    <tr><td><b>English CV</b></td><td>Europass preferred, with photo</td><td>Weighs more at master's level</td></tr>
    <tr><td><b>Bank statement</b></td><td>Last 6 months, sponsor's account</td><td><b>Not required to apply.</b> Needed at the visa stage; add a sponsor letter if someone else funds your studies</td></tr>
    <tr><td><b>Language certificate</b></td><td>IELTS or equivalent</td><td>Often <b>not</b> required: most universities run their own interview instead</td></tr>
  </tbody>
</table>
</div>

<h3>The English requirement</h3>
<p>Almost every programme in this catalogue is taught in English. The point applicants most often get
wrong is this: <b>most Hungarian universities do not ask for a language certificate at all</b>, because
they run their own interview or online test instead. Some do ask for IELTS, at 5, 6 or 6.5 depending on
the university and the programme.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Expected English level by study level</caption>
  <thead><tr><th>Level</th><th>Expected</th><th>If you have no certificate</th></tr></thead>
  <tbody>
    <tr><td><b>Bachelor's</b></td><td class="num">B2 in practice · IELTS 5, 6 or 6.5 where asked</td><td>English Language Preparatory programme</td></tr>
    <tr><td><b>Master's</b></td><td class="num">IELTS 6.5 or equivalent where asked</td><td>Preparatory year, then reapply</td></tr>
    <tr><td><b>Preparatory</b></td><td>University's own placement test</td><td>No certificate required</td></tr>
  </tbody>
</table>
</div>

<h2 id="exam">Entrance exams and interviews</h2>
{figure('metu-derslik',
        'Students working at laptops in a lecture theatre',
        'The decision rests on your school record and a subject assessment, not one exam day.',
        1280, 720)}
<p>No national entrance exam score is asked for; the university assesses you on its own terms instead.
For most applicants that is an advantage, because the decision rests on your school record and a
subject assessment rather than on one exam day, and the preparation windows are short. What to expect
by field:</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Entrance assessment by field</caption>
  <thead><tr><th>Field</th><th>Assessment</th><th>Preparation time</th></tr></thead>
  <tbody>
    <tr><td><b>Medicine, dentistry, pharmacy</b></td><td>Chemistry and biology exam, oral or written</td><td>6–10 weeks</td></tr>
    <tr><td><b>Engineering</b></td><td>Online physics and mathematics exam</td><td>4–6 weeks</td></tr>
    <tr><td><b>Architecture</b></td><td>Physics, mathematics and a portfolio</td><td>8–12 weeks</td></tr>
    <tr><td><b>Film, design, arts</b></td><td>Portfolio and/or film presentation</td><td>Depends on your portfolio</td></tr>
    <tr><td><b>Business, social sciences</b></td><td>Written test and/or interview may apply</td><td>2–4 weeks</td></tr>
  </tbody>
</table>
</div>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Preparation times are field observations drawn from the application files our advisers have handled,
not official university guidance. The admission decision always rests with the university.</p>

<h2 id="calendar">Calendar and process</h2>
{strip('Scenes from the campuses', [
 ('debrecen-cam-bina', 'A glass-fronted modern building at the University of Debrecen',
  'University of Debrecen.'),
 ('szeged-ana-bina', 'The yellow facade of the University of Szeged main building',
  'University of Szeged.'),
 ('obuda-sari-bina', 'The yellow historic building of Óbuda University',
  'Óbuda University, Budapest.'),
 ('metu-bina-tabela', 'The round campus building signed “Budapesti Metropolitan Egyetem”',
  'Budapest Metropolitan.'),
])}
<p>Hungary has two intakes a year. An intake can close before the published date once places run out,
which is why applying early matters.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Application window by intake</caption>
  <thead><tr><th>Intake</th><th>Studies begin</th><th>Application deadline</th><th>Start preparing</th></tr></thead>
  <tbody>
    <tr><td><b>Autumn</b></td><td class="num">September</td><td class="num">April – June (some until end of July)</td><td class="num">January – February</td></tr>
    <tr><td><b>Spring</b></td><td class="num">February</td><td class="num">End of October – November</td><td class="num">August – September</td></tr>
  </tbody>
</table>
</div>

<h3>The process step by step</h3>
<ol class="steps">
  <li><div><h3>File review</h3><p>We assess your documents and academic record and identify the programmes where you have a realistic chance.</p></div></li>
  <li><div><h3>Conditional offer</h3><p>The application goes to the university, and a Conditional Acceptance Letter is issued after a positive assessment.</p></div></li>
  <li><div><h3>Payment and enrolment</h3><p>You make the payment the university requests; the receipt is added to your file.</p></div></li>
  <li><div><h3>Final acceptance letter</h3><p>The official Acceptance Letter arrives by email. It is the core document for your visa application.</p></div></li>
  <li><div><h3>Visa application</h3><p>You apply at your nearest Hungarian consulate with the Acceptance Letter. The decision rests entirely with the consulate.</p></div></li>
  <li><div><h3>Travel and arrival</h3><p>After the visa we plan your flight, accommodation and arrival. You will need travel and accident insurance covering at least three months, ideally the full year.</p></div></li>
</ol>

<h3>Common mistakes</h3>
<ul>
  <li><b>Leaving the apostille until last.</b> This is where most time is lost. The apostille must come before the translation.</li>
  <li><b>Not preparing the bank statement early.</b> It has to cover the last six months, so it cannot be fixed retroactively.</li>
  <li><b>Applying to a single university.</b> Places can close mid-intake, so carrying more than one option lowers the risk.</li>
  <li><b>Assuming you must have graduated first.</b> Final-year students can pre-apply with a student certificate and add the diploma later.</li>
</ul>

<h2 id="faq">Frequently asked questions</h2>
{faq_block(qa_apply)}

<section id="sources" class="sources">
  <h2>Sources and verification</h2>
  <ol>
    <li>Document, language, entrance exam and calendar information is compiled by our advisory team from the universities' current admission conditions and reviewed before every application period.</li>
    <li>Preparation times are field observations from application files handled by our advisers; they are not official university guidance.</li>
    <li>The admission decision rests with the university and the visa decision with the relevant consulate. Treat the university's own admissions page as definitive.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Let us start your application today", "We will tell you which documents you need and which programmes you have a realistic chance at, in the first conversation. It is free and commits you to nothing.")}

{related([(S['costs'],"Costs","Tuition and living costs","Tuition fees, accommodation and one-off charges."),
          (S['progs'],"Catalogue","Filter the programmes","490 programmes by level, field, city and budget."),
          (S['unis'],"Universities","20 universities","Compare by city, type and leading fields.")])}
</article>
</div>'''

write(S['apply'], page(
    S['apply'],
    'Hungary University Admission Requirements (2026) | Hun Education',
    "Age limits, eligible nationalities, financial capacity, documents, the English requirement and "
    "entrance exams for applying to a university in Hungary, step by step.",
    'Admissions guide',
    'University admission requirements in Hungary',
    'Which documents are asked for, what English level is needed, which programmes set an entrance '
    'exam and when do applications close? The whole process, with its conditions.',
    body_apply, S['apply'],
    [HOME, ('Admissions', url_of('apply'))],
    qa_apply,
    howto=('How to apply to a university in Hungary', 'The six-step application process, from file review to the visa and arrival in Budapest.', [('File review', 'Your documents and academic record are assessed and the programmes you have a realistic chance at are identified.'), ('Conditional offer', 'The application goes to the university and, on a positive assessment, a conditional offer is issued.'), ('Payment and registration', 'The payment the university requires is made and the receipt is added to the file.'), ('Final Acceptance Letter', 'The official Acceptance Letter arrives by email. It is the core document for the visa application.'), ('Visa application', 'You apply at your nearest Hungarian consulate with the Acceptance Letter. The decision rests entirely with the consulate.'), ('Travel and arrival', 'Flights, accommodation and the airport pick-up are planned. Our Budapest team meets you and settles you into your accommodation.')])))

# =====================================================================
# 2) TUITION AND LIVING COSTS
# =====================================================================
qa_costs = [
    ("How much does one year of study in Hungary cost in total?",
     "<p>Tuition and living costs together come to <b>€8,500 – €14,000</b> a year. The range moves with "
     "your tuition fee and your accommodation choice: a student in a dormitory lands near the lower "
     "end, one in a studio flat near the upper end.</p>"),
    ("Why is medicine more expensive than other programmes?",
     "<p>Medicine and dentistry require laboratories, clinical practice and a longer course, which puts "
     "fees between €15,800 and $19,900 a year. Most bachelor's programmes sit between €3,000 and "
     "€5,000.</p>"),
    ("Are fees paid per term or per year?",
     "<p>The tuition fees on this page are annual, pilot training included. Payment schedules vary by "
     "university; most collect at the start of each term.</p>"),
    ("Are scholarships available?",
     "<p>Scholarship options vary by university, programme and academic year. Confirm current "
     "conditions on the university's official page before applying; your adviser will tell you which "
     "programmes have an open application window.</p>"),
]

body_costs = f'''<div class="alayout">
{toc([('tuition','Tuition fees'),('living','Living costs'),
      ('total','Your annual total'),
      ('faq','Frequently asked questions'),('sources','Sources')])}

<article class="prose">

<section id="short-answer" class="answer">
  <span class="answer__label">Short answer</span>
  <p>Studying and living in Hungary costs <b>€8,500 – €14,000</b> a year in total. Bachelor's tuition
  runs €3,000 – €5,000, <a class="link" href="{S['masters']}">master's</a> €4,000 – €6,000, and <a class="link" href="{S['medicine']}">medicine</a> and dentistry €15,800 to $19,900.
  Accommodation is €60 – €550 a month and everyday living costs about €300. The single most volatile
  item in the budget is your accommodation choice.</p>
</section>

<h2 id="tuition">Tuition fees</h2>
{strip('Scenes from the universities where fees vary', [
 ('semmelweis-modern-bina', 'The modern Semmelweis University building lit at dusk',
  'Semmelweis University, Budapest.'),
 ('debrecen-kuleli-bina', 'The towered building of the University of Debrecen',
  'University of Debrecen.'),
 ('corvinus-bina', 'The modern glass and stone facade of Corvinus University',
  'Corvinus University.'),
 ('miskolc-cam-bina', 'The glass-fronted building and forecourt at the University of Miskolc',
  'University of Miskolc.'),
 ('elte-tarihi-bina', 'The historic stone facade of ELTE', 'ELTE, Budapest.'),
])}
<p>Price is Hungary's strongest card: the same degree in Western Europe usually asks for close to
twice the budget. The table below shows annual tuition; accommodation and living costs are not
included.</p>
and living costs are not included.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Annual tuition by level and field (€)</caption>
  <thead><tr><th>Level / field</th><th>Annual fee</th><th>Duration</th></tr></thead>
  <tbody>
    <tr><td><b>Bachelor's</b></td><td class="num">€3,000 – €5,000</td><td>3 – 4 years</td></tr>
    <tr><td><b>Master's</b></td><td class="num">€4,000 – €6,000</td><td>2 years</td></tr>
    <tr><td><b>Doctorate</b></td><td class="num">€6,000 – €8,000</td><td>3 – 4 years</td></tr>
    <tr><td><b>Medicine</b></td><td class="num">€15,800 – $19,900</td><td>6 years</td></tr>
    <tr><td><b>Dentistry</b></td><td class="num">€18,600</td><td>5 years</td></tr>
    <tr><td><b>Psychology</b></td><td class="num">€7,800 – €9,400</td><td>3 years</td></tr>
    <tr><td><b><a class="link" href="{S['pilot']}">Pilot training</a></b></td><td class="num">€29,500 / year</td><td>3.5 years</td></tr>
    <tr><td><b>English foundation</b></td><td class="num">from €2,500 / year</td><td>1 year</td></tr>
  </tbody>
</table>
</div>

<h3>Differences between universities</h3>
<p>Programmes at the same level also differ from one university to the next:</p>
<div class="tablewrap">
<table class="dtable">
  <caption>Annual fee range at selected universities</caption>
  <thead><tr><th>University</th><th>City</th><th>Annual fee</th></tr></thead>
  <tbody>
    <tr><td><b>Eötvös Loránd University (ELTE)</b></td><td>Budapest</td><td class="num">€4,000 – €6,000</td></tr>
    <tr><td><b>University of Debrecen</b></td><td>Debrecen</td><td class="num">€3,500 – €5,500</td></tr>
    <tr><td><b>University of Pécs (PTE)</b></td><td>Pécs</td><td class="num">€3,000 – €5,000</td></tr>
  </tbody>
</table>
</div>

<h2 id="living">Living costs</h2>
{figure('szeged-yurt-binasi',
        'A student dormitory building in Szeged with people walking past',
        'Accommodation is the choice that moves your budget most.',
        1280, 720)}
<p>Living costs alone come to <b>€4,000 – €8,000</b> a year. Your choice of city is decisive here:
Budapest is the most expensive, while Szeged, Pécs and Nyíregyháza run noticeably lower.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Monthly living cost items</caption>
  <thead><tr><th>Item</th><th>Amount</th><th>Period</th><th>Note</th></tr></thead>
  <tbody>
    <tr><td><b>University dormitory</b></td><td class="num">€60 – €400</td><td>Monthly</td><td>Places are limited, apply early</td></tr>
    <tr><td><b>Room in a shared flat</b></td><td class="num">≈ €350</td><td>Monthly</td><td>Shared apartment</td></tr>
    <tr><td><b>Studio flat</b></td><td class="num">≈ €550</td><td>Monthly</td><td>Bills may be separate</td></tr>
    <tr><td><b>Groceries and bills</b></td><td class="num">≈ €300</td><td>Monthly</td><td>Average student spend</td></tr>
    <tr><td><b>Public transport</b></td><td class="num">€120</td><td>Monthly</td><td>Student discounts may vary</td></tr>
    <tr><td><b>Health insurance</b></td><td class="num">€300</td><td>Yearly</td><td>Compulsory for enrolment</td></tr>
  </tbody>
</table>
</div>

<h3>One-off fees</h3>
<div class="tablewrap">
<table class="dtable">
  <caption>One-off payments during application and settling in</caption>
  <thead><tr><th>Item</th><th>Amount</th><th>When</th></tr></thead>
  <tbody>
    <tr><td><b>Application fee</b></td><td class="num">€140</td><td>On application · non-refundable</td></tr>
    <tr><td><b>Student visa</b></td><td class="num">€95 – €145</td><td>After the acceptance letter</td></tr>
    <tr><td><b>Accommodation deposit</b></td><td class="num">€120</td><td>On moving in</td></tr>
  </tbody>
</table>
</div>

<h2 id="total">Your annual total</h2>
{figure('pecs-sehir-hava',
        'An aerial view of the red rooftops of central Pécs',
        'Pécs: a university city outside Budapest.')}
<p>Adding the items up one by one is misleading, because the accommodation choice alone shifts the
figure by several thousand euros a year. The realistic planning range is:</p>
<div class="answer">
  <span class="answer__label">Annual total</span>
  <p><b>€8,500 – €14,000</b>: tuition and living costs included, at bachelor's level.
  For medicine and dentistry the tuition alone runs from €15,800 to $19,900, so the total budget
  sits clearly above this range.</p>
</div>

<h3>How we build your budget</h3>
<ol class="steps">
  <li><div><h3>Fix the programme and the city</h3><p>Tuition and rent move together; plan them as one figure, not two.</p></div></li>
  <li><div><h3>Choose your accommodation scenario</h3><p>The gap between a dormitory, a shared room and a studio flat is the largest variable in the annual budget.</p></div></li>
  <li><div><h3>Add the first-year one-off fees</h3><p>Application, visa and deposit appear only in year one, but they pull your cash need forward.</p></div></li>
  <li><div><h3>Allow for currency risk</h3><p>Fees are quoted in euros and dollars; exchange rate movement over the payment schedule affects your budget.</p></div></li>
</ol>

<h2 id="faq">Frequently asked questions</h2>
{faq_block(qa_costs)}

<section id="sources" class="sources">
  <h2>Sources and verification</h2>
  <ol>
    <li>Tuition fees are compiled from the tariffs published by the universities; living costs come from the real spending data of our students in Hungary.</li>
    <li>Figures are re-verified by our advisory team at the start of each academic year.</li>
    <li>Fees may be changed by the universities. The university's official page is definitive for the final amount.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Let us draw up your budget", "We will build a realistic annual budget table around the programme, city and accommodation you choose.")}

{related([(S['apply'],"Admissions","Admission requirements","Documents, language, entrance exams and the calendar."),
          (S['progs'],"Catalogue","Programmes by budget","Narrow the list with the annual budget filter."),
          (S['edu'],"Guide","Study in Hungary","The system, the cities, visas and recognition.")])}
</article>
</div>'''

write(S['costs'], page(
    S['costs'],
    'Tuition Fees and Living Costs in Hungary (2026) | Hun Education',
    "Bachelor's, master's, medicine and pilot training tuition fees in Hungary, plus accommodation, "
    "living costs, visa and insurance, the realistic annual budget range.",
    'Cost guide',
    'Tuition fees and living costs in Hungary',
    'How tuition changes by programme, what you spend each month and what a realistic total budget '
    'for one year looks like, item by item.',
    body_costs, S['costs'],
    [HOME, ('Costs', url_of('costs'))],
    qa_costs))
