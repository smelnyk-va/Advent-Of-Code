__author__ = 'smelnyk'

import unittest
from day21_code import my_rpg_game

class Day21Part1Tests(unittest.TestCase):

    def test_foo(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2

        result = my_rpg_game(boss_health, boss_damage, boss_armor)
        print "Winner is: " + str(result)