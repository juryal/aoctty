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


"""
def _part_one(rows: list[str]) -> str:
    for row in rows:
        for x in range(2,len(row),4):
            
    stacks = []
    return str(list([x.pop() for x in stacks]))


def part_one(puzzle_path: str) -> int:
    import aoctty.utils.read_puzzle

    return _part_one(aoctty.utils.read_puzzle.get_raw_puzzle(puzzle_path))
"""
