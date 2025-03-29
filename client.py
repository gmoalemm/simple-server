import requests

BASE_URL = "http://127.0.0.1:5000"

# Test home endpoint
response = requests.get(BASE_URL)
print(response.json())
