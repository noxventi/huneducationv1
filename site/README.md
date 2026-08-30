# Hun Education — yeniden tasarım prototipi

Yerelde çalışan, bağımlılıksız bir ön yüz. Tüm animasyonlar bu depoda elle yazıldı:
GSAP, Framer Motion, Lenis, ScrollTrigger veya benzeri bir kütüphane **kullanılmadı**.

## Çalıştırma

```bash
python -m http.server 5199 --directory site
```

Sonra `http://localhost:5199` adresini açın. ES modülleri kullanıldığı için `file://`
üzerinden değil, bir sunucu üzerinden açılmalıdır.

## Diller ve URL yapısı

Site iki dilde, **iki ayrı alan adında** yayınlanır (WPML, dil başına alan adı):

| Dil | Alan adı |
|---|---|
| İngilizce (varsayılan) | `huneducation.com` |
| Türkçe | `tr.huneducation.com` |

**Slug'lar canlıdan alınmıştır ve değiştirilmez.** Bunlar hâlihazırda yayında ve
sıralaması olan adresler; yeni tasarım aynı URL'lerin üzerine geliyor. Türkçe
slug'lar anahtar kelimeyi zaten taşıyor (`macaristan-universite-fiyatlari` gibi),
kısaltmak kayıp olurdu.

| Sayfa | İngilizce | Türkçe |
|---|---|---|
| Ana sayfa | `/` | `/` |
| Neden Macaristan | `/why-hungary/` | `/neden-macaristanda-egitim/` |
| Ana rehber | `/education-in-hungary/` | `/macaristanda-universite-okumak/` |
| Üniversiteler | `/universities/` | `/macaristan-universiteleri/` |
| Katalog | `/courses/` | `/kurslar/` |
| Başvuru | `/admission/` | `/macaristan-universite-basvuru-sartlari/` |
| Maliyetler | `/costs/` | `/macaristan-universite-fiyatlari/` |
| Yüksek lisans | `/masters-education-in-hungary/` | `/macaristan-yuksek-lisans/` |
| Tıp | `/studying-medicine-in-hungary-…/` | `/macaristanda-tip-egitimi-…/` |
| Pilotaj | `/pilot-training-at-hungarian-universities/` | `/macaristan-universiteleri-pilotluk-egitimi/` |
| Yaşam | `/university-education-and-life-…/` | `/macaristanda-yasam-ve-universite-egitimi-…/` |
| Öğrenci görüşleri | `/student-perspectives/` | `/macaristan-universiteleri-ogrenci-gorusleri/` |
| Hakkımızda | `/about-us/` | `/hakkimizda/` |
| İletişim | `/contact/` | `/iletisim/` |
| Yasal (4 sayfa, **yeni**) | `/privacy-notice/` … | `/kvkk-aydinlatma/` … |

Toplam **36 sayfa** (18 çift). Son 4 çift canlıda yok, yeni URL olarak eklenir.

**Yereldeki `tr/` klasörü yalnızca dosyaları ayırmak içindir.** Canlıda iki dil de
tek WordPress kurulumunda durur ve WPML alan adına göre yönlendirir; `/tr/` diye
bir yol yoktur. Bu yüzden yerel dosyalar göreli bağlantı kullanır ama
canonical/hreflang/sitemap üretim URL'lerini yazar.

Taşıma haritası ve kontrol listesi: [`TASIMA-PLANI.md`](../TASIMA-PLANI.md)

### Her sayfada
* `<html lang>` doğru
* `canonical` kendi üretim URL'sini gösterir
* `hreflang` **karşılıklı**: en / tr / x-default üçlüsü iki tarafta da aynı çifti
  işaret eder — karşılıklı olmayan alternatifleri Google yok sayar
* Dil değiştirici karşı dilin **eş sayfasına** gider, ana sayfaya değil

Denetim: `python tools/audit_i18n.py site` (36 sayfanın tamamını kontrol eder).

## Dosya yapısı

