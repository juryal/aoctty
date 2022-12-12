from math import copysign


class Knot:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0


class Head(Knot):
    def move(self, direction: str):
        match direction:
            case "R":
                self.x_position += 1
            case "U":
                self.y_position += 1
            case "L":
                self.x_position += -1
            case "D":
                self.y_position += -1
            case _:
                raise ValueError


class Tail(Knot):
    def __init__(self, next_knot: Knot):
        super().__init__()
        self.history = {(0, 0)}
        self.next_knot = next_knot

    def set_position(self):
        x_difference = self.next_knot.x_position - self.x_position
        y_difference = self.next_knot.y_position - self.y_position
        if abs(x_difference) > 1 or abs(y_difference) > 1:
            if x_difference == 0:
                new_x = self.x_position
            else:
                new_x = int(x_difference / abs(x_difference)) + self.x_position
            if y_difference == 0:
                new_y = self.y_position
            else:
                new_y = int(y_difference / abs(y_difference)) + self.y_position
            self.x_position, self.y_position = new_x, new_y
            self.history.add((self.x_position, self.y_position))


class Rope:
    def __init__(self, tails_amount: int = 1):
        self.head = Head()
        self.tails = [Tail(self.head)]
        tails_amount += -1
        while tails_amount > 0:
            self.tails.append(Tail(self.tails[-1]))
            tails_amount += -1

    def move_head(self, movements):
        for movement in movements:
            direction, steps = movement.split()
            steps = int(steps)
            while steps > 0:
                self.head.move(direction)
                for tail in self.tails:
                    tail.set_position()
                steps += -1

    def count_positions(self):
        return len(self.tails[-1].history)


if __name__ == "__main__":
    import aoctty.utils.read_puzzle

    ropes = [Rope(), Rope(9)]
    for rope in ropes:
        rope.move_head(aoctty.utils.read_puzzle.get_raw_puzzle("puzzle.txt"))
        print(rope.count_positions())
