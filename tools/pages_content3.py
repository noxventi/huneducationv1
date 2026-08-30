# -*- coding: utf-8 -*-
# Kurumsal sayfalar.



# =====================================================================
# 5) HAKKIMIZDA
# =====================================================================
qa_hak = [
    ("Hun Education ne zaman kuruldu?",
     "<p>Hun Education 1999'dan bu yana Macaristan odaklı akademik danışmanlık yapar ve "
     "Macaristan'daki ilk Türk eğitim danışmanlığı şirketidir. Merkez ofis Budapeşte'dedir.</p>"),
    ("Danışmanlık ücreti üniversite ücretine dahil mi?",
     "<p>Hayır. Danışmanlık hizmet bedeli ile üniversiteye ödenen öğrenim ücreti birbirinden "
     "ayrıdır ve ayrı ayrı belirtilir. Hangi hizmetin kapsama dahil olduğunu ilk görüşmede yazılı "
     "olarak paylaşırız.</p>"),
    ("Öğrenci Macaristan'a gittikten sonra destek devam eder mu?",
     "<p>Evet. Budapeşte'deki merkez ofis; havalimanı karşılama, ikamet kaydı, üniversite kaydı ve "
     "şehir oryantasyonu aşamalarında yanınızdadır. Eğitim süresince aynı danışmana ulaşabilirsiniz.</p>"),
]

