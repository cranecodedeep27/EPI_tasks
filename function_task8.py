from math import *

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
    an = -1 / xt
    n = 0
    y = pi / 2 + an

    while True:
        k = -(2*n + 1) / ((2*n + 3) * xt**2)
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
Xbeg=2
Xend=4
Dx=0.5
Eps=0.001
+--------+---------+------+
I   X    I    Y    I   N  I
+--------+---------+------+
I   2.00 I   1.107 I    5 I
I   2.50 I   1.190 I    4 I
I   3.00 I   1.249 I    3 I
I   3.50 I   1.292 I    3 I
I   4.00 I   1.326 I    3 I
+--------+---------+------+'''