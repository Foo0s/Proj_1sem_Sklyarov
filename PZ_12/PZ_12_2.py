"""21 Вариант. Скляров Владимир.
    Условие:
    Из заданной строки отобразить только символы нижнего регистра. Использовать
    библиотеку string. Строка'In PyCharm, you can specify third-party standalone applications and
    run them as External Tools'.
    """
#Импортирование библиотеки string.
import string

#Задание второе.
string_from_work = "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet" \
                   " (147 metres) high." #Данная строка по условию
list_digit_from_string = [i for i in string_from_work if i in string.digits] #Генератор который проходит по всем элем.
print(list_digit_from_string) #Вывод