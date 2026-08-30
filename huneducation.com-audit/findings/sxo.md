# SXO Analysis — huneducation.com (Turkish market priority)

Scope note (per orchestrator instruction mid-task): deep SERP analysis narrowed to the
four highest-value Turkish queries below. Eight additional queries (pilotaj, yüksek
lisans, öğrenci vizesi, YKS'siz yurtdışı üniversite, and the three English queries)
were also searched and are used only as **supplementary** evidence for the "untapped
intent" finding — they were not classified/tabled with the same rigor as the four
primary queries. This is stated explicitly rather than inferred.

---

## 1. Query → Page-Type → Ranker → Match Table

| # | Query | Winning page type (SERP consensus) | Who ranks | HunEducation page (EN/TR) | Verdict |
|---|-------|--------------------------------------|-----------|----------------------------|---------|
| 1 | **"Macaristan'da üniversite okumak"** | **Hybrid (Service + Content)** — single consolidated agency "mega-guide" covering universities + costs + admission + language requirements on ONE url | Turkish study-abroad agencies: elt.com.tr, gedu.com.tr, gowest.com.tr, studyhungary.education, kayzinternational.com, derdanismanlik.com, academix.com.tr — no .edu, no forums, no video | `/education-in-hungary/` \| `/macaristanda-universite-okumak/` (768/1051 words, 6 H2s, no schema) | **MISMATCH (HIGH)** — right business-page category, but HunEducation split the topic across 4 siloed pages (this page + admission + costs + universities) instead of the one comprehensive page competitors rank with. Page did not surface in top results for its own target phrase. |
| 2 | **"Macaristan üniversite ücretleri"** | **Comparison/reference table synthesized as a fee table by department + a living-cost table by accommodation type** (business/eng. €3-4k, medicine €8-18k, dorm €150-300, rental €300-600, guesthouse €200-400) | Same agency set: elt.com.tr, icesturkey.com, edulife.com.tr, gedu.com.tr, kayzinternational.com, mtyedu.com — **tr.huneducation.com/macaristan-universite-fiyatlari/ appears in results (~pos. 7)** | `/costs/` \| `/macaristan-universite-fiyatlari/` — confirmed `has_table: False` on both language versions; costs live in prose under H2 "Hungarian Universities Departments Prices" and a single worked example under H2 "Sample Education and Living Wage Calculation" | **MISMATCH (HIGH)** — page partially ranks (proves topical relevance) but is structurally the wrong type: it needs to *be* a table/calculator, not prose that happens to contain numbers. |
| 3 | **"Macaristan'da tıp okumak"** | **Comparison guide with a structured entrance-exam point breakdown** (English 40 pts / medical English 20 / biology 20 / chemistry-physics 20 + oral interview) and per-university tuition (~$15,500) with explicit YÖK-recognition callouts; one competitor (kayzinternational.com) year-stamps the page "2026" for freshness | elt.com.tr, gedu.com.tr, in-bee.com, kayzinternational.com, sofiauni.com | `/studying-medicine-in-hungary-and-pursuing-a-medical-degree-in-hungary/` \| TR equivalent — 1,280 words, **duplicate H2 "Requirements for Studying Medicine in Hungary" appears twice** (content bug), no year-stamp, no per-university comparison table | **MISMATCH (CRITICAL)** — highest-stakes query in the set (parents comparing medical schools); page is a flat prose guide when the query demands a side-by-side university comparison table. Did not surface in this query's top results. |
| 4 | **"Macaristan üniversite başvuru şartları"** | **Procedural/checklist guide** (document list, apostille requirement, language-test thresholds, department-specific exceptions e.g. portfolio for arts, entrance exam for medicine); one competitor (iecc.com.tr) year-stamps "2026-2027" | elt.com.tr, icesturkey.com, gedu.com.tr, iecc.com.tr, edulife.com.tr, poseidon-tr.com, **and HunEducation twice** | `/admission/` **and** `/macaristan-universite-basvuru-sartlari/` **both appear in the same SERP** | **PARTIAL MATCH, but self-cannibalizing** — the page's underlying structure (H3 checklist: Age Limit → Visa → Eligibility → Application → Pre-Acceptance → Final Acceptance) is close to the right type. But two of the site's own URLs compete for the same query. Confirmed root cause: **zero real hreflang tags exist anywhere on the site** (grep found only RSS/oEmbed `rel="alternate"` links — no `hreflang="tr"` / `hreflang="en"` on any of the 18 pages fetched), so Google has no signal for which URL to serve to Turkish searchers. |

**SERP consensus across the 4 queries:** ~90%+ of visible organic results are Turkish study-abroad **agency** pages (Hybrid Service+Content type) — no Hungarian university (.edu/.hu) domains, no forums, no video results, no shopping/ads observed. HunEducation is fighting the correct competitive set (other agencies), not a category of publisher it can't compete with. The losses are structural, not category-level.

---

## 2. Three Clearest Page-Type Mismatches (structural fixes, not "add more content")

### Mismatch 1 — `/costs/` and `/macaristan-universite-fiyatlari/` need to become a **comparison table + cost calculator**, not prose
- Current: has_table=False; a single narrative "Sample Education and Living Wage Calculation" example, buried under an H2, not an interactive element.
- Fix: Replace the prose fee narrative with (a) a sortable **table**: university × department × annual tuition (EUR) × application fee, matching the exact breakdown Google already rewards (business/engineering €3-4k, medicine/dentistry €8-18k), and (b) an above-the-fold **interactive calculator**: dropdowns for city, degree level, department → outputs estimated annual tuition + living cost range. This is a Tool/Interactive page-type requirement, not a copywriting fix.

### Mismatch 2 — `/studying-medicine-in-hungary.../` needs to become a **university comparison table**, not a single narrative guide
- Current: one flat article; duplicate H2 "Requirements for Studying Medicine in Hungary"; no per-university breakdown.
- Fix: Add a **Comparison Page** module: rows = Semmelweis / Debrecen / Pécs / Szeged, columns = tuition (EUR/year), entrance exam format + point weights, duration, campus city, YÖK-equivalence status. This is the exact structure competitors' synthesized answers already contain — the page needs the table, not more paragraphs.

### Mismatch 3 — `/universities/` and `/macaristan-universiteleri/` need to become a **city/campus comparison or filterable directory**, not 12 sequential prose blurbs
- Current: 615 words, 18 images, one H2 per university (12 universities) written as sequential text blocks — no sortable data, no map, no city grouping (Budapest vs. Debrecen vs. Pécs vs. Szeged).
- Fix: Restructure as either (a) a **city-page cluster** — separate landing pages for "Study in Budapest" / "Study in Debrecen" / "Study in Pécs" (each with its own local intent: cost of living in that city, campuses located there, transport), mirroring how "study in Hungary" SERPs increasingly reward city-level content, or (b) a single **filterable comparison table** (university × city × QS/THE ranking × English programs count × tuition range), reusing the Ajax Search Pro filter component already built for `/courses/`.

**Bonus structural/technical fix (ties into Mismatch 4 in the query table):** implement real `hreflang="en"`/`hreflang="tr"` link tags between the `huneducation.com` and `tr.huneducation.com` page pairs. This is a one-time template fix that resolves the self-cannibalization seen on the admission query and likely affects all 9 page pairs, not just admission.

---

## 3. Biggest Untapped Intent

**A dedicated Hungary student-visa page does not exist anywhere in HunEducation's money-page set**, despite visa being a mandatory, high-anxiety step every persona must clear. The supplementary search on "Macaristan öğrenci vizesi" returned an entirely different competitor set — visa/travel agencies (vizemerkezi.com, ligarbatravel.com, mkmtur.com, endlessabroad.com.tr) — none of which are education consultancies. Their winning page type is a simple **procedural checklist**: required documents, biometric photo specs, accommodation proof, flight reservation proof, processing time ("15-30 business days"), and total service cost ("~350 €"). HunEducation, as an agency that already handles visa support for its placed students, has stronger authority to win this than pure visa-processing shops (real success/approval-rate data, real applicant stories) but currently cedes the entire query to them. A close second: "YKS'siz yurtdışı üniversite" is an awareness-stage entry query where HunEducation's core differentiator (no exam required) should dominate, but no page frames Hungary against the other no-exam destinations (Poland, Georgia, Malta) the way competitor yelkenegitim.com's comparison content does.

---

## 4. Persona Scoring

| Persona | Journey stage | Relevance /25 | Clarity /25 | Trust /25 | Action /25 | Total /100 | Rating |
|---|---|---|---|---|---|---|---|
| Turkish high-school senior + paying parent | Awareness→Consideration | 14 | 11 | 8 | 12 | **45** | Needs Work |
| Bachelor's graduate seeking a master's | Consideration→Decision | 15 | 12 | 9 | 13 | **49** | Needs Work |
| Medicine applicant comparing countries | Decision (high-stakes) | 13 | 10 | 7 | 11 | **41** | Needs Work |

**Turkish high-school senior + paying parent** — must visit 4 separate pages (why-hungary, education-in-hungary, costs, admission) to assemble the answer competitors give on one page (Relevance 14). No table means the parent can't quickly compare department fees (Clarity 11). Zero schema, zero testimonials, no visible accreditation badges or "since [year]" credibility markers for a parent trusting an agency with tuition money (Trust 8 — weakest cell across all three personas). CTA is generic "Get in Touch"/WhatsApp with no parent-specific offer (e.g., "Free eligibility check" or a downloadable cost PDF) (Action 12).
**Top fix:** add an Organization/EducationalOrganization schema block with verifiable placement numbers + a parent-facing "Is my child eligible? — free 10-minute check" CTA on the admission and costs pages.

**Bachelor's graduate seeking a master's** — masters page covers general advantages and a few field examples (Psychology, Business, Engineering) but doesn't link prominently to the actual filterable 490-programme catalogue at `/courses/`, so the persona must rediscover filtering on a separate page (Relevance 15, Clarity 12). No alumni outcomes or recognition proof beyond a generic "internationally recognized diploma" claim (Trust 9). CTA is "Learn More"/"Get in Touch," not "Browse Master's Programmes →" pre-filtered to level=Master's (Action 13).
**Top fix:** cross-link `/masters-education-in-hungary/` directly into a pre-filtered `/courses/` view by degree level, and add at least one graduate outcome/testimonial.

**Medicine applicant comparing countries** — this persona is explicitly evaluating Hungary against Poland/Georgia/Czechia etc., and the medicine page contains zero comparative-country framing (Relevance 13 — weakest relevance score of the three). The duplicated H2 and absence of a university-by-university exam/tuition table make the page hard to scan for a decision this consequential (Clarity 10). No accreditation/recognition proof (WHO/ECFMG-style listing, residency/pass-rate data), no named medical-education expert byline for E-E-A-T (Trust 7 — lowest trust score overall). Single generic "Get In Touch Now" CTA with no medicine-specific consultation offer (Action 11).
**Top fix:** fix the duplicate-H2 bug, add the Semmelweis/Debrecen/Pécs/Szeged comparison table (see Mismatch 2), and add a medicine-specific "Book a free entrance-exam readiness consultation" CTA.

**Systemic issue across all three personas:** Trust is the lowest-scoring dimension for every persona (7–9/25) — driven by the site-wide absence of schema markup (`schema: []` confirmed on all 18 pages checked), testimonials, accreditation badges, and visible freshness/update dates (all 18 pages fetched carry no real "last updated" date; image upload timestamps trace back to 2023, and htmldate's fallback guess of 2026-01-01 is not a real publication date signal).

---

## 5. Limitations

- WebSearch is not a verified google.com.tr session — results may not exactly match localized Turkish SERP ranking order, ads, PAA boxes, or AI Overview presence/citations. No PAA questions, related-searches list, or featured-snippet format could be directly confirmed; query-intent inference is based on the synthesized answer content and the domains that ranked.
- Per the narrowed scope, only 4 of the original 12 target queries were analyzed to full rigor. The other 8 (pilotaj eğitimi, yüksek lisans, öğrenci vizesi, YKS'siz yurtdışı üniversite, and the 3 English queries) were searched and results exist, but were used only as supporting evidence for the untapped-intent finding, not tabled/scored.
- Page-type classification of competitor URLs is based on WebSearch's synthesized summaries and titles, not a full render+parse of each competitor page (out of scope/turn budget) — treat competitor classification as directional, not verified line-by-line.
- No rank-tracking tool was used, so "position ~7" references are inferred from result order returned by WebSearch, not confirmed SERP position.
- Ads, AI Overview citations, and PAA clusters could not be independently confirmed for any of the 4 queries.

---

## Cross-Skill Recommendations
- Schema is absent site-wide (18/18 pages show `schema: []`) → recommend `/seo schema` for Organization, EducationalOrganization, Course, and FAQPage generation.
- Duplicate-H2 content bug on the medicine page and thin 615-word `/universities/` page → recommend `/seo page` for page-level audits.
- No E-E-A-T signals (author bylines, accreditation, outcomes data) on medicine/pilot/masters pages → recommend `/seo content` for a deep E-E-A-T pass.
- Missing hreflang between huneducation.com and tr.huneducation.com, confirmed across all 9 page pairs → technical SEO fix, flag in the main technical audit.

Score: 38/100
