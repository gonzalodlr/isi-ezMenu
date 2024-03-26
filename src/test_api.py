import requests, os
from dotenv import load_dotenv
import json

# Load .env file
load_dotenv()

# use the variable names as defined in .env file
api_key = os.getenv("API_KEY")  

url = "https://tasty.p.rapidapi.com/recipes/list"
food_name = "soup"
querystring = {"from":"0","size":"10","tags":"under_30_minutes","q":food_name}

headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": "tasty.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring).json()

#function that save the response in a json
filename = "results"
with open(filename, 'w') as file:
    json.dump(response, file)

# Accede a la lista de resultados
results = response.get("results", [])
# Imprime el 'name' de cada elemento en 'results'
for result in results:
    name = result.get("name")
    if name:
        print(name)