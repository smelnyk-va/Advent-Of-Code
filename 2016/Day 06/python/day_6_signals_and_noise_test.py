""" Day 6 Advent of Code 2016 - Python Solution Attempt Tests """
import unittest

from day_6_signals_and_noise import SignalsAndNoise


class SignalsAndNoisePart1Tests(unittest.TestCase):

    def setUp(self):
        super(SignalsAndNoisePart1Tests, self).setUp()

    def test_calculate_most_common_letter_of_given_list_returns_a_for_a_list_with_three_s_it(self):
        expected = 'a'
        column_list = ['a', 'a', 'a', 'b', 'c']
        actual = SignalsAndNoise.calculate_most_common_letter_of_given_list(column_list)
        self.assertEquals(expected, actual)

    def test_calculate_the_most_common_letter_of_given_lists_and_return_combined_string(self):
            expected = 'ahhboats'
            letter_list1 = ['a', 'm', 'a', 'b', 'z', 'a', 'u', 'm']
            letter_list2 = ['a', 'h', 'h', 'h', 'o', 'w', 't', 's']
            letter_list3 = ['o', 'h', 'h', 'x', 'o', 'h', 't', 's']
            letter_list4 = ['a', 'b', 'l', 'b', 'b', 'x', 'q', 'e']
            letter_list5 = ['v', 'p', 'o', 'b', 'o', 'o', 't', 'e']
            letter_list6 = ['b', 'a', 'q', 'a', 'p', 'a', 'q', 's']
            letter_list7 = ['w', 's', 't', 't', 'r', 't', 't', 'h']
            letter_list8 = ['s', 'w', 's', 'r', 'q', 's', 't', 's']
            actual = SignalsAndNoise.calculate_most_common_letter_of_the_given_column_return_combined_string(letter_list1,
                                                                                letter_list2,
                                                                                letter_list3,
                                                                                letter_list4, letter_list5, letter_list6, letter_list7, letter_list8)
            self.assertEquals(expected, actual)

    def test_find_answer_for_day_6_part_1(self):
        expected = 'agmwzecr'  # Got the right answer!
        actual = SignalsAndNoise.day_6_signals_and_noise_part_1()
        self.assertEquals(expected, actual)
