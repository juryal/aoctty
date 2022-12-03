def rucksack_to_compartments(rucksack: str) -> list[set]:
    divider = len(rucksack) // 2
    compartment1, compartment2 = set(rucksack[:divider]), set(rucksack[divider:])
    return [compartment1, compartment2]


def item_to_priority(item: str) -> int:
    if str.isupper(item):
        adjustment = -38
    else:
        adjustment = -96
    return ord(item) + adjustment


def _part_one(rucksacks: list[str]) -> int:
    priority_total = 0
    for rucksack in rucksacks:
        compartments = rucksack_to_compartments(rucksack)
        common_item = (compartments[0] & compartments[1]).pop()
        priority_total += item_to_priority(common_item)
    return priority_total


def _part_two(rucksacks: list[str]) -> int:
    priority_total = 0
    rucksack_id = 0
    for rucksack in rucksacks:
        if rucksack_id % 3 == 0:
            group_rucksacks = []
        group_rucksacks.append(set(rucksack))
        if rucksack_id % 3 == 2:
            priority_total += item_to_priority(set.intersection(*group_rucksacks).pop())
        rucksack_id += 1
    return priority_total


def part_one(puzzle_path: str) -> int:
    import aoctty.utils.read_puzzle

    return _part_one(aoctty.utils.read_puzzle.get_raw_puzzle(puzzle_path))


def part_two(puzzle_path: str) -> int:
    import aoctty.utils.read_puzzle

    return _part_two(aoctty.utils.read_puzzle.get_raw_puzzle(puzzle_path))
