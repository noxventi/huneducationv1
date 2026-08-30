# -*- coding: utf-8 -*-
"""Basvuru ve maliyet sayfalarinin yapisini sadelestirir.

Iki sayfa da ayni konuyu birden fazla basliga bolmustu; okuyucu
icindekilerde 7-8 satir gorup nereye bakacagina karar veremiyordu.

Basvuru: 7 bolum -> 4. Uygunluk basa aliniyor (belge hazirlamadan once
bilinmesi gereken sey bu), dil sarti belgelerin altina, adim adim surec
ve sik hatalar takvimin altina giriyor.

Maliyet: 6 bolum -> 3. Universite farklari ogrenim ucretinin, tek
seferlik kalemler yasam giderinin, butce plani ise yillik toplamin
altina giriyor.

Ayni sadelestirme Ingilizce sayfalara da uygulaniyor ki iki dil
birbirinden ayrilmasin.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sade_ortak import basvuru, maliyet

# --------------------------------------------------------------- TÜRKÇE
basvuru(
    'tools/pages_content.py',
    """{toc([('kisa-cevap','Kısa cevap'),('belgeler','Gerekli belgeler'),('dil','Dil yeterliliği'),('uygunluk','Uygun musunuz?'),
      ('sinav','Giriş sınavı ve mülakat'),('takvim','Başvuru takvimi'),('surec','Adım adım süreç'),
      ('istisna','İstisnalar ve sık yapılan hatalar'),('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}""",
    """{toc([('uygunluk','Kimler başvurabilir?'),('belgeler','Gerekli belgeler ve dil şartı'),
      ('sinav','Giriş sınavı ve mülakat'),('takvim','Başvuru takvimi ve süreç'),
      ('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}""",
    {'uygunluk': 'uygunluk', 'belgeler': 'belgeler', 'dil': 'dil',
     'surec': 'surec', 'istisna': 'istisna'},
    {'dil': 'Dil yeterliliği', 'surec': 'Adım adım süreç',
     'istisna': 'Sık yapılan hatalar'},
)

maliyet(
    'tools/pages_content.py',
    """{toc([('kisa-cevap','Kısa cevap'),('ogrenim','Öğrenim ücretleri'),('universite','Üniversiteye göre'),
      ('yasam','Yaşam giderleri'),('tekseferlik','Tek seferlik ücretler'),('toplam','Yıllık toplam'),
      ('plan','Bütçe planı nasıl kurulur'),('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}""",
    """{toc([('ogrenim','Öğrenim ücretleri'),('yasam','Yaşam giderleri'),
      ('toplam','Yıllık toplam bütçe'),
      ('sss','Sık sorulan sorular'),('kaynak','Kaynaklar')])}""",
    {'universite': 'universite', 'tekseferlik': 'tekseferlik', 'plan': 'plan'},
    {'universite': 'Üniversiteye göre farklar', 'tekseferlik': 'Tek seferlik ücretler',
     'plan': 'Bütçe planınızı nasıl kuruyoruz'},
)
