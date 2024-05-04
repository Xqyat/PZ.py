# 2. Создайте базовый класс "Транспорт" со свойствами
# "марка", "модель" и "год выпуска". От этого класса
# унаследуйте класс "Автомобиль" и добавьте в него
# свойство "тип кузова"

class Transport():
    mark = ""
    model = ""
    data_creation = ""

    def machine(self):
        print("Непонятно какая машина!")


class Automobil(Transport):
    body_type = ""

    def machine(self):
        print(f"Тип корпуса: {self.body_type}",
              f"Марка машины: {self.mark}",
              f"Модель машины: {self.model}",
              f"Год выпуска: {self.data_creation}", sep="\n")


First_machine = Automobil()
First_machine.mark = "Ford"
First_machine.model = "I-485"
First_machine.data_creation = "04.02.2008"
First_machine.body_type = "Vehicle"
First_machine.machine()