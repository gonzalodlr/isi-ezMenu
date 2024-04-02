import os, requests
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from ..models.food import Food
import json

food_bp = Blueprint('food', __name__)
# Load .env file
load_dotenv()

# Use the variable names as defined in .env file
api_key = os.getenv("API_KEY")
# Ruta de la carpeta 'assets'
route = os.path.abspath('../backend/assets/')

def exits_json(filename):
    # Verificar si la carpeta 'assets' existe
    if os.path.exists(route) and os.path.isdir(route):
        # Lista de archivos en la carpeta 'assets'
        archivos = os.listdir(route)
        # Verificar si hay algún archivo 'search.json'
        if filename + '.json' in archivos:
            return True
        else:
            return False
    else:
        # La carpeta 'assets' no existe
        return False

def search_json_data(filename):
    # Verificar si la carpeta 'assets' existe
    if os.path.exists(route) and os.path.isdir(route):
        # Lista de archivos en la carpeta 'assets'
        archivos = os.listdir(route)

        # Verificar si hay algún archivo 'search.json'
        if filename + '.json' in archivos:
            with open(os.path.join(route, filename + '.json')) as file:
                response = json.load(file)
            results = response.get("results", [])
            foods = []
            for result in results:
                name = result.get("name")
                id = result.get("id")
                description = result.get("description")
                thumbnail_url = result.get("thumbnail_url")
                prep_time_minutes = result.get("prep_time_minutes")
                cook_time_minutes = result.get("cook_time_minutes")
                num_servings = result.get("num_servings")
                instructions = result.get("instructions")
                sections = result.get("sections")
                user_ratings = result.get("user_ratings")
                video_url = result.get("video_url")
                price = result.get("price")
                ingredients = result.get("ingredients")
                nutrition = result.get("nutrition")

                # Crear un objeto de la clase Food
                food = Food(name, id, description, thumbnail_url, prep_time_minutes, cook_time_minutes, num_servings, instructions, sections, user_ratings, video_url, price, ingredients, nutrition)
                # Agregar el objeto a la lista de objetos
                foods.append(food)
            return foods
        else:
            return False
    else:
        # La carpeta 'assets' no existe
        return False

def serialize_food(food_list):
    serialized_food = []
    for food in food_list:
        serialized_food.append({
            "Name": food.get_name(),
            "ID": food.get_id(),
            "Description": food.get_description(),
            "Thumbnail_URL": food.get_thumbnail_url(),
            "Prep Time Minutes": food.get_prep_time_minutes(),
            "Cook Time Minutes": food.get_cook_time_minutes(),
            "Num Servings": food.get_num_servings(),
            "Instructions": food.get_instructions(),
            "Sections": food.get_sections(),
            "User Ratings": food.get_user_ratings(),
            "Video URL": food.get_video_url(),
            "Price": food.get_price(),
            "Ingredients": food.get_ingredients(),
            "Nutrition": food.get_nutrition()
        })
    return json.dumps(serialized_food)

@food_bp.route('/search-foods', methods=['GET'])
def search_foods():
    searchTerm = request.args.get('searchTerm')
    if exits_json(searchTerm):
        foods = search_json_data(searchTerm)
        serialized_foods = serialize_food(foods)
        return jsonify(serialized_foods)
    else:
        url = "https://tasty.p.rapidapi.com/recipes/list"
        querystring = {
            "from": "0",
            "size": "9",
            "q": searchTerm  # Use the provided search term
        }

        headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "tasty.p.rapidapi.com"
        }

        try:
            response = requests.get(url, headers=headers, params=querystring)
            if response.status_code != 200:
                return jsonify({"error": "The request was not successful"}), 500
            # Guarda la respuesta JSON en un archivo
            with open(os.path.join(route, searchTerm + '.json'), 'w') as file:
                json.dump(response.json(), file)
            # Leer el archivo JSON en un array de objetos de la clase Food
            foods = search_json_data(searchTerm)
            serialized_foods = serialize_food(foods)
            return jsonify(serialized_foods)

        except requests.exceptions.RequestException as e:
            # Handle any request error
            return jsonify({"error": str(e)}), 500