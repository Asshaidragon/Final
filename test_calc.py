import pytest
from calculator import checking_expression
# from main import ExampleApp




@pytest.mark.parametrize("expression, answer", [(["1", "+", "2"], 3),
                                                (["2", "-", "1"], 1),
                                                (["10", "/", "2"], 5),
                                                (["3", "*", "5"], 15),
                                                (["0.25", "+", "0.3"], 0.55),
                                                (["10", "+", "-5"], 5),])
def test_simple_operations(expression, answer):
    assert checking_expression(expression) == answer, "test simple operations failed"


# @pytest.mark.parametrize("expression, answer", [(["2", "+", "10", "/", "3", "-", "-100", "*", "0.01"], 6.333333333333334),
#                                                 (["12345679", "*", "9"], 111111111),
#                                                 (["99999999999999", "*", "99999999999999"], 9999999999999800000000000001),
#                                                 (["967", "/", "-0.2147", "+", "85134", "*", "999", "-", "0", "*", "0.01"], 85044362.04098742)])
# def test_hard_operations(expression, answer):
#     assert checking_expression(expression) == answer, "test hard operations failed"
#
#
# @pytest.mark.parametrize("expression, answer", [(["(", "1", "+", "2", ")"], 3),
#                                                 (["2", "*", "(", "10", "+", "5", ")", "/", "3"], 10),
#                                                 (["(", "(", "(", "(", "1", "+", "1", ")", ")", ")", ")"], 2),
#                                                 (["(", "1", "+", "1", ")", "*", "(", "2", "+", "2", ")"], 8),
#                                                 (["(", "(", "10", "+", "12", ")", "/", "2", ")", "*", "0.01"], 0.11)])
# def test_brackets(expression, answer):
#     assert checking_expression(expression) == answer, "test brackets operations failed"
#
#
# @pytest.mark.parametrize("expression, answer", [(["2", "/", "0"], "Ошибка: Делить на 0 нельзя"),
#                                                 ([], "Ошибка: Введено пустое выражение"),
#                                                 (["(", "+", "-", "/", ")", "*"], "Ошибка: Вы ввели значение без цифр"),
#                                                 (["("], "Ошибка: Количество введенных ( и ) не совпадает"),
#                                                 ([")", "("], "Ошибка: Закрывающая скобка не может быть раньше открывающей"),])
# def test_negative(expression, answer):
#     assert checking_expression(expression) == answer, "test brackets operations failed"





# @pytest.mark.parametrize("expression, answer", [(["2", "/", "0"], "Ошибка: Делить на 0 нельзя")])
# def test_negative(expression, answer):
#     assert checking_expression(expression) == answer, "test brackets operations failed"




# class a():
#     def set(self, name, value):
#         if name == "number":
#             self.number = value
#             return self.number
#
# ex = a()
# print(ex.set("number", 1))
# ee = ExampleApp()
# print(ee.returns("number"))



# @pytest.mark.parametrize("a, b, c", [(1, 2, 3), (2, 2, 4)])
# def test_valid(supply_calc, a, b, c):
    # try:
    #     2 / 0
    # except Exception as e:
    #     assert False, str(e)
    # assert supply_calc.calculate(a, b) == ans, "ppc"


