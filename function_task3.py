print('Введите Xbeg, Xend, Dx и Eps')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
eps = float(input('Eps='))

print("+--------+---------+------+")
print("I   X    I    Y    I   N  I")
print("+--------+---------+------+")

xt = xb
while xt <= xe:
    an = 1
    n = 0
    y = an

    while True:
        k = xt / (n + 1)
        an = an * k
        y = y + an
        n = n + 1
        if abs(an) < eps:
            break

    print("I{0:7.2f} I{1:8.3f} I{2:5} I"
          .format(xt, y, n + 1))

    xt = xt + dx

print("+--------+---------+------+")


# Output:
'''
Введите Xbeg, Xend, Dx и Eps
Xbeg=0
Xend=2
Dx=0.5
Eps=0.001
+--------+---------+------+
I   X    I    Y    I   N  I
+--------+---------+------+
I   0.00 I   1.000 I    2 I
I   0.50 I   1.649 I    6 I
I   1.00 I   2.718 I    8 I
I   1.50 I   4.482 I    9 I
I   2.00 I   7.389 I   11 I
+--------+---------+------+'''