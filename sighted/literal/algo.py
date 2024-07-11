import math


def bolded_letters(word_length, fixation):
    if word_length == 2:
        return 1
    elif word_length >= 3:
        return min(math.ceil(word_length * fixation / 5), word_length)
    else:
        return 1
