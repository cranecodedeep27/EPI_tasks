# Программа №3
# Вводим переменные
n = int(input("Сколько элементов вы хотите в массиве? Введите число --> "))

a = []
# Объявление переменных
summa_pol = 0  # положительные
summa_otr = 0  # отрицательные
summa_chet = 0  # четные
pro_nechet = 1  # нечетные
k_0 = 0  # количество нулевых значений

# Генерация списка
from random import randint

for i in range(n):
    a.append(randint(-300, 300))  # можно задать свой диапазон
for i in range(n):
    print(a[i], end=" ")

print()
# ставим условия:
for i in range(len(a)):
    if a[i] > 0:
        summa_pol += a[i]
        if a[i] % 2 == 0:
            summa_chet += a[i]
        else:
            pro_nechet *= a[i]
    elif a[i] < 0:
        summa_otr += a[i]
        if a[i] % 2 == 0:
            summa_chet += a[i]
        else:
            pro_nechet *= a[i]
    else:
        k_0 += 1
# выводим результаты:
print("Сумма положительных чисел:", summa_pol)
print("Сумма отрицательных чисел:", summa_otr)
print("Сумма чётных чисел:", summa_chet)
print("Произведение нечётных чисел:", pro_nechet)
print("Количество нулевых элементов:", k_0)
