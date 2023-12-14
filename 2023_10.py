from pathlib import Path
from typing import NamedTuple


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]


def get_new_heading(heading: int, pipe_section: str) -> int:
    match pipe_section:
        case "|" | "-":
            return heading
        case "L" if heading == 2:
            return 1
        case "L" if heading == 3:
            return 0
        case "J" if heading == 2:
            return 3
        case "J" if heading == 1:
            return 0
        case "7" if heading == 1:
            return 2
        case "7" if heading == 0:
            return 3
        case "F" if heading == 0:
            return 1
        case "F" if heading == 3:
            return 2
        case _:
            raise Exception(
                f"No match for heading {heading} and pipe section {pipe_section}"
            )


class Coordinates(NamedTuple):
    row: int
    column: int

    def _move(self, move: "Coordinates") -> "Coordinates":
        return Coordinates(row=self.row + move.row, column=self.column + move.column)

    def move(self, heading: int) -> "Coordinates":
        moves: dict[int, Coordinates] = {
            0: Coordinates(-1, 0),
            1: Coordinates(0, 1),
            2: Coordinates(1, 0),
            3: Coordinates(0, -1),
        }
        return self._move(moves[heading])


def find_start(puzzle: list[str]) -> Coordinates:
    for row, line in enumerate(puzzle):
        if (column := line.find("S")) != -1:
            return Coordinates(row=row, column=column)
    raise Exception("Start not found")


def get_pipesection(puzzle: list[str], coordinates: Coordinates) -> str:
    return puzzle[coordinates.row][coordinates.column]


def get_first_heading(puzzle: list[str], start_coordinates: Coordinates) -> int:
    for heading in range(4):
        new_coordinates = start_coordinates.move(heading)
        pipe_section = get_pipesection(puzzle, new_coordinates)
        try:
            get_new_heading(heading, pipe_section)
            return heading
        except:
            continue
    raise Exception("First pipe not found")


def part_one(puzzle_list: list[str]) -> int:
    start_coordinates = find_start(puzzle_list)
    heading = get_first_heading(puzzle_list, start_coordinates)
    current_coordinates = start_coordinates.move(heading)
    steps = 1
    while (pipe_section := get_pipesection(puzzle_list, current_coordinates)) != "S":
        heading = get_new_heading(heading, pipe_section)
        current_coordinates = current_coordinates.move(heading)
        steps += 1
    return steps // 2


print(part_one(get_raw_puzzle("2023_10_puzzle.txt")))
