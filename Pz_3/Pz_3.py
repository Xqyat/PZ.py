#1.Даны три целых числа: A, B, C. Проверить
#Проверить истинность высказывания: "Каждое из чисел
#A, B, C положительное"
try:
    first_num=int(input("Введите первое число: "))
    second_num=int(input("Введите второе число: "))
    third_num=int(input("Введите третье число: "))
    if first_num > 0 and second_num > 0 and third_num > 0:
        print("Каждое из чисел A, B, C положительное")
    else:
        print("Не каждое из чисел A, B, C положительное")
except:
    print("Введите целое число!")



