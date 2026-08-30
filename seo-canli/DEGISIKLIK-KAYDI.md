# huneducation.com — canlı değişiklik kaydı

Tarih: 2026-08-30 · Tümü canlı sitede uygulandı · Her adım anında doğrulandı

## Geri alma noktaları

| Ne | Nerede |
|---|---|
| Değişiklik öncesi option yedeği | `wp-content/uploads/_seo-geri-alma.json` (sunucuda) |
| Sinyal anlık görüntüleri | `00-oncesi.json` → `03-son.json` (41 URL) |
| Eklenen tek kod dosyası | `wp-content/mu-plugins/hun-seo-duzeltmeleri.php` — silmek geri almak için yeterli |

## Yapılanlar (sırayla)

1. **Yoast ayrıcı karakteri `sc-pipe` → `sc-ndash`** — açılıştan ÖNCE.
   Bu tek ayar, Yoast devreye girdiğinde 1.052 sayfanın başlığının değişmesini
   engelledi. Mevcut başlıklar en-dash kullanıyordu.
2. **25 adet genel `metadesc` şablonu boşaltıldı** — hepsi aynı Türkçe cümleydi;
   açılsaydı 500 İngilizce sayfaya aynı Türkçe açıklama basılacaktı.
3. **Auctollo "XML Sitemap Generator" kapatıldı** — bozuktu ve WordPress'in kendi
   sitemap'ini de gölgeliyordu.
4. **Yoast SEO 27.6 açıldı** (Premium 20.9 **açılmadı** — ana sürüm uyumsuz).
5. **Altı sayfadaki eski/yanlış Yoast başlığı düzeltildi**
   (`/hakkimizda/` "Macaristan'da Eğitim" diyordu; TR ana sayfada boşluk eksikti;
   dört sayfada marka "Hun Education" / "HunEducation" olarak tutarsızdı).
6. **mu-plugin: sayfalama düzeltmesi** — `/courses/N/` ve `/kurslar/N/` kendine
   canonical veriyor ve başlıkta sayfa numarası taşıyor. Yoast bunları tek sayfa
   sanıp hepsini `/courses/`'a canonical veriyordu; 24 sayfadaki ~550 program
   bağlantısı değersizleşecekti.
7. **WPML SEO açıldı + `head_langs` 0 → 1** — hreflang çıktısı WPML ayarından
   kapalıymış. Artık karşılıklı `en`/`tr`/`x-default` etiketleri var.
8. **Marka adı düzeltildi** — `company_name` ve `website_name`
   "Huneducation.com | Macaristan Üniversiteleri - Macaristan Yüksek Lisans"
   idi; "Hun Education" yapıldı. Sosyal profiller `sameAs`'e eklendi.
9. **mu-plugin: Organization şeması zenginleştirildi** — legalName, adres,
   telefon, e-posta, kuruluş yılı, `areaServed`, `knowsLanguage`, `knowsAbout`
   (7 madde), dile göre açıklama.
10. **Yoast llms.txt açıldı, sonra KAPATILDI** — WPML'i tanımıyor; İngilizce
    dosyada Türkçe sayfaları İngilizce alan adıyla listeliyordu. Yanlış makine
    dosyası hiç olmamasından kötü. Doğrusu elle yazılacak.

## Ölçülen sonuç (41 URL örneklemi)

| Sinyal | Önce | Sonra |
|---|---|---|
| Meta description | 2 | **29** |
| og:title | 0 | **37** |
| JSON-LD şema | 0 | **37** |
| hreflang | 0 | **37** |
| Sitemap URL (EN host) | 2 | **~1.008** |
| Sitemap URL (TR host) | 2 | **~996** |
| Hata dönen URL | 0 | **0** |

## Bilerek değiştirilen başlıklar (gerileme değil, düzeltme)

- **EN ana sayfa**: Türkçe başlık → "Study at Universities in Hungary – HunEducation"
- **TR ana sayfa**: marka + 154 karakterlik jenerik cümle → "Macaristan Üniversite Eğitimi – HunEducation"
- `/hakkimizda/`: yanlış başlık → sayfa adı

## Kozmetik farklar (işlem yapılmadı)

Yoast, tema gibi `wptexturize` uygulamıyor: kıvrık kesme işareti düz oluyor
("Hungary's" → "Hungary's"), program başlıklarındaki tire en-dash'e çevrilmiyor.
Sıralamaya etkisi yok; düzeltmek her sayfada ek filtre çalıştırmayı gerektirir.

## Sırada bekleyenler

