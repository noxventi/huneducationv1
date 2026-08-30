# HUN Education Web Sitesi Baştan Aşağı Yenileme PRD'si

**Belge türü:** Product Requirements Document (PRD) + Claude uygulama talimatı  
**Proje:** huneducation.com / tr.huneducation.com yeniden tasarımı  
**Tarih:** 2 Ağustos 2026  
**Birincil pazar:** Türkiye'den Macaristan'da hazırlık, lisans ve yüksek lisans eğitimi almak isteyen öğrenciler ve aileleri  
**Birincil dil:** Türkçe  
**İkincil dil:** İngilizce  
**Ana iş hedefi:** Nitelikli danışmanlık ve başvuru taleplerini artırmak

---

## 1. Claude için ana görev

Hun Education'ın mevcut web sitesini baştan aşağı yeniden tasarla. Yeni site yalnızca daha modern görünmemeli; kullanıcıyı doğru üniversite ve programa ulaştıran, Hun Education'a güven duymasını sağlayan ve danışmanlık görüşmesine yönlendiren yüksek dönüşümlü bir eğitim platformu olmalıdır.

Bu PRD'deki bilgi mimarisini, içerik hiyerarşisini, bileşenleri, kullanıcı akışlarını, SEO ve ölçüm gereksinimlerini temel al. Tasarımı mobil öncelikli kur. Gerçek verisi bulunmayan hiçbir başarı sayısı, üniversite ortaklığı, öğrenci yorumu, ücret, son başvuru tarihi veya denklik garantisi üretme. Eksik işletme bilgilerini uydurmak yerine açıkça **[CMS'den girilecek]** veya **[müşteri tarafından doğrulanacak]** olarak işaretle.

Mevcut WordPress + Elementor altyapısı korunacaksa tüm bileşenleri tekrar kullanılabilir global stiller, şablonlar ve dinamik içerik alanlarıyla kur. Farklı bir teknik çözüm kullanılacaksa aynı CMS düzenleme kolaylığı, SEO kontrolü ve program veri tabanı işlevleri eksiksiz karşılanmalıdır.

---

## 2. Mevcut durum denetimi

### 2.1 Korunması ve geliştirilmesi gereken güçlü varlıklar

- Hun Education'ın Macaristan odaklı net bir uzmanlık alanı bulunuyor.
- Marka, “1999'dan beri” ifadesiyle uzun geçmişini anlatabiliyor. Bu, yıl sayısını her sene elle değiştirmekten daha güvenilir ve sürdürülebilir bir ifade.
- Üniversite ve program sayfalarından oluşan değerli bir içerik/veri tabanı mevcut.
- Eğitim ücretleri, başvuru koşulları, Macaristan'da yaşam, tıp, pilotaj ve yüksek lisans gibi yüksek arama niyetli içerikler mevcut.
- Budapeşte merkez ofisi ile Türkiye ve Macaristan'daki danışman/temsilci ağı önemli bir güven unsuru.
- Öğrenci görüşleri ve gerçek öğrenci fotoğrafları güçlü sosyal kanıt üretme potansiyeline sahip.
- WhatsApp, telefon, e-posta ve form üzerinden birden fazla iletişim kanalı mevcut.

### 2.2 Yenilemede çözülmesi gereken sorunlar

- Türkçe site alt alan adında, İngilizce site ana alan adında çalışıyor. Dil mimarisi ve SEO sinyalleri tek, tutarlı bir sistem olarak ele alınmalı.
- Deneyim anlatımı farklı sayfalarda “20+”, “24+”, “26+” ve “1999'dan beri” şeklinde değişiyor. Tek doğrulanmış ifade kullanılmalı.
- Ana sayfadaki içerik, arama modülü ve çok sayıda bölüm arasında parçalı ilerliyor; birincil değer önerisi ve başvuru yolu yeterince berrak değil.
- Metinlerde yazım, anlatım ve çeviri hataları bulunuyor. Örnekler: “zHuneducation”, tekrar eden sözcükler, Türkçe sayfalarda İngilizce form metinleri ve “More information” bağlantıları.
- Üniversite ve program detay sayfalarında kritik karar bilgileri standart bir formatta sunulmuyor. Ücret, süre, dil, kabul şartı, başlangıç dönemi ve son güncelleme tarihi her sayfada aynı yerde olmalı.
- Bazı iddialar aşırı kesin veya mevzuata bağlı: YÖK denkliği, “sınavsız”, vize, oturum ve mezuniyet sonrası çalışma konuları koşullu ve kaynaklı anlatılmalı; garanti dili kullanılmamalı.
- Çok sayıda benzer CTA var fakat CTA metinleri ve sonrasındaki akış standart değil.
- İletişim sayfası çok uzun bir danışman listesine dönüşüyor; doğru danışmana yönlendirme ve hızlı başvuru önceliğini kaybediyor.
- Formlar sayfadan sayfaya dil ve alan yapısı bakımından tutarsız.
- Ana sayfa kaynak kodunda güçlü bir meta açıklama, Open Graph/Twitter etiketleri, hreflang ve görünür yapılandırılmış veri sinyalleri eksik veya yetersiz görünüyor.
- Sayfa çok sayıda Elementor/Jet eklentisi ve büyük bir HTML çıktısı kullanıyor. Performans ve eklenti yükü yeniden ele alınmalı.
- Sayfa yanıtlarında oturum çerezi ve `no-store/no-cache` davranışı görülüyor. Her ziyaretçi için zorunlu olmayan oturum başlatılmamalı; herkese açık sayfalar güvenli biçimde önbelleklenebilmelidir.

### 2.3 Yeniden konumlandırma

**Önerilen marka vaadi:**  
“Macaristan'da üniversite yolculuğunuzun her adımında, Türkiye'den yerleşime kadar yanınızdayız.”

**Destekleyici değer önerisi:**  
“1999'dan beri Macaristan odaklı akademik danışmanlık; program seçiminden başvuruya, vizeden konaklama ve şehir oryantasyonuna kadar uçtan uca destek.”

Bu cümleler yayına alınmadan önce hizmet kapsamıyla doğrulanmalıdır. “Resmî başvuru merkezi”, “ilk Türk danışmanlık şirketi”, “binlerce öğrenci” ve üniversite partnerliği gibi iddialar yalnızca belge veya doğrulanabilir şirket verisi varsa kullanılmalıdır.

### 2.4 Rakip ve benchmark analizi

Rakip değerlendirmesi yalnızca görsel tasarımla sınırlı tutulmamalıdır. Organik görünürlük, program veri modeli, güven inşası, karar destek araçları ve lead akışı birlikte incelenmelidir.

#### Türkiye pazarındaki doğrudan rakipler

| Rakip / grup | Güçlü olduğu alan | Gözlenen boşluk | Hun Education'ın üstünlük fırsatı |
| --- | --- | --- | --- |
| ELT | Macaristan için geniş rehber içerikleri; tıp, maliyet ve hizmetler gibi yüksek niyetli sayfalar; güncel tarihli içerik üretimi | Çok ülke ve hizmet odağı nedeniyle Macaristan uzmanlığı markanın tamamına hâkim değil | “Yalnızca Macaristan” uzmanlığını program veri tabanı, yerel ekip ve özgün saha verisiyle kanıtlamak |
| Academix | Köklü marka algısı; ülke ve kabul rehberleri | Macaristan içerikleri geniş portföyün bir parçası | Macaristan'a özel daha derin üniversite, bölüm, şehir ve başvuru içeriği |
| ICE Turkey | Kabul şartlarını hızlı ve maddeli anlatma | Genel bilginin ötesinde özgün veri ve karar araçları sınırlı | Üniversiteye göre şart/ücret/tarih karşılaştırması ve uygunluk değerlendirmesi |
| Meda / İntergenç ve benzeri ülke uzmanları | Macaristan tecrübesi ve temsilcilik söylemi | İçerik ve dijital ürün deneyimi çoğunlukla geleneksel ajans yapısında | Köklü uzmanlığı modern program bulucu, karşılaştırma ve gerçek öğrenci kanıtlarıyla birleştirmek |
| Genel yurtdışı eğitim siteleri | Çok sayıda ülke sayesinde yüksek domain kapsama alanı ve backlink | İçeriklerin güncelliği, özgünlüğü ve Macaristan derinliği değişken | Tek ülke için “başvurudan yerleşime” en güvenilir Türkçe kaynak olmak |

