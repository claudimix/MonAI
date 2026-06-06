import requests

reponse = requests.get("https://api.github.com")

print("Code :", reponse.status_code)