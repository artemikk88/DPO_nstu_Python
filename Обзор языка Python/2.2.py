import math
from math import pi

Radius = float(input("Введите радиус цилиндра (м): "))
Height = float(input("Введите высоту цилиндра (м): "))
Square = pi * Radius**2
Volume = Square * Height
print("Объем цилиндра равен ", round(Volume, 1), "м^3")
