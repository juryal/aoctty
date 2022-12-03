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
