#21 Вариант Скляров
'''Дано целое положительное число. Вывести символы, изображающие цифры этого
числа (в порядке справа налево)..'''

try:
    number = int(input('Введите число: ')) # Ввод числа
    list_1 = list() # создание пустого списка
    print("Изначальное число: ", number)
    stringg = [] # пустой список
    for i in str(number): # перебирает все элементы в введенном числе.
        list_1.append(int(i)) # добавление в список всех элементов в int формате
    for id in list_1:
        stringg.append(chr(id)) #  преобразует каждый элемент(цифру) в символьный аналог.
    print("Символы изображающие эти цифры:", stringg[::-1]) # Вывод
except ValueError:
    print('Ошибка') # Обработчик исключений - вывод ошибки если блок try не выполняется