```
site/
  index.html                       İngilizce ana sayfa (13 bölüm)
  courses.html                     Katalog: canlı filtre, URL senkronizasyonu
  why-hungary.html                 Neden Macaristan
  education-in-hungary.html        Ana rehber (pillar)
  universities.html                19 üniversite, şehir ve alan tablosu
  admission.html                   Başvuru şartları, belgeler, sınavlar, takvim
  costs.html                       Ücretler ve yaşam giderleri
  masters-education-in-hungary.html
  studying-medicine-in-hungary-…html
  pilot-training-at-hungarian-universities.html
  university-education-and-life-…html
  student-perspectives.html
  about-us.html · contact.html     Kurumsal ve iletişim
  privacy-notice.html · consent.html · cookie-policy.html · terms-of-use.html
  tr/                              Aynı 18 sayfanın Türkçesi
  sitemap.xml · robots.txt         Alan adı başına birer tane (tr/ altında da)
  assets/
    css/
      tokens.css          Renk, tipografi, uzay, hareket token'ları + self-host fontlar
      base.css            Reset, tipografi, erişilebilirlik, veri dürüstlüğü rozetleri
      components.css      Buton, kart, akordiyon, form, header, imleç, reveal ilkelleri
      sections.css        Ana sayfa bölümleri
      catalog.css         Katalog sayfası
    js/
      core/util.js        Matematik, easing, tek rAF döngüsü, ortam algılama
      core/scroll.js      Scroll ilerlemesi motoru + IntersectionObserver reveal
      core/i18n.js        Dil katmanı: sözlük, para/süre biçimi, rota adları
      modules/*.js        Bölüm davranışları
      main.js             Ana sayfa orkestrasyonu
      catalog.js          Katalog sayfası
    data/catalog.js       CMS veri modelinin ön yüz karşılığı (iki dilli)
    fonts/                Plus Jakarta Sans, Inter, JetBrains Mono (latin + latin-ext)
    img/                  Görseller
```

## Çeviri nasıl yönetiliyor

Tek kaynak, iki çıktı. Aynı metni iki dosyada tutmanın kaçınılmaz sonucu
sürüklenmedir; bu yüzden hiçbir metin iki kez yazılmaz:

| Katman | Kaynak | Nasıl |
|---|---|---|
| Sayfa gövdeleri | `pages_content*.py` (TR) · `en_content*.py` (EN) | `gen_pages.py <site> <tr\|en>` |
| Header/footer/künye | `gen_pages.py` içindeki `W` sözlüğü | Dile göre seçilir |
| JS arayüz metinleri | `assets/js/core/i18n.js` | `<html lang>` okunur, `t()` ile çözülür |
| Katalog verisi | `assets/data/catalog.js` | Her değer `{ en, tr }`; import anında düz metne çözülür |
| Tutarlar | `catalog.js` içinde **sayı** | Biçim i18n'de: `3.000 €` ↔ `€3,000` |

Tutarların metin değil sayı olarak durması bilinçli: Türkçede binlik ayıracı
nokta ve simge sonda, İngilizcede virgül ve simge başta. Aynı rakamı iki kez
yazmak, birini güncelleyip diğerini unutmanın en kısa yoludur.

---

## 1. Hareket mimarisi

Üç kural üzerine kuruldu:

**Tek kalp.** `core/util.js` içindeki `Ticker` sayfadaki tek `requestAnimationFrame`
döngüsüdür. Her modül ona abone olur. Sekme arka plana geçtiğinde döngü durur.

**Ölçüm ≠ her kare.** `core/scroll.js` `getBoundingClientRect()` çağrısını yalnız
yükleme, resize, font yüklenmesi ve `ResizeObserver` tetiklendiğinde yapar. Her karede
sadece `window.scrollY` okunur → layout thrash yok.

**JS "ne kadar", CSS "nasıl" bilir.** Motor `--hp`, `--fldp`, `--mp` gibi CSS
değişkenleri yazar; dönüşümü CSS yapar. Bu, animasyonu stil katmanında tutar ve
`prefers-reduced-motion` ile tek noktadan kapatılabilir kılar.

