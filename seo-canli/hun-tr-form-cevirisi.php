<?php
/**
 * Plugin Name: Hun Education - Turkce form cevirisi
 * Description: Iletisim formunu Turkce alan adinda Turkce basar. Silmek geri almak icin yeterlidir.
 * Version: 1.1
 *
 * NEDEN KODDA
 * Sitedeki tum iletisim formlari TEK bir Elementor 'global widget'ine
 * isaret ediyor: 5245 'Contact Form Template', dili 'en'. Form gosteren
 * 12 Turkce sayfa ve iki sablon (program + universite, ~506 sayfa) bu ayni
 * kaydi cagiriyor; yani tek bir Ingilizce widget her iki sitede de render
 * ediliyor ve sayfalarin kendi kopyalarindaki metinler render'a girmiyor.
 *
 * WPML String Translation bu dizeleri kaydetmis (context elementor-5245)
 * ve cevirileri de var, ama global widget 'render edilen gonderi' olmadigi
 * icin ikame calismiyor.
 *
 * IKI AYRI YER
 * 1. Gorunen HTML: etiket metni bosluklarla sarili geliyor
 *    ("<label ...> Name </label>"), bu yuzden duz dize degistirme yetmez;
 *    etiket icerigi duzenli ifadeyle, bosluklar korunarak degistiriliyor.
 * 2. data-settings ozniteligi: cok adimli form etiketleri JavaScript'e
 *    HTML-kodlu JSON olarak gecirilyor; orada da karsiliklari yaziliyor.
 *
 * Ingilizce alan adi ETKILENMIYOR - filtre yalnizca dil 'tr' iken calisir.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

/** Alan etiketleri. */
function hun_form_etiketleri() {
	return array(
		'Name'    => 'İsim',
		'Email'   => 'E-posta',
		'Phone'   => 'Telefon',
		'Message' => 'Mesaj',
	);
}

/** Duz metin karsiliklari. */
function hun_form_karsiliklar() {
	return array(
		'placeholder="Name"'                    => 'placeholder="İsim"',
		'placeholder="Email (required)"'        => 'placeholder="E-posta (zorunlu)"',
		'placeholder="Phone Number (required)"' => 'placeholder="Telefon Numarası (zorunlu)"',
		'placeholder="Message"'                 => 'placeholder="Mesaj"',
		'>Send</span>'                           => '>Gönder</span>',
		'>Next</span>'                           => '>Sonraki</span>',
		'>Previous</span>'                       => '>Önceki</span>',
		'&quot;step_next_label&quot;:&quot;Next&quot;'         => '&quot;step_next_label&quot;:&quot;Sonraki&quot;',
		'&quot;step_previous_label&quot;:&quot;Previous&quot;' => '&quot;step_previous_label&quot;:&quot;Önceki&quot;',
		'Your submission was successful.'                     => 'Mesajınız başarıyla gönderildi.',
		'Your submission failed because of an error.'         => 'Bir hata oluştu, mesajınız gönderilemedi.',
		'Your submission failed because the form is invalid.' => 'Form hatalı, lütfen alanları kontrol edin.',
		'This field is required.'                            => 'Bu alan zorunludur.',
	);
}

add_filter( 'elementor/widget/render_content', function ( $icerik, $widget ) {
	if ( ! is_object( $widget ) || $widget->get_name() !== 'form' ) { return $icerik; }
	if ( apply_filters( 'wpml_current_language', null ) !== 'tr' ) { return $icerik; }

	// 1) Etiket metni - cevresindeki bosluk korunur
	$etiket = hun_form_etiketleri();
	$icerik = preg_replace_callback(
		'#(<label[^>]*elementor-field-label[^>]*>)(\s*)([^<]*?)(\s*)(</label>)#i',
		function ( $m ) use ( $etiket ) {
			$t = $m[3];
			return $m[1] . $m[2] . ( $etiket[ $t ] ?? $t ) . $m[4] . $m[5];
		},
		$icerik
	);

	// 2) Yer tutucular, buton, data-settings ve mesajlar
	$k = hun_form_karsiliklar();
	return str_replace( array_keys( $k ), array_values( $k ), $icerik );
}, 20, 2 );

