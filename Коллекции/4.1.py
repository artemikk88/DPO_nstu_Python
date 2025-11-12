def reverseLookup(dictionary, val):
    list_keys = []
    for key, value in dictionary.items():
        if value == val:
            list_keys.append(key)
    return list_keys


products = {
    "Молоко": "Продукты",
    "Хлеб": "Продукты",
    "Ноутбук": "Электроника",
    "Телефон": "Электроника",
    "Книга": "Отдых и развлечения"
}

print(reverseLookup(products, "Электроника"))
print(reverseLookup(products, "Одежда"))
print(reverseLookup(products, "Отдых и развлечения"))