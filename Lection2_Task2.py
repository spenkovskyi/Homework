"""Задание 2
1.	Вычислите длину гипотенузы в прямоугольном треугольнике со сторонами 179 и 971.
2.	Дано двузначное число. Найдите число десятков в нем.
3.	Дано трехзначное число. Найдите сумму его цифр.
4.	Дано целое число n. Выведите следующее за ним чётное число.
5.	Дано положительное действительное число X. Выведите его дробную часть.
6.	Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.
"""
#1
g = (179**2+971**2)**0.5
print("Length of the hypotenuse is", g)
#2
c = 56
print("Quantity of dozens in", c, "is", c//10)
#3
d = 999
print("Amount of digits in", d, "is", d//100+((d-(d//100)*100)//10)+((d-(d//100)*100)%10))
#4
n = 56
if n % 2 == 1:
    print("Next paired number of", n, "is", n+1)
else:
    print("Next paired number of", n, "is", n+2)
#5
x = 441.912345678
print("Fractional part of", x,"is", round((x-x//1), len(str(x))))# Need to clarify how to round
#6
print("first digit after dot in", x, "is", int((x-x//1)*10//1))