body_hak = f'''<div class="alayout">
{toc([('kisa-cevap','Kısa cevap'),('hikaye','Kuruluş ve bugün'),('nasil','Nasıl çalışıyoruz'),
      ('ilkeler','Yayın ve veri ilkelerimiz'),('ofisler','Ofisler'),('sss','Sık sorulan sorular')])}

<article class="prose">

<section id="kisa-cevap" class="answer">
  <span class="answer__label">Kısa cevap</span>
  <p>Hun Education, 1999 yılından bu yana yalnızca Macaristan'da eğitim alanına odaklanan bir
  akademik danışmanlık kurumudur. Ülkede faaliyet gösteren ilk Türk eğitim danışmanlığı şirketi olarak
  yirmi beş yılı aşkın bir deneyime sahibiz.</p>

  <p>Merkez ofisimiz Budapeşte'de bulunur; Ankara, İstanbul, İzmir, Bursa ve Pécs'teki
  temsilciliklerimiz aracılığıyla öğrencilerimize hizmet veririz. Program seçiminden başvuruya, vize
  sürecinden konaklama ve şehir oryantasyonuna kadar her aşamada öğrencilerimizin yanında oluruz.</p>
</section>

<h2 id="hikaye">Kuruluş ve bugün</h2>
{strip('Öğrencilerimizden kareler', [
 ('pilotaj-ogrenciler-pist', 'Pilot gömlekli üç öğrenci, uçuş alanında birlikte',
  'Pilotaj öğrencilerimiz uçuş alanında.'),
 ('budapeste-koprude-ogrenciler', 'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci',
  'Özgürlük Köprüsü’nde öğrencilerimiz.'),
 ('pilotaj-fuar-standi', 'Üniformalı iki öğrenci, bir pilot akademisi fuar standının önünde',
  'Havacılık fuarında öğrencilerimiz.'),
 ('metu-ogrenci-grubu', 'Kampüs bahçesinde toplanmış uluslararası öğrenci grubu',
  'Kampüste uluslararası öğrenciler.'),
 ('obuda-ogrenciler', 'Óbuda Üniversitesi tabelası altında bankta oturan öğrenci grubu',
  'Ders arası.'),
])}
<p>Hun Education 1999'da, Macaristan'da eğitim almak isteyen Türk öğrenciler için tek bir ülkeye
odaklanan bir danışmanlık ihtiyacından doğdu. Bugün de aynı odakla çalışıyoruz: on ülkeye birden
bakmıyor, yalnızca Macaristan'ı takip ediyoruz.</p>
<p>Bu tercihin pratik karşılığı şudur, hangi üniversitenin hangi dönemde ne istediğini, hangi
bölümün mülakatının zorlaştığını ve hangi şehirde kiraların ne yöne gittiğini genel bir yurt dışı
eğitim broşüründen değil, her yıl aynı ülkede çalışarak biliyoruz.</p>

<div class="tablewrap">
<table class="dtable">
  <caption>Kurum bilgileri</caption>
  <thead><tr><th>Alan</th><th>Bilgi</th></tr></thead>
  <tbody>
    <tr><td><b>Şirket unvanı</b></td><td>HUN EDUCATION KFT.</td></tr>
    <tr><td><b>Faaliyet başlangıcı</b></td><td class="num">1999</td></tr>
    <tr><td><b>Merkez ofis</b></td><td>1204 Budapest, Bethlen utca 17, Macaristan</td></tr>
    <tr><td><b>Türkiye temsilcilikleri</b></td><td>Ankara · İstanbul (Kadıköy) · İzmir · Bursa</td></tr>
    <tr><td><b>Macaristan temsilciliği</b></td><td>Pécs</td></tr>
    <tr><td><b>Odak</b></td><td>Yalnızca Macaristan</td></tr>
  </tbody>
</table>
</div>

<h2 id="nasil">Nasıl çalışıyoruz</h2>
{figure('debrecen-ana-bina',
        'Debrecen Üniversitesi’nin sütunlu ana binası ve önündeki havuz',
        'Debrecen Üniversitesi ana binası.')}
<ol class="steps">
  <li><div><h3>Tek danışman, tek dosya</h3><p>Her aday bir danışmana atanır. Süreç boyunca aynı kişiyle konuşursunuz; her seferinde baştan anlatmak zorunda kalmazsınız.</p></div></li>
  <li><div><h3>Elenen seçenekleri de açıklarız</h3><p>Size yalnız uygun programları değil, hangi programın neden elendiğini de söyleriz.</p></div></li>
  <li><div><h3>Kapsam önceden yazılı</h3><p>Hangi hizmetin dahil olduğu, ne zaman başladığı ve danışmanlık bedelinin üniversite ücretinden ayrı olduğu görüşme öncesinde nettir.</p></div></li>
  <li><div><h3>Uçakta bitmez</h3><p>Havalimanı karşılama, ikamet kaydı ve kayıt haftası Budapeşte ekibiyle yürür.</p></div></li>
</ol>

<h2 id="ilkeler">Yayın ve veri ilkelerimiz</h2>
<p>Yurt dışı eğitim alanında en sık karşılaşılan sorun, eski bilgilerin güncelmiş gibi
sunulmasıdır. Bu sitede uyguladığımız kurallar:</p>
<ul>
  <li><b>Her ücretin yanında para birimi ve dönemi vardır.</b> Yıllık mı dönemlik mi olduğu açıkça yazar.</li>
  <li><b>Kaynak ve güncelleme tarihi görünür.</b> Rehber sayfalarının altında kaynak listesi ve değişiklik günlüğü bulunur.</li>
  <li><b>Garanti dili kullanmayız.</b> Kabul kararı üniversiteye, vize kararı konsolosluğa, denklik kararı YÖK'e aittir.</li>
  <li><b>Doğrulanmamış sayı yayınlamayız.</b> Kabul oranı, başarı yüzdesi gibi kanıtlanamayan iddialara yer vermeyiz.</li>
  <li><b>Öğrenci deneyimleri gerçektir.</b> Anonim ya da kurgulanmış referans kullanmayız.</li>
</ul>

<h2 id="ofisler">Ofisler</h2>
<div class="tablewrap">
<table class="dtable">
  <caption>Ofis ve temsilcilikler</caption>
  <thead><tr><th>Konum</th><th>Adres</th></tr></thead>
  <tbody>
    <tr><td><b>Budapeşte (merkez)</b></td><td>1204 Budapest, Bethlen utca 17, Macaristan</td></tr>
    <tr><td><b>Ankara</b></td><td>Kızılay Mah. Menekşe 2 Cad. No: 33/5, Çankaya</td></tr>
    <tr><td><b>İstanbul</b></td><td>Osmanağa Mah. Vahap Bey Sok. No: 10 D: 13, Kadıköy</td></tr>
    <tr><td><b>İzmir</b></td><td>Kıbrıs Şehitleri Cad. Can Yücel Sok. No: 13/4 D: 7, Alsancak</td></tr>
    <tr><td><b>Bursa</b></td><td>Özlüce Bulvarı, Öndül Elite Offices B Blok K: 6 D: 77, Nilüfer</td></tr>
    <tr><td><b>Pécs</b></td><td>Bölge temsilciliği</td></tr>
  </tbody>
</table>
</div>

<h2 id="sss">Sık sorulan sorular</h2>
{faq_block(qa_hak)}

{acta("Tanışalım", "İlk görüşme ücretsizdir ve sizi hiçbir şeye bağlamaz. Akademik geçmişinizi ve hedeflerinizi birlikte değerlendirelim.")}

{related([(S['contact'],"İletişim","Bize ulaşın","Ofisler, telefon, e-posta ve form."),
          (S['edu'],"Rehber","Macaristan'da eğitim","Sistem, şehirler, vize ve denklik."),
          (S['progs'],"Katalog","Program kataloğu","490 programı filtreleyerek karşılaştırın.")])}
</article>
</div>'''

