# GEO / AI Search Readiness Audit — huneducation.com & tr.huneducation.com

Audit date: 2026-08-30
Scope: huneducation.com (international/English host) and tr.huneducation.com (Turkish host), both WordPress + Elementor, ~984 course pages, 40 university pages, 14+14 editorial pages, 500-page crawl sample verified live during this session.

Note on method: Live SERP verification was attempted for the three benchmark queries via DuckDuckGo (returned a CAPTCHA challenge, no data obtained) and Bing (returned what appears to be a static "Hungary" country info-panel — tr.wikipedia.org/Macaristan, gezimanya.com, harita.gen.tr, ankara.mfa.gov.hu, transfermarkt.com.tr, avruparuyasi.com.tr, gidelimmi.com, ab.gov.tr, milliyet.com.tr — identical across all three distinct queries, which indicates an automation-triggered generic fallback rather than true per-query organic results). No DataForSEO MCP tools were available in this session. Competitive commentary below is therefore flagged qualitatively rather than presented as verified live rankings, and should be re-checked with a browser-based session or DataForSEO before final client presentation.

---

## 1. AI Crawler Accessibility — Both Hosts

Verified live from `https://huneducation.com/robots.txt` and `https://tr.huneducation.com/robots.txt` (byte-identical on both hosts):

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://[host]/sitemap.xml
Sitemap: https://[host]/sitemap.html
```

There is **no bot-specific block anywhere in robots.txt on either host** — no named user-agent stanzas for GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Google-Extended, Applebot-Extended, CCBot, or Bytespider. All of them inherit the wildcard `User-agent: *` rule, which disallows only `/wp-admin/`. Practical effect, per crawler:

| Crawler | Status | Basis |
|---|---|---|
| GPTBot | **Allowed** | Falls under `*`, no override |
| OAI-SearchBot | **Allowed** | Falls under `*`, no override |
| ChatGPT-User | **Allowed** | Falls under `*`, no override |
| ClaudeBot | **Allowed** | Falls under `*`, no override |
| Claude-User | **Allowed** | Falls under `*`, no override |
| PerplexityBot | **Allowed** | Falls under `*`, no override |
| Google-Extended | **Allowed** | Falls under `*`, no override |
| Applebot-Extended | **Allowed** | Falls under `*`, no override |
| CCBot | **Allowed** (unblocked, even though the skill brief lists this as optional-to-block for training-only use cases) | Falls under `*`, no override |
| Bytespider | **Allowed** (same caveat as CCBot) | Falls under `*`, no override |

This was cross-checked against the 500-page live crawl: `urllib.robotparser` evaluated every one of the 500 fetched URLs and blocked **zero** (`engelli: []`), and **zero** pages carried a `noindex` robots meta tag. Both hosts are also plain server-rendered WordPress (confirmed `is_spa: false`, raw HTML `Content-Length` ~50KB returned without JS execution) — there is no client-side-rendering barrier, so any crawler that respects robots.txt can read full content on first fetch. **Robots.txt is not the problem on this site; it is one of the only things already correct.** The real accessibility problems are (a) broken sitemap discovery and (b) a language-signal bug on the primary domain, both detailed below.

---

## 2. Why Zero Schema + Zero Meta Descriptions + Zero OG Is a GEO Problem (Not Just SEO)

Confirmed site-wide across the 500-page crawl: **0/500 pages contain any `"@type"` JSON-LD block, 0/500 carry an `og:title` tag, 494/500 (98.8%) have no `<meta name="description">`, and 0/500 carry `hreflang`.**

In classic SEO terms these are minor — meta description mostly affects SERP click-through, not ranking; JSON-LD mostly unlocks rich-result decoration. In a GEO context they are structural, because of how answer engines actually consume a page:

- **No entity/fact graph to parse.** AI engines (Perplexity, ChatGPT search/browse, Google AI Overviews, Bing Copilot) run an extraction pass before generating an answer, trying to resolve "what entity is this page about, what facts does it assert, who provides them, at what price/duration." With zero `Organization`/`EducationalOrganization`/`Course`/`CollegeOrUniversity`/`FAQPage` markup, every one of those facts must be inferred from unstructured Elementor `<div>` markup. A competing source that ships the same fact pre-structured (e.g. a university's own admissions page with `Course` schema) is functionally easier and safer for a model to extract from and cite — this site is competing with one hand tied behind its back on every query where a schema-marked competitor exists.
- **No meta-description safety net.** Several answer engines (Bing Copilot in particular, Google AI Overviews as a fallback) use the meta description as a candidate summary when passage-level extraction from the body is ambiguous. 494/500 pages have nothing to fall back on.
- **No OG tags means broken citation cards.** When a link is shared, pasted into a chat, or surfaced as a citation card (Perplexity's citation strip, ChatGPT's link preview, LinkedIn/X previews used to build off-site brand signal), `og:title`/`og:description`/`og:image` are what render that card. Zero OG tags means even a *successful* citation is likely to show a blank or malformed preview, which reduces click-through and perceived credibility at the exact moment a user is deciding whether to trust the source.
- **No hreflang means the two hosts look like duplicate/unrelated content rather than a deliberate bilingual pair**, so an engine has no signal for which host to prefer per query language — compounded by the title-tag bug in section 5.

---

## 3. Passage-Level Citability of the Editorial Pages

Corrected baseline (per coordinator sampling of 10 course pages): **course pages average ~330 words of real content (range 222–486 words)**. My own spot-check of the same course page with `render_page.py`'s trafilatura-based `extracted_text` (boilerplate-stripped, the closest proxy to what an automated answer-engine ingestion pipeline actually recovers) returned only **76 words** for `/course/medicine-pecs-university/`, and 73–81 words for `/costs/` and `/about-us/`. This is not a contradiction — it is itself a finding: **roughly 70-80% of the nominal on-page copy is structurally invisible to boilerplate-stripping extraction**, because Elementor renders content as deeply nested, non-semantic `<div class="elementor-element...">` containers with no `<article>`/`<main>` boundary trafilatura-class tools can anchor on, so they grab the first coherent block and drop the rest. AI crawlers with lighter-weight extraction than Googlebot are likely to see the same truncated ~75-90 words, not the full ~330.

Concrete examples:

- **`/course/medicine-pecs-university/`** (trafilatura sees 76 words): "The General Medicine course at Pécs is structured to provide a solid foundation... six years of both pre-clinical and clinical studies, spanning ten semesters, along with one year dedicated to clinical rotations." This is reasonably self-contained and states a real fact (6 years / 10 semesters + 1 clinical year), but: no question-phrased heading, no tuition figure on the page itself (that lives only on `/costs/`, disconnected), no date, no link to Pécs's own official programme page for corroboration.
- **`/costs/`** contains the single best citation-bait on the entire site and it is being wasted: buried in the body text (not a table, not a schema `Offer`, not tied to a question-heading) are specific, extractable figures — *"Hungarian Dentistry: Starting from 17,350 EUR annually," "Hungarian Medical Education: Starting from 16,500 USD annually," "Hungarian Pilot Training: Semesterly 7,500–13,500 USD," "Hungarian Psychology Bachelor's/Master's: Starting from 7,800 EUR," "English Preparatory: Starting from 2,500 EUR per semester."* This is exactly the kind of statistic AI engines prefer to cite, and it answers "Macaristan tıp fakültesi ücretleri" / "Hungary medical school fees" almost directly — but: (a) zero `<table>` elements exist on the page (confirmed via HTML grep), the numbers are comma-separated inline text; (b) currency is inconsistent — some figures in USD, others in EUR, on the same page; (c) the relevant H2 is "Hungarian Universities Departments Prices," not phrased as a question ("Macaristan'da tıp fakültesi ücreti ne kadar?"); (d) no source link to the issuing university or to Study in Hungary/Tempus Public Foundation for corroboration; (e) no date ("2026/27 academic year") attached to any figure.
- **`/about-us/`** (81 words extracted): "more than 24 years of experience" is a usable specific claim but has no anchor founding year, and is not attributed to a named person (see section 4).
- No outbound links to any authoritative third party were found on any sampled editorial page (About, Costs) — the only outbound links present are the company's own Twitter/X, Facebook, Instagram, and YouTube profiles. Zero citations to government sources (e.g. Study in Hungary, Tempus Public Foundation, the Hungarian embassy) or to the universities' own official pages.
- `publication_date` extraction (htmldate) fell back to a generic default guess on every sampled page — there is no real, detectable `datePublished`/`dateModified` signal anywhere, and no visible "last updated" text on-page. Recency is a real weighting factor for Perplexity and Bing Copilot in particular; this site currently supplies none.
- Heading structure exists (course pages average 2 H2s; `/costs/` has 9 H2/H3s) but none are phrased as questions, and there is no FAQPage-style Q&A pattern anywhere on the crawled 500 pages.

---

## 4. Entity Resolution: "Hun Education"

**What exists (real, usable signals):**
- A real registered legal entity: **HUN EDUCATION KFT.**, address **1204 Budapest, Bethlen utca 17, Hungary**, phone **+36 70 296 35 31**, email **info@huneducation.com** — but this NAP block appears in exactly one place found in this audit (the `/contact/` page body text), not in schema, not in a sitewide footer block, not repeated identically on the TR host in a way I could verify in this session.
- Two real, named staff members with direct contact details on `/contact/`: **Beyza Kantarcı** (beyza@huneducation.com, +90 534 260 00 27) and **Çağla Nur Türken** (cagla@huneducation.com, +36 20 360 2472) — genuine Person-level entity material that is currently disconnected from any content (no author bylines anywhere).
- A regional partner entity also listed on `/contact/`: **Aim Intermed Ltd.**, Bangkok, Thailand — evidence of a real multi-country operation, again unstructured.
- Social profiles: X/Twitter `@huneducation`, Facebook `/HunEducationGLB`, Instagram `@huneducation`, YouTube channel `UCtjkiFBPE4S-igdJ_GVbFUQ`. None of these are wired into any `sameAs` schema (because there is no schema at all), and none could be verified for follower/activity levels in this session (YouTube's about page requires JS rendering not exercised here).

**What is missing:**
- **No Wikipedia article.** A direct search of English Wikipedia for "Hun Education" as a Hungary study-abroad consultancy returned zero results ("no results matching the query").
- **No verifiable Wikidata item** (not independently queried via SPARQL in this session, but the absence of any Wikipedia article makes an existing, populated Wikidata node unlikely).
- **No LinkedIn company page** surfaced in any of the sampled pages (About, Costs, Contact) — a real gap for a B2B-adjacent consultancy, and directly relevant since the skill brief's own brand-signal table ranks Wikipedia entity presence and Reddit/YouTube mentions as the strongest AI-citation correlates, both of which are currently unconfirmed-to-absent here.
- **No third-party citations of "Hun Education" found** in this session's checks (Bing panel for the three benchmark queries surfaced only generic Hungary-country sources, never an education-consultancy domain, though see the data-reliability caveat at the top of this document).
- **No author/Person schema** connecting the two real named advisors to any of the editorial content they presumably wrote or could credibly review.

**Net effect:** the organization is real and has genuine NAP/people/social assets, but none of it is machine-legible or externally corroborated — from an entity-resolution standpoint (Google Knowledge Graph, and by extension the entity backbones many LLMs are trained/grounded against), "Hun Education" is effectively an unresolved entity today.

---

## 5. Niche Queries and Citation Prospects

| Query (TR / EN) | Intent | Current citation prospects for huneducation.com |
|---|---|---|
| "Macaristan'da üniversite okumak" / "studying at university in Hungary" | Broad informational | **Low.** This is precisely the query the homepage title should own, but the homepage `<title>` on the international host is a run-on Turkish marketing sentence (see below) with no meta description, no schema, and the page competes against Wikipedia, official Hungary/EU government pages, and general travel/education portals for broad "Hungary" intent. |
| "Macaristan tıp fakültesi ücretleri" / "Hungary medical school tuition fees" | Commercial/informational, high-intent for this business | **Moderate potential, currently unrealized.** `/costs/` holds genuinely specific, accurate-looking figures (dentistry from 17,350 EUR/yr, medicine from 16,500 USD/yr) that match this query almost exactly, but zero schema, zero table, mixed currencies, no date, and no third-party corroboration make it a weak citation candidate against university admissions pages that publish the same class of figure in a structured, sourced format. |
| "Macaristan öğrenci vizesi" / "Hungary student visa" | Transactional/informational | **Very low today.** No dedicated visa page was found among the crawled editorial set (visa content, if any, is folded into `/admission/`); official consulate/embassy and government sources naturally dominate this query type, and this site currently supplies no competing structured, dated, sourced content. |

Because AI engines increasingly reward exactly the signals this site lacks — dated, sourced, schema-tagged, question-answering passages — and because only an estimated ~11% of domains get cited by *both* ChatGPT and Google AI Overviews (per the skill brief), Hun Education should treat each platform as a distinct optimization target rather than assuming one fix serves all four.

**Qualitative platform readiness (no live DataForSEO/browser verification available this session — re-verify before client presentation):**

| Platform | Est. readiness | Rationale |
|---|---|---|
| Google AI Overviews | ~20/100 | No schema, 494/500 pages missing meta description, broken sitemap discovery all suppress the organic base AIO typically draws from. |
| ChatGPT (search/browse) | ~15/100 | GPTBot/OAI-SearchBot/ChatGPT-User are all crawl-allowed, but zero entity resolution (no Wikipedia/Wikidata) and content fragmented by Elementor markup make confident citation unlikely. |
| Perplexity | ~25/100 | PerplexityBot is crawl-allowed and `/costs/` has the statistic-density Perplexity favors, but no dates, no schema, no source attribution undercut trust scoring. |
| Bing Copilot | ~25/100 | Slightly higher because Copilot still leans on classic title/meta signals more than pure-LLM engines; the corrupted EN title tag directly damages this platform specifically. |

---

## 6. Recommended `llms.txt`

Neither host returns anything at `/llms.txt` (confirmed 404 on both). Drafts below — treat as a starting template; the TR page slugs are inferred from on-site Turkish navigation labels and were not individually crawl-confirmed in this session (only `/iletisim/` was verified live), so confirm each URL against `https://tr.huneducation.com/sitemap.html` before publishing.

