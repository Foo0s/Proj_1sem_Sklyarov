import random

c = int(input('Введите число: '))
if c % 2 == 0:
    A = [random.randint(0, 100) for a in range(c)]
a, b =int(input('Введите x координату для точки: ')), int(input('Введите y координату для точки: '))
B = []
B.append(a)
B.append(b)
for n in A:
    c = 1 / (A[n+2] - A[n])**2
print(c)
print(B)
print(A)

