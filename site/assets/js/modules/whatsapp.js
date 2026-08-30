/* WhatsApp: bulunduğunuz sayfaya göre hazır mesaj (PRD §8).
   Numara CMS'ten gelecek; burada tek bir yerden yönetilir. */

/* Hun Education merkez hat: +36 70 296 35 31 */
const NUMARA = '36702963531';

export function initWhatsApp() {
  const links = document.querySelectorAll('[data-wa]');
  if (!links.length) return;

  const baglam =
    document.querySelector('[data-wa-context]')?.dataset.waContext ||
    document.querySelector('h1')?.textContent?.trim() ||
    document.title.split('|')[0].trim();

  const mesaj =
    `Merhaba, Hun Education web sitesinde "${baglam}" sayfasını inceliyorum. ` +
    `Başvuru koşulları ve güncel ücret hakkında bilgi almak istiyorum.`;

  links.forEach((a) => {
    a.href = `https://wa.me/${NUMARA}?text=${encodeURIComponent(mesaj)}`;
    a.rel = 'noopener';
    a.target = '_blank';
    a.addEventListener('click', () => {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        event: 'whatsapp_click',
        page_path: location.pathname,
        content_name: baglam,
      });
    });
  });
}
