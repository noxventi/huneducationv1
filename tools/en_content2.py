# -*- coding: utf-8 -*-
# gen_pages.py tarafindan exec edilir (LANG=en).

# =====================================================================
# 3) PILLAR. STUDY IN HUNGARY
# =====================================================================
qa_pillar = [
    ("What language are degrees taught in?",
     "<p>The overwhelming majority of programmes aimed at international students are taught in "
     "<b>English</b>. Hungarian is not required to apply; it is useful in daily life but it is not a "
     "requirement of the course.</p>"),
    ("Will my degree be recognised in my home country?",
     "<p>Recognition of a foreign degree is decided by the competent authority in your own country, and "
     "the criteria typically cover the university's recognised status, the content of the programme, "
     "the length of study and the graduation conditions. Some fields require an additional exam. "
     "Because the rules change, check your national authority's current regulations before you apply. "
     "<b>We make no claim of automatic or guaranteed recognition.</b></p>"),
    ("Can I work while studying?",
     "<p>The right to work on a student residence permit, its limits and its conditions are governed by "
     "Hungarian law and can change. Confirm the current rules from an official source before you build "
     "your plans around income from work.</p>"),
    ("Which city suits a student best?",
     "<p>Budapest offers the widest choice of programmes and the largest international community, but it "
     "is the most expensive city to live in. Debrecen, Szeged and Pécs offer comparable academic quality "
     "at a lower cost of living. The right choice depends on where your programme is offered and on your "
     "budget.</p>"),
]

