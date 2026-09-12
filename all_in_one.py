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
print(f"Количество авто проехавших со скоростью больше 60 км/ч: {count_60}")

maxx_v = 0
for x in a:
    if x > maxx_v:
        maxx_v = x
print(f"Максимальная скорость проехавших автомобилей = {maxx_v}")

average = sum(a) / n
print(f"Средняя скорость, проехавших авто = {average}")

b, nb = list(), int(input())
count_chet_otr = 0
for i in range(nb):
    b.append(randint(-50, 50)) # генерируем новый список b , где будут отрицательные числа
print(b)
minn_el = min(b)
print(f"Минимальное значение в списке b: {minn_el}") # его будем заменять на 100

for i in range(len(b)):
    if b[i] < 0 and b[i] % 2 == 0:
        count_chet_otr += 1
    
    if b[i] == minn_el:
        b[i] = 100
print(f"Количесво чётных отрицательных элементов в списке b = {count_chet_otr}")
print(f"Массив в котором все минимальные значения элементов заменены на 100: {b}")

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
print(*c_bolshe_average, "- значения элементов массива c которые больше среднего арифметического")

# Создаём новый массив d, где будем менять элементы k1 и k2 местами:
d, nd = list(), 5
for i in range(nd):
    d.append(randint(0, 100))
print(f"вот созданный массив: {d}")
# Теперь надо поменять k1 и k2 местами (так понимаю, что 1 и 2 это индексы элементов списка)
k1 = d[1]
k2 = d[2]
# теперь меняем их местами и выводим изменённый список:
d[1], d[2] = d[2], d[1]
print(f"Изменённый список: {d}")