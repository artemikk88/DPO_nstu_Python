def mediana(list):
    list.sort()
    return list[1]


numbers = [int(input("Введите число: ")) for _ in range(3)]
print("Медиана данного набора чисел: ", mediana(numbers))
