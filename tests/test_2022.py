import unittest
import pathlib
from aoctty.year2022 import *
import aoctty.utils.read_puzzle as read_puzzle


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
        self.test_input = pathlib.Path(__file__).parent.joinpath("2022_03.txt")

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
        self.test_input = pathlib.Path(__file__).parent.joinpath("2022_04.txt")

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
        self.test_input = pathlib.Path(__file__).parent.joinpath("2022_05.txt")

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
        self.test_input = pathlib.Path(__file__).parent.joinpath("2022_06.txt")

    def test_part_one(self):
        self.assertEqual(
            day_06.part_one(self.test_input),
            (10),
        )


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