### `https://huneducation.com/llms.txt`

```markdown
# HunEducation

> HunEducation (legal entity: HUN EDUCATION KFT., registered in Budapest, Hungary) is an independent educational consultancy that helps international students apply to Bachelor's, Master's, and preparatory programmes at accredited Hungarian universities, taught in English and German. HunEducation receives no government funding and provides free application, visa, and enrolment guidance.

## Company
- [About Us](https://huneducation.com/about-us/): Company background and 24+ years of combined advisory experience.
- [Contact](https://huneducation.com/contact/): Registered address (1204 Budapest, Bethlen utca 17, Hungary), phone +36 70 296 35 31, email info@huneducation.com, named academic advisors.

## Guides
- [Why Hungary](https://huneducation.com/why-hungary/): Why international students choose Hungary for higher education.
- [Education in Hungary](https://huneducation.com/education-in-hungary/): Overview of the Hungarian higher-education system.
- [Costs](https://huneducation.com/costs/): Tuition ranges by field (medicine, dentistry, pilot training, psychology, preparatory year) and living costs.
- [Admission](https://huneducation.com/admission/): Application requirements and process.
- [Studying Medicine in Hungary](https://huneducation.com/studying-medicine-in-hungary-and-pursuing-a-medical-degree-in-hungary/): Medical degree structure, duration, clinical training.
- [Master's Education in Hungary](https://huneducation.com/masters-education-in-hungary/): Master's programme options and requirements.
- [Pilot Training at Hungarian Universities](https://huneducation.com/pilot-training-at-hungarian-universities/): 0-to-ATPL and aviation engineering pathways.
- [Student Perspectives](https://huneducation.com/student-perspectives/): First-person accounts of studying and living in Hungary.

## Universities and Courses
- [Universities](https://huneducation.com/universities/): Index of 15+ partner Hungarian universities (Semmelweis University, University of Pécs, Corvinus University of Budapest, Budapest Metropolitan University, University of Dunaújváros, and others).
- [Courses](https://huneducation.com/courses/): Searchable catalogue of ~980 English/German-taught degree programmes.

## Optional
- [Sitemap (HTML)](https://huneducation.com/sitemap.html): Human-readable page index. (Note: the site's XML sitemap is currently non-functional — see Technical Accessibility findings — do not rely on it for discovery until fixed.)
```