- Güvenlik başlıkları (HSTS, nosniff, Referrer-Policy, X-Frame-Options)
- PHPSESSID/`no-store` kök sebebi → sonra önbellek
- Program (`Course`) şeması — 984 sayfa, Elementor şablonu 925
- Görsel alt metni — 1.851 görsel, şablon seviyesinde
- 4 sayfada eksik meta description
- Elle yazılmış llms.txt (her host için ayrı)
- **Veri gerektiren:** 965 programın geçmiş başvuru tarihi; danışman ekibi bilgileri

---

# İkinci tur — 2026-08-30 (devam)

## 11. Güvenlik başlıkları
`mu-plugins/hun-seo-duzeltmeleri.php` içinden, `.htaccess`'e dokunmadan.
CSP **bilerek eklenmedi**: Elementor ve Jet eklentileri satır içi script/stil
kullanıyor, dar bir CSP sayfayı bozardı.

| Başlık | Değer |
|---|---|
| Strict-Transport-Security | max-age=31536000 |
| X-Content-Type-Options | nosniff |
| Referrer-Policy | strict-origin-when-cross-origin |
| X-Frame-Options | SAMEORIGIN |
| Permissions-Policy | geolocation/camera/microphone/payment kapalı |

İki alan adında da doğrulandı.

## 12. Course şeması — 984 program sayfası
Yeni dosya: `mu-plugins/hun-seo-course-schema.php`

Yoast'ın kendi grafiğine bağlanıyor (ayrı ada değil), `WebPage.mainEntity` ile
ilişkilendiriliyor. Alanlar: `name`, `description`, `provider`,
`educationalLevel`, `about`, `timeRequired`, `offers`, `locationCreated`.

**Kritik ayrıntı:** `course_institute` alanı her zaman **Türkçe** üniversite
kaydını tutuyor. Naif kullanılsa İngilizce program sayfası Türkçe üniversiteye,
üstelik yanlış alan adına bağlanacaktı. WPML ile o anki dile çözümleniyor.

**Bilerek eklenmeyenler:**
- `hasCourseInstance` — Google'ın Course zengin sonucu bunu istiyor ama geçerli
  olması için dönem tarihi veya haftalık ders yükü gerekiyor. 965 başvuru
  tarihinin tamamı geçmiş, haftalık yük verisi yok. Uydurma veri basmaktansa
  alan atlandı; 2026-27 tarihleri girildiğinde tek seferde eklenecek.
- `applicationDeadline` — aynı sebep. Geçmiş tarihi yapısal veri olarak
  yayınlamak, Google'a doğrulanabilir şekilde yanlış bilgi bildirmektir.

**338 açıklamasız program:** açıklama alan verisinden üretiliyor (seviye,
üniversite, şehir, dönem, ücret). Uydurma metin değil, mevcut olguların cümleye
çevrilmesi. Örnek çıktı doğrulandı.

## 13. CollegeOrUniversity şeması — 40 üniversite sayfası
Aynı dosyada. Course.provider bu düğümlere işaret ediyor; varlık zinciri artık
iki uçtan kapalı.

## 14. Dört eksik meta description yazıldı
`/admission/` (150), `/student-perspectives/` (137),
`/studying-medicine…/` (155), `/…ogrenci-gorusleri/` (115 karakter).

## Kapsam doğrulaması

16 URL örneklendi (6 EN program, 5 TR program, 3 EN üniversite, 2 TR üniversite).
Hepsinde beklenen şema düğümü, hreflang ve canonical mevcut. **Sorun: yok.**

Bir program sayfasında hreflang=1 çıktı — o programın karşı dilde çevirisi yok
(498 EN / 486 TR); beklenen davranış.

## Yanlış alarm düzeltmesi

Denetim raporunda "`course-year` terim slug'ı bozuk (`course-year-243`)" yazıyordu.
Doğrulandı: slug **doğru** (`2025`); `course-year-243` Elementor'ün gövde sınıfına
yazdığı terim ID'si. Şema tarafında sorun yok.

---

# Üçüncü tur — 2026-08-30

## 15. Görsel alt metni — bulgu düzeltmesi

Denetim raporundaki **"1.851 görselde alt metni yok (%71)"** bulgusu **yanlıştı**;
kendi tarayıcımın ölçüm hatasıydı. İki hata birleşmişti: (a) içerik bölgesi
bulunamayınca tüm HTML sayılıyordu, (b) dekoratif görsellerdeki `alt=""` —
ki bu **doğru** uygulamadır — "eksik" sayılıyordu.

Doğru ölçüm (11 sayfa, dekoratifler ayıklanmış):

| | |
|---|---|
| İçerik görseli, alt metni dolu | **75** |
| Dekoratif (bayrak, izleme pikseli) | 33 |
| Gerçekten eksik | **1** |

