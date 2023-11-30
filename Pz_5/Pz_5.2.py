# Описать функцию SortDес3(А, В, С), меняющую содержимое переменных А, В, С
#таким образом, чтобы их значения оказались упорядоченными по убыванию (А, В,
#С — вещественные параметры, являющиеся одновременно входными и
#выходными). С помощью этой функции упорядочить по убыванию два данных
#набора из трех чисел: (А1, В1, С1) и (А2, В2, С2).
num_a = int(input("Введите число: "))
num_b = int(input("Введите число: "))
num_c = int(input("Введите число: "))
num_a1 = int(input("Введите число: "))
num_b1 = int(input("Введите число: "))
num_c1 = int(input("Введите число: "))
def SortDес3(num_a, num_b, num_c):
    if num_c < num_b < num_a:
        return num_a, num_b, num_c
    elif num_b < num_c < num_a:
        return num_a, num_c, num_b
    elif num_b == num_c and num_a > num_c:
        return num_a, num_b, num_c

    elif num_a < num_c < num_b:
        return num_b, num_c, num_a
    elif num_c < num_a < num_b:
        return num_b, num_a, num_c
    elif num_a == num_c and num_a:
        return num_b, num_c, num_a

    elif num_a < num_b < num_c:
        return num_c, num_b, num_a
    elif num_b < num_a < num_c:
        return num_c, num_a, num_b
    elif num_b == num_a and num_c:
        return num_c, num_b, num_a

    else:
        return num_c, num_b, num_a

print(SortDес3(num_a, num_b, num_c))
print(SortDес3(num_a1, num_b1, num_c1))