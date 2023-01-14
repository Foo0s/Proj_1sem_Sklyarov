"""21 Вариант. Скляров Владимир Дмитриевич.
    Задача....
    2. Из предложенного текстового файла (text18-21.txt) вывести на экран его содержимое,
    количество знаков препинания. Сформировать новый файл, в который поместить текст в
    стихотворной форме выведя строки в обратном порядке.
"""

#Открытие файла
from typing import TextIO

f1 = open("text18-21.txt", "r", encoding="UTF-8")
f2 = f1.read()
score = 0 # счетчик
for i in f2:
    print(i, end='')
for n in range(len(f2)):
    if f2[n] in ",.!?;:":
        score += 1
print(f"\n\nКоличество знаков препинаний: {score}\n")
f1.close()

#Создание нового файла.
f4 = open("zadanie_2.txt", "r", encoding='UTF-8')
f3 = reversed(f4.readlines())
list_3 = []
for i in f3:
    list_3.append(i)
f4.close()
print(list_3)

#Запись в файл данных.
f4 = open("zadanie_2.txt", "w+", encoding="UTF-8")
for i in list_3:
    print(i)
    f4.write(i)
list_3 = []
f4.close()