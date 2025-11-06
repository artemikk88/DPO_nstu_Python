deposit = int(input("Введите первоначальный взнос: "))
first_year = deposit + deposit * 0.04
second_year = first_year + first_year * 0.04
third_year = second_year + second_year * 0.04
print(first_year, "\n", second_year, "\n", third_year)
