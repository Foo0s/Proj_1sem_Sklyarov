'''Практическая работа №5 задание 2. Выполнил Скляров Владимир. Группа - ИС-23.'''
'''Постановка задача
   Описать Функцию Powerl(A,B) вещественного типа, находящую величину AB по формуле
   AB=exp(B*ln(A))(параметры А и В - вещественные). В случае нулевого или отрицательного значения А
   функция возвращает 0. С помощью этой функции найти степень A**P, B**P, C**P, если даны числа A, B, C'''

import math
'''Импортирование математической библиотеки'''

def Powerl(A, B): ##Функция в которой происходит возведение в степень аргумента A в B.
    if A <= 0:     # Если переданный аргумент A меньше 1, то функция возвращает значение 0.
        return 0
    AB = math.exp(B*math.log(A))    # Возведение в степень.
    return round(AB, 5)             # Возвращение округлённого значения AB до 5 знаков, после запятой.

try:                                # Блок обработчика исключений.
    number_A = float(input('Введите вещественное число: '))     # Ввод данных 1 переменная.
    number_B = float(input('Введите вещественное число: '))     # Ввод данных 2 переменная.
    number_C = float(input('Введите вещественное число: '))     # Ввод данных 3 переменная.
    number_P = float(input('Введите второе вещественное число: '))  # Ввод данных 4 переменная, значение степени.
    print(Powerl(number_A, number_P))   # Вывод полученного значения для 1 переменной.
    print(Powerl(number_B, number_P))   # Вывод полученного значения для 2 переменной.
    print(Powerl(number_C, number_P))   # Вывод полученного значения для 3 переменной.
except Exception:                       # Обработчик исключений - вывод Ошибки если введённые данные не в float типе.
    print('Ошибка вы ввели не корректное число!')