# Canlıya taşıma planı

Bu belge, yerelde yenilenen huneducation.com'un canlıya nasıl alınacağını
anlatır. **Temel kural: hiçbir URL değişmiyor.** Yeni tasarım ve içerik,
canlıda hâlihazırda sıralaması olan adreslerin üzerine gelir. Bu yüzden bu bir
site migrasyonu değil, içerik/tasarım tazelemesidir ve **301 yönlendirmeye
ihtiyaç yoktur**.

Diller ayrı alan adında yayınlanır (WPML, dil başına alan adı):

| Dil | Alan adı |
|---|---|
| İngilizce (varsayılan) | `huneducation.com` |
| Türkçe | `tr.huneducation.com` |

---

## 1. Sayfa eşleme tablosu

14 çift canlıda yayında; slug ve WordPress ID'leri **aynen korunur**.
Sağdaki iki sütun yerel prototipteki karşılıklarıdır.

| # | Canlı EN slug | EN ID | Canlı TR slug | TR ID | Yerel EN dosya | Yerel TR dosya |
|---|---|---|---|---|---|---|
| 1 | `home` *(ön sayfa)* | 10 | `macaristanda-universite` | 2312 | `index.html` | `tr/index.html` |
| 2 | `why-hungary` | 101 | `neden-macaristanda-egitim` | 2313 | `why-hungary.html` | `tr/neden-macaristanda-egitim.html` |
| 3 | `education-in-hungary` | 427 | `macaristanda-universite-okumak` | 2314 | `education-in-hungary.html` | `tr/macaristanda-universite-okumak.html` |
| 4 | `universities` | 937 | `macaristan-universiteleri` | 2319 | `universities.html` | `tr/macaristan-universiteleri.html` |
| 5 | `courses` | 199 | `kurslar` | 2321 | `courses.html` | `tr/kurslar.html` |
| 6 | `admission` | 322 | `macaristan-universite-basvuru-sartlari` | 2329 | `admission.html` | `tr/macaristan-universite-basvuru-sartlari.html` |
| 7 | `costs` | 422 | `macaristan-universite-fiyatlari` | 2327 | `costs.html` | `tr/macaristan-universite-fiyatlari.html` |
| 8 | `masters-education-in-hungary` | 6604 | `macaristan-yuksek-lisans` | 6628 | `masters-education-in-hungary.html` | `tr/macaristan-yuksek-lisans.html` |
| 9 | `studying-medicine-in-hungary-…` | 7031 | `macaristanda-tip-egitimi-…` | 7043 | `studying-medicine-in-hungary-…html` | `tr/macaristanda-tip-egitimi-…html` |
| 10 | `pilot-training-at-hungarian-universities` | 7087 | `macaristan-universiteleri-pilotluk-egitimi` | 7123 | `pilot-training-…html` | `tr/macaristan-universiteleri-pilotluk-egitimi.html` |
| 11 | `university-education-and-life-…` | 6898 | `macaristanda-yasam-ve-universite-egitimi-…` | 6945 | `university-education-and-life-…html` | `tr/macaristanda-yasam-…html` |
| 12 | `student-perspectives` | 6652 | `macaristan-universiteleri-ogrenci-gorusleri` | 7495 | `student-perspectives.html` | `tr/macaristan-universiteleri-ogrenci-gorusleri.html` |
| 13 | `about-us` | 287 | `hakkimizda` | 2311 | `about-us.html` | `tr/hakkimizda.html` |
| 14 | `contact` | 1574 | `iletisim` | 2323 | `contact.html` | `tr/iletisim.html` |

### Yeni eklenen sayfalar (canlıda karşılığı yok)

Bunlar **yeni URL** olarak eklenir. Yeni URL eklemek risksizdir; mevcut URL
değiştirmek değildir.

| EN slug | TR slug |
|---|---|
| `privacy-notice` | `kvkk-aydinlatma` |
| `consent` | `acik-riza` |
| `cookie-policy` | `gizlilik-cerez` |
| `terms-of-use` | `kullanim-kosullari` |

### Dokunulmayanlar

