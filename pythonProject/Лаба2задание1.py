from math import *
while True:
 x = float(input("Введите значение х:"))
 if x < -2 : y = -x-2
 if x >= -2 and x <= 0: y=sqrt(1-(x+1)**2)
 if x>0 and x < 4: y = -sqrt(4-(x-2)**2)
 if x>=4 and x<6: y = -0,5*x + 2
 print("Значение: при x=" , x , " у =", y)

