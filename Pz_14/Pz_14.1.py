#1. В исходном текстовом файл() найти все даты
#в форматах ДД.ММ.ГГГГ и ДД/ММ/ГГГГ. Посчитать
#количество дат в каждом формате. Поместить в новый
#текстовый файл все даты февраля в формате ДД/ММ/ГГГГ
import re
dates = open("dates.txt")
text = dates.read()
right_format_point = re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", text)
right_format_slash = re.findall(r'\d{2}/\d{2}/\d{4}' , text)
count_point = len(right_format_point)
count_slash =len(right_format_slash)
print(right_format_point)
print(right_format_slash)
print("Количество дат в формате ДД.ММ.ГГГГ:", count_point)
print("Количество дат в формате ДД/ММ/ГГГГ:", count_slash)
new_data = open("Slash.txt", 'w')
new_text = [date + '\n' for date in right_format_slash]
new_data.writelines(new_text)