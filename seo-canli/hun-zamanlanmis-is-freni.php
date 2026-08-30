<?php
/**
 * Plugin Name: Hun Education - Zamanlanmis is freni
 * Description: Action Scheduler ve cron loopback'lerini kisitlar. Silmek geri almak icin yeterlidir.
 *
 * OLCULEN: erisim gunlugunde 1.999 istegin 701'i (%35) sitenin KENDINE
 * attigi loopback istegiydi (UA: WordPress/7.1; tek IP: sunucunun kendisi).
 * Sebep: DISABLE_WP_CRON tanimsiz + Action Scheduler varsayilan olarak ayni
 * anda 5 kuyruk calistiricisi aciyor. Hesabin entry-process siniri 20.
 * Kuyrukta 33 gecikmis, 110 basarisiz is vardi.
 *
 * Zamanlama CALISMAYA DEVAM EDER; yalnizca tek seritten ve daha yavas.
 * KALICI COZUM: wp-config'e DISABLE_WP_CRON true + cPanel'de gercek cron.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }
add_filter( 'action_scheduler_queue_runner_concurrent_batches', function () { return 1; }, 99 );
add_filter( 'action_scheduler_queue_runner_batch_size', function () { return 10; }, 99 );
add_filter( 'action_scheduler_queue_runner_time_limit', function () { return 15; }, 99 );
