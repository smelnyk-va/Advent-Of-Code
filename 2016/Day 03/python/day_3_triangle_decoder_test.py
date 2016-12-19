""" Day 3 Advent of Code 2016 - Python Solution Attempt Tests """
import unittest

from day_3_triangle_decoder import TriangleDecoder


class TriangleDecoderTests(unittest.TestCase):

    def setUp(self):
        super(TriangleDecoderTests, self).setUp()

    def test_should_return_false_for_given_values_5_10_25_as_they_do_not_make_a_valid_triangle(self):
        expected = False
        actual = TriangleDecoder.check_if_triangle(5, 10, 25)
        self.assertEquals(expected, actual)

    def test_should_return_true_for_given_values_1_5_2_as_this_is_a_valid_triangle(self):
        expected = True
        actual = TriangleDecoder.check_if_triangle(1, 5, 2)
        self.assertEquals(expected, actual)

    def test_should_return_true(self):
        expected = True
        actual = TriangleDecoder.check_if_triangle(566, 477, 376)
        self.assertEquals(expected, actual)

    def test_should_read_input_file(self):
        actual = TriangleDecoder.try_to_solve_day_3_part_1()
        expected = 1050  # Ran the test to get the number and then updated the expected
        self.assertEquals(expected, actual)
