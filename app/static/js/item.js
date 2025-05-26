const OPTIONS_CONTAINER = document.getAnimationsById('options-container');


document.addEventListener('DOMContentLoaded', () => {
  const cardData = JSON.parse(localStorage.getItem('selectedCard'));

  if (cardData) {
    
    document.getElementById('detail-title').textContent = cardData.title;
    document.getElementById('detail-description').textContent = cardData.description;
    document.getElementById('detail-price').textContent = cardData.price;
    document.getElementById('detail-image').src = cardData.imageSrc;
    document.getElementById('item_id').textContent = cardData.productId;
  }
});

const ITEM_ID = document.getAnimationsById('item_id');