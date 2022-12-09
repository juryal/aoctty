from pathlib import Path


def get_raw_puzzle(path_string):
    puzzle_path = Path(path_string)
    with open(puzzle_path) as raw_puzzle_file:
        raw_puzzle = [line.rstrip() for line in raw_puzzle_file]
    return raw_puzzle


def get_unstripped_puzzle(path_string):
    puzzle_path = Path(path_string)
    with open(puzzle_path) as raw_puzzle_file:
        raw_puzzle = [line.rstrip() for line in raw_puzzle_file]
    return raw_puzzle
