#2. В матрице найти отрицательные элементы, сформировать
# из них новый массив. Вывести размер полученного массива
import random as rand
Rows_hor = rand.randint(2, 4)
Rows_vert = rand.randint(2, 4)
Matrix = [[0] * Rows_hor for i in range(Rows_vert)]
new_arr = []
for i in range(Rows_vert):
    for j in range(Rows_hor):
        Nums = rand.randint(-8, 8)
        Matrix[i][j] = Nums
for i in Matrix:
    print(i)
for i in range(Rows_vert):
    for j in range(Rows_hor):
        if Matrix[i][j] < 0:
            new_arr.append(Matrix[i][j])
print("Отрицательные элементы:")
print(new_arr)
print("Размер полученного массива:", len(new_arr))