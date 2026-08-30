/* "Neden Hun Education?" — dört sebebin kaydırmayla açılması.

   Modülün tek işi bölümün ilerlemesini (0→1) --wp olarak yazmak;
   sırayı, çizimi ve yükselmeyi CSS yapar. Bu ayrım bilinçli: kart
   sayısı ya da düzen değişirse JS'e dokunmak gerekmez.

   Ölçüm penceresi bölümün üstü ekranın %78'ine geldiğinde başlar,
   altı %62'ye çıkınca biter — yani kartlar okuma alanındayken çizilir,
   ekrandan çıkarken değil.
*/

export function initWhy(scroller) {
  const el = document.querySelector('[data-why]');
  if (!el) return;

  scroller.track(el, {
    start: 'top 78%',
    end: 'bottom 62%',
    var: '--wp',
    smooth: 0.13,
  });
}
