import sys
from idlelib import window
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.uic.properties import QtGui

import calc_ui
import calculator

# pyuic5 calc_ui.ui -o calc_ui.py

class ExampleApp(QtWidgets.QMainWindow, calc_ui.Ui_Dialog):
    number = ""
    example_list = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.number
        # self.example_list
        self.setWindowTitle('Calculator')


        self.pushButton.clicked.connect(lambda: self.num("1"))
        self.pushButton_2.clicked.connect(lambda: self.num("2"))
        self.pushButton_3.clicked.connect(lambda: self.num("3"))
        self.pushButton_4.clicked.connect(lambda: self.num("4"))
        self.pushButton_5.clicked.connect(lambda: self.num("5"))
        self.pushButton_6.clicked.connect(lambda: self.num("6"))
        self.pushButton_7.clicked.connect(lambda: self.num("7"))
        self.pushButton_8.clicked.connect(lambda: self.num("8"))
        self.pushButton_9.clicked.connect(lambda: self.num("9"))
        self.pushButton_11.clicked.connect(lambda: self.num("0"))
        self.pushButton_12.clicked.connect(lambda: self.num("."))
        self.pushButton_22.clicked.connect(lambda: self.num("-"))
        self.pushButton_13.clicked.connect(lambda: self.oper("/"))
        self.pushButton_14.clicked.connect(lambda: self.oper("+"))
        self.pushButton_15.clicked.connect(lambda: self.oper("*"))
        self.pushButton_16.clicked.connect(lambda: self.oper("-"))
        self.pushButton_20.clicked.connect(lambda: self.oper("("))
        self.pushButton_21.clicked.connect(lambda: self.oper(")"))
        self.pushButton_17.clicked.connect(lambda: self.calculate())
        self.pushButton_18.clicked.connect(lambda: self.clear())


    def returns(self, name):
        if name == "number":
            return 1
        elif name == "example_list":
            return self.example_list

    # def set(self, name, value):
    #     if name == "number":
    #         self.number = value
    #         return self.number
    #     elif name == "example_list":
    #         self.example_list = value
    #         return self.example_list


#формирует одно число в глобальной переменной
    def num(self, n):
        if n == ".":
            if "." in self.number:
                n = ""
        self.number = self.number + n
        print(self.number)
        self.plainTextEdit.insertPlainText(n)





# заканчивает формировать число, добавляет операцию в пример
    def oper(self, o):
        if self.number != "":
            self.example_list.append(self.number)
            self.number = ""
        if len(self.example_list) != 0:
            if self.example_list[-1] in ("/", "*", "+", "-",""):
                if o in ("/", "*", "+", "-"):
                    o = ""
        self.example_list.append(o)
        self.plainTextEdit.insertPlainText(o)
        print(o)

#
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_1:
            self.num("1")
        if e.key() == Qt.Key_2:
            self.num("2")
        if e.key() == Qt.Key_3:
            self.num("3")
        if e.key() == Qt.Key_4:
            self.num("4")
        if e.key() == Qt.Key_5:
            self.num("5")
        if e.key() == Qt.Key_6:
            self.num("6")
        if e.key() == Qt.Key_7:
            self.num("7")
        if e.key() == Qt.Key_8:
            self.num("8")
        if e.key() == Qt.Key_9:
            self.num("9")
        if e.key() == Qt.Key_0:
            self.num("0")
        if e.key() == Qt.Key_Minus:
            self.oper("-")
        if e.key() == Qt.Key_Plus:
            self.oper("+")
        if e.key() == Qt.Key_Asterisk:
            self.oper("*")
        if e.key() == Qt.Key_Slash:
            self.oper("/")
        # if e.key() == Qt.Key_BracketLeft:
        #     self.oper("(")
        # if e.key() == Qt.Key_BraceRight:
        #     self.oper(")")
        if e.key() == Qt.Key_Equal:
            self.calculate()
        if e.key() == Qt.Key_Enter:
            self.calculate()
        if e.key() == Qt.Key_Delete:
            self.clear()
        if e.key() == Qt.Key_Backspace:
            self.clear()



#отсылает пример на решение
    def calculate(self):
        if self.number != "":
            self.example_list.append(self.number)
            self.number = ""
        print("Начал считать")
        result = calculator.checking_expression(self.example_list)
        print("answ:", result)
        self.example_list = []
        self.number = ""
        self.example_list.append(str(result))
        self.plainTextEdit.appendPlainText(f"= {result}")
        self.plainTextEdit.appendPlainText("")





    def clear(self):
        self.example_list =[]
        self.number = ""
        self.plainTextEdit.clear()





def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


main()



# TO DO
# 3 скобки не работают ++
# Пустые скобки ++
# ответ на негатив ++
# Что с выводом ++
# UI ++
# тесты ++
# деление на 0, 2 дел 0 ++
# крайние значения ++
# Что должно происходить если есть один знак и одно число?
# [')', '8', '('] ++