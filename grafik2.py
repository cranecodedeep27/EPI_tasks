from math import sqrt
import turtle as tr


# Функция, заданная графиком
def f(x):
    if x < -2:
        return x + 3
    elif x < 4:
        return -x / 2
    elif x < 6:
        return -2
    else:
        return -2 + sqrt(max(0, 4 - (x - 8) ** 2))


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
    n = max(1, int(length / 0.13))

    for i in range(0, n, 2):
        a = i / n
        b = min((i + 1) / n, 1)
        line(
            x1 + (x2 - x1) * a,
            y1 + (y2 - y1) * a,
            x1 + (x2 - x1) * b,
            y1 + (y2 - y1) * b
        )


# Стрелка
def arrow(x1, y1, x2, y2, size=0.16):
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


# Настройка окна
tr.setup(1100, 400)
tr.title("График функции 2")
tr.setworldcoordinates(-5, -3, 11.2, 2.7)
tr.bgcolor("white")
tr.hideturtle()
tr.speed(0)
tr.tracer(0)

# Координатные оси
tr.color("black")
tr.pensize(1)
arrow(-4.4, 0, 10.9, 0)
arrow(0, -2.4, 0, 2)

label(10.65, 0.15, "X", 16)
label(0.4, 1.6, "Y", 16)

# Деления на осях
for x in range(-4, 11):
    line(x, 0, x, -0.1)

for y in (-2, -1, 1):
    line(0, y, 0.1, y)

# Подписи
for x in (-4, 4, 6):
    label(x, 0.08, str(x))

label(-2, -0.65, "-2")
label(10, -0.65, "10")
label(0.2, 0.02, "0")
label(0.2, 0.83, "1")
label(0.2, -1.17, "-1", align="left")
label(-0.2, -2.17, "-2", align="right")

# Вспомогательные линии
tr.color("gray")
dashed(-4, 0, -4, -1)
dashed(-4, -1, 0, -1)
dashed(-2, -0.1, -2, 1.25)
dashed(-2, 1, 0, 1)
dashed(4, 0, 4, -2)
dashed(6, 0, 6, -2)
dashed(0, -2, 10.2, -2)
dashed(8, 0, 8, -2)

# Построение графика с шагом 0.01
tr.color("black")
tr.pensize(2.5)
tr.penup()
tr.goto(-4, f(-4))
tr.pendown()

for i in range(1, 1401):
    x = -4 + i / 100
    tr.goto(x, f(x))

tr.penup()

# Радиус полуокружности: R = 2
tr.color("dimgray")
tr.pensize(1)
arrow(8, -2, 8 + sqrt(2), -2 + sqrt(2))

tr.color("black")
label(9.25, -1.6, "R", 16)

tr.update()
tr.done()