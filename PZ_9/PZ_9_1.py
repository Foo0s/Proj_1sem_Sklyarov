'''
21 Вариант Скляров. Практическая работа №9.
Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
информацию из строки в словарь, найти среднее арифметическое оценок,
результаты вывести на экран.
'''

stri = "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4" # Данная нам строка
student = {} # Создание пустого словаря
a = stri.split() # Разбиение строки на отдельные массивы.
student["Фамилия"] = a[0]
student["Имя"] = a[1]
student["Группа"] = a[2]
student["Оценки"] = a[3::]
number = 0 # Счетчик

'''Функция которая считает среднее арифмитическое оценок студента.'''
def podshet(number):
    for i in a[3::]: #Цикл который проходится по каждому значению в массиве a
        number += int(i)
        if i == a[-1]:
            b = number / len(a[3::])
    return b                    # Возвращение значения

'''Вывод'''
student["Среднее арифмитическое"] = podshet(number)
'''Вывод данных.'''
print(student)
