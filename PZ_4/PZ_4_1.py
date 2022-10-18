while True:
    try:
        x = float(input('Введите вещественное число, оно должно быть меньше 1 и больше -1: '))
        n = int(input('Введите целое число, оно должно быть больше 0: '))
        number = 0
        a = 0
        if x > 1 or x < -1:
            continue
        if n < 0:
            continue
        else:
            while number != n:
                ln = -1**n-1 * x**n // n
                number += 1
                a += ln
                print(a)
                break
        break
    except Exception:
        print('Ошибка')
        continue