Türkiye rakiplerinde tekrar eden ortak sorun; aynı genel bilgilerin farklı cümlelerle çoğaltılması, eski ücretlerin güncelmiş gibi sunulması, kaynak ve son güncelleme tarihinin eksikliği, YÖK/vize konularında fazla kesin dil ve program sayfalarının standart olmayan yapısıdır. Hun Education bu sorunları tekrar etmemelidir.

#### Yurtdışı tabanlı benchmarklar

| Benchmark | En iyi yaptığı şey | Hun Education'a uyarlanacak özellik |
| --- | --- | --- |
| ApplyBoard | Program keşfi ile başvuru sürecini tek ürün deneyiminde birleştirmesi; güçlü sayısal güven bandı; farklı kullanıcı türleri için net giriş noktaları | Macaristan'a özel program bulucu, uygunluk akışı, yapılandırılmış profil ve başvuru adımları. Yalnızca doğrulanmış Hun Education metrikleri kullanılacak |
| IDP | Kurs/üniversite araması, danışmanlık hizmetini görünür kılması, ülkeye göre yerelleştirilmiş içerik ve ofis güveni | Türk öğrenciye özel arama filtreleri, Ankara/Budapeşte ve diğer aktif temsil noktalarının doğrulanmış bilgileri, yerel başvuru rehberi |
| StudyIn | Ülke landing page'inde program araması, üniversite keşfi, danışmanlık CTA'sı, güncel kariyer/vize rehberleri ve SSS'yi aynı karar akışında birleştirmesi | “Macaristan'da Eğitim” pillar sayfasında arama + rehber + danışmanlık + güncel içerik birleşimi |
| Go Overseas | Kullanıcıların programları hedef, bütçe ve süreyle karşılaştırabilmesi; gerçek incelemeleri program keşfine bağlaması | Üniversite/program karşılaştırma, doğrulanmış öğrenci deneyimleri ve bütçe filtreleri |
| IES Abroad | Ücretin neleri kapsadığını açıkça anlatması; başvuru öncesi, sonrası ve ülkedeki destek sorumlularını ayrıştırması; araştırmaya dayalı sonuçlar | Hun Education hizmet kapsamı matrisi, “bu aşamada kim destek olur?” anlatımı ve izinli mezun sonuç araştırması |
| WorldStrides / ISEP | Gelişmiş program filtreleri ve “nereden başlayacağını bilmiyorsan öneri al” kaçış yolu | Sonuç bulamayan veya kararsız kullanıcı için danışman destekli program eşleştirme |
| educations.com / Studyportals tipi platformlar | Büyük program veri tabanlarını temiz taksonomi, karşılaştırılabilir kartlar ve indekslenebilir destinasyon/alan sayfalarıyla sunmaları | İnce ama kaliteli programatik SEO: yalnızca özgün veri ve gerçek arama talebi olan kombinasyonların indekslenmesi |

#### Benchmarklardan alınmayacak uygulamalar

- Hun Education'ın sahip olmadığı büyük öğrenci/üniversite sayılarını taklit etmek
- Kullanıcıyı hesap açmaya zorlayarak bilgiye erişimi engellemek
- Çok sayıda zayıf şehir × bölüm × seviye sayfasını otomatik üretmek
- Sponsorlu programları organik öneri gibi göstermek
- Kullanıcı yorumlarını doğrulama olmadan yayınlamak
- “%95 kabul”, “kesin vize” veya benzeri kanıtlanamayan başarı iddiaları

#### Stratejik sonuç

Hun Education'ın rakipsizleşme formülü, rakiplerden daha fazla genel blog yazısı üretmek değildir. Savunulabilir üstünlük şu dört varlığın birleşiminden gelmelidir:

1. **Macaristan'a özel doğrulanmış veri tabanı:** program, ücret, tarih, şart, şehir ve üniversite ilişkileri.
2. **Birinci el deneyim:** gerçek danışman, öğrenci, ofis, oryantasyon, başvuru ve yerleşim bilgileri.
3. **Karar araçları:** filtreleme, karşılaştırma, maliyet hesaplama ve uygunluk ön değerlendirmesi.
4. **Yayın disiplini:** kaynak, editör, uzman kontrolü, son güncelleme ve değişiklik kaydı.

---

## 3. Ürün hedefleri ve başarı ölçütleri

### 3.1 Birincil hedefler

1. Nitelikli danışmanlık talebi sayısını artırmak.
2. Kullanıcının uygun üniversite/program bulma süresini kısaltmak.
3. Öğrenci ve özellikle ebeveyn tarafındaki güven kaygılarını gidermek.
4. Organik arama görünürlüğünü korumak ve yüksek niyetli sorgularda büyütmek.
5. Türkçe ve İngilizce içerikleri tek bir yönetilebilir sistemde tutmak.
6. Pazarlama ekibine kampanya bazında ölçülebilir landing page'ler üretme olanağı sağlamak.

### 3.2 Ana KPI'lar

- Başarılı form gönderimi sayısı ve oranı
- Nitelikli lead oranı
- WhatsApp görüşmesi başlatma oranı
- Telefon ve e-posta tıklamaları
- Program/üniversite sayfasından CTA tıklama oranı
- Form başlatma → form tamamlama oranı
- Organik trafik ve organik lead sayısı
- Marka dışı yüksek niyetli anahtar kelimelerde görünürlük
- Program araması kullanım ve sonuç tıklama oranı
- Mobil dönüşüm oranı
- Core Web Vitals geçiş oranı

İlk 30 gün mevcut performans için baz dönem kabul edilsin. Sonraki 90 günde nitelikli lead sayısında en az %30 artış hedeflensin; bu bir tasarım garantisi değil, optimizasyon hedefidir. Trafik kaynağı, reklam bütçesi ve satış takibi ayrıca değerlendirilmelidir.

---

## 4. Hedef kullanıcılar

### Persona A — Lise öğrencisi

- 16–20 yaş
- Bölüm ve ülke seçenekleri konusunda kararsız
- YKS'den bağımsız seçenek, İngilizce eğitim, Avrupa deneyimi ve sosyal yaşamla ilgileniyor
- Mobil ve Instagram ağırlıklı araştırma yapıyor
- Hızlı, görsel, kolay karşılaştırılabilir bilgi istiyor

### Persona B — Ebeveyn / karar verici

- Güvenlik, toplam maliyet, diploma tanınırlığı, konaklama, vize ve danışmanlık şirketinin güvenilirliğiyle ilgileniyor
- Net süreç, gerçek danışmanlar, ofis adresi, öğrenci hikâyeleri ve şeffaf fiyat bilgisi arıyor
- Telefonda veya WhatsApp üzerinden bir uzmanla görüşmek istiyor

### Persona C — Üniversite mezunu / yüksek lisans adayı

- 21–30 yaş
- Program uyumu, akademik şartlar, İngilizce seviyesi, kariyer ve çalışma olanaklarına odaklanıyor
- Filtrelenebilir program kataloğu ve güncel başvuru bilgisi bekliyor

### Persona D — Uluslararası aday

- İngilizce siteyi kullanıyor
- Uyruk bazlı başvuru yetkisi ve vize sürecinin değişebileceğini bilmek istiyor
- İngilizce içerikte Türkiye'ye özel ifadeler görmemeli

---

## 5. Bilgi mimarisi ve menü

### Ana navigasyon

1. **Macaristan'da Eğitim**
   - Neden Macaristan?
   - Eğitim Sistemi
   - Başvuru ve Kabul Şartları
   - Eğitim ve Yaşam Maliyetleri
   - Vize ve Oturum Süreci
   - Konaklama ve Öğrenci Yaşamı
2. **Üniversiteler**
3. **Programlar**
   - Hazırlık
   - Lisans
   - Yüksek Lisans
   - Tıp ve Sağlık
   - Mühendislik ve Teknoloji
   - İşletme ve Ekonomi
   - Psikoloji ve Sosyal Bilimler
   - Pilotaj
4. **Hizmetlerimiz**
5. **Öğrenci Hikâyeleri**
6. **Rehber**
7. **Hakkımızda**
8. Sağ üst birincil CTA: **Ücretsiz Ön Görüşme**

