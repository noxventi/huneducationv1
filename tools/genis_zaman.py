# -*- coding: utf-8 -*-
"""Govde metinlerini simdiki zamandan genis zamana cevirir.

Turkce kurumsal metinde bilgi aktaran cumleler genis zamanla kurulur
("ucretler programa gore degisir"), sirketin kendi eylemi ise birinci
cogul sahis ve simdiki zamanla anlatilir ("basvurulari yurutuyoruz").
Sayfalarin govdesi bastan sona simdiki zamandaydi.

IKI KURAL

  1. Kor bir "-yor -> -ir" donusumu Turkcede bozuk fiil uretir, o yuzden
     donusum ELDE YAZILMIS bir fiil tablosuyla yapilir. Tabloda olmayan
     hicbir kelimeye dokunulmaz.

  2. Turkcede birlesik yuklem zincirinde yalnizca son fiil cekimlenir:
     "belirliyor, ... yanlarinda oluyoruz". Buradaki "belirliyor"
     genis zamana cevrilirse cumle bozulur. Bu yuzden her eslesme icin
     AYNI CUMLE ICINDE ilerisi taranir; cumle "-yoruz / -yorsunuz /
     -yorum" ile bitiyorsa o fiil oldugu gibi birakilir.
"""
import io, re, glob

# ---------------------------------------------------------------- tablo
FIIL = {
    # olmak, bulunmak, durmak
    'oluyor': 'olur', 'bulunuyor': 'bulunur', 'oluşuyor': 'oluşur',
    'duruyor': 'durur', 'kalıyor': 'kalır', 'kalmıyor': 'kalmaz',
    'doluyor': 'dolar', 'biniyor': 'biner',
    # sunmak, vermek
    'sunuyor': 'sunar', 'veriyor': 'verir', 'veriliyor': 'verilir',
    'sunuluyor': 'sunulur', 'okutuluyor': 'okutulur', 'sağlıyor': 'sağlar',
    'kazandırıyor': 'kazandırır', 'yetiştiriyor': 'yetiştirir',
    # gerek, istek
    'gerekiyor': 'gerekir', 'isteniyor': 'istenir', 'istemiyor': 'istemez',
    'istenmiyor': 'istenmez', 'istiyor': 'ister', 'aranıyor': 'aranır',
    'bekleniyor': 'beklenir', 'gerektiriyor': 'gerektirir',
    'bekliyor': 'bekler', 'sorulmuyor': 'sorulmaz', 'soruyor': 'sorar',
    'istenebiliyor': 'istenebilir',
    # surec
    'yürüyor': 'yürür', 'yürütülüyor': 'yürütülür', 'yürütüyor': 'yürütür',
    'ilerliyor': 'ilerler', 'işliyor': 'işler', 'sürüyor': 'sürer',
    'geçiyor': 'geçer', 'başlıyor': 'başlar', 'bitiyor': 'biter',
    'kapanıyor': 'kapanır', 'tamamlanıyor': 'tamamlanır',
    'uygulanıyor': 'uygulanır', 'uyguluyor': 'uygular',
    'yapılıyor': 'yapılır', 'yapıyor': 'yapar', 'ediyor': 'eder',
    'etmiyor': 'etmez', 'işleniyor': 'işlenir', 'kurgulanıyor': 'kurgulanır',
    'düzenleniyor': 'düzenlenir', 'yenileniyor': 'yenilenir',
    'izliyor': 'izler', 'planlıyor': 'planlar', 'hazırlıyor': 'hazırlar',
    'hazırlanılıyor': 'hazırlanılır', 'tamamlıyor': 'tamamlar',
    # olcum, degisim
    'değişiyor': 'değişir', 'tutuyor': 'tutar', 'taşıyor': 'taşır',
    'kapsıyor': 'kapsar', 'gösteriyor': 'gösterir', 'artıyor': 'artar',
    'ekleniyor': 'eklenir', 'ekliyor': 'ekler', 'dayanıyor': 'dayanır',
    'sayılıyor': 'sayılır', 'sayıyor': 'sayar', 'yoğunlaşıyor': 'yoğunlaşır',
    'ayrışıyor': 'ayrışır', 'yansıtıyor': 'yansıtır', 'çekiyor': 'çeker',
    'üretiyor': 'üretir', 'üretiliyor': 'üretilir',
    # degerlendirme
    'belirliyor': 'belirler', 'belirleniyor': 'belirlenir',
    'değerlendiriliyor': 'değerlendirilir', 'değerlendiriyor': 'değerlendirir',
    'alınıyor': 'alınır', 'alıyor': 'alır', 'bakılıyor': 'bakılır',
    'bakıyor': 'bakar', 'bakmıyor': 'bakmaz', 'ödeniyor': 'ödenir',
    'çıkıyor': 'çıkar', 'çıkarıyor': 'çıkarır', 'geliyor': 'gelir',
    'gelmiyor': 'gelmez', 'seçiyor': 'seçer', 'hesaplıyor': 'hesaplar',
    'karşılaştırıyor': 'karşılaştırır', 'görülüyor': 'görülür',
    'görüyor': 'görür', 'derliyor': 'derler', 'inceliyor': 'incelir',
    'açıklanıyor': 'açıklanır', 'kaydediyor': 'kaydeder',
    # yasam, anlatim
    'yaşıyor': 'yaşar', 'okuyor': 'okur', 'söylüyor': 'söyler',
    'anlatıyor': 'anlatır', 'özetliyor': 'özetler', 'konuşuyor': 'konuşur',
    'yayınlanıyor': 'yayınlanır', 'yayımlanıyor': 'yayımlanır',
    'yazılıyor': 'yazılır', 'karşılıyor': 'karşılar', 'ağırlıyor': 'ağırlar',
    'seyrediyor': 'seyreder', 'rahatlıyor': 'rahatlar', 'açıyor': 'açar',
    'birleştiriyor': 'birleştirir', 'bağlıyor': 'bağlar',
    'dönüştürüyor': 'dönüştürür', 'dönüşüyor': 'dönüşür',
    'kolaylaştırıyor': 'kolaylaştırır', 'yaratıyor': 'yaratır',
    'kılıyor': 'kılar', 'götürüyor': 'götürür', 'yöneliyor': 'yönelir',
    # -ebiliyor / -abiliyor
    'değişebiliyor': 'değişebilir', 'çıkabiliyor': 'çıkabilir',
    'kapanabiliyor': 'kapanabilir', 'olabiliyor': 'olabilir',
    'edilebiliyor': 'edilebilir', 'yapılabiliyor': 'yapılabilir',
    'etkileyebiliyor': 'etkileyebilir',
}

