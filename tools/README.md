# tools/ — yayın araçları

Sitedeki 24 sayfanın 20'si burada üretilir. Header, footer, künye ve yasal
sayfa iskeleti altı sayfada birebir aynı olmak zorunda; iki dille birlikte bu
40 kopya eder. Elle sürdürmek yerine tek yerden üretilir.

Hepsi bağımlılıksız Python 3'tür.

## Sayfaları yeniden üret

```bash
python tools/gen_pages.py site en
```

```bash
python tools/gen_pages.py site tr
```

İngilizce çıktı `site/` köküne, Türkçe çıktı `site/tr/` altına yazılır.
Üretilen sayfalar: rehber, üniversiteler, başvuru, maliyetler, hakkımızda,
iletişim ve dört yasal sayfa.

`index.html` ve program kataloğu elle yazılmıştır; onların İngilizceye
aktarımı `en_home*.py` ve `en_programs.py` ile yapıldı (kaynak olarak
`site/tr/` kopyasını alırlar).

## Sitemap, robots ve bağ denetimi

```bash
python tools/seo_bilingual.py site
```

24 URL'lik `sitemap.xml`'i her biri karşılıklı hreflang alternatifleriyle
üretir, `robots.txt`'i yazar ve **tüm iç bağlantı ile varlık yollarının**
çözülüp çözülmediğini kontrol eder.

## İki dil denetimi

```bash
python tools/audit_i18n.py site
```

24 sayfanın tamamında şunları kontrol eder:

1. `<html lang>` doğru mu
2. `canonical` kendi URL'sini mi gösteriyor
3. `hreflang` en / tr / x-default üçlüsü eksiksiz ve **karşılıklı** mı
4. Dil değiştirici karşı dilin eş sayfasını mı gösteriyor, `aria-current` var mı
5. İngilizce sayfalarda çevrilmemiş Türkçe metin kalmış mı

Çıktıda yalnız özel isimler (Türkiye, Kadıköy, Pécs, danışman adları, KVKK
madde harfleri) beklenen kalıntılardır; bunlar `ALLOW` kümesinde tanımlı.

## İçerik nerede

| Dosya | Ne üretir |
|---|---|
| `pages_content.py` / `en_content.py` | Başvuru şartları, maliyetler |
| `pages_content2.py` / `en_content2.py` | Ana rehber, üniversiteler |
| `pages_content3.py` / `en_content3.py` | Hakkımızda, iletişim |
| `pages_content4.py` / `en_content4.py` | Dört yasal sayfa |

Header/footer metinleri içerik dosyalarında değil, `gen_pages.py` içindeki
`W` sözlüğündedir. Dosya adları (slug) `SLUG` tablosunda; bir slug değişirse
hem sayfa adı hem de tüm iç bağlantılar oradan güncellenir.

## URL şeması

`gen_pages.py` başındaki üç sabit her şeyi belirler:

```python
DOMAIN  = 'https://huneducation.com'
EN_BASE = DOMAIN + '/'
TR_BASE = DOMAIN + '/tr/'
```

Türkçe alt alan adına taşınacaksa `TR_BASE`'i `https://tr.huneducation.com/`
yapmak ve `seo_bilingual.py` içindeki `url_of()` fonksiyonunu aynı şekilde
güncellemek yeterlidir; dosya düzeni değişmez — `site/tr/` dizini o alan adının
kök dizini olur. Böyle bir geçişte `tr.huneducation.com/*` adreslerinden
`huneducation.com/tr/*` adreslerine 301 gerekir.