Medya kütüphanesi de iyi durumda: 1.067 görselin 827'sinde alt var; eksik olan
240'ın çoğu Elementor'ün ön yüzde hiç görünmeyen şablon ekran görüntüleri.

**Yapılan:** Bağlamı kesin olan 6 görsel (üniversite logoları) doğru alt metnine
kavuşturuldu. Kalan ~197 görsel galeri/içerik görseli; görmeden tarif etmek
uydurma olurdu — insan gözü gerektiriyor, listesi çıkarıldı.

## 16. llms.txt — elle, her host için ayrı

Yeni dosya: `mu-plugins/hun-seo-llms.php`

Yoast'ın yerleşik llms.txt'i **fiziksel dosya** yazıyordu (`public_html/llms.txt`).
İki alan adı aynı kök dizini paylaştığı için dosya dile göre ayrışamıyordu:
İngilizce dosyada Türkçe sayfalar İngilizce alan adıyla listeleniyordu. Dosya
silindi, PHP tabanlı çözüm kondu.

Artık her host doğru dilde çıktı veriyor, sayfa listesi yayındaki sayfalardan
otomatik üretiliyor (sayfa eklendikçe kendiliğinden güncel), program/üniversite
sayısı canlı sayılıyor, tam liste için sitemap'e yönlendiriyor. Günlük önbellek,
sayfa kaydedilince düşüyor.

## 17. robots.txt

llms.txt işareti eklendi. `Disallow: /wp-admin/` eklemeye çalışıldı ama Yoast 27
robots çıktısını kendi ayrıştırıcısıyla birleştirip aynı `User-agent` bloğunu
tekilleştirdiği için satır düşüyordu. wp-admin zaten kimlik doğrulama arkasında
ve noindex; sıralamaya etkisi yok. **Çalışmayan kod bırakılmadı**, kaldırıldı.

## Üçüncü tur doğrulaması (41 URL)

| Sinyal | Önce | Sonra |
|---|---|---|
| Meta description | 2 | **33** |
| og:title | 0 | **37** |
| JSON-LD | 0 | **37** |
| hreflang | 0 | **37** |
| canonical | 37 | 37 |
| Hatalı URL | 0 | **0** |

## Sunucudaki dosyalar (geri alma)

| Dosya | Ne yapar |
|---|---|
| `mu-plugins/hun-seo-duzeltmeleri.php` | sayfalama canonical/başlık, güvenlik başlıkları, Organization şeması, robots satırı |
| `mu-plugins/hun-seo-course-schema.php` | Course + CollegeOrUniversity şeması |
| `mu-plugins/hun-seo-llms.php` | iki dilli llms.txt |
| `uploads/_seo-geri-alma.json` | değişiklik öncesi option yedeği |

Üç mu-plugin dosyasını silmek, eklenen tüm kod davranışını geri alır.

---

# Dördüncü tur — SEO/GEO derinleştirme

## 18. İngilizce para sayfalarının başlıkları

Üç sayfanın başlığında **hiçbir anahtar kelime yoktu** — "Hungary" kelimesi bile.
Bu üçü özel bir durum: kaybedilecek anahtar kelime olmadığı için eklemek tek
yönlü kazanç.

| Sayfa | Önce | Sonra |
|---|---|---|
| `/costs/` | Costs | Tuition Fees and Living Costs in Hungary |
| `/admission/` | Admission | Hungary University Admission Requirements |
| `/courses/` | Courses | English-Taught Degree Programmes in Hungary |

Anahtar kelime taşıyan diğer sayfalara **dokunulmadı** ("Why Hungary",
"Education in Hungary", "Hungary's Universities", tıp/pilotaj/yüksek lisans).

## 19. Uzun başlıklarda kuyruk kesme

**Kural: başlığın ilk ~30 karakteri aynen korundu** — sıralama sinyali orada.
Yalnızca tekrar eden ve dolgu olan kuyruk kesildi.

| Sayfa | Kesilen | Sonuç |
|---|---|---|
| Studying Medicine… | "and Pursuing a Medical Degree in Hungary" (Hungary iki kez) | 84 → 58 |
| University Education and Life… | ": What You Need to Know" | 78 → 55 |
| Student Perspectives… | ": Life and Educational Experiences at…" | 95 → 56 |
| Macaristan'da Tıp Eğitimi… | ikinci "Macaristan'da" | 68 → 54 |
| Macaristan'da Yaşam… | ": Bilinmesi Gerekenler" | 78 → 56 |

