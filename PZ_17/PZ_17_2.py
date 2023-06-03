#Скляров Владимир Дмитриевич. Группа - ИС-23.
# 21 Вариант.

#Условие: Создайте базовый класс 'Животное' со свойствами 'вид', 'количество лап', 'цвет шерсти'. От этого
# класса унаследуйте класс 'Собака' и добавьте в него свойства 'кличка', 'порода'


class Animals:
    def __init__(self, vid, number, color_sh):
        """Инициализация данных."""
        self.vid = vid
        self.number_l = number
        self.color_sh = color_sh


class Dog(Animals):
    """Инициализация данных."""
    def __init__(self, klich, poroda):
        self.klich = klich
        self.poroda = poroda


#Вывод данных.
animal_1 = Animals("Немецкая овчарка", 4, "Темно-коричневый") #1-ый объект.
print(animal_1.vid)
print(animal_1.number_l)
print(animal_1.color_sh)

print()
animal_2 = Dog("Бобик!", "Бутельер") #2-ой объект.
print(animal_2.klich)
print(animal_2.poroda)
