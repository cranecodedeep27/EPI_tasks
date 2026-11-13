X = float(input("Введите X: "))
Y = float(input("Введите Y: "))

if Y == 0:
    print("Ошибка: деление на ноль.")
else:
    s = sum((i * X) / (i * Y) for i in range(3, 79, 3))

    root = abs(s) ** (1 / 5)
    if s < 0:
        root = -root

    K = 2 * X - Y + root
    print("K =", K)