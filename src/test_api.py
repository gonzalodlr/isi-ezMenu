import requests, os

api_key = os.environ.get('API_KEY')

url = "https://tasty.p.rapidapi.com/recipes/list"

querystring = {"from":"0","size":"10","tags":"under_30_minutes","q":"soup"}

headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": "tasty.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring).json()

#print(response.json())
# Accede a la lista de resultados
results = response.get("results", [])
# Imprime el 'name' de cada elemento en 'results'
for result in results:
    name = result.get("name")
    if name:
        print(name)