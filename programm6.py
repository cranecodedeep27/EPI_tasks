X = float(input("Введите X: "))
Y = float(input("Введите Y: "))

if X == 0:
    print("Ошибка: X не должен быть равен нулю.")
elif X * Y < 0:
    print("Ошибка: XY должно быть неотрицательным.")
else:
    B = 2 ** (Y / X)

    for n in range(2, 12):
        B += (n * X * Y) ** (1 / n)

    print("B =", B)