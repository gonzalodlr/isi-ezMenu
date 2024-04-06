import { Food } from './models/food.js';
const URL_BACKEND = 'http://127.0.0.1:5000/';
var pdf_url = "";
/*
const path = require('path');
// Credenciales
require('dotenv').config({ path: path.resolve(__dirname, '.../.env') });
const URL_SERVER = process.env.BACKEND_URL;
console.log(URL_SERVER)
*/

// Cart JS
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
const crearmenu = document.querySelector('.crear-menu');
// QR button hidden until menu is created
const crearqr = document.querySelector('.crear-qr');
crearqr.classList.add('hidden');

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

    //console.log(allProducts);

    showHTML();
  }
});

// Funcion para mostrar  HTML
const showHTML = () => {
  if (!allProducts.length) {
    cartEmpty.classList.remove('hidden');
    rowProduct.classList.add('hidden');
    cartTotal.classList.add('hidden');
    crearmenu.classList.add('hidden');
  } else {
    cartEmpty.classList.add('hidden');
    rowProduct.classList.remove('hidden');
    cartTotal.classList.remove('hidden');
    crearmenu.classList.remove('hidden');
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
// Array de productos
const food_array = []

// Función para limpiar la lista de productos
function limpiarListaProductos() {
  const container = document.querySelector(".container-items");
  container.innerHTML = '';
}

// Funcion que se ejecuta cuando el boton Search es presionado
document.getElementById("searchForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Evitar el comportamiento predeterminado del formulario
  var searchTerm = document.getElementById("searchInput").value;
  limpiarListaProductos();
  buscarComidas(searchTerm);
});

// Funcion que se ejecuta cuando el boton Crear Menu es presionado
crearmenu.addEventListener('click', async function (event) {
  event.preventDefault(); // Evita la recarga de la página
  const food_array_def = [];
  allProducts.forEach(product => {
    food_array.forEach(foodObj => {
      if (product.title === foodObj.name) {
        food_array_def.push(foodObj);
      }

    });
    console.log(food_array_def);
  }
  );
  const requestOptions = {
    method: 'POST',
    body: JSON.stringify(food_array_def),
    headers: {
      'Content-Type': 'application/json',
    },
  };

  // Realizar la solicitud
  try {
    const response = await fetch(URL_BACKEND + 'pdf', requestOptions);
    const data = await response.json();
    
    if (data.status === "success") {
      pdf_url = 'http://127.0.0.1:5000/' + data.link;
      abrirEnlaceEnNuevaPestana(pdf_url);
      document.getElementById("qr_boton").classList.remove("hidden");
    } else {
      console.error("La solicitud no tuvo éxito:", data);
    }
  } catch (error) {
    console.error("Error al realizar la solicitud:", error);
  }
});

function esperar(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Función para realizar la solicitud al backend con el término de búsqueda
function buscarComidas(searchTerm) {
  fetch(URL_BACKEND + 'search-foods?searchTerm=' + searchTerm)
    .then(response => response.json())
    .then(data => {
      const foodList = JSON.parse(data);
      foodList.forEach(food => {
        const foodObj = new Food(food)
        food_array.push(foodObj);
        const p = food.Price;
        const p1 = p.portion;
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
              </div>
              <button class="btn-add-cart">Add to the cart</button>
            </div>
          </article>
        `);

        const container = document.querySelector(".container-items");
        container.append(article);
      })
      const seccionCarrito = document.getElementById('carrito');
      if (seccionCarrito) {
        seccionCarrito.scrollIntoView({ behavior: 'smooth' });
      } else {
        console.error('La sección "carrito" no existe en este archivo HTML.');
      }
    })
    .catch(error => {
      console.error('Error al buscar comidas:', error);
    });
}

function generarQR() {
  fetch(URL_BACKEND + 'qr-generator?url=${pdf_url}')
    .then(response => response.json())
    .then(data => {
      const qrLink = URL_BACKEND + data.link;
      abrirEnlaceEnNuevaPestana(qrLink);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function abrirEnlaceEnNuevaPestana(url) {
  fetch(url)
    .then(response => {
      if (response.ok) {
        window.open(url, '_blank');
      } else {
        console.error('Error al realizar la solicitud:', response.status);
      }
    })
    .catch(error => {
      console.error('Error al realizar la solicitud:', error);
    });
}
const boton_hidden = document.getElementById("qr_boton");
boton_hidden.addEventListener("click", generarQR);