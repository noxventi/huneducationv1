# -*- coding: utf-8 -*-
# Yasal sayfalarin Ingilizce surumu.
#
# Cerceve farki bilinclidir: Turkce sayfa KVKK'yi one alir, Ingilizce sayfa
# GDPR'i one alir. Sirket Macaristan'da yerlesik oldugu icin birincil rejim
# GDPR; KVKK yalnizca Turkiye'den basvuran adaylar icin ayrica anilir.
# Yayin oncesi hukuk danismani onayi gerekir (README'de isaretli).

# =====================================================================
# 1) PRIVACY NOTICE
# =====================================================================
body_privacy = f'''<div class="alayout">
{toc([('controller','Data controller'),('data','Personal data we process'),('purposes','Purposes of processing'),
      ('legal-basis','Legal bases'),('collection','How we collect it'),('transfers','Transfers'),
      ('retention','Retention periods'),('rights','Your rights'),('requests','How to make a request')])}

<article class="prose">

<p>This notice is issued under Article 13 of the EU General Data Protection Regulation (“GDPR”) and,
for applicants resident in Türkiye, Article 10 of Turkish Law No. 6698 on the Protection of Personal
Data (“KVKK”). It explains what personal data we process, for what purpose and on what legal basis,
and what rights you have. Our company is established in Hungary, so your data is protected under the
GDPR in every case.</p>

<h2 id="controller">Data controller</h2>
<div class="tablewrap">
<table class="dtable">
  <tbody>
    <tr><td><b>Registered name</b></td><td>HUN EDUCATION KFT.</td></tr>
    <tr><td><b>Address</b></td><td>1204 Budapest, Bethlen utca 17, Hungary</td></tr>
    <tr><td><b>Email</b></td><td>info@huneducation.com</td></tr>
    <tr><td><b>Phone</b></td><td class="num">+36 70 296 35 31</td></tr>
  </tbody>
</table>
</div>

<h2 id="data">Personal data we process</h2>
<div class="tablewrap">
<table class="dtable">
  <thead><tr><th>Category</th><th>Examples</th><th>When it is collected</th></tr></thead>
  <tbody>
    <tr><td><b>Identity</b></td><td>First name, surname, date of birth, passport details</td><td>Consultation and application</td></tr>
    <tr><td><b>Contact</b></td><td>Phone, email, address</td><td>Form submission</td></tr>
    <tr><td><b>Education</b></td><td>Diploma, transcript, language certificate, CV</td><td>Preparing the application file</td></tr>
    <tr><td><b>Financial</b></td><td>Bank statement (for the visa file only)</td><td>Visa preparation</td></tr>
    <tr><td><b>Health</b><i> (special category)</i></td><td>Medical report (only where pilot training or insurance requires it, with explicit consent)</td><td>The relevant application stage</td></tr>
    <tr><td><b>Transaction security</b></td><td>Form submission record, first referral source on the site (UTM)</td><td>Site usage</td></tr>
    <tr><td><b>Images and recordings</b></td><td>Photograph, video (only with separate written permission)</td><td>Publishing a student story</td></tr>
  </tbody>
</table>
</div>

<h2 id="purposes">Purposes of processing</h2>
<ul>
  <li>Assessing your free consultation request and getting back to you</li>
  <li>Identifying suitable universities and programmes, preparing and submitting your application file</li>
  <li>Running and following up the admission, enrolment, visa and accommodation processes</li>
  <li>Providing arrival support, residence registration and enrolment help in Hungary</li>
  <li>Meeting legal obligations and providing evidence in the event of a dispute</li>
  <li>Marketing and information communications, where you have given consent</li>
</ul>

<h2 id="legal-basis">Legal bases</h2>
<div class="tablewrap">
<table class="dtable">
  <thead><tr><th>Basis</th><th>Reference</th><th>Scope</th></tr></thead>
  <tbody>
    <tr><td><b>Performance of a contract</b></td><td>GDPR Art. 6(1)(b) · KVKK Art. 5/2-c</td><td>Delivering the consultancy service, application and visa processes</td></tr>
    <tr><td><b>Legal obligation</b></td><td>GDPR Art. 6(1)(c) · KVKK Art. 5/2-ç</td><td>Accounting and statutory records</td></tr>
    <tr><td><b>Legitimate interests</b></td><td>GDPR Art. 6(1)(f) · KVKK Art. 5/2-f</td><td>Service quality, communication records, fraud prevention</td></tr>
    <tr><td><b>Consent</b></td><td>GDPR Art. 6(1)(a), Art. 9(2)(a) · KVKK Art. 5/1, 6, 9</td><td>Health data, international transfers, marketing communications, publishing photographs and video</td></tr>
  </tbody>
</table>
</div>

<h2 id="collection">How we collect it</h2>
<p>Your data is collected through the forms on this website, by email, telephone and WhatsApp
correspondence, in face-to-face meetings at our offices and from the documents you send us, by partly
automated and non-automated means. The storage technologies used by this site are explained in the
<a href="{S['cookies']}">Cookie Policy</a>.</p>

<h2 id="transfers">Transfers</h2>
<p>Your personal data is shared only to the extent necessary for the purposes above, with:</p>
<ul>
  <li><b>The Hungarian universities you apply to</b>: to submit your application file</li>
  <li><b>Hungarian consulates and official authorities</b>: for visa and residence procedures</li>
  <li><b>Accommodation providers</b>: for dormitory or rental applications, at your request</li>
  <li><b>Our service providers</b>: hosting, email and CRM infrastructure (acting as processors)</li>
</ul>
<p>Where data is transferred from Türkiye to Hungary, this falls under Article 9 KVKK and is put to
you for consent in the <a href="{S['consent']}">Consent Statement</a>. As Hungary is an EU member
state, transferred data remains under GDPR protection.</p>

<h2 id="retention">Retention periods</h2>
<div class="tablewrap">
<table class="dtable">
  <thead><tr><th>Data</th><th>Period</th></tr></thead>
  <tbody>
    <tr><td>Service agreement and application file</td><td>For the limitation period under the applicable legislation, from the end of the contractual relationship</td></tr>
    <tr><td>Consultation requests that did not proceed</td><td>Maximum 2 years from the last contact</td></tr>
    <tr><td>Accounting records</td><td>The minimum period required by the applicable legislation</td></tr>
    <tr><td>Marketing permissions</td><td>Until consent is withdrawn</td></tr>
  </tbody>
</table>
</div>
<p>Data whose retention period has expired is deleted, destroyed or anonymised.</p>

<h2 id="rights">Your rights (GDPR Art. 15–21 · KVKK Art. 11)</h2>
<ul>
  <li>To learn whether your personal data is being processed and to request information about it</li>
  <li>To learn the purpose of processing and whether the data is used in line with that purpose</li>
  <li>To learn the third parties, in the country or abroad, the data has been transferred to</li>
  <li>To request rectification of incomplete or inaccurate data</li>
  <li>To request erasure or destruction, and to ask that this be notified to the third parties concerned</li>
  <li>To object to a decision produced solely by automated analysis that works against you</li>
  <li>To claim compensation if you suffer damage due to unlawful processing</li>
  <li>To withdraw any consent you have given, at any time</li>
</ul>

<h2 id="requests">How to make a request</h2>
<p>You can send requests relating to your rights by email to <b>info@huneducation.com</b> or in writing
to <b>1204 Budapest, Bethlen utca 17, Hungary</b>. Your request is answered free of charge within 30
days at the latest. You also retain the right to lodge a complaint with the Hungarian supervisory
authority NAIH (Nemzeti Adatvédelmi és Információszabadság Hatóság), or with the Turkish Personal Data
Protection Board if you are resident in Türkiye.</p>

{related([(S['consent'],"Legal","Consent Statement","International transfers, health data and marketing permissions."),
          (S['cookies'],"Legal","Cookie Policy","The storage technologies this site uses."),
          (S['terms'],"Legal","Terms of Use","Scope of the service and limits of liability.")])}
</article>
</div>'''

