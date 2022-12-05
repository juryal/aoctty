from collections import deque


def _part_one(rows: list[str]) -> str:
    for row in rows:
        for x in range(2,len(row),4):
            
    stacks = []
    return str(list([x.pop() for x in stacks]))


def part_one(puzzle_path: str) -> int:
    import aoctty.utils.read_puzzle

    return _part_one(aoctty.utils.read_puzzle.get_raw_puzzle(puzzle_path))
