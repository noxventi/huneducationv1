# Structured Data Implementation Plan — huneducation.com / tr.huneducation.com

Audit date: 2026-08-30. Method: 500-page crawl (`crawl.json`) + raw/rendered fetches of homepage, a `/course/` page (`pharmacy`, Elementor template ID 925), a `/university/` page (University of Pécs), `/about-us/`, `/contact/`, and the TR homepage.

## 1. Current State (one line)

**Zero structured data exists anywhere on either domain** — 0 JSON-LD blocks, 0 Microdata/RDFa, 0 `@type` occurrences across all 500 crawled pages (course, university, and editorial templates alike) — root cause: **"Schema & Structured Data for WP & AMP" and both Yoast SEO plugins are installed but INACTIVE**, so WordPress core only emits the bare minimum (`<title>`, a default `rel=canonical`, RSS/oEmbed links); there is also no meta description, no Open Graph, and **no hreflang** on the pages inspected, despite WPML being active (`meta name="generator" content="WPML ver:4.9.4"` and a working language switcher). This is a from-scratch build, not a fix-and-validate job.

Supporting evidence:
- Course page (`/course/pharmacy/`, template ID 925): `<head>` has title + robots + canonical only. `structured_data.block_count = 0`. No `og:*`, no `hreflang`, no `<meta name="description">`.
- University page (`/university/university-of-pecs/`): same pattern; `block_count = 0`.
- No review/rating/testimonial markup or content found anywhere on the pages sampled — there is no first‑party review collection mechanism on the site today.
- JetEngine fields render as plain labelled text inside `.jet-listing-dynamic-field__content` divs, e.g. `Price: 8 800`, `<span class="currency">eur</span>/year (2 semesters)`, `Semesters: 10`, `University: University of Pécs (PTE)`, `Type of Entrance Exam: …`, `Language certificate requested: …`. Body classes on the course template also expose taxonomy terms directly: `course-month-september course-year-243 course-city-pecs course-level-pharmacy-degree course-category-medicine-dentistry-pharmacy`.
- **Data-quality flag**: the `course-year` term slug observed live was `course-year-243`, not a year string (`2024`, `2025`…). Verify real term slugs/names before using this taxonomy to derive `startDate` — if it's genuinely corrupted (a WPML duplicate-slug collision is a common cause), fix it in WordPress before wiring `hasCourseInstance.startDate` to it, or the emitted dates will be wrong.

## 2. Prioritised Implementation Table

