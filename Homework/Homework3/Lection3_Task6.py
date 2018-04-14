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
    if ((year % 4) == 0 and (y % 400) == 0) or ((y % 4) == 0 and (y % 100) != 0):
        result = True
    else:
        result = False
#    print("Method execution finished. Result is", result)
    return result
def treangle_existance(a):
    """
    Function will return True if triangle exist and False otherwise
    """
#    print("Method was called")
    a = sorted(a)
    if a[0] + a[1] > a[2]:
        result = True
    else:
        result = False
#    print("Method execution finished. Result is", result)
    return result
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
a = list()
a.append(float(input("Enter a \n")))
a.append(float(input("Enter b \n")))
a.append(float(input("Enter c \n")))
print(a)
if treangle_existance(a):
    print("triangle exist")
else:
    print("triangle does not exist")
