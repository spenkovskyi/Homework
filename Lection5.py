class Couple:
    pass

class Person:
#    desc= {"title":"Person"}

    def __init__(self, name="", surname="", age=1):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):
        self.fullname = self.name + " " + self.surname
        return self.fullname

    def make_older(self, years = 1):
        self.newage=self.age+years
        return self.newage
    def __str__(self):
        return "<Person names={}, surname={}, age={}>".format(self.name, self.surname,self.age)
    # def __add__(self, person):
    #     return Couple()


if __name__ == "__main__":
    p = Person("Nika", "Pupkina", 26)
    p2 = Person("Vasya", "Pupikov", 30)
    print(p.full_name())
    print("Age of", p.fullname, "is", p.age)
    print("New age of", p.fullname, "is", p.make_older(5))
    print(p)
    # m = p + p2
    # print(m)







# print(p.name)
#p.set_name()
#print("p:", p.name)
# print("p:", p.desc)
#

#p2 = Person()
#
#p2.set_name("Kolya", "Pupkin")
##p.set_name()
#print("p2:", p2.full_name)
#print("p2:", p2.desc)
#print(p.desc == p2.desc)
#print(p.desc is p2.desc)
#print(p.full_name == p2.full_name)
#print(p.full_name is p2.full_name)
