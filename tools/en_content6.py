# -*- coding: utf-8 -*-
# Canlida yayinda olup yeni tasarimda karsiligi olmayan sayfalar (2/2).

# =====================================================================
# MEDICINE  ->  /studying-medicine-in-hungary-.../
# =====================================================================
qa_med = [
    ("Is there an entrance exam for medicine in Hungary?",
     "<p>Yes, every medical faculty sets its own entrance assessment in chemistry and biology, oral or "
     "written depending on the university. No national exam score is asked for, and because the syllabus "
     "is defined, applicants typically prepare in 6 to 10 weeks.</p>"),
    ("How long does medicine take, and what degree do you get?",
     "<p>Six years for general medicine and five for dentistry, both single-cycle integrated programmes. "
     "The award is a doctoral-level professional degree (MD or DMD), not a bachelor's plus master's.</p>"),
    ("What does medicine cost per year?",
     "<p>It depends on the university and the currency it charges in: Semmelweis $19,900, Pécs $18,000 "
     "and Szeged €15,800 a year. Dentistry at Pécs is €18,600. Hun Education's published figure for "
     "medicine and dentistry including living costs is about €26,000 a year.</p>"),
    ("Can I practise at home with a Hungarian medical degree?",
     "<p>Medicine is a regulated profession everywhere, so practising requires recognition by the "
     "competent authority in the country where you want to work, and often a licensing examination. "
     "Check your national authority's current requirements before you apply. We do not promise "
     "recognition.</p>"),
]

