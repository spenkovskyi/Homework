"""Задания 9
Даны четыре действительных числа: x1, y1, x2, y2.
Напишите функцию distance(x1, y1, x2, y2),
вычисляющую расстояние между точкой (x1, y1) и (x2, y2).
Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.
"""
from Lection3_Task8 import number
def distance(x1,y1,x2,y2):
    distance = ((x2-x1)**2 + (y1-y2)**2)**0.5
    return distance


def enter_value(x):
    while True:
        try:
            a=(float(input("Enter value " + x +"\n")))
        except ValueError:
            print("Try to enter " + x + " again")
        else:
            return a

#a = list()
x1 = number("Enter value x1:\n")
y1 = number("Enter value y1:\n")
x2 = number("Enter value x2:\n")
y2 = number("Enter value y2:\n")
print(x1,y1,x2,y2)
print("distance between your points is", distance(x1,y1,x2,y2))
