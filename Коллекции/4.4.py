def create_dicts(first_word, sec_word):
    first_word = first_word.lower()
    sec_word = sec_word.lower()
    chr_word_1 = {i: 0 for i in first_word}
    chr_word_2 = {i: 0 for i in sec_word}
    for i in first_word:
        chr_word_1[i] += 1
    for i in sec_word:
        chr_word_2[i] += 1
    return chr_word_1, chr_word_2


def anagramas(first_word, sec_word):
    if len(first_word) != len(sec_word):
        return "Не являются анаграммами"
    results = create_dicts(first_word, sec_word)
    if (results[0] == results[1]):
        return "Являются анаграммами"
    else:
        return "Не являются анаграммами"


print(anagramas('выбор', 'обрыв'))
