# -*- coding: utf-8 -*-
"""audit-data.json'dan FULL-AUDIT-REPORT.md ve ACTION-PLAN.md üretir."""
import json, io

d = json.load(io.open('audit-data.json', encoding='utf-8'))
s = d['summary']
ROZET = {'Critical': '🔴 Kritik', 'High': '🟠 Yüksek', 'Medium': '🟡 Orta',
         'Low': '⚪ Düşük', 'Info': '🔵 Bilgi'}
SIRA = {'Critical': 0, 'High': 1, 'Medium': 2, 'Low': 3, 'Info': 4}

r = []
w = r.append

w('# huneducation.com — Kapsamlı SEO, GEO ve Sağlık Denetimi\n')
w('**Tarih:** %s   ·   **Taranan sayfa:** %d   ·   **Tahmini site boyutu:** ~%d URL\n'
  % (s['audit_date'], s['pages_crawled'], s['estimated_site_size']))
w('**İş modeli:** %s\n' % s['business_type'])

w('\n---\n\n## Yönetici özeti\n')
w('# SAĞLIK SKORU: %d / 100\n' % s['health_score'])
w('> Bu skor, kategorileri ağırlıklandırılmış ortalamadır. 31 puan, "kırık değil ama '
  'kapatılmış" bir siteyi tarif eder: altyapı satın alınmış, kurulmuş ve sonra devre '
  'dışı bırakılmış. İyi haber, düzeltmelerin çoğunun içerik üretmeyi değil **anahtar '
  'çevirmeyi** gerektirmesi.\n')

w('\n### Kategori skorları\n')
w('| Kategori | Skor | Ağırlık |')
w('|---|---|---|')
for c in d['categories']:
    ag = {'Technical SEO': '22%', 'Content Quality': '23%', 'On-Page SEO': '20%',
          'Schema / Structured Data': '10%', 'Performance (CWV)': '10%',
          'AI Search Readiness (GEO)': '10%', 'Images': '5%'}[c['name']]
    w('| %s | **%d**/100 | %s |' % (c['name'], c['score'], ag))
w('\nAğırlıklandırılmayan ek ölçümler: Sitemap/keşfedilebilirlik **14**/100 · '
  'Arama deneyimi (SXO) **38**/100 · Görsel/mobil **42**/100 · '
  'Otorite/backlink *ölçülemedi*.\n')

w('\n### En kritik beş bulgu\n')
for i, t in enumerate(s['top_findings'], 1):
    w('%d. %s' % (i, t))

w('\n### En hızlı beş kazanç\n')
for i, t in enumerate(s['quick_wins'], 1):
    w('%d. %s' % (i, t))

w('\n---\n\n## Kök sebep: SEO altyapısı kurulu ama kapalı\n')
w('Denetimdeki kritik bulguların çoğu tek bir olguya iniyor. Aşağıdaki eklentiler '
  'sitede **kurulu** ama **pasif**:\n')
w('| Eklenti | Pasif olmasının sonucu |')
w('|---|---|')
w('| Yoast SEO 27.6 + Premium 20.9 | 494/500 sayfada meta description yok, sitemap yok, OG yok |')
w('| WPML SEO 2.2.5 | hreflang hiç yok — EN ve TR aynı sorguda birbiriyle yarışıyor |')
w('| Schema & Structured Data 1.60 | site genelinde sıfır yapısal veri |')
w('| WP Rocket / WP Fastest Cache / LiteSpeed | önbellek yok |')
w('| Smush Pro | görsel optimizasyonu yok |')
w('\nBunun yerine çalışan **Auctollo "XML Sitemap Generator for Google" v4.1.23**, '
  'WordPress’in kendi sitemap’ini de gölgeliyor. Sonuç: `/wp-sitemap-posts-course-1.xml` '
  '498 geçerli URL içeriyor ama **HTTP 404** ile sunuluyor; `/wp-sitemap.xml` 200 dönüyor '
  'ama boş. Google hiçbirini kullanamıyor.\n')

