def is_sorted(tuple_nums):
    try:
        list_of_nums = [float(x) for x in tuple_nums]
    except ValueError:
        print("Ошибка кортеж должен состоять только из чисел")
        return False
    sorted_higher = sorted(list_of_nums)
    sorted_lower = sorted(list_of_nums, reverse=True)
    if ((list_of_nums == sorted_higher) or (list_of_nums == sorted_lower)):
        return True
    else:
        return False


numbers = tuple(input("Введите список чисел через пробел: ").split())
print(is_sorted(numbers))
