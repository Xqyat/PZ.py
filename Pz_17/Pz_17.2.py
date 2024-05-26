#2. Разработать программу с применением пакета tk, взяв в качестве
# условия одну любую задачу из ПЗ № 2 – 9.


#Дано двузначное число. Найти сумму и произведение его цифр
from tkinter import *

root = Tk()
root.title("Pz_17.2")
root.geometry('700x400')

label = Label(text = "Введите двузначное число: ")
label.pack()

entry = Entry()
entry.pack()

def on_clicked():
    try:
        a = int(entry.get())
        if 10 < a < 100:
            first_num = a % 10
            second_num = a // 10
            sum_f_s = first_num + second_num
            multi_f_s = first_num * second_num
            label_1.config(text=f"Сумма цифр числа {a}: {sum_f_s}", fg="black")
            label_2.config(text=f"Произведение цифр числа {a}: {multi_f_s}", fg="black")
        else:
            label_1.config(text="Введите двузначное число!!!!!", fg="red")
            label_2.config(text="")
    except:
        label_1.config(text="Введите число!!!!!", fg="red")
        label_2.config(text="")
label_1 = Label(root)
label_2 = Label(root)
label_1.pack()
label_2.pack()

button = Button(root,
text = "Вычислить",
width = 50,
command = on_clicked)
button.pack()

root.mainloop()