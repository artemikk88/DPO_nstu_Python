import random

bingo_dict = {'B': list(range(1, 15)),
              'I': list(range(16, 30)),
              'N': list(range(31, 45)),
              'G': list(range(46, 60)),
              'O': list(range(61, 75))}


def make_a_card(dictionary):
    card_dict = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
    for i in bingo_dict.keys():
        card_dict[i] = random.sample(bingo_dict[i], 5)
    return card_dict


result = make_a_card(bingo_dict)
print("B I N G O")
for i in range(5):
    row = ''
    for j in result.keys():
        row += str(result[j][i]) + " "
    print(row)
