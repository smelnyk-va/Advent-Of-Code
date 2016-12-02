__author__ = 'smelnyk'

import unittest
from day4_code import mine_bitcoins_part1, mine_bitcoins_part2


class Day4Part1Tests(unittest.TestCase):

    def test_first_test_example_given(self):
        secret_key = "abcdef"
        result = mine_bitcoins_part1(secret_key)
        self.assertEqual(609043, result)

    def test_second_test_example_given(self):
        secret_key = "pqrstuv"
        result = mine_bitcoins_part1(secret_key)
        self.assertEqual(1048970, result)

    def test_solve_day4_part1(self):
        secret_key = "yzbqklnj"
        result = mine_bitcoins_part1(secret_key)
        print "The Answer to Day 4, Part 1 is: " + str(result) #Answer: 282749


class Day4Part2Tests(unittest.TestCase):

    def test_first_test_example_given(self):
        secret_key = "abcdef"
        result = mine_bitcoins_part2(secret_key)
        # print "The Answer is: " + str(result) # Answer: 6742839
        self.assertEqual(6742839, result)

    def test_second_test_example_given(self):
        secret_key = "pqrstuv"
        result = mine_bitcoins_part2(secret_key)
        # print "The Answer is: " + str(result) # Answer: 5714438
        self.assertEqual(5714438, result)

    def test_solve_day4_part2(self):
        secret_key = "yzbqklnj"
        result = mine_bitcoins_part2(secret_key)
        # print "The Answer to Day 4, Part 2 is: " + str(result) # Answer: 9962624
        self.assertEqual(9962624, result)
