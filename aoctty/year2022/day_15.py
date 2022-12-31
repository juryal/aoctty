from aoctty import read_puzzle
from sys import argv
import re


class Parser:
    pattern = re.compile(r"[xy]=(-?\d+)")

    @staticmethod
    def parse(line):
        results = Parser.pattern.findall(line)
        sensor = (int(results[0]), int(results[1]))
        beacon = (int(results[2]), int(results[3]))
        return [sensor, beacon]


class Sensor:
    def __init__(self, position, beacon, empty_positions):
        self.position = position
        self.beacon = beacon
        self.empty_positions = empty_positions
        self.distance = self.get_distance()

    def get_distance(self):
        x_distance = abs(self.position[0] - self.beacon[0])
        y_distance = abs(self.position[1] - self.beacon[1])
        return x_distance + y_distance

    def mark_empty(self, x_distance, y_distance):
        empty_row = self.position[1] + y_distance
        if empty_row not in self.empty_positions:
            self.empty_positions.update(
                (
                    (
                        empty_row,
                        set(
                            (
                                self.position[0] + x_distance,
                                self.position[0] - x_distance,
                            )
                        ),
                    ),
                )
            )
        else:
            self.empty_positions[empty_row].update(
                (self.position[0] + x_distance, self.position[0] - x_distance)
            )

    def find_empty(self):
        for y_distance in range(self.distance + 1):
            for x_distance in range(self.distance - y_distance + 1):
                self.mark_empty(x_distance, y_distance)
                self.mark_empty(x_distance, -y_distance)


def part_one(puzzle, row):
    empty_positions = dict()
    beacons = []
    for line in puzzle:
        pair = Parser.parse(line)
        sensor = Sensor(pair[0], pair[1], empty_positions)
        beacons.append(pair[1])
        sensor.find_empty()
    for beacon in beacons:
        empty_positions[beacon[1]].discard(beacon[0])
    return len(empty_positions[row])


def main():
    args = argv[1:]
    puzzle = read_puzzle.get_raw_puzzle("day15.txt")
    if len(args) == 0 or "1" in args:
        print(part_one(puzzle, 2000000))
    if len(args) == 0 or "2" in args:
        pass


if __name__ == "__main__":
    main()
