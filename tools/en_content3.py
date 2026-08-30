# -*- coding: utf-8 -*-
# gen_pages.py tarafindan exec edilir (LANG=en).

# =====================================================================
# 5) ABOUT US
# =====================================================================
qa_about = [
    ("When was Hun Education founded?",
     "<p>Hun Education has been providing Hungary-focused academic consultancy since 1999 and was the "
     "first Turkish education consultancy established in Hungary. The head office is in Budapest.</p>"),
    ("Is the consultancy fee included in the tuition fee?",
     "<p>No. The consultancy fee and the tuition you pay to the university are separate and are stated "
     "separately. We put in writing which services are covered before you commit to anything.</p>"),
    ("Does support continue after the student arrives in Hungary?",
     "<p>Yes. The Budapest head office is with you through airport pick-up, residence registration, "
     "university enrolment and settling into the city. You can reach the same adviser throughout your "
     "studies.</p>"),
]

body_about = f'''<div class="alayout">
{toc([('short-answer','Short answer'),('story','Then and now'),('how','How we work'),
      ('principles','Our publishing and data principles'),('offices','Offices'),('faq','Frequently asked questions')])}

<article class="prose">

<section id="short-answer" class="answer">
  <span class="answer__label">Short answer</span>
  <p>Hun Education is an academic consultancy that has focused on one country, Hungary, since 1999,
  and was the first Turkish education consultancy in the country. The head office is in Budapest, with
  representatives in Ankara, Istanbul, Izmir, Bursa and Pécs. Our scope runs from choosing a programme
  to applying, and from the visa to accommodation and settling into your city.</p>
</section>

<h2 id="story">Then and now</h2>
{strip('Scenes from our students', [
 ('pilotaj-ogrenciler-pist', 'Three students in pilot shirts together at the airfield',
  'Our pilot students at the airfield.'),
 ('budapeste-koprude-ogrenciler', 'Two students on Liberty Bridge in Budapest',
  'Our students on Liberty Bridge.'),
 ('pilotaj-fuar-standi', 'Two students in uniform in front of a pilot academy exhibition stand',
  'Our students at an aviation fair.'),
 ('metu-ogrenci-grubu', 'A group of international students gathered in a campus garden',
  'International students on campus.'),
 ('obuda-ogrenciler', 'A group of students on a bench under the Óbuda University sign',
  'Between classes.'),
])}
<p>Hun Education began in 1999 out of a need for consultancy that concentrated on a single country for
students who wanted to study in Hungary. We still work with the same focus: we do not follow ten
countries at once, only Hungary.</p>
<p>What that choice means in practice: we know which university asks for what in which intake, which
programme's interview has become harder, and which way rents are moving in which city, not from a
general study-abroad brochure, but from working in the same country every year.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Company details</caption>
  <thead><tr><th>Field</th><th>Detail</th></tr></thead>
  <tbody>
    <tr><td><b>Registered name</b></td><td>HUN EDUCATION KFT.</td></tr>
    <tr><td><b>Operating since</b></td><td class="num">1999</td></tr>
    <tr><td><b>Head office</b></td><td>1204 Budapest, Bethlen utca 17, Hungary</td></tr>
    <tr><td><b>Representatives in Türkiye</b></td><td>Ankara · Istanbul (Kadıköy) · Izmir · Bursa</td></tr>
    <tr><td><b>Representative in Hungary</b></td><td>Pécs</td></tr>
    <tr><td><b>Focus</b></td><td>Hungary only</td></tr>
  </tbody>
</table>
</div>

<h2 id="how">How we work</h2>
{figure('debrecen-ana-bina',
        'The colonnaded main building of the University of Debrecen with its pool',
        'The main building in Debrecen.')}
<ol class="steps">
  <li><div><h3>One adviser, one file</h3><p>Every applicant is assigned to an adviser. You speak to the same person throughout, so you never have to start the story over.</p></div></li>
  <li><div><h3>We explain the options we rule out</h3><p>We tell you not only which programmes suit you, but why a particular programme was ruled out.</p></div></li>
  <li><div><h3>Scope in writing, up front</h3><p>Which services are included, when they begin, and the fact that the consultancy fee is separate from tuition, all clear before the consultation.</p></div></li>
  <li><div><h3>It does not end at the airport</h3><p>Airport pick-up, residence registration and enrolment week are handled by the Budapest team.</p></div></li>
</ol>

<h2 id="principles">Our publishing and data principles</h2>
<p>The most common problem in the study-abroad field is old information presented as current. The
rules we apply on this site:</p>
<ul>
  <li><b>Every fee carries its currency and its period.</b> Whether it is annual or per term is stated explicitly.</li>
  <li><b>The source and the update date are visible.</b> Guide pages carry a source list and a change log at the bottom.</li>
  <li><b>We do not use the language of guarantees.</b> Admission rests with the university, the visa with the consulate, and recognition with your national authority.</li>
  <li><b>We do not publish unverified numbers.</b> We leave out unprovable claims such as acceptance rates or success percentages.</li>
  <li><b>Student experiences are real.</b> We do not use anonymous or invented testimonials.</li>
</ul>

<h2 id="offices">Offices</h2>
<div class="tablewrap">
<table class="dtable">
  <caption>Offices and representatives</caption>
  <thead><tr><th>Location</th><th>Address</th></tr></thead>
  <tbody>
    <tr><td><b>Budapest (head office)</b></td><td>1204 Budapest, Bethlen utca 17, Hungary</td></tr>
    <tr><td><b>Ankara</b></td><td>Kızılay Mah. Menekşe 2 Cad. No: 33/5, Çankaya</td></tr>
    <tr><td><b>Istanbul</b></td><td>Osmanağa Mah. Vahap Bey Sok. No: 10 D: 13, Kadıköy</td></tr>
    <tr><td><b>Izmir</b></td><td>Kıbrıs Şehitleri Cad. Can Yücel Sok. No: 13/4 D: 7, Alsancak</td></tr>
    <tr><td><b>Bursa</b></td><td>Özlüce Bulvarı, Öndül Elite Offices B Blok K: 6 D: 77, Nilüfer</td></tr>
    <tr><td><b>Pécs</b></td><td>Regional representative</td></tr>
  </tbody>
</table>
</div>

<h2 id="faq">Frequently asked questions</h2>
{faq_block(qa_about)}

{acta("Let us meet", "The first consultation is free and commits you to nothing. Let us go through your academic record and your goals together.")}

{related([(S['contact'],"Contact","Get in touch","Offices, phone, email and the form."),
          (S['edu'],"Guide","Study in Hungary","The system, the cities, visas and recognition."),
          (S['progs'],"Catalogue","Programme catalogue","Filter and compare 490 programmes.")])}
</article>
</div>'''