Mobil menüde telefon ve WhatsApp aksiyonları sabit ve görünür olmalı. Masaüstünde dil seçici açıkça **TR / EN** göstermeli; bayrak tek başına kullanılmamalı.

### Footer

- Kısa marka açıklaması
- Hızlı bağlantılar
- Popüler üniversiteler
- Popüler programlar
- Türkiye ve Macaristan iletişim bilgileri
- Çalışma saatleri
- WhatsApp, telefon, e-posta
- Sosyal medya bağlantıları
- KVKK Aydınlatma Metni
- Açık Rıza Metni
- Gizlilik ve Çerez Politikası
- Kullanım Koşulları
- Yasal bilgilendirme: ücretlerin ve kabul koşullarının değişebileceği
- Telif ve şirket unvanı

---

## 6. Ana sayfa gereksinimleri

Ana sayfanın amacı, 60–90 saniye içinde şu beş soruyu yanıtlamaktır: Hun Education ne yapıyor, neden güvenilir, bana uygun seçenek var mı, süreç nasıl işliyor ve şimdi ne yapmalıyım?

### Bölüm 1 — Header

- Sol: logo
- Orta: ana navigasyon
- Sağ: TR/EN, WhatsApp ikonu, “Ücretsiz Ön Görüşme” butonu
- Scroll sonrası kompakt sticky header
- Telefon numarası mobilde tek dokunuşla aranabilir

### Bölüm 2 — Hero

**Eyebrow:** “1999'dan beri Macaristan odaklı eğitim danışmanlığı”  
**H1 önerisi:** “Macaristan'daki doğru üniversiteyi birlikte bulalım”  
**Alt metin:** “Program seçiminden başvuru ve vizeye, konaklamadan şehir oryantasyonuna kadar tüm süreçte Türkiye ve Macaristan'daki danışmanlarımızla yanınızdayız.”  
**Birincil CTA:** “Ücretsiz Ön Görüşme Al”  
**İkincil CTA:** “Programları İncele”  
**Mikro güven metni:** “Talebinize 1 iş günü içinde dönüş.” — mevcut operasyonla doğrulanmalı.

Hero görseli gerçek bir Hun Education öğrencisini Budapeşte bağlamında göstermeli. Yapay, aşırı pozlu stok “mezuniyet kepi” görselleri kullanılmamalı. Öğrencinin yüzü CTA'nın ters tarafına bakmalı; metin okunabilirliğini bozacak kalabalık arka plan olmamalı.

### Bölüm 3 — Güven bandı

Yalnızca doğrulanmış verilerle 3–4 kısa kanıt:

- 1999'dan beri Macaristan deneyimi
- Budapeşte'de merkez ofis
- Türkiye ve Macaristan'da danışman ağı
- [Doğrulanmış öğrenci sayısı]
- [Doğrulanmış üniversite/kurum iş birlikleri]

Partner logoları yalnızca kullanım izni ve aktif ilişki varsa gösterilmeli. Logolar “akreditasyon” izlenimi yaratmamalı.

### Bölüm 4 — Program bulucu

Ana sayfada büyük ve karmaşık filtre yerine 3 adımlı hızlı seçim:

1. Eğitim seviyesi
2. İlgi alanı
3. Tercih edilen şehir veya bütçe

CTA: “Bana Uygun Programları Göster”

Sonuçlar program listeleme sayfasına filtre parametreleriyle aktarılmalı. Arama başarısızsa kullanıcı boş sayfada bırakılmamalı; “Danışmana sor” seçeneği sunulmalı.

### Bölüm 5 — Popüler alanlar

6 görsel kart: Tıp, Diş Hekimliği, Mühendislik, İşletme, Psikoloji, Pilotaj. Her kartta başlangıç fiyatı ancak güncel ve doğrulanmışsa gösterilsin; para birimi ve ücret dönemi açık olsun.

### Bölüm 6 — Hun Education ile süreç

Altı adımlı yalın yol haritası:

1. Ücretsiz ön görüşme ve hedef analizi
2. Üniversite ve program eşleştirme
3. Evrakların hazırlanması
4. Başvuru, sınav/mülakat ve kabul takibi
5. Vize, konaklama ve seyahat hazırlığı
6. Macaristan'da karşılama ve oryantasyon

Her adımın hizmet kapsamı müşteri tarafından doğrulanmalı. Süre veya başarı garantisi verilmemeli.

### Bölüm 7 — Neden Hun Education?

- Tek ülkeye odaklanan uzmanlık
- Türkiye'den Macaristan'a devam eden destek
- Gerçek danışmanlara doğrudan erişim
- Güncel program ve maliyet rehberliği
- Başvuru sonrası yerleşim/orientasyon desteği

Bu bölüm genel sıfatlar yerine somut çalışma biçimini anlatmalı.

### Bölüm 8 — Öne çıkan üniversiteler

4–6 kart. Her kartta:

- Üniversite adı ve şehir
- Öne çıkan alanlar
- Eğitim dili
- “Üniversiteyi İncele” CTA
- Logo ve kampüs fotoğrafı için kullanım hakkı kontrolü

“Sıralama” veya “en iyi” iddiası kullanılıyorsa kaynak, yıl ve sıralama kuruluşu gösterilmeli.

### Bölüm 9 — Gerçek öğrenci hikâyeleri

- Video öncelikli
- Ad-soyad gösterimi için açık izin
- Üniversite, bölüm ve mezuniyet yılı
- Sonuç/deneyim, abartısız ve öğrencinin gerçek sözüyle
- Video transkripti ve erişilebilir altyazı
- CTA: “Tüm Öğrenci Hikâyeleri”

### Bölüm 10 — Maliyet görünürlüğü

“Bütçenizi daha baştan planlayın” başlığıyla eğitim, konaklama, ulaşım, sigorta, vize ve yaşam giderlerinin hangi kalemlerden oluştuğunu göster. Kesin toplam yerine güncellenebilir aralıklar kullan. Tüm ücretlerde:

- Para birimi
- Yıllık/dönemlik/aylık ayrımı
- Verinin son güncellenme tarihi
- Kaynak veya “üniversite tarafından değiştirilebilir” notu

CTA: “Eğitim ve Yaşam Maliyetlerini İncele”

### Bölüm 11 — İçerik rehberi

En güncel 3–4 içerik. Kartta kategori, güncelleme tarihi ve okuma süresi. Eski içeriklerin yayın tarihi kadar “son güncelleme” tarihi de görünür olmalı.

### Bölüm 12 — SSS

En fazla 6 soru:

- YKS gerekli mi?
- İngilizce belgesi gerekli mi?
- Başvurular ne zaman açılıyor?
- Toplam maliyet ne kadar?
- Vize sürecinde destek veriliyor mu?
- Diploma Türkiye'de tanınıyor mu?

Yanıtlar koşullu ve güncel kaynaklara bağlı yazılmalı. Özellikle denklik için YÖK'ün güncel kurallarına yönlendirme yapılmalı; “otomatik/doğrudan denklik garantisi” verilmemeli.

### Bölüm 13 — Final CTA

Başlık: “Hangi programın size uygun olduğundan emin değil misiniz?”  
Metin: “Akademik geçmişinizi ve hedeflerinizi birlikte değerlendirelim.”  
CTA: “Ücretsiz Ön Görüşme Al”  
İkincil: “WhatsApp'tan Sor”

---

## 7. Kritik sayfa şablonları

### 7.1 Üniversiteler listeleme sayfası

Filtreler:

- Şehir
- Üniversite türü
- Eğitim seviyesi
- Alan
- Eğitim dili
- Ücret aralığı

Kartlar karşılaştırılabilir olmalı. En fazla 3 üniversiteyi karşılaştırma özelliği ikinci fazda eklenebilir. Sıralama varsayılan olarak “öne çıkan” değil; alfabetik veya kullanıcı filtresine göre olmalı. Sponsorlu sıralama varsa açıkça etiketlenmeli.

### 7.2 Üniversite detay şablonu

