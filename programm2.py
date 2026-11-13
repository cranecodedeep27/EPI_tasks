from math import sin

x = 3
while x <= 14:
    y = sin(x) - 1 / x
    print(f"x = {x:.1f}, y = {y:.4f}")
    x += 0.5