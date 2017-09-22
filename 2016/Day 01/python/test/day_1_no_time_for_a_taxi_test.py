""" Day 1 Advent of Code 2016 - Python Solution Attempt Tests """
import unittest
from python.day_1_no_time_for_a_taxi import DirectionCalculator


class DirectionCalculatorPart1Tests(unittest.TestCase):

    def setUp(self):
        super(DirectionCalculatorPart1Tests, self).setUp()

    def test_should_return_0_0_for_starting_position(self):
        expected = (0, 0)
        actual = DirectionCalculator.direction_calculator()
        self.assertEquals(expected, actual)

    def test_fail(self):
        print " I failed "

