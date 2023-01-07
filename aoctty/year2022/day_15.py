from aoctty import read_puzzle
from sys import argv
from typing import Iterable
import re


class Parser:
    pattern = re.compile(r"[xy]=(-?\d+)")

    @staticmethod
    def parse(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
        results = Parser.pattern.findall(line)
        sensor = (int(results[0]), int(results[1]))
        beacon = (int(results[2]), int(results[3]))
        return (sensor, beacon)


class Sensor:
    def __init__(self, position: tuple[int, int], beacon: tuple[int, int]) -> None:
        self.position = position
        self.beacon = beacon
        self.distance = self.get_distance(beacon)
        self.set_bounding_box()

    def get_distance(self, coordinates: tuple[int, int]) -> int:
        x_distance = abs(self.position[0] - coordinates[0])
        y_distance = abs(self.position[1] - coordinates[1])
        return x_distance + y_distance

    def set_bounding_box(self) -> None:
        self.highest_x = self.position[0] + self.distance
        self.lowest_x = self.position[0] - self.distance
        self.highest_y = self.position[1] + self.distance
        self.lowest_y = self.position[1] - self.distance

    def is_inrange(self, coordinates: tuple[int, int]) -> bool:
        return self.get_distance(coordinates) <= self.distance

    def is_empty(self, coordinates: tuple[int, int]) -> bool:
        return self.is_inrange(coordinates) and coordinates != self.beacon


def get_boundaries(sensors: Iterable[Sensor]) -> tuple[int, int, int, int]:
    highest_x, lowest_x, highest_y, lowest_y = 0, 0, 0, 0
    for sensor in sensors:
        highest_x = max(highest_x, sensor.highest_x)
        lowest_x = min(lowest_x, sensor.lowest_x)
        highest_y = max(highest_y, sensor.highest_y)
        lowest_y = min(lowest_y, sensor.lowest_y)
    return (highest_x, lowest_x, highest_y, lowest_y)


def part_one(puzzle: list[str], row: int) -> int:
    empty_coordinates = set()
    sensors = tuple(Sensor(*Parser.parse(x)) for x in puzzle)
    boundaries = get_boundaries(sensors)
    for column in range(boundaries[1], boundaries[0] + 1):
        coordinates = (column, row)
        for sensor in sensors:
            if sensor.is_empty(coordinates):
                empty_coordinates.add(coordinates)
                break
    return len(empty_coordinates)


def part_two(puzzle: list[str], limit: int) -> int:
    sensors = tuple(Sensor(*Parser.parse(x)) for x in puzzle)
    boundaries = get_boundaries(sensors)
    for column in range(max(0, boundaries[1]), min(boundaries[0] + 1, limit)):
        for row in range(max(0, boundaries[3]), min(boundaries[2], limit)):
            coordinates = (column, row)
            eligible = True
            for sensor in sensors:
                if sensor.is_inrange(coordinates):
                    eligible = False
                    break
            if eligible is True:
                return column * 4000000 + row
    return 0


def main():
    args = argv[1:]
    puzzle = read_puzzle.get_raw_puzzle("day15.txt")
    if len(args) == 0 or "1" in args:
        print(part_one(puzzle, 2000000))
    if len(args) == 0 or "2" in args:
        print(part_two(puzzle, 4000000))


if __name__ == "__main__":
    main()
