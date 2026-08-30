<?php
/**
 * Plugin Name: Hun Education - Katalog merkez sayfalari
 * Description: course-category / course-level / course-city arsivlerini H1, baslik ve aciklama olarak duzeltir. Silmek geri almak icin yeterlidir.
 * Version: 1.0
 *
 * NEDEN
 * 984 program sayfasi tek bir sayfalanmis /courses/ listesinin arkasinda duruyor.
 * Kataloğun dogal merkez sayfalari - alan, seviye ve sehir arsivleri - zaten var
 * ve calisiyor (her biri 12 program + ozet basiyor) ama:
 *   - H1'leri WordPress varsayilani: "Course City: Debrecen"
 *   - <title>'lari "Debrecen Archives - HunEducation"
 *   - meta aciklamalari yok
 * Bu hallerinin indekslenmesi zarar verirdi. Once sayfalar duzeltiliyor; noindex
 * ancak ondan sonra kaldirilacak.
 *
 * DIL
 * Yoast'in taksonomi baslik sablonlari TEK bir deger tutuyor - iki alan adinda
 * ayni metni basardi. Daha once ayni tuzak metin aciklamalarinda gorulmustu
 * (25 sablonun hepsi Turkce'ydi). Bu yuzden sablon kullanilmiyor; metinler
 * burada o anki dile gore uretiliyor.
 *
 * SEHIR ADLARI
 * course-city terimleri WPML'de cevrilmiyor; iki dilde de "Budapest" yaziyor.
 * Turkce sorgu ise "budapeste universiteleri". Yalnizca Turkce ciktida
 * Turkce karsiligi olan sehirler eslestiriliyor - terim adi degistirilmiyor.
 *
 * TURKCE EK SORUNU
 * "-de/-da" eki sehir adina gore degisir (Budapeste'de, Debrecen'de, Pecs'te,
 * Miscolc'ta). Yanlis ek amator gorunur; bu yuzden ek gerektirmeyen kaliplar
 * secildi: "X Universiteleri ve Bolumleri", "Macaristan'in X sehrindeki...".
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Bu eklentinin ilgilendigi taksonomiler. course-year bilerek disarida: 2024/2025 arsivleri katalogun tamaminin kopyasi. */
function hun_ark_taksonomiler() {
	return array( 'course-category', 'course-level', 'course-city' );
}

/** O anki dil Turkce mi. */
function hun_ark_tr() {
	return ( apply_filters( 'wpml_current_language', null ) === 'tr' );
}

/** Sadece Turkce ciktida kullanilan sehir karsiliklari. Terim adi degismiyor. */
function hun_ark_sehir_tr( $ad ) {
	$k = array(
		'Budapest' => 'Budapeşte',
		'Vienna'   => 'Viyana',
	);
	return $k[ $ad ] ?? $ad;
}

/**
 * YALNIZCA <title> icin kisaltilmis ad. H1 ve aciklama tam adi kullanmaya devam eder.
 * Tek bir alan adi 53 karakter; basligi kacinilmaz olarak 79'a tasiyordu.
 */
function hun_ark_kisa_ad( $ad ) {
	$k = array(
		'Cultural Sciences, Education and Regional Development' => 'Cultural Sciences and Education',
		'Kültür Bilimleri, Eğitim ve Bölgesel Kalkınma'          => 'Kültür Bilimleri ve Eğitim',
	);
	return $k[ $ad ] ?? $ad;
}

/** Sayfadaki terim, yalnizca ilgilendigimiz taksonomilerden biriyse. */
function hun_ark_terim() {
	if ( ! is_tax( hun_ark_taksonomiler() ) ) {
		return null;
	}
	$t = get_queried_object();
	return ( $t instanceof WP_Term ) ? $t : null;
}

/** Terim adi, HTML varliklari cozulmus. */
function hun_ark_ad( $terim, $tr ) {
	$ad = html_entity_decode( $terim->name, ENT_QUOTES, 'UTF-8' );
	if ( $tr && $terim->taxonomy === 'course-city' ) {
		$ad = hun_ark_sehir_tr( $ad );
	}
	return $ad;
}

/* ---------------------------------------------------------------- H1 */

add_filter( 'get_the_archive_title', function ( $baslik ) {
	$terim = hun_ark_terim();
	if ( ! $terim ) {
		return $baslik;
	}
	$tr = hun_ark_tr();
	$ad = hun_ark_ad( $terim, $tr );

	if ( $terim->taxonomy === 'course-city' ) {
		return $tr ? $ad . ' Üniversiteleri ve Bölümleri' : 'Study in ' . $ad . ', Hungary';
	}
	if ( $terim->taxonomy === 'course-level' ) {
		return $tr ? 'Macaristan\'da ' . $ad . ' Programları' : $ad . ' Programmes in Hungary';
	}
	return $tr ? 'Macaristan\'da ' . $ad . ' Bölümleri' : $ad . ' Degrees in Hungary';
}, 20 );

