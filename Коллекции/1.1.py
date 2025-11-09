numbers = []
while True:
    a = int(input("Введите число или введите ноль для завершения ввода: "))
    if a == 0:
        break
    numbers.append(a)
for i in sorted(numbers):
    print(i)