| İçerik tipi | Adet | Karar |
|---|---|---|
| `course` | 498 EN / 486 TR | **Dokunulmaz.** Kendi JetEngine şablonuyla çalışır. |
| `university` | 20 EN / 20 TR | **Dokunulmaz.** |

Bu planda hiçbir kayıt silinmez, hiçbir kayıt draft'a çekilmez.

---

## 2. Neden 301 gerekmiyor

Slug'lar değişmediği için eski adresler yeni adreslerdir. Google'ın gördüğü tek
değişiklik sayfanın içeriği ve düzenidir; URL, başlık yapısı ve iç bağlantı
ağı yerinde kalır.

Bir istisna: **taşıma sırasında yeni bir kayıt açmayın.** Sayfa içeriği mevcut
post ID'nin üzerine yazılmalıdır. Yeni kayıt açmak yeni bir slug ve yeni bir ID
üretir; menüler, WPML çeviri bağları ve Elementor Theme Builder koşulları buna
bağlıdır.

---

## 3. İçerik pariteliği kontrolü

Yeni sayfa eskisinden **ince** olursa sıralama kaybedilir. Taşımadan önce her
çift için şunu kontrol edin:

- Eski sayfadaki her H2 başlığının yeni sayfada bir karşılığı var mı?
- Eski sayfada olup yenide olmayan bir tablo, SSS veya rakam var mı?
- Türkçe sayfalar hacimlidir; özellikle `macaristan-universite-basvuru-sartlari`
  ve `macaristanda-universite` (ana sayfa) karşılaştırılmadan değiştirilmemeli.

Eksik varsa taşımadan **önce** yeni sayfaya eklenir.

---

## 4. Taşıma sırası

### Öncesinde

1. **Search Console'dan** en çok trafik alan sayfa ve sorguları dışa aktarın.
   Bu veri bizde yok, sizde. Taşıma sonrası karşılaştırma için tek referans bu.
2. **Duplicator ile tam yedek** alın; 30 gün saklayın.
3. **Core Web Vitals'ı ölçün** (PageSpeed Insights, ana sayfa + iki iç sayfa).
4. **Instant Indexing'i geçici kapatın.** Aktif ve her değişiklikte Google/Bing'e
   ping atıyor; sayfa sayfa ilerlerken yarım kalmış içeriği bildirmesin.

### Sırasında

5. Sayfaları **tek tek** geçirin, her birinden sonra ön yüzü kontrol edin.
   Sıra önerisi: önce hukuki sayfalar (yeni, risksiz), sonra düşük trafikli
   iç sayfalar, en son ana sayfa.
6. Her sayfada **mevcut post ID'nin içeriğini değiştirin**, yeni kayıt açmayın.
7. Bir çiftin iki dilini birlikte geçirin; tek dilde bırakmak hreflang'i kırar.
8. **Elementor CSS önbelleğini** temizleyin (`_elementor_css` meta + uploads/elementor/css).
9. **LiteSpeed / sunucu önbelleğini** boşaltın.

### Sonrasında

10. **Instant Indexing'i geri açın**; bu noktada tam ve doğru içeriği bildirecek.
11. **Sitemap'i yenileyin** (XML Sitemap Generator aktif).
12. Search Console'da **kapsam hatalarını 2 hafta** izleyin.
13. **CWV'yi tekrar ölçün**; yeni yapıda kütüphane yok, fontlar yerel, tek rAF
    döngüsü var — iyileşme bekleniyor, ama ölçülmeden iddia edilmez.

### Zamanlama

Başvuru yoğunluğu **Nisan–Haziran** ve **Ekim–Kasım**. Bu aylarda taşıma
yapmayın. Ağustos–Eylül başı uygun pencere.

---

## 5. Geri alma

| Ne | Nasıl |
|---|---|
| Tek sayfa | WordPress revizyon geçmişinden önceki sürüme dön |
| Tüm site | Duplicator yedeğinden geri yükle |
| Staging | `staging/` klasörünü sil + `stg_` tablolarını düşür |

