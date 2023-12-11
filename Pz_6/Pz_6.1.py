# Дан список A размера N (N - нечётное число). Вывести
# его элементы с нечётными номерами в порядке убывания
# номеров: A(N), A(N-2), A(N-4), ..., A(1), Условный оператор
# не использовать.
import random as rand
quantity_num = int(input("Введите количество чисел, которые вы хотите добавить в список: "))


List_A = []
for i in range(quantity_num):
    N_num = rand.randint(1, 9)
    List_A.append(N_num)
print("Изначальный список: ", List_A)
List_A.reverse()
Rev_list = []
for i in List_A[1::2]:
    Rev_list.append(i)
print("Элементы в порядке убывания индекса: ", Rev_list)







