"""21 Вариант. Скляров Владимир.
    Условие:
    В матрице найти минимальный элемент в предпоследней строке."""

#Импортирование библиотеки рандом
import random

#Генерация случайного размера матрицы
number = random.randint(3, 5)

#Генерация матрицы
def matrix(number):
    matrix = [[1*random.randint(10, 40) for x in range(number)] for i in range(number)]
    yield matrix

def min_number(st):
    answ = iter(st)
    c = 0
    while True:
        b = next(answ)
        c += 1
        print(b)
        if c == len(st)-1:
            break
    print(answ)

answer = list(matrix(number))
for k in answer:
    for n in k:
        print(n, end='\n')
min_number(answer)