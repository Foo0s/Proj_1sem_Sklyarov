"""21 Вариант. Скляров Владимир.
    Условие:
    В матрице найти минимальный элемент в предпоследней строке."""

#Импортирование библиотеки рандом
import random

#Генерация случайного размера матрицы
number = random.randint(3, 5)

#Генерация матрицы
def matrix(number):
    matrix = [[1*random.randint(10, 40) for x in range(number)] for i in range(number)] #Генерация матрицы
    yield matrix #Возвращение значения

min_number_func = 0 #Флаг

def min_number(st): #Функция, которая выводит матрицу
    global min_number_func #Глобальная переменная
    print("Вывод матрицы:")
    answ = iter(st[0]) #Итерабельный объект
    while True: #Бесконечный цикл
        try: #Обработчик ошибок
            b = next(answ) #Проходит по всем элементам в итерабельном объекте
            if b == st[0][-2]: #Провека на предпоследнюю строку
                min_number_func = min(b) #Минимальное значение
            print(*b) #вывод строк матрицы
        except StopIteration: #Обработчик ошибки - остановка
            print("Минимальное значение в предпоследней строке:", min_number_func) #Вывод итого мин. элемента
            break

#Вызов 2-ух функций
answer = list(matrix(number))
min_number(answer)