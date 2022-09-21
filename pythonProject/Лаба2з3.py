from math import *
print("Введите Хb, Хe и Dх")
Xb = float(input("Xb = "))
Xe = float(input("Xe ="))
Dx = float(input("Dx ="))
print("Хb = {0:7.2f} Xe = {1: 7.2f}" .format(Xb, Xe))
print (" Dx={0:7.2f}" .format(Dx))
xt = Xb
print ("+--------+---------+")
print("I    X   I    Y    I")
print ("+--------+---------+")
while xt <= Xe:
      if xt< -2 :
           y = -xt-2
      elif xt>= -2 and xt<= 0:
           y=sqrt(1-( xt+1)**2)
      elif  xt>0 and  xt < 4:
           y = -sqrt(4-(xt-2)**2)
      elif xt >= 4 and xt < 6:
           y = -0.5* xt + 2
      else: y = -1
      print("I{0:7.2f} I {1:7.2f} I".format(xt, y))
      xt += Dx
print ("+--------+--------+")


