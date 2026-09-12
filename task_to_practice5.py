# 5.
from random import randint

b, nb = list(), int(input())
count_chet_otr = 0
for i in range(nb):
    b.append(
        randint(-50, 50)
    )  # генерируем новый список b , где будут отрицательные числа
print(b)
minn_el = min(b)
print(f"Минимальное значение в списке b: {minn_el}")  # его будем заменять на 100

for i in range(len(b)):
    if b[i] < 0 and b[i] % 2 == 0:
        count_chet_otr += 1

    if b[i] == minn_el:
        b[i] = 100
print(f"Количесво чётных отрицательных элементов в списке b = {count_chet_otr}")
print(f"Массив в котором все минимальные значения элементов заменены на 100: {b}")
