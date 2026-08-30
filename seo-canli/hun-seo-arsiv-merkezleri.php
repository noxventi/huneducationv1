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
	$ad  = hun_ark_ad( $terim, $tr );
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
