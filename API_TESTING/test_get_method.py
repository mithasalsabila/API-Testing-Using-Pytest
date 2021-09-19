import requests
import pytest 

url = 'https://reqres.in/api/users/2'

response = requests.get(url)

code = response.status_code

def test_get_method_positive():
    assert code == 200

def test_get_method_negative():
    assert code == 201