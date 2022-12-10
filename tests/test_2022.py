import unittest
import pathlib
from aoctty.year2022 import *


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
        import aoctty.utils.read_puzzle as read_puzzle

        self.test_input = pathlib.Path(__file__).parent.joinpath("2022_10.txt")
        self.CPU.process_instructions(read_puzzle.get_raw_puzzle(self.test_input))
        self.assertEqual(self.CPU.signal_strength, 13140)
