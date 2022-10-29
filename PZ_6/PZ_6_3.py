import random

A = []
B = [random.randint(1, 500)]
B.append(random.randint(1, 500))
i = 0
while i <= random.randrange(1, 500):
    A.append(random.randrange(1, 500))
    i += 1
print(B)
print(A)
