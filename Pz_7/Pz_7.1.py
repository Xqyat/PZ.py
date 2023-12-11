# Дана непустая строка S и целое число N(>0). Вывести строку,
# содержащие символы строки S, между которыми вставлено
# по N символов "*"
import random as rand
N_num = rand.randint(1, 3)
result = ""
S_str = input("Напишите непустое предложение: ")
print(N_num)
for i in range(len(S_str)):
    if S_str[i] == " ":
        result += "*" * N_num
    else:
        result += S_str[i]
print(result)

