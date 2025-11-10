def make_spisok(words):
    n = len(words)
    itog = ""
    for i in range(0, n):
        if (i == n-1) and (n > 1):
            itog += "и "
            itog += words[i]
        else:
            itog += words[i] + " "
    return itog


words_str = input("Ввести в строку слова через запятую: ")
words_str = words_str.replace(" ", "")
words_tuple = tuple(words_str.split(","))
print(make_spisok(words_tuple))
