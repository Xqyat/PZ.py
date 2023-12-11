#Дан список размера N и целое число K (1 < K < N).
#Осуществить сдвиг элементов списка вправо на K позиций
#(при этом А(1) перейдёт в А(к+1), А(2) - в А(к+2), ..А(N-K) - в
#А(N), а исходное значение К последних элементов будет потеряно)
#Первые К элементов полученного списка положить равными 0
import random as rand
N_num = rand.randint(4, 8)
K_num = rand.randint(2, N_num-1)
print(K_num)
List_A = []
for i in range(N_num):
    list_nums = rand.randint(1, 9)
    zero_list = [0] * N_num
    List_A.append(list_nums)
print(List_A)
for i in range(K_num):
    zero_list [i + K_num] = List_A [i]
print(zero_list)