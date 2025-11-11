def CountRange(spisok, min_gr, max_gr):
    count = 0
    for i in spisok:
        if (min_gr <= i < max_gr):
            count += 1
    return count


A = [1, 2, 3, 4, 5]
B = [10, 20, 3, 40, 50]
C = [1.5, 1.5, 1.5, 9, 10]
print("Количество элементов попадающих в границу: ", CountRange(
    A, 3, 5), "Количество уникальных элементов: ", len(set(A)))
print("Количество элементов попадающих в границу: ", CountRange(
    B, 25, 100), "Количество уникальных элементов: ", len(set(B)))
print("Количество элементов попадающих в границу: ", CountRange(
    C, 0.5, 1.5), "Количество уникальных элементов: ", len(set(C)))
