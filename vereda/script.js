document.documentElement.classList.add('js');

const header = document.querySelector('[data-header]');
const menuButton = document.querySelector('[data-menu-button]');
const navigation = document.querySelector('[data-nav]');

function setMenu(open) {
  if (!menuButton || !navigation) return;
  navigation.classList.toggle('is-open', open);
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
  document.body.classList.toggle('menu-open', open);
}

menuButton?.addEventListener('click', () => {
  setMenu(menuButton.getAttribute('aria-expanded') !== 'true');
});

navigation?.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => setMenu(false));
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && navigation?.classList.contains('is-open')) {
    setMenu(false);
    menuButton.focus();
  }
});

document.addEventListener('click', (event) => {
  if (header && !header.contains(event.target)) setMenu(false);
});

window.matchMedia('(min-width: 961px)').addEventListener('change', () => setMenu(false));

document.querySelectorAll('[data-tabs]').forEach((tabsRoot) => {
  const tabs = [...tabsRoot.querySelectorAll('[role="tab"]')];

  function selectTab(selectedTab, moveFocus = false) {
    tabs.forEach((tab) => {
      const active = tab === selectedTab;
      tab.setAttribute('aria-selected', String(active));
      tab.tabIndex = active ? 0 : -1;
      const panel = document.getElementById(tab.getAttribute('aria-controls'));
      if (panel) panel.hidden = !active;
    });
    if (moveFocus) selectedTab.focus();
  }

  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectTab(tab));
    tab.addEventListener('keydown', (event) => {
      let nextIndex;
      if (event.key === 'ArrowRight') nextIndex = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') nextIndex = (index - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') nextIndex = 0;
      if (event.key === 'End') nextIndex = tabs.length - 1;
      if (nextIndex !== undefined) {
        event.preventDefault();
        selectTab(tabs[nextIndex], true);
      }
    });
  });
});

const form = document.forms['diagnostico-vereda'];
const formStatus = document.querySelector('[data-form-status]');
const submitButton = form?.querySelector('[type="submit"]');
const requiredFields = form ? [...form.querySelectorAll('[required]')] : [];

const errorMessages = {
  name: 'Informe seu nome.',
  company: 'Informe o nome da empresa.',
  email: 'Informe um e-mail válido.',
  segment: 'Selecione o segmento da empresa.',
};

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
  field.addEventListener('change', () => showFieldError(field));
});

form?.addEventListener('submit', async (event) => {
  event.preventDefault();
  requiredFields.forEach(showFieldError);

  if (!form.checkValidity()) {
    const firstInvalid = requiredFields.find((field) => !field.validity.valid);
    formStatus.textContent = 'Revise os campos indicados antes de enviar.';
    firstInvalid?.focus();
    return;
  }

  const localPreview = ['localhost', '127.0.0.1', '[::1]'].includes(location.hostname) || location.protocol === 'file:';
  if (localPreview) {
    formStatus.textContent = 'Prévia local: a solicitação não foi enviada. O processamento deve ser verificado no ambiente Netlify antes da publicação.';
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
    const page = await response.text();
    if (!page.includes('data-submission-received')) throw new Error('Resposta inesperada');

    form.reset();
    formStatus.textContent = 'Solicitação recebida. Usaremos o e-mail informado para continuar a conversa.';
    formStatus.tabIndex = -1;
    formStatus.focus();
  } catch {
    formStatus.textContent = 'Não foi possível confirmar o envio. Seus dados continuam preenchidos. Verifique a conexão e tente novamente.';
  } finally {
    window.clearTimeout(timeout);
    form.removeAttribute('aria-busy');
    submitButton.disabled = false;
    submitButton.textContent = originalText;
  }
});
