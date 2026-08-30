# Performance Audit — huneducation.com

**Date:** 2026-08-30
**Tooling:** Lighthouse 13.4.1 (CLI, mobile default preset, simulated throttling), run against a local Playwright Chromium binary. PageSpeed Insights API and CrUX/GSC field data were **not available** in this environment (no Google API key configured; the anonymous PSI quota returned `429 rate limit exceeded` on every attempt).

## Coverage — read this first

**Only the homepage (`https://huneducation.com/`) was successfully measured** before the turn budget for this task ran out. The other three required URLs were **not measured**:

- `https://huneducation.com/courses/` — NOT MEASURED
- `https://huneducation.com/course/pharmacy/` — NOT MEASURED
- `https://tr.huneducation.com/macaristanda-universite/` — NOT MEASURED

Everything below the homepage numbers (plugin-cost breakdown, caching analysis, prioritized fixes) is derived from the homepage trace plus static knowledge of the declared plugin stack, and is called out as inferred/not directly measured where it applies to the other three URLs. Given that `/courses/` is stated to be 653 KB of HTML (2.4x the homepage) and JetEngine/JetSearch-heavy, it should be treated as the **highest-risk unmeasured page** and re-tested first once PSI/CrUX access or a stable Lighthouse run is available.

## Lab vs. field data — explicit caveat

**This is 100% lab data from a single Lighthouse run.** No CrUX field data, no Google Search Console field data, no PSI field percentiles were available (no credentials configured). Lab data reflects one simulated mobile device/network condition, not the distribution of real user visits, and Google's Core Web Vitals pass/fail assessment is based on the **75th percentile of real-user (CrUX) data**, which cannot be computed here. Treat every number below as directional/diagnostic, not a ranking-determining figure. FID is not referenced anywhere (correctly deprecated); INP has no lab equivalent in Lighthouse, so **Total Blocking Time (TBT) is used as the INP proxy**, per standard practice.

---

## Homepage — https://huneducation.com/ (measured)

**Lighthouse Performance score: 60/100** (mobile, simulated throttling)

| Metric | Value | CWV threshold | Status |
|---|---|---|---|
| LCP (headline, simulated/Lantern) | **12.7 s** | good is 2.5s or less | **Poor** (over 4.0s) |
| LCP breakdown (trace-observed, see caveat) | TTFB 0.83s + load delay 0.62s + load duration 0.43s + render delay 0.02s, sums to about 1.9s | — | See note below |
| TBT (INP proxy) | **39 ms** | INP good is 200ms or less | Good-range proxy, but TBT under-predicts real INP when 51 render-blocking resources + 3 GTM containers are present |
| CLS | **0.056** | good is 0.1 or less | **Good** |
| FCP | 5.3 s | — | Poor |
| Speed Index | 5.8 s | — | Poor |
| Time to Interactive | 16.6 s | — | Poor |
| Max Potential FID (legacy diagnostic, not a CWV) | 97 ms | — | informational only |
| TTFB (server-response-time audit) | **493 ms** (root document) | Well above the roughly 200ms "good" TTFB guidance | Poor — confirms "no active caching" |
| Total transferred bytes | **2,074 KiB (about 2.03 MB)** | — | Heavy for a homepage |
| Total requests | **125** | — | High |

**Note on the LCP discrepancy:** Lighthouse's headline LCP (12.7s) is computed via simulated/Lantern throttling over the full resource dependency graph, while the `lcp-breakdown-insight` sums the trace-observed sub-phases to only about 1.9s. These two Lighthouse-internal computation methods diverge sharply on this page — a strong signal in itself that the resource graph (51 render-blocking requests queued over HTTP/1.1, max about 6 connections/origin) is the bottleneck Lantern is penalizing. Both figures are lab estimates; neither should be read as an exact real-world LCP without CrUX confirmation.

### Render-blocking resources (51 items flagged, top offenders by estimated cost)

