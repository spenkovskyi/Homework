"""Задание 6
Это уже было, но теперь оформите это функцией:
1)	Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
2)	Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами. Если треугольник существует, вернёт True, иначе False.
"""

def is_year_leap(year):
    """
    Function will return True if the year is leap and False otherwise
    """
#    print("Method was called")
    if ((year % 400) == 0) or ((year % 4) == 0 and (year % 100) != 0):
        return True
    else:
        return False
#    print("Method execution finished. Result is", result)

def treangle_existance(a,b,c):
    """
    Function will return True if triangle exist and False otherwise
    """
#    print("Method was called")
    x = sorted([a,b,c])
    if x[0] + x[1] > x[2]:
        return True
    else:
        return False
#    print("Method execution finished. Result is", result)

#1
y = input("Enter your year \n")
try:
    y = int(y)
except ValueError:
    print("Year must be integer")
else:
    if is_year_leap(y):
        print(y,"is a leap year")
    else:
        print(y,"is not a leap year")
#2

a = float(input("Enter a \n"))
b = float(input("Enter b \n"))
c = float(input("Enter c \n"))
print(a,b,c)
if treangle_existance(a,b,c):
    print("triangle exist")
else:
    print("triangle does not exist")