body_med = f'''<div class="alayout">
{toc([('universities','Where medicine is taught'),
      ('structure','How the six years run'),
      ('exam','The entrance exam'),('cost','What it costs'),('faq','Frequently asked questions'),('sources','Sources')])}

<article class="prose">

<section id="short-answer" class="answer">
  <span class="answer__label">Short answer</span>
  <p>Studying medicine in Hungary is possible without a national entrance exam and entirely in
  English. The six-year integrated programme runs at <b>three long-established universities</b>:
  Semmelweis in Budapest, which has trained physicians since 1769, plus Pécs and Szeged. Annual tuition
  is $19,900, $18,000 and €15,800 respectively; dentistry at Pécs is €18,600 over five years. The key
  to admission is the faculty's own chemistry and biology assessment, and applicants typically prepare
  for it in 6 to 10 weeks.</p>
</section>

<h2 id="universities">Where medicine is taught</h2>
<p>Three universities, six programmes. Semmelweis is one of Europe's oldest medical faculties, Pécs is
the country's oldest university, and Szeged offers the most affordable medicine tuition in euros.
Dentistry and pharmacy run at the same faculties, so you do not have to narrow your list to a single
city.</p>
<div class="tablewrap">
<table class="dtable">
  <caption>Medical faculties open to international students</caption>
  <thead><tr><th>University</th><th>City</th><th>Programmes</th><th>Annual fee</th></tr></thead>
  <tbody>
    <tr><td><b>Semmelweis University (SOTE)</b></td><td>Budapest</td><td>Medicine (6 yrs)</td><td class="num">$19,900 / year</td></tr>
    <tr><td><b>University of Pécs (PTE)</b></td><td>Pécs</td><td>Medicine (6 yrs)</td><td class="num">$18,000 / year</td></tr>
    <tr><td><b>University of Szeged (SZTE)</b></td><td>Szeged</td><td>Medicine (6 yrs)</td><td class="num">€15,800 / year</td></tr>
    <tr><td><b>University of Pécs (PTE)</b></td><td>Pécs</td><td>Dentistry (5 yrs)</td><td class="num">€18,600 / year</td></tr>
    <tr><td><b>Semmelweis University (SOTE)</b></td><td>Budapest</td><td>Pharmacy (5 yrs)</td><td class="num">€12,600 / year</td></tr>
    <tr><td><b>University of Pécs (PTE)</b></td><td>Pécs</td><td>Pharmacy (5 yrs)</td><td class="num">€8,800 / year</td></tr>
  </tbody>
</table>
</div>

<h2 id="exam">The entrance exam and preparation</h2>
{figure('tip-ogrenci-calisma-grubu',
        'A group of students working together at a table in a classroom',
        'Preparation takes 6–10 weeks on average.')}
<p>This is the step that decides admission, and the good news is that the syllabus is known, the scope
is narrow and the preparation window is short. Instead of a national exam score, the faculty assesses
you in chemistry and biology, which means it is an exam you can prepare for from your school
syllabus.</p>
<div class="tablewrap">
<table class="dtable">
  <caption>What the assessment covers</caption>
  <thead><tr><th>Element</th><th>Detail</th></tr></thead>
  <tbody>
    <tr><td><b>Subjects</b></td><td>Chemistry and biology</td></tr>
    <tr><td><b>Format</b></td><td>Set by the university. Semmelweis records its assessment as an interview; Szeged runs a written and oral exam online.</td></tr>
    <tr><td><b>Language</b></td><td>English, alongside an assessment of your English itself</td></tr>
    <tr><td><b>Preparation</b></td><td>6 to 10 weeks is the range we observe across the files we handle</td></tr>
    <tr><td><b>Retake</b></td><td>Policy varies by university and by intake</td></tr>
  </tbody>
</table>
</div>
<p>You do not prepare alone: your adviser sets out what each faculty asks, where past applicants
struggled and how many weeks you personally need.</p>
{inline_cta("Let us look at your chemistry and biology background and build your preparation calendar.")}
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
The preparation range is a field observation from our own application files, not official university
guidance. The admission decision belongs entirely to the faculty.</p>

<h2 id="structure">How the six years run</h2>
{strip('Scenes from medical training', [
 ('tip-mikroskop-laboratuvar',
  'A researcher in a lab coat at a microscope, with blood sample tubes on the bench',
  'The first two years: basic sciences and the lab.'),
 ('tip-goruntuleme-ekranlari',
  'Brain imaging slices on screens in a radiology room',
  'The clinical years: diagnosis and imaging.'),
 ('tip-laboratuvar-tup',
  'A lab worker in a hairnet and goggles pipetting into blue test tubes',
  'Laboratory work runs through the whole degree.'),
])}
<ol class="steps">
  <li><div><h3>Years 1–2 · Basic sciences</h3><p>Anatomy, biochemistry, physiology. The heaviest examination load of the programme sits here, and it is where most attrition happens.</p></div></li>
  <li><div><h3>Years 3–4 · Preclinical and clinical</h3><p>Pathology, pharmacology and the move into clinical subjects, with hospital contact beginning.</p></div></li>
  <li><div><h3>Year 5 · Clinical rotations</h3><p>Rotations across the major specialties in teaching hospitals.</p></div></li>
  <li><div><h3>Year 6 · Practical year</h3><p>A full year of supervised clinical practice, then the final examinations and the degree.</p></div></li>
</ol>

<h2 id="cost">Fees and what they cover</h2>
<div class="answer">
  <span class="answer__label">Realistic annual total</span>
  <p><b>About €26,000</b> including living costs. That is Hun Education's own published figure for
  medicine and dentistry, and it sits far above the €8,500 to €14,000 typical of other programmes
  because tuition alone is €15,800 to $19,900.</p>
</div>
<p>That figure sits well below medical schools in Western Europe and North America, which is exactly
what makes Hungary attractive to international students. Plan across the full six years: the first year
also carries the one-off application, visa and deposit charges, and a programme priced in dollars means
budgeting for currency movement. We map the payment schedule out with you.</p>

<h3>If you are not ready yet</h3>
<p>Two routes exist for applicants who are not yet at the required level.</p>
<div class="tablewrap">
<table class="dtable">
  <caption>Pre-medical and language routes</caption>
  <thead><tr><th>Programme</th><th>University</th><th>Annual fee</th></tr></thead>
  <tbody>
    <tr><td><b>PreMedical / PreEngineering / PreBusiness</b></td><td>University of Pécs (PTE)</td><td class="num">€5,850</td></tr>
    <tr><td><b>Two-semester Pre-Medical Track</b></td><td>McDaniel College Budapest</td><td class="num">€7,230</td></tr>
    <tr><td><b>Pre-Medical (Intensive)</b></td><td>McDaniel College Budapest</td><td class="num">€7,800</td></tr>
    <tr><td>English Language Preparatory</td><td>Several universities</td><td class="num">from €2,500</td></tr>
  </tbody>
</table>
</div>
<p>All of these are in the <a href="{S['progs']}">catalogue</a> with their current fees and deadlines.</p>

<h3>After graduation</h3>
<p>Medicine is a regulated profession, and the degree alone does not confer the right to practise
anywhere. Recognition is decided by the competent authority in the country where you want to work,
usually on the basis of the university's standing, the programme content, its length and the clinical
training completed. Many countries add a licensing examination.</p>
<p>Check that pathway <b>before</b> you apply rather than in your final year. We go through the known
requirements with you during the consultation, and we do not promise an outcome that is not ours to
give.</p>

<h2 id="faq">Frequently asked questions</h2>
{faq_block(qa_med)}

<section id="sources" class="sources">
  <h2>Sources and verification</h2>
  <ol>
    <li>Fees, programme structure and entrance exam requirements are compiled from the faculties' current published conditions and reviewed each academic year.</li>
    <li>Preparation times are field observations from application files handled by our advisers.</li>
    <li>Recognition and licensing are decided by the competent authority in your own country; treat its current rules as definitive.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Take the first step towards medicine", "The entrance exam decides this application, and preparation typically takes 6 to 10 weeks. Let us look at your chemistry and biology background and build a preparation calendar around you. The consultation is free.")}

{related([(S['apply'],"Admissions","Admission requirements","Documents, language and the calendar."),
          (S['costs'],"Costs","Tuition and living costs","Why medicine sits above the usual range."),
          (S['unis'],"Universities","Medical faculties","Semmelweis, Pécs and Szeged.")])}
</article>
</div>'''