write(S['privacy'], legal_page(
    S['privacy'],
    'Privacy Notice | Hun Education',
    "How HUN EDUCATION KFT. processes personal data, purposes, legal bases, transfers, retention and "
    "your rights under the GDPR and KVKK.",
    'Privacy Notice',
    'What personal data we process, for what purpose and on what legal basis, and what rights you '
    'have over it.',
    body_privacy, 'Privacy Notice'))

# =====================================================================
# 2) CONSENT STATEMENT
# =====================================================================
body_consent = f'''<div class="alayout">
{toc([('scope','Scope of consent'),('transfers','International transfers'),('health','Health data'),
      ('marketing','Marketing communications'),('media','Photographs and video'),('withdrawal','Withdrawing consent')])}

<article class="prose">

<p>This statement is here to obtain your consent for those processing activities described in the
<a href="{S['privacy']}">Privacy Notice</a> that <b>depend on consent</b>. Each item of consent is
independent of the others; agreeing to one does not cover the rest, and receiving our consultancy
service does not depend on you consenting to marketing communications.</p>

<h2 id="scope">Scope of consent</h2>
<p>The activities listed under the headings below take place only if you tick the relevant box or give
written consent. Declining does not affect the parts of the service that do not require consent.</p>

<h2 id="transfers">International transfers</h2>
<p>By the nature of the university application, visa and accommodation processes, your identity,
contact, education and, where required, financial data must be transferred to
<b>universities, official authorities and accommodation providers in Hungary</b>, and this requires
your consent. The application process cannot be carried out without that transfer. As Hungary is an EU
member state, the transferred data is protected under the GDPR. For applicants resident in Türkiye
this transfer is also governed by Article 9 KVKK.</p>

<h2 id="health">Health data (special category)</h2>
<p>Health data is processed only for <b>pilot training applications</b> (aeromedical certificate) and
for <b>health insurance procedures</b>. It is not processed without your explicit consent, is passed
only to the institution concerned, and is not used for any other purpose.</p>

<h2 id="marketing">Marketing communications</h2>
<p>If you agree to be informed about new programmes, application deadline reminders and events by
email, SMS, telephone or WhatsApp, your contact details are used for that purpose. This permission is
subject to electronic communications legislation and can be cancelled at any time using the method
included in every message, or by writing to us.</p>

<h2 id="media">Photographs and video</h2>
<p>Publishing your experience in the student stories section, with your initial or full name, your
university and your programme, happens only with your <b>separate written permission</b>. If you
withdraw that permission, the content is taken down within a reasonable period.</p>

<h2 id="withdrawal">Withdrawing consent</h2>
<p>You can withdraw any consent you have given at any time and without giving a reason, by writing to
<b>info@huneducation.com</b>. Withdrawal does not affect the lawfulness of processing carried out up
to that point. If you withdraw consent to international transfers while an application is in progress,
we will tell you that the process cannot continue.</p>

{related([(S['privacy'],"Legal","Privacy Notice","Purposes of processing, legal bases and your rights."),
          (S['cookies'],"Legal","Cookie Policy","The storage technologies this site uses."),
          (S['contact'],"Contact","Get in touch","Channels for consent and data requests.")])}
</article>
</div>'''