| # | Page type | Volume | Schema to add | Priority |
|---|---|---|---|---|
| 1 | All pages (both languages) | ~1,058 pages | `Organization` (or `EducationalOrganization`) + `WebSite` graph, referenced everywhere | **Critical** |
| 2 | `/course/*` (Elementor template 925) | 498 EN + 486 TR = 984 | `Course` + `Offer` + conditional `hasCourseInstance` + `BreadcrumbList` + `WebPage` | **Critical** |
| 3 | `/university/*` | 20 + 20 = 40 | `CollegeOrUniversity` + `BreadcrumbList` + `WebPage` | **High** |
| 4 | `/courses/` and `/universities/` hub + pagination (`/courses/2/` … `/courses/25/`) | ~50 | `CollectionPage` + `ItemList` (global position across pages) | **High** |
| 5 | 14 editorial pages ×2 languages (homepage excluded, counted separately) | 26 | `WebPage` (or `Article`/`BlogPosting` only where a real author + real date exists) + `BreadcrumbList` | **Medium** |
| 6 | Homepage EN + TR | 2 | `WebPage` referencing `WebSite`/`Organization`, `ItemList` of featured course links if present | **Medium** |
| 7 | `about-us` | 2 | Extend `Organization` with `foundingDate`, `address`, `contactPoint`, `sameAs` (fill the Organization node's detail here, not a duplicate type) | **Medium** |
| 8 | `contact` | 2 | `ContactPage` (`WebPage` subtype) + `Organization.contactPoint` reused | **Low** |
| 9 | Any existing/new FAQ content | n/a | **FAQPage is not worth adding** — Google retired FAQ rich results for all sites (7 May 2026); only consider `FAQPage` if the client explicitly accepts the SERP benefit is gone and any AI/GEO benefit is unconfirmed. If the site has genuine visitor Q&A (not present today), use `QAPage`, never `FAQPage`. | **Info only** |
| — | Any page | — | `HowTo`, `SpecialAnnouncement`, `CourseInfo`, `EstimatedSalary`, `LearningVideo` | **Do not implement — deprecated/retired** |
| — | Any page | — | `AggregateRating` / `Review` | **Do not implement now** — no genuine review collection exists (see §6) |

## 3. Architecture — `@id` Graph Wiring

WPML here runs on **separate subdomains** (`huneducation.com` = EN, `tr.huneducation.com` = TR), not subdirectories. Design rule: **one legal entity → one `Organization` node, reused by absolute `@id` across both hosts.** Everything else (`WebSite`, `WebPage`, `Course`, `CollegeOrUniversity`, `BreadcrumbList`) is **per-language, self-contained** — an EN page's graph must never reference a TR-only node and vice versa, or Google's Rich Results parser may merge or drop entities unpredictably.

```
https://huneducation.com/#organization        (Organization — SAME @id string embedded verbatim on BOTH domains)
https://huneducation.com/#website              (WebSite, inLanguage: en, publisher -> #organization)
https://tr.huneducation.com/#website           (WebSite, inLanguage: tr, publisher -> #organization)

Per EN page:  {url}#webpage  -> isPartOf {https://huneducation.com/#website}, breadcrumb -> {url}#breadcrumb
Per TR page:  {url}#webpage  -> isPartOf {https://tr.huneducation.com/#website}, breadcrumb -> {url}#breadcrumb

Per EN course:  {url}#course  -> provider -> {EN university url}#university (same language only)
Per TR course:  {url}#course  -> provider -> {TR university url}#university (same language only)

Per EN university: {url}#university (CollegeOrUniversity)
Per TR university: {url}#university (CollegeOrUniversity) -- add sameAs pointing to the EN twin URL for entity consolidation
```

Rationale: `@id` is just an IRI, it does not need to be dereferenceable — reusing the exact same string for `Organization` on both hosts is the correct, standard pattern for one company operating twin-language domains, and is what lets Google fold both language versions' Organization mentions into a single Knowledge-Graph-eligible entity. Everything downstream of `Organization` should stay language-scoped to avoid cross-language entity bleed.

## 4. JSON-LD Templates

### 4.1 Organization + WebSite (inject site-wide, in `wp_head`, both domains)

Real NAP confirmed on `/contact/`: `1204 Budapest, Bethlen utca 17, Hungary`, `info@huneducation.com`, phone pattern `+36-70-296-35-31`. The favicon found (`logo-huneducation-favicon-white.png`) is **not** a valid `Organization.logo` — Google requires a proper logo image, ideally ≥112×112px, not a favicon; source the real primary logo asset before shipping.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "EducationalOrganization",
      "@id": "https://huneducation.com/#organization",
      "name": "HUN EDUCATION KFT.",
      "alternateName": "HunEducation",
      "url": "https://huneducation.com/",
      "logo": {
        "@type": "ImageObject",
        "url": "https://huneducation.com/wp-content/uploads/[REPLACE-WITH-REAL-LOGO-NOT-FAVICON].png"
      },
      "foundingDate": "1999",
      "email": "info@huneducation.com",
      "telephone": "+36-70-296-35-31",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Bethlen utca 17",
        "postalCode": "1204",
        "addressLocality": "Budapest",
        "addressCountry": "HU"
      },
      "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+36-70-296-35-31",
        "contactType": "customer service",
        "email": "info@huneducation.com",
        "areaServed": "Worldwide",
        "availableLanguage": ["en", "tr", "hu"]
      },
      "sameAs": [
        "https://www.instagram.com/huneducation",
        "https://www.youtube.com/@huneducation",
        "https://www.facebook.com/HunEducationGLB"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://huneducation.com/#website",
      "url": "https://huneducation.com/",
      "name": "HunEducation",
      "inLanguage": "en",
      "publisher": { "@id": "https://huneducation.com/#organization" }
    }
  ]
}
```

TR homepage/site-wide block is identical except: `"@id": "https://tr.huneducation.com/#website"`, `"url": "https://tr.huneducation.com/"`, `"inLanguage": "tr"`, and the **`Organization` object is repeated verbatim with the identical `@id` string `https://huneducation.com/#organization`** (do not mint a second Organization `@id` on the TR subdomain — see §3/§5).

