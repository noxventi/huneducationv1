<?php
/**
 * Plugin Name: Hun Education - Course semasi
 * Description: 984 program sayfasina Course yapisal verisi ekler. Yoast'in kendi grafigine baglanir. Silmek geri almak icin yeterlidir.
 * Version: 1.0
 *
 * TASARIM NOTLARI
 *
 * - provider: Hun Education DEGIL, programi veren universite. course_institute
 *   alani her zaman Turkce universite kaydini tutuyor; WPML ile o anki dilin
 *   kaydina cozumleniyor, aksi halde Ingilizce sayfa Turkce universiteye
 *   baglanirdi.
 *
 * - hasCourseInstance BILEREK EKLENMEDI. Google'in Course zengin sonucu bunu
 *   istiyor ama gecerli olmasi icin donem tarihi ya da haftalik yuk gerekiyor;
 *   sitedeki 965 basvuru tarihinin tamami gecmis ve haftalik yuk verisi yok.
 *   Uydurma veri basmaktansa alan atlaniyor. 2026-27 tarihleri girildiginde
 *   bu blok tek seferde eklenecek.
 *
 * - applicationDeadline ayni sebeple atlandi: gecmis tarihi yapisal veri olarak
 *   yayinlamak Google'a dogrulanabilir sekilde yanlis bilgi bildirmek olur.
 *
 * - Aciklamasi olmayan 338 programda aciklama ALAN VERISINDEN uretiliyor
 *   (seviye, universite, sehir, sure, ucret). Uydurma metin degil, mevcut
 *   olgularin cumleye cevrilmesi.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** O anki dil kodu. */
function hun_course_dil() {
	$d = apply_filters( 'wpml_current_language', null );
	return ( $d === 'tr' ) ? 'tr' : 'en';
}

/** Taksonomiden ilk terim adi. */
function hun_course_terim( $post_id, $taksonomi ) {
	$t = wp_get_post_terms( $post_id, $taksonomi, array( 'fields' => 'all' ) );
	if ( is_wp_error( $t ) || empty( $t ) ) {
		return '';
	}
	return html_entity_decode( $t[0]->name, ENT_QUOTES, 'UTF-8' );
}

/**
 * Aciklamasi olmayan programlar icin alan verisinden olgusal aciklama uretir.
 */
function hun_course_uret_aciklama( $tr, $ad, $uni, $sehir, $seviye, $donem, $fiyat, $para ) {
	$p = array();
	if ( $tr ) {
		$p[] = $uni ? sprintf( '%s, %s bünyesinde okutulan bir programdır.', $ad, $uni ) : $ad . '.';
		if ( $seviye ) {
			$p[] = sprintf( 'Seviye: %s.', $seviye );
		}
		if ( $donem ) {
			$p[] = sprintf( 'Program %d dönem sürer.', (int) $donem );
		}
		if ( $sehir ) {
			$p[] = sprintf( 'Eğitim %s şehrinde verilir.', $sehir );
		}
		if ( $fiyat ) {
			$p[] = sprintf( 'Yıllık öğrenim ücreti %s %s.', number_format( (float) $fiyat, 0, ',', '.' ), $para );
		}
	} else {
		$p[] = $uni ? sprintf( '%s is a programme taught at %s.', $ad, $uni ) : $ad . '.';
		if ( $seviye ) {
			$p[] = sprintf( 'Level: %s.', $seviye );
		}
		if ( $donem ) {
			$p[] = sprintf( 'The programme runs for %d semesters.', (int) $donem );
		}
		if ( $sehir ) {
			$p[] = sprintf( 'It is taught in %s, Hungary.', $sehir );
		}
		if ( $fiyat ) {
			$p[] = sprintf( 'Annual tuition is %s %s.', number_format( (float) $fiyat, 0, ',', ',' ), $para );
		}
	}
	return implode( ' ', $p );
}

/**
 * Course dugumunu Yoast grafigine ekler.
 */
