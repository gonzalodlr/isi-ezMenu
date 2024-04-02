import { Food } from './models/food.js';
/*
const path = require('path');
// Credenciales
require('dotenv').config({ path: path.resolve(__dirname, '.../.env') });
const URL_SERVER = process.env.BACKEND_URL;
console.log(URL_SERVER)
*/
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
const crearqr = document.querySelector('.crear-qr');

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
    crearqr.classList.add('hidden');
  } else {
    cartEmpty.classList.add('hidden');
    rowProduct.classList.remove('hidden');
    cartTotal.classList.remove('hidden');
    crearmenu.classList.remove('hidden');
    crearqr.classList.remove('hidden');
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
const food_array = []
// Constante de enlace a pdf
var pdf_url = "";

// Funcion que se ejecuta cuando el boton Search es presionado
document.getElementById("searchForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Evitar el comportamiento predeterminado del formulario
  var searchTerm = document.getElementById("searchInput").value;
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
      'Content-Type': 'application/json', // Tipo de contenido (JSON en este caso)
    },
  };

  // Realizar la solicitud
  try {
    const response = await fetch('http://127.0.0.1:5000/pdf', requestOptions);
    const data = await response.json();

    // Esperar 3 segundos antes de redirigir
    //await esperar(3000);

    if (data.status === "success") {
      pdf_url = 'http://127.0.0.1:5000/' + data.link;
      //window.location.href = pdf_url;
      // Si no se habilita, la nueva pestaña se bloquea
      abrirEnlaceEnNuevaPestana('http://127.0.0.1:5000/' + data.link);
      boton_hidden.style.display = "block";
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
  // Hacer la solicitud al backend (aquí iría tu código para hacer la solicitud HTTP)
  // Supongamos que aquí enviamos una solicitud GET al endpoint '/buscar-comidas' en el backend

  fetch('http://127.0.0.1:5000/search-foods?searchTerm=' + searchTerm) // Suponiendo que el backend escucha en '/buscar-comidas'
    .then(response => response.json())
    .then(data => {
      //console.log(data); // Compruebo respuesta del backend
      const foodList = JSON.parse(data);

      foodList.forEach(food => {
        // creo un objeto de tipo Food con todos los datos de food
        const foodObj = new Food(food)
        // introduzco en el food_array el objeto
        food_array.push(foodObj);
        //console.log(foodObj)
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
const boton_hidden = document.getElementById("qr_boton");
boton_hidden.style.display = "none";

function generarQR() {
  fetch(`http://127.0.0.1:5000/qr-generator?url=${pdf_url}`)
    .then(response => response.json())
    .then(data => {
      // Obtener el enlace del QR generado
      console.log(data)
      const qrLink = "http://127.0.0.1:5000/" + data.link;
      abrirEnlaceEnNuevaPestana(qrLink);
      // Mostrar el enlace o realizar alguna acción con él
      console.log('Enlace al código QR:', qrLink);
      // Aquí puedes usar el enlace, por ejemplo, mostrarlo en una etiqueta <a>
      //document.getElementById('qrLink').innerHTML = `<a href="${qrLink}" target="_blank">Descargar QR</a>`;
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function abrirEnlaceEnNuevaPestana(url) {
  // Realizar una solicitud GET utilizando fetch
  fetch(url)
    .then(response => {
      // Verificar si la solicitud fue exitosa (código de estado 200)
      if (response.ok) {
        // Abrir el enlace en una nueva pestaña utilizando window.open
        window.open(url, '_blank');
      } else {
        // Si la solicitud falla, mostrar un mensaje de error
        console.error('Error al realizar la solicitud:', response.status);
      }
    })
    .catch(error => {
      // Si hay un error al realizar la solicitud, mostrarlo en la consola
      console.error('Error al realizar la solicitud:', error);
    });
}
boton_hidden.addEventListener("click", generarQR);
// Ejemplo de uso
//abrirEnlaceEnNuevaPestana('https://www.ejemplo.com');
