"""Скляров В.Д. 21 Вариант. ИС-23
   Условие:
   В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
   фразу «Министерства образования Ростовской области», посчитать количество
   произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
   «50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.
   """

#Импортирование библиотеки.
import re

#Функция - работает с файлом.
def text_work(text):
    #Подсчитывает номера телефонов
    telephone_1 = re.findall(r"8\d{8}03", text) #Оканчив. - 03.
    telephone_2 = re.findall(r"8\d{8}50", text) #Оканчив. - 50.

    #Подсчитывает номера телефонов связанных с ЕГЭ, ГИА.
    file = re.split(r"\n", text) #Разбивает текст на отдельные строки.
    count_numbers = list() #Пустой список.
    for line in file: #Проходится по каждой значению в списке.
        if re.findall("ЕГЭ|ГИА", line): #Если находит.
            count_numbers += re.findall(r"8\d{10}", line) #Находит номер телефона в строке.
    return telephone_1 + telephone_2, count_numbers #Возвращение значений,данных.

#Открытие файла - чтение.
with open("PZ_14/hotline.txt", encoding="UTF-8") as f1:
    f2 = f1.read() #Чтение файла.
    count_line = "".join(f2) #Запись всех строк.
    telephone_one, telephone_two = text_work(f2) #Вызов функции
    print(f"Кол-во тел. номер оканчивающиеся на (03-50): {len(telephone_one)}\nКол-во тел. номеров связанных с ЕГЭ/ГИА:"
          f" {len(telephone_two)}")

#Открытие файла - запись.
with open("PZ_14/hotline.txt", "w", encoding="UTF-8") as f3: #Открытие файла в формате записи.
    #Вывод данных.
    f4 = f3.write(re.sub("«Горячая линия»", "«Горячая линия» «Министерства образования Ростовской области»", count_line))
    count_zamen = len(re.findall("«Горячая линия»", count_line))
    print(f"Кол-во замен: {count_zamen}")