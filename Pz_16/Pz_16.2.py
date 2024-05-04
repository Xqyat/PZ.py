#3. Для задачи из блока 1 создать две функции, save_def
# и load_def, которые позволяют сохранять информацию из
# экземпляров класса (3 шт.) в файл и загружать её
# обратно. Использовать модуль pickle для сериализации
# и десериализации объектов Python в бинарном формате
import pickle
class Animal():
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

def save_animals(animals, filename):
    with open(filename, 'wb') as f:
        pickle.dump(animals, f)

def load_animals(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

first_animal = Animal("Мурка", "Кошки")
second_animal = Animal("Боб", "Собаки")
third_animal = Animal("Лора", "Попугаи")
animals = [first_animal, second_animal, third_animal]
save_animals(animals, 'animals.bin')

loaded_animals = load_animals('animals.bin')

for animal in loaded_animals:
    print(f"Имя: {animal.name}", f"Вид: {animal.kind}", sep="\n")