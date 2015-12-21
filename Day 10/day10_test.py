__author__ = 'smelnyk'

import unittest
from day10_code import get_total_length, look_and_say, look_and_say_chris


class Day10Part1Tests(unittest.TestCase):

    def test_first_example_should_return_11(self):
        result = get_total_length(1)
        self.assertEqual(11, result)

    def test_example_should_return_12(self):
        result = get_total_length(2)
        self.assertEqual(12, result)

    def test_example_should_return_13(self):
        result = get_total_length(3)
        self.assertEqual(13, result)

    def test_example_should_return_14(self):
        result = get_total_length(4)
        self.assertEqual(14, result)

    def test_example_should_return_15(self):
        result = get_total_length(5)
        self.assertEqual(15, result)

    def test_example_should_return_16(self):
        result = get_total_length(6)
        self.assertEqual(16, result)

    def test_example_should_return_17(self):
        result = get_total_length(7)
        self.assertEqual(17, result)

    def test_example_should_return_18(self):
        result = get_total_length(8)
        self.assertEqual(18, result)

    def test_example_should_return_19(self):
        result = get_total_length(9)
        self.assertEqual(19, result)

    def test_example_should_return_10(self):
        result = get_total_length(0)
        self.assertEqual(10, result)

    def test_second_example_should_return_21(self):
        result = get_total_length(11)
        self.assertEqual(21, result)

    def test_third_example_should_return_1211(self):
        result = get_total_length(21)
        self.assertEqual(1211, result)

    def test_thirdish_example_should_return_1221(self):
        result = get_total_length(211)
        self.assertEqual(1221, result)

    def test_fourth_example_should_return_111221(self):
        result = get_total_length(1211)
        self.assertEqual(111221, result)

    def test_fifth_example_should_return_312211(self):
        result = get_total_length(111221)
        self.assertEqual(312211, result)


class Day10Part1JennaSolutionTests(unittest.TestCase):

    def test_solve_day_5_part1_for_me(self):
        result = look_and_say('3113322113') #Answer not: 132123222113 or 12
        print "result is: " + str(result)
        len_of_result = len(result)
        print "Length of the Result is: " + str(len_of_result)

    def test_first_example_should_return_11(self):
        result = look_and_say('1')
        self.assertEqual('11', result)

    def test_example_should_return_12(self):
        result = look_and_say('2')
        self.assertEqual('12', result)

    def test_example_should_return_13(self):
        result = look_and_say('3')
        self.assertEqual('13', result)

    def test_example_should_return_14(self):
        result = look_and_say('4')
        self.assertEqual('14', result)

    def test_example_should_return_15(self):
        result = look_and_say('5')
        self.assertEqual('15', result)

    def test_example_should_return_16(self):
        result = look_and_say('6')
        self.assertEqual('16', result)

    def test_example_should_return_17(self):
        result = look_and_say('7')
        self.assertEqual('17', result)

    def test_example_should_return_18(self):
        result = look_and_say('8')
        self.assertEqual('18', result)

    def test_example_should_return_19(self):
        result = look_and_say('9')
        self.assertEqual('19', result)

    def test_example_should_return_10(self):
        result = look_and_say('0')
        self.assertEqual('10', result)

    def test_second_example_should_return_21(self):
        result = look_and_say('11')
        self.assertEqual('21', result)

    def test_third_example_should_return_1211(self):
        result = look_and_say('21')
        self.assertEqual('1211', result)

    def test_thirdish_example_should_return_1221(self):
        result = look_and_say('211')
        self.assertEqual('1221', result)

    def test_fourth_example_should_return_111221(self):
        result = look_and_say('1211')
        self.assertEqual('111221', result)

    def test_fifth_example_should_return_312211(self):
        result = look_and_say('111221')
        self.assertEqual('312211', result)


class Day10Part1ChrisSolutionTests(unittest.TestCase):

    def test_solve_day_5_part1_for_me(self):
        result = look_and_say_chris('3113322113') #Answer not: 329356 or 6
        print "result is: " + str(result)
        len_of_result = len(result)
        print "Length of the Result is: " + str(len_of_result)