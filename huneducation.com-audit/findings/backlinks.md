# Otorite ve dış bağlantı profili

> **Güven düzeyi: DÜŞÜK.** Moz ve Bing Webmaster API anahtarları yapılandırılmamış.
> Elde yalnızca Common Crawl web grafiği ve doğrulama tarayıcısı vardı; backlink
> ajanı da oturum yeniden başlarken kesildi. Aşağıdakiler **eksiksiz bir bağlantı
> profili değildir** — referans veren alan adı sayısı, DA/PA ve zehirli bağlantı
> analizi için Ahrefs/Semrush/Moz gibi bir kaynak gerekir. Burada yalnızca
> doğrudan doğrulayabildiklerim var.

## Doğrulanan: varlık tutarlılığı

Sitenin yayınladığı dört sosyal profilin tamamı canlı:

| Profil | Durum |
|---|---|
| instagram.com/huneducation | 200 ✓ |
| facebook.com/HunEducationGLB | 200 ✓ |
| twitter.com/huneducation | 200 ✓ |
| youtube.com/channel/UCtjkiFBPE4S-igdJ_GVbFUQ | 200 ✓ |

**Düzeltme:** Bunlar hiçbir yerde `sameAs` olarak bildirilmiyor (sitede yapısal
veri yok). Organization düğümüne eklenmesi, arama motorunun kurumu tek varlık
olarak tanıması için en ucuz adım. YouTube bağlantısı kanal kimliğiyle veriliyor;
varsa `@kullanıcıadı` biçimi varlık eşleştirmesi için daha iyidir.

## Bulgu: dışa bağlantı neredeyse yok

Ana sayfadan çıkan **8 benzersiz dış alan adı** var ve bunların çoğu teknik
(gmpg.org, fonts.gstatic.com, facebook.com piksel). Gerçek bir otorite kaynağına
tek bağlantı: `immigration-portal.ec.europa.eu`.

Ücret, son başvuru tarihi ve kabul şartı yayınlayan bir sitede **kaynak
göstermemek** hem E-E-A-T hem GEO açısından zayıflık. Üretken motorlar kaynak
gösteren sayfaları tercih eder.

**Düzeltme:** Rakam geçen her sayfaya, o rakamın alındığı üniversite sayfasına
bağlantı ver. Bu aynı zamanda 20 üniversite sayfasıyla konu ilişkisini güçlendirir.

## Bu niş için bağlantı kazanım planı

Öncelik sırasıyla, gerçekçi olandan zora doğru:

1. **Üniversitelerin kendi "partner/agent" sayfaları** — Hun Education 20
   üniversiteyle çalışıyor. Çoğu Macar üniversitesi resmî temsilci listesi
   yayınlar. Bu, nişteki en yüksek otoriteli ve en kolay bağlantı.
2. **YÖK denklik ve konsolosluk kaynak sayfaları** — öğrenci vizesi ve denklik
   içeriği üretilirse, forum ve rehber sayfalarından doğal atıf gelir.
3. **Türk eğitim portalları ve forumları** — yurtdışı eğitim dizinleri, üniversite
   tercih forumları. Ücretli dizin değil, içerik katkısı yoluyla.
4. **Mezun ve öğrenci içeriği** — isimli öğrenci hikâyeleri hem E-E-A-T hem
   paylaşılabilir varlık üretir; şu an `/student-perspectives/` sayfasında tek bir
   isimli yorum yok.
5. **YouTube ve Instagram çapraz bağlantısı** — mevcut kanallar siteye
   bağlanmalı; sosyal bağlantılar sıralama geçirmez ama varlık tutarlılığı sağlar.

## Yapılmaması gereken

Ücretli bağlantı, dizin spam'i ve "guest post paketi" — bu nişte rakiplerin bir
kısmı bunu yapıyor; kısa vadeli, riskli ve bu sitenin asıl sorununu (indekslenme
ve yapısal veri) çözmüyor.

Score: (ölçülemedi — veri kaynağı yetersiz)
