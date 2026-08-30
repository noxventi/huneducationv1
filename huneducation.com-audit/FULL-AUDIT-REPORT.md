# huneducation.com — Kapsamlı SEO, GEO ve Sağlık Denetimi

**Tarih:** 2026-08-30   ·   **Taranan sayfa:** 500   ·   **Tahmini site boyutu:** ~1052 URL

**İş modeli:** Education consultancy / study-abroad agency (Türkiye → Macaristan). WordPress + Elementor Pro + JetEngine + WPML, dil başına alan adı.


---

## Yönetici özeti

# SAĞLIK SKORU: 31 / 100

> Bu skor, kategorileri ağırlıklandırılmış ortalamadır. 31 puan, "kırık değil ama kapatılmış" bir siteyi tarif eder: altyapı satın alınmış, kurulmuş ve sonra devre dışı bırakılmış. İyi haber, düzeltmelerin çoğunun içerik üretmeyi değil **anahtar çevirmeyi** gerektirmesi.


### Kategori skorları

| Kategori | Skor | Ağırlık |
|---|---|---|
| Technical SEO | **32**/100 | 22% |
| Content Quality | **34**/100 | 23% |
| On-Page SEO | **25**/100 | 20% |
| Schema / Structured Data | **6**/100 | 10% |
| Performance (CWV) | **60**/100 | 10% |
| AI Search Readiness (GEO) | **33**/100 | 10% |
| Images | **25**/100 | 5% |

Ağırlıklandırılmayan ek ölçümler: Sitemap/keşfedilebilirlik **14**/100 · Arama deneyimi (SXO) **38**/100 · Görsel/mobil **42**/100 · Otorite/backlink *ölçülemedi*.


### En kritik beş bulgu

1. Programların ilan edilen son başvuru tarihlerinin %100’ü geçmiş (965/965); katalog 14 ay bayat.
2. Sitemap fiilen boş: her iki alan adında 2 URL bildiriliyor, ~1.052 URL var. WordPress’in kendi sitemap’i dolu ama HTTP 404 ile sunuluyor.
3. Sıfır yapısal veri, sıfır hreflang, sıfır Open Graph; 494/500 sayfada meta description yok. Kök sebep: Yoast / WPML SEO / Schema eklentileri kurulu ama PASİF.
4. İngilizce ana sayfanın <title> etiketi tamamen Türkçe; lang=en-US ve H1 İngilizce.
5. Önbellek yok ve önbelleklenemez: her istek Cache-Control: no-store + PHPSESSID dönüyor; güvenlik başlığı hiç yok.

### En hızlı beş kazanç

1. EN ana sayfa <title> etiketini İngilizce yaz (dakikalar)
2. Auctollo sitemap eklentisini kapat, Yoast’ı etkinleştir → ~1.052 URL bildirilebilir hâle gelir
3. WPML SEO’yu etkinleştir → hreflang çıkar, EN/TR aynı sorguda birbirini yemekten kurtulur
4. İngilizce sitedeki Türkçe WhatsApp widget metnini dile göre ayarla
5. PHP 8.0’dan 8.2/8.3’e çık (destek dışı sürüm)

---

## Kök sebep: SEO altyapısı kurulu ama kapalı

Denetimdeki kritik bulguların çoğu tek bir olguya iniyor. Aşağıdaki eklentiler sitede **kurulu** ama **pasif**:

| Eklenti | Pasif olmasının sonucu |
|---|---|
| Yoast SEO 27.6 + Premium 20.9 | 494/500 sayfada meta description yok, sitemap yok, OG yok |
| WPML SEO 2.2.5 | hreflang hiç yok — EN ve TR aynı sorguda birbiriyle yarışıyor |
| Schema & Structured Data 1.60 | site genelinde sıfır yapısal veri |
| WP Rocket / WP Fastest Cache / LiteSpeed | önbellek yok |
| Smush Pro | görsel optimizasyonu yok |

Bunun yerine çalışan **Auctollo "XML Sitemap Generator for Google" v4.1.23**, WordPress’in kendi sitemap’ini de gölgeliyor. Sonuç: `/wp-sitemap-posts-course-1.xml` 498 geçerli URL içeriyor ama **HTTP 404** ile sunuluyor; `/wp-sitemap.xml` 200 dönüyor ama boş. Google hiçbirini kullanamıyor.


---


## Technical SEO — 32/100

**Çalışan yanlar**

- Canonical 500/500 sayfada doğru, hiçbiri yanlış hedefe işaret etmiyor
- Yanlışlıkla noindex konmuş sayfa yok
- robots.txt taramayı engellemiyor; tüm AI tarayıcılarına açık
- http→https ve www→kök yönlendirmeleri tek adımda, 301


### 🔴 Kritik — Sitemap fiilen boş (2 URL / ~1.052)