1. Üniversite adı, şehir, kampüs görseli
2. Kısa doğrulanmış özet
3. Hızlı bilgiler: kuruluş yılı, şehir, dil, tür, yaklaşık öğrenci sayısı
4. Neden bu üniversite?
5. Program listesi ve filtre
6. Ücretler ve başvuru dönemleri
7. Kabul şartları
8. Kampüs ve şehir yaşamı
9. Konaklama seçenekleri
10. Galeri/video
11. İlgili öğrenci hikâyeleri
12. SSS
13. Sticky başvuru CTA'sı

### 7.3 Programlar listeleme sayfası

Arama ve filtreler:

- Anahtar kelime
- Eğitim seviyesi
- Alan/kategori
- Üniversite
- Şehir
- Dil
- Başlangıç dönemi
- Süre
- Yıllık ücret aralığı

Seçili filtreler görünür etiketler halinde gösterilmeli; “Tümünü temizle” bulunmalı. Mobilde filtreler bottom sheet/drawer olarak açılmalı. Sonuç sayısı anlık görünmeli. URL parametreleri paylaşılabilir ve geri tuşuyla bozulmamalı.

### 7.4 Program detay şablonu

Sayfanın üst kısmında standart özet kartı:

- Program adı
- Üniversite
- Şehir
- Derece seviyesi
- Eğitim dili
- Süre
- Başlangıç dönemi
- Başvuru son tarihi
- Öğrenim ücreti ve ödeme dönemi
- Son güncelleme tarihi

Devamında:

1. Program hakkında
2. Kimler için uygun?
3. Kabul şartları
4. Gerekli belgeler
5. Sınav/mülakat bilgisi
6. Ders içeriği / müfredat
7. Kariyer olanakları
8. Eğitim ve yaşam maliyeti
9. Başvuru süreci
10. İlgili programlar
11. SSS
12. “Uygunluğumu Değerlendirin” formu

Ücret veya tarih bilinmiyorsa alan saklanmasın; “Güncel bilgi için danışmana sorun” denilsin. Eski veri sessizce gösterilmemeli.

### 7.5 Hizmetlerimiz sayfası

Hizmetleri gerçek kapsamla eşleştir:

- Akademik hedef analizi
- Üniversite ve program seçimi
- Başvuru dosyası hazırlığı
- Sınav/mülakat hazırlığı
- Kabul ve kayıt takibi
- Vize süreci rehberliği
- Konaklama desteği
- Karşılama ve şehir oryantasyonu
- Eğitim süresince danışmanlık

Her hizmet için “neleri kapsar / neleri kapsamaz / ne zaman başlar” açıklaması olmalı. Danışmanlık ücreti ve üniversiteye ödenen ücretler birbirinden ayrıştırılmalı.

### 7.6 Hakkımızda sayfası

- Markanın kuruluş hikâyesi ve 1999'dan bugüne zaman çizelgesi
- Macaristan odaklı uzmanlık
- Şirketin hukuki unvanı ve ofisleri
- Doğrulanmış sayılar
- Üniversite ilişkilerinin doğru tanımı
- Yönetim ve akademik danışman ekibi
- Çalışma ilkeleri
- Gerçek ofis fotoğrafları

Danışman kartlarında fotoğraf, uzmanlık alanı, şehir, konuştuğu diller ve iletişim yönlendirmesi bulunmalı. Kişisel telefon/e-posta paylaşımı KVKK ve operasyon politikasıyla uyumlu olmalı.

### 7.7 Öğrenci hikâyeleri sayfası

- Video / yazılı hikâye filtreleri
- Üniversite, bölüm ve şehir filtresi
- Her hikâyenin ayrı, indekslenebilir detay sayfası
- İzin kaydı ve içerik yayın onayı
- Sahte veya anonimleştirilmiş referans kullanılmamalı; yalnızca açıkça izin verilmiş gerçek deneyimler yayınlanmalı

### 7.8 İletişim / başvuru sayfası

Üstte kısa form; altta iletişim kanalları ve ofisler. Uzun danışman listesi ayrı “Ekibimiz” sayfasına taşınmalı.

Form alanları:

- Ad soyad
- Telefon ve ülke kodu
- E-posta
- İlgilenilen eğitim seviyesi
- İlgilenilen alan/program
- Hedef başlangıç dönemi
- Mesaj (opsiyonel)
- Tercih edilen iletişim kanalı
- KVKK aydınlatma bağlantısı ve gerekli açık rıza

Form sonrası:

- Başarı mesajı ve beklenen dönüş süresi
- WhatsApp ile görüşmeyi sürdürme butonu
- GA4 `generate_lead` olayı
- CRM'e kaynak, kampanya, sayfa ve seçilen program bilgilerinin aktarılması
- Kullanıcıya otomatik teyit e-postası

---

## 8. Dönüşüm sistemi

### Birincil CTA

Tüm sitede tek ifade: **Ücretsiz Ön Görüşme Al**

### Bağlama özel ikincil CTA'lar

- Program detayında: **Uygunluğumu Değerlendirin**
- Üniversite detayında: **Bu Üniversite Hakkında Bilgi Al**
- Maliyet sayfasında: **Bana Özel Bütçe Planı İstiyorum**
- Mobilde: **WhatsApp'tan Sor**

### Form stratejisi

- İlk temas formu kısa olmalı; detaylı profil soruları ikinci adımda veya danışman görüşmesinde alınmalı.
- Reklam landing page'lerinde 4–6 alanı geçmeyen tek amaçlı form kullanılmalı.
- Zorunlu alanlar açıkça işaretlenmeli.
- Form hataları alanın yanında ve anlaşılır Türkçeyle gösterilmeli.
- Telefon alanında ülke kodu ve format doğrulaması olmalı.
- Spam koruması kullanıcıyı yormayan bir yöntemle yapılmalı.
- Başarılı gönderimden sonra aynı lead'in tekrar tekrar gönderilmesi engellenmeli.

### WhatsApp davranışı

Sayfa bağlamına göre önceden doldurulmuş mesaj:

“Merhaba, Hun Education web sitesinde [Program/Üniversite Adı] sayfasını inceliyorum. Başvuru koşulları ve güncel ücret hakkında bilgi almak istiyorum.”

Tıklama `whatsapp_click` olarak; kaynak sayfa ve içerik adıyla ölçülmeli. WhatsApp balonu içerik veya form butonlarını kapatmamalı.

### Kampanya landing page şablonları

- Macaristan'da Tıp
- Macaristan'da Diş Hekimliği
- Macaristan'da Pilotaj
- Macaristan'da Psikoloji
- Macaristan'da Mühendislik
- Macaristan'da Yüksek Lisans
- İngilizce / Bölüm Hazırlık

Her sayfa reklam mesajıyla birebir eşleşen H1, faydalar, güncel program seçenekleri, güven kanıtları, SSS ve tek form içermeli. Ana menü kampanya sayfalarında sadeleştirilebilir fakat yasal/footer bağlantıları kaldırılmamalı.

---

## 9. Görsel tasarım sistemi

### Tasarım yönü

Marka hissi: **köklü, güvenilir, Avrupa merkezli, sıcak ve genç**. Banka kadar soğuk veya öğrenci kulübü kadar amatör görünmemeli.

- Mevcut Hun Education logosunun lacivert/mavi karakteri korunabilir.
- Ana renk: logodan türetilen derin lacivert **[nihai hex logodan alınacak]**
- İkincil renk: daha açık kobalt/mavi
- Aksiyon rengi: lacivertle yüksek kontrast oluşturan sıcak kırmızı veya mercan **[erişilebilirlik testi sonrası]**
- Zeminler: kırık beyaz, açık gri-mavi
- Başarı rengi: yeşil yalnızca durum/WhatsApp için
- Renkler Macar bayrağını dekoratif biçimde tekrar etmek için kullanılmamalı

### Tipografi

- Başlık: modern ama güven veren sans serif; örn. Manrope veya Plus Jakarta Sans
- Gövde: Inter
- Türkçe karakterler eksiksiz desteklenmeli
- Gövde metni mobilde en az 16 px
- Uzun satırlar 65–75 karakterle sınırlandırılmalı

### Görsel dil

Öncelik sırası:

1. Gerçek öğrenciler ve danışmanlar
2. Gerçek ofis, karşılama ve oryantasyon fotoğrafları
3. Üniversite kampüsleri ve şehir yaşamı
4. Gerektiğinde lisanslı, doğal stok fotoğraf

