import requests

name = input("Enter name of animal: ")
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': '/fRLricS5LkkRKwnoYQfJg==xR9rhenwOdxzldmD'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

# animals = response.json()
# for animal in animals :
#     print(animal["name"],animal["taxonomy"])
# <h2>The animal "goadohjasgfas" doesn't exist.</h2>

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  pass
