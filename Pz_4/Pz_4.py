#1. Дано целое число N(>0). Найти значение выражения
# 1.1-1.2+1.3-...(N слагаемых, знаки чередуются).
# Условный оператор не использовать.
# term_p_sum = 0
# term_p = 1.1
# term_o_sum = 0
# term_o = -1.2
# N_num=int(input("Введите число больше 0: "))
# for i in range(0, N_num // 2):
#     term_p_sum += term_p
#     term_p += 0.2
# for i in range(0, N_num // 2):
#     term_o_sum += term_o
#     term_o -= 0.2
# value = (term_p_sum + term_o_sum) + (term_p * (N_num % 2))
# print(value)
#Дополнительный вариант
znak = -1
term = 1
next_term = 0
value = 0
try:
    N_num=int(input("Введите число больше 0: "))
    for i in range(0, N_num):
        znak = -znak
        term += 0.1
        next_term = term * znak
        value += next_term
    print("Значение выражения: ", value)
except:
    print("Введите целое число!")