sitemap.xml → sitemap-misc.xml yalnızca ana sayfa ve /sitemap.html içeriyor. WordPress'in kendi /wp-sitemap-posts-course-1.xml dosyası 498 geçerli <loc> taşıyor ama HTTP 404 ile sunuluyor; /wp-sitemap.xml 200 dönüyor ama boş. Aynı desen tr.huneducation.com’da da var (486 program).

**Düzeltme:** Auctollo 'XML Sitemap Generator for Google' eklentisini kapat, Yoast SEO'yu etkinleştir; her alan adı için post-tipi bazlı sitemap index kur.

### 🔴 Kritik — Güvenlik başlığı hiç yok

HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy — hiçbiri yok (iki alan adında da).

**Düzeltme:** En azından HSTS, X-Content-Type-Options: nosniff, Referrer-Policy ve X-Frame-Options ekle.

### 🟠 Yüksek — Önbelleklenemez yanıt + oturum çerezi

Anonim ana sayfa isteği: Cache-Control: no-store, no-cache, must-revalidate + Expires: 1981 + Set-Cookie: PHPSESSID. Bu kombinasyon sayfa önbelleğini ve CDN’i peşinen devre dışı bırakır; önbellek eklentisi kurulsa bile çalışmaz.

**Düzeltme:** session_start() çağıran eklentiyi bul (Ajax Search Pro / Social Chat adayları), anonim isteklerde oturum açılmasını durdur; sonra tek bir önbellek eklentisi etkinleştir.

### 🟡 Orta — HTTP/1.1, CDN yok

125 istek HTTP/1.1 üzerinden; paralellik sınırlı.

**Düzeltme:** HTTP/2 desteğini aç; statik varlıklar için CDN değerlendir.


## Content Quality — 34/100

**Çalışan yanlar**

- Açıklaması olan program sayfaları ince değil (~330 kelime, gerçek prosa + benzersiz alan verisi)
- İki dil gerçekten ayrı yazılmış; makine çevirisi izlenimi yok
- /about-us/ bağımsızlık beyanı ve kuruluş yılı gibi doğru güven unsurlarını içeriyor


### 🔴 Kritik — Son başvuru tarihlerinin %100’ü geçmiş

Tarih girilmiş 965 programın 965’inde son başvuru tarihi geçmiş (892’si 2025). course-year taksonomisinde 2026 kaydı yok. En son düzenlenen program: 2026-03-09.

**Düzeltme:** 2026-27 dönemi tarihlerini toplu güncelle; geçmiş dönemli programı ya güncelle ya listeden düşür. Denetimdeki en yüksek ticari etkili madde.

### 🟠 Yüksek — 338 program sayfasında hiç açıklama metni yok

984 program kaydının 646’sında post_content dolu, 338’inde tamamen boş; bu sayfalar yalnızca alan bloğundan ibaret.

**Düzeltme:** Alan verisinden en az bir paragraflık açıklama üret; üretilmiş dolgu değil, veriyi cümleye çeviren şablon.

### 🟠 Yüksek — Bilgi amaçlı içerik katmanı hiç yok

Sitede 0 blog yazısı. Öğrenci vizesi, YÖK denkliği, apostil, ikamet kartı gibi dönüşüm öncesi sorgular tamamen karşılıksız. Macaristan öğrenci vizesi için ayrı bir sayfa dahi yok.

**Düzeltme:** Vize/denklik/apostil ekseninde rehber katmanı başlat; para sayfalarına iç bağlantı kaynağı olur.

### 🟠 Yüksek — E-E-A-T: kurum var, kişi yok

Danışman adı, unvanı, özgeçmişi hiçbir yerde yok. Yazar kimliği yok. /student-perspectives/ 481 kelime ama tek bir isimli öğrenci yorumu içermiyor. Sertifika/üyelik rozeti yok.

**Düzeltme:** Danışman ekibini isim ve deneyimle yayınla; öğrenci yorumlarını isimlendir ve tarihlendir.

### 🟡 Orta — Tarih/tazelik sinyali yok

Hiçbir sayfada 'son güncelleme' görünmüyor; yapısal veri olmadığı için dateModified de yok.

**Düzeltme:** Rakam yayınlayan her sayfaya görünür güncelleme tarihi ve Article.dateModified ekle.


## On-Page SEO — 25/100

**Çalışan yanlar**

- Canonical etiketleri kusursuz
- html lang iki dilde de doğru (en-US / tr-TR)
- viewport meta doğru
- Yanlış noindex yok


### 🔴 Kritik — İngilizce ana sayfanın başlığı tamamen Türkçe

huneducation.com/ → lang=en-US, H1 İngilizce, ama <title> 154 karakterlik Türkçe bir cümle: 'HunEducation – Macaristan üniversiteleri, Macaristan yüksek lisans…'.

