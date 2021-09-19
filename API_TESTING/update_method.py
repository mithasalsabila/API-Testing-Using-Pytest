import requests
import json

url = 'https://reqres.in/api/users/2'

response = requests.put(url)

json_response = json.loads(response.text)

print(response.status_code)
print(json_response)