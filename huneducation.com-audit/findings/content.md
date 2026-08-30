# İçerik kalitesi ve E-E-A-T — bulgular

Kaynak: 500 sayfalık canlı tarama + örnekleme (10 program sayfası, /about-us/,
/student-perspectives/, /costs/, /admission/) + WordPress veritabanından doğrudan
okuma. Tarih: 2026-08-30.

> Not: Bu dosya, denetimin içerik ajanı oturum yeniden başlarken kesildiği için
> orkestratör tarafından, ajanın topladığı doğrulanmış verilerle yazılmıştır.
> Kapsam bu yüzden ajanın planladığından dardır: 14 EN editoryal sayfanın
> tamamı değil, 4'ü tek tek incelendi.

## Kritik

### 1. İngilizce ana sayfanın `<title>` etiketi tamamen Türkçe
`https://huneducation.com/` → `lang="en-US"`, H1 İngilizce ("Search Your Favorite
Course Here"), ama başlık:

> "HunEducation – Macaristan üniversiteleri, Macaristan yüksek lisans ve
> Macaristan'da üniversite okumak hakkında profesyonel danışmanlık hizmetleri
> veriyoruz."

Sitenin en değerli tek URL'si, İngilizce içerik sunarken Türkçe anahtar
kelimelerle etiketlenmiş. Bu haliyle ne İngilizce sorgularda yarışabiliyor
(başlıkta İngilizce kelime yok) ne de Türkçe sorgularda (sayfa İngilizce).
Ayrıca 154 karakterle SERP'te kesiliyor.

**Düzeltme:** İngilizce, 60 karakterin altında, birincil hedefe göre yeniden
yazılmalı. Örn. *"Study in Hungary: English-Taught Degrees & Fees | Hun Education"*.

### 2. Editoryal sayfaların başlıkları tek kelimelik
`/courses/` → "Courses – HunEducation", `/admission/` → "Admission – HunEducation",
`/costs/` → "Costs – HunEducation". Hiçbirinde ülke adı, yıl, ücret aralığı ya da
hedef sorgu yok. Bunlar sitenin para sayfaları.

### 3. 494/500 sayfada meta description yok
Google snippet'i gövdeden uydurmak zorunda. Kök sebep: Yoast pasif.

## Yüksek

### 4. 338 program sayfasında hiç açıklama metni yok
984 program kaydının **646'sında** `post_content` dolu, **338'inde tamamen boş**.
Bu sayfalar yalnızca alan bloğundan (seviye, başlangıç, dönem, son başvuru,
ücret, üniversite, şehir) ibaret.

Açıklaması olanlar makul: örneklediğim 10 sayfa 222–486 kelime arasında
(ortalama ~330), gerçek bir "Course Description" bölümü var. Yani sorun
"hepsi ince" değil, **üçte biri boş**.

### 5. Bilgi amaçlı içerik katmanı hiç yok
Sitede **0 blog yazısı** var. Dönüşüm öncesi bütün sorgular karşılıksız:
öğrenci vizesi süreci ve red sebepleri, YÖK denkliği, apostil, ikamet kartı,
çalışma izni, ilk ay kontrol listesi, yurt başvurusu. Bunlar hem organik giriş
noktası hem de para sayfalarına iç bağlantı kaynağı olurdu.

SXO tarafındaki bulguyla örtüşüyor: **Macaristan öğrenci vizesi için ayrı bir
sayfa dahi yok** ve o sorgu tamamen vize/seyahat acentelerine bırakılmış.

### 6. E-E-A-T: kurum var, kişi yok
`/about-us/` 851 kelime ve doğru şeyleri söylüyor ("expert academic advisers",
"independent, receiving no support from the government", 1999'dan beri). Ama:

- Danışmanların **adı, unvanı, özgeçmişi yok** — "expert advisers" soyut kalıyor
- Yazar kimliği hiçbir sayfada yok; içerik kimin kaleminden belirsiz
- Üyelik/sertifika/akreditasyon rozeti yok
- `/student-perspectives/` 481 kelime ama **tek bir isimli öğrenci yorumu yok**;
  sayfa öğrenci deneyimi vadedip genel pazarlama metni veriyor

Ailelerin yılda ~10.000 € taahhüt ettiği bir hizmette bu, güvenin en zayıf
halkası. Rakipler aynı boşlukta.

## Orta

### 7. Tıp sayfasında iki başlık aynı şeyi söylüyor
`/macaristanda-tip-egitimi-ve-macaristanda-tip-okumak/` içinde:
"Macaristan'da Tıp Okumak İçin Gerekenler" ve "Macaristan'da Tıp Okuma Şartları"
— aynı konu, iki H2. Ayrıca sayfada **hiç tablo yok**, oysa sorgu
üniversite-üniversite karşılaştırma istiyor.

### 8. Tarih sinyali yok
Hiçbir sayfada "son güncelleme" tarihi görünmüyor; yapısal veri de olmadığı için
`dateModified` de yok. Ücret ve son başvuru tarihi yayınlayan bir sitede
tazelik sinyalinin yokluğu hem kullanıcı güvenini hem tazelik sıralamasını
düşürüyor.

## Bilgi — iyi durumda olanlar

- Program sayfalarının açıklaması olanlar **ince değil** (~330 kelime, gerçek
  prosa + benzersiz alan verisi). "Scaled content abuse" kapsamına girmezler:
  veriye dayalı katalog sayfası deseni, üretilmiş dolgu değil.
- `/about-us/` bağımsızlık beyanı ve kuruluş yılı gibi doğru güven unsurlarını
  içeriyor; eksik olan somutlaştırma.
- İçerik iki dilde gerçekten ayrı yazılmış; makine çevirisi izlenimi vermiyor.

## Öncelikli düzeltmeler

1. EN ana sayfa başlığını İngilizceye çevir *(dakikalar)*
2. 14+14 editoryal sayfaya başlık + meta description yaz *(bir gün)*
3. 338 boş program sayfasına en az bir paragraf açıklama üret *(şablon + veri)*
4. Danışman ekibini isim, unvan ve deneyimle yayınla; öğrenci yorumlarını
   isimlendir *(E-E-A-T'nin en hızlı kazancı)*
5. Vize / denklik / apostil eksenli bilgi içeriği katmanını başlat

Score: 34/100