Yapay görseller gerçek öğrenci başarısı veya ofis kanıtı gibi sunulmamalı. Kampüs ve üniversite logolarının kullanım hakları kontrol edilmeli. Her görselin anlamlı alt metni olmalı; dekoratif görseller boş alt ile işaretlenmeli.

### Bileşenler

- Buton: primary, secondary, text, icon
- Program ve üniversite kartları
- Güven metrikleri
- Danışman kartları
- Video testimonial
- Süreç adımları
- Accordion SSS
- Filtre drawer
- Form alanları ve durumları
- Sticky mobil CTA bar
- Breadcrumb
- Güncelleme tarihi etiketi
- Bilgilendirme/uyarı kutusu

### Hareket ve animasyon

- 150–250 ms mikro geçişler
- Scroll ile ağır parallax veya gereksiz giriş animasyonu yok
- `prefers-reduced-motion` desteği
- İçerik animasyon uğruna geciktirilmemeli

---

## 10. İçerik ve editoryal standartlar

### Ton

- Samimi ama profesyonel
- Açıklayıcı ama satış baskısı yaratmayan
- Öğrenciye doğrudan “siz” diye hitap eden
- Ebeveyn kaygılarını küçümsemeyen
- Kısa cümleli, aktif anlatım

### Yasaklı veya dikkat gerektiren dil

- “Kesin kabul”
- “Vize garantisi”
- “Kesin denklik”
- “Sınavsız” — üniversitenin kendi sınav/mülakatı varsa kullanılmamalı
- “Dünyanın en iyi” — kaynak yoksa kullanılmamalı
- “En ucuz” — karşılaştırmalı kanıt yoksa kullanılmamalı
- “Tüm üniversiteler” veya “tüm programlar” — veri bunu kapsamıyorsa kullanılmamalı

### Veri yönetişimi

Program ve üniversite içeriklerinde şu CMS alanları zorunlu olsun:

- Kaynak URL
- Veriyi doğrulayan kişi
- Son doğrulama tarihi
- Bir sonraki kontrol tarihi
- İçerik sahibi
- Yayın durumu

Ücret, başvuru tarihi ve kabul şartı içeren sayfalar en az dönemsel olarak gözden geçirilmeli. Süresi geçen veri CMS'de uyarı üretmeli.

---

## 11. Olağanüstü SEO ve GEO büyüme sistemi

### 11.1 Temel prensip ve gerçekçi hedef

Hedef, “Macaristan'da üniversite” konu alanında Türkiye'nin en güvenilir ve en kapsamlı organik kaynağı olmak; Google, Bing/Copilot ve ChatGPT Search gibi arama/yanıt deneyimlerinde düzenli kaynak gösterilmek ve bu görünürlüğü nitelikli lead'e çevirmektir.

Hiçbir kişi veya ajans birincilik ya da AI yanıtında alıntılanma garantisi veremez. Google'ın güncel yaklaşımında GEO, temel SEO'dan ayrı bir hile seti değildir. Başarı; indekslenebilir teknik yapı, özgün ve birinci el içerik, açık kaynaklandırma, güçlü marka sinyalleri ve iyi kullanıcı deneyiminin bileşiminden gelir. `llms.txt`, yapay “chunking”, anlamsız şema yığını veya seri AI içerik üretimi ana strateji yapılmamalıdır.

### 11.2 Arama talebi ve varlık haritası

İçerik takvimi hazırlanmadan önce en az son 16 aylık Search Console verisi, GA4 landing page verisi, reklam arama terimleri, CRM'deki gerçek aday soruları ve danışman görüşme notları analiz edilmelidir.

Her sorgu şu eksenlerde etiketlenmeli:

- **Niyet:** keşif, karşılaştırma, uygunluk, maliyet, başvuru, marka, işlem
- **Kullanıcı:** öğrenci, ebeveyn, lisans adayı, yüksek lisans adayı, uluslararası aday
- **Varlık:** ülke, şehir, üniversite, program, derece, sınav, ücret, vize, denklik
- **Funnel:** farkındalık, değerlendirme, karar, başvuru
- **Tazelik:** sabit, yıllık, dönemlik, sık değişen
- **Risk:** hukuki/mevzuat, finansal, akademik, düşük risk

Anahtar kelime listesi değil, bir **Macaristan Eğitim Knowledge Graph** oluşturulmalıdır:

- Macaristan → şehirler → üniversiteler → programlar
- Program → seviye → dil → süre → ücret → başlangıç dönemi → şartlar
- Üniversite → kampüs → şehir → programlar → öğrenci hikâyeleri
- Başvuru → belge → sınav/mülakat → kabul → vize → konaklama → oryantasyon

Bu varlıklar CMS'de tekil kayıt olarak yönetilmeli ve tüm sayfalarda aynı kaynaktan beslenmelidir. Böylece bir ücret veya tarih değiştiğinde çelişkili eski bilgiler kalmaz.

### 11.3 Topic authority mimarisi

#### Pillar 1 — Macaristan'da üniversite ana rehberi

Hedef sorgular: Macaristan'da üniversite, Macaristan üniversiteleri, Macaristan'da okumak.  
Alt içerikler: eğitim sistemi, avantaj/dezavantaj, başvuru takvimi, gerekli belgeler, dil şartı, YKS, maliyet, vize, konaklama, şehirler, çalışma hakları, mezuniyet ve denklik.

#### Pillar 2 — Üniversite veri tabanı

Her üniversite sayfası özgün veri, şehir bağlamı, güncel programlar, ücretler, kabul şartları, gerçek görseller, kaynaklar ve ilgili öğrenci deneyimleri içermelidir. Üniversite adı varyasyonları tek canonical URL'de birleştirilmelidir.

#### Pillar 3 — Program ve bölüm kümeleri

Öncelikli kümeler: tıp, diş hekimliği, eczacılık, veterinerlik, pilotaj, psikoloji, mühendislik, bilgisayar bilimleri, işletme, mimarlık, yüksek lisans ve hazırlık. Her alan sayfası genel bilgi + üniversite karşılaştırması + güncel program listesi + kabul şartları + maliyet + kariyer + SSS sunmalıdır.

#### Pillar 4 — Şehir ve yaşam kümeleri

Budapeşte, Pécs, Debrecen, Szeged, Dunaújváros, Nyíregyháza ve gerçekten program sunulan diğer şehirler. Her sayfada kira/yurt, ulaşım, güvenlik, öğrenci yaşamı, ilgili üniversiteler ve gerçek Hun Education saha bilgisi olmalıdır.

#### Pillar 5 — Karar ve işlem kümeleri

- 2026/27 başvuru takvimi
- YKS ve üniversiteye özel giriş sınavları
- İngilizce yeterlilik ve hazırlık
- YÖK denklik süreci
- D tipi öğrenci vizesi ve ikamet
- Gerekli belgeler ve örnek kontrol listesi
- Üniversite/şehir/program karşılaştırmaları
- Toplam maliyet ve bütçe planı

### 11.4 İçerik formatı ve “citation-ready” GEO standardı

Her yüksek değerli rehber aşağıdaki düzeni izlemelidir:

1. Arama niyetine 40–70 kelimelik doğrudan yanıt
2. “Kısa cevap” veya “En önemli bilgiler” kutusu
3. İçindekiler ve anlamlı anchor bağlantıları
4. Koşulları/ücretleri/tarihleri net tablo
5. Adım adım süreç
6. Üniversite veya programa göre istisnalar
7. Hun Education'ın birinci el gözlemi veya özgün verisi
8. Birincil kaynak bağlantıları
9. Uzman tarafından cevaplanan gerçek sorular
10. Yazar, uzman kontrolü, yayın ve son güncelleme tarihi
11. Değişiklik günlüğü
12. İçeriğin niyetine uygun CTA

AI yanıtlarında alıntılanabilirlik için cümleler kesin ama koşulları saklamayan biçimde yazılmalıdır. Örnek: “Macaristan'daki üniversitelerin kabul şartları programa göre değişir; çoğu lisans başvurusu diploma ve transkript isterken tıp, mühendislik veya sanat programları ek sınav, mülakat ya da portfolyo isteyebilir.”

Kritik bilgilerde kaynak önceliği:

