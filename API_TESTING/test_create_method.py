import requests
import pytest 

def test_post_method():

    url = 'https://reqres.in/api/users'

    response = requests.post(url)

    code = response.status_code

    assert code == 201