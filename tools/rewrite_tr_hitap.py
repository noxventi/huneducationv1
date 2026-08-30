# -*- coding: utf-8 -*-
"""Maliyet, yuksek lisans ve ogrenci gorusleri sayfalarinin girisleri.

audit_akicilik.py bu uc sayfada okura dogrudan hitap eden tek cumle
bulamadi; metin kimseye seslenmeden bilgi aktariyordu. Girisler
canlidaki gibi okurla konusan bir agiza cevriliyor, rakamlar aynen
kaliyor.
"""
import io

R = {
'tools/pages_content.py': [
("""<section id="giris" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Macaristan'da eğitim ve yaşam giderleri birlikte yıllık <b>8.500 – 14.000 €</b> tutar.""",
 """<section id="giris" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Yurt dışında okumayı düşünürken aklınıza gelen ilk soru büyük ihtimalle bütçe oluyor. Macaristan
  bu konuda rahatlatıcı bir tablo sunuyor: eğitim ve yaşam giderleri birlikte yıllık
  <b>8.500 – 14.000 €</b> tutuyor.""",),
],
'tools/pages_content5.py': [
("""  <p>Macaristan'da yüksek lisans iki yıl ve 120 AKTS, İngilizce yürüyor. Hun Education'ın yayınladığı
  aralık <b>yıllık 4.000 – 6.000 €</b>; katalog genelinde gerçek rakamlar daha geniş bir bantta,
  üniversiteye ve alana göre yaklaşık 3.200 € ile 14.000 € arasında. Kabul için ilgili alanda tanınan bir lisans diploması ve çoğu üniversitede IELTS 6,5
  isteniyor. Eylül dönemi başvuruları Nisan–Haziran arasında kapanıyor; birçok program Şubat dönemi de
  alıyor.</p>""",
 """  <p>Lisansını tamamlamış ve kariyerine Avrupa'da devam etmek isteyen öğrenciler için Macaristan
  oldukça pratik bir seçenek sunuyor. Yüksek lisans programları iki yıl sürüyor, 120 AKTS taşıyor ve
  baştan sona İngilizce yürüyor. Ücretler çoğunlukla <b>yıllık 4.000 – 6.000 €</b> bandında; katalog
  genelinde üniversiteye ve alana göre 3.200 € ile 14.000 € arasında değişiyor. Kabul için alanınızla
  ilgili tanınan bir lisans diploması, çoğu üniversitede de IELTS 6,5 isteniyor. Başvurunuzu Eylül
  dönemi için Nisan–Haziran arasında yapabilir, birçok programda Şubat dönemini de
  değerlendirebilirsiniz.</p>"""),
],
'tools/pages_content7.py': [
("""  <p>Aşağıdaki yorumlar başvurusunu birlikte yürüttüğümüz öğrencilere ait; izinleriyle ve kendi
  tercihleri doğrultusunda ad ve baş harfle yayınlanıyor. Budapeşte, Debrecen ve Pécs'te tıp,
  mühendislik, medya ve dil bilimleri okuyan öğrencileri kapsıyor.</p>""",
 """  <p>Bir ülkeyi anlatan en iyi kaynak, orada okuyan öğrencilerin kendisidir. Aşağıdaki yorumlar
  başvurusunu birlikte yürüttüğümüz öğrencilere ait ve izinleriyle, kendi tercihleri doğrultusunda ad
  ya da baş harfle yayınlanıyor. Budapeşte, Debrecen ve Pécs'te tıp, mühendislik, medya ve dil
  bilimleri okuyan arkadaşlarınızın deneyimlerini burada okuyabilirsiniz.</p>"""),
],
}

for yol, ciftler in R.items():
    s = io.open(yol, encoding='utf-8').read()
    n = 0
    for a, b in ciftler:
        if a in s:
            s = s.replace(a, b, 1); n += 1
        else:
            print('  ! eslesmedi %s :: %s' % (yol, ' '.join(a.split())[:66]))
    io.open(yol, 'w', encoding='utf-8').write(s)
    print('%-26s %d degisiklik' % (yol, n))
