# -*- coding: utf-8 -*-
"""Turkce dil kalitesi ve ic tutarlilik duzeltmeleri.

1. Basvuru sayfasinin "Kisa cevap"i, sayfanin geri kalanindaki duzeltmelerle
   celisiyordu: banka dokumunu zorunlu gosteriyor, IELTS'i abartiyor ve
   yas/uyruk/mali yeterlilik sartlarindan hic soz etmiyordu.
2. Hazirlik ucreti hala "donemlik" yaziliydi; canlida yillik.
3. Ana sayfadaki pilotaj ve ucret notlari "donemlik" diyordu.
4. Mobil alt menude Ingilizce kalmis baglantilar.
5. Ceviri kokan birkac kalip.
"""
import io, os, sys

TOOLS = sys.argv[1] if len(sys.argv) > 1 else 'tools'
SITE = sys.argv[2] if len(sys.argv) > 2 else 'site'

TR_ICERIK = {
'pages_content.py': [
 # --- kisa cevap: sayfanin geri kalaniyla uyumlu hale getirildi ---
 ("""  <p>Macaristan'da üniversite başvurusu için apostilli diploma, İngilizce transkript, pasaport
  fotokopisi, İngilizce özgeçmiş ve son 6 aylık banka hesap dökümü gerekir. Lisansta en az B2
  İngilizce beklenir; yüksek lisansta genellikle IELTS 6.5 istenir. Sağlık ve mühendislik
  programlarında üniversitenin kendi giriş sınavı uygulanır. Eylül dönemi için başvurular Haziran'a,
  Şubat dönemi için Kasım'a kadar yapılmalıdır.</p>""",
  """  <p>Başvuru için apostilli diploma, İngilizce transkript, pasaport fotokopisi ve İngilizce
  özgeçmiş gerekir; banka dökümü başvuruda değil vize aşamasında istenir. Lisansta pratikte B2
  İngilizce beklenir ama üniversitelerin çoğu dil belgesi yerine kendi mülakatını yapar. Yaş sınırı
  lisansta 25, yüksek lisansta 28; tıpta sınır yok. Eylül dönemi başvuruları Nisan ile Haziran
  arasında, Şubat dönemi başvuruları Ekim sonu ile Kasım arasında kapanır.</p>"""),

 # --- hazirlik ucreti donemlik degil yillik ---
 ("""     "<p>Evet. B2 seviyesinde bir belgeniz yoksa üniversitelerin bünyesindeki İngilizce Dil Hazırlık "
     "programına başvurabilirsiniz. Hazırlık ücretleri dönemlik 2.500 €'dan başlar ve başarıyla "
     "tamamlandığında bölüme geçiş yapılır.</p>"),""",
  """     "<p>Evet. Üniversitelerin çoğu zaten dil belgesi istemiyor, kendi mülakatını yapıyor. B2 "
     "seviyesinde değilseniz üniversite bünyesindeki İngilizce Dil Hazırlık programına "
     "başvurabilirsiniz; ücretler yıllık 2.500 €'dan başlar ve program başarıyla tamamlandığında "
     "bölüme geçiş yapılır.</p>"),"""),

 # --- ceviri kokan kalip ---
 ("Aşağıdaki liste tüm programlar için ortak çekirdek dosyadır. Program bazında ek belge\nistenebilir; kabul şartlarını başvuru öncesinde birlikte kontrol ederiz.",
  "Aşağıdaki belgeler her başvuruda isteniyor. Programa göre ek belge çıkabilir; kabul şartlarını\nbaşvurudan önce birlikte gözden geçiriyoruz."),
 ("<td>Geçerlilik süresi eğitim süresini karşılamalı</td>",
  "<td>Pasaportun geçerlilik süresi eğitim süresini kapsamalı</td>"),
],
'pages_content2.py': [
 # pilotaj sehir notu
 ("<td>Pilotluk ve mühendislik birleşik programı</td>",
  "<td>Pilotluk ve makine mühendisliğini birleştiren program</td>"),
 # "sahiptir" kalkasi
 ("<li><b>Köklü üniversite geleneği.</b> Ülkenin üniversiteleri yüzyıllara dayanan bir akademik\n  geçmişe sahiptir.</li>",
  "<li><b>Köklü üniversite geleneği.</b> Ülkedeki üniversitelerin akademik geçmişi yüzyıllara\n  dayanıyor.</li>"),
],
'pages_content5.py': [
 ("<li><b>Köklü üniversite geleneği.</b>", "<li><b>Köklü üniversite geleneği.</b>"),
],
}

