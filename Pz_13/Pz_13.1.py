#1. В матрице найти сумму и произведение элементов
# столбца N (N задать с клавиатуры)
import random as rand
Rows_vert = rand.randint(2, 4)
Rows_hor = rand.randint(2, 4)
Matrix = [[rand.randint(1, 8) for j in range(Rows_hor)] for i in range(Rows_vert)]
for i in Matrix:
    print(i)
N_num = int(input("Введите номер столбца N (отсчет с нуля): "))
sum_col = 0
subtr_col = 1
for i in range(Rows_vert):
    sum_col += Matrix[i][N_num]
    subtr_col *= Matrix[i][N_num]
print(f"\nСумма элементов столбца N: {sum_col}")
print(f"Произведение элементов столбца N: {subtr_col}")
