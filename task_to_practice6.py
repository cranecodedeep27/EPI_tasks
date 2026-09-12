# 6.
from random import randint

# Создаём новый массив c (на 15 элементов) и заполняем его новыми целыми случайными числами от 10 до 100
c, nc = list(), 15
for i in range(nc):
    c.append(randint(10, 100))
print(f"Новый массив c: {c}")

average_c = sum(c) / nc
print(f"Среднее значение элементов массива c: {average_c}")

c_bolshe_average = []
for x in c:
    if x > average_c:
        c_bolshe_average.append(x)
print(
    *c_bolshe_average,
    "- значения элементов массива c, которые больше среднего арифметического",
)
