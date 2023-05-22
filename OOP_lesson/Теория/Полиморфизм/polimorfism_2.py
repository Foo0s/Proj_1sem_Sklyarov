# Полиморфизм - урок 2.

class Rectagle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def get_pr(self):
        return 2*(self.w + self.h)

class Triangle:
    def __init__(self, st_1, st_2, st_3):
        self.st_1 = st_1
        self.st_2 = st_2
        self.st_3 = st_3

    def get_pr(self):
        return self.st_3 + self.st_2 + self.st_1

class Square:
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4*self.a

# Список
gnome = [Rectagle(10, 20), Rectagle(30, 40),
         Triangle(10, 10, 3), Triangle(20, 40, 1),
         Square(3), Square(4), Square(8)]

for i in gnome:
    print("Периметр равен: ", i.get_pr())
    print()



