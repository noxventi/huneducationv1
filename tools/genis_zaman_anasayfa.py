# -*- coding: utf-8 -*-
"""Ana sayfa govde metinleri: genis zaman ve kurumsal anlatim.

Hero basligi, cagri butonlari ve kapanis bolumu geri alindigi haliyle
KALIR; burada yalnizca bolum aciklamalari ve SSS govdeleri, sayfalarin
geri kalaniyla ayni dile cekilir.
"""
import io

R = [
# --- bolum girisleri ---
("""        Süreç boyunca aynı ekiple çalışıyorsunuz. Hangi adımda sizden ne beklendiğini ve bizim ne
        yaptığımızı baştan yazılı olarak paylaşıyoruz, böylece hiçbir aşamada belirsizlik kalmıyor.""",
 """        Süreç boyunca aynı ekiple çalışırsınız. Hangi adımda sizden ne beklendiğini ve bizim ne
        yaptığımızı baştan yazılı olarak paylaşırız; böylece hiçbir aşamada belirsizlik kalmaz."""),

("""        Bir yılın maliyeti yalnızca öğrenim ücretinden ibaret değil. Aşağıdan eğitim seviyenizi ve
        konaklama tercihinizi seçin; yıllık bütçenizin kalem kalem nasıl dağıldığını hemen görün.""",
 """        Bir yılın maliyeti yalnızca öğrenim ücretinden ibaret değildir. Aşağıdan eğitim seviyenizi
        ve konaklama tercihinizi seçin; yıllık bütçenizin kalem kalem nasıl dağıldığını hemen görün."""),

("""        Aşağıdaki yanıtları güncel koşullara göre düzenli olarak gözden geçiriyoruz. Kesin bilgi için her zaman""",
 """        Aşağıdaki yanıtları güncel koşullara göre düzenli olarak gözden geçiririz. Kesin bilgi için her zaman"""),

# --- alan kartlari ---
('<p class="fcard__desc">Klinik uygulama ağırlıklı bütünleşik program. Kontenjanlar sınırlı olduğu için başvuru takvimi kritik.</p>',
 '<p class="fcard__desc">Klinik uygulama ağırlıklı bütünleşik bir programdır. Kontenjanlar sınırlı olduğu için başvuru takvimi belirleyici olur.</p>'),
('<p class="fcard__desc">Macaristan\'da veterinerlik, eczacılık, mimarlık, hukuk ve müzik alanlarında da programlar bulunuyor.</p>',
 '<p class="fcard__desc">Macaristan\'da veterinerlik, eczacılık, mimarlık, hukuk ve müzik alanlarında da programlar bulunur.</p>'),
('<p class="fcard__desc">Yıllık ücret uçuş eğitimini de kapsar; Class 1 sağlık raporu ve dil şartı başvurudan önce ayarlanmalıdır.</p>',
 '<p class="fcard__desc">Yıllık ücret uçuş eğitimini de kapsar; Class 1 sağlık raporu ve dil şartı başvurudan önce tamamlanmalıdır.</p>'),

# --- SSS govdeleri ---
("""          <p>Macaristan'daki üniversiteler kendi başvuru ve kabul süreçlerini yürütüyor; YKS puanı
          genellikle bir kabul şartı değil. Bununla birlikte kabul her bölümde sınavsız ilerlemiyor,
          birçok programda üniversitenin kendi giriş sınavı bulunuyor:</p>""",
 """          <p>Macaristan'daki üniversiteler kendi başvuru ve kabul süreçlerini yürütür; YKS puanı
          genellikle bir kabul şartı değildir. Bununla birlikte kabul her bölümde sınavsız ilerlemez,
          birçok programda üniversitenin kendi giriş sınavı bulunur:</p>"""),

("""          <p>Üniversitelerin çoğu dil belgesi yerine kendi mülakatını ya da çevrim içi sınavını yapıyor.
          Belge isteyen okullarda <b>lisansta</b> IELTS <b>5, 6 veya 6,5</b>; <b>yüksek lisansta</b>
          <b>IELTS 6,5</b> veya eşdeğeri görülüyor.</p>""",
 """          <p>Üniversitelerin çoğu dil belgesi yerine kendi mülakatını ya da çevrim içi sınavını yapar.
          Belge isteyen okullarda <b>lisansta</b> IELTS <b>5, 6 veya 6,5</b>; <b>yüksek lisansta</b>
          <b>IELTS 6,5</b> veya eşdeğeri görülür.</p>"""),

("""          programlarına başvurabilirsiniz; ücreti yıllık 2.500 €'dan başlar. Kabul edilen belge türü ve
          minimum puan üniversiteye ve programa göre değişir.</p>""",
 """          programlarına başvurabilirsiniz; ücretler yıllık 2.500 €'dan başlar. Kabul edilen belge türü
          ve minimum puan üniversiteye ve programa göre değişir.</p>"""),
]

p = 'site/tr/index.html'
s = io.open(p, encoding='utf-8').read()
n = 0
for a, b in R:
    if a in s:
        s = s.replace(a, b, 1); n += 1
    else:
        print('  ! eslesmedi ::', ' '.join(a.split())[:70])
io.open(p, 'w', encoding='utf-8').write(s)
print('%-20s %d degisiklik' % (p, n))
