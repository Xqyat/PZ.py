#2. В матрице найти отрицательные элементы, сформировать
# из них новый массив. Вывести размер полученного массива
import random as rand
Rows_hor = rand.randint(2, 4)
Rows_vert = rand.randint(2, 4)
Matrix = [[rand.randint(-8, 8) for i in range(Rows_hor)] for i in range(Rows_vert)]
[print(row) for row in Matrix]
new_arr = [Matrix[i][j] for i in range(Rows_vert) for j in range(Rows_hor) if Matrix[i][j] < 0]
print("Отрицательные элементы:")
print(new_arr)
print("Размер полученного массива:", len(new_arr))