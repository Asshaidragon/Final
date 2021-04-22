import pytest
import requests
import logging

file_log = logging.FileHandler('Log.log')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(file_log, console_out),
                    format='[%(asctime)s | %(levelname)s]: %(message)s',
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)

logging.info('Info message??))')



# py.test -v test_users.py
# py.test -v -n6 test_users.py

@pytest.mark.parametrize("username, department", [("jan", 'HR')])
def test_two_filters(requests_users, username, department):
    assert requests.get('%s?username=%s&department=%s' % (requests_users, username, department)).text == "data: [{'id': '2', 'username': 'jan', 'email': 'jan@ya.ru', 'department': 'HR', 'date_joined': '2020.02.01 13:45'}]", \
        "Checking two filters failed"
        


@pytest.mark.parametrize("username", [("jan")])
def test_username_filter(requests_users, username):
    assert requests.get('%s?username=%s' % (requests_users, username)).text == "data: [{'id': '2', 'username': 'jan', 'email': 'jan@ya.ru', 'department': 'HR', 'date_joined': '2020.02.01 13:45'}]", \
        "Filter check by name failed"


@pytest.mark.parametrize("department", [("QA")])
def test_department_filters(requests_users, department):
    assert requests.get('%s?department=%s' % (requests_users, department)).text == "data: [{'id': '1', 'username': 'van', 'email': 'van@ya.ru', 'department': 'QA', 'date_joined': '2021.04.01 23:45'}]", \
        "Filter check by department failed"


def test_users_non_filters(requests_users):
    assert requests.get(requests_users).text == "data: [{'id': '1', 'username': 'van', 'email': 'van@ya.ru', 'department': 'QA', 'date_joined': '2021.04.01 23:45'}, " \
                                      "{'id': '2', 'username': 'jan', 'email': 'jan@ya.ru', 'department': 'HR', 'date_joined': '2020.02.01 13:45'}, " \
                                      "{'id': '3', 'username': 'pan', 'email': 'pan@ya.ru', 'department': 'DEV', 'date_joined': '2020.02.01 13:45'}, " \
                                      "{'id': '4', 'username': 'dan', 'email': 'dan@ya.ru', 'department': 'HR', 'date_joined': '2020.02.01 13:45'}]", \
        "Filter check by department failed"


def test_department_non_filters(requests_department):
    get = requests.get(requests_department).text
    assert 'HR' in get and 'QA' in get and 'DEV' in get, "Filter check by department failed"
















