import math
from math import pi
r = float(input("Введите радиус: "))
Square = pi*r**2
Volume = (4/3)*pi*r**3
print("Площадь круга = ", round(Square, 2),
      "\n", "Объем шара = ", round(Volume, 2))
