import requests
from python_repos import create_request

def test_check_status_code():
    assert create_request().status_code == 200