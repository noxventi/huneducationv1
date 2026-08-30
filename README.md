# huneducation

Hun Education (huneducation.com) için yürütülen yeniden tasarım ve SEO çalışmasının
tamamı. İki ayrı iş bir arada duruyor: yerelde sıfırdan yazılan **yeni site
prototipi** ve canlı WordPress kurulumunda yapılan **SEO/GEO düzeltmeleri**.

Site iki alan adında yayında: `huneducation.com` (İngilizce) ve
`tr.huneducation.com` (Türkçe). Canlı taraf WordPress + Elementor + JetEngine +
WPML üzerinde çalışıyor; buradaki prototip ise bağımlılıksız HTML/CSS/ES modülü.

## Dizinler

| Dizin | Ne var |
|---|---|
| `site/` | Yeni site prototipi. 24 sayfa (14 EN + 10 TR), bağımlılıksız ön yüz. |
| `tools/` | Sayfa üreticileri. 24 sayfanın 20'si `gen_pages.py` ile basılıyor. |
| `cikti/` | Üretilmiş paketler — staging'e taşınan zip'ler ve derlenmiş varlıklar. |
| `ham/` | Ham fotoğraf kaynakları. Sitedeki görseller buradan seçilip işlendi. |
| `seo-canli/` | Canlı sitede yapılan SEO/GEO çalışması: mu-plugin'ler, ölçüm araçları, değişiklik kaydı. |
| `huneducation.com-audit/` | 500 sayfalık kapsamlı SEO/GEO/sağlık denetimi ve raporları. |

## Prototipi üretmek

```
python tools/gen_pages.py site en
python tools/gen_pages.py site tr
```

Üretici, içerik modüllerini `exec` ile çalıştırıp sayfayı bütün olarak basar;
header, footer, künye ve yasal metinler tek yerden gelir. `site/` altındaki
sayfaların dördü elle yazılmıştır ve üretici tarafından ezilmez.

## Canlı SEO çalışması

`seo-canli/DEGISIKLIK-KAYDI.md` her turu, gerekçesini ve geri alma noktasını
kaydediyor. Canlıya giren her değişiklik öncesi ve sonrası 41 URL üzerinden
ölçüldü (`baseline.py` + `fark.py`); amaç sıralamada geriye gitmeden ilerlemekti.

Sunucudaki düzeltmeler `wp-content/mu-plugins/` altında tek tek dosyalar hâlinde
duruyor — her biri silindiğinde kendi değişikliğini geri alır. Kopyaları
`seo-canli/` içinde.

## Denetim

`huneducation.com-audit/` içinde 500 sayfalık tarama, 11 uzman bulgu dosyası,
20 ekran görüntüsü ve iki PDF rapor var. Denetimin ana bulgusu: sitenin SEO
altyapısı satın alınmış ve kurulmuş, sonra kapatılmıştı — Yoast, WPML SEO ve
WPML String Translation dâhil.
