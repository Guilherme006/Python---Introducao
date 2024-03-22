# Biblioteca Request
# pip install requests==2.31.0

print("\nImportação e uso de um módulo de terceiro")
import requests

url = "https://www.example.com"
responde = requests.get(url)
print(f"Solicitação HTTP para {url} retoronou o status {responde.status_code}")