`render-blocking-insight`: **Est. savings of 3,800 ms**. Worst individual blockers:
- `wp-content/plugins/wp-whatsapp-chat/.../style.css` (Social Chat plugin) — 7.6 KB, **1,034 ms** wasted (single biggest render-blocking cost on the page)
- `wp-includes/js/jquery/jquery.min.js` — 30.8 KB, 1,240 ms wasted
- `wp-content/cache/asp/style.basic-....css` (Ajax Search Pro) — 4.6 KB, 827 ms
- `wp-content/plugins/jet-search/assets/css/jet-search.css` — 8.2 KB, 827 ms
- `wp-includes/js/jquery/jquery-migrate.min.js` — 5.3 KB, 827 ms
- Multiple per-post Elementor CSS files (`post-1630.css`, `post-8607.css`, `post-393.css`, `post-10.css`, etc.) — 621–827 ms each
- Elementor-Pro widget CSS (nav-menu, sticky, testimonial-carousel, slides, form, carousel-module-base) — 621 ms each
- `jet-search/assets/lib/chosen/chosen.min.css` — 621 ms

**All 51+ blocking resources load over HTTP/1.1** (`modern-http-insight`: est. 3,310 ms savings from moving to HTTP/2+) — confirmed no CDN/HTTP2-terminating proxy is in front of the origin.

### Biggest byte offenders (by transfer size)

| Size | Type | Resource |
|---|---|---|
| 451.4 KiB | Image | `wp-content/uploads/2023/03/background-students.jpg` (hero background, 28% of page weight alone) |
| 186.6 KiB | Script | GTM container `G-88T4Y5BXLQ` |
| 163.7 KiB | Script | GTM container `G-BE3QXVJREL` (dataLayerPYS = PixelYourSite) |
| 123.4 KiB | Script | GTM/gtag container `UA-200599493-1` — **legacy Universal Analytics property, dead since GA4 migration; UA stopped processing in mid-2024** — pure waste |
| 105.1 KiB | Script | `connect.facebook.net/en_US/fbevents.js` (Facebook Pixel, via PixelYourSite) |
| 74.7 KiB | Font | JetMenu Font Awesome `fa-solid-900.woff2` (full icon set for a handful of menu icons) |
| 66.8 KiB | Script | Facebook Pixel signals/config beacon |
| 49.8 KiB | Document | homepage HTML itself |
| 40.1 KiB | Script | PixelYourSite `tld.min.js` |
| 39.2 KiB | Script | Elementor Swiper carousel lib (22.7 KB unused) |
| 36.7 KiB | Font | Google Fonts Roboto woff2 |
| 33.7 KiB | Script | **JetMenu's bundled Vue 2 runtime** (`vue.min.js?ver=2.6.11`) |
| 30.9 KiB | Script | Ajax Search Pro cached bundle (21.3 KB unused/dead code) |
| 30.0 KiB | Script | jQuery core |
| 27.4–27.7 KiB each | Images | `hungary-2.png`, plus `idea.png`/`books.png`/`graduated.png` — all served at 512x512 but displayed at 106x106 (about 66 KB combined wasted from missing responsive sizing) |

Unused code found: **33 KiB unused CSS** (jet-elements.css 21.6 KB unused, jet-menu Font Awesome CSS 12.4 KB unused) and **358 KiB unused/uncached-appropriately JS**, dominated by the 3 GTM containers, Facebook pixel, jet-elements.min.js (23.5 KB unused) and Swiper (22.7 KB unused).

Google Fonts: **3 separate font families loaded** (Roboto, Open Sans, Poppins) totaling 119.5 KB, render-blocking via `<link>` CSS, contributing to `font-display-insight`'s 120ms est. savings (FOIT risk).

### Third-party cost, broken down by plugin/vendor

| Vendor / Entity | Transfer size | Main-thread time | Likely source plugin(s) in this stack |
|---|---|---|---|
| Google Tag Manager (3 separate containers: 2x GA4 + 1x legacy UA) | **484,988 bytes (about 474 KB)** | 62.5 ms | MonsterInsights (GA/UA) + PixelYourSite (GTM/GA4 duplication) — **running two analytics plugins is firing 3 overlapping Google tags on every pageview** |
| Facebook (Pixel + Conversions API beacon) | **176,104 bytes (about 172 KB)** | 37.5 ms | PixelYourSite |
| Google Analytics (legacy `analytics.js` + collect beacon) | 21,816 bytes | 4.6 ms | MonsterInsights |
| Google Fonts | 119,509 bytes | 0 ms (but render-blocking) | Theme/Elementor global fonts, not a plugin in the stack list but compounds the same "too many external origins" problem |
| **Third-party total** | **about 802 KB (about 39% of total page weight)** | — | — |