### Sahte smooth-scroll neden yok?

Popüler kütüphaneler sayfayı bir `<div>` içine alıp `transform` ile kaydırır. Bu,
`position: sticky` ile yapılan pin bölümlerini, klavye gezinmesini, tarayıcı içi
aramayı ve adres çubuğu davranışını bozar. Bunun yerine: native scroll korundu,
yumuşatma yalnız **animasyon değerlerine** uygulandı (`Track.smooth`). Sonuç aynı
akıcılıkta, davranış ise doğru.

### Bölüm bölüm ne oluyor

| Bölüm | Teknik |
| --- | --- |
| Açılış perdesi | Gerçek yükleme durumu + zaman tabanı; en yavaş olan belirler. Tıklama/klavye ile atlanır, 2,6 sn tavan, oturumda bir kez. |
| Hero | `position: sticky` sahne. Görsel `scale` + `translate`, içerik `translate` + `opacity` + `blur`. Canvas'ta yavaş süzülen ışık zerreleri (logodaki tüy motifi). |
| Güven bandı | Marquee hızı scroll hızına bağlı; yön scroll yönüne göre dönüyor. Tek `transform`, modulo ile sonsuz döngü. |
| Program bulucu | Adım seçimi → ilerleme rayı, canlı sonuç sayısı, paylaşılabilir URL. Ok tuşlarıyla gezinilebilir `radiogroup`. |
| Popüler alanlar | Dikey scroll → yatay hareket. Pin `position: sticky` ile CSS'te; bölüm yüksekliği yatay mesafeye göre hesaplanıyor. Mobilde doğal yatay kaydırma + snap. |
| Süreç | Her adım kendi track'ini alır ve ekran ortasına yaklaşırken açılır. Soldaki halka SVG `stroke-dashoffset` ile ilerler. |
| Manifesto | Kelimeler scroll ile tek tek aydınlanır. Sınıf değişimi yalnız sınır geçildiğinde yapılır. |
| Üniversite haritası | Macaristan sınırı gerçek WGS84 koordinatlarından düzlemsel izdüşümle üretildi; şehir pinleri **aynı izdüşümü** kullanıyor, bu yüzden coğrafi olarak doğru duruyor. Sınır çizgisi scroll ile çiziliyor (`getTotalLength()`), aktif şehirde radar sinyali. |
| Maliyet | Toplam-önce teklif kartı: üstte tahmini yıllık aralık, altında iki segment kontrol (eğitim seviyesi, konaklama), sonra salt okunur döküm. Her satırın alt çizgisi aynı zamanda ölçü çubuğu — toplam içindeki payı kadar dolar. Kırılım noktası viewport değil `container-type: inline-size` ile kartın kendi genişliği. |
| SSS | Yükseklik animasyonu `grid-template-rows: 0fr → 1fr` ile; JS ölçüm yapmıyor. |
| Footer | Dev logotype scroll ile yukarı süzülüyor. |

### `prefers-reduced-motion`

Tek anahtar: CSS'te tüm reveal/transform/marquee nötrleniyor, JS'te `env.reduce`
parçacıkları, imleci, manyetik butonları ve perdeyi tamamen kapatıyor. Scrub metni
anında tam okunur hâle geliyor. **İçerik hiçbir koşulda animasyon için gecikmiyor:**
`data-reveal` stilleri yalnız `html.js-on` varken devreye giriyor, yani JS yoksa veya
çökerse sayfa %100 görünür kalıyor.

---

## 2. Tasarım kararları ve gerekçeleri

**Renk.** Ana lacivert/kobalt logodan türetildi. Aksiyon rengi olarak sıcak kor
(`#ff5a36`) seçildi: lacivert üzerinde yüksek kontrast veriyor ve sitedeki tek "tıkla"
sinyali olduğu için birincil CTA her yerde tartışmasız görünür oluyor. Yeşil yalnız
WhatsApp/durum için ayrıldı. Macar bayrağı renkleri dekoratif olarak tekrarlanmadı.

