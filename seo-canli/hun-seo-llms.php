<?php
/**
 * Plugin Name: Hun Education - llms.txt
 * Description: Her alan adi için dogru dilde llms.txt uretir. Silmek geri almak için yeterlidir.
 * Version: 1.0
 *
 * NEDEN ELLE
 * Yoast 27.6'nin yerlesik llms.txt uretici WPML'i tanimiyor: iki alan adinda
 * ayni dosyayi sunuyor ve Türkçe sayfalari İngilizce alan adiyla listeliyordu.
 * Uretken motorlara yanlis dil-URL eslesmesi bildirmek, dosyanin hic olmamasindan
 * zararli oldugu için o ozellik kapatildi ve dogrusu burada uretiliyor.
 *
 * ICERIK ILKESI
 * Sayfa listesi elle yazilmaz: sitedeki yayinda olan sayfalardan, o anki dile
 * göre uretilir. Boylece sayfa eklenip cikarildikca dosya kendiliginden guncel
 * kalir. Program ve üniversite listeleri sayilarak ozetlenir; 984 URL'yi buraya
 * dokmenin faydasi yok, sitemap zaten onu yapiyor.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action( 'init', function () {
	add_rewrite_rule( '^llms\.txt$', 'index.php?hun_llms=1', 'top' );
} );

add_filter( 'query_vars', function ( $v ) {
	$v[] = 'hun_llms';
	return $v;
} );

add_action( 'template_redirect', function () {
	if ( ! get_query_var( 'hun_llms' ) ) {
		return;
	}

	$dil = apply_filters( 'wpml_current_language', null );
	$tr  = ( $dil === 'tr' );
	$kok = untrailingslashit( home_url() );

	$onbellek_anahtari = 'hun_llms_txt_' . ( $tr ? 'tr' : 'en' );
	$metin             = get_transient( $onbellek_anahtari );

	if ( $metin === false ) {
		$metin = hun_llms_uret( $tr, $kok );
		set_transient( $onbellek_anahtari, $metin, DAY_IN_SECONDS );
	}

	header( 'Content-Type: text/plain; charset=utf-8' );
	header( 'X-Robots-Tag: noindex' );
	echo $metin; // phpcs:ignore WordPress.Security.EscapeOutput
	exit;
} );

function hun_llms_sayim( $tip ) {
	$q = new WP_Query( array(
		'post_type'              => $tip,
		'post_status'            => 'publish',
		'posts_per_page'         => 1,
		'fields'                 => 'ids',
		'no_found_rows'          => false,
		'update_post_meta_cache' => false,
		'update_post_term_cache' => false,
	) );
	return (int) $q->found_posts;
}

function hun_llms_uret( $tr, $kok ) {
	$program = hun_llms_sayim( 'course' );
	$uni     = hun_llms_sayim( 'university' );

	if ( $tr ) {
		$s   = "# Hun Education\n\n";
		$s  .= "> 1999'dan bu yana yalnızca tek bir ülkeye - Macaristan'a - odaklanan akademik\n";
		$s  .= "> danışmanlık. Uluslararası öğrencileri Macaristan üniversitelerindeki İngilizce\n";
		$s  .= "> programlarla eşleştiriyor, süreci program seçiminden varışa kadar yürütüyoruz.\n\n";
		$s  .= "Varlık: Hun Education (HUN EDUCATION KFT.), Bethlen utca 17, 1204 Budapeşte, Macaristan.\n";
		$s  .= "Kuruluş: 1999. Diller: Türkçe (tr.huneducation.com), İngilizce (huneducation.com).\n";
		$s  .= sprintf( "Kapsam: %d Macaristan üniversitesi, %d program.\n\n", $uni, $program );
		$bolum_baslik = "## Sayfalar\n";
		$son          = "## Notlar\n\n"
			. "- Kabul kararı üniversiteye, vize kararı konsolosluğa, denklik kararı YÖK'e aittir;\n"
			. "  bu site bu sonuçlar için garanti vermez.\n"
			. "- Ücretler yıllıktır ve üniversiteye göre değişir.\n"
			. sprintf( "- Program ve üniversite sayfalarının tam listesi: %s/sitemap_index.xml\n", $kok );
	} else {
		$s   = "# Hun Education\n\n";
		$s  .= "> An academic consultancy focused on one country - Hungary - since 1999.\n";
		$s  .= "> We match international students to English-taught programmes at Hungarian\n";
		$s  .= "> universities and run the process from choosing a programme to arrival.\n\n";
		$s  .= "Entity: Hun Education (HUN EDUCATION KFT.), Bethlen utca 17, 1204 Budapest, Hungary.\n";
		$s  .= "Founded 1999. Languages: English (huneducation.com), Turkish (tr.huneducation.com).\n";
		$s  .= sprintf( "Scope: %d Hungarian universities, %d programmes.\n\n", $uni, $program );
		$bolum_baslik = "## Pages\n";
		$son          = "## Notes\n\n"
			. "- Admission decisions rest with the university, visa decisions with the consulate\n"
			. "  and recognition with the national authority; this site does not guarantee those outcomes.\n"
			. "- Fees are annual and vary by university.\n"
			. sprintf( "- Full list of programme and university pages: %s/sitemap_index.xml\n", $kok );
	}

	$sayfalar = get_posts( array(
		'post_type'              => 'page',
		'post_status'            => 'publish',
		'posts_per_page'         => 40,
		'orderby'                => 'menu_order title',
		'order'                  => 'ASC',
		'suppress_filters'       => false,
		'update_post_term_cache' => false,
	) );

	$satir = array();
	foreach ( $sayfalar as $p ) {
		$url = get_permalink( $p );
		// Baska dilin alan adina dusen kayitlari atla
		if ( strpos( $url, $kok ) !== 0 ) {
			continue;
		}
		$ad  = html_entity_decode( get_the_title( $p ), ENT_QUOTES, 'UTF-8' );
		$acik = get_post_meta( $p->ID, '_yoast_wpseo_metadesc', true );
		$acik = trim( preg_replace( '/\s+/u', ' ', wp_strip_all_tags( (string) $acik ) ) );
		$satir[] = $acik
			? sprintf( '- [%s](%s): %s', $ad, $url, $acik )
			: sprintf( '- [%s](%s)', $ad, $url );
	}

	return $s . $bolum_baslik . "\n" . implode( "\n", $satir ) . "\n\n" . $son;
}

/** Sayfa kaydedilince onbellek dusurulur. */
add_action( 'save_post_page', function () {
	delete_transient( 'hun_llms_txt_tr' );
	delete_transient( 'hun_llms_txt_en' );
} );
