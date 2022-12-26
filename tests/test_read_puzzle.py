import unittest
from aoctty import read_puzzle
from pathlib import Path


class TestReadPuzzle(unittest.TestCase):
    def test_get_raw_puzzle(self):
        TEST_FILE = Path(__file__).parent.joinpath("test_input.txt")
        self.assertEqual(
            read_puzzle.get_raw_puzzle(TEST_FILE),
            (["abc", "def", "ghi", "jkl"]),
        )
