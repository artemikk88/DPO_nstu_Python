words = []
while True:
    a = input("Введите слово: ")
    if a == "":
        break
    if a not in words:
        words.append(a)
print(" ".join(words))
