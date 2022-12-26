from collections import deque


def marker_check(signal_buffer, character):
    signal_buffer.append(character)
    print(signal_buffer)
    return len(set(signal_buffer)) == 4


def marker_check2(signal_buffer, character):
    signal_buffer.append(character)
    print(signal_buffer)
    return len(set(signal_buffer)) == 14


def _part_one(signal):
    signal_buffer = deque(maxlen=4)
    return next(
        index
        for index, value in enumerate(signal[0], start=1)
        if marker_check(signal_buffer, value)
    )


def _part_two(signal):
    signal_buffer = deque(maxlen=14)
    return next(
        index
        for index, value in enumerate(signal[0], start=1)
        if marker_check2(signal_buffer, value)
    )


def part_one(puzzle_path: str) -> int:
    import aoctty.read_puzzle

    return _part_one(aoctty.read_puzzle.get_raw_puzzle(puzzle_path))


def part_two(puzzle_path: str) -> int:
    import aoctty.read_puzzle

    return _part_two(aoctty.read_puzzle.get_raw_puzzle(puzzle_path))
