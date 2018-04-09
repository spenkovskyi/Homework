"""Задание 4
Даны три числа a, b, c. Определите, существует ли треугольник с такими сторонами.
Если треугольник существует, выведите строку YES, иначе выведите строку NO."""

a = [1, 1, 1]
a[0] = float(input("Enter a \n"))
a[1] = float(input("Enter b \n"))
a[2] = float(input("Enter c \n"))

b = sorted(a)

if b[0] + b[1] > b[2]:
    print("triangle exist")
else:
    print("triangle does not exist")

