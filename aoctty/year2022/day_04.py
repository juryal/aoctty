def _assignment_to_sections(assignment: str) -> set[int]:
    section_endpoints = list(map(int, assignment.split("-")))
    section_endpoints[1] += 1
    return set(range(*section_endpoints))


def _pairs_to_assignments(pair):
    pair_sections = list(map(_assignment_to_sections, pair.split(",")))
    return pair_sections


def _part_one(pairs: list[str]) -> int:
    assignment_subsets = 0
    for pair in pairs:
        pair_sections = _pairs_to_assignments(pair)
        if max(map(len, pair_sections)) == len(set.union(*pair_sections)):
            assignment_subsets += 1
    return assignment_subsets


def _part_two(pairs: list[str]) -> int:
    assignment_overlaps = 0
    for pair in pairs:
        pair_sections = _pairs_to_assignments(pair)
        if sum(map(len, pair_sections)) != len(set.union(*pair_sections)):
            assignment_overlaps += 1
    return assignment_overlaps


def part_one(puzzle_path: str) -> int:
    import aoctty.utils.read_puzzle

    return _part_one(aoctty.utils.read_puzzle.get_raw_puzzle(puzzle_path))


def part_two(puzzle_path: str) -> int:
    import aoctty.utils.read_puzzle

    return _part_two(aoctty.utils.read_puzzle.get_raw_puzzle(puzzle_path))
