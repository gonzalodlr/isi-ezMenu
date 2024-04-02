import os
from flask import Blueprint, jsonify, request
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from ..models.food import Food

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
    link_pdf = route + i + pdf_name
    # Contesto con el link del pdf si todo ha salido bien
    return jsonify({"status": "success", "link": link_pdf})

def generar_pdf(foods, pdf_name):
    doc = SimpleDocTemplate(i + pdf_name, pagesize=letter)
    styles = getSampleStyleSheet()

    # Estilos personalizados
    estilo_encabezado = styles["Heading1"]
    estilo_texto = styles["BodyText"]
    estilo_titulo = ParagraphStyle(
        name='Titulo',
        fontSize=24,
        leading=28
    )

    data = [['Food Name', 'Description', 'Price', 'Image']]

    for food in foods:
        data.append([food.nombre, food.descripcion, "${:.2f}".format(food.precio), food.foto])

    table = Table(data, colWidths=[2*inch, 3*inch, 1*inch, 1.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    # Agregar Textos
    encabezado = Paragraph("Restaurant Menu", estilo_titulo)
    encabezado.alignment = 1  # 0=left, 1=center, 2=right
    pie_pagina = Paragraph("Thanks for your visit :)", estilo_texto)
    pie_pagina.alignment = 1
    # Construir el documento
    contenido = [encabezado, table, pie_pagina]
    doc.build(contenido)