**Düzeltme:** 60 karakter altında, İngilizce, hedef sorguya göre yeniden yaz.

### 🔴 Kritik — 494/500 sayfada meta description yok

Yalnızca 5 üniversite + 1 program sayfasında açıklama var.

**Düzeltme:** Yoast'ı etkinleştir; CPT bazlı açıklama şablonu tanımla, 14+14 editoryal sayfaya elle yaz.

### 🟠 Yüksek — Open Graph etiketi hiç yok

500/500 sayfada og: etiketi yok. WhatsApp ve Instagram bu işin ana paylaşım kanalları.

**Düzeltme:** Yoast'ın OG çıktısını aç; her sayfaya og:title, og:description, og:image.

### 🟠 Yüksek — hreflang hiç yok — EN/TR birbirini yiyor

İki dil iki ayrı alan adında ve aralarında dil bağı bildirilmemiş. SXO analizinde aynı sorgu için hem EN hem TR admission URL’sinin yarıştığı gözlendi.

**Düzeltme:** WPML SEO eklentisini etkinleştir; on-sayfa hreflang + x-default.

### 🟠 Yüksek — Editoryal sayfa başlıkları tek kelimelik

'Courses – HunEducation', 'Admission – HunEducation', 'Costs – HunEducation'. Ortalama başlık 42 karakter; 92 sayfa 30 karakterin altında; 17 tekrar eden başlık.

**Düzeltme:** Her para sayfasına anahtar kelime + yıl içeren, 60 karakter altında özgün başlık.

### 🟡 Orta — 25 sayfalama URL’si aynı başlık ve aynı H1

/courses/1..25 — hepsi 'Courses'. rel=next/prev yok, self-canonical var.

**Düzeltme:** Başlığa ve H1’e sayfa numarası ekle.

### 🟡 Orta — /contact/ sayfasında 4 adet H1

Tek H1 kuralı ihlali.

**Düzeltme:** Bir H1 bırak, diğerlerini H2’ye indir.


## Schema / Structured Data — 6/100

**Çalışan yanlar**

- Uygulama için zemin temiz: NAP tutarlı, JetEngine alan verisi zengin, WPML çalışıyor


### 🔴 Kritik — Site genelinde sıfır yapısal veri

500 sayfada tek bir JSON-LD bloğu yok; '@type' hiç geçmiyor. İki Yoast ve 'Schema & Structured Data' eklentisi kurulu ama pasif.

**Düzeltme:** Organization+WebSite @id grafiği site geneli; Course şablonu (Elementor ID 925) JetEngine alanlarıyla; CollegeOrUniversity 40 üniversite sayfasına; ItemList katalog hub’larına.

### 🟠 Yüksek — Course.provider üniversiteye bağlanmalı

Program sağlayıcısı Hun Education değil, ilgili üniversitedir.

**Düzeltme:** Course.provider → /university/ sayfasının CollegeOrUniversity düğümüne @id ile bağla.

### 🟡 Orta — course-year terim slug’ı bozuk

Gövde sınıfı 'course-year-243' — yıl taksonomisinin slug’ı yıl değil terim ID’si.

**Düzeltme:** startDate türetmeden önce terim slug’larını düzelt.

### 🔵 Bilgi — AggregateRating EKLENMEMELİ

Sitede hiçbir gerçek yorum/puan içeriği yok; puan şeması eklemek sahte değerlendirme politikası ihlali olur.

**Düzeltme:** Önce gerçek, doğrulanabilir öğrenci yorumu topla; şema ondan sonra.


## Performance (CWV) — 60/100

**Çalışan yanlar**

- CLS 0.056 — iyi
- TBT 39 ms — iyi (INP vekili)
- Yatay taşma yok


### 🟠 Yüksek — LCP 12,7 sn (lab, simüle)

FCP 5,3 sn, TTI 16,6 sn, 2.074 KiB / 125 istek, tamamı HTTP/1.1. 51 render-engelleyici kaynak, ~3.800 ms tasarruf potansiyeli; en kötü tek engelleyici Social Chat CSS’i (1.034 ms).

**Düzeltme:** Önbelleği aç (önce PHPSESSID sorununu çöz), Social Chat CSS/JS’ini ertele, per-post Elementor CSS’lerini birleştir.

### 🟠 Yüksek — Üçüncü taraf yükü ~802 KB (sayfanın %39’u)

3 ayrı Google etiketi (2 GA4 + 1 ölü eski UA), Facebook Pixel 172 KB, 3 aile Google Fonts 119 KB, JetMenu’nun Vue 2 çalışma zamanı 33,7 KB, Font Awesome 74,7 KB — hepsi site geneli.

