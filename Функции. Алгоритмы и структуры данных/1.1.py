import math


def find_gipotenuza(a, b):
    c = math.sqrt(a**2 + b**2)
    return c


a = int(input("Введите длину первого катета: "))
b = int(input("Введите длину второго катета: "))
print("Длина гипотенуза равна: ", find_gipotenuza(a, b))