**Tipografi.** Başlık Plus Jakarta Sans, gövde Inter, veri/etiketler JetBrains Mono.
Mono'nun rolü estetik değil retorik: ücret, tarih, kaynak ve durum etiketleri mono ile
yazıldığı için "bu bir veri alanı, kaynağı belli" mesajı görsel olarak taşınıyor.
Üç font da latin + latin-ext alt kümesiyle self-host edildi → Türkçe karakterler
eksiksiz, üçüncü taraf istek yok.

**Logo ölçeklendirmesi.** `logo2.png` yatay bir lockup (250×70) ve iç dağılımı dengesiz:
kuş kutunun tamamını kaplarken "HunEducation" yazısı yalnız %39'unu kaplıyor, üstelik
optik merkezi kutu merkezinin %7,1 altında. Bu yüzden boyut **kutu yüksekliğine göre değil
logotype cap-height'ine göre** seçildi — menü metninin 1,40 katı, tipografik hiyerarşide
markanın önerilen 1,3–1,5× bandında. Dikey hizalama `translateY(-7.1%)` ile telafi edilir;
yüzde elemanın kendi yüksekliğine bağlı olduğu için her boyutta kendiliğinden doğru kalır.

Tek yerden ayarlanır — `tokens.css`:

```css
--logo-h: 40px;          /* masaüstü kutu yüksekliği */
--logo-h-compact: 36px;  /* header scroll ile kompaktlaşınca */
--logo-optical: -7.1%;   /* yazıyı menüyle hizalayan telafi */
```

Bu değeri değiştirirseniz genişlik, hizalama ve mobil karşılıkları kendiliğinden takip eder.
Tek dikkat edilecek nokta: logo genişledikçe header'daki menü payı azalır; masaüstü menünün
drawer'a düştüğü eşik (`components.css`, şu an 1220px) buna göre yeniden ölçülmelidir.

**Mobil.** Ayrı bir denetimden geçti; her kural ölçülmüş bir bulguya karşılık gelir:

- **Tipografi tabanı yükseltildi.** `--step--2` ve `--step--1` mobilde 0,8 / 0,875 rem'e
  sabitlenir. Masaüstünde sorun olmayan 11,5 px'lik etiketler telefonda okunmuyordu —
  12,5 px altı gövde metni 30 örnekten 1'e indi (kalan tek örnek, mono bir eksen etiketi).
- **Dokunma hedefleri.** 44 px altı odaklanabilir öğe 42 → 2; WCAG 2.2 AA'nın 24 px
  eşiğinin altında kalan **hiçbir öğe yok** (12 sayfa × 360/375 px ölçüldü). Görsel
  boyutlar değişmedi; tıklama alanı dolgu + negatif margin ile büyütüldü.
- **Harita mobilde girdi aygıtı değil.** Pinler 375 px'te ~20 px'lik hedefe düşüyordu ve
  komşu şehirler yan yanaydı. Küçük ekranda harita görsel katman olur, seçim yatay çip
  şeridinden yapılır; pinler tab sırasından ve erişilebilirlik ağacından çıkarılır.
- **İçindekiler katlanır.** Rehber sayfalarında 9 bağlantılık blok içeriği aşağı itiyordu;
  mobilde kapalı başlar (477 px → 54 px), bir başlığa gidilince kendini kapatır.
- **Grid taşma hatası düzeltildi.** `1fr` sütunun varsayılan `min-width: auto` değeri geniş
  tabloları sütuna şişirtiyor ve tüm rehber sayfalarını yatay kaydırıyordu
  (672 px içerik / 375 px ekran). `minmax(0, 1fr)` ile tablolar kendi kutusunda kayar.
- **Footer sıkıştırıldı.** Bağlantı kolonları iki sütuna alındı: 1659 px → 1386 px.

