# WordPress altyapı sağlığı

Kaynak: canlı kurulumdan doğrudan okuma (Novamira), 2026-08-30. Salt okuma.

## Özet

| Ölçüm | Değer | Değerlendirme |
|---|---|---|
| PHP | 8.0.30 | **Ömrü dolmuş** — güvenlik yaması almıyor |
| WordPress | 7.1 | Güncel |
| Kurulu eklenti | 48 | Fazla |
| Aktif eklenti | 20 | — |
| **Pasif eklenti** | **28** | Kod diskte duruyor, güncellenmiyor: saldırı yüzeyi |
| Bekleyen güncelleme | **21** | Yüksek |
| Revizyon kaydı | 7.384 | `wp_posts`'un çoğu |
| autoload option boyutu | 329 KB | Sınırda (ideal < 200 KB) |

## Kritik

### PHP 8.0 destek dışı
PHP 8.0 Kasım 2023'te güvenlik desteğini yitirdi. Barındırma panelinden 8.2 veya
8.3'e çıkılmalı. Elementor 4.x ve WP 7.1 ikisini de destekliyor.

### 21 bekleyen eklenti güncellemesi
Aktif eklentilerin bir kısmı güncel değil. Elementor, JetEngine ve WPML gibi
temel bileşenlerde güvenlik yaması kaçırmak, tüm siteyi riske atar.

## Yüksek

### 28 pasif eklenti diskte duruyor
Pasif eklenti çalışmaz ama **dosyaları erişilebilir kalır** ve güncelleme almaz.
Bilinen açığı olan eski bir eklenti, pasifken bile bazı durumlarda sömürülebilir.
Kullanılmayacaklar silinmeli.

Ayrıca bu listede SEO açısından kritik dört eklenti var ve **pasif oldukları için
sitenin SEO'su fiilen kapalı**:

| Eklenti | Durum | Sonucu |
|---|---|---|
| Yoast SEO 27.6 | pasif | meta description yok, sitemap yok |
| Yoast SEO Premium 20.9 | pasif | — |
| WPML SEO 2.2.5 | pasif | **hreflang yok** |
| Schema & Structured Data 1.60 | pasif | **yapısal veri yok** |
| WP Rocket / WP Fastest Cache / LiteSpeed | pasif | önbellek yok |
| Smush Pro | pasif | görsel optimizasyonu yok |

Bu tek satır, denetimdeki kritik bulguların çoğunun kök sebebi.

### Veritabanı şişkinliği
`wp_postmeta` 155 MB / 77.185 satır, `wp_posts` 51 MB / 5.870 satır. İçinde
**7.384 revizyon** var — gerçek içerik 1.052 URL iken kayıt sayısı bunun beş katı.

Ayrıca:
- `wp_cbnetpo_ping_optimizer` 6,5 MB / 31.965 satır — WordPress Ping Optimizer
  eklentisi **pasif** ama tablosu büyümeye devam etmiş
- `wp_actionscheduler_logs` 6,2 MB / 19.953 satır — temizlenmiyor
- `wp_asp_index` 22 MB — Ajax Search Pro arama indeksi

**Düzeltme:** `wp-config.php`'ye `define('WP_POST_REVISIONS', 5);`, eski
revizyonları temizle, Action Scheduler log saklama süresini kısalt, kullanılmayan
eklenti tablolarını düşür. Tahmini kazanç: veritabanının ~%40'ı.

## Orta

### autoload 329 KB
Her sayfa isteğinde belleğe alınıyor. 28 pasif eklentinin bıraktığı ayarlar da
burada. Temizlik TTFB'ye doğrudan yansır.

## Not

Bu bölümdeki hiçbir şey için canlıya yazma yapılmadı; tamamı okuma sorgusudur.
