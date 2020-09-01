class human:
    def __init__(self, name):
        self.name = name
    def changeName(self, name):
        self.name = name

class female(human):
    def addAge(self, age):
        self.age = age
    def pee(self):
        po = 'A,N,I,K,A'
        return po


f = female('Anika')
f.addAge(20)
print(f.age)
print(f.name)
print(f.pee())