**Ölçek.** Tüm tipografi `clamp()` ile akışkan; mobil gövde metni hiçbir yerde 16 px
altına düşmüyor, satır uzunlukları 46–75 karakter arasında tutuldu.

**Erişilebilirlik.** Tek `h1`, doğru başlık sırası (denetlendi), tüm görsellerde
anlamlı `alt`, tüm buton/bağlantılarda erişilebilir isim, her yerde görünür focus
halkası, mobil menüde focus tuzağı + Escape, harita pinlerinde ok tuşu gezinme ve
44 px'lik görünmez dokunma hedefi, akordiyonda `aria-expanded`/`aria-controls`.

---

## 2b. İçerik sayfaları ve GEO düzeni

Site dışına içerik bağlantısı vermez — tüm rehberler bu depoda üretildi. İçerik
huneducation.com verisinden **yeniden yazıldı**, kopyalanmadı: yapı, başlıklar, tablolar
ve örnekler özgündür.

Her rehber PRD §11.4'teki "citation-ready" iskeleti izler:

1. **Kısa cevap kutusu** — 40–70 kelimelik doğrudan yanıt (AI alıntısı ve featured snippet için)
2. **İçindekiler** — yapışkan, okunan bölümü işaretler
3. **Veri tabloları** — her ücretin yanında para birimi ve dönem
4. **Adım adım süreç**
5. **İstisnalar ve sık yapılan hatalar**
6. **Birinci el gözlem** — Hun Education saha verisi, kaynak olarak ayrıca etiketli
7. **Kaynaklar** — erişim tarihiyle
8. **SSS** — akordiyon + `FAQPage` şeması
9. **Yazar, son güncelleme ve sonraki kontrol tarihi**
10. **Değişiklik günlüğü**
11. **Bağlama uygun CTA + ilgili sayfalar**

Şema kapsamı sayfa tipine göre: rehberler `Article + BreadcrumbList + FAQPage`,
katalog `CollectionPage + BreadcrumbList`, hakkımızda `AboutPage`, iletişim `ContactPage`,
ana sayfa `Organization/EducationalOrganization` (adres, telefon, sameAs, foundingDate ile)
`+ WebSite + FAQPage`. Her sayfada canonical, hreflang, og:image ve twitter:card tanımlıdır.
Kökte `robots.txt` (AI arama botları açıkça serbest, PRD §11.10) ve yalnız canonical
URL'leri içeren `sitemap.xml` bulunur.

