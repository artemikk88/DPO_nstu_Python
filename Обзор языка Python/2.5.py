order_sum = float(input("Введите сумму заказа (руб): "))
tips = order_sum * (18/100)
tax = order_sum * (20/100)
result = order_sum + tax + tips
print("Сумма налога (руб): ", round(tax, 2), "\n", "Сумма чаевых (руб): ",
      round(tips, 2), "\n", "Итого (руб): ", round(result, 2))
