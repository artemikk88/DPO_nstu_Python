def ravnenie_str(s, w):
    if len(s) >= w:
        return s
    result = " "*((w - len(s))//2) + s
    return result


str_1 = "Первая строка"
str_2 = "Строка с чуть большим количеством символом"
str_3 = "Короткая строка"
print(ravnenie_str(str_1, 30))
print(ravnenie_str(str_2, 20))
print(ravnenie_str(str_3, 50))
