dirt_str = input("Введите строку: ").lower()
znaki = [",", "!", ".", "?", ":", ";", "'", "-"]
clear_str = ""
for i in dirt_str:
    if i not in znaki:
        clear_str += i
list_of_words = clear_str.split()
if list_of_words == list_of_words[::-1]:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