w('\n---\n')
for c in d['categories']:
    w('\n## %s — %d/100\n' % (c['name'], c['score']))
    if c['what_works']:
        w('**Çalışan yanlar**\n')
        for t in c['what_works']:
            w('- %s' % t)
        w('')
    for f in sorted(c['findings'], key=lambda x: SIRA[x['severity']]):
        w('\n### %s — %s\n' % (ROZET[f['severity']], f['title']))
        w(f['description'] + '\n')
        w('**Düzeltme:** ' + f['recommendation'])
    w('')

w('\n---\n\n## Kapsam ve güven sınırları\n')
w('Bu denetimin neyi ölçemediği, ölçtüğü kadar önemlidir:\n')
for t in d['limitations']:
    w('- %s' % t)

w('\n---\n\n## Üretilen dosyalar\n')
w('- `FULL-AUDIT-REPORT.md` — bu rapor')
w('- `ACTION-PLAN.md` — önceliklendirilmiş eylem planı')
w('- `audit-data.json` — yapılandırılmış denetim verisi')
w('- `findings/` — 11 uzman bulgu dosyası (teknik, içerik, şema, sitemap, performans, '
  'GEO, SXO, görsel, on-page, altyapı sağlığı, backlink)')
w('- `screenshots/` — 20 ekran görüntüsü (5 sayfa × masaüstü/mobil)')
w('- `crawl.json` — 500 sayfalık ham tarama verisi')

io.open('FULL-AUDIT-REPORT.md', 'w', encoding='utf-8').write('\n'.join(r) + '\n')

# ---------------- eylem plani ----------------
p = []
a = p.append
a('# huneducation.com — Eylem Planı\n')
a('Sıra, **etki ÷ efor** oranına göre. Faz 1’in tamamı yapılandırma; içerik üretimi gerektirmez.\n')
ETKI = {0: 'Çok yüksek', 1: 'Yüksek', 2: 'Orta', 3: 'Sürekli'}
for i, f in enumerate(d['action_plan']['phases']):
    a('\n## %s\n' % f['name'])
    a('**Zaman:** %s   ·   **Beklenen etki:** %s\n' % (f['timeframe'], ETKI[i]))
    for it in f['items']:
        a('- [ ] %s' % it)

a('\n---\n\n## Önce şunu yap\n')
a('Tek bir madde seçilecekse: **program son başvuru tarihlerini güncelle.** Tarih girilmiş '
  '965 programın 965’inde tarih geçmiş; katalog ziyaretçiye 14 ay önce kapanmış dönemleri '
  'gösteriyor. Bu bir SEO sorunu değil, doğrudan gelir kaybı — ve düzeltmesi toplu '
  'güncelleme işidir, içerik yazımı değil.\n')
a('İkinci sıradaki: **Auctollo’yu kapat, Yoast + WPML SEO’yu aç.** Bu tek hamle sitemap, '
  'meta description, Open Graph ve hreflang’i aynı anda devreye alır — ~1.052 URL '
  'bildirilebilir hâle gelir.\n')

a('\n## Ölçüm kurulumu (paralel yürüsün)\n')
a('- [ ] Search Console’u her iki alan adı için doğrula ve denetime bağla')
a('- [ ] GA4 (G-88T4Y5BXLQ) organik segmentini raporlamaya bağla')
a('- [ ] Değişiklik öncesi baz çizgi al: sıralama, gösterim, indekslenen sayfa sayısı')
a('- [ ] Backlink profilini bir kez gerçek araçla ölç (bu denetimde ölçülemedi)')

io.open('ACTION-PLAN.md', 'w', encoding='utf-8').write('\n'.join(p) + '\n')
print('FULL-AUDIT-REPORT.md ve ACTION-PLAN.md yazıldı')
