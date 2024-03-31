import os, requests
from dotenv import load_dotenv
from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS
from ..models.food import Food
import json

app = Flask(__name__)
CORS(app)
# Load .env file
load_dotenv()

# Use the variable names as defined in .env file
api_key = os.getenv("API_KEY")

def get_soup():
    filename = "../assets/results.json"
    with open(filename, 'r') as file:
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

@app.route('/search-foods', methods=['GET'])
def search_foods():
    searchTerm = request.args.get('searchTerm')
    if searchTerm == "soup":
        foods = get_soup()
        serialized_foods = serialize_food(foods)
        return jsonify(serialized_foods)
    
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
        response.raise_for_status()  # Handle HTTP errors
        data = response.json()        
        food_array = []
        # Obtain each result in an array
        for result in data["results"]:
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
            
            food = Food(name, id, description, thumbnail_url, prep_time_minutes, cook_time_minutes, num_servings, instructions, sections, user_ratings, video_url, price, ingredients, nutrition)
            print(food)
            food_array.append(food)

        serialized_foods = serialize_food(foods)
        return jsonify(serialized_foods)

    except requests.exceptions.RequestException as e:
        # Handle any request error
        return jsonify({"error": str(e)}), 500

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

if __name__ == '__main__':
    app.run(debug=True)
