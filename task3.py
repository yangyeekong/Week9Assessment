#Use the template below to get started
import requests

url = https://api.nationalize.io/?name=nathaniel
response = requests.get(url)

if response.status_code == "ok":
data = response.json("name")
else:
print(f"Error code: {“error code”}")
name = data[index of name]
print(name)