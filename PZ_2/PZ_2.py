'''21 Вариант Скляров'''
'''
   Дано трехзначное число. Вывести число, полученное при
   перестановке цифр десятков и единиц исходного числа (например, 123 перейдет в 132).'''

try:
    number = int(input("Введите число: "))
    if 100 <= number <= 999:
        print(f"Значение после перестановки: {int(str(number // 100) + str(number % 10) + str((number // 10) % 10))}")
    else:
        print("Неверное значени!")
except ValueError:
    print("Неверное значение!")