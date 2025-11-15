def taxi_bill(len_path):
    cost = 4
    len_path = len_path * 1000
    cost = cost + ((len_path//140) * 0.25)
    return cost


print(taxi_bill(100), "$")
print(taxi_bill(0.1), "$")
print(taxi_bill(0.42), "$")