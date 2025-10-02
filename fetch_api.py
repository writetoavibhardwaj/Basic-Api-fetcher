import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Name:", data["name"])
    print("Base experience:", data["base_experience"])
    print("Abilities:", [a["ability"]["name"] for a in data["abilities"]])
else:
    print("Error:", response.status_code)
