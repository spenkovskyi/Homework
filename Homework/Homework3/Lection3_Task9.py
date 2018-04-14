"""Задания 9
Даны четыре действительных числа: x1, y1, x2, y2.
Напишите функцию distance(x1, y1, x2, y2),
вычисляющую расстояние между точкой (x1, y1) и (x2, y2).
Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.
"""

def distance(a):
    distance = ((a[2]-a[0])**2 + (a[1]-a[3])**2)**0.5
    return distance


def enter_value(x):
    while True:
        try:
            a=(float(input("Enter value " + x +"\n")))
        except ValueError:
            print("Try to enter " + x + "again")
        else:
            return a

a = list()
a.append(enter_value("x1"))
a.append(enter_value("y1"))
a.append(enter_value("x2"))
a.append(enter_value("y2"))
print(a)
print("distance between your points is", distance(a))