1. İlgili üniversitenin resmî sayfası
2. Macaristan ve Türkiye'deki resmî kurumlar
3. YÖK ve resmî mevzuat
4. Hun Education'ın tarihli ve yöntemi açıklanmış birinci el verisi
5. Saygın ikincil kaynak

Kaynaklar dipte belirsiz bir liste olarak bırakılmamalı; ilgili iddianın yanında verilmelidir. Kaynak URL, erişim tarihi ve verinin geçerli olduğu dönem CMS'de tutulmalıdır.

### 11.5 Özgün veri ve dijital PR hendeği

Rakiplerin kolayca kopyalayamayacağı içerik varlıkları üretilmelidir:

- Yıllık “Türk Öğrenciler İçin Macaristan Üniversite Ücretleri Raporu”
- Dönemsel “Başvuru Takvimi ve Kontenjan Durumu” merkezi
- Şehir bazlı gerçek öğrenci bütçesi araştırması
- Anonimleştirilmiş başvuru/kabul trendleri — yeterli örneklem ve izin varsa
- Öğrenci ve mezun sonuç araştırması — yöntem ve örneklem açıkça belirtilerek
- Üniversite yetkilileri ve akademisyenlerle özgün röportajlar
- Danışmanların hazırladığı sınav/mülakat rehberleri
- İndirilebilir ama HTML karşılığı bulunan kontrol listeleri
- Basın ve eğitim yayınlarına sunulabilecek veri görselleri

Bu çalışmalar basın, üniversite, öğrenci kulübü, mezun ve sektörel kuruluşlara gerçek editoryal değerle duyurulmalıdır. Satın alınmış, alakasız veya yapay backlink ağı kullanılmamalıdır.

### 11.6 Programatik SEO — kalite kontrollü

Program, üniversite, şehir ve alan veri modeli indekslenebilir sayfalar üretebilir; ancak her filtre kombinasyonu indekslenmemelidir.

**İndekslenebilir olabilecek sayfalar:**

- Arama talebi olan ve en az 3 ilgili program içeren kategori sayfaları
- Özgün giriş, karşılaştırma tablosu, uzman açıklaması ve SSS içeren sayfalar
- Güncel, tam ve doğrulanmış veri bulunan üniversite/program sayfaları

**Noindex/canonical uygulanacak sayfalar:**

- Sıralama ve görünüm varyasyonları
- UTM ve takip parametreleri
- İçeriksiz veya tek zayıf sonuca sahip filtre kombinasyonları
- Aynı sonuç setini üreten eş anlamlı URL'ler
- Site içi arama sonuçları

Otomatik sayfa üretimi, Google'ın ölçekli içerik kötüye kullanımı politikasını ihlal edecek “keyword doorway” sistemine dönüşmemelidir. AI yalnız araştırma ve taslak desteği verebilir; her sayfa editoryal kalite ve veri doğrulama kapısından geçmelidir.

### 11.7 Teknik SEO

- Mevcut tüm indekslenmiş URL, backlink, trafik ve dönüşüm envanteri çıkarılmalı.
- Eski → yeni URL için birebir 301 yönlendirme haritası hazırlanmalı; yönlendirme zinciri olmamalı.
- Trafik ve backlink alan URL gereksiz yere değiştirilmemeli.
- Tercih edilen yapı değerlendirmesi: `huneducation.com/tr/` ve `/en/` tek domain altında uzun vadede otoriteyi birleştirebilir; subdomain'den klasöre geçiş yalnız ölçülmüş risk, eksiksiz redirect/hreflang ve geri dönüş planıyla yapılmalı. Sırf estetik için migrasyon yapılmamalı.
- Türkçe ve İngilizce sayfalar karşılıklı `hreflang` ile eşleştirilmeli; `x-default` tanımlanmalı.
- Otomatik dil yönlendirmesi botları veya kullanıcıyı içerikten mahrum bırakmamalı.
- Her sayfada benzersiz title, meta description, canonical, Open Graph ve Twitter Card bulunmalı.
- XML sitemap içerik tiplerine ve dillere göre ayrılmalı; yalnız canonical ve indekslenebilir 200 URL'ler yer almalı.
- Filtre, arama, parametre ve pagination kuralları dokümante edilmeli.
- Breadcrumb, crawlable `<a href>` bağlantıları ve anlamlı slug yapısı kullanılmalı.
- Sunucu tarafında ana içerik hazır gelmeli; kritik içerik yalnız kullanıcı etkileşimi sonrası JavaScript ile yüklenmemeli.
- `robots.txt`, CDN/WAF ve güvenlik eklentileri Googlebot, Bingbot ve izin verilen AI arama botlarını yanlışlıkla engellememeli.
- Herkese açık sayfalarda gereksiz session cookie ve `no-store` kaldırılmalı; doğru cache header kullanılmalı.
- Silinen içerik 404/410 vermeli; alakasız biçimde ana sayfaya yönlendirilmemeli.
- Log file analiziyle tarama davranışı ve israf edilen URL'ler izlenmeli.

### 11.8 Yapılandırılmış veri

- `Organization` ve uygun özelliklerle eğitim danışmanlığı markası
- Doğrulanmış ofisler için uygun yerel işletme yapısı; aynı telefon/adres bilgisiyle
- `WebSite` ve gerçek site araması varsa `SearchAction`
- `BreadcrumbList`
- `Article` / `BlogPosting`
- `Person` — danışman/yazar profilleri ve gerçek uzmanlıkla
- `VideoObject` — öğrenci ve uzman videoları
- `FAQPage` — yalnız görünür gerçek SSS ve arama motorunun güncel uygunluk kurallarına göre
- `Course` — yalnız program sayfasındaki görünür ve güncel alanlar doğru eşleşiyorsa

Şema zengin sonuç garantisi değildir, özel bir GEO şeması yoktur ve görünmeyen iddialar JSON-LD içine eklenmemelidir. Google'ın desteklemediği şemalara kaynak ayrılmadan önce iş değeri değerlendirilmelidir.

### 11.9 E-E-A-T ve güven sistemi

- Her rehberde gerçek yazar ve gerekiyorsa “uzman kontrolü” bilgisi
- Yazar sayfasında eğitim, deneyim, uzmanlık, şehir ve yayınlar
- Editoryal politika, düzeltme politikası ve kaynaklandırma standardı
- Şirket unvanı, açık adres, telefon, e-posta ve ekip tutarlılığı
- “Hakkımızda” sayfasında tarihçe ve doğrulanabilir kanıtlar
- Öğrenci yorumlarında izin, üniversite/bölüm/yıl ve gerçek bağlam
- Ücret/şart değişikliklerinde görünür güncelleme tarihi
- Finansal, yasal veya denklik konularında sorumlu uyarı ve resmî kaynağa bağlantı
- İçerik üretiminde AI kullanılıyorsa son doğrulamayı yapan insan ve editoryal sorumluluk açık olmalı

### 11.10 AI arama botları ve dağıtım

- ChatGPT Search görünürlüğü isteniyorsa `OAI-SearchBot` robots.txt ve CDN düzeyinde engellenmemeli.
- OpenAI'nin yayınladığı bot/IP bilgileri zaman zaman kontrol edilmeli; kullanıcı aracısı taklitlerine karşı yalnız isim bazlı gevşek güvenlik uygulanmamalı.
- Bing için sitemap ve IndexNow kurulmalı; yeni/güncellenen/silinen URL'ler hızlı bildirilmelidir.
- Google Search Console ve Bing Webmaster Tools doğrulanmalıdır.
- `llms.txt` diğer sistemler için deneysel olarak eklenebilir; fakat Google sıralaması veya görünürlüğü için gerekli/etkili kabul edilmemeli ve sitemap'ın alternatifi yapılmamalıdır.
- ChatGPT referalleri `utm_source=chatgpt.com` ve kaynak/landing page bazında GA4'te raporlanmalıdır.

### 11.11 İç link ve navigasyon sistemi

Her içerik şu dört yönde bağlanmalıdır:

- Üst konu/pillar
- İlgili üniversite ve programlar
- Sürecin bir önceki ve sonraki adımı
- Dönüşüm CTA'sı

Üniversite sayfası ilgili programlara; program sayfası üniversite, şehir, maliyet ve kabul rehberine; şehir sayfası üniversitelere; öğrenci hikâyesi ilgili program ve üniversiteye bağlanmalıdır. “Benzer yazılar” rastgele değil varlık ilişkilerine göre üretilmelidir.

