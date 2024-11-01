import urllib.request
import json


url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json"

with urllib.request.urlopen(url) as response:
    if response.status == 200:
        data = response.read()  # Leer los datos
        json_data = json.loads(data)  # Convertir a diccionario
        print(json_data)
    else:
        print(f"Error: {response.status}")