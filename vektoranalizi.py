import numpy as np

x1 = np.array([1, 0, 0])  # x1 eksenindeki birim vektör
x2 = np.array([0, 1, 0])  # x2 eksenindeki birim vektör
x3 = np.array([0, 0, 1])  # x3 eksenindeki birim vektör

x= int(input("x bileşeni giriniz: "))
y= int(input("y bileşeni giriniz: "))
z= int(input("z bileşeni giriniz: "))


def kartezyen_koordinat(x,y,z):
    r = x * i + y * j + z * k
    return r


print("r =",kartezyen_koordinat(x,y,z))










