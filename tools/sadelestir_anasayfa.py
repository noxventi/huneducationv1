# -*- coding: utf-8 -*-
"""Ana sayfa: bilgi karmasasini azaltir, Turkceyi dogallastirir.

Uc sorun vardi:

  1. Program bulucu (3 soru) ile "Populer alanlar" galerisi ayni soruyu
     ust uste soruyordu: "hangi alanda okumak istiyorsunuz?" Ziyaretci
     hangisini kullanacagini bilemiyordu. Galeri artik alternatif degil,
     "alanini zaten bilenler icin kisayol" olarak konumlaniyor.
  2. "Neden Hun Education?" ustbasligi ve H2'si birebir ayniydi.
  3. Bolum girisleri telgraf gibi yaziliydi. Canlidaki gibi akici
     cumlelere cevriliyor.

Sadelestirme bolum silmiyor; bolumler arasindaki iliskiyi acik hale
getiriyor, cunku her bolumun kendi isi var.
"""
import io

R = {
'site/tr/index.html': [
# --- 1) alanlar galerisi: rakip degil kisayol ---
("""        <p class="eyebrow">Popüler alanlar</p>
        <h2 class="h-md display" id="fields-h">Türk öğrencilerin en çok<br>araştırdığı bölümler</h2>""",
 """        <p class="eyebrow">Alanınızı biliyorsanız</p>
        <h2 class="h-md display" id="fields-h">Doğrudan bölümünüze<br>göz atın</h2>"""),

# --- 2) "Neden Hun Education?" tekrari ---
("""<p class="eyebrow" data-reveal="up-sm">Neden Hun Education?</p>""",
 """<p class="eyebrow" data-reveal="up-sm">Nasıl çalışıyoruz?</p>"""),

# --- 3) surec girisi: dogal Turkce ---
("""        Altı adımın tamamında aynı ekiple çalışırsınız. Her adımda sizden ne beklendiği ve
        bizim ne yaptığımız önceden yazılı olarak bellidir.""",
 """        Süreç boyunca aynı ekiple çalışıyorsunuz. Hangi adımda sizden ne beklendiğini ve bizim ne
        yaptığımızı baştan yazılı olarak paylaşıyoruz, böylece hiçbir aşamada belirsizlik kalmıyor."""),

# --- 4) maliyet girisi ---
("""        Toplam maliyet yalnızca öğrenim ücreti değildir. Eğitim seviyenizi ve konaklama
        tercihinizi seçin; yıllık tahmini aralık ve kalem kalem dağılımı anında güncellensin.""",
 """        Bir yılın maliyeti yalnızca öğrenim ücretinden ibaret değil. Aşağıdan eğitim seviyenizi ve
        konaklama tercihinizi seçin; yıllık bütçenizin kalem kalem nasıl dağıldığını hemen görün."""),

# --- 5) SSS basligi ---
("""<h2 class="h-md display" id="faq-h" data-split>En çok merak edilen<br>altı soru</h2>""",
 """<h2 class="h-md display" id="faq-h" data-split>En çok sorulan<br>altı soru</h2>"""),
],

'site/index.html': [
("""        <p class="eyebrow">Popular fields</p>""",
 """        <p class="eyebrow">If you already know your field</p>"""),

("""<p class="eyebrow" data-reveal="up-sm">Why Hun Education?</p>""",
 """<p class="eyebrow" data-reveal="up-sm">How we work</p>"""),
],
}

for yol, ciftler in R.items():
    s = io.open(yol, encoding='utf-8').read()
    n = 0
    for a, b in ciftler:
        if a in s:
            s = s.replace(a, b, 1); n += 1
        else:
            print('  ! eslesmedi %s :: %s' % (yol, ' '.join(a.split())[:64]))
    io.open(yol, 'w', encoding='utf-8').write(s)
    print('%-20s %d degisiklik' % (yol, n))