**Düzeltme:** Ölü UA etiketini kaldır, MonsterInsights/PixelYourSite çift takibini tekilleştir, fontları yerel barındır, JetMenu’yu gerekmediği şablonlarda kapat.

### 🔵 Bilgi — Ölçüm kapsamı sınırlı

Yalnızca ana sayfa ölçüldü; /courses/ (653 KB HTML), /course/pharmacy/ ve TR ana sayfası ölçülmedi. CrUX/GSC saha verisi yok — bu skor yalnızca lab verisidir.

**Düzeltme:** GSC/CrUX bağlandıktan sonra saha verisiyle yeniden ölç.


## AI Search Readiness (GEO) — 33/100

**Çalışan yanlar**

- robots.txt her iki alan adında da tüm AI tarayıcılarına açık (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot dahil) — darboğaz burası değil
- /costs/ sayfası somut ücret rakamları taşıyor — alıntı yemi olarak güçlü ham madde


### 🔴 Kritik — Makine okunur olgu katmanı yok

Sıfır JSON-LD, sıfır OG, 494/500 açıklama yok, hiçbir sayfada tarih sinyali yok. Üretken motorların çıkarabileceği yapılandırılmış olgu yok.

**Düzeltme:** Önce şema, sonra tarihli ve kaynaklı olgu blokları.

### 🟠 Yüksek — Elementor markup’ı çıkarımı bozuyor

Program sayfaları ~330 kelime taşıyor ama boilerplate ayıklayan çıkarım yalnızca ~75–90 kelime kurtarabiliyor — AI ingest için vekil ölçüm.

**Düzeltme:** Semantik markup (article/section, tablo) kullan; olguları tabloya al.

### 🟠 Yüksek — Varlık çözünürlüğü zayıf

'Hun Education' için Wikipedia/Wikidata yok, doğrulanmış üçüncü taraf atıfı yok; sosyal profiller sameAs olarak bildirilmiyor.

**Düzeltme:** Organization şeması + sameAs; üniversitelerin resmî temsilci listelerinde yer al.

### 🟡 Orta — llms.txt yok

İki alan adında da yok.

**Düzeltme:** Hazırlanan taslağı her iki host’a koy ve robots.txt’te bildir.

### 🟡 Orta — Kaynak göstermeme

Ana sayfadan çıkan 8 dış alan adının yalnızca biri gerçek otorite kaynağı. Ücret ve tarih yayınlayan bir sitede kaynak yok.

**Düzeltme:** Her rakamı üniversitenin kendi sayfasına bağlayarak kaynaklandır.


## Images — 25/100

**Çalışan yanlar**

- Görseller ilgili ve gerçek; kurgusal stok izlenimi vermiyor
- Yatay taşmaya yol açmıyorlar


### 🟠 Yüksek — 2.614 görselin 1.851’inde alt metni yok (%71)

500 sayfanın 450’sinde 4 veya daha fazla alt metinsiz görsel var. Çoğu Elementor şablonundan geliyor.

**Düzeltme:** Şablon seviyesinde düzelt — tek seferde binlerce görseli kapsar.

### 🟡 Orta — Görsel optimizasyonu kapalı

Smush Pro kurulu ama pasif; WebP/AVIF yok, boyutlandırma hataları ~240 KB tasarruf bırakıyor.

**Düzeltme:** Smush’ı etkinleştir, toplu dönüşüm çalıştır.


---

## Kapsam ve güven sınırları

Bu denetimin neyi ölçemediği, ölçtüğü kadar önemlidir:

- Google API kimlik bilgisi yok: GSC indeksleme durumu, CrUX saha verisi ve GA4 organik trafik ölçülmedi.
- Moz/Bing anahtarı yok: backlink profili ve DA/PA ölçülemedi.
- Performans yalnızca ana sayfada, lab verisiyle ölçüldü.
- SERP analizi doğrulanmış bir google.com.tr oturumu değil; sıralama iddiaları niteliksel.
- Tarama 500 sayfayla sınırlandı (~1.052 URL’nin %48’i); örnek ağırlıklı olarak /course/ sayfaları.
- İçerik, görsel ve backlink ajanları oturum yeniden başlarken kesildi; bu üç dosya orkestratör tarafından ajanların doğrulanmış verileriyle yazıldı.

---

## Üretilen dosyalar

- `FULL-AUDIT-REPORT.md` — bu rapor
- `ACTION-PLAN.md` — önceliklendirilmiş eylem planı
- `audit-data.json` — yapılandırılmış denetim verisi
- `findings/` — 11 uzman bulgu dosyası (teknik, içerik, şema, sitemap, performans, GEO, SXO, görsel, on-page, altyapı sağlığı, backlink)
- `screenshots/` — 20 ekran görüntüsü (5 sayfa × masaüstü/mobil)
- `crawl.json` — 500 sayfalık ham tarama verisi
