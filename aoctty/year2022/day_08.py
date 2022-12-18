class TreeMap:
    def __init__(self, tree_map: list[str]) -> None:
        self.tree_map = tree_map

    def get_column(self, column_index: int) -> list[str]:
        return [row[column_index] for row in self.tree_map]

    def is_visible(tree_index: int, tree_line: list[str]) -> bool:
        return not (
            any(
                int(tree_line[tree_index]) <= int(tree)
                for tree in tree_line[:tree_index]
            )
            and any(
                int(tree_line[tree_index]) <= int(tree)
                for tree in tree_line[tree_index + 1 :]
            )
        )

    def count_visible(self) -> int:
        visible = len(self.tree_map * 2) + ((len(self.tree_map[0]) - 2) * 2)
        for row_index in range(1, len(self.tree_map) - 1):
            for column_index in range(1, len(self.tree_map[row_index]) - 1):
                visible += TreeMap.is_visible(
                    column_index, self.tree_map[row_index]
                ) or TreeMap.is_visible(row_index, self.get_column(column_index))
        return visible

    def count_site_lines(self, row_index: int, column_index: int) -> int:
        up = self.get_column(column_index)[: row_index + 1][::-1]
        down = self.get_column(column_index)[row_index:]
        right = self.tree_map[row_index][column_index:]
        left = self.tree_map[row_index][: column_index + 1][::-1]
        return (
            TreeMap.count_los_distance(up)
            * TreeMap.count_los_distance(down)
            * TreeMap.count_los_distance(right)
            * TreeMap.count_los_distance(left)
        )

    def count_los_distance(tree_line: list[str]) -> int:
        height = int(tree_line[0])
        los_distance = 0
        for tree in tree_line[1:]:
            los_distance += 1
            if int(tree) >= height:
                break
        return los_distance

    def find_largest_view(self) -> int:
        return max(
            self.count_site_lines(row_index, column_index)
            for row_index in range(len(self.tree_map))
            for column_index in range(len(self.tree_map[row_index]))
        )


if __name__ == "__main__":
    import aoctty.utils.read_puzzle

    treemap = TreeMap(aoctty.utils.read_puzzle.get_raw_puzzle("puzzle.txt"))
    print(treemap.count_visible())
    print(treemap.find_largest_view())