write(S['consent'], legal_page(
    S['consent'],
    'Consent Statement | Hun Education',
    'The scope of consent for international data transfers, health data, marketing communications and '
    'publishing photographs or video, and how to withdraw it.',
    'Consent Statement',
    'The activities that depend on consent and what each one covers. Every item is independent and '
    'can be withdrawn at any time.',
    body_consent, 'Consent Statement'))

# =====================================================================
# 3) COOKIE POLICY
# =====================================================================
body_cookies = f'''<div class="alayout">
{toc([('principles','Our privacy principles'),('security','Data security'),('storage','Cookies and local storage'),
      ('third-party','Third-party services'),('analytics','Analytics'),('changes','Changes to this policy')])}

<article class="prose">

<h2 id="principles" style="margin-top:0">Our privacy principles</h2>
<ul>
  <li>We collect only the data the service requires; we do not ask for data “in case it comes in useful”.</li>
  <li>We never sell or rent your data to any third party.</li>
  <li>Transfers are limited to the recipients listed in the <a href="{S['privacy']}">Privacy Notice</a>.</li>
  <li>No non-essential tracking technology runs without your permission.</li>
</ul>

<h2 id="security">Data security</h2>
<p>Your connection to this website is encrypted with TLS. Access to personal data is limited to staff
who need it for their role. Application documents are held in systems protected against unauthorised
access; data whose retention period has expired is deleted or anonymised.</p>

<h2 id="storage">Cookies and local storage</h2>
<p>This site uses browser storage rather than classic tracking cookies. Every record actually in use is
listed below:</p>

<div class="tablewrap">
<table class="dtable">
  <thead><tr><th>Record</th><th>Type</th><th>Purpose</th><th>Lifetime</th></tr></thead>
  <tbody>
    <tr><td class="num">hun_curtain</td><td>sessionStorage</td><td>Stops the opening animation repeating within the same session</td><td>Deleted when the tab closes</td></tr>
    <tr><td class="num">hun_first_touch</td><td>localStorage</td><td>Matches the source you first arrived from (e.g. search, an advert) with your form submission, it only reaches us if you submit a form</td><td>Until you clear your browser data</td></tr>
  </tbody>
</table>
</div>
<p>These records do not identify you and are not passed to third parties. You can delete them at any
time using your browser's clear-site-data feature; the site will continue to work.</p>

<h2 id="third-party">Third-party services</h2>
<div class="tablewrap">
<table class="dtable">
  <thead><tr><th>Service</th><th>When it comes into play</th><th>Note</th></tr></thead>
  <tbody>
    <tr><td><b>WhatsApp (Meta)</b></td><td>Only when you click an “Ask on WhatsApp” link</td><td>The conversation is subject to WhatsApp's own privacy policy; no data is sent automatically from this site</td></tr>
    <tr><td><b>Social media links</b></td><td>Only when you click them</td><td>They contain no embedded tracking code</td></tr>
  </tbody>
</table>
</div>

<h2 id="analytics">Analytics</h2>
<p>If analytics measurement (for example Google Analytics) is used, that non-essential technology is
enabled only <b>after your permission has been obtained</b>; if you do not give permission, no
analytics data is collected. This section will be updated with the tools and retention periods in use
once analytics infrastructure is switched on.</p>

<h2 id="changes">Changes to this policy</h2>
<p>This policy is updated when needed; the effective date appears at the top of the page. Substantial
changes are announced on the site. For questions: <b>info@huneducation.com</b></p>

{related([(S['privacy'],"Legal","Privacy Notice","Purposes of processing, legal bases and your rights."),
          (S['consent'],"Legal","Consent Statement","Consent-based activities and withdrawal."),
          (S['terms'],"Legal","Terms of Use","Scope of the service and limits of liability.")])}
</article>
</div>'''

