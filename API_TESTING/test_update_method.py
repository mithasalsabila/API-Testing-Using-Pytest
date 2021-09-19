import requests
import pytest 

url = 'https://reqres.in/api/users/2'

response = requests.put(url)

code = response.status_code

def test_put_method_positive():
    assert code == 200

def test_put_method_negative():
    assert code == 201