write(S['medicine'], page(
    S['medicine'],
    'Studying Medicine in Hungary: Entrance Exam and Fees (2026) | Hun Education',
    'Medicine in Hungary for international students: the three universities that teach it, real annual '
    'fees from €15,800 to $19,900, the entrance assessment and what recognition requires afterwards.',
    'Medicine guide',
    'Studying medicine in Hungary',
    'Six years, taught in English, at three universities. What the entrance assessment asks, how the '
    'years are structured and what the whole thing really costs.',
    body_med, S['medicine'],
    [HOME, ('Medicine', url_of('medicine'))],
    qa_med))

# =====================================================================
# PILOT TRAINING  ->  /pilot-training-at-hungarian-universities/
# =====================================================================
qa_pilot = [
    ("What licence does the programme lead to?",
     "<p>The BSc in professional pilot training combines an academic degree with flight training toward "
     "a commercial pilot licence. The exact licence, ratings and hour count are set by the university and "
     "the aviation authority, and they change; confirm the current structure with the university before "
     "you commit.</p>"),
    ("What does the fee cover?",
     "<p>The annual fee covers the academic programme and the flight training that goes with it, which is "
     "why pilot training costs several times what an engineering degree does. Ask the university for a "
     "written breakdown before you commit: what is included, and what you pay separately.</p>"),
    ("What medical certificate is required?",
     "<p>A Class 1 aeromedical certificate, which must be obtained from an approved examiner. Get it "
     "assessed before you apply, not after: it is the single most common reason a pilot application "
     "stops.</p>"),
]

