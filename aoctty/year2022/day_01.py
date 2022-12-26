import heapq


def _part_one(list):
    calories_heap = []
    calories_total = 0
    for line in list:
        if len(line) == 0:
            heapq.heappush(calories_heap, -calories_total)
            calories_total = 0
        else:
            calories_total += int(line)
    heapq.heappush(calories_heap, -calories_total)
    return -calories_heap[0]


def _part_two(list):
    calories_heap = []
    calories_total = 0
    for line in list:
        if len(line) == 0:
            heapq.heappush(calories_heap, -calories_total)
            calories_total = 0
        else:
            calories_total += int(line)
    heapq.heappush(calories_heap, -calories_total)
    top_three = []
    for x in range(3):
        top_three.append(-heapq.heappop(calories_heap))
    return sum(top_three)


def part_one(path_string):
    import aoctty.read_puzzle

    return _part_one(aoctty.read_puzzle.get_raw_puzzle(path_string))


def part_two(path_string):
    import aoctty.read_puzzle

    return _part_two(aoctty.read_puzzle.get_raw_puzzle(path_string))
