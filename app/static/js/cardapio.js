const radioGroup = [
    document.getElementById("radioItem1"),
    document.getElementById("radioItem2"),
    document.getElementById("radioItem3"),
    document.getElementById("radioItem4"),
    document.getElementById("radioItem5"),
].filter(Boolean); 
radioGroup.forEach((item) => {
    item.addEventListener("click", () => {
        radioGroup.forEach((i) => i.classList.remove("active"));
        item.classList.add("active");
    });
});

function redirectToDetails(card) {
    const productId = card.querySelector("#item_id").textContent.trim();

    if (productId) {
        window.location.href = `/cardapio/item/${productId}`;
    } else {
        console.error("ID do item não encontrado.");
    }
}