body_pilot = f'''<div class="alayout">
{toc([('why','Why train in Hungary?'),('where','Where it is taught'),
      ('cost','How the cost is built'),('requirements','Requirements before you apply'),
      ('faq','Frequently asked questions'),('sources','Sources')])}

<article class="prose">

<section id="short-answer" class="answer">
  <span class="answer__label">Short answer</span>
  <p>Two Hungarian universities run pilot training in English, and they are priced very differently.
  The Budapest University of Technology and Economics offers a <b>Professional Pilot</b> programme at
  <b>€29,500 a year</b> over 7 semesters. The University of Dunaújváros combines pilot training to ATPL
  with mechanical engineering at <b>€66,800 a year</b>, also over 7 semesters. Both figures are annual
  tuition, and both include the flight training that makes this the most expensive programme in the
  catalogue.</p>
</section>
{figure('pilotaj-hangar-egitim-ucagi',
        'A student in flight uniform and high-visibility vest in front of a twin-engine training aircraft in a hangar',
        'One of our students on the pilot training programme, in front of a training aircraft.',
        oncelik=True)}

<h2 id="why">Why train in Hungary?</h2>
<p>A would-be pilot usually has three routes open: an airline cadet programme, a university aviation
degree, or a private flight school. Each carries a cost of its own. Cadet programmes tie you to a long
contract, and flight schools charge a high fee for a licence alone, leaving you without a degree.</p>

<p>Hungary's difference sits exactly there. The flight training runs inside an integrated degree, so
ground school and flight hours advance on the same calendar and you graduate holding both a commercial
pilot licence and a university degree. If a medical certificate is ever not renewed, the academic
qualification still stands, which matters in a profession built on periodic medical checks.</p>

<p>Add to that teaching entirely in English and living costs below Western Europe, and it becomes clear
why the country takes in more international pilot students every year.</p>
{strip('Scenes from pilot training', [
 ('pilotaj-ogrenci-pervane',
  'A student in pilot uniform beside the propeller of a single-engine training aircraft',
  'First hours on a single-engine trainer.'),
 ('pilotaj-ogrenciler-hangara-giderken',
  'A group of students in high-visibility vests walking across grass towards an aircraft hangar',
  'Flying day: students heading to the hangar.'),
 ('pilotaj-derslik-uniformali',
  'A group of students in pilot uniform at their desks in a classroom',
  'A theory class.'),
 ('pilotaj-apron-gun-batimi',
  'An airport apron at sunset with an airliner at the jet bridge',
  'Commercial aviation: the goal after licensing.'),
 ('pilotaj-ogrenciler-pist',
  'Three students in pilot shirts together at the airfield',
  'Our students at the airfield.'),
])}

<h2 id="where">Where it is taught</h2>
<p>Two universities, two different propositions. <b>BME</b> in Budapest runs a Professional Pilot
programme; the <b>University of Dunaújváros (UOD)</b> runs a combined track that takes you from zero to
an ATPL alongside a mechanical engineering degree, which is why its fee is more than double. UOD sits
south of Budapest on the Danube and has a markedly lower cost of living than the capital.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Aviation programmes and their annual tuition</caption>
  <thead><tr><th>Programme</th><th>University</th><th>Duration</th><th>Annual fee</th></tr></thead>
  <tbody>
    <tr><td><b>Professional Pilot</b></td><td>BME, Budapest</td><td>7 semesters</td><td class="num">€29,500</td></tr>
    <tr><td><b>Pilot Training (0 to ATPL) + Mechanical Engineering</b></td><td>UOD, Dunaújváros</td><td>7 semesters</td><td class="num">€66,800</td></tr>
    <tr><td>BSc Mechanical Engineering <i>(no flight training)</i></td><td>UOD, Dunaújváros</td><td>7 semesters</td><td class="num">€3,950</td></tr>
  </tbody>
</table>
</div>
<p>The third row is there for scale: the same engineering degree without flight training costs €3,950 a
year. The difference is the flying.</p>

<h2 id="cost">How the cost is built</h2>
{figure('pilotaj-ucak-motoru',
        'The engine and wing of an airliner on the apron under a cloudy sky',
        'Flight hours drive the cost more than anything else.')}
<p>Pilot training is the one programme in our catalogue where the headline fee needs unpacking, because
it is not a tuition figure in the ordinary sense.</p>
<div class="tablewrap">
<table class="dtable">
  <caption>What the term fee covers</caption>
  <thead><tr><th>Component</th><th>How it is charged</th><th>Note</th></tr></thead>
  <tbody>
    <tr><td><b>Ground school</b></td><td>Included in the annual tuition</td><td>Theory, simulators, examinations</td></tr>
    <tr><td><b>Flight hours</b></td><td>Included in the annual tuition</td><td>The reason the fee is 7 to 17 times a normal engineering degree</td></tr>
    <tr><td><b>Aeromedical certificate</b></td><td>One-off, before admission</td><td>Renewed periodically during training</td></tr>
    <tr><td><b>Living costs</b></td><td>Monthly</td><td>Lower in Dunaújváros than Budapest</td></tr>
  </tbody>
</table>
</div>
<p>Getting a written breakdown of what the fee covers is a standard step in this application: how
many flight hours are included, what happens if you need more, and whether the aeromedical certificate
and its renewals sit inside the tuition. We request it on your behalf, so you compare the two
universities on the same terms.</p>
{inline_cta("Let us put the two programmes side by side and pick the one that fits your budget.")}

<h2 id="requirements">What to arrange before you apply</h2>
{figure('budapeste-koprude-ogrenciler',
        'Two students on Liberty Bridge in Budapest',
        'Our students on Liberty Bridge.')}
<ol class="steps">
  <li><div><h3>Class 1 aeromedical certificate</h3><p>Obtained from an approved examiner. Have it assessed first: it is the most common point at which a pilot application stops.</p></div></li>
  <li><div><h3>English proficiency</h3><p>Assessed for the degree and, separately, for aviation radio communication.</p></div></li>
  <li><div><h3>Aptitude evaluation</h3><p>Set by the university, covering the coordination and situational judgement the training assumes.</p></div></li>
  <li><div><h3>Academic file</h3><p>Apostilled diploma, transcript, passport, English CV and a six-month bank statement, as for any programme.</p></div></li>
</ol>

<h3>Ground school and flight training</h3>
<p>The academic side covers aerodynamics, meteorology, navigation, air law and human performance, taught
and examined like any BSc. The flight side runs in parallel, moving from simulator time to supervised
flight and building the hours the licence requires. The two are scheduled together, which is why the
programme runs three and a half years rather than three.</p>

<h2 id="faq">Frequently asked questions</h2>
{faq_block(qa_pilot)}

<section id="sources" class="sources">
  <h2>Sources and verification</h2>
  <ol>
    <li>Programme structure and fees are compiled from the University of Dunaújváros' published conditions and reviewed each academic year.</li>
    <li>Licence structure, required hours and medical standards are set by the aviation authority and can change; the university's current documentation is definitive.</li>
    <li>Because flight hours are billed as flown, the programme total varies between students.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Your first step towards the cockpit", "We start with the Class 1 medical certificate. We will tell you what to arrange first and in what order, before any fee is paid. The consultation is free.")}

{related([(S['progs'],"Catalogue","Aviation programmes","Pilot training and aeronautical engineering."),
          (S['costs'],"Costs","How fees are charged","Per term, per year and the one-off charges."),
          (S['apply'],"Admissions","Admission requirements","Documents, language and the calendar.")])}
</article>
</div>'''

write(S['pilot'], page(
    S['pilot'],
    'Pilot Training in Hungary: Cost, Licence and Requirements | Hun Education',
    'Pilot training in Hungary at BME and the University of Dunaújváros: €29,500 and €66,800 a year, '
    'what the fee covers, and the Class 1 aeromedical certificate you need first.',
    'Pilot training',
    'Pilot training at Hungarian universities',
    'Two universities, two very different price tags. What the fee covers and what you need to arrange '
    'before you apply.',
    body_pilot, S['pilot'],
    [HOME, ('Pilot training', url_of('pilot'))],
    qa_pilot))
