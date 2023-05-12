# Николаю треубется проверить, возможно ли из представленных
# отрезков условной длины сформировать треугольник. Для этого
# он решил создать класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения
# (в зависимости от ситуации)
# Ура, можно построить треугольник
# С отрицательными числами ничего не выйдет!
# Нужно вводить только числа!
# Жаль, но из этого треугольника не выйдет.


class TriangleChecker:
    def __init__(self, st1, st2, st3):
        self.st1 = st1
        self.st2 = st2
        self.st3 = st3

    def is_triangle(self):
        if type(self.st1) == int and type(self.st2) == int and type(self.st3) == int:
            if self.st1 < 0 or self.st2 < 0 or self.st3 < 0:
                print("С отрицательными числами ничего не выйдет!")
            elif self.st1 + self.st2 > self.st3 or self.st2 + self.st3 > self.st1 or self.st3 + self.st1 > self.st2:
                print("Ура треугольник можно построить.")
        else:
            print("Нужно вводить только числа!")

a = TriangleChecker(1, 4 , 6)
print(a.is_triangle())