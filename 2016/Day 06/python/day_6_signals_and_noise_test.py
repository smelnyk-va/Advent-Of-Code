""" Day 6 Advent of Code 2016 - Python Solution Attempt Tests """
import unittest

from day_6_signals_and_noise import SignalsAndNoise


class SignalsAndNoisePart1Tests(unittest.TestCase):

    def setUp(self):
        super(SignalsAndNoisePart1Tests, self).setUp()

    def test_calculate_most_common_letter_of_given_list_returns_a_for_a_list_with_three_s_it(self):
        expected = 'a'
        actual = SignalsAndNoise.calculate_most_common_letter_of_given_list(['a', 'a', 'a', 'b', 'c'])
        self.assertEquals(expected, actual)
