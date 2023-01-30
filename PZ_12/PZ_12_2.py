"""21 Вариант. Скляров Владимир.
    Условие:
    Из заданной строки отобразить только цифры. Использовать библиотеку string.
    Строка - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand
    481 feet (147 metres) high.
    """
#Импортирование библиотеки string.
import string

#Задание второе.
string_from_work = "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet" \
                   " (147 metres) high." #Данная строка по условию
#Проверка каждого элемента в строке.
list_digit_from_string = list(filter(lambda x: x in string.digits, string_from_work)) #Добавляет только True
print(list_digit_from_string) #Вывод