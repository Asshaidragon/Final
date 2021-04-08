import pytest
from requests import *


@pytest.fixture()
def requests_users():
    return Requests_users

# @pytest.fixture()
# def requests_department():
#     return requests_department