### `https://tr.huneducation.com/llms.txt`

```markdown
# HunEducation (Türkçe)

> HunEducation (yasal unvanı: HUN EDUCATION KFT., Budapeşte, Macaristan merkezli), Macaristan'daki akredite üniversitelerde İngilizce ve Almanca eğitim veren lisans, yüksek lisans ve hazırlık programlarına uluslararası öğrenci yerleştiren bağımsız bir eğitim danışmanlığı şirketidir. Hükümetten destek almaz; başvuru, vize ve kayıt süreçlerinde ücretsiz danışmanlık sağlar.

## Şirket
- [Hakkımızda](https://tr.huneducation.com/hakkimizda/): Şirket geçmişi ve 24+ yıllık danışmanlık deneyimi.
- [İletişim](https://tr.huneducation.com/iletisim/): Adres (1204 Budapeşte, Bethlen utca 17, Macaristan), telefon +36 70 296 35 31, e-posta info@huneducation.com, isimli akademik danışmanlar.

## Rehberler
- [Neden Macaristan'da Eğitim](https://tr.huneducation.com/neden-macaristanda-egitim/): Uluslararası öğrencilerin Macaristan'ı tercih etme nedenleri.
- [Macaristan'da Üniversite Okumak](https://tr.huneducation.com/macaristanda-universite-okumak/): Macaristan yükseköğretim sistemine genel bakış.
- [Macaristan Üniversite Fiyatları](https://tr.huneducation.com/macaristan-universite-fiyatlari/): Alana göre öğrenim ücretleri (tıp, diş hekimliği, pilotluk, psikoloji, hazırlık) ve yaşam maliyetleri.
- [Başvuru Koşulları](https://tr.huneducation.com/basvuru-kosullari/): Başvuru gereklilikleri ve süreci.
- [Macaristan'da Tıp Eğitimi](https://tr.huneducation.com/macaristanda-tip-egitimi-ve-macaristanda-tip-okumak/): Tıp eğitiminin yapısı, süresi ve klinik eğitim.
- [Macaristan Yüksek Lisans](https://tr.huneducation.com/macaristan-yuksek-lisans/): Yüksek lisans programı seçenekleri ve şartları.
- [Macaristan Üniversiteleri Pilotluk Eğitimi](https://tr.huneducation.com/macaristan-universiteleri-pilotluk-egitimi/): 0'dan ATPL'ye pilotluk ve havacılık mühendisliği programları.
- [Öğrenci Görüşleri](https://tr.huneducation.com/ogrenci-gorusleri/): Macaristan'da okuyan öğrencilerin deneyimleri.

## Üniversiteler ve Bölümler
- [Üniversiteler](https://tr.huneducation.com/universiteler/): 15+ ortak Macaristan üniversitesi dizini (Semmelweis Üniversitesi, Pécs Üniversitesi, Corvinus Üniversitesi, Budapest Metropolitan Üniversitesi, Dunaújváros Üniversitesi ve diğerleri).
- [Bölümler](https://tr.huneducation.com/bolumler/): İngilizce/Almanca eğitim veren ~980 lisans/yüksek lisans programı kataloğu.

## İsteğe Bağlı
- [Site Haritası (HTML)](https://tr.huneducation.com/sitemap.html): İnsan tarafından okunabilir sayfa dizini. (Not: XML site haritası şu anda çalışmıyor — bkz. Teknik Erişilebilirlik bulguları.)
```

