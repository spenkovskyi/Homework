"""
Задание 7
Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами
и если существует, то возвращает тип треугольника
Equilateral triangle (равносторонний),
Isosceles triangle (равнобедренный),
Versatile triangle (разносторонний) или не треугольник (Not a triangle).
"""

def treangle_type(b,c,d):
    """
    Function will return string with triangle type (equilateral, isosceles, versatile)
    if it exist and False if it is not exist
    """

    a = sorted([b,c,d])
    if a[0] + a[1] > a[2]:
        if a[0] == a[1] == a[2]:
            triangle = "equilateral"
        elif (a[0]== a[1] != a[2]) or (a[0]!= a[1] == a[2]) or (a[0]== a[2] != a[1]):
            triangle = "isosceles"
        else:
            triangle = "versatile"
    else:
        triangle = False
#    print("Method execution finished. Result is", result)
    return triangle
#1
#a = list()
try:
    a = float(input("Enter a \n"))
    b = float(input("Enter b \n"))
    c = float(input("Enter c \n"))
except ValueError:
    print("Input must be digital")
else:
    print(a,b,c)
    t = treangle_type(a,b,c)
    if t:
        print("triangle exist and it is", t)
    else:
        print("triangle does not exist")
