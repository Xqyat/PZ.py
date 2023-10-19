#Дано двузначное число. Найти сумму и произведение его цифр
try:
  a = int(input("Введите двузначное число: "))
  if 10<a<100:
    first_num = a % 10
    second_num = a // 10
    sum_f_s = first_num + second_num
    multi_f_s = first_num * second_num
    print("Сумма цифр числа", a,": ", sum_f_s)
    print("Произведение цифр числа", a,": ", multi_f_s)
  else:
    print("Введите двузначное число!")
except:
  print("Введите число!")