# -*- coding: utf-8 -*-
"""Ana sayfadan öğrenci hikâyeleri bölümünü ve "Kısaca" tablosunu kaldırır.

KALDIRILANLAR
  1. #hikayeler bölümü. İçerik kaybolmuyor: öğrenci görüşleri kendi
     sayfasında duruyor ve header menüsünden erişiliyor.
  2. .brief__facts tanım listesi (çağrı hücresi dâhil) ve altındaki
     .brief__meta satırı.

BİRLİKTE DÜZELTİLMESİ GEREKENLER
  - DefinedTermSet şeması bu tablodan üretiliyordu. Tablo gidince şema
    da gitmeli; aksi hâlde yapısal veri sayfada olmayan içeriği beyan
    eder ve bu bir arama motoru ihlalidir.
  - WebPage.speakable seçicileri .brief__facts'i gösteriyordu; artık
    yalnızca .brief__lead kalıyor.
  Bu ikisi anasayfa_schema.py içinde yapılıyor; burada yalnızca HTML
  temizleniyor ve şema betiği yeniden çalıştırılıyor.
"""
import io, re, sys

SITE = sys.argv[1] if len(sys.argv) > 1 else 'site'

# Bölüm yorumu + section gövdesi birlikte gider
HIKAYE = re.compile(
    r'<!-- ={10,}\s*\n\s*(?:BÖLÜM|SECTION)[^\n]*\n\s*={10,} -->\s*\n'
    r'<section class="stories section" id="hikayeler".*?\n</section>\n\n?', re.S)

FACTS = re.compile(r'\n\s*<dl class="brief__facts">.*?</dl>\n', re.S)
META = re.compile(r'\n\s*<p class="brief__meta">.*?</p>\n', re.S)


def temizle(yol):
    s = io.open(yol, encoding='utf-8').read()
    once = len(s)

    s, n1 = HIKAYE.subn('', s, count=1)
    s, n2 = FACTS.subn('\n', s, count=1)
    s, n3 = META.subn('\n', s, count=1)

    if not (n1 and n2 and n3):
        print('  ! eksik eşleşme (%s): hikaye=%d tablo=%d not=%d' % (yol, n1, n2, n3))
        return False

    for zorunlu in ('<header class="hdr', '<main', '</main>', '<footer', 'brief__lead'):
        if zorunlu not in s:
            print('  ! %s kayboldu, yazma iptal: %s' % (zorunlu, yol)); return False
    # Kalıntı kontrolü yalnızca HTML'e bakar; JSON-LD içindeki
    # speakable seçicisi hâlâ .brief__facts diyor, onu şema betiği
    # düzeltiyor.
    if '<section class="stories' in s or '<dl class="brief__facts"' in s:
        print('  ! kalıntı var, yazma iptal:', yol); return False

    io.open(yol, 'w', encoding='utf-8').write(s)
    print('%-22s %d -> %d byte' % (yol, once, len(s)))
    return True


for d in ('tr/index.html', 'index.html'):
    temizle(SITE + '/' + d)