---

## 7. Prioritised GEO Actions

### Critical
1. **Fix the EN-host homepage `<title>` language bug.** `https://huneducation.com/` (declared `lang="en-US"`, English nav/body copy, confirmed via live fetch) currently renders `<title>HunEducation – Macaristan üniversiteleri, Macaristan yüksek lisans ve Macaristan'da üniversite okumak hakkında profesyonel danışmanlık hizmetleri veriyoruz.</title>` — pure Turkish text on the international/English domain. Any language-classification step in an AI crawler's pipeline will see a title/body language mismatch on the exact page meant to own English-language "study in Hungary" queries. Likely cause: a shared SEO-plugin title field duplicated across the EN/TR WordPress installs. Effort: **Low** (single settings fix). Impact: site-wide, since this is the entity's primary international landing page.
2. **Repair sitemap infrastructure on both hosts.** The robots.txt-declared `sitemap.xml` resolves to a `sitemapindex` pointing only to `sitemap-misc.xml`, which contains exactly 2 URLs (homepage + `/sitemap.html`). The native `/wp-sitemap.xml` returns an empty `<urlset/>` on both hosts. **Zero of the ~984 course pages, 40 university pages, or 28 editorial pages are declared in any machine-readable sitemap**, on either huneducation.com or tr.huneducation.com. Discovery depends entirely on AI crawlers following raw internal links from the homepage, with no lastmod/priority signal. Fix: retire the abandoned "Google Sitemap Generator" plugin (generator comment shows arnebrachhold.de, v4.1.23, a long-discontinued plugin) in favor of Yoast/RankMath/core WP sitemaps configured for the `course` and `university` custom post types, then update robots.txt to point at the new sitemap. Effort: **Medium**. Impact: unlocks discoverability for essentially the entire content inventory.
3. **Add JSON-LD site-wide (currently 0/500 pages).** Minimum set: `Organization`/`EducationalOrganization` sitewide (name, url, logo, address, telephone, `sameAs` to the four social profiles); `Course` schema on the ~984 programme pages (name, provider, educationalCredentialAwarded); `CollegeOrUniversity` on the 40 university pages; `FAQPage` on `/costs/`, `/admission/`, and any visa-related content. Templatable across the shared course/university templates. Effort: **Medium-High** (dev time, but one-time templated build). Impact: gives every AI engine an unambiguous fact graph instead of forcing inference from Elementor markup.

