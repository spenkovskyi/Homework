"""Задание 4
Даны три числа a, b, c. Определите, существует ли треугольник с такими сторонами.
Если треугольник существует, выведите строку YES, иначе выведите строку NO."""

a = list()
a.append(float(input("Enter a \n")))
a.append(float(input("Enter b \n")))
a.append(float(input("Enter c \n")))

b = sorted(a)

if b[0] + b[1] > b[2]:
    print("triangle exist")
else:
    print("triangle does not exist")