add_filter( 'wpseo_schema_graph', function ( $graph, $context ) {
	if ( ! is_singular( 'course' ) ) {
		return $graph;
	}
	$id = get_queried_object_id();
	if ( ! $id ) {
		return $graph;
	}

	$tr    = ( hun_course_dil() === 'tr' );
	$url   = get_permalink( $id );
	$ad    = html_entity_decode( get_the_title( $id ), ENT_QUOTES, 'UTF-8' );
	$ad    = trim( preg_replace( '/\s*[-\x{2013}\x{2014}]\s*$/u', '', $ad ) );

	// --- saglayici universite, DOGRU DILDE ---
	$kurum_ham = (int) get_post_meta( $id, 'course_institute', true );
	$uni_ad    = '';
	$uni_url   = '';
	if ( $kurum_ham ) {
		$cev = apply_filters( 'wpml_object_id', $kurum_ham, 'university', true, $tr ? 'tr' : 'en' );
		$uni = $cev ? get_post( $cev ) : null;
		if ( $uni && $uni->post_status === 'publish' ) {
			$uni_ad  = html_entity_decode( $uni->post_title, ENT_QUOTES, 'UTF-8' );
			$uni_url = get_permalink( $uni );
		}
	}

	$seviye = hun_course_terim( $id, 'course-level' );
	$alan   = hun_course_terim( $id, 'course-category' );
	$sehir  = hun_course_terim( $id, 'course-city' );
	$donem  = (int) get_post_meta( $id, 'course_semesters', true );
	$fiyat  = get_post_meta( $id, 'course_price', true );
	$para   = strtoupper( (string) get_post_meta( $id, 'course_price_currency', true ) );

	// --- aciklama ---
	$govde = get_post_field( 'post_content', $id );
	$govde = trim( wp_strip_all_tags( strip_shortcodes( $govde ) ) );
	if ( mb_strlen( $govde ) < 50 ) {
		$aciklama = hun_course_uret_aciklama( $tr, $ad, $uni_ad, $sehir, $seviye, $donem, $fiyat, $para );
	} else {
		$aciklama = mb_substr( preg_replace( '/\s+/u', ' ', $govde ), 0, 320 );
	}

	$course = array(
		'@type'       => 'Course',
		'@id'         => $url . '#course',
		'name'        => $ad,
		'description' => $aciklama,
		'url'         => $url,
		'inLanguage'  => $tr ? 'tr' : 'en',
	);

	if ( $uni_ad ) {
		$course['provider'] = array(
			'@type' => 'CollegeOrUniversity',
			'name'  => $uni_ad,
			'url'   => $uni_url,
		);
	}
	if ( $seviye ) {
		$course['educationalLevel'] = $seviye;
	}
	if ( $alan ) {
		$course['about'] = $alan;
	}
	if ( $donem > 0 ) {
		// Donem sayisi TOPLAM sure (6 donem = 3 yil). Yariyil = 6 ay.
		$course['timeRequired'] = 'P' . ( $donem * 6 ) . 'M';
	}
	if ( $fiyat && $para ) {
		$course['offers'] = array(
			'@type'         => 'Offer',
			'price'         => (string) (float) $fiyat,
			'priceCurrency' => $para,
			'category'      => $tr ? 'Yıllık öğrenim ücreti' : 'Annual tuition',
			'url'           => $url,
		);
	}
	if ( $sehir ) {
		$course['locationCreated'] = array(
			'@type'   => 'Place',
			'address' => array(
				'@type'           => 'PostalAddress',
				'addressLocality' => $sehir,
				'addressCountry'  => 'HU',
			),
		);
	}

	// WebPage dugumune bagla ki grafik tek parca kalsin
	foreach ( $graph as $i => $dugum ) {
		$t = $dugum['@type'] ?? '';
		$t = is_array( $t ) ? $t : array( $t );
		if ( in_array( 'WebPage', $t, true ) ) {
			$graph[ $i ]['mainEntity'] = array( '@id' => $url . '#course' );
			break;
		}
	}

	$graph[] = $course;
	return $graph;
}, 20, 2 );
