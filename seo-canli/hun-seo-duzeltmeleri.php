<?php
/**
 * Plugin Name: Hun Education - SEO duzeltmeleri
 * Description: Katalog sayfalamasi icin kendine referans veren canonical ve sayfa numarali baslik. Tek dosya; silmek geri almak icin yeterlidir.
 * Version: 1.0
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

/**
 * /courses/2/ ve /kurslar/2/ WordPress'in kendi sayfalamasi degil, ozel bir
 * yeniden yazma kurali. Yoast bunlari ayni sayfa sanip hepsine /courses/
 * canonical'i basiyordu; Google ise sayfalama URL'lerinin KENDINE canonical
 * vermesini soyluyor (page 2 -> page 1 canonical acikca onerilmiyor).
 * Sayfa 2-25 toplam ~550 benzersiz program bagi tasiyor; bunlari birlestirmek
 * o baglarin degerini dusururdu.
 */
function hun_seo_sayfalama_no() {
    $yol = parse_url( $_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH );
    if ( ! $yol ) { return 0; }
    if ( preg_match( '#^/(?:courses|kurslar)/(\d+)/?$#', $yol, $m ) ) {
        return (int) $m[1];
    }
    return 0;
}

add_filter( 'wpseo_canonical', function ( $canonical ) {
    $n = hun_seo_sayfalama_no();
    if ( $n < 2 ) { return $canonical; }
    return home_url( parse_url( $_SERVER['REQUEST_URI'], PHP_URL_PATH ) );
}, 20 );

add_filter( 'wpseo_title', function ( $baslik ) {
    $n = hun_seo_sayfalama_no();
    if ( $n < 2 ) { return $baslik; }
    $etiket = ( function_exists( 'wpml_get_current_language' ) && wpml_get_current_language() === 'tr' ) ? 'Sayfa ' : 'Page ';
    // Ayirici sc-ndash; ham karakter ya da entity gelebilir. Sayfa etiketi
    // ILK ayiricinin ardina eklenir: 'Courses - Sayfa 2 - HunEducation'.
    $desen = '/(\s*(?:\x{2013}|&#8211;|&ndash;)\s*)/u';
    if ( preg_match( $desen, $baslik, $m, PREG_OFFSET_CAPTURE ) ) {
        $kes = $m[0][1] + strlen( $m[0][0] );
        return substr( $baslik, 0, $kes ) . $etiket . $n . $m[0][0] . substr( $baslik, $kes );
    }
    return $baslik . ' ' . html_entity_decode( '&ndash;' ) . ' ' . $etiket . $n;
}, 20 );

/**
 * Organization dugumunu gercek kurum verisiyle zenginlestirir.
 * Yoast ucretsiz surum yalnizca ad, logo ve sameAs veriyor; adres, telefon,
 * kurulus yili ve uzmanlik alanlari hem Google'in varlik esleştirmesi hem de
 * uretken motorlarin 'bu konuda kim otorite' degerlendirmesi icin gerekli.
 * Veriler dogrulanmis: HUN EDUCATION KFT., Bethlen utca 17, 1204 Budapest.
 */
