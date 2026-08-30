# huneducation.com — SEO Denetimi (2. tur)

**Tarih:** 2026-08-30 · **Örneklenen sayfa:** 94 · **Site boyutu:** ~1114 URL

**İş modeli:** Education consultancy / programme catalogue (agency + publisher hybrid)


---

## Yönetici özeti

# SAĞLIK SKORU: 69 / 100

> Sabah ölçülen skor **31** idi. Aradaki fark, o denetimden sonra kapatılan altyapı eksiklerinden geliyor: Yoast, WPML SEO ve String Translation açıldı, 58 katalog merkez sayfası indekse girdi, H1 ve önbellek başlıkları düzeltildi.


> **Ama skor sıralama demek değil.** Bu denetimin en önemli bulgusu skorda görünmüyor: otorite.


### Otorite karşılaştırması

| Alan adı | PageRank sırası | Harmonik merkezilik |
|---|---|---|
| **huneducation.com** | **19.666.393** | **13.997.358** |
| studyinhungary.hu | 399.605 | 518.353 |
| unipage.net | 517.537 | 518.302 |
| studyineurope.eu | 1.361.137 | 529.098 |

Kaynak: Common Crawl web graph, cc-main-2026-jan-feb-mar


### Kategori skorları

| Kategori | Skor | Ağırlık |
|---|---|---|
| Technical SEO | **81**/100 | 22% |
| Content Quality | **52**/100 | 23% |
| On-Page SEO | **68**/100 | 20% |
| Schema / Structured Data | **88**/100 | 10% |
| Performance (CWV) | **55**/100 | 10% |
| AI Search Readiness (GEO) | **82**/100 | 10% |
| Images | **70**/100 | 5% |

### En kritik beş bulgu

1. Otorite tavani: PageRank sirasi 19.666.393 - studyinhungary.hu 399.605. Bas terimlerde kisa vadede yarisilamaz.
2. 965 basvuru tarihinin tamami gecmis; en yenisi 2026-06-30, bugunden iki ay once.
3. 984 programin 338'inde hic icerik yok (50 karakterden kisa).
4. Turkce program sayfalarinin hicbirinde meta aciklama yok (olculen 18/18 bos).
5. 44 render engelleyici stil dosyasi ve sayfa onbellegi yok; TTFB 0,74-1,23 s.

### En hızlı beş kazanç

1. ~1.100 program ve universite sayfasina alan verisinden meta aciklama uret.
2. IndexNow kur; 58 yeni merkez sayfasi ve 506 degisen TR adresini gonder.
3. hreflang'i eksik iki TR program sayfasini tamamla.
4. Gorselleri WebP'ye cevir; dort gorsele width/height ekle.
5. http://www zincirini iki atlamadan bire indir.

---


## Technical SEO — 81/100

**Çalışan yanlar**

- Indekslenebilirlik neredeyse kusursuz: 13 sayfa tipinin hepsinde index/follow, kendine canonical, tam 1 H1, 3 hreflang
- Parametreli URL'ler temiz adrese canonical'laniyor; kopya icerik riski yok
- SSR: H1, JSON-LD ve canonical ham HTML'de; JS render riski yok
- 22/22 ic baglanti saglam; 404 gercekten 404 donuyor
- Sitemap robots.txt'de bildirilmis: 563 EN + 551 TR URL


### 🟠 Yüksek — Sayfa onbellegi yok, TTFB 0,74-1,23 s

Dort olcumun ucu Google'in 800 ms esiginin ustunde. Aktif onbellek eklentisi yok; her istek tam PHP calistiriyor. PixelYourSite her istekte session_start cagirdigi icin korlemesine onbellek acmak oturum sizintisi riski tasir.

**Düzeltme:** Once oturumun gercekten gerekli olup olmadigini incele; ardindan oturum tasiyan istekleri muaf tutan bir onbellek kur.

### 🟠 Yüksek — 44 render engelleyici stil dosyasi

head icinde 44 stylesheet, sayfa genelinde 49. Ayrica 51 script ve 593 KB JS. preload 0, fetchpriority 0.

**Düzeltme:** Elementor Improved CSS Loading ayarini ac; LCP gorseline preload ve fetchpriority=high ver.

### 🟡 Orta — IndexNow yapilandirilmamis

/indexnow.txt 404 donuyor. Bing, Yandex ve Naver aninda indekslemeyi destekliyor.

**Düzeltme:** Anahtar dosyasini kur; 58 yeni merkez sayfasi ve 506 degisen TR adresini gonder.

### ⚪ Düşük — http://www iki atlamali yonlendirme

http://www once https://www adresine, sonra https:// adresine gidiyor. Diger uc varyant tek atlama.

**Düzeltme:** Sunucu duzeyinde tek adima indir.


## Content Quality — 52/100

**Çalışan yanlar**

- Bilgi sayfalari guclu: EN ortalama 1.298, TR ortalama 1.316 kelime
- Universite sayfalari 927-1.060 kelime
- 1999'dan beri tek ulkeye odaklanma net bir uzmanlik sinyali


### 🔴 Kritik — 338 programda hic icerik yok

984 programin 338'inde post_content 50 karakterden kisa. Olculen program sayfalari 296-331 kelime; bu neredeyse tamamen sablon metni. Bu sayfalar kendi basliklari disinda hicbir sorgu icin yarisamaz.

**Düzeltme:** Program basina 120-150 kelime ozgun metin: mufredat, giris sartlari, mezuniyet sonrasi. Once en yuksek hacimli 100 program.

