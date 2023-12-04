import re

test_line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
file = "input.txt"

result = 0


def get_card_points(card):
    n_correct_numbers = 0
    data_str = card.split(": ")[1]
    card_str, win_str = data_str.split("| ")
    card_lst = [int(i) for i in re.findall("([0-9 ][0-9][^0-9:])", card_str)]
    win_lst = [int(i) for i in re.findall("([0-9 ][0-9][^0-9:])", win_str)]
    for n in card_lst:
        if n in win_lst:
            n_correct_numbers += 1
    return n_correct_numbers


