from collections import deque
from math import lcm


class ThrowItem:
    def __init__(self, item: int, monkey_index: int):
        self.item, self.monkey_index = item, monkey_index


class Monkey:
    def __init__(self, items: deque[int], operation: callable, test: callable):
        self.items, self.operation, self.test = items, operation, test
        self.inspections = 0

    def __lt__(self, other: "Monkey"):
        return self.inspections < other.inspections

    def throw(self, item: int, target_monkey: "Monkey"):
        target_monkey.receive(item)

    def receive(self, item: int):
        self.items.append(item)

    def reduce_worry(self, item):
        return item // 3

    def inspect_item(self, item) -> ThrowItem:
        item = self.reduce_worry(self.operation(item))
        monkey_index = self.test(item)
        self.inspections += 1
        return ThrowItem(item, monkey_index)

    def inspect_items(self) -> list[ThrowItem]:
        throws = []
        while self.items:
            throws.append(self.inspect_item(self.items.popleft()))
        return throws


class MonkeyRevenge(Monkey):
    def __init__(self, items: deque[int], operation: callable, test: callable):
        super().__init__(items, operation, test)
        self.worry_divisor = 0

    def reduce_worry(self, item):
        return item % self.worry_divisor


class KeepAway:
    def __init__(self, monkey_definitions: list[str], part_two: bool = False):
        self.round = 0
        self.monkey_list = []
        self.divisors = []
        self.part_two = part_two
        for x in range(1, len(monkey_definitions), 7):
            self.monkey_list.append(self.build_monkey(monkey_definitions[x : x + 5]))
        if part_two is True:
            self.worry_divisor = lcm(*self.divisors)
            for monkey in self.monkey_list:
                monkey.worry_divisor = self.worry_divisor

    def run_round(self):
        for monkey in self.monkey_list:
            throws = monkey.inspect_items()
            for throw in throws:
                self.monkey_list[throw.monkey_index].receive(throw.item)
        self.round += 1

    def monkey_business(self):
        toptwomonkeys = sorted(self.monkey_list, reverse=True)[0:2]
        return toptwomonkeys[0].inspections * toptwomonkeys[1].inspections

    def build_monkey(self, monkey_definitions: list[str]) -> Monkey:
        items = KeepAway.gather_items(monkey_definitions[0])
        operation = KeepAway.create_operation(monkey_definitions[1])
        test = self.create_test(monkey_definitions[2:])
        if self.part_two is False:
            return Monkey(items, operation, test)
        else:
            return MonkeyRevenge(items, operation, test)

    def gather_items(items_definition: str):
        return deque(int(x) for x in items_definition.split(":")[1].split(","))

    def create_operation(operation_definition: str):
        allowed_operands = ["*", "+"]
        operation_elements = operation_definition.split("=")[1].split()
        try:
            int(operation_elements[0])
        except ValueError:
            if operation_elements[0] != "old":
                raise
        try:
            int(operation_elements[2])
        except ValueError:
            if operation_elements[2] != "old":
                raise
        if operation_elements[1] not in allowed_operands:
            raise ValueError
        return eval(
            "lambda old: {first} {operand} {second}".format(
                first=operation_elements[0],
                operand=operation_elements[1],
                second=operation_elements[2],
            )
        )

    def create_test(self, test_definition: list[str]):
        divisor = int(test_definition[0].split()[-1])
        self.divisors.append(divisor)
        true_monkey = int(test_definition[1].split()[-1])
        false_monkey = int(test_definition[2].split()[-1])

        def test(item: int) -> int:
            if item % divisor == 0:
                return true_monkey
            else:
                return false_monkey

        return test


if __name__ == "__main__":
    import aoctty.read_puzzle

    keepaway1 = KeepAway(aoctty.read_puzzle.get_raw_puzzle("puzzle.txt"))

    for x in range(20):
        keepaway1.run_round()
    print(keepaway1.monkey_business())

    keepaway2 = KeepAway(aoctty.read_puzzle.get_raw_puzzle("puzzle.txt"), part_two=True)
    for x in range(10000):
        keepaway2.run_round()
    print(keepaway2.monkey_business())
