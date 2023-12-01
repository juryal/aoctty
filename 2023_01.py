from pathlib import Path
import re


def get_raw_puzzle(path_string: str | Path) -> list[str]:
    puzzle_path: Path = Path(Path.cwd()).joinpath(path_string)
    with puzzle_path.open() as puzzle_file:
        return [line.rstrip() for line in puzzle_file]


def part_one(list):
    runningtotal = 0
    for line in list:
        firstdigit = int(next((x for x in line if x.isdigit())))
        lastdigit = int(next((x for x in reversed(line) if x.isdigit())))
        runningtotal = runningtotal + (firstdigit * 10) + lastdigit
    return runningtotal


print(part_one(get_raw_puzzle("./2023_01_puzzle.txt")))
labels = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numberdictionary = {k: v + 1 for (v, k) in enumerate(labels)}


def get_int(number: str) -> int:
    if not number.isdigit():
        return numberdictionary[number]
    else:
        return int(number)


def part_two(list):
    runningtotal = 0
    regex = "(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))"
    for line in list:
        matches = [x.group(1) for x in re.finditer(regex, line)]
        firstdigit = get_int(matches[0])
        lastdigit = get_int(matches[-1])
        runningtotal = runningtotal + (firstdigit * 10) + lastdigit
    return runningtotal


print(part_two(get_raw_puzzle("./2023_01_puzzle.txt")))
