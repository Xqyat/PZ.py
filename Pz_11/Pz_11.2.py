#2. Из предложенного текстового файла (text18-12.txt) вывести
#на экран его содержимое, количество пробельных символов.
#Сформировать новый файл, в которой поместить текст в
#стихотворной форме предварительно вставив после каждой строки
#строку из символов "+".
import random as rand
pluses = rand.randint (4, 8)
count_spacebar = 0

poem = open("text18-12.txt", encoding="UTF-16")
print(poem.read())
poem.close()

poem = open("text18-12.txt", encoding="UTF-16")
for i in poem.read():
    if i == " ":
        count_spacebar += 1
print("Количество пробелов: ", count_spacebar)
poem.close()

poem = open("text18-12.txt", encoding="UTF-16")
new_poem = open("New_poem.txt", "w", encoding="UTF-16")
for i in poem.read():
    new_poem.write(i)
    if i == "\n":
        new_poem.write("+" * pluses)
        new_poem.write("\n")
    elif i == "…":
        new_poem.write("\n")
        new_poem.write("+" * pluses)