### 11.12 SERP ve dönüşüm optimizasyonu

- Title'lar sorgu + somut fayda + güncellik sinyalini doğal biçimde vermeli.
- Meta description her sayfa için gerçek, özgün bir teklif olmalı; otomatik şablonlar kalite kontrolünden geçmeli.
- H1, title ve içerik niyeti aynı olmalı.
- Featured snippet/AI alıntısı için tanımlar, tablolar ve adımlar açık olmalı; sırf snippet için gereksiz tekrar yapılmamalı.
- Görsel arama için özgün fotoğraf, açıklayıcı dosya adı, alt metin, caption ve image sitemap kullanılmalı.
- Video sayfalarında transkript, bölüm işaretleri ve ilgili metin içeriği bulunmalı.
- Organik landing page'lerin her biri görünür, bağlama uygun danışmanlık CTA'sına sahip olmalı.

### 11.13 SEO/GEO yayın operasyonu

Her içerik şu iş akışından geçmelidir:

1. Search intent ve SERP/rakip analizi
2. Birincil kaynak ve özgün veri toplama
3. Uzman röportajı veya danışman girdisi
4. Editoryal brief
5. Taslak
6. Akademik/hukuki doğruluk kontrolü
7. SEO, iç link, şema ve dönüşüm kontrolü
8. Yayın
9. Search Console/Bing/AI görünürlük izleme
10. 30/60/90 günlük iyileştirme

Tazelik SLA'sı:

- Ücret, deadline ve vize: değişiklik olduğunda; en az aylık kontrol
- Program/kabul şartları: dönemlik kontrol
- Üniversite/şehir rehberleri: en az 6 ayda bir
- Evergreen rehberler: en az yılda bir ve mevzuat değişiminde hemen

### 11.14 Ölçüm panosu

SEO:

- İndekslenebilir/indekslenen URL oranı
- Non-brand tıklama ve gösterim
- Sorgu kümesine göre ilk 3/10 görünürlük
- Organik landing page dönüşüm ve nitelikli lead oranı
- Backlink veren ilgili domain ve editoryal mention sayısı
- İçerik tazelik uyumu
- Crawl hatası, canonical ve hreflang sorunları

GEO:

- Google Search Console Generative AI performans raporu mevcut hesapta kullanıma açıldığında görünüm/tıklama ve cited URL'ler
- Bing Webmaster Tools AI Performance: toplam citation, cited pages ve grounding query kümeleri
- ChatGPT referral sessions, landing pages ve lead'ler
- Tanımlı 50–100 gerçek kullanıcı sorusundan oluşan sabit test setinde aylık marka/kaynak görünürlüğü
- AI yanıtlarındaki yanlış/eskimiş atıfların kayıt ve düzeltme süreci

Manuel AI testi kişiselleştirme ve model değişkenliği nedeniyle “sıralama” gibi raporlanmamalı; trend ve içerik boşluğu sinyali olarak kullanılmalıdır.

### 11.15 İlk 12 aylık organik büyüme yol haritası

**0–30 gün:** teknik/URL envanteri, veri modeli, keyword-intent map, rakip gap analizi, kritik iddia düzeltmeleri, ölçüm kurulumu.  
**31–90 gün:** ana pillar, üniversite ve program şablonları, en yüksek niyetli 10 sayfa, redirect/hreflang, form ve CTA sistemi.  
**3–6 ay:** tüm öncelikli üniversite/alan/şehir kümeleri, gerçek video ve danışman içerikleri, maliyet hesaplayıcı, ilk özgün veri raporu.  
**6–9 ay:** karşılaştırma aracı, dijital PR, üniversite/mezun röportajları, içerik refresh sistemi, İngilizce fırsat kümeleri.  
**9–12 ay:** veri bazlı genişleme, dönüşüm A/B testleri, citation gap iyileştirmeleri, zayıf içerik konsolidasyonu ve ikinci yıllık araştırma planı.

---

## 12. Teknik gereksinimler

### CMS ve içerik modeli

Dinamik içerik tipleri:

- Üniversite
- Program
- Şehir
- Danışman
- Öğrenci hikâyesi
- Rehber yazısı
- SSS
- Kampanya landing page

İlişkiler:

- Üniversite ↔ programlar
- Üniversite ↔ şehir
- Program ↔ kategori/seviye
- Öğrenci hikâyesi ↔ üniversite/program
- Danışman ↔ şehir/uzmanlık

Program verisi sayfa metninin içine manuel gömülmemeli; ücret, süre, dil ve dönem gibi alanlar yapılandırılmış olmalı.

### WordPress/Elementor uygulanırsa

- Hello Elementor ve Elementor Pro korunabilir; yalnızca gerçekten gereken eklentiler tutulmalı.
- Jet eklenti paketlerinin her biri için gereklilik denetimi yapılmalı; işlevi olmayan eklenti kaldırılmalı.
- Header, footer, program, üniversite, danışman ve blog şablonları Theme Builder ile global kurulmalı.
- Renk, tipografi, spacing ve butonlar global token olarak tanımlanmalı.
- Child theme/custom code değişiklikleri belgelenmeli.
- Üretim sitesinde doğrudan çalışma yapılmamalı; staging ortamı kullanılmalı.
- Güncelleme öncesi tam yedek ve geri dönüş planı oluşturulmalı.

### Performans

- LCP ≤ 2.5 sn
- INP ≤ 200 ms
- CLS ≤ 0.1
- Mobil Lighthouse performansı hedefi ≥ 85; erişilebilirlik ve SEO ≥ 95
- Above-the-fold ana görsel AVIF/WebP, responsive `srcset`, doğru ölçü ve preload
- Hero dışındaki görseller lazy-load
- Fontlar self-host ve gerekli ağırlıklarla sınırlı
- Kullanılmayan CSS/JS ve ikon paketleri kaldırılmalı
- Üçüncü taraf scriptler onay ve etkileşim ihtiyacına göre geciktirilmeli
- Herkese açık sayfalar CDN/cache uyumlu olmalı; gereksiz PHP oturumu başlatılmamalı

### Erişilebilirlik

- WCAG 2.2 AA hedefi
- Klavye ile tam gezinme
- Görünür focus state
- Form label'ları ve hata özetleri
- Minimum 44×44 px dokunma hedefi
- Renk kontrastı en az 4.5:1
- Video altyazıları ve transkript
- Heading sırası ve landmark kullanımı
- Modal/drawer focus yönetimi

### Güvenlik ve gizlilik

- KVKK ve gerekli durumlarda GDPR uyumu hukuk danışmanıyla doğrulanmalı.
- Pazarlama izni ile zorunlu veri işleme onayı ayrıştırılmalı.
- Çerezler kategori bazlı izin alınmadan çalışmamalı; zorunlu olmayan analitik/pazarlama scriptleri beklemeli.
- Form verisi TLS ile iletilmeli, erişim yetkileri sınırlandırılmalı ve saklama süresi tanımlanmalı.
- reCAPTCHA alternatifi veya kullanıcı dostu spam koruması kullanılmalı.
- WordPress, tema ve eklentiler güncel tutulmalı; gereksiz kullanıcılar ve eklentiler kaldırılmalı.

---

## 13. Analitik ve CRM

### Zorunlu olaylar

- `cta_click` — CTA metni, sayfa, bölüm
- `form_start` — form türü
- `form_submit` / GA4 önerilen `generate_lead`
- `form_error` — alan/hata türü, kişisel veri olmadan
- `whatsapp_click`
- `phone_click`
- `email_click`
- `program_search`
- `filter_apply`
- `program_view`
- `university_view`
- `video_start`, `video_complete`
- `language_switch`

### UTM ve lead attribution

Formla birlikte görünmez alanlarda:

- İlk ve son kaynak/medium/campaign
- Giriş sayfası
- Lead olunan sayfa
- Program/üniversite ilgisi
- GCLID/uygun reklam kimlikleri
- Kullanıcının izniyle analitik kimlik eşleştirmesi

CRM'de lead durumu en az şu aşamalardan geçmeli: Yeni → Ulaşıldı → Görüşme Planlandı → Nitelikli → Başvuru Başladı → Kabul → Kayıt → Kayıp. Böylece yalnız form sayısı değil gerçek başvuru kalitesi ölçülür.