write(S['about'], page(
    S['about'],
    'Hakkımızda: 1999’dan Beri Macaristan Odaklı Danışmanlık | Hun Education',
    "Hun Education, 1999'dan bu yana yalnızca Macaristan'da eğitim alanına odaklanan bir akademik "
    "danışmanlık kurumudur. "
    "Budapeşte merkez ofis, Türkiye temsilcilikleri, çalışma biçimi ve yayın ilkeleri.",
    'Hakkımızda',
    'Yalnızca Macaristan. 1999’dan beri.',
    'On ülkeye birden bakmıyoruz. Tek bir ülkeyi her yıl yeniden öğrenerek biriken bir bilgiyle '
    'çalışıyoruz, ve neyi bilmediğimizi de söylüyoruz.',
    body_hak, S['about'],
    [HOME, ('Hakkımızda', url_of('about'))],
    qa_hak))

# =====================================================================
# 6) İLETİŞİM
# =====================================================================
DANISMANLAR = [
    ('Beyza Kantarcı', 'Budapeşte · Merkez ofis', 'Hazırlık, lisans, yüksek lisans'),
    ('Veli Çınaroğlu', 'Pécs · Macaristan temsilcisi', 'Hazırlık, lisans, yüksek lisans'),
    ('Çağla Nur Türken', 'Debrecen · Nyíregyháza', 'Hazırlık, lisans, yüksek lisans'),
    ('Hacer Çakmak', 'Budapeşte', 'Hazırlık, lisans, yüksek lisans'),
    ('Nesrin Ertaş', 'Ankara', 'Hazırlık, lisans, yüksek lisans'),
    ('Funda Toksoy', 'Ankara', 'Hazırlık, lisans, yüksek lisans'),
    ('Orkun Tokdemir', 'İstanbul · Kadıköy', 'Hazırlık, lisans, yüksek lisans'),
    ('Nur Alpay', 'İzmir', 'Hazırlık, lisans, yüksek lisans'),
    ('Figen Durmaz', 'Bursa', 'Hazırlık, lisans, yüksek lisans'),
    ('Deniz Hızal', 'Çanakkale', 'Hazırlık, lisans, yüksek lisans'),
    ('Ali Yalçın', 'Denizli', 'Hazırlık, lisans, yüksek lisans'),
]
dan_rows = '\n'.join(
    '    <tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % d for d in DANISMANLAR)

body_iletisim = f'''<div class="alayout">
{toc([('form','Ön görüşme talebi'),('kanallar','İletişim kanalları'),('ofisler','Ofisler'),
      ('ekip','Danışman ekibi'),('nezaman','Ne zaman dönüş yapıyoruz')])}

<article class="prose">

<section id="form">
  <h2 style="margin-top:0">Ücretsiz ön görüşme talebi</h2>
  <p>Formu doldurun, size uygun danışmana yönlendirelim. Ön görüşme ücretsizdir ve sizi hiçbir
  şeye bağlamaz.</p>

  <form class="final__form" style="box-shadow:var(--sh-2);border:1px solid var(--line);margin-top:1.2rem" novalidate data-lead-form>
    <div class="final__row">
      <label class="field">
        <span class="field__label">Ad soyad <span class="field__req" aria-hidden="true">*</span></span>
        <input class="field__ctl" name="ad" type="text" autocomplete="name" required aria-describedby="err-ad">
        <span class="field__err" id="err-ad" role="alert"></span>
      </label>
      <label class="field">
        <span class="field__label">Telefon <span class="field__req" aria-hidden="true">*</span></span>
        <input class="field__ctl" name="tel" type="tel" inputmode="tel" placeholder="+90 5XX XXX XX XX" autocomplete="tel" required aria-describedby="err-tel">
        <span class="field__err" id="err-tel" role="alert"></span>
      </label>
    </div>
    <div class="final__row">
      <label class="field">
        <span class="field__label">E-posta <span class="field__req" aria-hidden="true">*</span></span>
        <input class="field__ctl" name="eposta" type="email" autocomplete="email" required aria-describedby="err-eposta">
        <span class="field__err" id="err-eposta" role="alert"></span>
      </label>
      <label class="field">
        <span class="field__label">İlgilendiğiniz seviye</span>
        <select class="field__ctl" name="seviye">
          <option value="">Seçiniz</option><option>Hazırlık</option><option>Lisans</option>
          <option>Yüksek lisans</option><option>Tıp / diş / eczacılık</option><option>Pilotaj</option>
          <option>Henüz emin değilim</option>
        </select>
      </label>
    </div>
    <label class="field">
      <span class="field__label">Mesajınız <span class="field__hint" style="display:inline">(opsiyonel)</span></span>
      <textarea class="field__ctl" name="mesaj" rows="3" placeholder="Hangi bölümü düşünüyorsunuz, hangi dönemde başlamak istiyorsunuz?"></textarea>
    </label>
    <label class="check">
      <input type="checkbox" name="kvkk" required>
      <span>Kişisel verilerimin, ön görüşme talebimi değerlendirmek amacıyla işlenmesini kabul ediyorum.
        <a href=S['privacy'] target="_blank" rel="noopener">KVKK Aydınlatma Metni</a></span>
    </label>
    <span class="field__err" id="err-kvkk" role="alert"></span>
    <button class="btn btn--primary btn--lg final__submit" type="submit" data-magnetic>
      <span class="btn__label"><span data-t="Ücretsiz Ön Görüşme Al">Ücretsiz Ön Görüşme Al</span></span>
    </button>
    <input type="hidden" name="ilk_kaynak"><input type="hidden" name="son_kaynak">
    <input type="hidden" name="giris_sayfasi"><input type="hidden" name="lead_sayfasi">
    <input type="hidden" name="ilgi_program"><input type="hidden" name="gclid">
    <div class="final__done" data-form-done hidden role="status">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>
      <h3>Talebiniz alındı</h3>
      <p>Danışmanımız çalışma saatleri içinde size dönecek. Dilerseniz görüşmeyi hemen WhatsApp'tan sürdürebilirsiniz.</p>
      <a class="btn btn--wa" href="https://wa.me/" data-wa><span class="btn__label"><span data-t="WhatsApp'tan devam et">WhatsApp'tan devam et</span></span></a>
    </div>
  </form>
</section>

<h2 id="kanallar">İletişim kanalları</h2>
{strip('Öğrencilerimizden kareler', [
 ('budapeste-koprude-ogrenciler', 'Budapeşte’de Özgürlük Köprüsü üzerinde iki öğrenci',
  'Özgürlük Köprüsü’nde öğrencilerimiz.'),
 ('pilotaj-fuar-standi', 'Üniformalı iki öğrenci, bir pilot akademisi fuar standının önünde',
  'Havacılık fuarında öğrencilerimiz.'),
 ('metu-ogrenci-grubu', 'Kampüs bahçesinde toplanmış uluslararası öğrenci grubu',
  'Kampüste uluslararası öğrenciler.'),
 ('obuda-ogrenciler', 'Óbuda Üniversitesi tabelası altında bankta oturan öğrenci grubu',
  'Ders arası.'),
])}
<div class="tablewrap">
<table class="dtable">
  <caption>Doğrudan iletişim</caption>
  <thead><tr><th>Kanal</th><th>Bilgi</th><th>Ne zaman</th></tr></thead>
  <tbody>
    <tr><td><b>Telefon</b></td><td class="num"><a href="tel:+36702963531">+36 70 296 35 31</a></td><td>Pazartesi – Cuma · 09:00 – 18:00</td></tr>
    <tr><td><b>E-posta</b></td><td><a href="mailto:info@huneducation.com">info@huneducation.com</a></td><td>Her zaman</td></tr>
    <tr><td><b>WhatsApp</b></td><td><a href="https://wa.me/" data-wa>Mesaj gönderin</a></td><td>Çalışma saatleri içinde yanıt</td></tr>
  </tbody>
</table>
</div>

<h2 id="ofisler">Ofisler</h2>
<div class="tablewrap">
<table class="dtable">
  <caption>Ofis ve temsilcilikler</caption>
  <thead><tr><th>Konum</th><th>Adres</th></tr></thead>
  <tbody>
    <tr><td><b>Budapeşte (merkez)</b></td><td>1204 Budapest, Bethlen utca 17, Macaristan</td></tr>
    <tr><td><b>Ankara</b></td><td>Kızılay Mah. Menekşe 2 Cad. No: 33/5, Çankaya</td></tr>
    <tr><td><b>İstanbul</b></td><td>Osmanağa Mah. Vahap Bey Sok. No: 10 D: 13, Kadıköy</td></tr>
    <tr><td><b>İzmir</b></td><td>Kıbrıs Şehitleri Cad. Can Yücel Sok. No: 13/4 D: 7, Alsancak</td></tr>
    <tr><td><b>Bursa</b></td><td>Özlüce Bulvarı, Öndül Elite Offices B Blok K: 6 D: 77, Nilüfer</td></tr>
  </tbody>
</table>
</div>

<h2 id="ekip">Danışman ekibi</h2>
<p>Talebiniz, hedeflediğiniz seviye ve bulunduğunuz şehre göre aşağıdaki danışmanlardan birine
yönlendirilir.</p>
<div class="tablewrap">
<table class="dtable">
  <caption>Danışmanlar ve görev bölgeleri</caption>
  <thead><tr><th>Danışman</th><th>Bölge</th><th>Uzmanlık</th></tr></thead>
  <tbody>
{dan_rows}
  </tbody>
</table>
</div>
<p class="notice"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/></svg>
Her danışmanın doğrudan telefonu ve e-posta adresi var; sıraya girmeden doğru kişiye
ulaşabilirsiniz. Bize yazın, seviyenize ve şehrinize bakan danışmana yönlendirelim.</p>

<h2 id="nezaman">Ne zaman dönüş yapıyoruz</h2>
<p>Çalışma saatlerimiz <b>Pazartesi – Cuma, 09:00 – 18:00</b> (Orta Avrupa saati). Bu saatler
dışında gelen talepler bir sonraki iş günü değerlendirilir. Başvuru dönemlerinin yoğun olduğu
Nisan–Haziran ve Ekim–Kasım aylarında dönüş süresi uzayabilir; acil konularda WhatsApp en hızlı
kanaldır.</p>

{acta("Sorunuzu yazın, biz arayalım", "Formu doldurmak bir dakikanızı alır. Hangi programın size uygun olduğunu birlikte netleştirelim.")}
</article>
</div>'''

write(S['contact'], page(
    S['contact'],
    'İletişim. Ücretsiz Ön Görüşme | Hun Education',
    "Hun Education ile iletişime geçin: Budapeşte merkez ofis, Ankara, İstanbul, İzmir ve Bursa "
    "temsilcilikleri, telefon, WhatsApp ve ücretsiz ön görüşme formu.",
    'İletişim',
    'Konuşarak başlayalım',
    'Ön görüşme ücretsizdir ve sizi hiçbir şeye bağlamaz. Formu doldurun ya da doğrudan arayın; '
    'talebinizi doğru danışmana yönlendirelim.',
    body_iletisim, S['contact'],
    [HOME, ('İletişim', url_of('contact'))],
    None,
    extra_css='\n<link rel="stylesheet" href="%sassets/css/catalog.css">' % A))
