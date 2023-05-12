# #Напишите программу по следующему описанию:
#
# 1.Есть класс Person, конструктор которого принимает три параметра (не учитывая self) –
# имя, фамилию и квалификацию специалиста. Квалификация имеет значение заданное по умолчанию, равное единице.
#
# 2. У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.
#
# 3. Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер …"
# (вместо троеточия должны выводиться имя и фамилия объекта).
#
# 4. В основной ветке программы создайте три объекта класса Person.
# Посмотрите информацию о сотрудниках и увольте самое слабое звено.
#
# 5. В конце программы добавьте функцию input(), чтобы скрипт не завершился сам,
# пока не будет нажат Enter. Иначе вы сразу увидите как удаляются все объекты при завершении работы программы.

class Person:
    def special(self, name, surname, kval=1):
        self.name = name
        self.surname = surname
        self.kval = kval

    def infor(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nКвалификация: {self.kval}\n"

    def destruction(self):

        string_p = f"До свидания, мистер {self.name}"
        if getattr(self.name, self.surname, self.kval):
            info = [self.name, self.surname, self.kval]
            for i in info:
                del i
        print(string_p)

obj1 = Person()
obj1.special("Геннадий", "Васильевич", "Программист")
obj2 = Person()
obj2.special("Лариса", "Васильевна", "Инженер")
obj3 = Person()
obj3.special("Владимир", "Туроев", "Историк")

print(obj1.infor())
print(obj2.infor())
print(obj3.infor())

obj3.destruction()
print("Нету" if obj3.name else obj3.name)