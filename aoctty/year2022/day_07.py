from typing import Optional


class Node:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_size(self) -> int:
        return 0


class Directory(Node):
    def __init__(self, name: str, children: Optional[list[Node]] = None) -> None:
        Node.__init__(self, name)
        if not children:
            self.children = []
        else:
            self.children = children[:]

    def get_size(self) -> int:
        size = 0
        for child in self.children:
            size += child.get_size()
        return size

    def add_child(self, node: Node) -> None:
        self.children.append(node)


class File(Node):
    def __init__(self, name: str, size: int) -> None:
        Node.__init__(self, name)
        self.size = size

    def get_size(self) -> int:
        return self.size


class Terminal:
    def __init__(self, terminal_output: list[str]) -> None:
        self.path = []
        self.terminal_output = terminal_output
        self.process_terminal_output()
        self.sizes = []
        self.get_directory_sizes(self.path[0])

    def process_output(self, output: str) -> None:
        if output[0:3] == "dir":

            self.path[-1].add_child(Directory(output.split()[-1]))
        else:
            output = output.split()
            self.path[-1].add_child(File(output[1], int(output[0])))

    def process_input(self, input: str) -> None:
        if input[0:2] == "cd":
            if input[3:] == "..":
                self.path.pop()
            else:
                directory_name = input.split()[-1]
                try:
                    self.path.append(
                        next(
                            (
                                x
                                for x in self.path[-1].children
                                if x.name == directory_name
                            )
                        )
                    )
                except IndexError:
                    self.path.append(Directory(directory_name))

    def process_line(self, line: str) -> None:
        if line[0] == "$":
            self.process_input(line[2:])
        else:
            self.process_output(line)

    def process_terminal_output(self):
        for line in self.terminal_output:
            self.process_line(line)

    def get_directory_sizes(self, node: Node) -> list[int]:
        if type(node) is File:
            return node.get_size()
        else:
            node_size = node.get_size()
            self.sizes.append(node_size)
            for child in node.children:
                self.get_directory_sizes(child)
            return node_size

    def get_sums(self, limit: int) -> int:

        return sum(x for x in self.sizes if x <= limit)

    def free_space(self) -> int:
        TOTALSPACE = 70000000
        NEEDEDFREE = 30000000
        usedspace = max(self.sizes)
        todelete = NEEDEDFREE - (TOTALSPACE - usedspace)
        return min([x for x in self.sizes if x >= todelete])


if __name__ == "__main__":
    import aoctty.utils.read_puzzle

    terminal = Terminal(aoctty.utils.read_puzzle.get_raw_puzzle("puzzle.txt"))
    print(terminal.get_sums(100000))
    print(terminal.free_space())
