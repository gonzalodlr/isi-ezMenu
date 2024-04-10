import os
import uuid  # Módulo para generar identificadores únicos
from flask import Blueprint, jsonify, request
import requests
from ..models.food import Food
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

pdf_bp = Blueprint('pdf', __name__)
i = 0
pdf_name = "menu.pdf"
route = os.path.abspath('../backend/assets/')
pdf_path = os.path.join(route, pdf_name)
@pdf_bp.route('/pdf', methods=['POST'])
def upload_pdf():
    # Obtener los datos del array de objetos enviados desde el frontend
    data = request.json
    # Convierto json en un array de objetos de tipo comida
    foods = []
    for item in data:
        food = Food(
            item['name'],
            item['id'],
            item['description'],
            item['thumbnailURL'],
            item['prepTimeMinutes'],
            item['cookTimeMinutes'],
            item['numServings'],
            item['instructions'],
            item['sections'],
            item['userRatings'],
            item['videoURL'],
            item['price'],
            item['ingredients'],
            item['nutrition']
        )
        foods.append(food)
    # Genero Menu pdf
    generar_pdf(foods)
    # Enlace pdf generado
    link_pdf = 'backend/assets/' + pdf_name
    # Contesto con el link del pdf si todo ha salido bien
    return jsonify({"status": "success", "link": link_pdf})

def generar_pdf(foods):
    c = canvas.Canvas(pdf_path, pagesize=letter)

    for food in foods:
        c.setFont("Helvetica", 12)
        y = 750

        response = requests.get(food.thumbnail_url)
        if response.status_code == 200:
            image_data = response.content

            image_filename = str(uuid.uuid4()) + ".jpg"
            image_path = image_filename

            with open(image_path, 'wb') as f:
                f.write(image_data)

            # Colocar la imagen en el centro de la página arriba
            c.drawImage(image_path, x=(letter[0]-200)/2, y=letter[1]-250, width=200, height=200)
            os.remove(image_path)

            # Colocar el nombre del alimento justo debajo de la imagen
            c.drawCentredString(letter[0]/2, letter[1]-300, "Food Name: {}".format(food.name))
            
            # Colocar la descripción debajo del nombre del alimento
            description_lines = text_wrap(food.description, c)
            y -= len(description_lines) * 15 + 350
            for line in description_lines:
                c.drawCentredString(letter[0]/2, y, line)
                y -= 15

            # Colocar el precio centrado debajo de la descripción
            c.drawCentredString(letter[0]/2, y - 10, "Price: ${:.2f}".format(food.price['portion']))

            c.showPage()

    c.save()

def text_wrap(text, canvas, max_width=500):
    if text is None:
        return ['']  # Devuelve una lista con una cadena vacía si text es None
    
    lines = []
    line = ''
    for word in text.split():
        if canvas.stringWidth(line + ' ' + word) < max_width:
            line += ' ' + word
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines
