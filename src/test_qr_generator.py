import requests
import os

url = "https://qr-code-generator20.p.rapidapi.com/generatebasicimage"

API_KEY = os.environ['QR_KEY'] 
querystring = {"data":"https://gonzalodlr.github.io/","size":"500"}

headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "qr-code-generator20.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
print(response)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Specify the file path where you want to save the image
    file_path = "image.jpg"

    # Write the binary content to the file
    with open(file_path, "wb") as image_file:
        image_file.write(response.content)

    print(f"Image saved to {file_path}")
else:
    print(f"Error: {response.status_code} - {response.text}")