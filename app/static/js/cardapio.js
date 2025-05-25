const radioGroup = [
  document.getElementById("radioItem1"),
  document.getElementById("radioItem2"),
  document.getElementById("radioItem3"),
  document.getElementById("radioItem4"),
  document.getElementById("radioItem5")
].filter(Boolean); // Filtra para remover possíveis elementos null/undefined

radioGroup.forEach(item => {
  item.addEventListener('click', () => {
    radioGroup.forEach(i => i.classList.remove('active'));
    item.classList.add('active');
  });
});

function redirectToDetails(card) {
  const title = card.querySelector('.card-title').textContent;
  const description = card.querySelector('.card-text').textContent;
  const price = card.querySelector('.card-price').textContent;
  const imageSrc = card.querySelector('.card-img').src;

  localStorage.setItem('selectedCard', JSON.stringify({
    title,
    description,
    price,
    imageSrc
  }));

  window.location.href = 'item.html';
}