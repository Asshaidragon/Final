



#Описывает приоритет операндов для порядка их выполнения
def priority(z):
    if z == "(":
        return 10
    elif z == ")":
        return 100
    elif z in ["*", "/"]:
        return 1
    elif z in ["+", "-"]:
        return 2
    else:
        return ("Ошибка: неизвестный знак")


#проверяет на число
def number(n):
    # print("преобразовываю", n)
    try:
        return int(n)
    except:
        try:
            return float(n)
        except:
            return False



#выполняет математические действия
def calculations(a, b, c):
        if c == "+":
            return b + a
        elif c == "-":
            return b - a
        elif c == "/":
            try:
                return b / a
            except:
                return ("Ошибка: Делить на 0 нельзя")
        elif c == "*":
            return b * a
        else:
            return ("Ошибка: Неизвестная операция")





#определяет порядок вычисления исходя из приоритетов
def logic(example_list):
    try:
        print("Переданный лист:", example_list)
        num = []
        oper = []
        for x in example_list:
            if number(x) != False:
                num.append(number(x))
                print(num)
            elif x == "0":
                num.append(0)
            elif x == "(":
                oper.append(x)
            else:
                oper.append(x)
                print("oper", oper)
                if len(oper) == 1:
                    pass
                else:
                    while len(oper) > 1:
                        if priority(oper[-2]) - priority(oper[-1]) <= 0:
                            if oper[-2] == "(" and oper[-1] == ")":
                                oper.pop()
                                oper.pop()
                            elif oper[-2] == "(":
                                break
                            else:
                                num.append(calculations(num.pop(), num.pop(), oper.pop(-2)))
                        else:
                            break
        while True:
            if len(oper) <= 1:
                break
            elif priority(oper[-2]) - priority(oper[-1]) <= 0:
                if oper[-2] == "(":
                    oper.pop()
                    oper.pop()
                else:
                    num.append(calculations(num.pop(), num.pop(), oper.pop(-2)))
            elif priority(oper[-1]) < priority(oper[-2]):
                num.append(calculations(num.pop(), num.pop(), oper.pop()))



        print("finaly", num, oper)
        if len(num) != 1:
            result = calculations(num.pop(), num.pop(), oper.pop())
            print("resul", result)
        else:
            result = num.pop()
        # print(result)
        return result
    except:
        print("Вы ввели некоректные значения, попробуйте снова")
        return "Ошибка: Вы ввели некоректные значения, попробуйте снова"






#данная функция от части проверяет на возможность выполнения задачи
def checking_expression(ex):
    print("проверка на вшивость", ex)
    #Проверяет на пустое значение
    if len(ex) == 0:
        print("Ошибка: Введено пустое выражение")
        return "Ошибка: Введено пустое выражение"
    #Убирает текст ошибки полученный при прошлых вычислениях
    if "Ошибка:" in ex[0]:
        del ex[0]
    #убирает пустые значки
    if "" in ex:
        while True:
            ex.remove('')
            if '' in ex:
                pass
            else:
                break
    # Проверяет количество ( и ), а так же их порядок
    if "(" in ex or ")" in ex:
        a = 0
        for i in ex:
            if i == "(":
                a = a + 1
            elif i == ")":
                a = a - 1
                if a < 0:
                    print("Ошибка: Закрывающая скобка не может быть раньше открывающей")
                    return "Ошибка: Закрывающая скобка не может быть раньше открывающей"
        print("проверяю совпадает ли количество скобок")
        if a != 0:
            print("Ошибка: Количество введенных ( и ) не совпадает")
            return ("Ошибка: Количество введенных ( и ) не совпадает")
        print("количество скобок совпадает")
    # Проверяет на наличие чисел в примере
    if True:
        count = 0
        for i in ex:
            if i in ["*", "/", "+", "-", "(", ")"]:
                count = count + 1
            else:
                break
        if count == len(ex):
            print("Ошибка: Вы ввели значение без цифр")
            return ("Ошибка: Вы ввели значение без цифр")
    print("пропускаем этого хлопца")
    return logic(ex)







# checking_expression(["967", "/", "-0.2147", "+", "85134", "*", "999", "-", "0", "*", "0.01"])
# checking_expression(["99999999999999", "*", "99999999999999"])
# logic(["0", "/", '2'])
# logic(["2", "/", '0'])
# logic(['(', "1", "+", '1', ")"])
# logic(['5', '+', '3', '*', '(', '2', '/', '1', '+', '(', '5', '+','(', '5', '+', '(', '9', '+','(', '5', '+', '5', ')', '-', '5', ')', '-', '5', ')', '-', '5', ')', ')', '-', '4', '+', '(', '1', '+', '1', ')'])
# logic(['1', '+', '(', '1', '+', '1', ')'])
# logic(['(', '(', '(', '1', ')', ')', ')'])
# print(type(int(str(0))))















# def logic(example_list):
#     print(example_list)
#     num = []
#     oper = []
#     for x in example_list:
#         if x.isdigit():
#             num.append(int(x))
#         else:
#             oper.append(x)
#     print(num, oper)
#     num.reverse()
#     oper.reverse()
#
#     while len(num) != 0:
#
#         while len(oper) > 1:
#             if priority(oper[-2]) - priority(oper[-1]) <= 0:
#                 num.append(calculations(num.pop(), num.pop(), oper.pop(-2)))
#             else:
#                 break
#     result = calculations(num.pop(), num.pop(), oper.pop())
#     print(result)
#     print("end:" , num, oper)