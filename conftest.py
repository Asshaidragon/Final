import pytest
from logic import *
import requests


@pytest.fixture()
def requests_users():
    return requests.get('http://127.0.0.1:8080/users/').text


# @pytest.fixture()
# def requests_users():
#     return requests.get('http://127.0.0.1:8080/users/?username=%s' % name).text


@pytest.fixture()
def requests_department():
    return requests.get('http://127.0.0.1:8080/department/').text

