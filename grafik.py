from math import sqrt
import turtle as tr


# Функция, заданная графиком
def f(x):
    if x < -5:
        return -3
    elif x < -3:
        return 1.5 * (x + 3)
    elif x <= 3:
        return sqrt(max(0, 9 - x ** 2))
    elif x < 8:
        return 0.6 * (x - 3)
    else:
        return 3


# Отрезок
def line(x1, y1, x2, y2):
    tr.penup()
    tr.goto(x1, y1)
    tr.pendown()
    tr.goto(x2, y2)
    tr.penup()


# Надпись
def label(x, y, text, size=12, align="center"):
    tr.penup()
    tr.goto(x, y)
    tr.write(text, align=align, font=("Arial", size, "normal"))


# Пунктирный отрезок
def dashed(x1, y1, x2, y2):
    length = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    n = max(1, int(length / 0.15))

    for i in range(0, n, 2):
        a = i / n
        b = min((i + 1) / n, 1)
        line(
            x1 + (x2 - x1) * a,
            y1 + (y2 - y1) * a,
            x1 + (x2 - x1) * b,
            y1 + (y2 - y1) * b
        )


# Стрелка на конце отрезка
def arrow(x1, y1, x2, y2, size=0.18):
    line(x1, y1, x2, y2)
    length = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    ux = (x2 - x1) / length
    uy = (y2 - y1) / length

    tr.goto(x2, y2)
    tr.pendown()
    tr.begin_fill()
    tr.goto(x2 - size * ux - size * uy / 2,
            y2 - size * uy + size * ux / 2)
    tr.goto(x2 - size * ux + size * uy / 2,
            y2 - size * uy - size * ux / 2)
    tr.goto(x2, y2)
    tr.end_fill()
    tr.penup()


# Настройка окна и системы координат
tr.setup(1000, 460)
tr.title("График функции")
tr.setworldcoordinates(-9, -4.2, 11.2, 4.8)
tr.bgcolor("white")
tr.hideturtle()
tr.speed(0)
tr.tracer(0)

# Координатные оси
tr.color("black")
tr.pensize(1)
arrow(-8, 0, 10.5, 0)
arrow(0, -3.6, 0, 4)

label(10.45, 0.22, "X", 16)
label(-0.4, 3.65, "Y", 16)

# Деления на осях
for x in range(-8, 11):
    line(x, 0, x, -0.13)

for y in range(-3, 4):
    if y != 0:
        line(-0.13, y, 0, y)

# Подписи, как на исходном рисунке
for x in (-8, -4, -3, 3, 8, 10):
    label(x, -0.65, str(x))

label(-5, 0.2, "-5")
label(0.28, -0.55, "0")
label(0.22, 3.02, "3", align="left")
label(-0.35, -3.2, "-3", align="right")

# Вспомогательные пунктирные линии
tr.color("gray")
dashed(-5, 0, -5, -3)
dashed(-5, -3, 0, -3)
dashed(0, 3, 8, 3)
dashed(8, 0, 8, 3)

# График: вычисляем y по формуле для каждого x
tr.color("black")
tr.pensize(2.5)
tr.penup()
tr.goto(-8, f(-8))
tr.pendown()

# Шаг 0.01; все точки соединения участков включены
for i in range(1, 1801):
    x = -8 + i / 100
    tr.goto(x, f(x))

tr.penup()

# Радиус полуокружности
tr.pensize(1)
tr.color("dimgray")
r = 3 / sqrt(2)
arrow(0, 0, -r, r)
tr.color("black")
label(-1.55, 0.75, "R", 15)

tr.update()
tr.done()