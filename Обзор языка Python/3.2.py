change = int(input("Введите сдачу в центах: "))
nominals = [200, 100, 25, 10, 5, 1]
result = [0, 0, 0, 0, 0, 0]
for i in range(len(nominals)):
    while not ((change - nominals[i]) < 0):
        change -= nominals[i]
        result[i] += 1
for i in range(len(result)):
    print(nominals[i], "-", result[i], "\n")
