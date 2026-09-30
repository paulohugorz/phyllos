document.documentElement.classList.add('js');

const page = document.body;
const segment = page.dataset.segment || '';
const variant = page.dataset.variant || '';
const landingPage = page.dataset.landingPage || location.pathname;

window.dataLayer = window.dataLayer || [];

function track(event, details = {}) {
  const payload = {
    event,
    segment,
    variant,
    landing_page: landingPage,
    ...details,
  };
  window.dataLayer.push(payload);
  window.dispatchEvent(new CustomEvent('vereda:experiment', { detail: payload }));
}

track('vereda_landing_view');

document.querySelectorAll('[data-track-cta]').forEach((link) => {
  link.addEventListener('click', () => {
    track('vereda_cta_click', { cta_position: link.dataset.trackCta });
  });
});

const form = document.forms['diagnostico-vereda-lp'];
const formStatus = form?.querySelector('[data-form-status]');
const submitButton = form?.querySelector('[type="submit"]');
const requiredFields = form ? [...form.querySelectorAll('[required]')] : [];

const errorMessages = {
  name: 'Informe seu nome.',
  company: 'Informe o nome da empresa.',
  email: 'Informe um e-mail válido.',
};

function setHiddenField(name, value) {
  const field = form?.elements.namedItem(name);
  if (field) field.value = value;
}

if (form) {
  const params = new URLSearchParams(location.search);
  setHiddenField('segment', segment);
  setHiddenField('variant', variant);
  setHiddenField('landing_page', landingPage);
  for (const key of ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term']) {
    setHiddenField(key, (params.get(key) || '').slice(0, 180));
  }
}

function showFieldError(field) {
  const target = document.getElementById(`${field.id}-error`);
  if (!target) return;
  const invalid = !field.validity.valid;
  field.setAttribute('aria-invalid', String(invalid));
  target.textContent = invalid ? errorMessages[field.name] || 'Revise este campo.' : '';
}

requiredFields.forEach((field) => {
  field.addEventListener('blur', () => showFieldError(field));
  field.addEventListener('input', () => {
    if (field.getAttribute('aria-invalid') === 'true') showFieldError(field);
  });
});

let formStarted = false;
form?.addEventListener('focusin', () => {
  if (formStarted) return;
  formStarted = true;
  track('vereda_form_start');
});

form?.addEventListener('submit', async (event) => {
  event.preventDefault();
  requiredFields.forEach(showFieldError);

  if (!form.checkValidity()) {
    const firstInvalid = requiredFields.find((field) => !field.validity.valid);
    formStatus.textContent = 'Revise os campos indicados antes de enviar.';
    firstInvalid?.focus();
    track('vereda_form_error', { error_type: 'validation' });
    return;
  }

  const localPreview = ['localhost', '127.0.0.1', '[::1]'].includes(location.hostname) || location.protocol === 'file:';
  if (localPreview) {
    formStatus.textContent = 'Prévia local: a solicitação não foi enviada. O processamento será validado no ambiente Netlify.';
    formStatus.tabIndex = -1;
    formStatus.focus();
    return;
  }

  if (submitButton.disabled) return;

  const controller = new AbortController();
  const timeout = window.setTimeout(() => controller.abort(), 20000);
  const originalText = submitButton.textContent;
  submitButton.disabled = true;
  submitButton.textContent = 'Enviando…';
  form.setAttribute('aria-busy', 'true');
  formStatus.textContent = '';

  try {
    const response = await fetch(form.action, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams(new FormData(form)).toString(),
      signal: controller.signal,
    });

    if (!response.ok) throw new Error('Falha no envio');
    const responsePage = await response.text();
    if (!responsePage.includes('data-submission-received')) throw new Error('Resposta inesperada');

    form.reset();
    setHiddenField('segment', segment);
    setHiddenField('variant', variant);
    setHiddenField('landing_page', landingPage);
    formStatus.textContent = 'Solicitação recebida. Usaremos o e-mail informado para continuar a conversa.';
    formStatus.tabIndex = -1;
    formStatus.focus();
    track('vereda_lead_submitted');
  } catch {
    formStatus.textContent = 'Não foi possível confirmar o envio. Seus dados continuam preenchidos. Verifique a conexão e tente novamente.';
    track('vereda_form_error', { error_type: 'network' });
  } finally {
    window.clearTimeout(timeout);
    form.removeAttribute('aria-busy');
    submitButton.disabled = false;
    submitButton.textContent = originalText;
  }
});
