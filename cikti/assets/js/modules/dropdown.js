/* Header açılır menüleri ve mobil akordiyon.

   Masaüstünde işaretçi menünün üzerine gelince açılır, ayrılınca kapanır;
   klavye ve dokunma için tıklama da çalışır. Panel `hidden` ile kapanır,
   böylece kapalıyken erişilebilirlik ağacında da bulunmaz.

   Kapanma gecikmesi: başlıkla panel arasında birkaç piksellik boşluk var,
   fare oradan geçerken menü kapanmasın diye kapanış küçük bir gecikmeyle
   yapılır. Yeniden giriş gecikmeyi iptal eder. */

const KAPANMA_GECIKMESI = 140;

function kur(item) {
  const btn = item.querySelector('.hdr__link--drop');
  const panel = item.querySelector('.hdr__menu');
  if (!btn || !panel) return null;

  let zaman = 0;

  const ac = () => {
    clearTimeout(zaman);
    if (item.classList.contains('is-open')) return;
    panel.hidden = false;
    /* hidden kalkar kalkmaz sınıf eklenirse tarayıcı iki durumu tek
       karede birleştirir ve geçiş çalışmaz. Araya bir reflow koyuyoruz.
       requestAnimationFrame kullanmıyoruz: sekme arka plandayken rAF
       geri çağrıları durur ve menü hiç açılmaz. */
    void panel.offsetWidth;
    item.classList.add('is-open');
    btn.setAttribute('aria-expanded', 'true');
  };

  const kapat = (hemen) => {
    clearTimeout(zaman);
    const bitir = () => {
      item.classList.remove('is-open');
      btn.setAttribute('aria-expanded', 'false');
      /* Geçiş bitmeden hidden verilirse panel bir anda kaybolur */
      setTimeout(() => {
        if (!item.classList.contains('is-open')) panel.hidden = true;
      }, 220);
    };
    if (hemen) bitir();
    else zaman = setTimeout(bitir, KAPANMA_GECIKMESI);
  };

  /* İnce işaretçi (fare) varsa hover ile aç; dokunmatikte yalnız tıklama */
  if (matchMedia('(hover: hover) and (pointer: fine)').matches) {
    item.addEventListener('pointerenter', ac);
    item.addEventListener('pointerleave', () => kapat(false));
  }

  btn.addEventListener('click', () => {
    if (item.classList.contains('is-open')) kapat(true);
    else ac();
  });

  /* Menüden sekmeyle çıkıldığında kapansın */
  item.addEventListener('focusout', (e) => {
    if (!item.contains(e.relatedTarget)) kapat(true);
  });

  item.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && item.classList.contains('is-open')) {
      kapat(true);
      btn.focus();
    }
    /* Aşağı ok: başlıktan ilk kaleme geç */
    if (e.key === 'ArrowDown' && document.activeElement === btn) {
      e.preventDefault();
      ac();
      panel.querySelector('a')?.focus();
    }
  });

  return { item, kapat };
}

export function initDropdowns() {
  const menuler = Array.from(document.querySelectorAll('.hdr__item[data-drop]'))
    .map(kur)
    .filter(Boolean);

  if (menuler.length) {
    /* Dışarı tıklayınca hepsi kapanır */
    document.addEventListener('pointerdown', (e) => {
      menuler.forEach(({ item, kapat }) => {
        if (!item.contains(e.target)) kapat(true);
      });
    });
  }

  /* ---- Mobil akordiyon ---- */
  document.querySelectorAll('.mnav__toggle').forEach((btn) => {
    const panel = document.getElementById(btn.getAttribute('aria-controls'));
    if (!panel) return;
    btn.addEventListener('click', () => {
      const acik = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!acik));
      panel.hidden = acik;
    });
  });
}