### High
4. **Write real meta descriptions for the 494/500 pages missing one**, in 40-60 word direct-answer form (not marketing copy) — templatable by course type/tuition tier for the ~984 programme pages, manual for the ~28 editorial pages. Effort: Medium.
5. **Restructure `/costs/` (and the other core editorial pages) around the numeric answers they already contain.** Move the existing tuition figures (dentistry 17,350 EUR/yr, medicine 16,500 USD/yr, pilot training 7,500–13,500 USD/semester, psychology 7,800 EUR, preparatory 2,500 EUR/semester) into the first 40-60 words under a question-phrased H2 ("Macaristan'da tıp fakültesi ücreti ne kadar?"), normalize to one currency, render as an actual `<table>` (currently zero `<table>` elements exist on this page), and wrap in `FAQPage`/`Course` schema. Effort: Medium.
6. **Add real dated signals.** htmldate could not extract a genuine publish/modified date from any sampled page (fell back to a default guess) and no visible "last updated" text exists. Add `datePublished`/`dateModified` schema plus a visible "Son güncelleme" / "Last updated" line, and anchor pricing to an academic year ("2026/27 tuition"). Effort: Low-Medium.
7. **Build real hreflang + deep cross-linking between the two hosts.** Today the only EN⇄TR connection is a manual nav link to the other host's homepage, and 0/500 pages carry `hreflang`. Add reciprocal `hreflang="en"`/`hreflang="tr"` tags per equivalent page pair and deep-link the language switcher (course-to-course, university-to-university) instead of homepage-to-homepage. Effort: Medium.