Note: use `EducationalOrganization` (a subtype of `Organization`) since HunEducation is an education consultancy — but see §6 for why it should **not** be reused as `Course.provider`.

### 4.2 Course template (Elementor ID 925 — JetEngine dynamic fields)

**Implementation mechanism**: because several fields are conditional (27%/25%/36% fill rates) and pricing needs light normalization (currency uppercasing), do **not** try to build this purely with Elementor's dynamic-tag picker in an HTML widget — implement as a small PHP snippet (mu-plugin or a code snippet manager, NOT inside a generic schema plugin) hooked to `wp_head`, scoped to `is_singular('course')`, reading the same JetEngine post-meta/taxonomy data the template already displays. Placeholders below use `{{field_slug}}` to name the exact JetEngine meta/taxonomy keys given in the brief.

```php
add_action( 'wp_head', function () {
    if ( ! is_singular( 'course' ) ) return;

    $post_id   = get_the_ID();
    $lang      = function_exists('icl_object_id') ? apply_filters('wpml_current_language', null) : 'en'; // 'en' | 'tr'
    $home      = ( $lang === 'tr' ) ? 'https://tr.huneducation.com' : 'https://huneducation.com';
    $url       = get_permalink( $post_id );

    $price      = get_post_meta( $post_id, 'course_price', true );              // e.g. "8800"
    $currency   = strtoupper( get_post_meta( $post_id, 'course_price_currency', true ) ); // "eur" -> "EUR"
    $semesters  = get_post_meta( $post_id, 'course_semesters', true );          // e.g. "10"
    $institute  = get_post_meta( $post_id, 'course_institute', true );         // e.g. "University of Pécs (PTE)"
    $deadline   = get_post_meta( $post_id, 'course_application_deadline', true ); // convert to YYYY-MM-DD before output
    $eng_level  = get_post_meta( $post_id, 'course_english_level', true );      // 27% filled — may be empty
    $entrance   = get_post_meta( $post_id, 'course_entrance_exam', true );      // 25% filled — may be empty
    $lang_cert  = get_post_meta( $post_id, 'course_language_certificate', true );// 36% filled — may be empty

    $city_terms  = get_the_terms( $post_id, 'course-city' );
    $level_terms = get_the_terms( $post_id, 'course-level' );
    $cat_terms   = get_the_terms( $post_id, 'course-category' );
    $month_term  = get_the_terms( $post_id, 'course-month' );
    $year_term   = get_the_terms( $post_id, 'course-year' ); // VERIFY slug integrity before using (see §1 flag)

    // ---- provider lookup: resolve course_institute -> matching /university/ CPT node ----
    // Prefer: if a JetEngine relation field to the university CPT exists, use its permalink + #university @id.
    // Fallback (institute is free text only): emit an inline CollegeOrUniversity object with name only (no @id link).
    $university_url = huneducation_lookup_university_url( $institute, $lang ); // custom helper, implement via slug match

    $graph = [];

    $course = [
        '@type'       => 'Course',
        '@id'         => $url . '#course',
        'url'         => $url,
        'name'        => get_the_title( $post_id ),
        'description' => wp_strip_all_tags( get_the_excerpt( $post_id ) ), // TODO: needs real unique meta descriptions, see §6
        'inLanguage'  => $lang,
        'provider'    => $university_url
            ? [ '@id' => $university_url . '#university' ]
            : [ '@type' => 'CollegeOrUniversity', 'name' => $institute ],
    ];

    if ( $cat_terms && ! is_wp_error( $cat_terms ) ) {
        $course['about'] = array_map( fn($t) => $t->name, $cat_terms );
    }
    if ( $level_terms && ! is_wp_error( $level_terms ) ) {
        $course['educationalLevel'] = $level_terms[0]->name; // flag: verify these map to real academic levels, see §6
    }

    if ( $price !== '' && $currency !== '' ) {
        $course['offers'] = [
            '@type'         => 'Offer',
            'url'           => $url,
            'price'         => $price,
            'priceCurrency' => $currency,        // must be ISO 4217, e.g. "EUR" not "eur"
            'category'      => 'Paid',
            'description'   => 'Annual tuition fee' . ( $semesters ? " (program length: {$semesters} semesters)" : '' ),
        ];
    }

    // Only emit hasCourseInstance when we have a trustworthy intake date AND a location.
    if ( $month_term && $year_term && ! is_wp_error( $month_term ) && ! is_wp_error( $year_term ) && $city_terms ) {
        $course['hasCourseInstance'] = [
            '@type'      => 'CourseInstance',
            'courseMode' => 'Onsite',
            'startDate'  => huneducation_month_year_to_iso( $month_term[0]->name, $year_term[0]->name ), // e.g. "2025-09-01" — VERIFY year term first
            'location'   => [
                '@type'   => 'Place',
                'name'    => $city_terms[0]->name,
                'address' => [ '@type' => 'PostalAddress', 'addressLocality' => $city_terms[0]->name, 'addressCountry' => 'HU' ],
            ],
        ];
    }

    // Optional recommended extras — only emit if non-empty, never emit empty strings/placeholders.
    if ( $eng_level !== '' )  $course['competencyRequired'][] = "English level: {$eng_level}";
    if ( $entrance !== '' )   $course['coursePrerequisites'][] = $entrance;
    if ( $lang_cert !== '' )  $course['coursePrerequisites'][] = "Language certificate: {$lang_cert}";

    $graph[] = $course;

    $graph[] = [
        '@type'          => 'WebPage',
        '@id'            => $url . '#webpage',
        'url'            => $url,
        'name'           => get_the_title( $post_id ),
        'isPartOf'       => [ '@id' => $home . '/#website' ],
        'inLanguage'     => $lang,
        'mainEntity'     => [ '@id' => $url . '#course' ],
        'breadcrumb'     => [ '@id' => $url . '#breadcrumb' ],
    ];

    $graph[] = [
        '@type'           => 'BreadcrumbList',
        '@id'             => $url . '#breadcrumb',
        'itemListElement' => [
            [ '@type' => 'ListItem', 'position' => 1, 'name' => 'Home',    'item' => $home . '/' ],
            [ '@type' => 'ListItem', 'position' => 2, 'name' => 'Courses', 'item' => $home . '/courses/' ],
            [ '@type' => 'ListItem', 'position' => 3, 'name' => get_the_title( $post_id ), 'item' => $url ],
        ],
    ];

    echo '<script type="application/ld+json">' . wp_json_encode(
        [ '@context' => 'https://schema.org', '@graph' => $graph ],
        JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE
    ) . '</script>' . "\n";
}, 20 );
```

