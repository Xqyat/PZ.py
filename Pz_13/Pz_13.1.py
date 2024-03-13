#1. В матрице найти сумму и произведение элементов
# столбца N (N задать с клавиатуры)
import random as rand
Rows_vert = rand.randint(2, 4)
Rows_hor = rand.randint(2, 4)
Matrix = [[rand.randint(1, 8) for i in range(Rows_hor)] for i in range(Rows_vert)]
[print(row) for row in Matrix]
N_num = int(input("Введите номер столбца N (отсчет с нуля): "))
sum_col = sum(Matrix[i][N_num] for i in range(Rows_vert))
subtr_col = 1
for i in range(Rows_vert):
    subtr_col *= Matrix[i][N_num]
print(f"Сумма элементов столбца N: {sum_col}")
print(f"Произведение элементов столбца N: {subtr_col}")
