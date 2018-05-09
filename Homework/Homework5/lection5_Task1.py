"""Задание 1 (на создание классов)
Переделываем (а что-то повторяем и закрепляем) наши классы таким образом:
1) Person (два свойства:
1. теперь full_name пусть будет свойством, а не функцией, а свойств name и surname нет
(одно поле – предполагается, что тип строка и состоит из двух слов «имя фамилия»),
2. год рождения).
Реализовать методы, которые:
1.	выделяет только имя из full_name
2.	выделяет только фамилию из full_name;
3.	вычисляет сколько лет есть/исполнится в году, который передаётся параметром (obj.age(years));
если не передавать параметр, по умолчанию, сколько лет в этом году;
** (только для продвинутых) Можете в конструкторе проверить, что в full_name передаётся строка,
состоящая из двух слов, если нет, вызывайте исключение 😊
** (только для продвинутых) Можете проверить, что в год рождения меньше 2018, но больше 1900,
если нет вызывайте исключение
2) Employee (наследуемся от Person) (добавляются свойства: должность, опыт работы, зарплата)
Реализовать новые методы:
1.	возвращает должность с приставкой, которая зависит от опыта работы: Junior — менее 3 лет, Middle — от 3 до 6 лет,
Senior — больше 6 лет. Т.е. метод должен вернуть позицию с приставкой Junior/Middle/Senior <position>. Если например у
вас объект имел должность programmer с опытом 2 года, метод должен вернуть “Junior programmer”
2.	метод, который увеличивает зарплату на сумму, которую вы передаёте параметром.
3) ITEmployee (наследуемся от Employee)
1. Реализовать метод добавления одного навыка в новое свойство skills (список) новым методом add_skill (см. презентацию).
2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список) новым методом add_skills.
Тут можно выбрать разные подходы: или аргумент один и он список навыков, которым вы расширяете список-свойство skill, или
вы принимаете неопределённое количество аргументов и все их добавляете в список-свойство skill
"""


class Person:
    def __init__(self, full_name="Vasya Pupikov", year_of_birth=1985):
        if len(full_name.split()) != 2:
            raise Exception("Full name must consist of 2 words")
        if year_of_birth not in range (1900,2018):
            raise Exception("Year of birth must be in range 1900 - 2018")
        self.full_name = full_name
        self.year_of_birth = year_of_birth
    def name_from_full_name(self):
        name = self.full_name.split()[0]
        return name
    def surname_from_full_name(self):
        surname = self.full_name.split()[1]
        return surname
    def age(self, current_year=2018):
        age = current_year - self.year_of_birth
        return age


class Employee(Person):
    def __init__(self, *args, position="no position", experience=1, salary=1000,**kwargs):
        super(Employee, self).__init__(*args,**kwargs)
        self.position = position
        self.position = position
        self.experience = experience
        self.salary = salary
    def current_position(self):
        if self.experience in range (0,3):
            current_position = "Junior " + self.position
        elif self.experience in range (3,6):
            current_position = "Middle " + self.position
        elif self.experience in range (6,80):
            current_position = "Senior " + self.position
        else:
            raise Exception("Expirience is out of range")
        return current_position
    def salary_upgrade(self, upgrade=200):
        self.salary = self.salary + upgrade
        return self.salary


class ITEmployee(Employee):
    def __init__(self, *args, skills=list(),**kwargs):
        super(ITEmployee, self).__init__(*args,**kwargs)
        self.skills = skills

    def add_skill(self, new_skill):
        self.skills.append(new_skill)
        return self.skills
    def add_skills(self, new_skills=list()):
        self.skills = self.skills + new_skills
        return self.skills

if __name__ == "__main__":
    person = Person(full_name="Vaselina Pupkova", year_of_birth=2000)
    # person = Person(full_name="VaselinaPupkova", year_of_birth=2000)
    # person = Person(full_name="Vaselina Pupkova", year_of_birth=1000)
    print(person.name_from_full_name())
    print(person.surname_from_full_name())
    print("Age is", person.age(2015))
    
    empl1 = Employee()
    print(empl1.full_name, empl1.year_of_birth, empl1.experience, empl1.position, empl1.salary)
    
    empl2 = Employee(full_name="Vasek Pupov", year_of_birth=1999, position="QA engineer", experience=3, salary=1500)
    print(empl2.full_name, empl2.year_of_birth, empl2.experience, empl2.position, empl2.salary)
    print("Age is", empl2.age())
    print("Current position is", empl2.current_position())
    print("Salary of",empl2.name_from_full_name(),"after upgrade is", empl2.salary_upgrade(250))
    
    itempl1=ITEmployee()
    print(itempl1.full_name, itempl1.year_of_birth, itempl1.experience, itempl1.position, itempl1.salary, itempl1.skills)

    itempl2=ITEmployee(full_name="Vasisualy Pupichkov", year_of_birth=1990, position="HW engineer", experience=12, salary=4500, skills=["Logic","Python","Manual QA","Hardware"])
    print(itempl2.full_name, itempl2.year_of_birth, itempl2.experience, itempl2.position, itempl2.salary,itempl2.skills)
    print("Age is", itempl2.age())
    print("Current position is", itempl2.current_position())
    print("Salary of",itempl2.name_from_full_name(),"after upgrade is", itempl2.salary_upgrade(500))
    itempl2.add_skill("Automation")
    print(itempl2.skills)
    itempl2.add_skills(["Management", "Patience", "Work for free"])
    print(itempl2.skills)
