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
    an = 2 * xt
    n = 0
    y = an

    while True:
        k = xt**2 * (2*n + 1) / (2*n + 3)
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
Xbeg=-0.5
Xend=0.5
Dx=0.25
Eps=0.001
+--------+---------+------+
I   X    I    Y    I   N  I
+--------+---------+------+
I  -0.50 I  -1.098 I    5 I
I  -0.25 I  -0.511 I    3 I
I   0.00 I   0.000 I    2 I
I   0.25 I   0.511 I    3 I
I   0.50 I   1.098 I    5 I
+--------+---------+------+'''