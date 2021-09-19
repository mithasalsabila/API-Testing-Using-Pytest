import requests
import json

url = 'https://reqres.in/api/users'

response = requests.post(url)
json_response = json.loads(response.text)

print(response.status_code)
print(json_response)