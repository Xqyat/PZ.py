#1. Организовать и вывести послеовательность из N случайных
#целых чисел. Из исходной последовательности организовать
#новую последовательность, содержащую положительные числа.
#Найти их количество
import random as rand
quantity = rand.randint(5, 10)
subsequence = [rand.randint(-5, 10) for value in range (quantity)]
print("Исходная последовательность:", subsequence)
new_subsequence = [i for i in subsequence if i > 0]
print("Новая последовательность: ", new_subsequence, "Количество положительных чисел: ", len(new_subsequence), sep="\n")