Resulting example output (real data from `/course/pharmacy/`, illustrating the non-conditional fields only):

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "@id": "https://huneducation.com/course/pharmacy/#course",
      "url": "https://huneducation.com/course/pharmacy/",
      "name": "Medical Degree – Pharmacy M.D. (English)",
      "description": "[real unique description needed — see §6]",
      "inLanguage": "en",
      "provider": { "@id": "https://huneducation.com/university/university-of-pecs/#university" },
      "about": ["Medicine, Dentistry, Pharmacy"],
      "educationalLevel": "Pharmacy Degree",
      "offers": {
        "@type": "Offer",
        "url": "https://huneducation.com/course/pharmacy/",
        "price": "8800",
        "priceCurrency": "EUR",
        "category": "Paid",
        "description": "Annual tuition fee (program length: 10 semesters)"
      }
    }
  ]
}
```

### 4.3 University pages (`/university/*`)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "CollegeOrUniversity",
      "@id": "https://huneducation.com/university/university-of-pecs/#university",
      "name": "University of Pécs (PTE)",
      "url": "https://huneducation.com/university/university-of-pecs/",
      "foundingDate": "1367",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Pécs",
        "addressCountry": "HU"
      },
      "description": "[unique meta description text]",
      "sameAs": []
    },
    {
      "@type": "WebPage",
      "@id": "https://huneducation.com/university/university-of-pecs/#webpage",
      "url": "https://huneducation.com/university/university-of-pecs/",
      "isPartOf": { "@id": "https://huneducation.com/#website" },
      "inLanguage": "en",
      "mainEntity": { "@id": "https://huneducation.com/university/university-of-pecs/#university" },
      "breadcrumb": { "@id": "https://huneducation.com/university/university-of-pecs/#breadcrumb" }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://huneducation.com/university/university-of-pecs/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://huneducation.com/" },
        { "@type": "ListItem", "position": 2, "name": "Universities", "item": "https://huneducation.com/universities/" },
        { "@type": "ListItem", "position": 3, "name": "University of Pécs (PTE)", "item": "https://huneducation.com/university/university-of-pecs/" }
      ]
    }
  ]
}
```

Do not add `foundingDate`/history facts to the `Organization` node — those belong to the university entity (e.g. "Founded in 1367") and must stay separate from HUN EDUCATION KFT.'s own `foundingDate` (1999). These are two different entities; conflating them is the single easiest schema mistake to make on this site.

### 4.4 Editorial pages (WebPage + BreadcrumbList; Article only where justified)

None of the sampled pages exposed a real `datePublished`/`dateModified` in HTML (htmldate could only guess "today" as a fallback, meaning no visible date signal exists). WordPress core still has real `post_date`/`post_modified` values independent of Yoast — pull dates from there via `get_the_date('c')`/`get_the_modified_date('c')`, but **verify they reflect true publish history and are not all set to a migration date** before using them in `Article.datePublished` (a required Google property for Article rich results).

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://huneducation.com/why-hungary/#webpage",
      "url": "https://huneducation.com/why-hungary/",
      "name": "[H1 / title]",
      "isPartOf": { "@id": "https://huneducation.com/#website" },
      "about": { "@id": "https://huneducation.com/#organization" },
      "inLanguage": "en",
      "breadcrumb": { "@id": "https://huneducation.com/why-hungary/#breadcrumb" }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://huneducation.com/why-hungary/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://huneducation.com/" },
        { "@type": "ListItem", "position": 2, "name": "Why Hungary", "item": "https://huneducation.com/why-hungary/" }
      ]
    }
  ]
}
```

Use `Article`/`BlogPosting` instead of `WebPage` **only** for pages with a verifiable author + real `datePublished` (candidates: `student-perspectives`, `university-life`, possibly `masters`/`medicine`/`pilot-training` if written by a named advisor) — add `headline`, `image`, `author` (Person or the Organization), `datePublished`, `dateModified`, `publisher` (`{@id}` to Organization). Do **not** apply Article to `about-us`, `contact`, `courses`, `universities`, `admission`, `costs` — these are utility/hub pages, keep them `WebPage`/`CollectionPage`/`ContactPage`.

**FAQPage**: do not add proactively. If the client still wants it for possible AI/GEO surfacing despite zero Google SERP benefit (FAQ rich results retired for all sites 7 May 2026), scope it narrowly to pages with genuine, already-published Q&A copy — never fabricate questions to qualify.

### 4.5 ItemList for `/courses/` and `/universities/` hubs

Both hubs paginate (`/courses/2/` … observed up to `/courses/25/`, consistent with ~498 EN courses at ~20/page). `position` must be **global**, not reset per page.

```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "@id": "https://huneducation.com/courses/#webpage",
  "url": "https://huneducation.com/courses/",
  "isPartOf": { "@id": "https://huneducation.com/#website" },
  "mainEntity": {
    "@type": "ItemList",
    "@id": "https://huneducation.com/courses/#itemlist",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "url": "https://huneducation.com/course/pharmacy/" },
      { "@type": "ListItem", "position": 2, "url": "https://huneducation.com/course/medicine-bsc/" }
    ]
  }
}
```

For `/courses/2/`: same `@type`/`@id` pattern at `.../courses/2/#webpage`, but `position` continues from wherever page 1 left off (e.g. 21, 22, 23…) using `(page_number - 1) * posts_per_page + index + 1`. Do the same for `/universities/`.

## 5. WPML / Multi-domain Notes

1. **Fix hreflang first** — none was found on the sampled pages despite WPML being active with a working language switcher menu. This is a prerequisite for any language-aware schema to be trustworthy: without `hreflang`, Google has no reliable signal that `huneducation.com/course/pharmacy/` and its `tr.huneducation.com` counterpart are the same entity in two languages, which weakens the value of any `@id` cross-referencing described in §3. Enable WPML's hreflang output (Settings → Languages → "Language URL format" / SEO options) site-wide, including on the Elementor course/university templates.
2. **Never duplicate the `Organization` `@id`** — embed the byte-identical `Organization` JSON-LD object (same `@id`: `https://huneducation.com/#organization`) on both domains. Do not let the TR site mint `https://tr.huneducation.com/#organization` as a second entity.
3. **Every other node is per-language** — `WebSite`, `WebPage`, `Course`, `CollegeOrUniversity`, `BreadcrumbList`, `ItemList` must use the current page's own host in their `@id`/`url`, and `Course.provider`/breadcrumb links must resolve to same-language URLs only (an EN course page must link to the EN `/university/...` page, never the TR one).
4. **Dynamic fields must read the current translation's data**, not fall back to EN defaults. When resolving `course_institute`, `course_price`, taxonomy terms, etc. inside the PHP snippet in §4.2, confirm the JetEngine meta and WPML taxonomy term translations are being read for `get_the_ID()` of the *current* translated post (JetEngine custom fields are typically per-post, but taxonomy term translations depend on WPML's term-translation setup — verify `course-level`/`course-category`/`course-city` term names are actually translated into Turkish, not just the taxonomy labels).
5. **`inLanguage`** must be `"en"` on huneducation.com and `"tr"` on tr.huneducation.com everywhere (Organization stays language-neutral / omit `inLanguage` on it).
6. Add `sameAs` between twin `CollegeOrUniversity` nodes (EN ⇄ TR) for the same 20 institutions so Google can consolidate them as one real-world entity across languages.

## 6. Validation Risks & Guardrails

1. **Do not set `Course.provider` to HUN EDUCATION KFT.** HunEducation is a placement consultancy, not the degree-granting institution — the real provider is the Hungarian university (`CollegeOrUniversity`). Mislabeling the consultancy as the course provider is a misrepresentation risk under Google's structured-data guidelines. Link `Course.provider` to the matching `/university/` `@id` instead (Organization can still appear as `sponsor`/publisher of the *page*, not as the academic provider of the *course*).
2. **`course_institute` may be free text, not a relation.** Confirm with the dev team whether it's a JetEngine relationship field to the university CPT or a plain string. If it's free text, the provider `@id` lookup in §4.2 needs a reliable name→URL mapping (slugify + match, or better: convert it to a true relation field) across ~984 course pages before shipping — a fuzzy/broken match will silently produce wrong or missing `provider` links.
3. **No `AggregateRating`/`Review` — ever, unless a real review system is built.** No testimonials, star ratings, or review collection mechanism were found anywhere on the site. Fabricating or reusing marketing testimonials as `Review`/`AggregateRating` violates Google's structured-data policies (misleading markup, review scam) and puts the whole domain's rich-result eligibility at risk. Only add this after a genuine, verifiable student review pipeline exists (e.g., Trustpilot integration, verified on-site reviews).
4. **`course-year` taxonomy slug anomaly** (`course-year-243` observed instead of a year) — verify all `course-year` term slugs/names are clean years before deriving `hasCourseInstance.startDate` from `course-month` + `course-year`. If corrupted, fix the taxonomy data first or omit `hasCourseInstance` entirely (it's optional/recommended, not required).
5. **`Course` required properties**: Google requires `name` + `description` at minimum for any Course markup to be valid. Course pages currently have **no meta description at all** (SEO plugin inactive) — `description` must not be left blank or filled with boilerplate/placeholder text; either write real unique descriptions per course or reliably derive one from the post excerpt/first content paragraph (already-existing body copy, not fabricated).
6. **Partially-filled fields (`course_english_level` 27%, `course_entrance_exam` 25%, `course_language_certificate` 36%)**: never emit empty-string properties or placeholder text like "N/A" — conditionally omit the property entirely when the JetEngine field is empty (as shown in the PHP snippet). Emitting empty/placeholder values fails Google's "no placeholder text" validation rule and can look manipulative on ~700+ of the ~984 course pages combined.
7. **Currency normalization**: the visually displayed currency is lowercase (`eur`); `Offer.priceCurrency` must be a valid uppercase ISO 4217 code (`EUR`, `USD`, `HUF`). Confirm the underlying `course_price_currency` meta value and uppercase it at output time if needed.
8. **Price semantics**: `course_price` on the sampled page is an **annual** tuition figure ("…/year (2 semesters)"), not total program cost. Don't let `Offer.price` be misread as full-program price — the `description` field in the Offer template clarifies this; consider a `PriceSpecification`/`unitText` upgrade later if Google surfaces this ambiguously in rich results.
9. **Deprecated types — do not use anywhere**: `HowTo` (removed Sept 2023), `SpecialAnnouncement` (deprecated Jul 2025), `CourseInfo`/`EstimatedSalary`/`LearningVideo` (retired Jun 2025). None were found on the site, but avoid the temptation to use `HowTo` for "how to apply" content — use plain `WebPage`/`Article` with normal headings instead.
10. **`FAQPage` — info only.** No Google SERP benefit since the 7 May 2026 retirement of FAQ rich results for all sites. Do not treat it as a priority; if implemented at all, scope to genuine existing Q&A copy and set expectations that only unconfirmed AI/GEO value remains. Genuine user Q&A (if ever built) should use `QAPage`.
11. **Avoid duplicate markup.** Both dormant plugins ("Schema & Structured Data for WP & AMP", Yoast SEO/Yoast SEO Premium) can independently emit generic `Organization`/`Article`/`BreadcrumbList` blocks if reactivated. If any of them are turned on later (e.g., just for basic meta descriptions/OG tags), explicitly disable their schema/structured-data output modules, or you will end up with two competing `Organization`/`BreadcrumbList` graphs on the same page — the custom mu-plugin approach in §4 should be the single source of truth for JSON-LD.
12. **Logo asset**: replace the favicon currently in use with a real, adequately sized logo file before publishing `Organization.logo`.

## 7. Rollout Order (suggested)

1. Fix WPML hreflang output (prerequisite, not schema itself, but blocks correct language wiring).
2. Ship §4.1 Organization/WebSite graph site-wide (both domains) — quick win, unlocks Knowledge Panel eligibility.
3. Ship §4.2 Course template via mu-plugin (984 pages in one deployment) — biggest volume, biggest AI/GEO and rich-result surface area, but gate on resolving the provider-lookup (#2 above) and description-content gap (#5 above) first.
4. Ship §4.3 University pages (40 pages, mostly static — can hand-write per page).
5. Ship §4.4 editorial WebPage/BreadcrumbList (26 pages) and §4.5 ItemList hubs.
6. Re-audit with Rich Results Test / Search Console after each wave before moving to the next.
