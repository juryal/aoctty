from pathlib import Path


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]


def get_distances(time: int) -> list[int]:
    racing_time = 0
    distances = list()
    while time >= 0:
        distances.append(time * racing_time)
        time -= 1
        racing_time += 1
    return distances


def part_one(puzzle_list: list[str]) -> int:
    grid = []
    for line in puzzle_list:
        values = [int(x) for x in line.split(":")[1].split()]
        grid.append(values)
    grid = tuple(zip(*grid))
    victory_product = 1
    for race in grid:
        victories = len([x for x in get_distances(race[0]) if x > race[1]])
        victory_product *= victories
    return victory_product


print(part_one(get_raw_puzzle("2023_06_puzzle.txt")))


def get_victories(time: int, record: int) -> int:
    racing_time = 0
    victories = 0
    while time >= 0:
        if distance := time * racing_time > record:
            victories += 1
        time -= 1
        racing_time += 1
    return victories


def part_two(puzzle_list: list[str]) -> int:
    grid = []
    for line in puzzle_list:
        grid.append(int(line.split(":")[1].replace(" ", "")))
    return get_victories(grid[0], grid[1])


print(part_two(get_raw_puzzle("2023_06_puzzle.txt")))
