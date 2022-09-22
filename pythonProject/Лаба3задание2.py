from math import *
from random import *
flag = 0
print("  R      X      Y     Res")
print("--------------------------")
for n in range(10):
    x = uniform(-10, 10)
    y = uniform(-10, 10)
    R = uniform(1, 10)
    if R ** 2 <= (x - R) ** 2 + (y - R) ** 2 and y <= x:
        flag = 1
    if R ** 2 <= (x + R) ** 2 + (y + R) ** 2 and y <= x:
        flag = 1
    else:
        flag = 0
    print("{0: 7.2f} {1: 7.2f} {2: 7.2f}" .format(R, x, y), end=" ")
    if flag:
        print("Yes")
    else:
        print("No")



