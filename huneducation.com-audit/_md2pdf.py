# -*- coding: utf-8 -*-
"""Denetim raporlarını tek bir PDF'e basar — kurulum gerektirmez.

NEDEN BU YOL
  Beceri paketinin kendi PDF üreticisi WeasyPrint'e bağlı; WeasyPrint de
  Windows'ta GTK yerel kütüphanelerini (libgobject/pango/cairo) arıyor ve
  bu makinede kurulu değil. Oysa Chromium zaten burada (Playwright ile
  geldi) ve --print-to-pdf ile aynı işi sistem kurulumu olmadan yapıyor.

  Markdown -> HTML dönüşümü için kütüphane eklenmedi: dönüştürülecek
  markdown'ı bu denetim kendisi ürettiği için alt küme bilinen ve dar.
"""
import io, os, re, subprocess, sys, glob

KOK = os.path.dirname(os.path.abspath(__file__))
CHROME = os.path.expanduser(
    '~/.claude/skills/seo/ms-playwright/chromium-1234/chrome-win64/chrome.exe')

CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
* { box-sizing: border-box; }
body { font: 10.5pt/1.55 "Segoe UI", system-ui, sans-serif; color: #1a1d29;
       margin: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
h1 { font-size: 21pt; line-height: 1.2; margin: 0 0 6pt; color: #0f1330;
     letter-spacing: -0.01em; }
h1.skor { font-size: 30pt; text-align: center; color: #b3261e; margin: 14pt 0 4pt;
          padding: 12pt; border: 2pt solid #b3261e; border-radius: 6pt; }
h2 { font-size: 15pt; margin: 20pt 0 7pt; padding-bottom: 4pt;
     border-bottom: 1.4pt solid #4650e0; color: #0f1330; page-break-after: avoid; }
h3 { font-size: 11.5pt; margin: 13pt 0 4pt; color: #23283f; page-break-after: avoid; }
p { margin: 0 0 7pt; }
ul, ol { margin: 0 0 8pt; padding-left: 17pt; }
li { margin-bottom: 3pt; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0 12pt;
        font-size: 9.5pt; page-break-inside: avoid; }
th { background: #eef0fb; text-align: left; font-weight: 600; }
th, td { border: 0.6pt solid #ccd0e4; padding: 4.5pt 6pt; vertical-align: top; }
tr:nth-child(even) td { background: #fafbff; }
blockquote { margin: 8pt 0; padding: 7pt 11pt; background: #f5f6fd;
             border-left: 3pt solid #4650e0; color: #33384d; }
code { font-family: "Cascadia Mono", Consolas, monospace; font-size: 9pt;
       background: #f1f2f8; padding: 1pt 3pt; border-radius: 2pt; }
hr { border: 0; border-top: 0.6pt solid #d5d8e8; margin: 16pt 0; }
strong { color: #0f1330; }
.kapak { text-align: center; padding-top: 55mm; page-break-after: always; }
.kapak .alt { color: #5b6076; font-size: 11pt; margin-top: 8pt; }
.kapak .tarih { color: #8b90a6; font-size: 9.5pt; margin-top: 26pt; }
.yeni-sayfa { page-break-before: always; }
"""


def satir_ici(t):
    t = (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
    return t


def md2html(md):
    out, i = [], 0
    satir = md.split('\n')
    liste = None
    while i < len(satir):
        s = satir[i]
        # tablo
        if s.startswith('|') and i + 1 < len(satir) and re.match(r'^\|[\s:|-]+\|$', satir[i + 1]):
            basliklar = [c.strip() for c in s.strip('|').split('|')]
            out.append('<table><thead><tr>' +
                       ''.join('<th>%s</th>' % satir_ici(c) for c in basliklar) +
                       '</tr></thead><tbody>')
            i += 2
            while i < len(satir) and satir[i].startswith('|'):
                h = [c.strip() for c in satir[i].strip('|').split('|')]
                out.append('<tr>' + ''.join('<td>%s</td>' % satir_ici(c) for c in h) + '</tr>')
                i += 1
            out.append('</tbody></table>')
            continue
        m = re.match(r'^(#{1,4})\s+(.*)', s)
        if m:
            if liste:
                out.append('</%s>' % liste); liste = None
            n = len(m.group(1))
            metin = satir_ici(m.group(2))
            if n == 1 and 'SAĞLIK SKORU' in m.group(2):
                out.append('<h1 class="skor">%s</h1>' % metin)
            else:
                out.append('<h%d>%s</h%d>' % (n, metin, n))
            i += 1; continue
        if s.startswith('> '):
            if liste:
                out.append('</%s>' % liste); liste = None
            blok = []
            while i < len(satir) and satir[i].startswith('> '):
                blok.append(satir[i][2:]); i += 1
            out.append('<blockquote>%s</blockquote>' % satir_ici(' '.join(blok)))
            continue
        m = re.match(r'^\s*[-*]\s+(?:\[[ x]\]\s+)?(.*)', s)
        if m:
            if liste != 'ul':
                if liste: out.append('</%s>' % liste)
                out.append('<ul>'); liste = 'ul'
            out.append('<li>%s</li>' % satir_ici(m.group(1)))
            i += 1; continue
        m = re.match(r'^\s*\d+\.\s+(.*)', s)
        if m:
            if liste != 'ol':
                if liste: out.append('</%s>' % liste)
                out.append('<ol>'); liste = 'ol'
            out.append('<li>%s</li>' % satir_ici(m.group(1)))
            i += 1; continue
        if liste:
            out.append('</%s>' % liste); liste = None
        if s.strip() == '---':
            out.append('<hr>')
        elif s.strip():
            out.append('<p>%s</p>' % satir_ici(s))
        i += 1
    if liste:
        out.append('</%s>' % liste)
    return '\n'.join(out)


def uret(kaynaklar, cikti_pdf, baslik, altbaslik):
    govde = ['<div class="kapak"><h1>%s</h1><div class="alt">%s</div>'
             '<div class="tarih">Hazırlanma: 30 Ağustos 2026</div></div>'
             % (baslik, altbaslik)]
    for n, yol in enumerate(kaynaklar):
        md = io.open(yol, encoding='utf-8').read()
        govde.append('<div%s>' % (' class="yeni-sayfa"' if n else ''))
        govde.append(md2html(md))
        govde.append('</div>')
    html = ('<!doctype html><html lang="tr"><head><meta charset="utf-8">'
            '<title>%s</title><style>%s</style></head><body>%s</body></html>'
            % (baslik, CSS, '\n'.join(govde)))
    gec = os.path.join(KOK, '_rapor.html')
    io.open(gec, 'w', encoding='utf-8').write(html)

    if not os.path.exists(CHROME):
        print('Chromium bulunamadı:', CHROME); return None
    komut = [CHROME, '--headless', '--disable-gpu', '--no-sandbox',
             '--no-pdf-header-footer', '--print-to-pdf-no-header',
             '--print-to-pdf=' + cikti_pdf, 'file:///' + gec.replace('\\', '/')]
    r = subprocess.run(komut, capture_output=True, timeout=180)
    if not os.path.exists(cikti_pdf):
        print('PDF üretilemedi:', r.stderr.decode('utf-8', 'replace')[:400]); return None
    return cikti_pdf


if __name__ == '__main__':
    # 1) Ana rapor + eylem planı
    p = uret([os.path.join(KOK, 'FULL-AUDIT-REPORT.md'),
              os.path.join(KOK, 'ACTION-PLAN.md')],
             os.path.join(KOK, 'huneducation-SEO-denetim.pdf'),
             'huneducation.com', 'Kapsamlı SEO, GEO ve Sağlık Denetimi')
    if p:
        print('  %-42s %.0f KB' % (os.path.basename(p), os.path.getsize(p) / 1024))

    # 2) Uzman bulguları eki
    bulgular = sorted(glob.glob(os.path.join(KOK, 'findings', '*.md')))
    p2 = uret(bulgular, os.path.join(KOK, 'huneducation-SEO-bulgular.pdf'),
              'huneducation.com', 'Uzman bulgu dosyaları (ek)')
    if p2:
        print('  %-42s %.0f KB' % (os.path.basename(p2), os.path.getsize(p2) / 1024))
