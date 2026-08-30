<?php
/**
 * Plugin Name: Hun Education - Onbellek basliklari
 * Description: no-store basligini kaldirir, oturumu bozmadan. Silmek geri almak icin yeterlidir.
 * Version: 1.0
 *
 * SORUN
 * Her sayfa "Cache-Control: no-store, no-cache, must-revalidate" ile donuyordu.
 * Kaynak bir eklenti ayari degil, PHP'nin kendisi: PixelYourSite her on yuz
 * isteginde session_start() cagiriyor; php.ini'de session.cache_limiter=nocache
 * oldugu icin PHP oturum acilirken bu uc direktifi kendiliginden basiyor.
 *
 * NEDEN ONEMLI
 * no-store, Chrome'da geri/ileri onbellegini (bfcache) TAMAMEN kapatan tek
 * direktiftir. Ziyaretci geri tusuna bastiginda sayfa sifirdan kuruluyor:
 * yeni PHP isteği, yeni Elementor cizimi, yeni LCP. Katalogda gezinen bir
 * kullanici bunu her programda yasiyor. Ayrica onune konacak hicbir CDN veya
 * tarayici onbellegi calisamaz.
 *
 * COZUM VE SINIRI
 * Oturuma DOKUNULMUYOR - PixelYourSite izlemesi, JetEngine form akislari ve
 * WPML calismaya devam ediyor. Yalnizca PHP'nin oturum acarken baslik basmasi
 * kapatiliyor (session_cache_limiter('')), yerine acik bir baslik konuyor:
 *
 *   private, max-age=0, must-revalidate
 *
 * "private" ortak onbelleklerin (CDN, vekil) sayfayi saklamasini yasaklar -
 * oturum tasiyan bir yanitin baska kullaniciya servis edilmesi mumkun degil.
 * "max-age=0, must-revalidate" her gezinmede dogrulama ister; yani AG davranisi
 * bugunkuyle ayni kalir. Degisen tek sey bfcache'in acilmasi.
 *
 * Giris yapmis kullanici, yonetim paneli, AJAX ve REST istekleri tamamen
 * disarida birakildi; oralarda WordPress'in kendi nocache_headers()'i gecerli.
 *
 * OLCULEN SONUC (30 Agustos 2026)
 * Canlida donen baslik: "Cache-Control: max-age=0" - buradaki tam dize degil.
 * Sebep: .htaccess'te WP Rocket'tan kalma bir blok var ve Apache'nin
 * mod_expires'i "ExpiresByType text/html access plus 0 seconds" ile PHP'nin
 * bastigi Cache-Control'u ezip yerine max-age=0 yaziyor.
 *
 * BU BILEREK DUZELTILMEDI. Asil hedef - no-store'un kalkmasi - gerceklesti;
 * bfcache artik calisiyor. Geriye kalan tek fark "private" kelimesinin
 * bulunmamasi ve pratikte bir karsiligi yok: ortada CDN yok, yanit Set-Cookie
 * tasiyor ve "public" yok, dolayisiyla ortak onbellekler zaten saklamaz.
 * Bunun icin .htaccess'e dokunmak gerekirdi; canli sitede tek yazim hatasi
 * tum siteyi 500'e dusurur. Sifira yakin kazanc icin alinacak risk degil.
 *
 * Buradaki header() satiri yine de birakildi: .htaccess ileride temizlenirse
 * dogru baslik kendiliginden devreye girer.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/*
 * mu-plugins, normal eklentilerden ONCE yuklenir; bu yuzden PixelYourSite
 * session_start()'a gelmeden once limiter bosaltilmis oluyor.
 */
if ( ! headers_sent() && function_exists( 'session_cache_limiter' ) ) {
	@session_cache_limiter( '' );
}

add_action( 'send_headers', function () {
	if ( headers_sent() ) {
		return;
	}
	if ( is_admin() || is_user_logged_in() ) {
		return;
	}
	if ( ( defined( 'DOING_AJAX' ) && DOING_AJAX ) || ( defined( 'DOING_CRON' ) && DOING_CRON ) ) {
		return;
	}
	if ( defined( 'REST_REQUEST' ) && REST_REQUEST ) {
		return;
	}
	if ( is_404() || is_search() ) {
		return;
	}
	// POST/PUT gibi degistiren istekler onbelleklenmemeli.
	if ( ! isset( $_SERVER['REQUEST_METHOD'] ) || $_SERVER['REQUEST_METHOD'] !== 'GET' ) {
		return;
	}
	header( 'Cache-Control: private, max-age=0, must-revalidate', true );
	header( 'Pragma: ', true ); // PHP'nin bastigi "Pragma: no-cache" kaldirilir
}, 9 );
