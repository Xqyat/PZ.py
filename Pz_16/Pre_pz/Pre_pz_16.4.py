class Person():
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
    @staticmethod
    def total_people():
        print(Person.count)
c1 = Person("First")
c2 = Person("Second")
c3 = Person("First")
c4 = Person("Second")
Person.total_people()