add_filter( 'wpseo_schema_organization', function ( $veri ) {
    $tr = ( function_exists( 'wpml_get_current_language' ) && wpml_get_current_language() === 'tr' );
    $veri['legalName']    = 'HUN EDUCATION KFT.';
    $veri['foundingDate'] = '1999';
    $veri['email']        = 'info@huneducation.com';
    $veri['telephone']    = '+36-70-296-35-31';
    $veri['address']      = array(
        '@type'           => 'PostalAddress',
        'streetAddress'   => 'Bethlen utca 17',
        'postalCode'      => '1204',
        'addressLocality' => 'Budapest',
        'addressCountry'  => 'HU',
    );
    $veri['areaServed']    = array( 'TR', 'HU' );
    $veri['knowsLanguage'] = array( 'tr', 'en', 'hu' );
    $veri['contactPoint']  = array(
        '@type'             => 'ContactPoint',
        'telephone'         => '+36-70-296-35-31',
        'email'             => 'info@huneducation.com',
        'contactType'       => 'customer service',
        'availableLanguage' => array( 'Turkish', 'English', 'Hungarian' ),
    );
    $veri['description'] = $tr
        ? '1999 yılından bu yana yalnızca Macaristan\'da eğitim alanına odaklanan akademik danışmanlık kurumu.'
        : 'An academic consultancy focused on one country, Hungary, since 1999.';
    $veri['knowsAbout'] = $tr
        ? array( 'Macaristan\'da üniversite eğitimi', 'Macaristan üniversite başvuru şartları', 'Macaristan\'da tıp eğitimi', 'Macaristan\'da pilotaj eğitimi', 'Macaristan\'da yüksek lisans', 'Macaristan üniversite ücretleri', 'Macaristan öğrenci vizesi' )
        : array( 'Studying at a university in Hungary', 'Hungarian university admission requirements', 'Studying medicine in Hungary', 'Pilot training in Hungary', 'Master\'s degrees in Hungary', 'Tuition fees in Hungary', 'Hungarian student visa' );
    // sameAs Yoast ayarlarindan eksik/yanlis geliyordu: YouTube hic cikmiyor,
    // Instagram iki alan adinda da Turkce hesabi gosteriyordu. Dort profilin
    // de yasadigi dogrulandi (HTTP 200); dile gore burada sabitleniyor.
    $veri['sameAs'] = array(
        'https://www.facebook.com/HunEducationGLB',
        $tr ? 'https://www.instagram.com/huneducation_tr/' : 'https://www.instagram.com/huneducation/',
        'https://x.com/huneducation',
        'https://www.youtube.com/channel/UCtjkiFBPE4S-igdJ_GVbFUQ',
    );
    return $veri;
}, 20 );

/**
 * Guvenlik basliklari.
 *
 * .htaccess yerine PHP tarafindan gonderiliyor: yanlis bir .htaccess satiri
 * tum siteyi 500'e dusurur, buradaki hata ise en fazla baslik gondermemekle
 * sonuclanir. CSP BILEREK eklenmedi - Elementor ve Jet eklentileri satir ici
 * script/stil kullaniyor, dar bir CSP sayfayi bozardi.
 */
add_action( 'send_headers', function () {
    if ( is_admin() ) { return; }
    if ( headers_sent() ) { return; }
    // Site tamamen HTTPS ve http->https 301 zaten calisiyor.
    if ( is_ssl() ) {
        header( 'Strict-Transport-Security: max-age=31536000' );
    }
    header( 'X-Content-Type-Options: nosniff' );
    header( 'Referrer-Policy: strict-origin-when-cross-origin' );
    header( 'X-Frame-Options: SAMEORIGIN' );
    header( 'Permissions-Policy: geolocation=(), camera=(), microphone=(), payment=()' );
}, 1 );

/**
 * robots.txt'ye llms.txt isareti.
 *
 * NOT: Buraya once 'Disallow: /wp-admin/' da eklenmisti ama Yoast 27
 * robots ciktisini kendi ayristiricisiyla birlestirip ayni User-agent
 * blogunu tekillestirdigi icin o satir dusuyordu. wp-admin zaten
 * kimlik dogrulama arkasinda ve noindex; siralamaya etkisi yok.
 * Calismayan kod birakilmadi.
 */
add_filter( 'robots_txt', function ( $cikti ) {
    return $cikti . "\n# Uretken motorlar icin site ozeti: " . home_url( '/llms.txt' ) . "\n";
}, 20 );

/**
 * WebSite dugumu: marka adi ve aciklama.
 *
 * alternateName 'Huneducation.com | Macaristan'da Universite Okumak' idi -
 * marka alani anahtar kelime deposu degil. description ise site sloganindan
 * geliyordu ve Turkce; Ingilizce sitede Turkce aciklama varlik anlayisini
 * bozuyor. Slogan iki dilde ortak oldugu icin (String Translation kapali)
 * dogru cozum burada dile gore yazmak.
 */
add_filter( 'wpseo_schema_website', function ( $veri ) {
    $tr = ( function_exists( 'wpml_get_current_language' ) && wpml_get_current_language() === 'tr' );
    $veri['name']          = 'Hun Education';
    $veri['alternateName'] = 'HunEducation';
    $veri['description']   = $tr
        ? 'Macaristan üniversitelerinde İngilizce eğitim veren programlar, başvuru şartları ve ücretler; 1999\'dan beri.'
        : 'English-taught degree programmes at Hungarian universities: admission requirements and fees, since 1999.';
    return $veri;
}, 20 );

