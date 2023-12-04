from pathlib import Path


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]


def part_one(list: list[str]) -> int:
    running_total = 0
    for line in list:
        winning_numbers, selected_numbers = line.split(":")[1].strip().split("|")
        winning_numbers = set(winning_numbers.split())
        selected_numbers = set(selected_numbers.split())
        shared = len(winning_numbers.intersection(selected_numbers))
        if shared > 0:
            running_total += 2 ** (shared - 1)
    return running_total


print(part_one(get_raw_puzzle("2023_04_puzzle.txt")))


def part_two(list: list[str]) -> int:
    cards_scratched = {}
    for linenumber, line in enumerate(list):
        card_number = linenumber + 1
        cards_scratched[card_number] = cards_scratched.setdefault(card_number, 0) + 1
        winning_numbers, selected_numbers = line.split(":")[1].strip().split("|")
        winning_numbers = set(winning_numbers.split())
        selected_numbers = set(selected_numbers.split())
        shared = len(winning_numbers.intersection(selected_numbers))
        for i in range(1, shared + 1):
            cards_scratched[card_number + i] = cards_scratched.setdefault(
                card_number + i, 0
            ) + (1 * cards_scratched[card_number])
    return sum(cards_scratched.values())


print(part_two(get_raw_puzzle("2023_04_puzzle.txt")))
