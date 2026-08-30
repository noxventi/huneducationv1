# tr.huneducation.com — Türkiye pazarı rakip kıyaslaması

**Tarih:** 30 Ağustos 2026
**Rakip seçimi:** tahminle değil, iki Türkçe sorguda gerçekten sıralanan siteler
(`macaristan üniversite eğitim danışmanlık Türkiye` ve
`"macaristan'da üniversite okumak" bölümler ücretler başvuru`).

---

## 1. Otorite (Common Crawl web grafiği, cc-main-2026-jan-feb-mar)

| Site | PageRank sırası | Harmonik merkezilik | Host |
|---|---|---|---|
| academix.com.tr | **1.378.391** | 7.259.522 | 6 |
| elt.com.tr | 8.170.009 | 15.279.131 | 2 |
| icesturkey.com | 8.184.805 | **3.359.349** | 3 |
| **huneducation.com** | **19.666.393** | 13.997.358 | 3 |
| macaristandauniversite.com | sıralamada yok | — | — |
| gedu.com.tr | sıralamada yok | — | — |
| iecc.com.tr | sıralamada yok | — | — |
| unioku.com | sıralamada yok | — | — |

**Okuma:** Türkiye pazarında orta sıradayız. academix ~14 kat, elt ve icesturkey
~2,4 kat önde; dört rakip ise Common Crawl sıralamasına hiç girmemiş, yani bizden
zayıf ya da benzer. Bu, uluslararası kıyaslamadan (studyinhungary.hu 399.605,
bizden 49 kat önde) **çok farklı** bir tablo.

**Sınır:** Common Crawl kayıtlı alan adı düzeyinde ölçer; `tr.` alt alanı ayrı
ölçülemez. Rakamlar `huneducation.com` bütününe aittir.

---

## 2. Baş terim sayfası — içerik derinliği

Karşılaştırılan sayfa: her sitenin "Macaristan'da üniversite" hedefli sayfası.

| Site | Ham HTML kelime (menü/footer hariç) | Render edilmiş tam belge |
|---|---|---|
| academix.com.tr | 3.673 | 14.805 |
| icesturkey.com | 3.541 | 20.510 |
| elt.com.tr | 3.122 | 9.133 |
| gedu.com.tr | 2.524 | 11.910 |
| iecc.com.tr | 1.302 | 6.099 |
| **BİZ — macaristanda-universite-okumak** | **1.013** | 7.283 |
| unioku.com | 817 | 5.800 |
| deltaegitim.com.tr | 192 *(JS ile basıyor)* | 30.173 |
| macaristandauniversite.com | 90 *(JS ile basıyor)* | 5.007 |

**Ölçüm uyarısı — iki sütun da tek başına yanıltıcıdır.**
Ham HTML sütunu, içeriğini JavaScript ile basan siteleri (deltaegitim,
macaristandauniversite) olduğundan ince gösterir. Render sütunu ise menüyü,
footer'ı ve liste öğelerini de sayar; bizim katalog sayfamızın 40.282 çıkması
bundandır. Savunulabilir okuma: sunucu tarafında basan rakiplerin (academix,
icesturkey, elt, gedu) gövde metniyle bizimkini karşılaştırmak. O ölçüte göre
baş terim sayfamız **en güçlü dördün yaklaşık üçte biri**.

---

## 3. Teknik ve yapısal sinyaller

| Site | hreflang | canonical | OG | title uzunluğu | şema tipi |
|---|---|---|---|---|---|
| **BİZ** | **3** | var | var | **23–46** | 12 |
| elt.com.tr | 0 | var | var | 59 | 9 |
| gedu.com.tr | 0 | var | var | 59 | 13 |
| icesturkey.com | 0 | var | var | 63 | 5 |
| academix.com.tr | 0 | var | var | 60 | 8 |
| iecc.com.tr | 0 | **YOK** | var | 42 | 0 |
| unioku.com | 0 | var | **YOK** | 73 | 0 |
| deltaegitim.com.tr | 0 | var | var | 87 | 12 |
| macaristandauniversite.com | 0 | var | var | 20 | 7 |

**Rakiplerin hiçbirinde hreflang yok.** İki dilli çalışan ve bunu doğru
bildiren tek site biziz.

**Başlık disiplini bizde.** 23–46 karakter; rakiplerin çoğu 59–87 arasında,
yani birkaçı arama sonucunda kesiliyor.

### Şema karşılaştırması

| Site | Temel dışı şema |
|---|---|
| **BİZ** | BreadcrumbList, Organization, ContactPoint, PostalAddress **+ program sayfalarında Course, üniversite sayfalarında CollegeOrUniversity** |
| academix.com.tr | AggregateRating, ItemList, Service, SiteNavigationElement, ContactPoint, Organization |
| gedu.com.tr | Article, BreadcrumbList, CommentAction, Organization |
| deltaegitim.com.tr | Article, BreadcrumbList, Organization |
| elt.com.tr | FAQPage, Question, Answer, Organization |
| icesturkey.com | FAQPage, Question, Answer |
| iecc.com.tr / unioku.com | yok |

**Not:** elt ve icesturkey'in FAQPage kullanımı artık avantaj değil. Google
7 Mayıs 2026'da FAQ zengin sonuçlarını tüm siteler için kaldırdı. Bunu
kopyalamayın.

---

## 4. Ölçek ve kapsam — asıl fark burada

| Site | Sitemap URL | Kapsam |
|---|---|---|
| academix.com.tr | 4.503 | ~20 ülke: İngiltere, Kanada, İtalya, Hollanda, Ukrayna, İrlanda… |
| icesturkey.com | 721 | Çok ülke, alan bazlı sayfalar (mühendislik, sağlık, mimarlık…) |
| **tr.huneducation.com** | **551** | **Tamamı Macaristan:** 487 program + 21 üniversite + 29 merkez + 14 sayfa |

academix'in URL sayısı bizden fazla ama yaklaşık yirmi ülkeye yayılmış; ülke
başına derinlik ince. **Macaristan özelinde program düzeyinde derinliği olan
tek site biziz.** Bu, uzun kuyruk sorgularının ("debrecen üniversitesi makine
mühendisliği ücret") tam olarak karşılığıdır ve otoritenin en az önemli olduğu
yerdir.

---

## 5. Sonuç

**Kaybettiğimiz yer:** baş terim bilgi sayfalarının derinliği (1.013'e karşı
2.524–3.673) ve otorite (academix 14 kat önde).

**Kazandığımız yer:** hreflang (tek biz), başlık disiplini, Course/
CollegeOrUniversity yapısal verisi (rakiplerde yok) ve Macaristan'a özel
program derinliği.

**Kopyalanacak:** academix'in AggregateRating, Service ve ItemList şeması.
**Kopyalanmayacak:** FAQPage — Google Mayıs 2026'da kaldırdı.
