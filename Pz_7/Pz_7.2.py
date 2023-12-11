# Дана строка-предложение на русском языке. Вывести самое короткое слово в предложению.
# Если таких слов несколько, то вывести последнее из них. Словом считать набор символов,
# не содержащий пробелов, знаков препинания и ограниченный пробелами, знаками препинания
# или началом/концом строки
words = []
cur_word = ""
S_str = input("Напишите непустое предложение: ")
for i in S_str:
    if i.isalpha():
        cur_word += i

    elif cur_word:
        words.append(cur_word)
        cur_word = ""

if cur_word:
    words.append(cur_word)

result = words[0]

for i in words[1:]:
    if len(i) <= len(result):
        result = i
print(result)