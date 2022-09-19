from math import *
flag = 0
print("Введите координаты точек и радиус:")
x = float(input("x="))
y = float(input("y="))
R = float(input("R="))
if R**2 <= (x-R)**2 + (y-R)**2 and y<=x: flag = 1
if R**2 <= (x+R)**2 + (y+R)**2 and y<=x: flag = 1
else: flag = 0
print ("Точка Х={0:3f} Y={1:3F}"\
       .format(x,y) , end="")
if flag:
    print("\n Попадает в область")
else:
    print("\n Не попадает в область")
