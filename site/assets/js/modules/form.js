/* Lead formu: alan bazlı doğrulama (hata metinleri i18n katmanından),
   çift gönderim koruması, UTM/attribution taşıma ve GA4 olay iskeleti
   (PRD §8 ve §13). */

import { t } from '../core/i18n.js';

const track = (name, params = {}) => {
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({ event: name, ...params });
};

const RE_MAIL = /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}$/;
/* Ülke kodu + 7–14 hane; boşluk/parantez/tire serbest */
const RE_TEL = /^\+?[0-9][0-9\s()\-.]{8,18}[0-9]$/;

export function initForm() {
  document.querySelectorAll('[data-lead-form]').forEach(setup);
}

function setup(form) {
  const done = form.querySelector('[data-form-done]');
  const submit = form.querySelector('[type="submit"]');
  let started = false;
  let sent = false;

  fillAttribution(form);

  form.addEventListener(
    'input',
    () => {
      if (started) return;
      started = true;
      track('form_start', { form_type: 'on_gorusme' });
    },
    { once: false }
  );

  /* Alan bazlı doğrulama */
  const rules = {
    ad: (v) => (v.trim().length >= 2 ? '' : t('form.name')),
    tel: (v) => (RE_TEL.test(v.trim()) ? '' : t('form.tel')),
    eposta: (v) => (RE_MAIL.test(v.trim()) ? '' : t('form.mail')),
  };

  const setError = (input, msg) => {
    const box = form.querySelector(`#err-${input.name}`);
    input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    if (box) box.textContent = msg;
    return !msg;
  };

  Object.keys(rules).forEach((name) => {
    const input = form.elements[name];
    if (!input) return;
    input.addEventListener('blur', () => {
      if (input.value.trim()) setError(input, rules[name](input.value));
    });
    input.addEventListener('input', () => {
      if (input.getAttribute('aria-invalid') === 'true') setError(input, rules[name](input.value));
    });
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (sent) return;

    let ok = true;
    let firstBad = null;

    for (const [name, rule] of Object.entries(rules)) {
      const input = form.elements[name];
      if (!input) continue;
      const good = setError(input, rule(input.value));
      if (!good) {
        ok = false;
        firstBad = firstBad || input;
        track('form_error', { field: name, error_type: 'validation' });
      }
    }

    const kvkk = form.elements.kvkk;
    const kvkkErr = form.querySelector('#err-kvkk');
    if (kvkk && !kvkk.checked) {
      ok = false;
      if (kvkkErr) kvkkErr.textContent = t('form.consent');
      firstBad = firstBad || kvkk;
      track('form_error', { field: 'kvkk', error_type: 'consent' });
    } else if (kvkkErr) {
      kvkkErr.textContent = '';
    }

    if (!ok) {
      firstBad?.focus();
      return;
    }

    sent = true;
    submit.disabled = true;
    submit.style.opacity = '0.6';

    /* Üretimde: fetch(...) → CRM + otomatik teyit e-postası */
    track('generate_lead', {
      form_type: 'on_gorusme',
      seviye: form.elements.seviye?.value || '(belirtilmedi)',
      page_path: location.pathname,
    });

    if (done) {
      done.hidden = false;
      done.querySelector('h3')?.focus?.();
    }
  });
}

/* UTM / kaynak bilgisi — kişisel veri içermez, yalnız kampanya bağlamı. */
function fillAttribution(form) {
  const q = new URLSearchParams(location.search);
  const now = {
    kaynak: q.get('utm_source') || (document.referrer ? new URL(document.referrer).hostname : 'direct'),
    medium: q.get('utm_medium') || '',
    campaign: q.get('utm_campaign') || '',
    gclid: q.get('gclid') || '',
  };

  let first;
  try {
    first = JSON.parse(localStorage.getItem('hun_first_touch') || 'null');
    if (!first) {
      first = { ...now, landing: location.pathname, ts: Date.now() };
      localStorage.setItem('hun_first_touch', JSON.stringify(first));
    }
  } catch {
    first = now;
  }

  const set = (name, val) => {
    if (form.elements[name]) form.elements[name].value = val ?? '';
  };
  set('ilk_kaynak', `${first.kaynak}/${first.medium}/${first.campaign}`);
  set('son_kaynak', `${now.kaynak}/${now.medium}/${now.campaign}`);
  set('giris_sayfasi', first.landing || location.pathname);
  set('lead_sayfasi', location.pathname + location.search);
  set('gclid', now.gclid);
  set('ilgi_program', q.get('program') || q.get('alan') || '');
}
