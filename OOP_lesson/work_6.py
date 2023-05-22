# Задача 1.

class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, x):
        self.__name = x
        return self.__name


obj_1 = Person("Владимир")
print(obj_1.get_name())
print(obj_1.set_name("Данила"))
