class Person:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def getbmi(self):
        return self.weight / (self.height / 100) ** 2

    def __str__(self):
        return "[Name]:{n}\t[Height]:{h}".format(n=self.name,
                                                 h=self.height)

    def __repr__(self):
        return self.__str__()

class SuperPerson(Person):

    def __init__(self, name, height, weight, live):
        Person.__init__(self, name, height, weight)
        self.live = live

    def __str__(self):
        return "{}\t{}".format(Person.__str__(self),
                               self.live)



p1 = Person("Elwing", 175, 75)
# p1 -> str(p1) -> p1.__str__()
print(p1)
print(p1.getbmi())
p2 = SuperPerson("Bob", 200, 100, "Taipei")
print(p2)
# [p1] -> repr(p1) -> p1.__repr__()
print([p1, p2])