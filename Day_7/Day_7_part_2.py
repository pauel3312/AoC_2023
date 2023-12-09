from functools import total_ordering
from Day_7_part_1 import get_char_rank, file

card_order = "AKQT98765432J"


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
        if 'J' not in self:
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
        else:  # hand contains Jokers
            self.type_rank = -1
            for card in card_order[:-1]:  # Iterate through all the possible replacement characters
                # replace the first J with this card (that way I check it all using recursion)
                new_hand_text = self[:self.index('J')]+card+self[self.index('J')+1:]
                new_hand = Hand(new_hand_text)  # create a new hand object from the new text
                # check if its type_rank is higher than current hand's type_rank
                if new_hand.type_rank > self.type_rank:
                    self.type_rank = new_hand.type_rank  # if yes, replace current hand's type_rank
                del new_hand

        self.rank = self.type_rank * 10**10
        for i, char in enumerate(self):
            self.rank += get_char_rank(char) * 10 ** ((4 - i) * 2)

    def __gt__(self, other) -> bool:
        return self.rank > other.rank

    def __lt__(self, other):
        return self.rank < other.rank


def main():
    f = open(file, 'r')
    hands = []
    hands_to_bids = {}
    for line in f.readlines():
        hand = line.split(" ")[0]
        hand = Hand(hand)
        hands.append(hand)
        hands_to_bids[hand] = int(line.split(' ')[1])
    hands.sort(key=lambda x: x.rank)
    result = 0
    for i in range(len(hands)):
        if hands.count(hands[i]) > 1:
            raise Exception("Identical hands")
        result += (i+1)*hands_to_bids[hands[i]]
    print(result)


if __name__ == '__main__':
    main()
