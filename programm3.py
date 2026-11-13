N = int(input("Введите количество членов ряда: "))

if N < 1:
    print("Количество должно быть положительным.")
else:
    a = 1
    summa = 0
    product = 1

    for n in range(1, N + 1):
        if n > 1:
            a = 1 + a ** n

        if a % 2 == 0:
            summa += a
        else:
            product *= a

    print("Сумма чётных чисел:", summa)
    print("Произведение нечётных чисел:", product)