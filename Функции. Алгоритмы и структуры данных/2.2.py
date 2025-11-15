dict_of_numeral = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
                   5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                   9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'}


def num_in_numeral(number):
    if number in dict_of_numeral:
        return dict_of_numeral[number]
    return ""


if __name__ == "__main__":
    for i in range(1, 13):
        print(i, "-", num_in_numeral(i))
