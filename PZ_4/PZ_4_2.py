
i = 1
while True:
    try:
        n = int(input('Введите целое число: '))
        if n < 0:
            break
        else:
            while True:
                if i**3 < n:
                    i += 1
                else:
                    print(i**3==n)
                    break
    except Exception:
        print('Ошибка')
        continue
