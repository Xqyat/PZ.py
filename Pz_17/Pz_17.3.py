#3. Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
# оформленный согласно требованиям. Все задания выполняются c использованием модуля
# OS:
# -перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
# вложенных подкаталогов выводить не нужно.
# -перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
# файлов в папке test.
# -перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
# консоль. Использовать функцию basename () (os.path.basename()).
# -перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
# привязанной к нему пр


# -перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
# вложенных подкаталогов выводить не нужно.
import os

os.chdir("../Pz_11")
print("", os.listdir())
# os.makedirs("test/test1")



# os.replace("../Pz_6/Pz_17_file1.py", "../Pz_11/test/Pz_17_file1.py")
# os.replace("../Pz_6/Pz_17_file2.py", "../Pz_11/test/Pz_17_file2.py")
# os.replace("../Pz_7/Pz_17_file3.py", "../Pz_11/test/test1/Pz_17_file3.py")
#
# os.rename("../Pz_11/test/Pz_17_file2.py", "test.txt")
# print("Размер файлов: ", os.stat("../Pz_11/test/Pz_17_file1.py").st_size, os.stat("../Pz_11/test/test.txt").st_size, os.stat("../Pz_11/test/test1/Pz_17_file3.py").st_size, sep="\n")
#
# short_filename = ""
# for i in os.listdir():
#     if len(i) < len(short_filename) or short_filename == "":
#         short_filename = i
#
# print(os.path.basename(short_filename))


# os.startfile('C:/Users/user/Documents/Kolesnikov IS-23/PZ.py/Reports/Pz_3.pdf')

# os.remove("../Pz_11/test/test.txt")