Plugin assets that load site-wide from the declared stack, evidenced directly in this trace:
- **JetMenu**: Vue 2 runtime (33.7 KB) + Font Awesome icon webfont (74.7 KB) + `public.css`/theme-integration CSS (all HTTP/1.1, several flagged render-blocking) — loads on every page regardless of whether the mega-menu is the active nav widget on that template.
- **Elementor Pro nav-menu widget CSS** (`widget-nav-menu.min.css`) was *also* enqueued alongside JetMenu's own menu CSS on the homepage — worth verifying only one mega-menu system is actually rendered; if Elementor Pro's native nav menu isn't used anywhere, its widget CSS/JS should be excluded via Elementor's "unused widget" controls.
- **JetElements**: `jet-elements.css`/`.js` loaded with 21.6 KB CSS + 23.5 KB JS unused on this specific page — indicates JetElements widgets are enqueued sitewide even where none of its widgets are placed on the page.
- **Ajax Search Pro (JetSearch assets also present in the trace)**: CSS/JS + a "chosen" select-box library loading on the homepage even though the visible search widget is likely a single input — 827 ms of blocking cost from just its CSS.
- **Social Chat** (`wp-whatsapp-chat` plugin): single biggest render-blocking CSS cost on the page (1,034 ms) plus 56.6 ms of JS bootup — for a floating chat bubble that could be deferred until after first paint.
- **PixelYourSite**: orchestrates the GTM containers + Facebook Pixel load (about 660 KB combined) plus its own 40.1 KB `tld.min.js` — the single largest contributor to third-party weight.
- **JetTabs / JetTricks**: not directly visible in the homepage's top-cost lists (they likely contribute smaller CSS/JS bundles that still register in `modern-http-insight`'s HTTP/1.1 list but weren't singled out in top-15 by size) — **not conclusively isolated in this trace; verify on templates that don't use tabs, e.g. `/course/pharmacy/`, once that URL is retested.**

### Caching plugins: all four installed, all four inactive — evidence and impact

Confirmed directly from response headers (captured separately via header fetch of `/`):

```
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Set-Cookie: PHPSESSID=...   (a PHP session is started on every anonymous homepage hit)
Server: Apache
```

Combined with `modern-http-insight` showing every single asset served over **HTTP/1.1** (no HTTP/2, no HTTP/3, no CDN edge), this is conclusive: **no page cache, no object cache, no HTTP/2 termination, and no image optimization are active anywhere in the delivery path**, matching the stated "installed but inactive" status of WP Rocket, WP Fastest Cache, LiteSpeed Cache and Smush.

**Two specific blockers worth fixing before/while turning caching plugins on:**
1. **`Set-Cookie: PHPSESSID` fires on every anonymous request.** A live PHP session on every hit will bypass or fragment full-page HTML caching in WP Rocket/WP Fastest Cache/LiteSpeed Cache unless the plugin/theme starting the session (commonly Ajax Search Pro or a login/cart-adjacent plugin) is configured not to start sessions for anonymous visitors. This must be resolved or the cache hit-rate will be poor even after activation.
2. **`Server: Apache`, not LiteSpeed Web Server (LSWS/OpenLiteSpeed).** The LiteSpeed Cache plugin's headline benefit (server-level page cache + ESI) requires an actual LiteSpeed-family web server; on plain Apache it degrades to a slower, PHP-driven equivalent of WP Rocket. **Do not run LiteSpeed Cache and WP Rocket simultaneously** — pick one full-page cache plugin (WP Rocket is the more complete choice here given its JS-delay and CSS-optimization features) and leave the others deactivated to avoid double-caching conflicts.

**Plausible impact of turning caching on (estimates from measured baseline, not re-tested):**
- **TTFB 493-830 ms to about 80-150 ms**: serving cached static HTML instead of a full WP bootstrap on every request typically cuts TTFB by 70-85% on comparable Apache/WordPress stacks (assuming the PHPSESSID issue above is fixed first).
- **Render-blocking savings (3,800 ms Lantern estimate) largely recoverable**: WP Rocket's CSS/JS minify+combine and "load JS after user interaction" (delay JS) features are a near-exact match for this page's problem (3 GTM containers + FB pixel + ASP + WhatsApp chat all currently parse-blocking on load).
- **Smush reactivation** directly targets the two measured image findings: `image-delivery-insight` (175 KB est. savings from WebP/AVIF + correct sizing) and the 66 KB wasted on the three 512x512 icon PNGs displayed at 106x106.
- **HTTP/2 (via CDN or LiteSpeed/Enterprise hosting change)** recovers the 3,310 ms `modern-http-insight` estimate by removing the 6-connections-per-origin bottleneck that is currently serializing 125 requests.

