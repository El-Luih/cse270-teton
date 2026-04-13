import pytest
import requests
 
def test_valid_login_returns_200():
    response = requests.get("http://127.0.0.1:8000/users/?username=admin&password=qwerty")
    assert response.status_code == 200
 
def test_invalid_login_returns_401():
    response = requests.get("http://127.0.0.1:8000/users/?username=admin&password=admin")
    assert response.status_code == 401