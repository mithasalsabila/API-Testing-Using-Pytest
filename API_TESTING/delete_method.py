import requests

url = 'https://reqres.in/api/users/680'

response = requests.delete(url)

print(response.status_code)
print(response.content)