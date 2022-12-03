import unittest
import pathlib
from aoctty.utils import read_puzzle

TEST_INPUT = pathlib.Path(__file__).parent.joinpath("test_input.txt")


class TestReadPuzzle(unittest.TestCase):
    def test_get_raw_puzzle(self):
        self.assertEqual(
            read_puzzle.get_raw_puzzle(TEST_INPUT),
            (["abc", "def", "ghi", "jkl"]),
        )