/**
 * H1 metnini yalnizca goruntulenen sayfada degistirir.
 *
 * H1 sayfanin kendi icerigi degil; Elementor sablonu 1630'daki
 * theme-post-title widget'i post_title'i basiyor. post_title'i degistirmek
 * menuleri, kirinti yolunu ve tum ic baglanti capa metinlerini de
 * degistirirdi - H1 kazancinin haklı cikarmayacagi bir yayilma.
 * Bu yuzden yalnizca widget CIKTISI hedefleniyor.
 *
 * 'Costs', 'Admission', 'Courses' basliklari hedef sorgu tasimiyordu;
 * <title> etiketleri duzeltildi, H1 de ayni cizgiye getiriliyor.
 */
function hun_seo_h1_haritasi() {
    return array(
        422 => 'Tuition Fees and Living Costs in Hungary',
        322 => 'University Admission Requirements in Hungary',
        199 => 'English-Taught Degree Programmes in Hungary',
        2321 => 'Macaristan\'da Üniversite Bölümleri',
    );
}

add_filter( 'elementor/widget/render_content', function ( $icerik, $widget ) {
    if ( ! is_object( $widget ) || $widget->get_name() !== 'theme-post-title' ) { return $icerik; }
    if ( ! is_singular() ) { return $icerik; }
    $id = get_queried_object_id();
    $harita = hun_seo_h1_haritasi();
    if ( ! isset( $harita[ $id ] ) ) { return $icerik; }
    $eski = get_the_title( $id );
    if ( $eski === '' ) { return $icerik; }
    return str_replace( $eski, esc_html( $harita[ $id ] ), $icerik );
}, 20, 2 );

/**
 * Ingilizce ana sayfanin H1'i.
 *
 * 'Search Your Favorite Course Here' bir arayuz talimatiydi; sitenin en
 * degerli H1'i hicbir sorgu hedeflemiyordu. Yeni metin hem arayuz olarak
 * anlamli (altinda arama formu var) hem de hedef ifadeyi tasiyor.
 * Turkce ana sayfaya DOKUNULMADI: 'Macaristan' ve 'Universite' zaten var.
 */
add_filter( 'elementor/widget/render_content', function ( $icerik, $widget ) {
    if ( ! is_object( $widget ) || $widget->get_name() !== 'heading' ) { return $icerik; }
    if ( $widget->get_id() !== 'bdf27b5' ) { return $icerik; }
    if ( ! is_front_page() ) { return $icerik; }
    $tr = ( function_exists( 'wpml_get_current_language' ) && wpml_get_current_language() === 'tr' );
    if ( $tr ) { return $icerik; }
    return str_replace(
        'Search Your Favorite Course Here',
        'Find Your Programme at a Hungarian University',
        $icerik
    );
}, 20, 2 );

/**
 * TARAMA HIZI FRENI - 30 Agustos 2026
 *
 * OLCULEN OLAY: IndexNow'a 1.110 URL bildirildikten bir dakika sonra trafik
 * 80 istek/dk'dan 480'e cikti (YandexBot 239/dk, bingbot 91/dk). Sayfa
 * onbellegi olmayan ve TTFB'si ~1 sn olan sitede bu saniyede 8 tam PHP
 * render'i demek; barindirma hesabinin kaynak siniri asildi ve site
 * yaklasik 15 dakika boyunca 508 dondu.
 *
 * Yandex ve Bing Crawl-delay direktifini DIKKATE ALIR (Google almaz, ama
 * Google zaten kendi hizini sunucu yanitina gore ayarliyor).
 *
 * BU GECICI BIR ONLEMDIR. Kalici cozum sayfa onbellegi; o devreye girince
 * bu blok kaldirilmali, aksi halde tarama hizini gereksiz yere kisitlar.
 */
add_filter( 'robots_txt', function ( $metin ) {
	$fren = "\n# Tarama hizi freni - sunucu kapasitesi nedeniyle (30.08.2026)\n"
		. "User-agent: YandexBot\nCrawl-delay: 10\n\n"
		. "User-agent: bingbot\nCrawl-delay: 10\n\n"
		. "User-agent: Amazonbot\nCrawl-delay: 10\n\n"
		. "User-agent: SeznamBot\nCrawl-delay: 10\n\n"
		. "User-agent: PetalBot\nCrawl-delay: 20\n\n"
		. "User-agent: SemrushBot\nCrawl-delay: 30\n\n"
		. "User-agent: AhrefsBot\nCrawl-delay: 30\n";
	return $metin . $fren;
}, 20 );
