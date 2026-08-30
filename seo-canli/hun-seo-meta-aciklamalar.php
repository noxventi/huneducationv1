<?php
/**
 * Plugin Name: Hun Education - Program ve universite meta aciklamalari
 * Description: Aciklamasi olmayan program/universite sayfalarina alan verisinden aciklama uretir. Silmek geri almak icin yeterlidir.
 * Version: 1.0
 *
 * NEDEN
 * Yoast'in course ve university icin metadesc sablonlari BOS. Sonuc: 984
 * programin 846'sinda ve 40 universitenin 7'sinde meta aciklama yok.
 * Olculdu: Turkce program sayfalarinin 18/18'inde bos, Ingilizce 18/6.
 *
 * ELLE YAZILMISA DOKUNULMAZ
 * 138 program ve 33 universitede elle yazilmis Yoast aciklamasi var.
 * Filtre yalnizca gelen deger BOSSA devreye girer; insanin yazdigi metnin
 * uzerine asla yazmaz.
 *
 * UYDURMA YOK
 * Metin yalnizca kayitli alanlardan kurulur: seviye, universite, sehir,
 * donem sayisi, ucret, para birimi, kurulus yili, universite tipi.
 * Verisi olmayan parca cumleye hic girmez.
 *
 * Son basvuru tarihi BILEREK kullanilmadi: 965 tarihin tamami gecmis.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

/** O anki dil Turkce mi. */
function hun_ma_tr() {
	return ( apply_filters( 'wpml_current_language', null ) === 'tr' );
}

/** Taksonomiden ilk terim adi. */
function hun_ma_terim( $id, $tx ) {
	$t = wp_get_post_terms( $id, $tx, array( 'fields' => 'names' ) );
	if ( is_wp_error( $t ) || empty( $t ) ) { return ''; }
	return html_entity_decode( $t[0], ENT_QUOTES, 'UTF-8' );
}

/** Cumleyi 158 karakterde, kelime sinirinda keser. */
function hun_ma_kirp( $s ) {
	$s = trim( preg_replace( '/\s+/u', ' ', $s ) );
	if ( mb_strlen( $s ) <= 158 ) { return $s; }
	$kes = mb_substr( $s, 0, 158 );
	$n = mb_strrpos( $kes, '. ' );
	if ( $n !== false && $n > 80 ) { return mb_substr( $kes, 0, $n + 1 ); }
	$b = mb_strrpos( $kes, ' ' );
	return rtrim( mb_substr( $kes, 0, $b ?: 158 ), " ,;:-·" ) . '.';
}

