X = float(input("Введите X: "))
Y = float(input("Введите Y: "))

if Y == 0:
    print("Ошибка: деление на ноль.")
else:
    numerator = sum((i / 10) * X for i in range(3, 26, 2))
    B = numerator / (1.033 * Y)
    print("B =", B)