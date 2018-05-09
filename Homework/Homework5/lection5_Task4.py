"""
Задание 4 (на создание тестов c помощью unittest)
Создайте наборы тестов на тестирование класса ITEmployee, который вы реализовали в Задании 1
(или Employee, или Person в зависимости до куда вы дошли в выполнении Задания 1).
"""
import unittest
from Homework.Homework5.lection5_Task1 import ITEmployee

class ITEmployeeTest(unittest.TestCase):
    def setUp(self):
        self.empl = ITEmployee(full_name="Vasunya Pupochkin", year_of_birth=1995, position="SW engineer", experience=2, salary=500, skills=["English","QA"])
    def test_add_skill(self):
        res = self.empl.add_skill("Auto")
        self.assertEqual(res, self.empl.skills)
    def test_add_skills(self):
        res = self.empl.add_skills(["ISTQB","CCNA","CCNP"])
        self.assertEqual(res, self.empl.skills)
    def test_name(self):
        res = self.empl.name_from_full_name()
        self.assertEqual(res, "Vasunya")
    def test_surname(self):
        res = self.empl.surname_from_full_name()
        self.assertEqual(res, "Pupochkin")

if __name__ == "__main__":
    unittest.main()