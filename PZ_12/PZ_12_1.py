"""21 Вариант. Скляров Владимир.
    Условие:
    Даны две последовательности. Найти элементы, различные для двух
    последовательностей и их среднее арифметическое.
    """

#Импортирование библиотеки рандом.
import random

#####ВТОРОЕ РЕШЕНИЕ#####
list_number_one = [random.randint(-10, 20) for _ in range(random.randint(2, 8))] #Генерация уникального множества
list_number_two = [random.randint(-10, 20) for _ in range(random.randint(2, 8))] #Генерация уникального множества
list_test = list(filter(lambda x: x not in list_number_two, list_number_one)) #Сортировка элем. которые входят только в 1
list_test_2 = list(filter(lambda x: x not in list_number_one, list_number_two)) #Сортировка элем. которе вх только в 2

#Вывод содержимого множеств
print("Элементы первого множества:", list_number_one)
print("Элементы второго множества:", list_number_two)
print("Итог. Новое множество:", list_test+list_test_2)

# Ответ
print(f"Среднее арифмитическое: {sum(list_test+list_test_2) // len(list_test+list_test_2)}")