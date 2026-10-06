const form = document.querySelector('.request-form');

if (form) {
  const description = form.querySelector('[name="description"]');
  const count = form.querySelector('[data-character-count]');
  const submitButton = form.querySelector('button[type="submit"]');
  const buttonLabel = form.querySelector('[data-button-label]');

  const updateCount = () => {
    count.textContent = `${description.value.length} / 1500`;
  };

  description.addEventListener('input', updateCount);
  updateCount();

  form.addEventListener('submit', (event) => {
    if (!form.checkValidity()) {
      event.preventDefault();
      form.reportValidity();
      return;
    }

    submitButton.disabled = true;
    buttonLabel.textContent = 'Gönderiliyor...';
  });
}