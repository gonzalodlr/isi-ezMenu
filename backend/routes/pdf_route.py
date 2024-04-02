import os
import uuid  # Módulo para generar identificadores únicos
from flask import Blueprint, jsonify, request
import requests
from backend.models.food import Food
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

pdf_bp = Blueprint('pdf', __name__)
i = 0
pdf_name = "menu.pdf"
route = os.path.abspath('../backend/assets/')

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
    generar_pdf(foods, pdf_name)
    # Enlace pdf generado
    link_pdf = route + str(i) + pdf_name
    # Contesto con el link del pdf si todo ha salido bien
    return jsonify({"status": "success", "link": link_pdf})

def generar_pdf(foods, pdf_name):
    c = canvas.Canvas(pdf_name, pagesize=letter)

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

"""
def generar_pdf(foods, pdf_name):
    c = canvas.Canvas(pdf_name, pagesize=letter)
    x = 0
    for food in foods:
        # Descargar la imagen desde la URL
        response = requests.get(food.thumbnail_url)
        if response.status_code == 200:
            # Obtener los datos de la imagen
            image_data = response.content

            # Guardar la imagen en un archivo temporal
            image_path = str(x) + "temp_image.jpg"
            x += 1
            with open(image_path, 'wb') as f:
                f.write(image_data)

            # Insertar la imagen en el PDF
            c.drawImage(image_path, x=100, y=600, width=200, height=200)

            # Eliminar el archivo temporal de la imagen
            os.remove(image_path)

            # Agregar información sobre el alimento
            c.drawString(100, 500, "Food Name: {}".format(food.name))
            c.drawString(100, 480, "Description: {}".format(food.description))
            c.drawString(100, 460, "Price: ${:.2f}".format(food.price['portion']))

            # Agregar un salto de página
            c.showPage()

    # Guardar el PDF
    c.save()
"""