body_pillar = f'''<div class="alayout">
{toc([('why','Why Hungary?'),('system','The system and degrees'),
      ('cities','Cities'),('visa','Visa and residence'),
      ('faq','Frequently asked questions'),('sources','Sources')])}

<article class="prose">

<section id="short-answer" class="answer">
  <span class="answer__label">Short answer</span>
  <p>Hungary is one of the most practical ways to study in English inside the EU and graduate with a
  degree that travels. <b>There is no national entrance exam</b>; universities run their own
  assessment. A bachelor's takes 3–4 years, a <a class="link" href="{S['masters']}">master's</a> 2 years, and integrated programmes such as <a class="link" href="{S['medicine']}">medicine</a> and dentistry 5–6 years, with tuition and living costs together at €8,500 – €14,000 a year.
  Our catalogue holds 490 English-taught programmes at 20 universities.</p>
</section>

<h2 id="why">Why Hungary?</h2>
{figure('budapeste-balikci-tabyasi',
        'A view of Budapest at sunrise through an arch of the Fisherman’s Bastion',
        'Budapest from the Fisherman’s Bastion.')}
{stats([('490', 'English-taught programmes'),
        ('20', 'Universities'),
        ('€8,500', 'Lower bound for one year'),
        ('No exam', 'The university assesses you itself')])}
<p>What makes Hungary stand out for international students is not a single advantage but several
factors working together:</p>
<ul>
  <li><b>A European degree on a measured budget.</b> Tuition and living costs noticeably below
  Western Europe.</li>
  <li><b>A broad English-taught catalogue.</b> Programmes open to international students from medicine
  to pilot training, engineering to the arts.</li>
  <li><b>A long university tradition.</b> The University of Pécs was founded in 1367, Semmelweis has
  trained physicians since 1769, and scientists of Hungarian origin have won 16 Nobel Prizes.</li>
  <li><b>A central location.</b> Vienna, Bratislava and Prague are a few hours away by road.</li>
  <li><b>An established international student community.</b> Around 40,000 international students
  study in Hungary, with strong support networks in Budapest, Debrecen and Pécs.</li>
</ul>

{strip('Scenes from Hungarian universities', [
 ('elte-tarihi-bina', 'The historic stone facade of ELTE', 'ELTE, Budapest.'),
 ('debrecen-ana-bina', 'The colonnaded main building of the University of Debrecen with its pool',
  'The main building in Debrecen.'),
 ('szeged-ana-bina', 'The yellow facade of the University of Szeged main building',
  'The University of Szeged.'),
 ('pecs-tas-kemer-giris', 'The stone archway entrance to a University of Pécs courtyard',
  'A courtyard entrance in Pécs.'),
 ('bme-tuna-kiyisi', 'A historic university building on the Danube bank with a boat on the river',
  'A university building on the Danube.'),
])}

<h2 id="system">The system and degrees</h2>
<p>Hungary uses a three-cycle structure aligned with the Bologna system. Fields such as medicine,
dentistry, pharmacy and architecture run as integrated (single-cycle) programmes.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Degree levels, duration and annual fee ranges</caption>
  <thead><tr><th>Level</th><th>Duration</th><th>Annual fee</th><th>Entry requirement</th></tr></thead>
  <tbody>
    <tr><td><b>Preparatory</b></td><td>1 year</td><td class="num">from €2,500 / year</td><td>University's own test</td></tr>
    <tr><td><b>Bachelor's</b></td><td>3 – 4 years</td><td class="num">€3,000 – €5,000</td><td>High school diploma · B2 English</td></tr>
    <tr><td><b>Master's</b></td><td>2 years</td><td class="num">€4,000 – €6,000</td><td>Bachelor's degree · university assessment</td></tr>
    <tr><td><b>Doctorate</b></td><td>3 – 4 years</td><td class="num">€6,000 – €8,000</td><td>Master's degree</td></tr>
    <tr><td><b>Integrated (medicine, dentistry)</b></td><td>5 – 6 years</td><td class="num">€15,800 – $19,900</td><td>Chemistry and biology entrance exam</td></tr>
  </tbody>
</table>
</div>

<h3>Language of instruction</h3>
<p>International programmes are taught in English; you do not need Hungarian to apply. Bachelor's
programmes expect at least B2, and some universities ask for IELTS 6.5 at master's level. Applicants without a
certificate can apply to the universities' English Language Foundation programme.</p>
<p>Hungarian is an advantage for daily life and internship opportunities; many universities offer
free or low-cost beginner Hungarian classes.</p>

<h2 id="cities">Which city should you choose?</h2>
{figure('pecs-sehir-hava',
        'An aerial view of the red rooftops of central Pécs',
        'Pécs. Living costs outside Budapest are markedly lower.')}
<p>Your choice of city matters as much as your choice of university: cost of living, transport and
the student community all vary from one to the next.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Main cities offering programmes</caption>
  <thead><tr><th>City</th><th>Region</th><th>Known for</th></tr></thead>
  <tbody>
    <tr><td><b>Budapest</b></td><td>Central Hungary</td><td>Widest choice of programmes · highest cost of living</td></tr>
    <tr><td><b>Debrecen</b></td><td>Eastern Hungary</td><td>Long tradition in health and engineering · over 130 programmes in the catalogue</td></tr>
    <tr><td><b>Szeged</b></td><td>Southern Hungary</td><td>Campus and city blended · lower cost</td></tr>
    <tr><td><b>Pécs</b></td><td>South-west</td><td>The country's oldest university · walkable city</td></tr>
    <tr><td><b>Miskolc</b></td><td>North-east</td><td>Engineering and earth sciences</td></tr>
    <tr><td><b>Dunaújváros</b></td><td>Central Hungary</td><td>Combined pilot training and engineering</td></tr>
    <tr><td><b>Nyíregyháza</b></td><td>North-east</td><td>Low cost of living</td></tr>
    <tr><td><b>Kecskemét</b></td><td>Central Hungary</td><td>Industry-linked engineering</td></tr>
  </tbody>
</table>
</div>

<h2 id="visa">Visa, residence and recognition</h2>
<p>International students enter Hungary on a <b>type D student visa</b>. The core document for the visa
application is the final Acceptance Letter from the university; a six-month bank statement, proof of
accommodation and health insurance are also required.</p>
<ol class="steps">
  <li><div><h3>Acceptance letter</h3><p>You receive the final acceptance from the university.</p></div></li>
  <li><div><h3>Consulate application</h3><p>You book an appointment at your nearest Hungarian consulate and submit the file.</p></div></li>
  <li><div><h3>Entering the country</h3><p>Once the visa is approved, travel is planned.</p></div></li>
  <li><div><h3>Residence registration</h3><p>The residence permit formalities are completed after arrival.</p></div></li>
</ol>
<p>We build the visa file for you: which document to prepare in what order, the appointment calendar
and the format the consulate expects. The decision is the consulate's, of course, but making sure the
file arrives complete is our job.</p>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Your protection: if the visa is refused, tuition is usually refunded within 30 working days once the
consulate’s written refusal reaches the university. Because the decision rests with an official
authority, no consultancy can guarantee a visa; treat any source that promises one with caution.</p>

<h3>Recognition and after graduation</h3>
<p>If you plan to use your degree in your home country, it will normally go through a recognition
process run by the national authority there. Recognition is assessed on the university's standing,
the content of the programme, the length of study and the graduation conditions; some fields require
an additional exam.</p>
<p>We do not leave this to the end: we go through the recognition points that matter while choosing
the programme, so nothing surprises you at graduation. Because the rules change, review your national
authority's current regulations before you apply as well; the decision is theirs, so we make no
commitment about the outcome.</p>

<h2 id="faq">Frequently asked questions</h2>
{faq_block(qa_pillar)}

<section id="sources" class="sources">
  <h2>Sources and verification</h2>
  <ol>
    <li>Degree durations and fee ranges are compiled from the universities' official publications; city information comes from the field experience of our teams in Budapest and Pécs.</li>
    <li>The binding source on recognition is your national authority's current regulation, and on visas the relevant consulate.</li>
    <li>Students' right to work is governed by Hungarian law and can change.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Start your Hungarian degree today", "Tell us about your academic background and your goal, and we will name 3–5 realistic programmes in the first conversation. The consultation is free; what happens next is up to you.")}

{related([(S['unis'],"Universities","20 universities","The full list with city, type and fields."),
          (S['apply'],"Admissions","Admission requirements","Documents, language, entrance exams and the calendar."),
          (S['costs'],"Costs","Fees and living costs","The realistic annual budget range.")])}
</article>
</div>'''

write(S['edu'], page(
    S['edu'],
    'Study in Hungary: System, Cities, Tuition Fees (2026) | Hun Education',
    "A guide to studying at a university in Hungary: degree levels and durations, language of "
    "instruction, cities, annual cost, the type D student visa and degree recognition.",
    'Main guide',
    'Study at a university in Hungary',
    'How the system works, what each city offers, what it costs and what the degree means when you '
    'go home, everything you need before you decide.',
    body_pillar, S['edu'],
    [HOME, ('Study in Hungary', url_of('edu'))],
    qa_pillar))

# =====================================================================
# 4) UNIVERSITIES
# =====================================================================
rows = '\n'.join(
    '    <tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td><td><a href="%s?uni=%s">Programmes</a></td></tr>'
    % (u['ad'], u['sehir'], u['tur'], ' · '.join(u['alanlar'][:3]), S['progs'], u['id'])
    for u in sorted(UNIS, key=lambda x: (x['sehir'] == '—', x['sehir'], x['ad'])))

by_city = {}
for u in UNIS:
    by_city.setdefault(u['sehir'], []).append(u['ad'])
city_list = '\n'.join(
    '  <li><b>%s</b>: %s</li>' % (c, ', '.join(v))
    for c, v in sorted(by_city.items(), key=lambda kv: (kv[0] == '—', -len(kv[1]))))

qa_uni = [
    ("Which university can I apply to?",
     "<p>It depends on your qualification, your English level, the field you choose and your budget. "
     "The same subject can be offered at several universities with different admission conditions. "
     "Start by filtering the programme catalogue.</p>"),
    ("What is the difference between a state and a private university?",
     "<p>State universities are generally older and offer a wider range of programmes. Private and "
     "foundation universities can offer smaller classes, industry-linked programmes and more flexible "
     "intakes. What matters for the validity of the degree is the institution's recognised status, "
     "not whether it is state or private.</p>"),
    ("Can I apply to more than one university at the same time?",
     "<p>Yes, and we recommend it. Places can close mid-intake, so carrying more than one option "
     "lowers the risk. Bear in mind that each university has its own application fee.</p>"),
]