# --- elle yazilmis sayfalar ---
TR_SAYFA = {
'tr/index.html': [
 # mobil alt menu Ingilizce kalmis
 ('<a href="macaristanda-universite-okumak.html">Why Hungary?</a>', '<a href="macaristanda-universite-okumak.html">Neden Macaristan?</a>'),
 ('<a href="macaristan-universite-basvuru-sartlari.html">Admissions</a>', '<a href="macaristan-universite-basvuru-sartlari.html">Başvuru ve Kabul</a>'),
 ('<a href="#maliyet">Costs</a>', '<a href="#maliyet">Maliyetler</a>'),
 ('<a href="macaristanda-universite-okumak.html#visa">Visa &amp; Residence</a>', '<a href="macaristanda-universite-okumak.html#vize">Vize ve Oturum</a>'),
 # pilotaj karti: ucret artik yillik ve ucus dahil
 ('<p class="fcard__desc">Teorik eğitim ve uçuş saatleri ayrı ayrı ücretlendirilir; sağlık raporu ve dil şartı önden planlanmalıdır.</p>',
  '<p class="fcard__desc">Yıllık ücret uçuş eğitimini de kapsar; Class 1 sağlık raporu ve dil şartı başvurudan önce ayarlanmalıdır.</p>'),
 # alan notu: pilotajda donemlik ifadesi artik yanlis
 ('Ücretler yıllık öğrenim ücretidir (pilotajda dönemliktir) ve üniversiteye göre değişir;',
  'Ücretler yıllık öğrenim ücretidir ve üniversiteye göre değişir;'),
],
'index.html': [
 ('<p class="fcard__desc">Ground school and flight hours are priced separately; the medical certificate and language requirement need planning up front.</p>',
  '<p class="fcard__desc">The annual fee covers the flight training; the Class 1 medical certificate and language requirement need arranging before you apply.</p>'),
 ('Fees shown are annual tuition (per term for pilot training) and vary by university; universities',
  'Fees shown are annual tuition and vary by university; universities'),
],
'tr/kurslar.html': [
 ('<p><b>Ücretler yıllık öğrenim ücretidir</b> (pilotajda dönemliktir) ve programa göre değişir.',
  '<p><b>Ücretler yıllık öğrenim ücretidir</b> ve programa göre değişir.'),
],
'courses.html': [
 ('<p><b>Fees shown are annual tuition</b> (per term for pilot training) and vary by programme.',
  '<p><b>Fees shown are annual tuition</b> and vary by programme.'),
],
}


def uygula(kok, tablo, etiket):
    for dosya, ciftler in tablo.items():
        p = os.path.join(kok, dosya)
        if not os.path.exists(p):
            print('  ! yok:', p); continue
        s = io.open(p, encoding='utf-8').read()
        n = 0
        for a, b in ciftler:
            if a == b:
                continue
            if a in s:
                s = s.replace(a, b); n += 1
            else:
                print('  ! eslesmedi: %s :: %s' % (dosya, ' '.join(a.split())[:58]))
        io.open(p, 'w', encoding='utf-8').write(s)
        print('%-8s %-24s %d' % (etiket, dosya, n))


uygula(TOOLS, TR_ICERIK, 'icerik')
uygula(SITE, TR_SAYFA, 'sayfa')