### 🔴 Kritik — 965 basvuru tarihinin tamami gecmis

course_application_deadline alani 984 programin 965'inde dolu; aralik 2023-07-31 ile 2026-06-30. Bugun 2026-08-30. Katalogun tamami ziyaretciye kapanmis donem gosteriyor. Bu bir siralama sorunu degil, dogrudan gelir kaybi.

**Düzeltme:** 2026-27 tarihlerini toplu guncelle. Bu ayrica hasCourseInstance semasini acar.

### 🟡 Orta — Basvuru baslangic tarihi neredeyse hic yok

course_application_start 984 programin yalnizca 22'sinde dolu; en yenisi 2024-09-01.

**Düzeltme:** Son basvuru tarihiyle birlikte guncelle.


## On-Page SEO — 68/100

**Çalışan yanlar**

- H1'ler hedef ifadeye cevrildi; her sayfada tam 1 adet
- 60 karakter ustu baslik EN tarafinda 47'de 3
- Ic baglanti yogunlugu iyi: sayfa basina ortalama 30-45 ic baglanti


### 🟠 Yüksek — Turkce program sayfalarinda meta aciklama yok

Olculen 18 TR program sayfasinin 18'inde de meta aciklama bos. Ingilizce tarafta 18'in yalnizca 6'sinda var. Ekstrapolasyon: yaklasik 1.100 sayfa aciklamasiz.

**Düzeltme:** Arsivlerde kurulan desenin aynisiyla alan verisinden dile duyarli aciklama uret.

### ⚪ Düşük — TR basliklari uzun

TR tarafinda 47 sayfanin 8'inde title 60 karakteri asiyor.

**Düzeltme:** Uzun program adlarinda kisaltma kurali uygula.

### ⚪ Düşük — Iki TR program sayfasinda hreflang eksik

makine-muhendisligi-miscolc ve neo-latin-dilleri-ve-kulturleri sayfalarinda karsilik yok.

**Düzeltme:** Eksik cevirileri tamamla ya da hreflang'i tek dilli birak.


## Schema / Structured Data — 88/100

**Çalışan yanlar**

- Course semasi 18/18 program sayfasinda, iki dilde de
- CollegeOrUniversity 6/6 universite sayfasinda
- Organization, WebSite, BreadcrumbList, ContactPoint, PostalAddress her sayfada


### 🟡 Orta — hasCourseInstance yok

Google'in Course zengin sonucu bunu istiyor ama gecerli olmasi icin gelecek tarihli donem bilgisi gerekiyor; 965 tarihin tamami gecmis. Uydurma veri basmaktansa alan bilerek atlandi.

**Düzeltme:** 2026-27 tarihleri girilince tek seferde ekle.

### 🟡 Orta — Review / AggregateRating yok

Ogrenci gorusleri sayfasi var ama yapisal veriye bagli degil.

**Düzeltme:** Gercek ve dogrulanabilir gorusleri Review semasiyla isaretle.


## Performance (CWV) — 55/100

**Çalışan yanlar**

- Sayfa agirliklari makul: 134-676 KB, Googlebot 2 MB sinirinin cok altinda


### 🔵 Bilgi — Gercek CWV olculemedi

CrUX saha verisi API anahtari olmadigi icin alinamadi. 55 puan gercek CWV degil; TTFB, render engelleyici varlik sayisi ve JS agirligi gibi vekil gostergelerin skorudur.

**Düzeltme:** GOOGLE_API_KEY tanimla; saha verisi acilir ve bu kategori tahmin olmaktan cikar.


## AI Search Readiness (GEO) — 82/100

**Çalışan yanlar**

- llms.txt iki dilde, 200 ile ve yonlendirmesiz
- Varlik tanimi net: Organization, legalName, foundingDate, adres, sameAs
- SSR sayesinde tum icerik ham HTML'de
- Tum yapay zeka tarayicilarina izin veriliyor


### 🟡 Orta — Alintilanabilir olgusal blok az

Program sayfalari uretken motorlarin alintilayacagi yogunlukta olgu tasimiyor; ucret, sure ve sehir disinda veri yok.

**Düzeltme:** Giris sartlari ve mezuniyet ciktilarini kisa, olgusal cumlelerle ekle.


## Images — 70/100

**Çalışan yanlar**

- 15/15 gorselde alt metni var
- 12/15 lazy yukleme


### 🟡 Orta — Modern format kullanilmiyor

Olculen 15 gorselin hicbiri WebP veya AVIF degil.

**Düzeltme:** WebP'ye cevir; ayni kalitede yuzde 25-35 kuculme.

### 🟡 Orta — Dort gorselde boyut belirtilmemis

15 gorselin 11'inde width ve height var, dordunde yok - duzen kaymasi riski.

**Düzeltme:** Tum gorsellere acik boyut ekle.


---

## Kapsam ve güven sınırları

Bu denetimin neyi ölçemediği, ölçtüğü kadar önemlidir:

- CrUX saha verisi ve Search Console indeksleme durumu olculemedi: Google API kimlik bilgisi yok.
- Laboratuvar boyama metrikleri (LCP, FCP) yakalanamadi; tarayici bolmesi gorunur boyutta degil.
- Backlink verisi yalnizca Common Crawl alan adi duzeyinde; Moz ve Bing anahtarlari yok, yonlendiren alan adi listesi cikarilamadi.
- 94 sayfalik temsili ornek olculdu, 1.114 URL'nin tamami degil.
- Bugun yapilan degisikliklerin siralama etkisi henuz olculemez; yeniden tarama ve indeksleme haftalar alir.
