# -*- coding: utf-8 -*-
"""Canlı siteden indirilen görselleri sayfalar için hazırlar.

SEÇİM İLKESİ
  69 aday görselin tamamı kontak sayfalarına dizilip TEK TEK BAKILDI;
  dosya adına güvenilmedi. Bu önemliydi: canlıdaki
  "macaristanda_tip_okumak.jpg" aslında jenerik bir ders çalışma
  fotoğrafı, tıpla ilgisi yok. Listeye alınmadı.

  Aşağıdaki her kayıttaki açıklama, görselde GERÇEKTEN görüneni anlatır.
  Kurum adı yalnızca binada tabela okunuyorsa ya da kaynak kümesi o
  kuruma aitse yazıldı.

ÇIKTI
  Her görsel iki genişlikte webp: büyük (1400w) ve 760w.
"""
import os
from PIL import Image

HAM = 'ham'
HEDEF = 'site/assets/img'
GENISLIKLER = [(1400, ''), (760, '-760')]

# (kaynak, cikti adi, gorselde gercekten ne var)
SECIM = [
    # ---------------- PİLOTAJ: gerçek öğrenci fotoğrafları ----------------
    ('IMG_5913_Original-scaled.jpg', 'pilotaj-hangar-egitim-ucagi',
     'Uçuş üniforması ve reflektif yelek giymiş öğrenci, hangarda çift motorlu eğitim uçağının önünde'),
    ('IMG_0641.jpg', 'pilotaj-ogrenciler-hangara-giderken',
     'Reflektif yelekli öğrenci grubu, çimenlikten uçak hangarına doğru yürürken'),
    ('IMG_0667.jpg', 'pilotaj-egitim-ucaklari-apron',
     'Apronda yan yana dizilmiş tek motorlu eğitim uçakları'),
    ('IMG_4757_Original-scaled.jpg', 'pilotaj-ogrenci-pervane',
     'Pilot üniformalı öğrenci, tek motorlu eğitim uçağının pervanesinin yanında'),
    ('IMG_4908_Original-scaled.jpg', 'pilotaj-ogrenciler-pist',
     'Pilot gömlekli üç öğrenci, uçuş alanında birlikte'),
    ('IMG_9020_Original-scaled.jpg', 'pilotaj-fuar-standi',
     'Üniformalı iki öğrenci, bir pilot akademisi fuar standının önünde'),

    # --- PİLOTAJ: canlı sayfanın karuselindeki iki stok kare ve derslik ---
    # Bunlar canlıdaki pilotaj sayfasında halihazırda kullanılıyor; sayfa
    # birebir aynı kareleri taşısın diye listeye alındı. İkisi stok
    # fotoğraf (havalimanı ve uçak motoru); alt yazıları da öyle söyler,
    # kendi öğrencimiz ya da kendi filomuz gibi sunulmaz.
    ('18f73a81-aa47-4495-8c26-9b48b0805251.jpeg', 'pilotaj-derslik-uniformali',
     'Pilot üniformalı öğrenci grubu, derslikte sıraların başında'),
    ('pexels-tanathip-rattanatum-2026324-1-scaled.jpg', 'pilotaj-apron-gun-batimi',
     'Gün batımında havalimanı apronu, körüğe yanaşmış yolcu uçağı'),
    ('pexels-ahmed-muntasir-912050-scaled.jpg', 'pilotaj-ucak-motoru',
     'Apronda bir yolcu uçağının motoru ve kanadı, bulutlu gökyüzü'),

    # ---------------- TIP ----------------
    # Canlı tıp sayfasının karuselindeki dört kare. Üçü laboratuvar ve
    # görüntüleme konulu stok fotoğraf; alt yazılar kurum adı vermez.
    ('pexels-edward-jenner-4032060-scaled.jpg', 'tip-mikroskop-laboratuvar',
     'Laboratuvarda önlüklü bir araştırmacı mikroskop başında; tezgâhta kan tüpleri'),
    ('pexels-mart-production-7089023-scaled.jpg', 'tip-goruntuleme-ekranlari',
     'Radyoloji odasında ekranlarda beyin görüntüleme kesitleri'),
    ('pexels-chokniti-khongchum-3938023-scaled.jpg', 'tip-laboratuvar-tup',
     'Bone ve gözlük takmış laboratuvar çalışanı, mavi deney tüplerine pipetle sıvı aktarıyor'),
    ('macaristanda_tip_okumak-scaled.jpg', 'tip-ogrenci-calisma-grubu',
     'Derslikte masa başında birlikte çalışan öğrenci grubu'),

    ('semmelweis-1.jpg', 'semmelweis-tarihi-bina',
     'Semmelweis Üniversitesi’nin tarihi tuğla ve taş cepheli binası'),
    ('semmelweis-2.jpg', 'semmelweis-vitray',
     'Semmelweis Üniversitesi binasındaki renkli vitray pencere'),
    ('semmelweis-3.jpg', 'semmelweis-modern-bina',
     'Semmelweis Üniversitesi’nin akşam ışıklandırılmış modern binası'),
    ('pte6-1280x720-1.jpg', 'pecs-kampus-hava',
     'Pécs Üniversitesi kampüsünün havadan görünümü'),

    # ---------------- ÜNİVERSİTELER ----------------
    ('pte5-1280x720-1.jpg', 'pecs-universitesi-tabela',
     'Pécs Üniversitesi binası; girişte “University of Pécs” tabelası'),
    ('pte10-1280x720-1.jpg', 'pecs-tas-kemer-giris',
     'Pécs Üniversitesi’nin taş kemerli avlu girişi'),
    ('pte4-1280x720-1.jpg', 'pecs-sonbahar-kampus',
     'Sonbaharda Pécs Üniversitesi binası ve önündeki ağaçlar'),
    ('debrecen-6.jpeg', 'debrecen-ana-bina',
     'Debrecen Üniversitesi’nin sütunlu ana binası ve önündeki havuz'),
    ('debrecen-7.jpeg', 'debrecen-cam-bina',
     'Debrecen Üniversitesi’nin cam cepheli modern binası'),
    ('debrecen-8.jpeg', 'debrecen-kuleli-bina',
     'Debrecen Üniversitesi’nin kuleli binası'),
    ('elte2-1280x720-1.jpg', 'elte-tarihi-bina',
     'ELTE’nin tarihi taş cepheli binası'),
    ('elte3-1280x720-1.jpg', 'elte-avlu',
     'ELTE’nin kemerli iç avlusu'),
    ('elte6-1280x720-1.jpg', 'elte-kutuphane',
     'ELTE’nin ahşap raflı, iki katlı tarihi kütüphane salonu'),
    ('elte4-1280x720-1.jpg', 'elte-gece-cephe',
     'ELTE binasının gece ışıklandırılmış cephesi'),
    ('szeged1-1280x720-1.jpg', 'szeged-ana-bina',
     'Szeged Üniversitesi’nin sarı cepheli ana binası'),
    ('szeged4-1280x720-1.jpg', 'szeged-modern-bina',
     'Szeged Üniversitesi’nin cam cepheli modern binası'),
    ('szeged-dorm.jpeg', 'szeged-yurt-binasi',
     'Szeged’de bir öğrenci yurdu binası ve önünden geçen yayalar'),
    ('ME_summer-scaled.jpg', 'miskolc-cam-bina',
     'Miskolc Üniversitesi’nin cam cepheli binası ve önündeki meydan'),
    ('UM-panorama-01.jpg', 'miskolc-kampus-hava',
     'Sonbaharda Miskolc Üniversitesi kampüsünün havadan panoraması'),
    ('obuda-1.jpeg', 'obuda-sari-bina',
     'Óbuda Üniversitesi’nin sarı cepheli tarihi binası'),
    ('obuda-2.jpeg', 'obuda-ogrenciler',
     'Óbuda Üniversitesi tabelası altında bankta oturan öğrenci grubu'),
    ('obuda-7.jpeg', 'obuda-yemekhane',
     'Óbuda Üniversitesi’nin geniş, aydınlık yemekhanesi'),
    ('metropolitan.jpg', 'metu-bina-tabela',
     '“Budapesti Metropolitan Egyetem” yazılı yuvarlak kampüs binası'),
    ('metropolitan1.jpg', 'metu-ogrenci-grubu',
     'Kampüs bahçesinde toplanmış uluslararası öğrenci grubu'),
    ('metropolitan2.jpg', 'metu-ogrenci-portre',
     'Kampüs koridorunda, cam cephenin önünde duran bir öğrenci'),
    ('metropolitan3.jpg', 'metu-derslik',
     'Amfi dersliğinde dizüstü bilgisayar başında çalışan öğrenciler'),
    ('metropolitan5.jpg', 'metu-tasarim-atolye',
     'Tasarım atölyesinde yere serilmiş baskı çalışmaları ve bir öğrenci'),
    ('bme3-1280x720-1.jpg', 'bme-tuna-kiyisi',
     'Tuna kıyısındaki tarihi üniversite binası ve nehirde bir gemi'),
    ('bme4-1280x720-1.jpg', 'bme-kampus-ogrenciler',
     'Kampüs çimenliğinde birlikte proje kuran öğrenci grubu'),
    ('bme8-1280x720-1.jpg', 'bme-tarihi-salon',
     'Kemerli pencereleri olan tarihi çalışma salonu ve sıralar'),
    ('vet-1280x720-1.jpg', 'univet-avlu-heykeller',
     'Veteriner Üniversitesi’nin avlusu; iki yanda köpek heykelleri'),
    ('Corvinus-Prep-School-Building-1.jpg', 'corvinus-bina',
     'Corvinus Üniversitesi’nin modern cam ve taş cepheli binası'),

    # ---------------- ŞEHİR / YAŞAM ----------------
    ('budapest-6928973_1280.jpg', 'budapeste-balikci-tabyasi',
     'Balıkçı Tabyası’nın kemerinden gün doğumunda Budapeşte manzarası'),
    ('IMG_8095_Original-scaled.jpg', 'budapeste-koprude-ogrenciler',
     'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci'),
    ('pte8-1280x720-1.jpg', 'pecs-sehir-hava',
     'Pécs şehir merkezinin kırmızı çatılı havadan görünümü'),
]


