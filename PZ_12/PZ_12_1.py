"""21 Вариант. Скляров Владимир.
    Условие:
    В последовательности на n целых элементов в первой ее половине найти
    количество положительных элементов.
    """

#Импортирование библиотеки рандом.
import random

#####ВТОРОЕ РЕШЕНИЕ#####
list_number_one = set([random.randint(-10, 20) for _ in range(random.randint(5, 13))]) #Генерация уникального множества
list_number_two = set([random.randint(-10, 20) for _ in range(random.randint(6, 12))]) #Генерация уникального множества
list_test = list_number_one - list_number_two #Вычитание, все элементы который уникальны для первого множества

#Вывод содержимого множеств
print("Элементы первого множества:", list_number_one)
print("Элементы второго множества:", list_number_two)
print("Итог. Новое множество:", list_test)

# Ответ
print(f"Среднее арифмитическое: {sum(list_test) // len(list_test)}")