from math import sqrt

A = float(input("Введите A: "))
B = float(input("Введите B: "))

if A < B:
    print("Ошибка: A − B должно быть неотрицательным.")
elif B == 0:
    print("Ошибка: знаменатель равен нулю.")
else:
    numerator = sum(i ** A for i in range(2, 17, 2))
    denominator = sum(i * B for i in range(3, 18, 2))
    C = sqrt(A - B) + numerator / denominator
    print("C =", C)