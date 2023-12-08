
card_order = "AKQJT98765432"
test_cases = ["AAAAA", "AA8AA", "23332", "TTT98", "23432", "A23A4", "23456"]


class Hand(str):

    def __init__(self, *args):
        char1 = self[0]
        char2 = self[1]
        char3 = self[2]
        char4 = self[3]
        char5 = self[4]
        for char in self[1:]:
            if char != char1:
                char2 = char
        for char in self[1:]:
            if char != char1 and char != char2:
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


def main():
    for tc in test_cases:
        a = Hand(tc)
        print(a.is_5_of_a_kind, a.is_4_of_a_kind, a.is_full_house, a.is_3_of_a_kind)


if __name__ == "__main__":
    main()
