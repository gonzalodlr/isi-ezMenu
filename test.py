import os
from dotenv import load_dotenv


# Load .env file
load_dotenv()

# use the variable names as defined in .env file
api_key = os.getenv("API_KEY")  
print(api_key)