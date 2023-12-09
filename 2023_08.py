from pathlib import Path
from math import lcm


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]


class Map_Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.connections: dict[str, "Map_Node"] = {}

    def add_connection(self, direction: str, map_node: "Map_Node") -> None:
        self.connections[direction] = map_node


def part_one(puzzle_list: list[str]) -> int:
    map_nodes: dict[str, Map_Node] = {}
    for line in puzzle_list[1:]:
        if line:
            name, connected_nodes = [x.strip(" ()") for x in line.split("=")]
            map_nodes.setdefault(name, Map_Node(name))
            for idx, connected_node in enumerate(
                (x.strip() for x in connected_nodes.split(","))
            ):
                direction_map = {0: "L", 1: "R"}
                map_nodes[name].add_connection(
                    direction_map[idx],
                    map_nodes.setdefault(connected_node, Map_Node(connected_node)),
                )
    directions = puzzle_list[0]
    current_node = map_nodes["AAA"]
    end_node = map_nodes["ZZZ"]
    steps = 0
    while current_node != end_node:
        current_node = current_node.connections[directions[steps % len(directions)]]
        steps += 1
    return steps


print(part_one(get_raw_puzzle("2023_08_sample_1.txt")))
print(part_one(get_raw_puzzle("2023_08_sample_2.txt")))
print(part_one(get_raw_puzzle("2023_08_puzzle.txt")))


def part_two(puzzle_list: list[str]) -> int:
    map_nodes: dict[str, Map_Node] = {}
    for line in puzzle_list[1:]:
        if line:
            name, connected_nodes = [x.strip(" ()") for x in line.split("=")]
            map_nodes.setdefault(name, Map_Node(name))
            for idx, connected_node in enumerate(
                (x.strip() for x in connected_nodes.split(","))
            ):
                direction_map = {0: "L", 1: "R"}
                map_nodes[name].add_connection(
                    direction_map[idx],
                    map_nodes.setdefault(connected_node, Map_Node(connected_node)),
                )
    directions = puzzle_list[0]
    current_nodes = [map_nodes[x] for x in map_nodes if x[-1] == "A"]
    print(f"There are {len(directions)} instructions")
    steps_list: list[int] = []
    for node in current_nodes:
        steps = 0
        while not node.name.endswith("Z"):
            node = node.connections[directions[steps % len(directions)]]
            steps += 1
        steps_list.append(steps)
    return lcm(*steps_list)

    return steps


print(part_two(get_raw_puzzle("2023_08_puzzle.txt")))
