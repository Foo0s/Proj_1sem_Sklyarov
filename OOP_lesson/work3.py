# Создайте класс Список, который имеет методы для добавления
# и удаления элементов, поиска элемента и сортировк списка.
# Создать экземпляр класса и выполнить в нем следующие действия
# 1. Заполнить список 15 случайными числами.
# 2. Проверить наличие в списке элемента со значением 2
# и удалить его из списка
# 3. Выполнить сортировку оставшихся элементов
# Резултаты работы вывести в консоль

import random

class Listings:

    def __init__(self, number):
        """Содержит массив - список из рандомных чисел"""
        self.list = [random.randint(1, 60) for i in range(number)]

    def upload_list(self, number_new):
        """Функция, которая добавляет новое значение в массив."""
        self.list.append(number_new)
        return f"Значение {number_new} было добавлено"

    def checked_and_delete(self):
        print(f"Изначальный массив: {self.list}")
        print("Количество найденных 2 в массиве: {}".format(len([i for i in self.list if i == 2])))
        for i in self.list:
            if i == 2:
                del self.list[self.list.index(i)]
        print("Отсортированный массив: ",sorted(self.list))


#Создание экземпляра.
prog1 = Listings(10)
prog1.upload_list(2)
print(prog1.checked_and_delete())