**Editoryal ses:** sitedeki tüm veriler birinci ağızdan sunulur ("danışmanlık ekibimiz
tarafından güncellenir"); üçüncü şahıs kaynak beyanı ve demo/prototip notları kaldırılmıştır.
Rehberlerin değişiklik günlüğüne 05.08.2026 denetim kaydı eklendi.

**Header, footer ve mobil menü** altı sayfada birebir aynıdır ve crawlable `<a href>` olarak
HTML'dedir (PRD §11.7 gereği JS ile enjekte edilmedi). Elle kopyalamak yerine bir üreticiyle
yazıldılar; üretimdeki karşılığı WordPress Theme Builder şablonudur. Üniversite tablosu
`assets/data/catalog.js`'ten okunur — tek kaynak korunur.

---

## 3. Veri kaynağı ve dürüstlük politikası (PRD §10, §16)

Sitedeki tüm işletme verisi Hun Education'ın kendi yayınından derlendi
(**3 Ağustos 2026**):

| Ne | Nereden |
| --- | --- |
| Şirket unvanı, ofisler, telefon, e-posta, çalışma saatleri | `tr.huneducation.com/iletisim/` |
| Üniversite listesi ve şehirler | `tr.huneducation.com/macaristan-universiteleri/` + ana sayfa |
| Öğrenim ücretleri, yaşam giderleri, harçlar | `tr.huneducation.com/macaristan-universite-fiyatlari/` |
| Belgeler, dil şartı, giriş sınavları, başvuru takvimi, iade koşulu | `tr.huneducation.com/macaristan-universite-basvuru-sartlari/` |
| Öğrenci yorumları | `tr.huneducation.com/macaristan-universiteleri-ogrenci-gorusleri/` |
| Alan/kategori taksonomisi (17 kategori) | `tr.huneducation.com/kurslar/` filtreleri |
| Rehber içerikleri ve URL'leri | `huneducation.com` blog menüsü |

Uydurma hiçbir rakam yok. Veriyi taşırken korunan kurallar:

- **Her ücretin yanında para birimi ve dönemi var** (yıllık / dönemlik / tek seferlik).
  Pilotaj dönemlik olduğu için kartında "Dönemlik ücret" yazıyor — yıllıkmış gibi gösterilmiyor.
- **Toplam, ~10 aylık akademik yıl üzerinden hesaplanır.** Aylık kalemleri 12 ile çarpmak
  yayınlanan rakamın üstünde bir toplam üretiyordu; öğrenci yaz aylarını Macaristan'da
  geçirmediği için doğru çarpan 10. Bu varsayımla lisans + yurt senaryosu
  **8.455 – 13.905 €** veriyor ve Hun Education'ın yayınladığı **8.500 – 14.000 €/yıl**
  aralığıyla %1 içinde örtüşüyor. Bu iki rakam kartın altında yan yana gösterilir ki
  hesabın kaynakla tutarlı olduğu görülebilsin.
- **Yalnız gerçek değişkenler seçilebilir.** Eğitim seviyesi ve konaklama tercihi kullanıcının
  eline verildi; "yaşam gideri" veya "sağlık sigortası" gibi kalemler kapatılamıyor, çünkü
  öğrenci bunları zaten ödeyecek — kapatılabilir yapmak sahte bir senaryo üretirdi.
- **Öğrenci yorumları birebir alındı**, isimler kaynaktaki gibi baş harfle. Fotoğraf yok:
  stok görseli gerçek öğrenci gibi sunmamak için sözü tipografi taşıyor.
- **Kodolányi János ve MATE Budapeşte'de** işaretli; kaynakta şehir bilgisi ilk taramada
  eksikti, teyit edildikten sonra haritaya ve katalog filtresine eklendi.
- **Bütçe filtresi "yaklaşık" etiketli.** Bant, giriş ücretinden türetilir ve dönemlik
  tutarlar yıllığa çevrilir; kesin tutar her zaman kartın üzerinde yazar.
- JSON-LD'ye yalnız sayfada görünen iddialar konuldu.

Kalıcı yasal uyarı hem footer'da hem ilgili bölümlerde duruyor: ücretler, tarihler ve
kabul koşulları üniversiteler tarafından değiştirilebilir; vize ve denklik kararları
resmî kurumlara aittir.

---

## 4. Kaynak sitede bulunamayan / çözülemeyen maddeler

Tüm içerik kaynaktan dolduruldu. Aşağıdakiler **sitede karşılığı olmadığı için** açık kaldı:

### 4.1 Yasal metinler — taslaklar yazıldı, hukuk onayı bekliyor

`huneducation.com`'da bu metinler **hiç yayınlanmamış** (tüm olası URL'ler 404; iletişim
formundaki onay kutusu var olmayan metinlere atıf yapıyor). Bu yüzden dört sayfa sıfırdan
yazıldı: [kvkk-aydinlatma.html](kvkk-aydinlatma.html), [acik-riza.html](acik-riza.html),
[gizlilik-cerez.html](gizlilik-cerez.html), [kullanim-kosullari.html](kullanim-kosullari.html).

İçerik; şirketin doğrulanmış bilgileri (unvan, adres, iletişim) ve **bu sitenin fiilî veri
işlemleri** (form alanları, `hun_first_touch`/`hun_curtain` depolaması, WhatsApp yönlendirmesi,
izne bağlı analitik) üzerine kuruldu. KVKK m.10/11 + GDPR yapısı izlendi; iade koşulu
(vize reddinde 30 iş günü) kaynaktaki gerçek politikadan alındı. Footer ve form bağlantıları
tüm sayfalarda bu metinlere bağlandı; sayfalar sitemap'te (öncelik 0.3).

