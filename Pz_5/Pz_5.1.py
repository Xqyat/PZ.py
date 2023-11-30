#Составить функцию, которая выполнит суммирование
#числового ряда
def summary():
    all_num_sum = 0
    quantity_num = int(input("Введите количество чисел, которые вы хотите ввести: "))
    while quantity_num > 0:
        num=int(input("Введите число: "))
        all_num_sum = all_num_sum + num
        quantity_num -= 1
    print("Сумма введённых вами чисел: ", all_num_sum)
summary()