# 1. 
from random import randint

n = 50  # количество претендентов на баскетбол
a = [0] * n  # Пустой список из баскетболистов
for i in range(n):
    a[i] = randint(150, 200)  # генерируем рост всех 50 баскетболистов

# print(a)
count = 0
for x in a:
    if x >= 170:
        count += 1
print(f"{count} - cтолько человек прошло отбор в баскетбольную команду")