write(S['about'], page(
    S['about'],
    'About Us: Hungary-Focused Consultancy Since 1999 | Hun Education',
    "Hun Education has focused solely on Hungary since 1999. Our Budapest head office, representatives "
    "in Türkiye, how we work and the principles behind what we publish.",
    'About us',
    'Hungary only. Since 1999.',
    'We do not follow ten countries at once. We work from knowledge built by learning one country '
    'again every year, and we tell you what we do not know.',
    body_about, S['about'],
    [HOME, ('About Us', url_of('about'))],
    qa_about))

# =====================================================================
# 6) CONTACT
# =====================================================================
ADVISERS = [
    ('Beyza Kantarcı', 'Budapest · Head office', 'Preparatory, bachelor’s, master’s'),
    ('Veli Çınaroğlu', 'Pécs · Hungary representative', 'Preparatory, bachelor’s, master’s'),
    ('Çağla Nur Türken', 'Debrecen · Nyíregyháza', 'Preparatory, bachelor’s, master’s'),
    ('Hacer Çakmak', 'Budapest', 'Preparatory, bachelor’s, master’s'),
    ('Nesrin Ertaş', 'Ankara', 'Preparatory, bachelor’s, master’s'),
    ('Funda Toksoy', 'Ankara', 'Preparatory, bachelor’s, master’s'),
    ('Orkun Tokdemir', 'Istanbul · Kadıköy', 'Preparatory, bachelor’s, master’s'),
    ('Nur Alpay', 'Izmir', 'Preparatory, bachelor’s, master’s'),
    ('Figen Durmaz', 'Bursa', 'Preparatory, bachelor’s, master’s'),
    ('Deniz Hızal', 'Çanakkale', 'Preparatory, bachelor’s, master’s'),
    ('Ali Yalçın', 'Denizli', 'Preparatory, bachelor’s, master’s'),
]
adv_rows = '\n'.join(
    '    <tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % d for d in ADVISERS)

body_contact = f'''<div class="alayout">
{toc([('form','Request a consultation'),('channels','Contact channels'),('offices','Offices'),
      ('team','The advisory team'),('response','When we get back to you')])}

<article class="prose">

<section id="form">
  <h2 style="margin-top:0">Request a free consultation</h2>
  <p>Fill in the form and we will route you to the right adviser. The first consultation is free and
  commits you to nothing.</p>

  <form class="final__form" style="box-shadow:var(--sh-2);border:1px solid var(--line);margin-top:1.2rem" novalidate data-lead-form>
    <div class="final__row">
      <label class="field">
        <span class="field__label">Full name <span class="field__req" aria-hidden="true">*</span></span>
        <input class="field__ctl" name="ad" type="text" autocomplete="name" required aria-describedby="err-ad">
        <span class="field__err" id="err-ad" role="alert"></span>
      </label>
      <label class="field">
        <span class="field__label">Phone <span class="field__req" aria-hidden="true">*</span></span>
        <input class="field__ctl" name="tel" type="tel" inputmode="tel" placeholder="+44 7700 900000" autocomplete="tel" required aria-describedby="err-tel">
        <span class="field__err" id="err-tel" role="alert"></span>
      </label>
    </div>
    <div class="final__row">
      <label class="field">
        <span class="field__label">Email <span class="field__req" aria-hidden="true">*</span></span>
        <input class="field__ctl" name="eposta" type="email" autocomplete="email" required aria-describedby="err-eposta">
        <span class="field__err" id="err-eposta" role="alert"></span>
      </label>
      <label class="field">
        <span class="field__label">Level you are interested in</span>
        <select class="field__ctl" name="seviye">
          <option value="">Please choose</option><option>Foundation</option><option>Bachelor&rsquo;s</option>
          <option>Master&rsquo;s</option><option>Medicine / dentistry / pharmacy</option><option>Pilot training</option>
          <option>Not sure yet</option>
        </select>
      </label>
    </div>
    <label class="field">
      <span class="field__label">Your message <span class="field__hint" style="display:inline">(optional)</span></span>
      <textarea class="field__ctl" name="mesaj" rows="3" placeholder="Which subject are you considering, and which intake would you like to start in?"></textarea>
    </label>
    <label class="check">
      <input type="checkbox" name="kvkk" required>
      <span>I consent to my personal data being processed in order to assess my consultation request.
        <a href="{S['privacy']}" target="_blank" rel="noopener">Privacy Notice</a></span>
    </label>
    <span class="field__err" id="err-kvkk" role="alert"></span>
    <button class="btn btn--primary btn--lg final__submit" type="submit" data-magnetic>
      <span class="btn__label"><span data-t="Book a Free Consultation">Book a Free Consultation</span></span>
    </button>
    <input type="hidden" name="ilk_kaynak"><input type="hidden" name="son_kaynak">
    <input type="hidden" name="giris_sayfasi"><input type="hidden" name="lead_sayfasi">
    <input type="hidden" name="ilgi_program"><input type="hidden" name="gclid">
    <div class="final__done" data-form-done hidden role="status">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>
      <h3>We have your request</h3>
      <p>An adviser will come back to you during working hours. If you prefer, you can carry on the conversation on WhatsApp right away.</p>
      <a class="btn btn--wa" href="https://wa.me/" data-wa><span class="btn__label"><span data-t="Continue on WhatsApp">Continue on WhatsApp</span></span></a>
    </div>
  </form>
</section>

<h2 id="channels">Contact channels</h2>
{strip('Scenes from our students', [
 ('budapeste-koprude-ogrenciler', 'Two students on Liberty Bridge in Budapest',
  'Our students on Liberty Bridge.'),
 ('pilotaj-fuar-standi', 'Two students in uniform in front of a pilot academy exhibition stand',
  'Our students at an aviation fair.'),
 ('metu-ogrenci-grubu', 'A group of international students gathered in a campus garden',
  'International students on campus.'),
 ('obuda-ogrenciler', 'A group of students on a bench under the Óbuda University sign',
  'Between classes.'),
])}
<div class="tablewrap">
<table class="dtable">
  <caption>Direct contact</caption>
  <thead><tr><th>Channel</th><th>Detail</th><th>When</th></tr></thead>
  <tbody>
    <tr><td><b>Phone</b></td><td class="num"><a href="tel:+36702963531">+36 70 296 35 31</a></td><td>Monday – Friday · 09:00 – 18:00 CET</td></tr>
    <tr><td><b>Email</b></td><td><a href="mailto:info@huneducation.com">info@huneducation.com</a></td><td>Any time</td></tr>
    <tr><td><b>WhatsApp</b></td><td><a href="https://wa.me/" data-wa>Send a message</a></td><td>Replies during working hours</td></tr>
  </tbody>
</table>
</div>

<h2 id="offices">Offices</h2>
<div class="tablewrap">
<table class="dtable">
  <caption>Offices and representatives</caption>
  <thead><tr><th>Location</th><th>Address</th></tr></thead>
  <tbody>
    <tr><td><b>Budapest (head office)</b></td><td>1204 Budapest, Bethlen utca 17, Hungary</td></tr>
    <tr><td><b>Ankara</b></td><td>Kızılay Mah. Menekşe 2 Cad. No: 33/5, Çankaya</td></tr>
    <tr><td><b>Istanbul</b></td><td>Osmanağa Mah. Vahap Bey Sok. No: 10 D: 13, Kadıköy</td></tr>
    <tr><td><b>Izmir</b></td><td>Kıbrıs Şehitleri Cad. Can Yücel Sok. No: 13/4 D: 7, Alsancak</td></tr>
    <tr><td><b>Bursa</b></td><td>Özlüce Bulvarı, Öndül Elite Offices B Blok K: 6 D: 77, Nilüfer</td></tr>
  </tbody>
</table>
</div>

<h2 id="team">The advisory team</h2>
<p>Your request is routed to one of the advisers below, based on the level you are aiming for and
where you are.</p>
<div class="tablewrap">
<table class="dtable">
  <caption>Advisers and the regions they cover</caption>
  <thead><tr><th>Adviser</th><th>Region</th><th>Specialism</th></tr></thead>
  <tbody>
{adv_rows}
  </tbody>
</table>
</div>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Each adviser has a direct phone number and email address, so you can reach the right person without
going through a queue. Ask us and we will point you to the adviser who covers your level and your
city.</p>

<h2 id="response">When we get back to you</h2>
<p>Our working hours are <b>Monday – Friday, 09:00 – 18:00</b> Central European Time. Requests that
arrive outside those hours are handled on the next working day. Response times can lengthen during
the busy application months of April–June and October–November; for urgent matters WhatsApp is the
fastest channel.</p>

{acta("Write your question and we will call you", "The form takes a minute. Let us work out together which programme suits you.")}
</article>
</div>'''

write(S['contact'], page(
    S['contact'],
    'Contact: Free Consultation | Hun Education',
    "Get in touch with Hun Education: Budapest head office, representatives in Ankara, Istanbul, Izmir "
    "and Bursa, phone, WhatsApp and the free consultation form.",
    'Contact',
    'Let us start with a conversation',
    'The first consultation is free and commits you to nothing. Fill in the form or call us directly, '
    'and we will route your request to the right adviser.',
    body_contact, S['contact'],
    [HOME, ('Contact', url_of('contact'))],
    None,
    extra_css='\n<link rel="stylesheet" href="%sassets/css/catalog.css">' % A))
