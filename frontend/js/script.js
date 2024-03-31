const btnCart = document.querySelector('.container-cart-icon');
const containerCartProducts = document.querySelector(
	'.container-cart-products'
);

btnCart.addEventListener('click', () => {
	containerCartProducts.classList.toggle('hidden-cart');
});

/* ========================= */
const cartInfo = document.querySelector('.cart-product');
const rowProduct = document.querySelector('.row-product');

// Lista de todos los contenedores de productos
const productsList = document.querySelector('.container-items');

// Variable de arreglos de Productos
let allProducts = [];

const valorTotal = document.querySelector('.total-pagar');

const countProducts = document.querySelector('#contador-productos');

const cartEmpty = document.querySelector('.cart-empty');
const cartTotal = document.querySelector('.cart-total');

productsList.addEventListener('click', e => {
	if (e.target.classList.contains('btn-add-cart')) {
		const product = e.target.parentElement;

		const infoProduct = {
			quantity: 1,
			title: product.querySelector('h2').textContent,
			price: product.querySelector('p').textContent,
		};

		const exits = allProducts.some(
			product => product.title === infoProduct.title
		);

		if (exits) {
			const products = allProducts.map(product => {
				if (product.title === infoProduct.title) {
					product.quantity++;
					return product;
				} else {
					return product;
				}
			});
			allProducts = [...products];
		} else {
			allProducts = [...allProducts, infoProduct];
		}

		showHTML();
	}
});

rowProduct.addEventListener('click', e => {
	if (e.target.classList.contains('icon-close')) {
		const product = e.target.parentElement;
		const title = product.querySelector('p').textContent;

		allProducts = allProducts.filter(
			product => product.title !== title
		);

		console.log(allProducts);

		showHTML();
	}
});

// Funcion para mostrar  HTML
const showHTML = () => {
	if (!allProducts.length) {
		cartEmpty.classList.remove('hidden');
		rowProduct.classList.add('hidden');
		cartTotal.classList.add('hidden');
	} else {
		cartEmpty.classList.add('hidden');
		rowProduct.classList.remove('hidden');
		cartTotal.classList.remove('hidden');
	}

	// Limpiar HTML
	rowProduct.innerHTML = '';

	let total = 0;
	let totalOfProducts = 0;

	allProducts.forEach(product => {
		const containerProduct = document.createElement('div');
		containerProduct.classList.add('cart-product');

		containerProduct.innerHTML = `
            <div class="info-cart-product">
                <span class="cantidad-producto-carrito">${product.quantity}</span>
                <p class="titulo-producto-carrito">${product.title}</p>
                <span class="precio-producto-carrito">${product.price}</span>
            </div>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="icon-close"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M6 18L18 6M6 6l12 12"
                />
            </svg>
        `;

		rowProduct.append(containerProduct);

		total =
			total + parseInt(product.quantity * product.price.slice(1));
		totalOfProducts = totalOfProducts + product.quantity;
	});

	valorTotal.innerText = `$${total}`;
	countProducts.innerText = totalOfProducts;
};
// Obtener todas las tarjetas
const cards = document.querySelectorAll(".card");
const imageUrl = "./assets/img/burger.jpg"; // URL de la imagen de fondo

// Funcion que se ejecuta cuando el boton Search es presionado
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
    console.log(data); // Compruebo respuesta del backend
    const foodList = JSON.parse(data);

    foodList.forEach(food => {
      /*const ima = food.Thumbnail_URL;
          const name = food.Price;
          const n1 = name.consumption_portion;
          console.log(`Nombre del alimento: ${ima}`);*/
      const p = food.Price;
      const p1= p.portion;
        const article = document.createRange().createContextualFragment(`
          <article>
            <div class="item">
              <figure>
                <img
                  src="${food.Thumbnail_URL}"
                  alt="producto"
                />
              </figure>
              <div class="info-product">
                <h2>${food.Name}</h2>
                <p class="price">$${p1}</p>
                <button class="btn-add-cart">Añadir al carrito</button>
              </div>
            </div>
          </article>
        `);
  
        const container = document.querySelector(".container-items"); // Corregí el selector
      container.append(article);
  
      
      })
      const seccionCarrito = document.getElementById('carrito');
      if (seccionCarrito) {
        seccionCarrito.scrollIntoView({ behavior: 'smooth' });
      } else {
        console.error('La sección "carrito" no existe en este archivo HTML.');
      }
    //window.location.href = "carrito.html?foodList=" + encodeURIComponent(JSON.stringify(foodList));
    // Itera sobre la lista de alimentos y obtén el valor del campo "Name"
    /*foodList.forEach(food => {
        const name = food.Price;
        const n1 = name.consumption_portion;
        console.log(`Nombre del alimento: ${n1}`);
    
    });*/
    
  })
  .catch(error => {
      console.error('Error al buscar comidas:', error);
  });
}
