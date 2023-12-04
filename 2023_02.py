from pathlib import Path
import re
from functools import reduce


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]


def part_one(list: list[str]) -> int:
    TOTAL_CUBES = {"red": 12, "green": 13, "blue": 14}
    game_sum = 0
    for line in list:
        split_line = line.split(":")
        draws = split_line[-1].strip().split(";")
        highest_draw = dict()
        color_search = "(\d+) (\w+)"
        for draw in draws:
            cube_draws = re.findall(color_search, draw)
            for cube_draw in cube_draws:
                if int(cube_draw[0]) > highest_draw.get(cube_draw[1], 0):
                    highest_draw[cube_draw[1]] = int(cube_draw[0])
        success = True
        for item in highest_draw.items():
            if item[1] > TOTAL_CUBES[item[0]]:
                success = False
        if success:
            game_number = int(split_line[0].split()[-1])
            game_sum += game_number
    return game_sum


print(part_one(get_raw_puzzle("2023_02_puzzle.txt")))


def part_two(list: list[str]) -> int:
    game_sum = 0
    for line in list:
        split_line = line.split(":")
        draws = split_line[-1].strip().split(";")
        highest_draw = dict()
        color_search = "(\d+) (\w+)"
        for draw in draws:
            cube_draws = re.findall(color_search, draw)
            for cube_draw in cube_draws:
                if int(cube_draw[0]) > highest_draw.get(cube_draw[1], 0):
                    highest_draw[cube_draw[1]] = int(cube_draw[0])
        game_power = reduce(lambda x, y: x * y, highest_draw.values())
        game_sum += game_power
    return game_sum


print(part_two(get_raw_puzzle("2023_02_puzzle.txt")))
