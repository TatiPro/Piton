import sys, traceback
from math import (sqrt)
a = ""
while (a != "отстань"):
    a = input("Введите значение а:")
    if (a.strip("-").isnumeric()):
        a = int(a)
        if (a>0 and (a - sqrt(2*a)) != 0 and (a + 2) != 0):
            z1 = ((a + 2)/sqrt(2*a) - a/(sqrt(2*a) + 2) + 2 / (a - sqrt(2*a))) * ((sqrt(a) - sqrt(2)) / (a + 2))
            z2 = 1 / (sqrt(a) + sqrt(2))
            print('z=', z1, 'z2=', z2)
        else:
            print("Решений нет. Данное значение не входит в ОДЗ")
    else:
        print("Неверный формат.")








