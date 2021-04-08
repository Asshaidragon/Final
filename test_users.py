import pytest
from requests import *



# py.test -v test_users.py


@pytest.mark.parametrize("username, department", [("jan", 'HR')])
def test_two_filters(requests_users, username, department):
    assert requests_users.GET('', username, department) == "data: [{'id': '2', 'username': 'jan', 'email': 'jan@ya.ru', 'department': 'HR', 'date_joined': '2020.02.01 13:45'}]", \
        "Checking two filters failed"


@pytest.mark.parametrize("username", [("jan")])
def test_username_filter(requests_users, username):
    assert requests_users.GET('', username) == "data: [{'id': '2', 'username': 'jan', 'email': 'jan@ya.ru', 'department': 'HR', 'date_joined': '2020.02.01 13:45'}]", \
        "Filter check by name failed"


@pytest.mark.parametrize("department", [("QA")])
def test_department_filters(requests_users, department):
    assert requests_users.GET('', '', department) == "data: [{'id': '1', 'username': 'van', 'email': 'van@ya.ru', 'department': 'QA', 'date_joined': '2021.04.01 23:45'}]", \
        "Filter check by department failed"


@pytest.mark.parametrize("", [()])
def test_users_non_filters(requests_users):
    assert requests_users.GET('') == "data: [{'id': '1', 'username': 'van', 'email': 'van@ya.ru', 'department': 'QA', 'date_joined': '2021.04.01 23:45'}, " \
                                      "{'id': '2', 'username': 'jan', 'email': 'jan@ya.ru', 'department': 'HR', 'date_joined': '2020.02.01 13:45'}, " \
                                      "{'id': '3', 'username': 'pan', 'email': 'pan@ya.ru', 'department': 'DEV', 'date_joined': '2020.02.01 13:45'}, " \
                                      "{'id': '4', 'username': 'dan', 'email': 'dan@ya.ru', 'department': 'HR', 'date_joined': '2020.02.01 13:45'}]", \
        "Filter check by department failed"








# @pytest.mark.parametrize("expression, answer", [(["1", "+", "2"], 3),
#                                                 (["2", "-", "1"], 1),
#                                                 (["10", "/", "2"], 5),
#                                                 (["3", "*", "5"], 15),
#                                                 (["0.25", "+", "0.3"], 0.55),
#                                                 (["10", "+", "-5"], 5)])
# def test_simple_operations(expression, answer):
#     assert checking_expression(expression) == answer, "test simple operations failed"








# @pytest.mark.parametrize("a, b, c", [(1, 2, 3), (2, 2, 4)])
# def test_valid(supply_calc, a, b, c):
    # try:
    #     2 / 0
    # except Exception as e:
    #     assert False, str(e)
    # assert supply_calc.calculate(a, b) == ans, "ppc"


