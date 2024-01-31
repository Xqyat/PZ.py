#1. Средствами языка Python сформировть  текстовый файл (.txt),
#содержащий последовательность из целых положительных и
#отрицательных чисел. Сформировать новый текстовый файл
#(.txt) следующего вида, предваритильно выполнив требуюмую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Максимальный элемент:
#Среднее арифмитическое элементов первой трети:
import random as rand
quantity = rand.randint(9, 18)
row = []

for i in range(quantity):
    nums_for_row_minus = rand.randint(-10, -1)
    row.append(nums_for_row_minus)

for i in range(quantity):
    nums_for_row_plus = rand.randint(1, 10)
    row.append(nums_for_row_plus)

biggest_num = max(row)

indexs_of_row = len(row)

one_third_of_row = round(indexs_of_row / 3)

for_mid_math = row[0: one_third_of_row]

mid_math = (sum(for_mid_math)) / 2

new_file = open("Nums.txt", "w", encoding = "UTF-8")
new_file.write(f"Исходные данные: {str(row)} \n")
new_file.write(f"Количество элементов: {str(len(row))} \n")
new_file.write(f"Максимальный элемент: {biggest_num} \n")
new_file.write(f"Среднее арифмитическое элементов первой трети: {mid_math} \n")
new_file.close()




