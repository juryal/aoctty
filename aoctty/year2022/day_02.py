def round_points(shapes):
    if shapes in ["AY", "BZ", "CX"]:
        return 6
    elif shapes in ["AX", "BY", "CZ"]:
        return 3
    else:
        return 0


def shape_points(shape):
    if shape == "X":
        return 1
    elif shape == "Y":
        return 2
    elif shape == "Z":
        return 3
    else:
        raise ValueError


def shape_converter(shapes):
    shift = 0
    if shapes[1] == "X":
        shift, points = 0, 0
    elif shapes[1] == "Y":
        shift, points = 1, 3
    elif shapes[1] == "Z":
        shift, points = 2, 6
    newshape = chr(((ord(shapes[0]) + shift) % 3 + 88))
    return shape_points(newshape) + points


def _part_one(list):
    total_points = 0
    for line in list:
        total_points += shape_points(line[2]) + round_points(line[0] + line[2])
    return total_points


def _part_two(list):
    total_points = 0
    for line in list:
        total_points += shape_converter(line[0] + line[2])
    return total_points


def part_one(path_string):
    import aoctty.read_puzzle

    return _part_one(aoctty.read_puzzle.get_raw_puzzle(path_string))


def part_two(path_string):
    import aoctty.read_puzzle

    return _part_two(aoctty.read_puzzle.get_raw_puzzle(path_string))
