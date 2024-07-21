from math import ceil


def bolded_letters(word_length: int, fixation: int) -> int:
    """calculate the limit length that need to be bolded

    Args:
        word_length (int): word length
        fixation (int): desired fixation

    Returns:
        int: the max length limit in the word that need to be bolded
    """

    if word_length == 2:
        return 1
    elif word_length >= 3:
        return min(ceil(word_length * fixation / 5), word_length)
    else:
        return 1
