from pathlib import Path


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]


def get_differences(history: list[int]) -> list[int]:
    return [x - y for x, y in zip(history[:-1], history[1:])]


def part_one(puzzle_list: list[str]) -> int:
    running_total = 0
    for line in puzzle_list:
        history = [int(x) for x in line.split()]
        differences = [get_differences(history)]
        while not all(x == 0 for x in differences[-1]):
            differences.append(get_differences(differences[-1]))
        differences[-1].append(0)
        while len(differences) > 1:
            current_differences = differences.pop(-1)
            differences[-1].append(differences[-1][-1] - current_differences[-1])
        history.append(history[-1] - differences[-1][-1])
        running_total += history[-1]
    return running_total


print(part_one(get_raw_puzzle("2023_09_puzzle.txt")))


def part_two(puzzle_list: list[str]) -> int:
    running_total = 0
    for line in puzzle_list:
        history = [int(x) for x in reversed(line.split())]
        differences = [get_differences(history)]
        while not all(x == 0 for x in differences[-1]):
            differences.append(get_differences(differences[-1]))
        differences[-1].append(0)
        while len(differences) > 1:
            current_differences = differences.pop(-1)
            differences[-1].append(differences[-1][-1] - current_differences[-1])
        history.append(history[-1] - differences[-1][-1])
        running_total += history[-1]
    return running_total


print(part_two(get_raw_puzzle("2023_09_puzzle.txt")))
