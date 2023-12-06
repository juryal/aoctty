from pathlib import Path
from copy import deepcopy


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]


def updatemap(destination_start, source_start, span, seeds_map, index_marker):
    change = destination_start - source_start
    for idx, x in enumerate(list(zip(*seeds_map))[index_marker]):
        if x in range(source_start, source_start + span):
            seeds_map[idx][index_marker + 1 :] = [x + change] * len(
                seeds_map[idx][index_marker + 1 :]
            )
            pass


def part_one(puzzle_list: list[str]) -> int:
    seeds_map = [[int(x)] * 8 for x in puzzle_list[0].split(":")[1].split()]
    index_marker = -1
    for line in list(filter(None, puzzle_list[1:])):
        if line[0].isdigit():
            destination_start, source_start, span = [int(x) for x in line.split()]
            updatemap(destination_start, source_start, span, seeds_map, index_marker)
        elif line[0].isalpha():
            index_marker += 1
    return min(list(zip(*seeds_map))[-1])


print(part_one(get_raw_puzzle("2023_05_puzzle.txt")))


def seed_exists(candidate, row, conversion_map):
    while row < 8:
        for destination_range in conversion_map[row]:
            if candidate in range(destination_range[0], destination_range[1]):
                if row != 7:
                    return seed_exists(
                        candidate - destination_range[2], row + 1, conversion_map
                    )
                else:
                    return True
        row += 1
    return False


def downstream_check(candidate, row, conversion_map):
    while row > 0:
        row -= 1
        for destination_range in conversion_map[row]:
            if candidate in range(destination_range[0], destination_range[1]):
                return False
    return True


def part_two(puzzle_list: list[str]) -> int:
    possible_ranges = [[] for _ in range(8)]
    index_marker = 0
    for line in list(filter(None, reversed(puzzle_list[1:]))):
        if line[0].isdigit():
            destination, source, span = [int(x) for x in line.split()]
            possible_ranges[index_marker].append(
                (destination, destination + span, destination - source)
            )
        elif line[0].isalpha():
            index_marker += 1
    seeds = iter(puzzle_list[0].split(":")[1].split())
    possible_ranges[-1].extend(
        [(int(x), int(x) + int(y), 0) for x, y in zip(seeds, seeds)]
    )
    minimum = min(possible_ranges[-1])[0]
    for idx, x in enumerate(deepcopy(possible_ranges)):
        while x:
            candidate = x.pop(x.index(min(x)))
            if candidate[0] < minimum and downstream_check(
                candidate[0], idx, possible_ranges
            ):
                if seed_exists(candidate[0] - candidate[2], idx + 1, possible_ranges):
                    minimum = min(minimum, candidate[0])
                elif candidate[0] + 1 < candidate[1]:
                    x.append((candidate[0] + 1, candidate[1], candidate[2]))
                    pass
    return minimum


print(part_two(get_raw_puzzle("2023_05_puzzle.txt")))
