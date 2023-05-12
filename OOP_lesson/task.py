
class Point:
    "Класс который выводит информацию"

    color = 'red'
    circle = 2

# Вывод информации.
print(Point.color, Point.circle)
print(Point.__doc__)

#Экземпляр класса.
pointOne = Point()
print(pointOne.circle)

pointTwo = Point()
print(pointTwo.color)

#Изменение значения в классе.
Point.color = "green"

print(pointOne.color)
print(pointTwo.color)

pointTwo.color = 'orange'
print(pointTwo.color)
print(pointOne.color) #Не изменяется.

#Добавление атрибутов.
Point.more = True
Point.inner = False
pointTwo.prem = 34

print(Point.more, Point.inner)
print(pointTwo.prem)

#Удаление атрибутов.
#Функция getattr проверяет наличие атрибута у класса.
#Функция hasattr та же проверяет. - удаляет.

#Проверка на наличие.
print("\n", 1)
print(getattr(Point, "more"))
print(getattr(Point, "circle"))
print(hasattr(pointTwo, "prem")) #Наличие.

#Удаление.
if hasattr(Point, "more"):
    del Point.more

print(getattr(Point, "more"))
