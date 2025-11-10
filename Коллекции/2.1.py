def raspred_nums(numbers):
    sred_arif = sum(numbers)/len(numbers)
    higher = []
    equal = []
    lower = []
    for i in numbers:
        if i > sred_arif:
            higher.append(i)
        elif i == sred_arif:
            equal.append(i)
        else:
            lower.append(i)
    print("Среднее арифметическое списка чисел: ", sred_arif)
    print("Числа выше среднего арифметического:", higher, "\n", "Числа меньше среднего арифметического:",
          lower, "\n", "Числа равные среднему арифметическому:", equal)


numbers = []
while True:
    a = input("Введите число или оставьте строку пустой для окончания ввода: ")
    if not a:
        break
    try:
        numbers.append(int(a))
    except ValueError:
        print("Попробуйте ввести число")

raspred_nums(tuple(numbers))
