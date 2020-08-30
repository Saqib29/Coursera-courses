CURRENT_YEAR = 2020
class Person:
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born
    def getAge(self):
        return CURRENT_YEAR - self.year_born
    def __str__(self):
        return '{} ({})'.format(self.name, self.getAge())

class Student(Person):
    def __init__(self, name, year_born):
        Person.__init__(self, name, year_born)
        self.knowledge = 0
    def study(self):
        self.knowledge += 1


alice = Student('Saqib Aminul', 1995)
alice.study()
print(alice)
print(alice.knowledge)