**⚠ Bu metinler hukuki tavsiye değildir. Yayın öncesi bir hukuk danışmanı tarafından
incelenmeli; özellikle saklama süreleri, yetkili hukuk ve NAIH/KVKK başvuru usulleri
teyit edilmelidir.**

### 4.2 Çelişkili deneyim ifadesi — karar verildi

Kaynakta **dört farklı** ifade var: ana sayfada "26 yılı aşkın", hakkımızda sayfasında
"24 yılı aşkın", footer'da "20+ yıl", ayrıca "1999'dan beri". PRD §2.2 bunu zaten bir
sorun olarak işaretlemişti; bulgu doğruladı.

**Karar:** sitede tek ifade olarak **"1999'dan beri"** kullanıldı — her yıl elle
güncellenmesi gerekmeyen, kendi kendini doğrulayan tek biçim.

### 4.3 Kaynaktan alınan, belgeye bağlanması gereken iddialar

Bunlar sitede yayında olduğu için kullanıldı; sahibinin belgeyle desteklemesi hâlinde
kalmalı, aksi hâlde çıkarılmalı (PRD §2.3):

- "Macaristan'daki ilk Türk eğitim danışmanlığı şirketi"
- "Binlerce Türk öğrenci" — sayısallaştırılacaksa hesaplama yöntemiyle birlikte

### 4.4 Kaynağın veremediği teknik girdiler

- **Ücretlerin geçerlilik dönemi** — fiyat sayfasında yayın/güncelleme tarihi yok.
  Sitede "derlendi 03.08.2026" olarak işaretlendi; her akademik yıl başında
  doğrulanmalı (PRD §11.13: ücret ve deadline için aylık kontrol).
- **Öğrenci yorumlarında tam ad** kullanılıp kullanılmayacağı — kaynak baş harf
  kullanıyor, aynısı korundu.
- **Danışmanların doğrudan hat ve e-postaları.** Kaynak sitede 11 danışmanın cep telefonu ve
  e-postası açıkta yayınlanıyor. İletişim sayfasında ad, bölge ve uzmanlık gösterildi;
  doğrudan iletişim bilgileri KVKK ve operasyon politikası netleşene kadar merkezî kanala
  yönlendirildi. Politika izin veriyorsa danışman kartlarına eklenebilir.
- CRM uç noktası, GA4/GTM kimlikleri.
- Üniversite logosu kullanılacaksa izin kontrolü — şu an hiçbir kurum logosu yok.

**Görseller hakkında:** `assets/img/` altındaki fotoğraflar temsilî/stok niteliğindedir.
PRD §9 gereği bunlar gerçek Hun Education öğrencisi, ofisi veya başarı kanıtı olarak
sunulmamalıdır; hero ve rehber görselleri gerçek, izinli fotoğraflarla değiştirilmelidir.

**Tek yerden yönetilen değerler:** WhatsApp numarası
`assets/js/modules/whatsapp.js` → `NUMARA`; tüm katalog verisi `assets/data/catalog.js`.

---

## 5. Bu prototipin kapsamadıkları

Bilerek yapılmayanlar, karışıklık olmasın diye:

- Üniversite/program **detay** sayfa şablonları (ana sayfa + liste yapıldı)
- İngilizce (EN) sürüm — dil mimarisi ve `hreflang` etiketleri hazır, içerik yok
- Gerçek form gönderimi: `form.js` doğrulama, çift gönderim koruması, UTM taşıma ve
  GA4 olay iskeletini içerir; ancak hiçbir uç noktaya istek atmaz
- Danışman ekibi sayfası — iletişim sayfasındaki 11 danışmanın adı, şehri ve uzmanlığı
  kaynakta mevcut; PRD §7.8 bunları ayrı bir "Ekibimiz" sayfasına taşımayı öneriyor
- Çerez izni banner'ı ve Consent Mode
- WordPress/Elementor'a aktarım