body_uni = f'''<div class="alayout">
{toc([('list','University list'),('by-city','Distribution by city'),
      ('choosing','How to choose'),('faq','Frequently asked questions'),('sources','Sources')])}

<article class="prose">

<section id="short-answer" class="answer">
  <span class="answer__label">Short answer</span>
  <p>You can apply to <b>{len(UNIS)} universities</b> in Hungary through Hun Education, spread across eight
  cities. The widest choice of programmes is in Budapest, while Debrecen, Szeged and Pécs offer
  comparable academic quality at a lower cost of living. Across the whole list the catalogue holds
  <b>{sum(u["programSayisi"] for u in UNIS)} English-taught programmes</b>, from preparatory years to medicine and pilot training.</p>
</section>

<h2 id="list">University list</h2>
{galeri([
 ('pecs-universitesi-tabela',
  'A University of Pécs building with the “University of Pécs” sign at the entrance',
  'University of Pécs', 'The country’s oldest university; medicine, dentistry and pharmacy.'),
 ('debrecen-cam-bina',
  'A glass-fronted modern building at the University of Debrecen',
  'University of Debrecen', 'A long tradition in health sciences and engineering.'),
 ('elte-avlu', 'The arcaded inner courtyard at ELTE',
  'ELTE', 'Humanities, social sciences and psychology.'),
 ('szeged-modern-bina', 'A glass-fronted modern building at the University of Szeged',
  'University of Szeged', 'Medicine and sciences; low cost of living.'),
 ('miskolc-cam-bina', 'The glass-fronted building and forecourt at the University of Miskolc',
  'University of Miskolc', 'Engineering and earth sciences.'),
 ('obuda-sari-bina', 'The yellow historic building of Óbuda University',
  'Óbuda University', 'Engineering and IT in Budapest.'),
 ('metu-bina-tabela', 'The round campus building signed “Budapesti Metropolitan Egyetem”',
  'Budapest Metropolitan', 'Design, media and business.'),
 ('univet-avlu-heykeller',
  'The courtyard of the University of Veterinary Medicine, with dog statues on either side',
  'Veterinary Medicine', 'Veterinary training in Budapest.'),
 ('corvinus-bina', 'The modern glass and stone facade of Corvinus University',
  'Corvinus University', 'Business and economics.'),
])}
<p>The table below is ordered by city. The “leading fields” column shows the main fields for which we
hold programmes at that university in our catalogue; it is not the institution's full faculty
structure.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Universities you can apply to through Hun Education</caption>
  <thead><tr><th>University</th><th>City</th><th>Type</th><th>Leading fields</th><th>Catalogue</th></tr></thead>
  <tbody>
{rows}
  </tbody>
</table>
</div>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
This list is not a statement of partnership or representation; it shows the institutions we can
submit applications to.</p>

<h2 id="by-city">Distribution by city</h2>
{strip('Scenes from the university cities', [
 ('miskolc-kampus-hava', 'An aerial panorama of the University of Miskolc campus in autumn',
  'The Miskolc campus in autumn.'),
 ('debrecen-kuleli-bina', 'The towered building of the University of Debrecen',
  'A campus in Debrecen.'),
 ('pecs-sonbahar-kampus', 'A University of Pécs building among autumn trees',
  'Autumn in Pécs.'),
 ('elte-gece-cephe', 'The ELTE facade lit at night', 'An evening in Budapest.'),
])}
<ul>
{city_list}
</ul>

<h2 id="choosing">How to choose</h2>
{figure('pecs-kampus-hava',
        'An aerial view of the University of Pécs campus',
        'The University of Pécs campus from the air.')}
<ol class="steps">
  <li><div><h3>Fix the subject first</h3><p>You choose a programme, not a university. Once you know the subject, comparing the universities that offer it becomes meaningful.</p></div></li>
  <li><div><h3>Check the admission conditions</h3><p>Entrance exams, language scores and portfolio requirements differ from institution to institution.</p></div></li>
  <li><div><h3>Think about the city and the budget together</h3><p>A city with low tuition but high rent can cost more in total.</p></div></li>
  <li><div><h3>Carry more than one option</h3><p>Apply to at least two universities in case places close.</p></div></li>
</ol>

<h2 id="faq">Frequently asked questions</h2>
{faq_block(qa_uni)}

<section id="sources" class="sources">
  <h2>Sources and verification</h2>
  <ol>
    <li>The list reflects the current scope of the applications we handle and is reviewed before every application period.</li>
    <li>Programmes, fees and admission conditions may be changed by the universities.</li>
    <li>The university's official page is definitive for final information.</li>
  </ol>
  {CHANGELOG}
</section>

{acta("Which university fits you?", "Let us put the universities that match your profile side by side, with their admission conditions, fees and cities.")}

{related([(S['progs'],"Catalogue","Programme catalogue","Filter and compare 490 programmes."),
          (S['costs'],"Costs","Fees by university","ELTE, Debrecen and Pécs compared."),
          (S['apply'],"Admissions","Admission requirements","Documents, exams and the calendar.")])}
</article>
</div>'''

write(S['unis'], page(
    S['unis'],
    'Universities in Hungary: 20 Universities by City | Hun Education',
    "The universities in Hungary you can apply to, with city, type and leading fields. Options in "
    "Budapest, Debrecen, Szeged, Pécs and other cities.",
    'University guide',
    'Universities in Hungary',
    'Which university is in which city, and what fields does it offer? The full list, gathered in one '
    'comparable table.',
    body_uni, S['unis'],
    [HOME, ('Universities', url_of('unis'))],
    qa_uni))
