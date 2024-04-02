from dotenv import load_dotenv
import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from .routes.pdf_route import pdf_bp
from .routes.food_route import food_bp
from .routes.qr_route import qr_bp

app = Flask(__name__)
CORS(app)
# Load .env file
load_dotenv()

# use the variable names as defined in .env file
api_key = os.getenv("API_KEY")  

# Registrar las rutas 
app.register_blueprint(food_bp)
app.register_blueprint(pdf_bp)
app.register_blueprint(qr_bp)

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

# Configurar ruta estática frontend
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('../frontend', path)

#Configurar ruta estatica backend assets para el menu
@app.route('/backend/assets/<path:path>')
def static_files_assets(path):
    return send_from_directory('assets', path)

if __name__ == "__main__":
    app.run(debug=True)
