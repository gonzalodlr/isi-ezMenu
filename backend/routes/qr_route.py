import base64
import json
import re
import uuid
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
import os, requests

qr_bp = Blueprint('qr', __name__)
# Load .env file
load_dotenv()

# Use the variable names as defined in .env file
api_key = os.getenv("API_KEY")

qr_name = "qr_image.jpg"
route = os.path.abspath('../backend/assets/')
qr_path = os.path.join(route, qr_name)

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        contenido = img_file.read()

    # Expresión regular para buscar la cadena base64 en la etiqueta img
    patron = re.compile(r'<img\s+src="data:image\/png;base64,([^"]+)"\s*\/?>')

    # Busca todas las coincidencias en el contenido
    coincidencias = patron.findall(contenido.decode())

    # Variable para almacenar las cadenas base64 encontradas
    cadenas_base64 = ""

    # Recorre todas las coincidencias encontradas
    for coincidencia in coincidencias:
        # Agrega la cadena base64 a la lista
        cadenas_base64 += coincidencia
    return cadenas_base64

@qr_bp.route('/qr-generator', methods=['GET'])
def generate_qr():
    data = request.args.get('url')
    url = "https://qr-code-generator20.p.rapidapi.com/generatebasicimage"

    querystring = {"data":data,"size":"500"}
    headers = {
    	"X-RapidAPI-Key": api_key,
    	"X-RapidAPI-Host": "qr-code-generator20.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    image_filename = "qr_image.jpg"
    image_path = image_filename
    
    # Guardar la respuesta del servidor
    with open(image_path, 'wb') as f:
        f.write(response.content)

    # Obtén los datos de la imagen en formato base64
    base64_image_data = image_to_base64(image_path)

    # Decodifica el contenido Base64
    image_data = base64.b64decode(base64_image_data)

    # Guarda la imagen decodificada en un archivo JPG
    with open(qr_path, "wb") as image_file:
        image_file.write(image_data)

    link_qr = 'backend/assets/' + qr_name
    # borro la imagen temp
    os.remove(image_path)
    # Contesto con el link del pdf si todo ha salido bien
    return jsonify({"status": "success", "link": link_qr})