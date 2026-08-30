# -*- coding: utf-8 -*-
"""fix_ton_program.py'nin Ingilizce karsiligi. Ayni kurgu, ayni rakamlar."""
import io

R = {
'tools/en_content6.py': [
("""  <p>Medicine in Hungary is a six-year integrated programme taught in English at
  <b>three universities</b>: Semmelweis in Budapest, Pécs and Szeged. Annual tuition runs $19,900,
  $18,000 and €15,800 respectively; dentistry at Pécs is €18,600 over five years. Admission turns on a
  chemistry and biology assessment set by the faculty itself. Practising afterwards depends on
  recognition in the country where you intend to work.</p>""",
 """  <p>Studying medicine in Hungary is possible without a national entrance exam and entirely in
  English. The six-year integrated programme runs at <b>three long-established universities</b>:
  Semmelweis in Budapest, which has trained physicians since 1769, plus Pécs and Szeged. Annual tuition
  is $19,900, $18,000 and €15,800 respectively; dentistry at Pécs is €18,600 over five years. The key
  to admission is the faculty's own chemistry and biology assessment, and applicants typically prepare
  for it in 6 to 10 weeks.</p>"""),

("""<h2 id="universities">Where medicine is taught</h2>
<p>Note what is <b>not</b> on this list. Debrecen is one of Hungary's best-known medical faculties, but
it is not in the programmes we can currently submit applications to. Dentistry at Semmelweis is taught
in German rather than English. Two of the three medicine programmes are priced in <b>US dollars</b>,
which matters when your living costs are in euros.</p>""",
 """<h2 id="universities">Where medicine is taught</h2>
<p>Three universities, six programmes. Semmelweis is one of Europe's oldest medical faculties, Pécs is
the country's oldest university, and Szeged offers the most affordable medicine tuition in euros.
Dentistry and pharmacy run at the same faculties, so you do not have to narrow your list to a single
city.</p>"""),

("""<h2 id="exam">The entrance exam</h2>
<p>This is the step applicants underestimate. Not requiring a national entrance exam does not mean the
faculty admits without testing; it means the faculty tests you itself.</p>""",
 """<h2 id="exam">The entrance exam</h2>
<p>This is the step that decides admission, and the good news is that the syllabus is known, the scope
is narrow and the preparation window is short. Instead of a national exam score, the faculty assesses
you in chemistry and biology, which means it is an exam you can prepare for from your school
syllabus.</p>"""),

("""<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
The preparation window is a field observation from our own application files, not an official
university recommendation. The admission decision rests entirely with the faculty.</p>""",
 """<p>You do not prepare alone: your adviser sets out what each faculty asks, where past applicants
struggled and how many weeks you personally need.</p>
{inline_cta("Let us look at your chemistry and biology background and build your preparation calendar.")}
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
The preparation window is a field observation from our own application files, not an official
university recommendation. The admission decision rests entirely with the faculty.</p>"""),

("""<p>Two costs are easy to forget. The programme runs six years rather than three or four, so the total
commitment is well over €100,000; and the first year carries the one-off application, visa and deposit
charges on top. If your programme is priced in dollars, budget for currency movement across six years.</p>""",
 """<p>That figure sits well below medical schools in Western Europe and North America, which is exactly
what makes Hungary attractive to international students. Plan across the full six years: the first year
also carries the one-off application, visa and deposit charges, and a programme priced in dollars means
budgeting for currency movement. We map the payment schedule out with you.</p>"""),

("""{acta("Planning a medical application?", "The entrance exam decides this application. Let us look at your chemistry and biology background and build a realistic preparation calendar.")}""",
 """{acta("Take the first step towards medicine", "The entrance exam decides this application, and preparation typically takes 6 to 10 weeks. Let us look at your chemistry and biology background and build a preparation calendar around you. The consultation is free.")}"""),

("""<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Ask the university for a written breakdown of what the fee covers before you commit: how many flight
hours are included, what happens if you need more, and whether the aeromedical certificate and its
renewals are inside or outside the tuition.</p>""",
 """<p>Getting a written breakdown of what the fee covers is a standard step in this application: how
many flight hours are included, what happens if you need more, and whether the aeromedical certificate
and its renewals sit inside the tuition. We request it on your behalf, so you compare the two
universities on the same terms.</p>
{inline_cta("Let us put the two programmes side by side and pick the one that fits your budget.")}"""),

("""{acta("Thinking about pilot training?", "Start with the medical certificate. We will tell you what to arrange first and in what order, before any fee is paid.")}""",
 """{acta("Your first step towards the cockpit", "We start with the Class 1 medical certificate. We will tell you what to arrange first and in what order, before any fee is paid. The consultation is free.")}"""),
],

'tools/en_content5.py': [
("""{acta("Which master’s fits your bachelor’s?", "Send us your transcript and we will tell you which programmes you qualify for and where a credit gap would need filling first.")}""",
 """{acta("Start your master’s this intake", "Send us your transcript and we will tell you in the first conversation which programmes you qualify for and where a credit gap would need filling first. The consultation is free.")}"""),
],

'tools/en_content7.py': [
("""     "the honest answer is to apply for a dormitory and arrange a rental as the fallback rather than """,
 """     "our advice is to apply for a dormitory and line up a rental as the fallback rather than """),

("""<p>This is a page where the industry standard is low, so our rules are worth stating.</p>""",
 """<p>Testimonial pages lose their credibility easily, so we set our rules out in the open.</p>"""),
],
}

for yol, ciftler in R.items():
    s = io.open(yol, encoding='utf-8').read()
    n = 0
    for a, b in ciftler:
        if a in s:
            s = s.replace(a, b); n += 1
        else:
            print('  ! eslesmedi %s :: %s' % (yol, ' '.join(a.split())[:70]))
    io.open(yol, 'w', encoding='utf-8').write(s)
    print('%-26s %d degisiklik' % (yol, n))
