from flask import jsonify
import requests, os
from dotenv import load_dotenv
import json
import assets
from models.food import Food

# Load .env file
load_dotenv()

# use the variable names as defined in .env file
api_key = os.getenv("API_KEY")  

# open assets folder an open the results.json file to read the data of a soup search
filename = "/home/gonzalo/Desktop/Isi/isi-ezMenu/backend/assets/results.json"
with open(filename, 'r') as file:
    response = json.load(file)

# Accede a la lista de resultados
results = response.get("results", [])

# Crear un array de objetos de la clase Food
foods = []
serialized_food = []
# iterador de cada resultado que me cree un objeto de la clase Food
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
    total_ratings = result.get("total_ratings")
    video_url = result.get("video_url")
    price = result.get("price")
    ingredients = result.get("ingredients")
    nutrition = result.get("nutrition")

    # Crear un objeto de la clase Food
    food = Food(name, id, description, thumbnail_url, prep_time_minutes, cook_time_minutes, num_servings, instructions, sections, user_ratings, video_url, price, ingredients, nutrition)
    # Agregar el objeto a la lista de objetos
    foods.append(food)

    # Imprimir los datos de la receta
    print("Name: ", food.get_name())
    print("ID: ", food.get_id())
    print("Description: ", food.get_description())
    print("Thumbnail URL: ", food.get_thumbnail_url())
    print("Prep Time Minutes: ", food.get_prep_time_minutes())
    print("Cook Time Minutes: ", food.get_cook_time_minutes())
    print("Num Servings: ", food.get_num_servings())
    print("Instructions: ", food.get_instructions())
    print("Sections: ", food.get_sections())   
    print("User Ratings: ", food.user_ratings)
    print("Video URL: ", food.video_url)
    print("Price: ", food.price)
    print("Ingredients: ", food.ingredients)
    print("Nutrition: ", food.nutrition)
    print()
    serialized_food.append({
            "Name": food.get_name(),
            "ID": food.get_id(),
            "Description": food.get_description(),
            "Thumbnail URL": food.get_thumbnail_url(),
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

#serialized_foods = serialize_food(foods)
jsonify(serialized_foods)