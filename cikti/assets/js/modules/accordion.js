/* SSS akordiyonu — yükseklik animasyonu CSS'te (grid 0fr→1fr),
   JS yalnız durum ve erişilebilirlik özniteliklerini yönetir. */

export function initAccordion() {
  document.querySelectorAll('[data-acc]').forEach((acc) => {
    const items = Array.from(acc.querySelectorAll('.acc__item'));
    const single = acc.dataset.acc !== 'multi';

    items.forEach((item, i) => {
      const btn = item.querySelector('.acc__btn');
      const panel = item.querySelector('.acc__panel');
      const id = `acc-${Math.random().toString(36).slice(2, 7)}-${i}`;
      panel.id = id;
      btn.setAttribute('aria-controls', id);

      btn.addEventListener('click', () => {
        const open = item.classList.contains('is-open');
        if (single && !open) {
          items.forEach((o) => {
            o.classList.remove('is-open');
            o.querySelector('.acc__btn').setAttribute('aria-expanded', 'false');
          });
        }
        item.classList.toggle('is-open', !open);
        btn.setAttribute('aria-expanded', String(!open));
      });

      btn.addEventListener('keydown', (e) => {
        const dir = { ArrowDown: 1, ArrowUp: -1 }[e.key];
        if (!dir) return;
        e.preventDefault();
        const n = (i + dir + items.length) % items.length;
        items[n].querySelector('.acc__btn').focus();
      });
    });
  });
}
