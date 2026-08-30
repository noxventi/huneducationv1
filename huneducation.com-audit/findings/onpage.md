# On-Page SEO — bulgular

Kaynak: 500 sayfalık canlı tarama (`crawl.json`, 2026-08-30) + doğrudan doğrulama.
Kapsam: huneducation.com (EN) ve tr.huneducation.com (TR).

## Kritik

### 1. Meta description 500 sayfanın 494'ünde yok
Yalnızca 6 sayfada açıklama var (5 üniversite + 1 program sayfası). Ana sayfa dâhil
hiçbir editoryal sayfada yok. Google snippet'i gövdeden uydurmak zorunda kalıyor;
tıklama oranı üzerinde doğrudan etki.

**Kanıt:** `/university/university-of-pecs/` var; `/`, `/courses/`, `/admission/`,
`/costs/` ve 494 sayfa daha yok.

**Kök sebep:** Yoast SEO kurulu ama **pasif**. Şablon seviyesinde açıklama üretimi
kapalı.

**Düzeltme:** Yoast'ı etkinleştir, CPT bazlı açıklama şablonu tanımla
(`course`: `%%title%% – %%ct_course-city%% · yıllık %%cf_course_price%% %%cf_course_price_currency%%`),
14+14 editoryal sayfaya elle yaz.

### 2. Open Graph etiketi hiç yok (500/500)
WhatsApp ve Instagram bu işin ana paylaşım kanalları; paylaşılan her bağlantı
başlıksız/görselsiz görünüyor. Sosyal tıklama doğrudan kaybediliyor.

### 3. hreflang hiç yok (500/500)
İki dil iki ayrı alan adında (WPML domain-per-language) ve aralarında hiçbir
dil bağı bildirilmemiş. WPML SEO eklentisi kurulu ama **pasif**.

## Yüksek

### 4. 25 sayfalama URL'si aynı başlık ve aynı H1 ile
`/courses/`, `/courses/2/` … `/courses/25/` — hepsinin `<title>` değeri
"Courses – HunEducation", hepsinin H1'i "Courses". `rel=next/prev` yok
(deprecated ama yine de sinyal), self-canonical var (doğru).

**Düzeltme:** başlığa sayfa numarası (`Courses – Page 3`), H1'e de aynı şekilde;
ya da sayfalamayı filtreli katalog sayfasına çevir.

### 5. 92 sayfada başlık 30 karakterin altında
Program sayfalarının başlığı yalnızca `<program adı> – HunEducation`. Ne şehir,
ne üniversite, ne ücret, ne seviye. Uzun kuyruk sorgularının hiçbirini
hedeflemiyor.

**Ortalama başlık uzunluğu 42 karakter** — SERP'te ~60 karaktere kadar yer var,
yani sayfa başına ~18 karakterlik hedefleme alanı kullanılmıyor.

### 6. 17 tekrar eden başlık
Aynı `<title>` birden çok URL'de. Örnekler: "Hungary s Universities HunEducation" (2),
"Electrical Engineering BME HunEducation" (2) — aynı programın iki kaydı.

## Orta

### 7. `/contact/` sayfasında 4 adet H1
Tek H1 kuralı ihlali; sayfanın ana konusu belirsizleşiyor.

### 8. Başlıklarda apostrof kaybı
"Hungary s Universities", "Macaristan da üniversite okumak" — apostrof HTML'e
düz metin olarak yazılmış ve kaybolmuş. Marka algısı ve tam eşleşme sorgular
için zarar verici.

## Bilgi

- Canonical: 500/500 sayfada var ve **hiçbiri** yanlış hedefe işaret etmiyor. Bu iyi.
- `noindex` yanlışlıkla konmuş sayfa yok.
- TR ana sayfası (`/macaristanda-universite/`) doğru şekilde köke canonical veriyor.
- robots.txt her iki alan adında da tarama engellemiyor.

## Görsel (Images)

| Ölçüm | Değer |
|---|---|
| Taranan sayfalardaki toplam görsel | 2.614 |
| **Alt metni olmayan** | **1.851 (%71)** |
| Sayfa başına ortalama görsel | 5,2 |
| 4+ alt metinsiz görseli olan sayfa | 450 / 500 |

Alt metin eksikliği hem erişilebilirlik hem görsel arama kaybı. Çoğu Elementor
şablonundan geliyor — şablon seviyesinde düzeltilirse tek seferde çözülür.

## Not: yanlış pozitif
Taramada `https://huneducation.com/itemDataObject.url` 404 verdi. Bu **site hatası
değil**: JetMenu'nün Vue şablonu `<script type="text/x-template">` içinde
`:href="itemDataObject.url"` taşıyor ve benim tarayıcım script içinden href
çıkardı. Gerçek tarayıcılar script içeriğini bağlantı saymaz. Yine de bu şablonun
her sayfada ham olarak gönderildiğini gösteriyor — performans tarafında ayrıca
değerlendirilmeli.
