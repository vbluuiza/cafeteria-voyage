document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('opcionais-form');
  const hiddenInput = document.getElementById('selected_opcional');

  if (form) {
    form.addEventListener('change', () => {
      const selected = form.querySelector('input[name="opcional"]:checked');
      if (selected && hiddenInput) {
        hiddenInput.value = selected.value;
        console.log("Opção selecionada:", selected.value);
      }
    });
  }

  const textarea = document.querySelector('.notes-textarea');
  const counter = document.querySelector('.mini-text');

  if (textarea && counter) {
    textarea.addEventListener('input', () => {
      const length = textarea.value.length;
      counter.textContent = `${length}/140`;
    });
  }
});