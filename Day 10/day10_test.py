__author__ = 'smelnyk'

import unittest
from day10_code import get_total_length


class Day10Part1Tests(unittest.TestCase):

    def test_first_example_should_return_11(self):
        result = get_total_length(1)
        self.assertEqual(11, result)

    def test_second_example_should_return_21(self):
        result = get_total_length(11)
        self.assertEqual(21, result)

    def test_third_example_should_return_1211(self):
        result = get_total_length(21)
        self.assertEqual(1211, result)