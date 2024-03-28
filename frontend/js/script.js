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

// Funcion que se ejecuta cuando el boton Search es presionado
/*document.getElementById("searchButton").addEventListener("click", function() {
  var searchTerm = document.getElementById("searchInput").value;
  buscarComidas(searchTerm);
});*/
document.getElementById("searchForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Evitar el comportamiento predeterminado del formulario
  var searchTerm = document.getElementById("searchInput").value;
  buscarComidas(searchTerm);
});

// Función para realizar la solicitud al backend con el término de búsqueda
function buscarComidas(searchTerm) {
  // Hacer la solicitud al backend (aquí iría tu código para hacer la solicitud HTTP)
  // Supongamos que aquí enviamos una solicitud GET al endpoint '/buscar-comidas' en el backend
  
  fetch('http://127.0.0.1:5000/search-foods?searchTerm=' + searchTerm) // Suponiendo que el backend escucha en '/buscar-comidas'
  .then(response => response.json())
  .then(data => {
      // Manejar los datos recibidos (en este caso, se supone que recibimos un array de objetos tipo Food)
      console.log(data); // Puedes hacer lo que necesites con los datos
  })
  .catch(error => {
      console.error('Error al buscar comidas:', error);
  });
}