RX = re.compile(r'(?<![\wçğıöşüÇĞİÖŞÜ])(%s)(?![\wçğıöşüÇĞİÖŞÜ])'
                % '|'.join(sorted(map(re.escape, FIIL), key=len, reverse=True)))

# Cumle sonu: nokta, soru/unlem ya da blok etiketi kapanisi
CUMLE_SONU = re.compile(r'[.!?]|</p>|</li>|</td>|</h[1-6]>')
BIRINCI_COGUL = re.compile(r'(?:yoruz|yorsunuz|yorum)(?![\wçğıöşüÇĞİÖŞÜ])')


def ayni_cumlede_biz_var_mi(s, i):
    """i konumundan cumle sonuna kadar birinci cogul cekim var mi?

    Varsa bu fiil bir birlesik yuklem zincirinin parcasidir ve
    cevrilmemelidir: "belirliyor, ... yanlarinda oluyoruz".
    """
    son = CUMLE_SONU.search(s, i)
    parca = s[i:son.start()] if son else s[i:i + 400]
    return bool(BIRINCI_COGUL.search(parca))


DOSYALAR = sorted(glob.glob('tools/pages_content*.py'))
toplam = atlanan = 0

for p in DOSYALAR:
    s = io.open(p, encoding='utf-8').read()
    n = a = 0
    parcalar, son = [], 0
    for m in RX.finditer(s):
        parcalar.append(s[son:m.start()])
        if ayni_cumlede_biz_var_mi(s, m.end()):
            parcalar.append(m.group(1)); a += 1
        else:
            parcalar.append(FIIL[m.group(1)]); n += 1
        son = m.end()
    parcalar.append(s[son:])
    io.open(p, 'w', encoding='utf-8').write(''.join(parcalar))
    toplam += n; atlanan += a
    print('%-26s %3d cevrildi, %d korundu' % (p, n, a))

print('toplam: %d cevrildi, %d birlesik yuklem korundu' % (toplam, atlanan))
