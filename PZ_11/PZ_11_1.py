#21 вариант Скляров Владимир.
'''Задача:
    1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
    последовательности из целых положительных и отрицательных чисел. Сформировать
    новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
    обработку элементов:
    Содержимое первого файла:
    Отрицательные элементы:
    Количество отрицательных элементов:
    Среднее арифметическое:

    Содержимое второго файла:
    Положительные элементы:
    Количество положительных элементов:
    Сумма положительных элементов:
    2. Из предложенного текстового файла (text18-21.txt) вывести на экран его содержимое,
    количество знаков препинания. Сформировать новый файл, в который поместить текст в
    стихотворной форме выведя строки в обратном порядке.
'''

import random

#Создание первого файла.
f1 = open("file_1.txt", "w", encoding="UTF-8")
list_1 = [random.randint(-10, 20) for i in range(random.randint(1, 20))]
list_2 = [i for i in list_1 if i < 0]
f1.write("Содержимое первого файла: \n")
f1.writelines(f"Отрицательные элементы: {list_2}\n")
f1.write(f"Количество отрицательных элементов: {len(list_2)}\n")
f1.write(f"Среднее арифмитическое: {sum(list_2) / len(list_2) if len(list_2) > 0 else 0}")
f1.close()

#Создание второго файла.
f1 = open("file_2.txt", "w", encoding="UTF-8")
list_1 = [random.randint(-10, 20) for i in range(random.randint(1, 20))]
list_2 = [i for i in list_1 if i < 0] # Отрицательные элементы
list_3 = [i for i in list_1 if i > 0] # Положительные элементы
f1.write("Содержимое второго файла: \n")
f1.writelines(f"Положительные элементы: {list_3}\n")
f1.write(f"Количество положительных элементов: {len(list_3)}\n")
f1.write(f"Сумма элементов: {sum(list_3)}")
f1.close()
