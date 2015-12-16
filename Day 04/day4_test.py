__author__ = 'smelnyk'

import unittest
from day4_code import mine_bitcoins


class Day4Part1Tests(unittest.TestCase):

    def test_first_test_example_given(self):
        secret_key = "abcdef"
        result = mine_bitcoins(secret_key)
        self.assertEqual(609043, result)

    def test_second_test_example_given(self):
        secret_key = "pqrstuv"
        result = mine_bitcoins(secret_key)
        self.assertEqual(1048970, result)

    # def test_solve_day4_part1(self):
    #     secret_key = "yzbqklnj"
    #     result = mine_bitcoins(secret_key)
    #     print "The Answer to Day 4, Part 1 is: " + str(result)