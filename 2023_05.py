from pathlib import Path


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]

def updatemap(destination_start,source_start,span,seeds_map,index_marker):
    change =  destination_start - source_start
    for idx,x in enumerate(list(zip(*seeds_map))[index_marker]):
        if x in range(source_start,source_start+span):
            seeds_map[idx][index_marker + 1:] = [x + change] * len(seeds_map[idx][index_marker + 1:])
            pass

            
def part_one(puzzle_list: list[str]) -> int:
    seeds_map = [[int(x)] * 8 for x in puzzle_list[0].split(":")[1].split()]
    index_marker=-1
    for line in list(filter(None,puzzle_list[1:])):
        if line[0].isdigit():
            destination_start,source_start,span = [int(x) for x in line.split()]
            updatemap(destination_start,source_start,span,seeds_map,index_marker)
        elif line[0].isalpha():
            index_marker +=1
    return min(list(zip(*seeds_map))[-1])

print(part_one(get_raw_puzzle('2023_05_puzzle.txt')))