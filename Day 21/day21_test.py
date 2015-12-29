__author__ = 'smelnyk'

import unittest
from day21_code import my_rpg_game


class Day21Part1Tests(unittest.TestCase):

    # Decide on some weapons, armor, accessories to buy
    # Store options are:
    # Weapons: Dagger, Shortsword, Warhammer, Longsword, Greataxe
    # Armor: Leather, Chainmail, Splintmail, Bandedmail, Platemail
    # Accessories: Damage1, Damage2, Damage3, Defence1, Defence2, Defence3

    """ Weapons Only Tests """

    def test_using_just_a_dagger_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor = None
        accessories1 = None
        accessories2 = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor, accessories1, accessories2)
        self.assertEqual(8, result)
        # Dies in 12 turns with -8 health, Player does 2 damage, boss does 9

    def test_using_just_a_shortsword_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor = None
        accessories1 = None
        accessories2 = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor, accessories1, accessories2)
        self.assertEqual(10, result)
        # Dies in 12 turns with -8 health, Player does 3 damage, boss does 9

    def test_using_just_a_warhammer_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor = None
        accessories1 = None
        accessories2 = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor, accessories1, accessories2)
        self.assertEqual(25, result)
        # Dies in 12 turns with -8 health, Player does 4 damage, boss does 9

    def test_using_just_a_longsword_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor = None
        accessories1 = None
        accessories2 = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor, accessories1, accessories2)
        self.assertEqual(40, result)
        # Dies in 12 turns with -8 health, Player does 5 damage, boss does 9

    def test_using_just_a_Greataxe_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor = None
        accessories1 = None
        accessories2 = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor, accessories1, accessories2)
        self.assertEqual(74, result)
        # Dies in 12 turns with -8 health, Player does 6 damage, boss does 9

    """ Armor Only Tests """

    def test_using_just_leather_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Leather'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(13, result)
        # Dies in 13 turns with -4 health, Player does 1 damage, boss does 8

    def test_using_just_chainmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Chainmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(31, result)
        # Dies in 15 turns with -5 health, Player does 1 damage, boss does 7

    def test_using_just_Splintmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Splintmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(53, result)
        # Dies in 17 turns with -2 health, Player does 1 damage, boss does 6

    def test_using_just_bandedmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Bandedmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(75, result)
        # Dies in 20 turns with 0 health, Player does 1 damage, boss does 5

    def test_using_just_platemail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Platemail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(102, result)
        # Dies in 25 turns with 0 health, Player does 1 damage, boss does 4

    """ Accessories Only Tests """

    def test_using_just_one_damage1_ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = None
        accessories1_name = 'Damage1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(25, result)
        # Dies in 12 turns with -8 health, Player does 1 damage, boss does 9

    def test_using_just_one_damage2_ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = None
        accessories1_name = 'Damage2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(50, result)
        # Dies in 12 turns with -8 health, Player does 1 damage, boss does 9

    def test_using_just_one_damage3_ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = None
        accessories1_name = 'Damage3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(100, result)
        # Dies in 12 turns with -8 health, Player does 1 damage, boss does 9

    def test_using_just_one_defense1_ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = None
        accessories1_name = 'Defense1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(20, result)
        # Dies in 13 turns with -4 health, Player does 1 damage, boss does 8

    def test_using_just_one_defense2_ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = None
        accessories1_name = 'Defense2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(40, result)
        # Dies in 15 turns with -5 health, Player does 1 damage, boss does 7

    def test_using_just_one_defense3_ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = None
        accessories1_name = 'Defense3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(80, result)  # Gold Spent 80
        # Dies in 17 turns with -2 health, Player does 1 damage, boss does 6

    """ Simple Weapon and Armor Upgraded Tests """

    def test_using_a_Dagger_and_Leather_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = 'Leather'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(21, result)  # Gold Spent 21
        # Dies in 13 turns with -4 health, Player does 2 damage, boss does 8

    def test_using_a_Shortsword_and_Chainmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = 'Chainmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(41, result)  # Gold Spent 41
        # Dies in 15 turns with -5 health, Player does 3 damage, boss does 7

    def test_using_a_Warhammer_and_Splintmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = 'Splintmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(78, result)  # Gold Spent 78 (25 + 53)
        # Dies in 17 turns with -2 health left. Boss has 35 health remaining.
        # Player does 4 damage, boss does 6 damage.

    def test_using_a_Longsword_and_Bandedmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = 'Bandedmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(115, result)  # Gold Spent 115 (40 + 75)
        # Dies in 20 turns with 0 health left. Boss has 3 health remaining.
        # Player does 5 damage, boss does 5 damage.

    def test_using_a_Greataxe_and_Platemail_armor_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = 'Platemail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(176, result)  # Gold Spent 176 (74 + 102)
        # !WINS! in 18 turns with 28 health left. Boss has -5 health remaining.
        # Player does 6 damage, boss does 4 damage.

    """ Different Weapons and Leather Armor """

    def test_using_a_Shortsword_and_Leather_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = 'Leather'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(23, result)  # Gold Spent 23 (10 + 13)
        # Dies in 13 turns with -4 health left. Boss has 64 health remaining.
        # Player does 3 damage, boss does 9 damage.

    def test_using_a_Warhammer_and_Leather_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = 'Leather'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(38, result)  # Gold Spent 23 (25 + 13)
        # DEAD! Player died in 13 turns with -4 health left.
        # Boss has 51 health remaining. Player does 4 damage, boss does 9 damage.

    def test_using_a_Longsword_and_Leather_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = 'Leather'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(53, result)  # Gold Spent 23 (40 + 13)
        # DEAD! Player died in 13 turns with -4 health left. Boss has 38 health remaining.
        # Player does 5 damage, boss does 9 damage.

    def test_using_a_Greataxe_and_Leather_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = 'Leather'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(87, result)  # Gold Spent 23 (74 + 13)
        # DEAD! Player died in 13 turns with -4 health left. Boss has 25 health remaining.
        # Player does 6 damage, boss does 9 damage.

    """ Different Weapons and Chainmail Armor """

    def test_using_a_Dagger_and_Chainmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = 'Chainmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(39, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 73 health remaining.
        # Player does 2 damage, boss does 9 damage. Gold spent 39.

    def test_using_a_Warhammer_and_Chainmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = 'Chainmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(56, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 43 health remaining.
        # Player does 4 damage, boss does 9 damage. Gold spent 56.

    def test_using_a_Longsword_and_Chainmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = 'Chainmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(71, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 28 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 71.

    def test_using_a_Greataxe_and_Chainmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = 'Chainmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(105, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 13 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 105.

    """ Different Weapons and Splintmail Armor """

    def test_using_a_Dagger_and_Splintmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = 'Splintmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(61, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 69 health remaining.
        # Player does 2 damage, boss does 9 damage. Gold spent 61.

    def test_using_a_Shortsword_and_Splintmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = 'Splintmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(63, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 52 health remaining.
        # Player does 3 damage, boss does 9 damage. Gold spent 63.

    def test_using_a_Longsword_and_Splintmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = 'Splintmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(93, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 18 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 93.

    def test_using_a_Greataxe_and_Splintmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = 'Splintmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(127, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 1 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 127.

    """ Different Weapons and Bandedmail Armor """

    def test_using_a_Dagger_and_Bandedmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = 'Bandedmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(83, result)
        # DEAD! Player died in 20 turns with 0 health left. Boss has 63 health remaining.
        # Player does 2 damage, boss does 9 damage. Gold spent 83.

    def test_using_a_Shortsword_and_Bandedmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = 'Bandedmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(85, result)
        # DEAD! Player died in 20 turns with 0 health left. Boss has 43 health remaining.
        # Player does 3 damage, boss does 9 damage. Gold spent 85.

    def test_using_a_Warhammer_and_Bandedmail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = 'Bandedmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(100, result)
        # DEAD! Player died in 20 turns with 0 health left. Boss has 23 health remaining.
        # Player does 4 damage, boss does 9 damage. Gold spent 100.

    def test_using_a_Greataxe_and_Bandedmail_armor_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = 'Bandedmail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(149, result)  # Gold Spent 149 (74 + 75)
        # !WINS! in 18 turns with 10 health left. Boss has -5 health remaining.
        # Player does 6 damage, boss does 5 damage.

    """ Different Weapons and Platemail Armor """

    def test_using_a_Dagger_and_Platemail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = 'Platemail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(110, result)  # Gold Spent 142 (40 + 102)
        # DEAD! Player died in 25 turns with 0 health left. Boss has 53 health remaining.
        # Player does 2 damage, boss does 9 damage. Gold spent 110.

    def test_using_a_Shortsword_and_Platemail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = 'Platemail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(112, result)  # Gold Spent 142 (40 + 102)
        # DEAD! Player died in 25 turns with 0 health left. Boss has 28 health remaining.
        # Player does 3 damage, boss does 9 damage. Gold spent 112.

    def test_using_a_Warhammer_and_Platemail_armor_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = 'Platemail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(127, result)
        # DEAD! Player died in 25 turns with 0 health left. Boss has 3 health remaining.
        # Player does 4 damage, boss does 9 damage. Gold spent 127.

    def test_using_a_Longsword_and_Platemail_armor_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = 'Platemail'
        accessories1_name = None
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(142, result)  # Gold Spent 142 (40 + 102)
        # !WINS! in 21 turns with 16 health left. Boss has -2 health remaining.
        # Player does 5 damage, boss does 4 damage.

    """ Weapons + 1 damage ring """

    def test_using_a_Dagger_and_Damage1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = None
        accessories1_name = 'Damage1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(33, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 67 health remaining.
        # Player does 3 damage, boss does 9 damage. Gold spent 33.

    def test_using_a_Dagger_and_Damage2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = None
        accessories1_name = 'Damage2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(58, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 55 health remaining.
        # Player does 4 damage, boss does 9 damage. Gold spent 58.

    def test_using_a_Dagger_and_Damage3Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = None
        accessories1_name = 'Damage3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(108, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 43 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 108.

    def test_using_a_Shortsword_and_Damage1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = None
        accessories1_name = 'Damage1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(35, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 55 health remaining.
        # Player does 4 damage, boss does 9 damage. Gold spent 35.

    def test_using_a_Shortsword_and_Damage2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = None
        accessories1_name = 'Damage2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(60, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 43 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 60.

    def test_using_a_Shortsword_and_Damage3Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = None
        accessories1_name = 'Damage3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(110, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 31 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 110.

    def test_using_a_Warhammer_and_Damage1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = None
        accessories1_name = 'Damage1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(50, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 43 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 50.

    def test_using_a_Warhammer_and_Damage2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = None
        accessories1_name = 'Damage2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(75, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 31 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 75.

    def test_using_a_Warhammer_and_Damage3Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = None
        accessories1_name = 'Damage3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(125, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 19 health remaining.
        # Player does 7 damage, boss does 9 damage. Gold spent 125.

    def test_using_a_Longsword_and_Damage1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = None
        accessories1_name = 'Damage1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(65, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 31 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 65.

    def test_using_a_Longsword_and_Damage2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = None
        accessories1_name = 'Damage2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(90, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 19 health remaining.
        # Player does 7 damage, boss does 9 damage. Gold spent 90.

    def test_using_a_Longsword_and_Damage3Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = None
        accessories1_name = 'Damage3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(140, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 7 health remaining.
        # Player does 8 damage, boss does 9 damage. Gold spent 140.

    def test_using_a_Greataxe_and_Damage1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = None
        accessories1_name = 'Damage1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(99, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 19 health remaining.
        # Player does 7 damage, boss does 9 damage. Gold spent 99.

    def test_using_a_Greataxe_and_Damage2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = None
        accessories1_name = 'Damage2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(124, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has 7 health remaining.
        # Player does 8 damage, boss does 9 damage. Gold spent 124.

    def test_using_a_Greataxe_and_Damage3Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = None
        accessories1_name = 'Damage3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(174, result)
        # DEAD! Player died in 12 turns with -8 health left. Boss has -5 health remaining.
        # Player does 9 damage, boss does 9 damage. Gold spent 174.

    """ Weapons + 1 defense ring """

    def test_using_a_Dagger_and_Defense1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = None
        accessories1_name = 'Defense1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(28, result)
        # DEAD! Player died in 13 turns with -4 health left. Boss has 77 health remaining.
        # Player does 2 damage, boss does 9 damage. Gold spent 28.

    def test_using_a_Dagger_and_Defense2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = None
        accessories1_name = 'Defense2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(48, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 73 health remaining.
        # Player does 2 damage, boss does 9 damage. Gold spent 48.

    def test_using_a_Dagger_and_Defense3Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = None
        accessories1_name = 'Defense3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(88, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 69 health remaining.
        # Player does 2 damage, boss does 9 damage. Gold spent 88.

    def test_using_a_Shortsword_and_Defense1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = None
        accessories1_name = 'Defense1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(30, result)
        # DEAD! Player died in 13 turns with -4 health left. Boss has 64 health remaining.
        # Player does 3 damage, boss does 9 damage. Gold spent 30.

    def test_using_a_Shortsword_and_Defense2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = None
        accessories1_name = 'Defense2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(50, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 58 health remaining.
        # Player does 3 damage, boss does 9 damage. Gold spent 50.

    def test_using_a_Shortsword_and_Defense3Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = None
        accessories1_name = 'Defense3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(90, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 52 health remaining.
        # Player does 3 damage, boss does 9 damage. Gold spent 90.

    def test_using_a_Warhammer_and_Defense1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = None
        accessories1_name = 'Defense1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(45, result)
        # DEAD! Player died in 13 turns with -4 health left. Boss has 51 health remaining.
        # Player does 4 damage, boss does 9 damage. Gold spent 45.

    def test_using_a_Warhammer_and_Defense2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = None
        accessories1_name = 'Defense2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(65, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 43 health remaining.
        # Player does 4 damage, boss does 9 damage. Gold spent 65.

    def test_using_a_Warhammer_and_Defense3Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = None
        accessories1_name = 'Defense3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(105, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 35 health remaining.
        # Player does 4 damage, boss does 9 damage. Gold spent 105.

    def test_using_a_Longsword_and_Defense1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = None
        accessories1_name = 'Defense1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(60, result)
        # DEAD! Player died in 13 turns with -4 health left. Boss has 38 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 60.

    def test_using_a_Longsword_and_Defense2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = None
        accessories1_name = 'Defense2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(80, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 28 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 80.

    def test_using_a_Longsword_and_Defense3Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = None
        accessories1_name = 'Defense3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(120, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 18 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 120.

    def test_using_a_Greataxe_and_Defense1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = None
        accessories1_name = 'Defense1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(94, result)
        # DEAD! Player died in 13 turns with -4 health left. Boss has 25 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 94.

    def test_using_a_Greataxe_and_Defense2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = None
        accessories1_name = 'Defense2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(114, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 13 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 114.

    def test_using_a_Greataxe_and_Defense3Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = None
        accessories1_name = 'Defense3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(154, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 1 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 154.

    """ Armor + 1 Damage rings """


    """ Armor + 1 Defense rings """


    """ Weapons + 2 Rings """


    """ Armor + 2 Rings """

    def test_using_LeatherArmor_and_one_of_each_1_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Leather'
        accessories1_name = 'Damage1'
        accessories2_name = 'Defense1'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(58, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 88 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 58.

    def test_using_ChainmailArmor_and_one_of_each_1_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Chainmail'
        accessories1_name = 'Damage1'
        accessories2_name = 'Defense1'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(76, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 86 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 76.

    def test_using_SplintmailArmor_and_one_of_each_1_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Splintmail'
        accessories1_name = 'Damage1'
        accessories2_name = 'Defense1'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(98, result)
        # DEAD! Player died in 20 turns with 0 health left. Boss has 83 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 98.

    def test_using_BandedmailArmor_and_one_of_each_1_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Bandedmail'
        accessories1_name = 'Damage1'
        accessories2_name = 'Defense1'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(120, result)
        # DEAD! Player died in 25 turns with 0 health left. Boss has 78 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 120.

    def test_using_PlatemailArmor_and_one_of_each_1_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Platemail'
        accessories1_name = 'Damage1'
        accessories2_name = 'Defense1'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(147, result)
        # DEAD! Player died in 34 turns with -2 health left. Boss has 69 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 147.

    def test_using_LeatherArmor_and_one_of_each_2_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Leather'
        accessories1_name = 'Damage2'
        accessories2_name = 'Defense2'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(103, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 86 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 103.

    def test_using_ChainmailArmor_and_one_of_each_2_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Chainmail'
        accessories1_name = 'Damage2'
        accessories2_name = 'Defense2'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(121, result)
        # DEAD! Player died in 20 turns with 0 health left. Boss has 83 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 121.

    def test_using_SplintmailArmor_and_one_of_each_2_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Splintmail'
        accessories1_name = 'Damage2'
        accessories2_name = 'Defense2'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(143, result)
        # DEAD! Player died in 25 turns with 0 health left. Boss has 78 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 143.

    def test_using_BandedmailArmor_and_one_of_each_2_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Bandedmail'
        accessories1_name = 'Damage2'
        accessories2_name = 'Defense2'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(165, result)
        # DEAD! Player died in 34 turns with -2 health left. Boss has 69 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 165.

    def test_using_PlatemailArmor_and_one_of_each_2_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Platemail'
        accessories1_name = 'Damage2'
        accessories2_name = 'Defense2'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(192, result)
        # DEAD! Player died in 50 turns with 0 health left. Boss has 53 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 192.

    def test_using_LeatherArmor_and_one_of_each_3_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Leather'
        accessories1_name = 'Damage3'
        accessories2_name = 'Defense3'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(193, result)
        # DEAD! Player died in 20 turns with 0 health left. Boss has 83 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 193.

    def test_using_ChainmailArmor_and_one_of_each_3_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Chainmail'
        accessories1_name = 'Damage3'
        accessories2_name = 'Defense3'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(211, result)
        # DEAD! Player died in 25 turns with 0 health left. Boss has 78 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 211.

    def test_using_SplintmailArmor_and_one_of_each_3_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Splintmail'
        accessories1_name = 'Damage3'
        accessories2_name = 'Defense3'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(233, result)
        # DEAD! Player died in 34 turns with -2 health left. Boss has 69 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 233.

    def test_using_BandedmailArmor_and_one_of_each_3_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Bandedmail'
        accessories1_name = 'Damage3'
        accessories2_name = 'Defense3'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(255, result)
        # DEAD! Player died in 50 turns with 0 health left. Boss has 53 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 255.

    def test_using_PlatemailArmor_and_one_of_each_3_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = None
        armor_name = 'Platemail'
        accessories1_name = 'Damage3'
        accessories2_name = 'Defense3'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(282, result)
        # DEAD! Player died in 100 turns with 0 health left. Boss has 3 health remaining.
        # Player does 1 damage, boss does 9 damage. Gold spent 282.

    """ Weapon + Armor + 1 Ring Combos """

    def test_using_a_Dagger_and_LeatherArmor_and_Damage1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = 'Leather'
        accessories1_name = 'Damage1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(46, result)
        # DEAD! Player died in 13 turns with -4 health left. Boss has 64 health remaining.
        # Player does 3 damage, boss does 9 damage. Gold spent 46.

    def test_using_a_Shortsword_and_ChainmailArmor_and_Damage1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = 'Chainmail'
        accessories1_name = 'Damage1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(66, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 43 health remaining.
        # Player does 4 damage, boss does 9 damage. Gold spent 66.

    def test_using_a_Warhammer_and_SplintmailArmor_and_Damage1Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = 'Splintmail'
        accessories1_name = 'Damage1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(103, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 18 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 103.

    def test_using_a_Longsword_and_BandedmailArmor_and_Damage1Ring_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = 'Bandedmail'
        accessories1_name = 'Damage1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(140, result)
        # !WINS! Player wins in 18 turns with 10 health left. Boss has -5 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 140.

    def test_using_a_Greataxe_and_PlatemailArmor_and_Damage1Ring_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = 'Platemail'
        accessories1_name = 'Damage1'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(201, result)
        # !WINS! Player wins in 15 turns with 40 health left. Boss has -2 health remaining.
        # Player does 7 damage, boss does 9 damage. Gold spent 201.

    def test_using_a_Dagger_and_LeatherArmor_and_Damage2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = 'Leather'
        accessories1_name = 'Damage2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(71, result)
        # DEAD! Player died in 13 turns with -4 health left. Boss has 51 health remaining.
        # Player does 4 damage, boss does 9 damage. Gold spent 71..

    def test_using_a_Shortsword_and_ChainmailArmor_and_Damage2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = 'Chainmail'
        accessories1_name = 'Damage2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(91, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 28 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 91.

    def test_using_a_Warhammer_and_SplintmailArmor_and_Damage2Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = 'Splintmail'
        accessories1_name = 'Damage2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(128, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 1 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 128.

    def test_using_a_Longsword_and_BandedmailArmor_and_Damage2Ring_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = 'Bandedmail'
        accessories1_name = 'Damage2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(165, result)
        # !WINS! Player wins in 15 turns with 25 health left. Boss has -2 health remaining.
        # Player does 7 damage, boss does 9 damage. Gold spent 165.

    def test_using_a_Greataxe_and_PlatemailArmor_and_Damage2Ring_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = 'Platemail'
        accessories1_name = 'Damage2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(226, result)
        # !WINS! Player wins in 13 turns with 48 health left. Boss has -1 health remaining.
        # Player does 8 damage, boss does 9 damage. Gold spent 226.

    def test_using_a_Dagger_and_LeatherArmor_and_Damage3Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = 'Leather'
        accessories1_name = 'Damage3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(121, result)
        # DEAD! Player died in 13 turns with -4 health left. Boss has 38 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 121.

    def test_using_a_Shortsword_and_ChainmailArmor_and_Damage3Ring_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = 'Chainmail'
        accessories1_name = 'Damage3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(141, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 13 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 141.

    def test_using_a_Warhammer_and_SplintmailArmor_and_Damage3Ring_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = 'Splintmail'
        accessories1_name = 'Damage3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(178, result)
        # !WINS! Player wins in 15 turns with 10 health left. Boss has -2 health remaining.
        # Player does 7 damage, boss does 9 damage. Gold spent 178.

    def test_using_a_Longsword_and_BandedmailArmor_and_Damage3Ring_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = 'Bandedmail'
        accessories1_name = 'Damage3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(215, result)
        # !WINS! Player wins in 13 turns with 35 health left. Boss has -1 health remaining.
        # Player does 8 damage, boss does 9 damage. Gold spent 215.

    def test_using_a_Greataxe_and_PlatemailArmor_and_Damage3Ring_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = 'Platemail'
        accessories1_name = 'Damage3'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(276, result)
        # !WINS! Player wins in 12 turns with 52 health left. Boss has -5 health remaining.
        # Player does 9 damage, boss does 9 damage. Gold spent 276.

    def test_using_a_Longsword_and_ChainmailArmor_and_Damage2Ring_PART1SOLUTION(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = 'Chainmail'
        accessories1_name = 'Damage2'
        accessories2_name = None
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(121, result)
        # !WINS! Player wins in 15 turns with -5 health left. Boss has -2 health remaining.
        # Player does 7 damage, boss does 9 damage. Gold spent 121.

    """ Weapon + Armor + 2 Rings Combos """

    def test_using_a_Dagger_and_LeatherArmor_and_one_of_each_1_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = 'Leather'
        accessories1_name = 'Damage1'
        accessories2_name = 'Defense1'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(66, result)
        # DEAD! Player died in 15 turns with -5 health left. Boss has 58 health remaining.
        # Player does 3 damage, boss does 9 damage. Gold spent 66.

    def test_using_a_Shortsword_and_ChainmailArmor_and_one_of_each_1_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = 'Chainmail'
        accessories1_name = 'Damage1'
        accessories2_name = 'Defense1'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(86, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 35 health remaining.
        # Player does 4 damage, boss does 9 damage. Gold spent 86.

    def test_using_a_Warhammer_and_SplintmailArmor_and_one_of_each_1_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = 'Splintmail'
        accessories1_name = 'Damage1'
        accessories2_name = 'Defense1'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(123, result)
        # DEAD! Player died in 20 turns with 0 health left. Boss has 3 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 123.

    def test_using_a_Longsword_and_BandedmailArmor_and_one_of_each_1_Rings_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = 'Bandedmail'
        accessories1_name = 'Damage1'
        accessories2_name = 'Defense1'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(160, result)
        # !WINS! Player wins in 18 turns with 28 health left. Boss has -5 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 160.

    def test_using_a_Greataxe_and_PlatemailArmor_and_one_of_each_1_Rings_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = 'Platemail'
        accessories1_name = 'Damage1'
        accessories2_name = 'Defense1'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(221, result)
        # !WINS! Player wins in 15 turns with 55 health left. Boss has -2 health remaining.
        # Player does 7 damage, boss does 9 damage. Gold spent 221.

    def test_using_a_Dagger_and_LeatherArmor_and_one_of_each_2_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = 'Leather'
        accessories1_name = 'Damage2'
        accessories2_name = 'Defense2'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(111, result)
        # DEAD! Player died in 17 turns with -2 health left. Boss has 35 health remaining.
        # Player does 4 damage, boss does 9 damage. Gold spent 111.

    def test_using_a_Shortsword_and_ChainmailArmor_and_one_of_each_2_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = 'Chainmail'
        accessories1_name = 'Damage2'
        accessories2_name = 'Defense2'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(131, result)
        # DEAD! Player died in 20 turns with 0 health left. Boss has 3 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 131.

    def test_using_a_Warhammer_and_SplintmailArmor_and_one_of_each_2_Rings_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = 'Splintmail'
        accessories1_name = 'Damage2'
        accessories2_name = 'Defense2'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(168, result)
        # !WINS! Player wins in 18 turns with 28 health left. Boss has -5 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 168.

    def test_using_a_Longsword_and_BandedmailArmor_and_one_of_each_2_Rings_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = 'Bandedmail'
        accessories1_name = 'Damage2'
        accessories2_name = 'Defense2'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(205, result)
        # !WINS! Player wins in 15 turns with 55 health left. Boss has -2 health remaining.
        # Player does 7 damage, boss does 9 damage. Gold spent 205.

    def test_using_a_Greataxe_and_PlatemailArmor_and_one_of_each_2_Rings_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = 'Platemail'
        accessories1_name = 'Damage2'
        accessories2_name = 'Defense2'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(266, result)
        # !WINS! Player wins in 13 turns with 74 health left. Boss has -1 health remaining.
        # Player does 8 damage, boss does 9 damage. Gold spent 266.

    def test_using_a_Dagger_and_LeatherArmor_and_one_of_each_3_Rings_DEAD(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Dagger'
        armor_name = 'Leather'
        accessories1_name = 'Damage3'
        accessories2_name = 'Defense3'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(201, result)
        # DEAD! Player died in 20 turns with 0 health left. Boss has 3 health remaining.
        # Player does 5 damage, boss does 9 damage. Gold spent 201.

    def test_using_a_Shortsword_and_ChainmailArmor_and_one_of_each_3_Rings_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Shortsword'
        armor_name = 'Chainmail'
        accessories1_name = 'Damage3'
        accessories2_name = 'Defense3'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(221, result)
        # !WINS! Player wins in 18 turns with 28 health left. Boss has -5 health remaining.
        # Player does 6 damage, boss does 9 damage. Gold spent 221.

    def test_using_a_Warhammer_and_SplintmailArmor_and_one_of_each_3_Rings_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Warhammer'
        armor_name = 'Splintmail'
        accessories1_name = 'Damage3'
        accessories2_name = 'Defense3'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(258, result)
        # !WINS! Player wins in 15 turns with 55 health left. Boss has -2 health remaining.
        # Player does 7 damage, boss does 9 damage. Gold spent 258.

    def test_using_a_Longsword_and_BandedmailArmor_and_one_of_each_3_Rings_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Longsword'
        armor_name = 'Bandedmail'
        accessories1_name = 'Damage3'
        accessories2_name = 'Defense3'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(295, result)
        # !WINS! Player wins in 13 turns with 74 health left. Boss has -1 health remaining.
        # Player does 8 damage, boss does 9 damage. Gold spent 295.

    def test_using_a_Greataxe_and_PlatemailArmor_and_one_of_each_3_Rings_WIN(self):
        boss_health = 103
        boss_damage = 9
        boss_armor = 2
        weapon_name = 'Greataxe'
        armor_name = 'Platemail'
        accessories1_name = 'Damage3'
        accessories2_name = 'Defense3'
        result = my_rpg_game(boss_health, boss_damage, boss_armor, weapon_name,
                             armor_name, accessories1_name, accessories2_name)
        self.assertEqual(356, result)
        # !WINS! Player wins in 12 turns with 88 health left. Boss has -5 health remaining.
        # Player does 9 damage, boss does 9 damage. Gold spent 356.