/* ------------------------------------------------------------ <title> */

add_filter( 'wpseo_title', function ( $baslik ) {
	$terim = hun_ark_terim();
	if ( ! $terim ) {
		return $baslik;
	}
	$tr  = hun_ark_tr();
	$ad  = hun_ark_kisa_ad( hun_ark_ad( $terim, $tr ) );
	$son = ' – HunEducation';

	if ( $terim->taxonomy === 'course-city' ) {
		$yeni = $tr ? $ad . ' Üniversite Bölümleri' : 'English-Taught Programmes in ' . $ad;
	} elseif ( $terim->taxonomy === 'course-level' ) {
		$yeni = $tr ? 'Macaristan\'da ' . $ad . ' Programları' : $ad . ' Programmes in Hungary';
	} else {
		// Uzun alan adlari basligi 60 karakterin uzerine tasiyor; o durumda ek atiliyor.
		$ek   = $tr ? ' Bölümleri' : ' Programmes in Hungary';
		$yeni = $tr ? 'Macaristan\'da ' . $ad . $ek : $ad . $ek;
		if ( mb_strlen( $yeni . $son ) > 62 ) {
			$yeni = $tr ? $ad . ' Bölümleri' : $ad . ' Programmes';
		}
	}
	return $yeni . $son;
}, 30 );

/* ------------------------------------------------------- meta aciklama */

add_filter( 'wpseo_metadesc', function ( $aciklama ) {
	$terim = hun_ark_terim();
	if ( ! $terim ) {
		return $aciklama;
	}
	$tr = hun_ark_tr();
	$ad = hun_ark_ad( $terim, $tr );
	$n  = (int) $terim->count;

	if ( $terim->taxonomy === 'course-city' ) {
		return $tr
			? sprintf( 'Macaristan\'ın %s şehrindeki üniversitelerde İngilizce okutulan %d bölüm. Ücretler, başvuru şartları ve Hun Education danışmanlığı.', $ad, $n )
			: sprintf( '%d English-taught degree programmes at universities in %s, Hungary. Tuition, entry requirements and application support from Hun Education.', $n, $ad );
	}
	if ( $terim->taxonomy === 'course-level' ) {
		return $tr
			? sprintf( 'Macaristan üniversitelerinde İngilizce okutulan %d %s programı. Ücretler, başvuru şartları ve Hun Education danışmanlığı.', $n, $ad )
			: sprintf( '%d %s programmes taught in English at Hungarian universities. Tuition, entry requirements and application support from Hun Education.', $n, $ad );
	}
	return $tr
		? sprintf( 'Macaristan üniversitelerinde İngilizce okutulan %d %s bölümü. Ücretler, başvuru şartları ve Hun Education danışmanlığı.', $n, $ad )
		: sprintf( '%d English-taught %s programmes at Hungarian universities. Tuition, entry requirements and application support from Hun Education.', $n, $ad );
}, 30 );

/**
 * Uzun alan adlari aciklamayi 155'in uzerine tasiyabiliyor. Kesme kelime
 * sinirinda yapilir ve cumle yarim birakilmaz: son nokta varsa oraya kadar.
 */
add_filter( 'wpseo_metadesc', function ( $a ) {
	if ( ! hun_ark_terim() || mb_strlen( $a ) <= 158 ) { return $a; }
	$kes = mb_substr( $a, 0, 158 );
	$nokta = mb_strrpos( $kes, '. ' );
	if ( $nokta !== false && $nokta > 90 ) { return mb_substr( $kes, 0, $nokta + 1 ); }
	$bosluk = mb_strrpos( $kes, ' ' );
	return rtrim( mb_substr( $kes, 0, $bosluk ?: 158 ), " ,;:-" ) . '.';
}, 31 );

