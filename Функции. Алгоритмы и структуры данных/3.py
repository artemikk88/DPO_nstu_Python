def Tokenizing(s):
    temp = ''
    result = []
    s = s.replace(' ', '')
    for i in s:
        if i.isdigit():
            temp += i
        else:
            if temp:
                yield temp
                temp = ''
            yield i
    if temp:
        yield temp


s = input("Введите строку состоящую из математического выражения: ")
tokens = list(Tokenizing(s))
print("Списко лексем", tokens)
