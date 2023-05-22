# Полиморфизм.

# Это возможность работы с разными объектами единым образом.

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_rect_pr(self):
        return 2*(self.y + self.x)

class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_pr(self):
        return 4*self.a


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
print(r1.get_rect_pr(), r2.get_rect_pr())
print(s1.get_sq_pr(), s2.get_sq_pr())

#################################################

geom = [r1, r1, s1, s1]
# for g in geom:
#     print(g.get_sq_pr()) #Будет ошибка т.к у r1 нет методы get_sq_pr


#Исправление ошибки.
for g in geom:
    if isinstance(g, Rectangle):
        print(g.get_rect_pr())
    else:
        print(g.get_sq_pr())
