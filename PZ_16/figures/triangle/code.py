#Дефолт. значения
a, b, c = 7, 2, 8

def triangle_plosh(st1=a, st2=b, st3=c):
    """Вычисляет периметер треугольника.
    Необходимы 3 стороны - 3 значения."""
    print(st2+st1+st3)

def triangle_area(st1, st2=b, st3=c):
    """Вычисляет плошадь треугольника.
    Необходимы 3 стороны - 3 значения."""
    pol_p = (st2 + st3 + st1) / 2
    print((pol_p * (pol_p - st1) * (pol_p - st2) * (pol_p- st3)) ** 0.5)
