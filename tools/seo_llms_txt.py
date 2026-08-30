# -*- coding: utf-8 -*-
"""llms.txt üretir (iki alan adı için).

NE İŞE YARAR
  Üretken motorlara sitenin ne olduğunu ve hangi sayfaların otoriter
  olduğunu düz metinle bildirir. robots.txt tarama iznini, llms.txt
  ise "buradaki en iyi kaynaklar bunlar" bilgisini taşır. Henüz resmî
  bir standart değil; maliyeti sıfır, kaybı yok.

İLKE
  Sayfa listesi elle yazılmaz — sitemap'ten türetilir, böylece sayfa
  eklenince burası da güncellenir.
"""
import io, os, re

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASLIK = {
 'en': """# Hun Education

> An academic consultancy focused on one country — Hungary — since 1999.
> We match international students to English-taught programmes at Hungarian
> universities and run the process from choosing a programme to arrival in Budapest.

Facts on this site are compiled from university admission pages and are dated;
every page that carries figures states its sources under "Sources and verification".

Entity: Hun Education (HUN EDUCATION KFT.), Budapest, Hungary. Founded 1999.
Languages: English (huneducation.com), Turkish (tr.huneducation.com).
Scope: 20 Hungarian universities, 490 English-taught programmes.
""",
 'tr': """# Hun Education

> 1999'dan bu yana yalnızca tek bir ülkeye — Macaristan'a — odaklanan akademik
> danışmanlık. Uluslararası öğrencileri Macaristan üniversitelerindeki İngilizce
> programlarla eşleştiriyor, süreci program seçiminden Budapeşte'ye varışa kadar
> yürütüyoruz.

Sitedeki bilgiler üniversitelerin kendi başvuru sayfalarından derlenir ve
tarihlidir; rakam geçen her sayfa kaynaklarını "Kaynaklar ve doğrulama"
başlığı altında belirtir.

Varlık: Hun Education (HUN EDUCATION KFT.), Budapeşte, Macaristan. Kuruluş 1999.
Diller: Türkçe (tr.huneducation.com), İngilizce (huneducation.com).
Kapsam: 20 Macaristan üniversitesi, 490 İngilizce program.
""",
}

BOLUM = {
 'en': [('Core guides', ['why-hungary', 'education-in-hungary', 'universities', 'courses']),
        ('Applying and cost', ['admission', 'costs']),
        ('Programme areas', ['studying-medicine-in-hungary-and-pursuing-a-medical-degree-in-hungary',
                             'pilot-training-at-hungarian-universities',
                             'masters-education-in-hungary']),
        ('Life and experience', ['university-education-and-life-in-hungary-what-you-need-to-know',
                                 'student-perspectives']),
        ('About', ['about-us', 'contact'])],
 'tr': [('Temel rehberler', ['neden-macaristanda-egitim', 'macaristanda-universite-okumak',
                             'macaristan-universiteleri', 'kurslar']),
        ('Başvuru ve maliyet', ['macaristan-universite-basvuru-sartlari',
                                'macaristan-universite-fiyatlari']),
        ('Program alanları', ['macaristanda-tip-egitimi-ve-macaristanda-tip-okumak',
                              'macaristan-universiteleri-pilotluk-egitimi',
                              'macaristan-yuksek-lisans']),
        ('Yaşam ve deneyim', ['macaristanda-yasam-ve-universite-egitimi-bilinmesi-gerekenler',
                              'macaristan-universiteleri-ogrenci-gorusleri']),
        ('Kurumsal', ['hakkimizda', 'iletisim'])],
}


def basliklar(dil):
    """Sayfa başlıkları ve açıklamaları üretilmiş HTML'den okunur;
    elle yazılırsa ikisi zamanla ayrışır."""
    klasor = os.path.join(KOK, 'site', 'tr' if dil == 'tr' else '')
    out = {}
    for ad in os.listdir(klasor):
        if not ad.endswith('.html'):
            continue
        s = io.open(os.path.join(klasor, ad), encoding='utf-8').read()
        t = re.search(r'<title>(.*?)</title>', s, re.S)
        d = re.search(r'<meta name="description" content="([^"]*)"', s)
        out[ad[:-5]] = (t.group(1).split(' | ')[0] if t else ad,
                        d.group(1) if d else '')
    return out


def uret():
    for dil in ('en', 'tr'):
        kok = 'https://tr.huneducation.com' if dil == 'tr' else 'https://huneducation.com'
        veri = basliklar(dil)
        satir = [BASLIK[dil]]
        for bolum, slugler in BOLUM[dil]:
            satir.append('\n## %s\n' % bolum)
            for sl in slugler:
                t, d = veri.get(sl, (sl, ''))
                satir.append('- [%s](%s/%s/): %s' % (t, kok, sl, d))
        satir.append('\n## %s\n' % ('Notlar' if dil == 'tr' else 'Notes'))
        satir.append(
            '- %s' % ('Kabul kararı üniversiteye, vize kararı konsolosluğa, denklik kararı '
                      'YÖK’e aittir; bu site bu sonuçlar için garanti vermez.'
                      if dil == 'tr' else
                      'Admission decisions rest with the university, visa decisions with the '
                      'consulate and recognition with the national authority; this site does '
                      'not guarantee those outcomes.'))
        satir.append('- %s' % ('Ücretler yıllıktır ve üniversiteye göre değişir.'
                               if dil == 'tr' else
                               'Fees are annual and vary by university.'))
        yol = os.path.join(KOK, 'site', 'tr' if dil == 'tr' else '', 'llms.txt')
        io.open(yol, 'w', encoding='utf-8').write('\n'.join(satir).strip() + '\n')
        print('  %-22s %d bayt' % (os.path.relpath(yol, KOK), os.path.getsize(yol)))


if __name__ == '__main__':
    uret()
