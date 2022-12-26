from collections import deque


def _split_list(original_list: list[str]) -> int:
    return next(i for i, v in enumerate(original_list) if v[0:1] == "")


def assemble_stacks(stack_list):
    stack_queues = []
    for row in stack_list:
        for i, v in enumerate(range(1, len(row), 4)):
            if row[v] != " ":
                if len(stack_queues) < i + 1:
                    stack_queues.extend(
                        deque() for x in range(i + 1 - len(stack_queues))
                    )
                stack_queues[i].appendleft(row[v])
    return stack_queues


def move_crate(instruction, stack_queues):
    instruction = instruction.split()
    quantity = int(instruction[1])
    source = int(instruction[3])
    destination = int(instruction[5])
    for x in range(quantity):
        stack_queues[destination - 1].append(stack_queues[source - 1].pop())


def move_crate_9001(instruction, stack_queues):
    instruction = instruction.split()
    quantity = int(instruction[1])
    source = int(instruction[3])
    destination = int(instruction[5])
    crane = deque()
    for x in range(quantity):
        crane.append(stack_queues[source - 1].pop())
    for x in range(quantity):
        stack_queues[destination - 1].append(crane.pop())


def _part_one(puzzle: list[str]) -> str:
    divider = _split_list(puzzle)
    stack_queues = assemble_stacks(puzzle[: divider - 1])
    instructions = puzzle[divider + 1 :]
    for instruction in instructions:
        move_crate(instruction, stack_queues)
    return "".join(list([x.pop() for x in stack_queues]))


def _part_two(puzzle: list[str]) -> str:
    divider = _split_list(puzzle)
    stack_queues = assemble_stacks(puzzle[: divider - 1])
    instructions = puzzle[divider + 1 :]
    for instruction in instructions:
        move_crate_9001(instruction, stack_queues)
    return "".join(list([x.pop() for x in stack_queues]))


def part_one(puzzle_path: str) -> int:
    import aoctty.read_puzzle

    return _part_one(aoctty.read_puzzle.get_raw_puzzle(puzzle_path))


def part_two(puzzle_path: str) -> int:
    import aoctty.read_puzzle

    return _part_two(aoctty.read_puzzle.get_raw_puzzle(puzzle_path))
