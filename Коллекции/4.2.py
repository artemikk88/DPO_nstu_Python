import random

expected = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
            7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}


def throw_dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return (a+b)


dict_results = {i: 0 for i in range(2, 13)}
for i in range(1000):
    result = throw_dice()
    dict_results[result] += 1

for key in range(2, 13):
    count = dict_results[key]
    freq = count / 1000 * 100
    print(f"{key:<6}{count:<12}{freq:<14.2f}{expected[key]:<15.2f}")
