"""
Задание 3 (на создание тестов c помощью unittest)
Создайте наборы тестов на написанные функции из прошлого домашнего задания:
•	Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
если год високосный, и False иначе.
•	Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами.
Если треугольник существует, вернёт True, иначе False.
•	Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами
и если существует, то возвращает тип треугольника Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный),
Versatile triangle (разносторонний) или не треугольник (Not a triangle).
"""
import unittest
from Homework.Homework3.Lection3_Task6 import is_year_leap
from Homework.Homework3.Lection3_Task6 import treangle_existance
from Homework.Homework3.Lection3_Task7 import treangle_type

class Is_year_leapTest(unittest.TestCase):
    def test_leap_year(self):
        res = is_year_leap(2000)
        self.assertEqual(res, True)
    def test_not_leap_year(self):
        res = is_year_leap(2001)
        self.assertEqual(res, False)
        res = is_year_leap(600)
        self.assertEqual(res, False)

class TriangleExistanceTest(unittest.TestCase):
    def test_treangle_exist(self):
        res = treangle_existance(2,3,4)
        self.assertEqual(res, True)
    def test_treangle_does_not_exist(self):
        res = treangle_existance(3,6,1)
        self.assertEqual(res, False)

class TriangleTypeTest(unittest.TestCase):
    def test_equilateral_treangle(self):
        res = treangle_type(3,3,3)
        self.assertEqual(res, "equilateral")
    def test_isosceles_treangle(self):
        res = treangle_type(3,3,1)
        self.assertEqual(res, "isosceles")
    def test_versatile_treangle(self):
        res = treangle_type(2,3,4)
        self.assertEqual(res, "versatile")
    def test_triangle_does_not_exist(self):
        res = treangle_type(2,5,8)
        self.assertEqual(res, False)

if __name__ == "__main__":
    unittest.main()