"""21 Вариант. Скляров Владимир. ИС-23
    Условие:
    В квадратной матрице элементы на главной диагонали увеличить в 2 раза.
    """

#Импортирование библиотек
import random

#Генерация рандомного четного числа.
def random_number():
    number = random.randint(2, 6)
    return number

#Создание матрицы.
def matrix(n):
    matrix_sq = [[random.randint(1, 30) for i in range(number)] for k in range(number)] #Генератор матрицы
    yield matrix_sq #Возвращает значение

#Вывод матрицы.
def print_matrix(matrix): # Функция которая работает с итер. объектом. Выводя результат
    iter_object = iter(matrix[0]) #Итерируемый объект с индексом 0
    print("Вывод матрицы")
    while True:
        try:
            el_matrix = next(iter_object) # Проходит по каждому элементу
            print(*el_matrix) # Вывод каждый элемент
        except StopIteration: # обработчик ошибок
            print("StopIteration. Операция закончилась.\n")
            break # Остановка цикла

    print("Вывод измененной матрицы\n")

    iter_object_two = iter(matrix[0])
    chet = 0 # Счетчик
    while True:
        try:
            el_matrix_two = next(iter_object_two)
            el_matrix_two[chet] *= 2 # Умножение каждого элемента на главной диагонали
            print(*el_matrix_two)
            chet += 1 # Прибавление к счетчику значений.
        except StopIteration:
            print("StopIteration. Операция закончилась.")
            break # Остановка цикла

number = random_number() # Вызов 1-й функции, генерация ранд. числа
a = list(matrix(number)) # Вызов 2-й функции, генерация матрицы. В list - списке.
print_matrix(a) # Вызов 3-й функции. Вывод матрицы. Вывод измененной матрицы.