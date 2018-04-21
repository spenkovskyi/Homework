from Lection5 import Person

class Employee(Person):
    def __str__(self):
        return "<Employee names={}, surname={}, age={}, position={}, salary={}>".format(self.name, self.surname,self.age,self.position,self.salary)

    def __init__(self, name=None, surname=None, age=None, position=None, salary = 0):
        super().__init__(name, surname, age)
        # self.name = name
        # self.surname = surname
        # self.age = age
        self.position = position
        self.salary = salary

    def income(self, month=1):
        self.income = self.salary*month
        return self.income

if __name__ == "__main__":
    e = Employee("Vasya", "Pupikov", 30, position="Engineer", salary=1000)
    print(e)
    print(e.name,"income is", e.income(10))

