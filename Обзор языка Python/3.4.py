Time_input = input(
    "Введите временной отрезок в виде дни , часы , минуты , секунды через запятую: ")
Time_list = Time_input.split(",")
for i in range(len(Time_list)):
    Time_list[i] = int(Time_list[i])
result = (Time_list[0]*24*60**2)+(Time_list[1]*60**2) + \
    (Time_list[2]*60)+Time_list[3]
print("Данный отрезок в секундах: ", result)
