# 1.Создайте класс "Животное" с атрибутами "имя" и "вид".
# Напишите метод , который выводит информацию о животном в
# формате "Имя: имя, Вид: вид".
class Animal():
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind


first_animal = Animal("Мурка", "Кошки")
print(f"Имя: {first_animal.name}", f"Вид: {first_animal.kind}", sep="\n")
