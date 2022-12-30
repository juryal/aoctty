class Cavern:
    def __init__(self, part_two=False):
        self.tiles = set()
        self.deepest = 0
        self.floor = 2
        self.part_two = part_two

    def set_deepest(self):
        self.deepest = max(tile[1] for tile in self.tiles)
        self.floor = self.deepest + 2
        if self.part_two:
            self.deepest = self.floor + 1

    def add_tile(self, coordinates):
        self.tiles.update({coordinates})

    def remove_tile(self, coordinates):
        self.tiles.remove(coordinates)

    def move_tile(self, old_coordinates, new_coordinates):
        self.remove_tile(old_coordinates)
        self.add_tile(new_coordinates)

    def draw_rock(self, vertices):
        for index in range(len(vertices) - 1):
            x_difference = abs(vertices[index][0] - vertices[index + 1][0])
            y_difference = abs(vertices[index][1] - vertices[index + 1][1])
            [
                self.add_tile(
                    (
                        min(vertices[index][0], vertices[index + 1][0]) + x,
                        min(vertices[index][1], vertices[index + 1][1]) + y,
                    )
                )
                for x in range(x_difference + 1)
                for y in range(y_difference + 1)
            ]
        self.set_deepest()

    def tile_exists(self, coordinates):
        if coordinates in self.tiles or coordinates[1] == self.floor:
            return True
        else:
            return False

    def fill_sand(self):
        sand_count = 0
        while True:
            if self.tile_exists((500, 0)):
                return sand_count
            else:
                sand = SandTile(self)
                if sand.fall():
                    sand_count += 1
                else:
                    return sand_count


class SandTile:
    def __init__(self, cavern: Cavern):
        self.cavern = cavern
        self.coordinates = (500, 0)
        self.cavern.add_tile(self.coordinates)

    def fall_down(self):
        new_coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        return self.try_fall(new_coordinates)

    def fall_left(self):
        new_coordinates = (self.coordinates[0] - 1, self.coordinates[1] + 1)
        return self.try_fall(new_coordinates)

    def fall_right(self):
        new_coordinates = (self.coordinates[0] + 1, self.coordinates[1] + 1)
        return self.try_fall(new_coordinates)

    def try_fall(self, new_coordinates):
        if not self.cavern.tile_exists(new_coordinates):
            self.cavern.move_tile(self.coordinates, new_coordinates)
            self.coordinates = new_coordinates
            return True
        else:
            return False

    def fall(self):
        while True:
            if self.fall_down():
                if self.coordinates[1] > self.cavern.deepest:
                    return False
            elif self.fall_left():
                pass
            elif self.fall_right():
                pass
            else:
                return True


class PuzzleParser:
    @staticmethod
    def parse(line):
        vertices = []
        sections = line.split(" -> ")
        for section in sections:
            coordinates = section.split(",")
            vertices.append((int(coordinates[0]), int(coordinates[1])))
        return vertices


def part_one(rock_paths):
    cavern = Cavern()
    [cavern.draw_rock(PuzzleParser.parse(x)) for x in rock_paths]
    return cavern.fill_sand()


def part_two(rock_paths):
    cavern = Cavern(part_two=True)
    [cavern.draw_rock(PuzzleParser.parse(x)) for x in rock_paths]
    return cavern.fill_sand()


def main():
    from aoctty import read_puzzle
    from sys import argv

    args = argv[1:]
    rock_paths = read_puzzle.get_raw_puzzle("day14.txt")
    if len(args) == 0 or "1" in args:
        print(part_one(rock_paths))
    if len(args) == 0 or "2" in args:
        print(part_two(rock_paths))


if __name__ == "__main__":
    main()
