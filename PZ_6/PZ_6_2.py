'''21 Вариант Скляров Владимир. Группа: ИС-23.'''

'''
   Дан целочисленный список размера N. Если он является перестановкой, то есть
   содержит все числа от 1 до N, то вывести 0; в противном случае вывести номер
   первого недопустимого элемента.'''

try:
    number = int(input("Введите число: "))
    list_1 = []
    for i in range(1, number+1):
        list_1.append(i)
    n = [i for i in range(1, number+1)]
    if list_1 == n:
        print(0)
    else:
        m = 0
        print(list_1)
        print(n)
        for i in list_1:
            if m == len(n):
                m = m - 1
            if i != n[m]:
                print(f"Первый недопустимый элемент: {m}")
            m += 1

except ValueError:
    print("Ошибка")