Sonuç: 60 karakteri aşan başlık **6 → 1** (kalan tek başlık sayfalama URL'si,
SERP hedefi değil). Ortalama başlık uzunluğu 43 karakter.

## 20. WebSite şema düğümü

`alternateName` "Huneducation.com | Macaristan'da Üniversite Okumak" idi —
marka alanı anahtar kelime deposu değil. `description` ise site sloganından
geliyordu ve İngilizce sitede bile Türkçeydi. İkisi de dile göre düzeltildi.

## 21. sameAs — dört profil, dile göre

Yoast ayarlarından **YouTube hiç çıkmıyordu** ve iki alan adı da Türkçe
Instagram'ı gösteriyordu. Dört profilin de yaşadığı doğrulandı (HTTP 200);
Organization filtresinde dile göre sabitlendi:

- Facebook (ortak), X (ortak), YouTube (ortak)
- Instagram: EN → `huneducation`, TR → `huneducation_tr`

## 22. Doğrulanan, işlem gerekmeyenler

- **Görsel sitemap** çalışıyor: 14 sayfa URL'sinde 32 `<image:image>` girdisi
- **İç bağlantı canlıda sorunsuz**: tıp/pilotaj/yüksek lisans sayfalarının her
  biri 23-24 bağlantı alıyor. "0 iç bağlantı" bulgusu yerel tasarıma aitti.

## Dördüncü tur doğrulaması (41 URL)

Meta description 2 → **33** · og:title 0 → **37** · JSON-LD 0 → **37** ·
hreflang 0 → **37** · canonical 37 → 37 · **hatalı URL: 0**

## İnsan eli gereken (5 dakikalık, sıfır riskli)

Elementor'de üç H1 hâlâ jenerik: "Costs", "Admission", "Courses". Başlıklar
düzeldi ama H1'ler sayfa içeriğinde gömülü. Canlı sayfada JSON ameliyatı
yapmaktansa Elementor editöründen elle düzeltilmesi daha güvenli.

Öneri: "Tuition Fees and Living Costs in Hungary" /
"University Admission Requirements" / "English-Taught Degree Programmes".

---

## Tur 6 — H1 duzeltmeleri (30 Agustos 2026)

### Sorun
Uc ic sayfanin H1'i tek kelimeydi: "Costs", "Admission", "Courses". Ingilizce
ana sayfanin H1'i ise "Search Your Favorite Course Here" — bir arayuz talimati,
hicbir sorgu hedeflemiyor. Sitenin en degerli H1'i bosa gidiyordu.

### Neden post_title degistirilmedi
H1 sayfa iceriginde degil: Elementor tema sablonu **1630** ("Page Template",
kosul `include/singular/page`) icindeki `theme-post-title` widget'i `post_title`i
basiyor. `post_title`i degistirmek menuleri, kirinti yolunu ve tum ic baglanti
capa metinlerini de degistirirdi — H1 kazancinin haklı cikarmayacagi bir yayilma
ve siralama riski. Bu yuzden yalnizca **widget ciktisi** hedeflendi.

### Yontem
`hun-seo-duzeltmeleri.php` icine iki `elementor/widget/render_content` filtresi:
1. `theme-post-title` widget'i + sayfa kimligi haritasi (422, 322, 199, 2321)
2. `heading` widget'i + widget kimligi `bdf27b5` + `is_front_page()` + dil kontrolu

Hicbir veritabani icerigi degistirilmedi. Elementor `_elementor_css`,
`_elementor_element_cache`, `_elementor_page_assets` meta'lari dusuruldu.

### Degisenler
| URL | Onceki H1 | Yeni H1 |
|---|---|---|
| /costs/ | Costs | Tuition Fees and Living Costs in Hungary |
| /admission/ | Admission | University Admission Requirements in Hungary |
| /courses/ | Courses | English-Taught Degree Programmes in Hungary |
| / (EN) | Search Your Favorite Course Here | Find Your Programme at a Hungarian University |
| /kurslar/ (TR) | Bolumler | Macaristan'da Universite Bolumleri |

**Dokunulmayanlar:** TR ana sayfa H1'inde "Macaristan" ve "Universite" zaten
vardi — sitenin en degerli TR sayfasinda gereksiz risk alinmadi.

### Dogrulama
- Hedef sayfalarda yeni H1, hepsinde `<h1>` sayisi = 1
- /about-us/ H1 hala "About Us" (yan etki yok)
- Ana sayfa menusunde `>Costs<`, `>Admission<`, `>Courses<` capa metinleri yerinde

### Geri alma
`hun_seo_h1_haritasi` fonksiyonundan sonraki iki filtre blogu silinir; ya da
tum dosya silinir.