/** Universitenin yayindaki program sayisi. */
function hun_ma_uni_program_sayisi( $uni_id ) {
	static $bellek = array();
	if ( isset( $bellek[ $uni_id ] ) ) { return $bellek[ $uni_id ]; }
	global $wpdb;
	$n = (int) $wpdb->get_var( $wpdb->prepare(
		"SELECT COUNT(*) FROM {$wpdb->postmeta} pm
		 JOIN {$wpdb->posts} p ON p.ID = pm.post_id AND p.post_type='course' AND p.post_status='publish'
		 WHERE pm.meta_key='course_institute' AND pm.meta_value = %s", (string) $uni_id ) );
	$bellek[ $uni_id ] = $n;
	return $n;
}

add_filter( 'wpseo_metadesc', function ( $aciklama ) {
	// Insanin yazdigi aciklamanin uzerine ASLA yazma
	if ( is_string( $aciklama ) && trim( $aciklama ) !== '' ) { return $aciklama; }
	if ( is_singular( 'course' ) ) { return hun_ma_program_aciklamasi(); }
	if ( is_singular( 'university' ) ) { return hun_ma_universite_aciklamasi(); }
	return $aciklama;
}, 25 );

/** Program sayfasi aciklamasi - yalnizca kayitli alanlardan. */
function hun_ma_program_aciklamasi() {
	$id = get_queried_object_id();
	if ( ! $id ) { return ''; }
	$tr = hun_ma_tr();

	// Saglayici universite, DOGRU DILDE
	$uni_ad = '';
	$ham = (int) get_post_meta( $id, 'course_institute', true );
	if ( $ham ) {
		$cev = apply_filters( 'wpml_object_id', $ham, 'university', true, $tr ? 'tr' : 'en' );
		$u = $cev ? get_post( $cev ) : null;
		if ( $u && $u->post_status === 'publish' ) {
			$uni_ad = html_entity_decode( $u->post_title, ENT_QUOTES, 'UTF-8' );
		}
	}
	$seviye = hun_ma_terim( $id, 'course-level' );
	$sehir  = hun_ma_terim( $id, 'course-city' );
	$donem  = (int) get_post_meta( $id, 'course_semesters', true );
	$fiyat  = get_post_meta( $id, 'course_price', true );
	$para   = strtoupper( (string) get_post_meta( $id, 'course_price_currency', true ) );

	$p = array();
	if ( $tr ) {
		$bas = array();
		if ( $uni_ad ) { $bas[] = $uni_ad; }
		if ( $sehir )  { $bas[] = $sehir; }
		$p[] = ( $bas ? implode( ', ', $bas ) . ' — ' : '' )
		     . 'İngilizce' . ( $seviye ? ' ' . $seviye : '' ) . ' programı.';
		if ( $donem > 0 ) { $p[] = sprintf( '%d dönem.', $donem ); }
		if ( $fiyat && $para ) { $p[] = sprintf( 'Yıllık ücret %s %s.', number_format( (float) $fiyat, 0, ',', '.' ), $para ); }
		$p[] = 'Başvuru şartları ve Hun Education danışmanlığı.';
	} else {
		// Ingilizce metin daha uzun; kapanis cumlesinin 158 sinirinda
		// kirpilmamasi icin bas kisim sikistirildi.
		$bas = ( $seviye ?: 'Degree programme' );
		if ( $uni_ad ) { $bas .= ' at ' . $uni_ad; }
		if ( $sehir )  { $bas .= ', ' . $sehir; }
		$p[] = $bas . ', Hungary.';
		$ikinci = 'Taught in English';
		if ( $donem > 0 ) { $ikinci .= sprintf( ', %d semesters', $donem ); }
		$p[] = $ikinci . '.';
		if ( $fiyat && $para ) { $p[] = sprintf( 'Annual tuition %s %s.', number_format( (float) $fiyat, 0, ',', ',' ), $para ); }
		$p[] = 'Application support from Hun Education.';
	}
	return hun_ma_kirp( implode( ' ', $p ) );
}

/** Universite sayfasi aciklamasi. */
function hun_ma_universite_aciklamasi() {
	$id = get_queried_object_id();
	if ( ! $id ) { return ''; }
	$tr  = hun_ma_tr();
	$ad  = html_entity_decode( get_the_title( $id ), ENT_QUOTES, 'UTF-8' );
	$sehir = trim( (string) get_post_meta( $id, 'university_city', true ) );
	$yil   = trim( (string) get_post_meta( $id, 'university_foundation_year', true ) );
	$tip   = trim( (string) get_post_meta( $id, 'university_type', true ) );
	// Program sayisi Ingilizce kayittan sayilir; katalog tek kaynak
	$en_id = apply_filters( 'wpml_object_id', $id, 'university', true, 'en' );
	$n = hun_ma_uni_program_sayisi( $en_id ?: $id );

	$p = array();
	if ( $tr ) {
		$tip_tr = '';
		if ( stripos( $tip, 'priv' ) !== false ) { $tip_tr = 'özel'; }
		elseif ( $tip !== '' ) { $tip_tr = 'devlet'; }
		$p[] = $ad . ( $sehir ? ', ' . $sehir : '' ) . ' — Macaristan.';
		if ( $yil && $tip_tr ) { $p[] = sprintf( '%s kuruluşlu %s üniversitesi.', $yil, $tip_tr ); }
		elseif ( $yil ) { $p[] = sprintf( '%s kuruluşlu.', $yil ); }
		if ( $n > 0 ) { $p[] = sprintf( 'İngilizce okutulan %d bölüm.', $n ); }
		$p[] = 'Ücretler, başvuru şartları ve Hun Education danışmanlığı.';
	} else {
		$p[] = $ad . ( $sehir ? ' in ' . $sehir : '' ) . ', Hungary.';
		if ( $yil && $tip ) { $p[] = sprintf( 'Founded %s, %s.', $yil, strtolower( $tip ) ); }
		elseif ( $yil ) { $p[] = sprintf( 'Founded %s.', $yil ); }
		if ( $n > 0 ) { $p[] = sprintf( '%d English-taught degree programmes.', $n ); }
		$p[] = 'Tuition, entry requirements and application support from Hun Education.';
	}
	return hun_ma_kirp( implode( ' ', $p ) );
}
