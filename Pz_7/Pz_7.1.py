import random as rand
N_num = rand.randint(1, 4)
S_str = input("Напишите непустое предложение: ")
for i in S_str:
    if i == " ":
        i += N_num