### Medium
8. **Publish the `llms.txt` files drafted in Section 6** on both hosts; low effort, immediate.
9. **Build entity presence.** Create a Wikidata item for HUN EDUCATION KFT. (confirmed zero Wikipedia article and, by inference, no populated Wikidata node); add a LinkedIn Company Page (none found linked from About/Costs/Contact); connect the four existing social profiles via `sameAs` schema once JSON-LD exists (item 3).
10. **Add author/Person schema using the two real named advisors** (Beyza Kantarcı, Çağla Nur Türken) already listed with direct contact details on `/contact/` — attach them as content authors/reviewers on the editorial pages. Low effort, genuine E-E-A-T gain since these are real people who already exist in the source, just disconnected from content.
11. **Add third-party source attribution** on every pricing/duration/visa claim — link to the specific university's own admissions page or to Study in Hungary/Tempus Public Foundation. Zero such outbound citations were found on the sampled pages (About, Costs); only the company's own social links appear.
12. **Build a genuine informational layer** answering the niche's actual long-tail questions directly ("Macaristan öğrenci vizesi nasıl alınır?", step-by-step with named requirements) — "Blog" already appears in the nav but resolves to 0 posts. Highest effort, highest ceiling item on this list.

### Low
13. Robots.txt is already fully AI-crawler-permissive on both hosts; no functional change required. Optionally add explicit named `User-agent` stanzas for GPTBot/OAI-SearchBot/ClaudeBot/PerplexityBot with `Allow: /` purely for documentation/clarity — behavior does not change, since the wildcard rule already allows them.
14. Fix image alt text: 1,851 of 2,614 images sitewide (70.8%) have no `alt` attribute (crawl-verified), which weakens multi-modal/image-citation potential (e.g. Google AI Overviews' use of image context) at negligible fix cost per image once a workflow exists.

---

## 8. Dimension Scoring (0-100, skill weighting)

| Dimension | Weight | Score | Weighted |
|---|---|---|---|
| Citability | 25% | 35 | 8.75 |
| Structural Readability | 20% | 30 | 6.0 |
| Multi-Modal Content | 15% | 25 | 3.75 |
| Authority & Brand Signals | 20% | 25 | 5.0 |
| Technical Accessibility | 20% | 45 | 9.0 |

**Total: 32.5 → 33/100**

Rationale for Technical Accessibility (45, the highest of the five despite the sitemap/title bugs): robots.txt is fully permissive to every AI crawler on both hosts and the site is plain server-rendered HTML with no JS-rendering barrier — both genuinely good foundations — but this is offset by a completely non-functional sitemap layer (0 of ~1,050+ pages declared) and the EN-host title-language bug, which is why the score sits at 45 rather than materially higher.

Score: 33/100
