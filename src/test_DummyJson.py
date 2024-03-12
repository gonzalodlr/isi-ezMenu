import requests

url = 'https://dummyjson.com/products'

headers: {
    'Authorization': 'KEY'
}
# Realizar la solicitud GET
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Imprimir los datos obtenidos en formato JSON
    print(response.json())
else:
    print('Error al realizar la solicitud:', response.status_code)