None of the above are re-measured post-fix (no before/after test was run); they are extrapolations from the specific Lighthouse findings above and standard behavior of these plugins on comparable WordPress/Apache stacks.

---

## Pages NOT measured (explicitly out of scope for this report)

- **`/courses/` (653 KB HTML, heaviest page)**: expected to be the worst performer — JetEngine listing grids + JetSearch/Ajax Search Pro filtering UI + likely dozens of course thumbnail images. Should be retested first.
- **`/course/pharmacy/` (141 KB HTML)**: a single detail page; useful to confirm whether JetTabs/JetTricks assets are being loaded here even if unused, and to check LCP on a page with a different hero treatment.
- **`tr.huneducation.com/macaristanda-universite/` (233 KB, Turkish homepage)**: on a subdomain — worth checking whether it shares the same caching/no-cache header pattern, and whether it duplicates the same 3x GTM/analytics tags for a second time (double-counting if PixelYourSite/MonsterInsights are configured per-subdomain).

---

## Prioritized remediation list

| # | Fix | Plugin/area | Expected impact | Effort |
|---|---|---|---|---|
| 1 | Fix the anonymous `PHPSESSID` session start, then activate one full-page cache (WP Rocket recommended) with CSS/JS minify + combine + "delay JS execution" enabled | Core WP + WP Rocket | TTFB 493 to about 100ms; recovers much of the 3,800ms render-blocking estimate; single highest-leverage fix available | Medium (session fix needs debugging which plugin starts it; cache config is quick) |
| 2 | Reactivate Smush, enable WebP/AVIF + auto-resize; compress `background-students.jpg` and resize `idea.png`/`books.png`/`graduated.png` to their displayed dimensions | Smush + media library | About 175 KB + about 66 KB saved (roughly 240 KB, about 12% of page weight), direct LCP-image win | Low |
| 3 | Consolidate tracking: remove the redundant legacy Universal Analytics tag (`UA-200599493-1`, dead since 2024) and reconcile MonsterInsights vs. PixelYourSite so only one GTM/GA4 container fires; move Facebook Pixel + remaining GTM to load after first interaction or via a facade | MonsterInsights + PixelYourSite | Removes about 123 KB dead UA script outright; defers about 660 KB / about 100ms main-thread time off the critical path | Low-Medium |
| 4 | Defer/lazy-load the Social Chat (WhatsApp) widget CSS/JS until after first paint (currently the single biggest render-blocking cost, 1,034ms) | Social Chat (wp-whatsapp-chat) | Removes the largest individual render-blocking entry | Low |
| 5 | Audit JetMenu/JetElements/JetSearch/JetTabs/JetTricks enqueues per-template; dequeue JetElements CSS/JS and JetMenu's Vue 2 + Font Awesome bundle on templates that don't use them (verify Elementor Pro's native nav-menu isn't double-loaded alongside JetMenu) | JetEngine suite + Elementor Pro | About 33 KB unused CSS + about 23.5 KB unused JS removed on homepage alone; likely larger savings on `/course/pharmacy/` if confirmed unused there | Medium (requires per-template asset conditionals, e.g. Elementor's "Improve Asset Loading" / Asset Manager) |
| 6 | Move hosting/CDN to get HTTP/2 or HTTP/3 (Cloudflare or equivalent in front of Apache, or migrate to true LiteSpeed/OpenLiteSpeed if activating LiteSpeed Cache) | Infrastructure | Recovers about 3,310ms `modern-http-insight` estimate from connection-limit queuing across 125 requests | Medium-High (infra change) |
| 7 | Consolidate Google Fonts to 1-2 families, self-host the used weights only, confirm `font-display: swap`, preload the LCP-critical weight | Theme/Elementor global fonts | 119.5 KB likely reduced to under 30 KB; removes render-blocking font CSS | Low |
| 8 | Re-run this audit on `/courses/`, `/course/pharmacy/`, and the Turkish homepage once the above are in place, and obtain a Google API key so PSI/CrUX field data can supplement lab data | Process | Confirms real-world (75th percentile) pass/fail vs. this single lab run | Low |

**Score: 60/100**