/* ------------------------------------------------ eksik gettext cevirileri */
/**
 * Turkce dil dosyalarindaki bosluklari doldurur.
 *
 * Iki yer olculdu:
 * 1. Arsiv sayfalamasi 'Next ->' / '<- Previous' basiyordu. hello-elementor
 *    bunlari cevrilebilir birakmis ama tema tr_TR.mo dosyasinda karsiliklari
 *    yok. Bu 58 katalog merkez sayfasinda gorunuyor.
 * 2. Karusel oklarinin aria-label'lari 'Next slide' / 'Previous slide'
 *    kaliyordu. Ekran okuyucu kullanan ziyaretci icin bu gercek metin.
 *
 * KOSUL: yalnizca .mo dosyasi diziyi HIC cevirmemisse devreye girer
 * ($ceviri === $metin). Mevcut bir cevirinin uzerine yazilmaz.
 * Alan adi kontrolu en basta; gettext her istekte binlerce kez calisir.
 */
function hun_tr_gettext_haritasi() {
	static $h = null;
	if ( $h === null ) {
		$h = array(
			'hello-elementor' => array(
				'Next %s'     => 'Sonraki %s',
				'%s Previous' => '%s Önceki',
			),
			// Karusel oklarinin aria-label'lari elementor-pro'dan geliyor;
			// tr_TR.mo bu dizeleri cevirmemis. Ikisi de listede.
			'elementor' => array(
				'Next slide'     => 'Sonraki slayt',
				'Previous slide' => 'Önceki slayt',
				'Next'           => 'Sonraki',
				'Previous'       => 'Önceki',
			),
			'elementor-pro' => array(
				'Next slide'     => 'Sonraki slayt',
				'Previous slide' => 'Önceki slayt',
				'Next'           => 'Sonraki',
				'Previous'       => 'Önceki',
			),
		);
	}
	return $h;
}

add_filter( 'gettext', function ( $ceviri, $metin, $alan ) {
	if ( $alan !== 'elementor' && $alan !== 'elementor-pro' && $alan !== 'hello-elementor' ) { return $ceviri; }
	if ( $ceviri !== $metin ) { return $ceviri; }
	static $tr = null;
	if ( $tr === null ) { $tr = ( apply_filters( 'wpml_current_language', null ) === 'tr' ); }
	if ( ! $tr ) { return $ceviri; }
	$h = hun_tr_gettext_haritasi();
	return $h[ $alan ][ $metin ] ?? $ceviri;
}, 20, 3 );

/* ------------------------------------- cok adimli form etiketleri (sarmalayici) */
/**
 * step_next_label / step_previous_label widget'in KENDI HTML'inde degil,
 * sarmalayici div'in data-settings ozniteliginde duruyor; render_content
 * filtresi oraya erisemiyor. Bu yuzden ayar, render'dan once degistiriliyor.
 *
 * Bu dizeler su an gorunmuyor (form tek adimli), ama form ileride adimlara
 * bolunurse butonlar Turkce cikar.
 */
add_action( 'elementor/frontend/before_render', function ( $oge ) {
	if ( ! is_object( $oge ) || $oge->get_name() !== 'form' ) { return; }
	if ( apply_filters( 'wpml_current_language', null ) !== 'tr' ) { return; }
	$a = $oge->get_settings();
	if ( isset( $a['step_next_label'] ) && $a['step_next_label'] === 'Next' ) {
		$oge->set_settings( 'step_next_label', 'Sonraki' );
	}
	if ( isset( $a['step_previous_label'] ) && $a['step_previous_label'] === 'Previous' ) {
		$oge->set_settings( 'step_previous_label', 'Önceki' );
	}
} );