def hazirla():
    os.makedirs(HEDEF, exist_ok=True)
    kayit, eksik = [], []
    for kaynak, ad, _ in SECIM:
        yol = os.path.join(HAM, kaynak)
        if not os.path.exists(yol):
            eksik.append(kaynak); continue
        im = Image.open(yol).convert('RGB')
        ow, oh = im.size
        # Dikey görsel dar bir sütunda durur; BÜYÜK boyu küçültülür.
        # Küçük boy küçültülmez: yüksek DPR telefonda 760 CSS px'lik
        # yuvayı doldurmalı, yoksa büyütülüp bulanıklaşır.
        dikey = oh > ow
        for g0, ek in GENISLIKLER:
            g = round(g0 * 0.72) if (dikey and not ek) else g0
            k = im.copy()
            if ow > g:
                k = k.resize((g, round(oh * g / ow)), Image.LANCZOS)
            k.save(os.path.join(HEDEF, '%s%s.webp' % (ad, ek)),
                   'WEBP', quality=80, method=6)
        buyuk = os.path.join(HEDEF, ad + '.webp')
        w, h = Image.open(buyuk).size
        kayit.append((ad, w, h, os.path.getsize(buyuk)))
    for e in eksik:
        print('  ! kaynak yok:', e)
    print('%d görsel hazırlandı, toplam %.0f KB'
          % (len(kayit), sum(x[3] for x in kayit) / 1024))
    return kayit


if __name__ == '__main__':
    hazirla()
