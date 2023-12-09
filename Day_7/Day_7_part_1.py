from functools import total_ordering

file = 'input.txt'

card_order = "AKQJT98765432"
test_cases = ["AAAAA", "AA8AA", "23332", "TTT98", "23432", "A23A4", "23456"]


@total_ordering
class Hand(str):

    def __init__(self, *args):
        super().__init__()
        char1 = self[0]
        char2 = self[1]
        char3 = self[2]
        char4 = self[3]
        char5 = self[4]
        for char in self[1:]:
            if char != char1:
                char2 = char
        for char in self[1:]:
            if char not in (char1, char2):
                char3 = char
        for char in self[1:]:
            if char not in (char1, char2, char3):
                char4 = char
        for char in self[1:]:
            if char not in (char1, char2, char3, char4):
                char5 = char

        self.is_5_of_a_kind = self.count(self[0]) == 5
        self.is_4_of_a_kind = self.count(char1) == 4 or self.count(char2) == 4
        self.is_full_house = ((self.count(char1) == 3 and
                               self.count(char2) == 2) or
                              (self.count(char1) == 2 and
                               self.count(char2) == 3))

        self.is_3_of_a_kind = (3 in ((lambda x: self.count(x))(x)
                                     for x in (char1, char2, char3))) and char3 not in (char1, char2)

        self.is_2_pair = (char5 in (char1, char2, char3) and
                          char3 not in (char1, char2) and
                          char4 in (char1, char2, char3) and
                          not self.is_3_of_a_kind)

        self.is_pair = (char5 in (char1, char2, char3, char4)) and (char4 not in (char1, char2, char3))

        for char in self:
            if self.count(char) > 1:
                self.is_high_card = False
                break
        else:
            self.is_high_card = True

        self.type_rank = (self.is_high_card,
                          self.is_pair,
                          self.is_2_pair,
                          self.is_3_of_a_kind,
                          self.is_full_house,
                          self.is_4_of_a_kind,
                          self.is_5_of_a_kind).index(True)

        self.rank = self.type_rank * 10**10
        for i, char in enumerate(self):
            self.rank += get_char_rank(char) * 10 ** ((4 - i) * 2)

    def __gt__(self, other) -> bool:
        return self.rank > other.rank

    def __lt__(self, other):
        return self.rank < other.rank


def get_char_rank(char):
    return len(card_order) - card_order.index(char)


def main():
    f = open(file, 'r')
    hands = []
    hands_to_bids = {}
    for line in f.readlines():
        hand = line.split(" ")[0]
        hands.append(Hand(hand))
        hands_to_bids[hand] = int(line.split(' ')[1])
    hands.sort(key=lambda x: x.rank)
    result = 0
    for i in range(len(hands)):
        result += (i+1)*hands_to_bids[hands[i]]
    print(result)


if __name__ == "__main__":
    main()
