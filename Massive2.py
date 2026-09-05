# Генерируем массив, состоящий из n целых положительных чисел
print("Программа вывода элементов списка, кратных 7")
n = int(input("Введите количество элементов списка --> "))

a = []

from random import randint

for i in range(n):
    a.append(randint(1, 100))

for i in range(n):
    print(a[i], end=" ")

print()

print("Числа, кратные 7:")
for i in range(len(a)):
    if a[i] % 7 == 0:
        print(a[i], end=" ")