---

## 14. İçerik migrasyonu

1. Tüm URL, trafik, backlink, indeks ve içerik envanteri çıkar.
2. Her sayfayı **koru / güncelle / birleştir / kaldır** olarak sınıflandır.
3. Yazım ve bilgi doğruluğu denetimi yap.
4. Üniversite ve program verisini yapılandırılmış CMS alanlarına taşı.
5. Görsel kullanım haklarını ve öğrenci izinlerini kontrol et.
6. Eski URL'leri yeni en yakın eşdeğere 301 yönlendir; alakasız tüm URL'leri ana sayfaya yönlendirme.
7. Canonical, hreflang, sitemap ve robots kurallarını staging'de test et.
8. Search Console ve analitik karşılaştırması için yayın öncesi baz veri al.

---

## 15. Fazlandırma

### Faz 1 — Strateji ve veri

- İçerik/URL envanteri
- Gerçek hizmet kapsamı ve iddia doğrulama
- Kullanıcı akışları
- CMS veri modeli
- Wireframe ve tasarım sistemi

### Faz 2 — MVP geliştirme

- Global header/footer
- Ana sayfa
- Üniversite ve program listeleri
- Üniversite/program detay şablonları
- Başvuru ve iletişim
- Hakkımızda, hizmetler, öğrenci hikâyeleri
- Temel içerik sayfaları
- TR/EN mimarisi
- GA4/GTM/CRM entegrasyonu

### Faz 3 — SEO migrasyonu ve yayın

- İçerik taşıma
- 301 haritası
- Teknik SEO
- Performans/erişilebilirlik testi
- Form ve ölçüm QA
- Staging → production

### Faz 4 — Optimizasyon

- A/B testleri
- Program karşılaştırma
- Kaydedilen programlar
- Etkileşimli bütçe hesaplayıcı
- Kişiselleştirilmiş program önerisi
- Lead kalite geri beslemesi

---

## 16. Yayın öncesi kabul kriterleri

### Tasarım ve UX

- 360, 390, 768, 1024, 1440 ve 1920 px genişliklerde kırılma yok.
- Mobil CTA içerik veya çerez bildirimini kapatmıyor.
- Ana görevler en fazla 3 etkileşimde başlatılabiliyor.
- Tüm durumlar tasarlanmış: loading, empty, error, success.

### İçerik

- Türkçe sayfalarda İngilizce arayüz metni kalmamış.
- Deneyim, öğrenci sayısı, ofis, partnerlik ve hizmet kapsamı tutarlı.
- Tüm ücret/tarih alanlarında son güncelleme bilgisi var.
- Denklik, vize ve kabul metinleri garanti vermiyor.

### Form ve entegrasyon

- Tüm formlar mobil ve masaüstünde çalışıyor.
- Doğru CRM kaydı, bildirim ve teyit e-postası oluşuyor.
- UTM ve bağlam bilgileri kaybolmuyor.
- Double submit ve spam senaryoları kontrol edilmiş.
- WhatsApp mesajı doğru sayfa/program bilgisini içeriyor.

### SEO

- 301 listesi test edilmiş, yönlendirme zinciri yok.
- Canonical ve hreflang çift yönlü ve doğru.
- Sitemap yalnızca indekslenebilir URL'leri içeriyor.
- Structured data doğrulama hatası yok.
- Eski organik trafik alan URL'lerde yanlış 404 yok.

### Performans ve erişilebilirlik

- Core Web Vitals hedefleri staging benzeri koşullarda karşılanıyor.
- Klavye, ekran okuyucu temel akışları ve renk kontrastı test edilmiş.
- Görseller optimize, boyutları tanımlı ve alt metinleri mevcut.

### Ölçüm

- Tüm kritik olaylar GA4 DebugView/GTM Preview ile doğrulanmış.
- Kişisel veri event parametrelerine gönderilmiyor.
- Consent Mode/çerez davranışı kullanıcı seçimiyle uyumlu.

---

## 17. Claude'un teslim etmesi gereken çıktılar

Claude bu PRD'ye göre yalnız görsel bir mockup üretmemeli. Aşağıdaki çıktıları sırayla hazırlamalı:

1. Mevcut site için kısa sorun/çözüm matrisi
2. Türkiye ve yurtdışı rakipleri için özellik/içerik/SEO/GEO karşılaştırma matrisi
3. Keyword-intent-topic map ve rakip content gap listesi
4. Onaylanabilir sitemap
5. Ana kullanıcı akışları
6. CMS knowledge graph, içerik modeli ve alan listesi
7. Masaüstü + mobil low-fidelity wireframe açıklamaları
8. Tasarım token'ları ve bileşen sistemi
9. Ana sayfa için eksiksiz Türkçe metin taslağı
10. Üniversite ve program detay sayfası örnekleri
11. Form, WhatsApp ve CRM davranışları
12. SEO migrasyon, redirect, canonical ve hreflang planı
13. 12 aylık SEO/GEO yayın takvimi ve ölçüm dashboard'u
14. Uygulama planı ve dosya/bileşen mimarisi
15. Test planı ve kabul kriterleri

Her aşamada şu kurallara uy:

- Placeholder lorem ipsum kullanma.
- Sahte öğrenci yorumu veya kurum logosu üretme.
- İçeriği mevcut siteden körlemesine kopyalama; doğruluk ve dil editinden geçir.
- Mobil görünümü masaüstünün küçültülmüş hâli olarak ele alma.
- Bir sayfada birincil CTA'yı sürekli değiştirme.
- Tasarım kararlarını dönüşüm, güven, erişilebilirlik ve performans gerekçesiyle açıkla.
- Eksik ticari veya hukuki bilgileri maddeler halinde kullanıcıdan talep et; cevap gelene kadar doğrulanmamış iddiaları canlı içeriğe yazma.

---

## 18. Proje başlamadan Hun Education'dan istenecek içerikler

- Güncel logo ve kurumsal kimlik dosyaları
- Resmî şirket unvanları ve ofis bilgileri
- Kullanılacak ana telefon/WhatsApp/e-posta
- Doğrulanmış kuruluş tarihi, öğrenci sayısı ve ekip bilgileri
- Aktif üniversite ilişkileri ve logo kullanım izinleri
- Güncel program, ücret, başlangıç dönemi ve başvuru tarihi veri seti
- Danışmanlık hizmet kapsamı ve ücret politikası
- Öğrenci fotoğraf/video yayın izinleri
- Gerçek öğrenci hikâyeleri
- KVKK/GDPR metinleri ve veri saklama politikası
- CRM ve e-posta altyapısı
- GA4, GTM, Search Console ve reklam hesabı erişim planı
- Eski sitenin yedeği, hosting ve staging bilgileri

---

## 19. İnceleme kaynakları

Bu PRD; 2 Ağustos 2026 tarihinde erişilebilen Hun Education Türkçe ve İngilizce ana sayfaları, iletişim, başvuru, maliyet, üniversite, program, öğrenci görüşü ve alan rehberi sayfalarının incelenmesine dayanır. Uygulama öncesinde tüm ücret, tarih, yasal koşul ve kurum ilişkileri yeniden doğrulanmalıdır.

- https://huneducation.com/
- https://tr.huneducation.com/
- https://tr.huneducation.com/iletisim/
- https://tr.huneducation.com/macaristan-universite-fiyatlari/
- https://tr.huneducation.com/macaristan-universiteleri/
- https://tr.huneducation.com/kurslar/
- https://tr.huneducation.com/macaristan-universiteleri-ogrenci-gorusleri/
- https://tr.huneducation.com/macaristan-universite-basvuru-sartlari/

Rakip ve uluslararası benchmarklar:

- https://www.elt.com.tr/macaristanda-universite-egitim
- https://www.academix.com.tr/yurtdisinda-universite/macaristanda-universite
- https://www.applyboard.com/
- https://www.idp.com/
- https://gostudyin.com/study-in-uk/
- https://www.gooverseas.com/study-abroad
- https://www.iesabroad.org/
- https://worldstrides.com/en-us/higher-ed/programs

SEO/GEO için güncel resmî rehberler:

- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://developers.google.com/search/docs/appearance/ai-features
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- https://developers.openai.com/api/docs/bots
- https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview
