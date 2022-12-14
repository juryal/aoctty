import unittest
import pathlib
from aoctty.year2022 import (
    day_01,
    day_02,
    day_03,
    day_04,
    day_05,
    day_06,
    day_07,
    day_08,
    day_09,
    day_10,
    day_11,
    day_12,
    day_13,
    day_14,
    day_15,
)
import aoctty.read_puzzle as read_puzzle


class TestDayOne(unittest.TestCase):
    def setUp(self):
        self.test_input = pathlib.Path(__file__).parent.joinpath("2022_01.txt")

    def test_part_one(self):
        self.assertEqual(
            day_01.part_one(self.test_input),
            (24000),
        )

    def test_part_two(self):
        self.assertEqual(
            day_01.part_two(self.test_input),
            (45000),
        )


class TestDayTwo(unittest.TestCase):
    def setUp(self):
        self.test_input = pathlib.Path(__file__).parent.joinpath("2022_02.txt")

    def test_part_one(self):
        self.assertEqual(
            day_02.part_one(self.test_input),
            (15),
        )

    def test_part_two(self):
        self.assertEqual(
            day_02.part_two(self.test_input),
            (12),
        )


class TestDayThree(unittest.TestCase):
    def setUp(self):
        self.test_input = str(pathlib.Path(__file__).parent.joinpath("2022_03.txt"))

    def test_part_one(self):
        self.assertEqual(
            day_03.part_one(self.test_input),
            (157),
        )

    def test_part_two(self):
        self.assertEqual(
            day_03.part_two(self.test_input),
            (70),
        )


class TestDayFour(unittest.TestCase):
    def setUp(self):
        self.test_input = str(pathlib.Path(__file__).parent.joinpath("2022_04.txt"))

    def test_part_one(self):
        self.assertEqual(
            day_04.part_one(self.test_input),
            (2),
        )

    def test_part_two(self):
        self.assertEqual(
            day_04.part_two(self.test_input),
            (4),
        )


class TestDayFive(unittest.TestCase):
    from collections import deque

    def setUp(self):
        self.test_list = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
        ]
        self.test_input = str(pathlib.Path(__file__).parent.joinpath("2022_05.txt"))

    def test_split_list(self):
        self.assertEqual(day_05._split_list(self.test_list), (4))

    def test_assemble_stacks(self):
        self.assertEqual(
            day_05.assemble_stacks(self.test_list[0:3]),
            ([self.deque(["Z", "N"]), self.deque(["M", "C", "D"]), self.deque(["P"])]),
        )

    def test_part_one(self):
        self.assertEqual(day_05.part_one(self.test_input), ("CMZ"))


class TestDaySix(unittest.TestCase):
    def setUp(self):
        self.test_input = str(pathlib.Path(__file__).parent.joinpath("2022_06.txt"))

    def test_part_one(self):
        self.assertEqual(
            day_06.part_one(self.test_input),
            (10),
        )


class TestDaySeven(unittest.TestCase):
    def test_directory_get_size(self):
        directory = day_07.Directory("/")
        self.assertEqual(directory.get_size(), 0)

    def test_get_sum(self):
        test_input = pathlib.Path(__file__).parent.joinpath("2022/2022_07.txt")
        terminal = day_07.Terminal(read_puzzle.get_raw_puzzle(test_input))
        self.assertEqual(terminal.get_sums(100000), 95437)

    def test_free_space(self):
        test_input = pathlib.Path(__file__).parent.joinpath("2022/2022_07.txt")
        terminal = day_07.Terminal(read_puzzle.get_raw_puzzle(test_input))
        self.assertEqual(terminal.free_space(), 24933642)


class TestDayEight(unittest.TestCase):
    def setUp(self) -> None:
        import aoctty.read_puzzle

        self.treemap = day_08.TreeMap(
            aoctty.read_puzzle.get_raw_puzzle(
                pathlib.Path(__file__).parent.joinpath("2022/2022_08.txt")
            )
        )

    def test_get_column(self):
        self.assertEqual(self.treemap.get_column(2), ["3", "5", "3", "5", "3"])

    def test_count_visible(self):
        self.assertEqual(self.treemap.count_visible(), 21)

    def test_site_lines(self):
        self.assertEqual(self.treemap.count_site_lines(1, 2), 4)

    def test_find_largest_view(self):
        self.assertEqual(self.treemap.find_largest_view(), 8)


