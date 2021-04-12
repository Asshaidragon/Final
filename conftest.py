import pytest
from logic import *
import requests


@pytest.fixture()
def requests_users():
    return 'http://127.0.0.1:8080/users/'


@pytest.fixture()
def requests_department():
    return 'http://127.0.0.1:8080/department/'

