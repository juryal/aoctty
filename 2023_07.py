from pathlib import Path


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]


class camel_hand:
    face_card = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    base = 15

    def __init__(self, hand: str) -> None:
        self.hand = tuple(x for x in hand)
        self.numeric = self.get_numeric() + self.get_hand_type()

    def __lt__(self, other):
        return self.numeric < other.numeric

    def __eq__(self, other):
        return self.numeric == self.numeric

    def get_hand_type(self):
        cards = {}
        for card in self.hand:
            cards[card] = cards.setdefault(card, 0) + 1
        cards = sorted(cards.items(), key=lambda x: x[1], reverse=True)
        match cards[0][1]:
            case 5:
                return self.base**5 * 7
            case 4:
                return self.base**5 * 6
            case 3:
                if cards[1][1] == 2:
                    return self.base**5 * 5
                else:
                    return self.base**5 * 4
            case 2:
                if cards[1][1] == 2:
                    return self.base**5 * 3
                else:
                    return self.base**5 * 2
            case 1:
                return self.base**5 * 1

    def get_numeric(self):
        number = 0
        for idx, card in enumerate(reversed(self.hand)):
            if card.isdigit():
                number += int(card) * self.base**idx
            else:
                number += self.face_card[card] * self.base**idx
        return number

    def __str__(self):
        return f"camel_hand({self.hand})"

    def __repr__(self):
        return f"{self.hand}"


def part_one(puzzle_list: list[str]) -> int:
    hands = [(camel_hand(x.split()[0]), int(x.split()[1])) for x in puzzle_list]
    hands.sort(key=lambda x: x[0])
    running_total = 0
    for idx, hand in enumerate(hands):
        running_total += hand[1] * (idx + 1)
    return running_total


print(part_one(get_raw_puzzle("2023_07_puzzle.txt")))