/* ------------------------------------------ course-city: paylasilan terim duzeltmeleri */
/**
 * course-city ve course-year WPML'de CEVRILMIYOR (taxonomies_sync_option = 0).
 * Terim iki dilde tek kayit oldugu icin get_term_link() hangi alan adini
 * dondurecegi konusunda kararsiz. Olculen sonuc:
 *   - tr.huneducation.com/course-city/debrecen/ kendini
 *     huneducation.com/course-city/debrecen/ adresine canonical'liyordu;
 *     yani Turkce sayfa Google'a 'asil surumum Ingilizce' diyordu.
 *   - Turkce sitemap 8 sehirden 3'unu Ingilizce alan adiyla listeliyordu.
 *   - Iki sayfa arasinda hreflang yoktu; birbirinin kopyasi gorunuyorlardi.
 * Ucu de burada duzeltiliyor. Terim verisine dokunulmuyor - taksonomiyi
 * WPML'de cevrilebilir yapmak 8 terimin ID ve URL'sini degistirirdi.
 */
function hun_ark_dil_kokleri() {
	$a = get_option( 'icl_sitepress_settings' );
	$kok = array( ( $a['default_language'] ?? 'en' ) => untrailingslashit( get_option( 'home' ) ) );
	foreach ( (array) ( $a['language_domains'] ?? array() ) as $kod => $alan ) {
		$alan = preg_replace( '#^https?://#', '', untrailingslashit( $alan ) );
		if ( $alan ) { $kok[ $kod ] = 'https://' . $alan; }
	}
	return $kok;
}

/** Verilen URL'nin yolunu koruyup alan adini o anki dile tasir. */
function hun_ark_ayni_alan( $url ) {
	$kok = hun_ark_dil_kokleri();
	$bu  = hun_ark_tr() ? ( $kok['tr'] ?? null ) : ( $kok['en'] ?? null );
	if ( ! $bu ) { return $url; }
	// Gelen deger yuzde-kodlanmis olabilir; parse_url oyle bir dizede sema goremez.
	if ( strpos( $url, '%3A%2F%2F' ) !== false ) { $url = urldecode( $url ); }
	$p = wp_parse_url( $url );
	if ( empty( $p['path'] ) || empty( $p['host'] ) ) { return $url; }
	return $bu . $p['path'] . ( isset( $p['query'] ) ? '?' . $p['query'] : '' );
}

/**
 * Yoast 27 canonical'i filtreye YUZDE-KODLANMIS geciriyor
 * ('https%3A%2F%2Fhuneducation.com%2F...'), bu yuzden parse_url sema goremeyip
 * tum dizeyi 'path' saniyor. Olculdu, tahmin degil. Bu yuzden gelen deger
 * hic ayristirilmiyor: canonical dogrudan terimin kendisinden kuruluyor.
 */
add_filter( 'wpseo_canonical', function ( $canonical ) {
	if ( ! is_tax( 'course-city' ) ) { return $canonical; }
	$t = get_queried_object();
	if ( ! ( $t instanceof WP_Term ) ) { return $canonical; }
	$bag = get_term_link( $t );
	if ( is_wp_error( $bag ) ) { return $canonical; }
	$p = wp_parse_url( $bag );
	if ( empty( $p['path'] ) ) { return $canonical; }
	$kok = hun_ark_dil_kokleri();
	$bu  = hun_ark_tr() ? ( $kok['tr'] ?? null ) : ( $kok['en'] ?? null );
	return $bu ? $bu . $p['path'] : $canonical;
}, 30 );

add_filter( 'wpseo_sitemap_entry', function ( $girdi, $tip, $nesne ) {
	if ( $tip !== 'term' || ! ( $nesne instanceof WP_Term ) ) { return $girdi; }
	if ( $nesne->taxonomy !== 'course-city' ) { return $girdi; }
	if ( ! is_array( $girdi ) || empty( $girdi['loc'] ) ) { return $girdi; }
	$girdi['loc'] = hun_ark_ayni_alan( $girdi['loc'] );
	return $girdi;
}, 10, 3 );

add_action( 'wp_head', function () {
	if ( ! is_tax( 'course-city' ) ) { return; }
	$t = get_queried_object();
	if ( ! ( $t instanceof WP_Term ) ) { return; }
	$kok = hun_ark_dil_kokleri();
	if ( empty( $kok['en'] ) || empty( $kok['tr'] ) ) { return; }
	$p = wp_parse_url( hun_ark_ayni_alan( get_term_link( $t ) ) );
	if ( empty( $p['path'] ) ) { return; }
	$en = $kok['en'] . $p['path'];
	$tr = $kok['tr'] . $p['path'];
	printf( '<link rel="alternate" hreflang="en" href="%s" />' . "\n", esc_url( $en ) );
	printf( '<link rel="alternate" hreflang="tr" href="%s" />' . "\n", esc_url( $tr ) );
	printf( '<link rel="alternate" hreflang="x-default" href="%s" />' . "\n", esc_url( $en ) );
}, 1 );
