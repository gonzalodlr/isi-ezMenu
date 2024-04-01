from dotenv import load_dotenv
import os
from flask import Flask
from flask_cors import CORS
from .models.food import Food
from .routes.pdf_route import pdf_bp
from .routes.food_route import food_bp

app = Flask(__name__)
CORS(app)
# Load .env file
load_dotenv()

# use the variable names as defined in .env file
api_key = os.getenv("API_KEY")  

# Registrar las rutas de foodroute.py
app.register_blueprint(food_bp)
# Registrar las rutas de pdfroute.py
app.register_blueprint(pdf_bp)

if __name__ == "__main__":
    app.run(debug=True)
