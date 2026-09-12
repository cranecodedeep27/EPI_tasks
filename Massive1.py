print("Программа создания и вывода целых чисел на экран")
n = int(input("Введите количество элементов списка --> "))
print()
from random import randint

a = [0] * n
for i in range(n):
    a[i] = randint(-100, 100)

print("исходный список:")
for i in range(n):
    print(a[i], end=" ")
print("\n")
# Сортируем в два списка все отрицательные, положительные
otr = []
pol = []
k_pol = 0
k_otr = 0
# формируем новые списки , параллельно подсчитываем количество
for i in range(len(a)):
    if a[i] < 0:
        otr.append(a[i])
        k_otr += 1
    elif a[i] > 0:
        pol.append(a[i])
        k_pol += 1
# выводим результаты сформированных списков
print("Итоговый список из отрицательных чисел:")
for i in range(len(otr)):
    print(otr[i], end=" ")
print()
print("Количество элементов списка =", k_otr)

print()

print("Итоговый список из положительных чисел:")
for i in range(len(pol)):
    print(pol[i], end=" ")
print()
print("Количество элементов списка =", k_pol)
