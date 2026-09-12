# 2. 
from random import randint

n = 15
a = [0] * n
for i in range(n):
    a[i] = randint(0, 100)

print(a)
# 1)
maxx_el = max(a)
minn_el = min(a)
print("1)")
print(f"{maxx_el} - максимальный элемент списка")
print(f"{minn_el} - минимальный элемент списка")

# 2)
average = sum(a) / n
print(f"2) Среднее значение массива = {average}")

# 3)
count = abs(a.index(maxx_el) - a.index(minn_el)) - 1
print(f"3) Количество элементов между макс и мин значениями: {count}")

# 4)
for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] *= 3
    if a[i] % 2 != 0:
        a[i] -= 4
print(f"4) Изменённый массив по пункту 4: {a}")

# 5)
for i in range(len(a)):
    if a[i] == 0:
        a[i] = 1
    if a[i] == 1:
        a[i] == 0
print(f"5) Изменённый массив по пункту 5: {a}")