Staging ortamı canlıdan tamamen bağımsızdır: ayrı dosya ağacı, ayrı tablo öneki.
Canlı dosyalara ve `wp_` tablolarına bu çalışma boyunca yazılmadı.

---

## 6. Yerel yapıyı üretme

```bash
python tools/gen_pages.py site en
```

```bash
python tools/gen_pages.py site tr
```

```bash
python tools/seo_bilingual.py site
```

```bash
python tools/audit_i18n.py site
```

Son komut 36 sayfanın tamamında `<html lang>`, canonical, karşılıklı hreflang,
dil değiştirici ve çevrilmemiş metin kontrolü yapar.

---

## 7. Veri doğruluğu denetimi (8 Ağustos 2026)

Yerel içerik, canlı huneducation.com verisiyle karşılaştırıldı. Bulunan
hatalar ve düzeltmeleri:

| Konu | Yerelde yanlıştı | Canlıdaki doğrusu |
|---|---|---|
| **Program kataloğu** | 46 kayıt, elle derlenmiş | **490 kayıt**, canlı `course` kayıtlarından üretiliyor |
| **Üniversite sayısı** | 19; MATE listede, UNIVET ve Wekerle yok | **20**; MATE canlıda yok, UNIVET ve Wekerle var |
| **Tıp ücreti** | 16.000 € (tek rakam) | SOTE **19.900 $**, PTE **18.000 $**, SZTE **15.800 €** |
| **Tıp veren üniversite** | 4 (Debrecen dahil) | **3**: SOTE, PTE, SZTE. Debrecen katalogda yok |
| **Diş hekimliği** | 17.350 €'dan | PTE **18.600 €**; SOTE'de diş Almanca |
| **Pilotaj** | Dunaújváros, 7.500–13.500 $/dönem | **BME 29.500 €/yıl**; UOD birleşik program **66.800 €/yıl** |
| **Hazırlık ücreti** | dönemlik | **yıllık** (`course_price` yıllıktır) |
| **Tıp hazırlık** | Szeged'de | **McDaniel** (7.230 / 7.800 €) ve **PTE** (5.850 €) |
| **METU türü** | Özel | **Devlet** |
| **IELTS** | zorunlu gibi | Çoğu üniversite belge istemiyor, kendi mülakatını yapıyor |
| **Banka dökümü** | çekirdek belge | Başvuru için **zorunlu değil**; vize aşamasında gerekli |
| **İade** | koşulsuz 30 iş günü | Konsolosluğun **yazılı ret gerekçesi** iletildikten sonra, "genellikle"; **kayıt ücreti de** iade dışı |
| **Danışman iletişimi** | "yayınlanmıyor" | Her danışmanın doğrudan telefon ve e-postası **yayında** |
| **Öğrenci alıntıları** | aşırı kısaltılmış | Canlıdaki tam metinler kondu |
| **Ülke maliyet tablosu** | Hollanda/Almanya/İngiltere rakamları **benim tahminimdi** | Kaldırıldı; kaynağı olmayan rakam yayınlanmıyor |

### Canlıda olup bende hiç olmayan, eklenen şartlar

- **Yaş sınırı:** hazırlık 25 · lisans 25 · yüksek lisans 28 · tıp/diş/eczacılık sınırsız
- **Uyruk kısıtı:** Hun Education her ülkeden başvuru kabul edemiyor; 20 ülkelik liste eklendi
- **Mali yeterlilik:** ~650 €/ay × 10 ay = **6.500 €** gösterilmesi bekleniyor
- **Sigorta:** en az 3 ay, tercihen 1 yıl seyahat ve kaza sigortası
- **Son başvuru:** bazı üniversiteler **Temmuz sonuna** kadar alıyor

### Katalog nasıl güncellenir

```bash
python tools/build_catalog.py tools/canli.json site/assets/data/catalog.js
```

`canli.json` canlıdaki `course` ve `university` kayıtlarından dışa aktarılır.
Ücretin **yıllık** olduğu kurs sayfasında yazılı: "Price: 19 900 usd/year
(2 semesters)". Dönem sayısı programın toplam uzunluğudur, yıllık ücretin
böleni değil.