write(S['cookies'], legal_page(
    S['cookies'],
    'Cookie Policy | Hun Education',
    'The data security principles of the Hun Education website, the browser storage it uses, '
    'third-party services and our analytics consent policy.',
    'Cookie Policy',
    'The storage technologies this site actually uses, the third-party services involved and our data '
    'security principles, in full, as they are.',
    body_cookies, 'Cookie Policy'))

# =====================================================================
# 4) TERMS OF USE
# =====================================================================
body_terms = f'''<div class="alayout">
{toc([('service','Nature of the service'),('information','Nature of the information on this site'),('no-guarantee','What we do not guarantee'),
      ('fees','Fees and refunds'),('ip','Intellectual property'),('liability','Limitation of liability'),
      ('changes','Changes and governing law')])}

<article class="prose">

<h2 id="service" style="margin-top:0">Nature of the service</h2>
<p>HUN EDUCATION KFT. provides <b>academic consultancy and application services</b> for admission to
higher education institutions in Hungary: goal analysis, programme matching, preparation of the
application file, following up the admission, visa guidance, accommodation support and orientation
after arrival. Hun Education is not a higher education institution; decisions on admission, enrolment,
visas and degree recognition rest with the relevant authorities.</p>

<h2 id="information">Nature of the information on this site</h2>
<p>Tuition fees, application dates, admission conditions and programme details on this site are updated
periodically by our advisory team, but <b>may be changed by the universities at any time</b> and do
not constitute a binding undertaking. Final conditions are set by the university's own official
publications and by the service agreement signed with you.</p>

<h2 id="no-guarantee">What we do not guarantee</h2>
<ul>
  <li><b>No guarantee of admission.</b> The admission decision belongs solely to the university applied to.</li>
  <li><b>No guarantee of a visa.</b> The visa decision belongs solely to the relevant consulate or official authority.</li>
  <li><b>No guarantee of degree recognition.</b> Recognition is subject to the current rules of the competent authority in your own country.</li>
  <li>Information on scholarships, work permits and post-graduation opportunities is general information; the applicable legislation can change.</li>
</ul>

<h2 id="fees">Fees and refunds</h2>
<p>The consultancy fee is separate from the fees paid to the university and is stated explicitly in the
service agreement. If your visa application is refused, the <b>tuition paid to the university is
refunded within 30 working days</b>; application and entrance exam fees fall outside the refund. The
detail of the refund conditions is set out in the service agreement.</p>

<h2 id="ip">Intellectual property</h2>
<p>The text, design, logo and images on this site belong to HUN EDUCATION KFT. or are used with
permission. Short quotations with attribution are permitted; copying, reproducing or commercially
exploiting the content without permission is prohibited. University names belong to the institutions
concerned and are referred to for information only.</p>

<h2 id="liability">Limitation of liability</h2>
<p>Hun Education cannot be held responsible for the decisions and actions of universities, official
authorities or third-party service providers, for changes in legislation, or for uninterrupted
availability of this site. Your rights under mandatory consumer legislation are reserved.</p>

<h2 id="changes">Changes and governing law</h2>
<p>These terms are updated when necessary; the current version is always published on this page with
its effective date at the top. Disputes arising from the service agreement are subject to the
governing law and jurisdiction set out in that agreement; consumers' rights to bring proceedings in
their place of residence are reserved.</p>

{related([(S['privacy'],"Legal","Privacy Notice","How your personal data is processed."),
          (S['about'],"Company","About us","Hungary-focused consultancy since 1999."),
          (S['contact'],"Contact","Get in touch","Channels for your questions.")])}
</article>
</div>'''

write(S['terms'], legal_page(
    S['terms'],
    'Terms of Use | Hun Education',
    'The scope of the Hun Education consultancy service, the nature of the information on this site, '
    'what is not guaranteed, refund conditions and limits of liability.',
    'Terms of Use',
    'What our service is and what it is not; the nature of the information on this site and the '
    'rights and responsibilities of each party.',
    body_terms, 'Terms of Use'))
