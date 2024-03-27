// Obtener todas las tarjetas
const cards = document.querySelectorAll(".card");
const imageUrl = "./assets/img/burger.jpg"; // URL de la imagen de fondo
const number = 0; // Número de la tarjeta

// Iterar sobre cada tarjeta y modificar sus atributos
cards.forEach((card) => {
  card.style.backgroundImage = `url(${imageUrl})`;
  card.style.backgroundSize = "cover";
  card.style.backgroundPosition = "center";
  card.style.backgroundAttachment = "fixed";
  card.style.backgroundClip = "border-box";
  card.style.backgroundRepeat = "no-repeat";
  card.style.height = "300px";
  card.style.width = "300px";
  card.style.borderRadius = "10px";
  card.style.color = "white";
  card.style.fontWeight = "bold";
  card.style.textAlign = "center";
  card.style.padding = "20px";
  card.style.margin = "20px";
  card.style.display = "flex";
  card.style.justifyContent = "center";
  card.style.alignItems = "center";
  card.style.flexDirection = "column";
  card.style.boxShadow = "0 4px 8px rgba(0,0,0,0.1)";
  card.style.transition = "transform 0.3s";
  card.style.cursor = "pointer";
  card.style.transform = "scale(1)";
  card.style.overflow = "hidden";
    card.style.position = "relative";
});
