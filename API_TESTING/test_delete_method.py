import requests
import pytest 

def test_delete_method():

    url = 'https://reqres.in/api/users/2'

    response = requests.delete(url)

    code = response.status_code
    assert code == 204