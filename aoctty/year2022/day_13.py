from typing import Any
import bisect

Value = list[Any] | int
Packet = list[Value]
Pair = dict[str, Packet]


class ElfPacket(list):
    def __lt__(self, other_packet: "ElfPacket") -> bool:
        return ElfPacket._compare(self, other_packet) < 0

    @staticmethod
    def _compare(left_packet: Value, right_packet: Value) -> int:
        if isinstance(left_packet, int):
            if isinstance(right_packet, int):
                return left_packet - right_packet
            else:
                return ElfPacket._compare([left_packet], right_packet)
        elif isinstance(right_packet, int):
            return ElfPacket._compare(left_packet, [right_packet])
        else:
            for (left, right) in zip(left_packet, right_packet):
                result = ElfPacket._compare(left, right)
                if result != 0:
                    return result
            return len(left_packet) - len(right_packet)


def assemble_packets(puzzle: list[str]) -> list[ElfPacket]:
    packet_list = []
    for x in range(0, len(puzzle), 3):
        packet_list.extend([ElfPacket(eval(puzzle[x])), ElfPacket(eval(puzzle[x + 1]))])
    return packet_list


def assemble_pairs(packets: list[ElfPacket]) -> list[Pair]:
    pairs = []
    for x in range(0, len(packets), 2):
        pairs.append({"left": packets[x], "right": packets[x + 1]})
    return pairs


def part_one(packets: list[ElfPacket]) -> int:
    pairs = assemble_pairs(packets)
    sum = 0
    for index, pair in enumerate(pairs):
        if ElfPacket._compare(pair["left"], pair["right"]) < 0:
            sum += index + 1
    return sum


def part_two(packets: list[ElfPacket]) -> int:
    packets.sort()
    FIRST_MARKER = ElfPacket([[2]])
    SECOND_MARKER = ElfPacket([[6]])
    first_position = bisect.bisect(packets, FIRST_MARKER) + 1
    second_position = bisect.bisect(packets, SECOND_MARKER) + 2
    return first_position * second_position


def main() -> None:
    from aoctty import read_puzzle
    from sys import argv

    args = argv[1:]
    packets = assemble_packets(read_puzzle.get_raw_puzzle("day13.txt"))
    if len(args) == 0 or "1" in args:
        print(part_one(packets))
    if len(args) == 0 or "2" in args:
        print(part_two(packets))


if __name__ == "__main__":
    main()


# def compare_values(value1, value2) -> int:
#     try:
#         if value1 < value2:
#             return 1
#         elif value1 > value2:
#             return -1
#         else:
#             return 0
#     except TypeError:
#         if type(value1) is not list:
#             value1 = [value1]
#         if type(value2) is not list:
#             value2 = [value2]
#         try:
#             return next(
#                 compare_values(*x)
#                 for x in zip(value1, value2)
#                 if compare_values(*x) != 0
#             )
#         except StopIteration:
#             if len(value1) < len(value2):
#                 return 1
#             elif len(value1) > len(value2):
#                 return -1
#             else:
#                 return 0


# if __name__ == "__main__":
#     import aoctty.utils.read_puzzle

#     packets = aoctty.utils.read_puzzle.get_raw_puzzle("puzzle.txt")
#     total = 0
#     index = 1
#     for x in range(0, len(packets), 3):
#         value1 = eval(packets[x])
#         value2 = eval(packets[x + 1])

#         if compare_values(value1, value2) == 1:
#             total += index
#         index += 1
#     print(total)
