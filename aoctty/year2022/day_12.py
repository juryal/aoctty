from collections import deque


class MapNode:
    def __init__(
        self,
        name: tuple[int],
        elevation: int = 0,
    ):
        self.name, self.elevation = name, elevation
        self.adjacent_nodes = set()

    def add_adjacent(self, *nodes: "MapNode"):
        for node in nodes:
            self.adjacent_nodes.add(node)

    def get_adjacent(self):
        return self.adjacent_nodes

    def check_adjacent(self, node: "MapNode"):
        return node in self.adjacent_nodes

    def set_elevation(self, elevation: int):
        self.elevation = elevation


class ElevationMap:
    def __init__(self, puzzle_input: list[str]):
        self.map_nodes = set()
        for row_index, row in enumerate(puzzle_input):
            for column_index, column in enumerate(row):

                current_node = MapNode((column_index, row_index))
                if column == "S":
                    self.start_node = current_node
                    current_node.set_elevation(97)
                elif column == "E":
                    self.end_node = current_node
                    current_node.set_elevation(122)
                else:
                    current_node.set_elevation(ord(column))
                self.map_nodes.add(current_node)
        for node in self.map_nodes:
            adjacent_adjustments = (-1, 0), (0, 1), (1, 0), (0, -1)
            node.add_adjacent(
                *[
                    x
                    for x in self.map_nodes
                    if x.name
                    in [
                        tuple(x - y for x, y in zip(node.name, x))
                        for x in adjacent_adjustments
                    ]
                ]
            )

    def get_start_node(self):
        return self.start_node

    def get_end_node(self):
        return self.end_node

    def find_shortest_steps(self, start_node=None):
        if start_node is None:
            start_node = self.start_node
            reject_elevation = 0
        else:
            reject_elevation = start_node.elevation
        visited_nodes = {start_node}
        node_queue = deque([start_node])
        parents_dict = {}
        while node_queue:

            current_node = node_queue.pop()
            if current_node == self.end_node:
                count = 0
                while current_node in parents_dict:
                    count += 1
                    current_node = parents_dict[current_node]
                return count
            for adjacent_node in current_node.get_adjacent():
                if (
                    adjacent_node not in visited_nodes
                    and adjacent_node.elevation <= current_node.elevation + 1
                    and adjacent_node.elevation != reject_elevation
                ):
                    parents_dict[adjacent_node] = current_node
                    visited_nodes.add(adjacent_node)
                    node_queue.appendleft(adjacent_node)
        return None

    def find_hiking_trail(self):
        possible_trails = set()
        for node in [x for x in self.map_nodes if x.elevation == 97]:
            steps = self.find_shortest_steps(node)
            if steps is not None:
                possible_trails.add(steps)
        return min(possible_trails)


if __name__ == "__main__":
    import aoctty.utils.read_puzzle

    elevationmap = ElevationMap(aoctty.utils.read_puzzle.get_raw_puzzle("puzzle.txt"))
    print(elevationmap.find_shortest_steps())
    print(elevationmap.find_hiking_trail())
