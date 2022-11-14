'''Практическая работа №6 Скляров Владимир Группа ИС-23.'''
'''Поставновка задачи
   Дан список размера N и целые числа от K и L (1<K<L<N). Найти сумму всех элементов списка,
   кроме элементов с номерами от K до L включительно.'''

from random import randint
'''Импортирование из библиотеки random функции randint.'''
def numbers_random(number_1, number_2, number_3):  #В функции 3 аргумента
    list_1 = []
    for number in range(0, number_1):   #Цикл пока индекс в диапазоне списка(от 0 до number_input).
        list_1.append(randint(1, 100))      # Добавление в список значения от 1 до 100.
    print('Изначальный список: ', list_1)
    del list_1[number_3:number_2+1]         # Удаление в списке значений от K до L
    print('Список после удаления индексов от k до L: ', list_1) # Вывод списка после удаления значений от k до l
    sums = f'Сумма списка: {sum(list_1)}'
    return sums                     # Возвращение СУММЫ списка (итоговое значение после вычета элементов от k до L)

'''Ввод/Вывод данных'''
number_input = int(input('Введите размер списка N: '))
number_L = int(input('Введите число L, оно должно быть меньше N: '))
number_K = int(input('Введите число K, оно должно быть больше 1 и меньше L: '))

if number_L >= number_input or number_L <= number_K: # Вывод ошибки если не соответствует условию.
    print('Ошибка')
elif number_K <= 1 or number_K >= number_L:
    print("Ошибка")
else:
    print(numbers_random(number_input, number_L, number_K)) # Вызов функции
