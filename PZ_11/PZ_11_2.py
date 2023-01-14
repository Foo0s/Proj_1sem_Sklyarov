#Открытие файла
from typing import TextIO

f1 = open("text18-21.txt", "r")
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
f4 = open("zadanie_2.txt", encoding='UTF-8')
f2 = f4.readlines()
for i in f2[::-1]:
    f4.write(i)