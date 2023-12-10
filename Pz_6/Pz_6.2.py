import random as rand
N_num = rand.randint(2, 9)
List_A = []
for i in range(N_num):
    list_nums = rand.randint(1, 9)
    List_A.append(list_nums)

max_num_1 = max(List_A)
print(List_A)
List_A.remove(max_num_1)
max_num_2 = max(List_A)
print(max_num_1, max_num_2)

