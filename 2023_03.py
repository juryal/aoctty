from pathlib import Path
import re
from itertools import product


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]


def part_one(list: list[str]) -> int:
    adjustments = tuple(x for x in product((-1, 0, 1), (-1, 0, 1)))
    symbol = "[^0-9\.]"
    sum = 0
    for line_number, line in enumerate(list):
        number = ""
        is_part_number = False
        for char_number, character in enumerate(line):
            if character.isdigit():
                number += character
                possibilities = [
                    (line_number + x, char_number + y) for (x, y) in adjustments
                ]
                for possibilty in possibilities:
                    if 0 <= possibilty[0] < len(list) - 1:
                        if 0 <= possibilty[1] < len(line):
                            if re.search(symbol, list[possibilty[0]][possibilty[1]]):
                                is_part_number = True
            else:
                if is_part_number:
                    sum += int(number)
                number = ""
                is_part_number = False
        if is_part_number:
            sum += int(number)
    return sum


print(part_one(get_raw_puzzle("2023_03_puzzle.txt")))


def part_two(list: list[str]) -> int:
    adjustments = tuple(x for x in product((-1, 0, 1), (-1, 0, 1)))
    symbol = "[^0-9\.]"
    sum = 0
    symbols: dict[tuple[int, int] : list[str]] = {}
    for line_number, line in enumerate(list):
        number = ""
        is_part_number = False
        local_symbols = set()
        for char_number, character in enumerate(line):
            if character.isdigit():
                number += character
                possibilities = [
                    (line_number + x, char_number + y) for (x, y) in adjustments
                ]
                for possibilty in possibilities:
                    if 0 <= possibilty[0] < len(list) - 1:
                        if 0 <= possibilty[1] < len(line):
                            if re.search(symbol, list[possibilty[0]][possibilty[1]]):
                                local_symbols.add(possibilty)
                                is_part_number = True
            else:
                if is_part_number:
                    for local_symbol in local_symbols:
                        symbols.setdefault(local_symbol, []).append(int(number))
                number = ""
                is_part_number = False
                local_symbols = set()
        if is_part_number:
            for local_symbol in local_symbols:
                symbols.setdefault(local_symbol, []).append(int(number))
    for values in symbols.values():
        if len(values) == 2:
            sum += values[0] * values[1]
    return sum


print(part_two(get_raw_puzzle("2023_03_puzzle.txt")))
