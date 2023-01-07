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

    def get_outside_ring(self) -> list[tuple[int, int]]:
        radius = self.distance + 1
        coordinates: set[tuple[int, int]] = set()
        for x in range(radius + 1):
            vertical = radius - x
            horizontal = x
            coordinates.add(
                (self.position[0] + horizontal, self.position[1] + vertical)
            )
            coordinates.add(
                (self.position[0] + horizontal, self.position[1] - vertical)
            )
            coordinates.add(
                (self.position[0] - horizontal, self.position[1] + vertical)
            )
            coordinates.add(
                (self.position[0] - horizontal, self.position[1] - vertical)
            )
        return list(coordinates)


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
    for sensor in sensors:
        ring = [
            x
            for x in sensor.get_outside_ring()
            if all(y >= 0 and y <= limit for y in x)
        ]
        for coordinate in ring:
            try:
                next(x for x in sensors if x.is_inrange(coordinate))
            except StopIteration:
                return (coordinate[0] * 4000000) + coordinate[1]
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
