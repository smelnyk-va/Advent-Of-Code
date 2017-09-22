""" Day 1 Advent of Code 2016 - Python Solution Attempt Tests """
import unittest
from day_1_no_time_for_a_taxi import DirectionCalculator


class DirectionCalculatorPart1Tests(unittest.TestCase):

    def setUp(self):
        super(DirectionCalculatorPart1Tests, self).setUp()

    def test_should_return_0_0_0_0_for_starting_position(self):
        actual = DirectionCalculator.direction_calculator([])
        print actual

    # def test_should_return_0_0_0_0_for_starting_position(self):
    #     expected = (0, 0, 0, 0)
    #     actual = DirectionCalculator.direction_calculator([])
    #     self.assertEquals(expected, actual)
    #
    # def test_should_return_0_1_0_0_for_moving_right_one(self):
    #     expected = (0, 1, 0, 0)
    #     directions_given = ['R1']
    #     actual = DirectionCalculator.direction_calculator(directions_given)
    #     self.assertEquals(expected, actual)
    #
    # def test_should_return_0_0_0_1_for_moving_left_one(self):
    #     expected = (0, 0, 0, 1)
    #     directions_given = ['L1']
    #     actual = DirectionCalculator.direction_calculator(directions_given)
    #     self.assertEquals(expected, actual)
    #
    # def test_should_return_0_2_0_0_for_moving_right_twice(self):
    #     expected = (0, 2, 0, 0)
    #     directions_given = ['R2']
    #     actual = DirectionCalculator.direction_calculator(directions_given)
    #     self.assertEquals(expected, actual)

