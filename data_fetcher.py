import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

# Check if the API key is loaded
if not API_KEY:
    raise ValueError("API_KEY is not set in the .env file!")

def fetch_data(animal_name):
    """
    Fetches the animal data for the specified 'animal_name'.
    Returns: a list of animals, where each animal is a dictionary:
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    try:
        response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
        animal_info = response.json()
        return animal_info
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None




