"""
Задание 7
Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами
и если существует, то возвращает тип треугольника
Equilateral triangle (равносторонний),
Isosceles triangle (равнобедренный),
Versatile triangle (разносторонний) или не треугольник (Not a triangle).
"""

def treangle_type(a):
    """
    Function will return type of triangle
    (Equilateral triangle,  Isosceles triangle, Versatile triangle) if it exist and "Triangle does not exist" otherwise
    """
    #    print("Method was called")
    a = sorted(a)
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
a = list()
try:
    a.append(float(input("Enter a \n")))
    a.append(float(input("Enter b \n")))
    a.append(float(input("Enter c \n")))
except ValueError:
    print("Input must be digital")
else:
    print(a)
    t = treangle_type(a)
    if t:
        print("triangle exist and it is", t)
    else:
        print("triangle does not exist")
