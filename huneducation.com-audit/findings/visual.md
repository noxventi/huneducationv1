# Görsel ve mobil değerlendirme

Kaynak: 20 ekran görüntüsü (5 sayfa × masaüstü/mobil × üst kısım/tam sayfa),
`screenshots/` klasöründe. Mobil 390×844, masaüstü 1440×900.

> Not: Görsel ajanı yakalamayı tamamladı ama analiz dosyasını yazamadan oturum
> yeniden başladı. Bu dosya, yakalanan görüntüler doğrudan incelenerek yazıldı.

## Kritik

### 1. Program kartlarında ilan edilen son başvuru tarihlerinin %100'ü geçmiş
`courses_mobile_abovefold.png` — ilk kartta büyük puntoyla:

> **Application deadline: June 30, 2025**

Bugün 2026-08-30. Veritabanından doğruladım: tarih girilmiş **965 programın
965'inde** son başvuru tarihi geçmiş.

| Son başvuru yılı | Program |
|---|---|
| 2023 | 3 |
| 2024 | 68 |
| **2025** | **892** |
| 2026 | 2 |

`course-year` taksonomisi de aynı: 953 program "2025", 31 program "2024", **2026
kaydı yok**. En son düzenlenen program: 2026-03-09 — yaklaşık altı ay önce.

Yani sitenin ana varlığı olan ~984 sayfalık katalog, ziyaretçiye 14 ay önce
kapanmış başvuru dönemlerini gösteriyor. Bu hem dönüşümü doğrudan öldürür hem de
arama motorlarına bayatlık sinyali verir. Teknik bir SEO sorunu değil — ticari
bir sorun.

### 2. İngilizce sitede Türkçe WhatsApp widget'ı
Beş ekran görüntüsünün hepsinde, alt kısımda sabit duran yeşil düğme:
**"Size Nasıl Yardımcı Olabiliriz?"** — `huneducation.com` (lang="en-US")
üzerinde. İngilizce ziyaretçi anlamadığı bir dille karşılanıyor.

Türkçe `<title>` bulgusuyla aynı sınıftan: dil ayrımı yapılandırılmamış.

## Yüksek

### 3. Ana sayfanın üst kısmında değer önerisi yok, arama formu var
`home_mobile_abovefold.png`: ilk ekranın tamamı H1 + 6 filtre alanı + 2 düğme.

- H1 **"Search Your Favorite Course Here"** — bir arayüz talimatı; hedeflediği
  hiçbir sorgu yok. Sitenin en değerli sayfasının H1'i bu.
- Değer önerisi ("The best Hungarian universities' majors in English & German")
  H1'in altında küçük punto, tamamı büyük harf — okunması zor.
- Ne telefon numarası, ne "1999'dan beri", ne öğrenci sayısı, ne bir güven
  işareti. Ailenin yılda ~10.000 € taahhüt edeceği bir kararda ilk ekran
  hiçbir güven unsuru taşımıyor.
- "English & German" ifadesi sitenin geri kalanıyla çelişiyor (her yerde
  İngilizce eğitim deniyor).

### 4. Katalog mobilde kullanılamayacak kadar yavaş ilerliyor
`courses_mobile_full.png`: filtre formu ilk ekranı tamamen kaplıyor, ilk program
kartı ancak ikinci ekranda başlıyor ve tek kart neredeyse bir ekran yüksekliğinde.
490 program, sayfa başına ~20 kayıt, 25 sayfa. Telefonda programa ulaşmak için
önce formu geçmek, sonra sayfalama yapmak gerekiyor.

Kartın içeriği iyi (seviye, başlangıç, son başvuru, ücret, üniversite) — sorun
yoğunluk ve gezinme.

## Orta

### 5. Hero görselinin üzerindeki gradyan görüntüyü yok ediyor
Sarı→camgöbeği degrade, arkadaki öğrenci fotoğrafını neredeyse tamamen bastırıyor.
Fotoğraf var ama görünmüyor; hem estetik hem güven açısından boşa harcanmış alan.

### 6. Katalog başlığındaki kırmızı bant
`Courses` başlığı düz kırmızı zemin üzerinde; sitenin lacivert/sarı kimliğiyle
ilişkisiz. Şablon varsayılanı izlenimi veriyor.

## Bilgi — iyi olanlar

- **Yatay taşma yok**: beş sayfanın hiçbirinde, iki görünümde de
  (`horizontalOverflow: 0`). Bu gerçek bir artı.
- Dokunma hedefleri geniş; form alanları ve düğmeler 44 px eşiğinin üzerinde.
- Yazı tipi boyutları mobilde okunabilir.
- Program kartındaki bilgi mimarisi doğru: kullanıcının sorduğu beş şey
  (seviye, tarih, süre, ücret, üniversite) tek bakışta görünüyor.

## Ölçülen yükleme davranışı

| Sayfa | DOMContentLoaded | load | Belge yüksekliği (mobil) |
|---|---|---|---|
| Ana sayfa | 3,28 sn | 5,09 sn | 14.790 px |
| Ana sayfa (mobil) | 3,36 sn | 5,17 sn | — |

Beş saniyeye yakın yükleme, mobil bağlantıda daha da uzayacaktır.

Score: 42/100