class TestDayNine(unittest.TestCase):
    def setUp(self):

        self.test_input = pathlib.Path(__file__).parent.joinpath("2022_09.txt")

    def test_part_one(self):
        rope = day_09.Rope()
        rope.move_head(read_puzzle.get_raw_puzzle(self.test_input))
        self.assertEqual(
            rope.count_positions(),
            13,
        )

    def test_part_two(self):
        rope = day_09.Rope(9)
        rope.move_head(read_puzzle.get_raw_puzzle(self.test_input))
        self.assertEqual(
            rope.count_positions(),
            1,
        )

    def test_part_two_longer(self):
        rope = day_09.Rope(9)
        rope.move_head(
            read_puzzle.get_raw_puzzle(
                pathlib.Path(__file__).parent.joinpath("2022/2022_09b.txt")
            )
        )
        self.assertEqual(
            rope.count_positions(),
            36,
        )


class TestDayTen(unittest.TestCase):
    def setUp(self):
        self.CPU = day_10.SimpleCPU([20, 60, 100, 140, 180, 220])

    def test_load_operation(self):
        self.CPU.load_operation("addx -7")
        self.assertEqual(
            self.CPU.operation,
            {"adjustment": -7, "counter": 2},
        )

    def test_run_operation(self):
        self.CPU.load_operation("addx -7")
        self.CPU.run_operation()
        self.assertEqual(
            self.CPU.register,
            -6,
        )

    def test_part_one(self):

        self.test_input = pathlib.Path(__file__).parent.joinpath("2022_10.txt")
        self.CPU.process_instructions(read_puzzle.get_raw_puzzle(self.test_input))
        self.assertEqual(self.CPU.signal_strength, 13140)


class TestDayEleven(unittest.TestCase):
    def setUp(self):

        self.test_input = pathlib.Path(__file__).parent.joinpath("2022_11.txt")

    def test_part_one(self):
        keepaway1 = day_11.KeepAway(read_puzzle.get_raw_puzzle(self.test_input))
        for x in range(20):
            keepaway1.run_round()
            print(keepaway1.monkey_business())

        self.assertEqual(
            keepaway1.monkey_business(),
            10605,
        )

    def test_part_two(self):
        keepaway1 = day_11.KeepAway(
            read_puzzle.get_raw_puzzle(self.test_input), part_two=True
        )
        for x in range(10000):
            keepaway1.run_round()
            print(keepaway1.monkey_business())

        self.assertEqual(
            keepaway1.monkey_business(),
            2713310158,
        )


class TestDayTwelve(unittest.TestCase):
    def setUp(self):

        self.test_input = pathlib.Path(__file__).parent.joinpath("2022/2022_12.txt")
        self.elevationmap = day_12.ElevationMap(
            read_puzzle.get_raw_puzzle(self.test_input)
        )

    def test_get_start_node(self):
        self.assertEqual(self.elevationmap.get_start_node().name, (0, 0))

    def test_get_end_node(self):
        self.assertEqual(self.elevationmap.get_end_node().name, (5, 2))

    def test_find_shortest_steps(self):
        self.assertEqual(self.elevationmap.find_shortest_steps(), 31)

    def test_find_hiking_trail(self):
        self.assertEqual(self.elevationmap.find_hiking_trail(), 29)


class TestDayThirteen(unittest.TestCase):
    def setUp(self):
        self.test_input = read_puzzle.get_raw_puzzle(
            pathlib.Path(__file__).parent.joinpath("2022/2022_13.txt")
        )

    def test_assemble_packets(self):
        self.assertEqual(
            day_13.assemble_packets(self.test_input),
            [
                [1, 1, 3, 1, 1],
                [1, 1, 5, 1, 1],
                [[1], [2, 3, 4]],
                [[1], 4],
                [9],
                [[8, 7, 6]],
                [[4, 4], 4, 4],
                [[4, 4], 4, 4, 4],
                [7, 7, 7, 7],
                [7, 7, 7],
                [],
                [3],
                [[[]]],
                [[]],
                [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
                [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
            ],
        )

    def test_assemble_pairs_0(self):
        packets = day_13.assemble_packets(self.test_input)
        self.assertEqual(
            day_13.assemble_pairs(packets)[0],
            {"left": [1, 1, 3, 1, 1], "right": [1, 1, 5, 1, 1]},
        )

    def test_assemble_pairs_7(self):
        packets = day_13.assemble_packets(self.test_input)
        self.assertEqual(
            day_13.assemble_pairs(packets)[7],
            {
                "left": [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
                "right": [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
            },
        )

    def test_ElfPacket_compare_0(self):
        pairs = day_13.assemble_pairs(day_13.assemble_packets(self.test_input))

        self.assertLess(
            day_13.ElfPacket._compare(pairs[0]["left"], pairs[0]["right"]), 0
        )

    def test_ElfPacket_compare_3(self):
        pairs = day_13.assemble_pairs(day_13.assemble_packets(self.test_input))

        self.assertLess(
            day_13.ElfPacket._compare(pairs[3]["left"], pairs[3]["right"]), 0
        )

    def test_ElfPacket_compare_7(self):
        pairs = day_13.assemble_pairs(day_13.assemble_packets(self.test_input))

        self.assertGreater(
            day_13.ElfPacket._compare(pairs[7]["left"], pairs[7]["right"]), 0
        )

    def test_part_one(self):
        self.assertEqual(day_13.part_one(day_13.assemble_packets(self.test_input)), 13)

    def test_part_two(self):
        self.assertEqual(day_13.part_two(day_13.assemble_packets(self.test_input)), 140)


class TestDayFourteen(unittest.TestCase):
    def setUp(self):
        self.test_input = read_puzzle.get_raw_puzzle(
            pathlib.Path(__file__).parent.joinpath("2022/2022_14.txt")
        )

    def test_draw_rocks_vertical_short(self):
        cavern = day_14.Cavern()
        cavern.draw_rock([(1, 1), (1, 2)])
        self.assertSetEqual(cavern.tiles, {(1, 1), (1, 2)})

    def test_draw_rocks_horizontal_long(self):
        cavern = day_14.Cavern()
        cavern.draw_rock([(600, 11), (606, 11)])
        self.assertSetEqual(
            cavern.tiles,
            {
                (600, 11),
                (601, 11),
                (602, 11),
                (603, 11),
                (604, 11),
                (605, 11),
                (606, 11),
            },
        )

    def test_draw_rocks_zig_zag(self):
        cavern = day_14.Cavern()
        cavern.draw_rock([(10, 100), (13, 100), (13, 96), (14, 96)])
        self.assertSetEqual(
            cavern.tiles,
            {
                (10, 100),
                (11, 100),
                (12, 100),
                (13, 100),
                (13, 99),
                (13, 98),
                (13, 97),
                (13, 96),
                (14, 96),
            },
        )

    def test_set_deepest(self):
        cavern = day_14.Cavern()
        cavern.draw_rock([(5, 10), (5, 28)])
        cavern.set_deepest()
        self.assertEqual(cavern.deepest, 28)

    def test_move_tile(self):
        cavern = day_14.Cavern()
        cavern.add_tile((100, 1))
        cavern.move_tile((100, 1), (100, 2))
        self.assertSetEqual(cavern.tiles, {(100, 2)})

    def test_empty_cavern(self):
        cavern = day_14.Cavern()
        self.assertEqual(cavern.fill_sand(), 0)

    def test_simple_cavern_1(self):
        cavern = day_14.Cavern()
        cavern.draw_rock([(499, 50), (501, 50)])
        self.assertEqual(cavern.fill_sand(), 1)

    def test_simple_cavern_2(self):
        cavern = day_14.Cavern()
        cavern.draw_rock([(498, 50), (502, 50)])
        self.assertEqual(cavern.fill_sand(), 4)

    def test_simple_cavern_3(self):
        cavern = day_14.Cavern()
        cavern.draw_rock([(498, 50), (502, 50)])
        cavern.draw_rock([(498, 5), (498, 7), (501, 7), (501, 5)])
        self.assertEqual(cavern.fill_sand(), 6)

    def test_parser(self):
        self.assertListEqual(
            day_14.PuzzleParser.parse("498,4 -> 498,6 -> 496,6"),
            [(498, 4), (498, 6), (496, 6)],
        )

    def test_part_one(self):
        self.assertEqual(day_14.part_one(self.test_input), 24)

    def test_part_two(self):
        self.assertEqual(day_14.part_two(self.test_input), 93)


class TestDayFifteen(unittest.TestCase):
    def setUp(self):
        self.test_input = read_puzzle.get_raw_puzzle(
            pathlib.Path(__file__).parent.joinpath("2022/2022_15.txt")
        )

    def test_parser(self):
        self.assertTupleEqual(
            day_15.Parser.parse(self.test_input[0]), ((2, 18), (-2, 15))
        )

    def test_get_outside_ring_1(self):
        sensor = day_15.Sensor((0, 0), (1, 1))
        self.assertEqual(len(sensor.get_outside_ring()), 12)

    def test_get_outside_ring_2(self):
        sensor = day_15.Sensor((0, 0), (2, 2))
        self.assertIn((3, 2), sensor.get_outside_ring())

    def test_part_one(self):
        self.assertEqual(day_15.part_one(self.test_input, 10), 26)

    def test_part_two(self):
        self.assertEqual(day_15.part_two(self.test_input, 20), 56000011)
