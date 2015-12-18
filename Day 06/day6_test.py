__author__ = 'smelnyk'

import unittest

from day6_code import toggle_lights


class Day6Part1Tests(unittest.TestCase):

    # def test_turn_on_first_row_of_lights_from_string(self):
    #     result = toggle_lights('turn on 0,0 through 999,999')
    #     print "Result should turn on first line of 1000 lights. It did: " + str(result)
    #     self.assertEqual(1000, result)

    def test_turn_on_first_row_of_lights_from_file(self):
        light_instructions = open('testinput_part1.txt', 'r')
        result = toggle_lights(light_instructions)
        print "Result should turn on first line of 1000 lights. It did: " + str(result)
        self.assertEqual(1000, result)
