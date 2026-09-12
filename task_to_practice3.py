# 3. 
from random import randint

n = int(input()) # Количесво проехавших авто (можно поставить 1000)
a = [] # Создали пустой список , куда будем складывать сгенерированные скорости n автомобилей
for i in range(n):
    a.append(randint(20, 300)) # Пусть будет диапозон скоростей от 20 до 300 км/ч
print(a)
count_60 = 0
for x in a:
    if x > 60:
        count_60 += 1
print(f"1) Количество авто проехавших со скоростью больше 60 км/ч: {count_60}")

maxx_v = 0
count_max = 0
for x in a:
    if x > maxx_v:
        maxx_v = x
for x in a:
    if x == maxx_v:
        count_max += 1

print(f"2) Максимальная скорость проехавших автомобилей = {maxx_v}")
print(f"3) Количество авто, проехавших с макс скоростью: {count_max}")

average = sum(a) / n
print(f"4) Средняя скорость, проехавших авто = {average}")

count_nizhe_average = 0
for x in a:
    if x < average:
        count_nizhe_average += 1
print(f"5) Количество авто , проехавших со скоростью ниже средней: {count_nizhe_average}")