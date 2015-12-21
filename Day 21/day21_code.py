__author__ = 'smelnyk'
"""
In this game, the player (you) and the enemy (the boss) take turns attacking.
The player always goes first.
Each attack reduces the opponent's hit points by at least 1.
The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage
score minus the defender's armor score.
An attacker always does at least 1 damage.
So, if the attacker has a damage score of 8, and the defender has an
armor score of 3, the defender loses 5 hit points.

If the defender had an armor score of 300, the defender would still
lose 1 hit point.

Your damage score and armor score both start at zero.
They can be increased by buying items in exchange for gold.
You start with no items and have as much gold as you need.
Your total damage or armor is equal to the sum of those stats
from all of your items. You have 100 hit points.

For example:
Suppose you have 8 hit points, 5 damage, and 5 armor,
and that the boss has 12 hit points, 7 damage, and 2 armor:

The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.

In this scenario, the player wins! (Barely.)

You have 100 hit points. The boss's actual stats are in your puzzle input.
What is the least amount of gold you can spend and still win the fight?

"""

def my_rpg_game(b_health, b_attack, b_defence):

    player_health = 100
    player_damage = 0
    player_defence = 0
    player_gold = 1000
    player_gold_spent = 0

    num_of_turns_taken = 0

    boss_health = b_health
    boss_damage = b_attack
    boss_defence = b_defence
    boss_damage_dealt = 0

    while boss_health > 0:
        # Increment the turn counter to know how many turns have gone by
        num_of_turns_taken += 1

        #decide on some weapons, armor, accessories to buy
        weapon_cost, weapon_damage, weapon_armor = buy_item_from_store('Dagger')

        # Check whether the player can afford the weapon or not
        if player_gold - weapon_cost >= 0:
            player_gold = player_gold - weapon_cost

            #Update player stats with the new weapon:
            player_damage = player_damage + weapon_damage
            player_defence = player_defence + weapon_armor
        else:
            print "Could not afford the weapon. Please earn more gold or sell some items."

        # Calculate the damage dealt for the turn = attacker's damage score minus the defender's armor score
        player_damage_dealt = player_damage - boss_defence

        # An attacker always does at least 1 damage.
        if player_damage_dealt < 1:
            player_damage_dealt = 1

        # Now that damage is calculate, hit the boss
        boss_health = boss_health - player_damage_dealt

        # Calculate the boss' damage
        boss_damage_dealt = boss_damage - player_defence

        # hit the player back
        player_health = player_health - boss_damage_dealt

        if player_health <= 0 and boss_health > 0:
            print "You have died! Please try again. Your stats were as follows: "
            print "Player Health: %d " % player_health
            print "Player Damage: %d " % player_damage
            print "Player Defence: %d " % player_defence
            print "Player Gold: %d " % player_gold
            print "You have died! Please try again. The Bosses Stats were as follows: "
            print "Boss Health: %d " % boss_health
            print "Boss Damage: %d " % boss_damage
            print "Boss Defence: %d " % boss_defence
            return player_health

        elif player_health > 0 and boss_health <= 0:
            print "You have won! Woot! Your stats were as follows: "
            print "Player Health: %d " % player_health
            print "Player Damage: %d " % player_damage
            print "Player Defence: %d " % player_defence
            print "Player Gold: %d " % player_gold
            print "You have won! Woot! The Bosses Stats were as follows: "
            print "Boss Health: %d " % boss_health
            print "Boss Damage: %d " % boss_damage
            print "Boss Defence: %d " % boss_defence
            return player_health


# Here is what the item shop is selling:
def buy_item_from_store(item_name):

    # Weapons:    Cost  Damage  Armor
    # Dagger        8     4       0
    # Shortsword   10     5       0
    # Warhammer    25     6       0
    # Longsword    40     7       0
    # Greataxe     74     8       0

    if item_name == 'Dagger':
        dagger_cost = 8
        dagger_attack = 4
        dagger_armor = 0
        return dagger_cost, dagger_attack, dagger_armor

    elif item_name == 'Shortsword':
        shortsword_cost = 10
        shortsword_attack = 5
        shortsword_armor = 0
        return shortsword_cost, shortsword_attack, shortsword_armor

    elif item_name == 'Warhammer':
        warhammer_cost = 25
        warhammer_attack = 6
        warhammer_armor = 0
        return warhammer_cost, warhammer_attack, warhammer_armor

    elif item_name == 'Longsword':
        longsword_cost = 40
        longsword_attack = 7
        longsword_armor = 0
        return longsword_cost, longsword_attack, longsword_armor

    elif item_name == 'Greataxe':
        longsword_cost = 74
        longsword_attack = 8
        longsword_armor = 0
        return longsword_cost, longsword_attack, longsword_armor

    # Armor:      Cost  Damage  Armor
    # Leather      13     0       1
    # Chainmail    31     0       2
    # Splintmail   53     0       3
    # Bandedmail   75     0       4
    # Platemail   102     0       5

    elif item_name == 'Leather':
        leather_armor_cost = 13
        leather_armor_attack = 0
        leather_armor_armor = 1
        return leather_armor_cost, leather_armor_attack, leather_armor_armor

    elif item_name == 'Chainmail':
        chainmail_armor_cost = 31
        chainmail_armor_attack = 0
        chainmail_armor_armor = 2
        return chainmail_armor_cost, chainmail_armor_attack, chainmail_armor_armor

    elif item_name == 'Splintmail':
        splintmail_armor_cost = 53
        splintmail_armor_attack = 0
        splintmail_armor_armor = 3
        return splintmail_armor_cost, splintmail_armor_attack, splintmail_armor_armor

    elif item_name == 'Bandedmail':
        bandedmail_armor_cost = 75
        bandedmail_armor_attack = 0
        bandedmail_armor_armor = 4
        return bandedmail_armor_cost, bandedmail_armor_attack, bandedmail_armor_armor

    elif item_name == 'Platemail':
        platemail_armor_cost = 102
        platemail_armor_attack = 0
        platemail_armor_armor = 5
        return platemail_armor_cost, platemail_armor_attack, platemail_armor_armor

    # Rings:      Cost  Damage  Armor
    # Damage +1    25     1       0
    # Damage +2    50     2       0
    # Damage +3   100     3       0
    # Defense +1   20     0       1
    # Defense +2   40     0       2
    # Defense +3   80     0       3

    elif item_name == 'Damage1':
        damage1_cost = 25
        damage1_armor_attack = 1
        damage1_armor_armor = 0
        return damage1_cost, damage1_armor_attack, damage1_armor_armor

    elif item_name == 'Damage2':
        damage2_cost = 50
        damage2_attack = 2
        damage2_armor = 0
        return damage2_cost, damage2_attack, damage2_armor

    elif item_name == 'Damage3':
        damage3_cost = 100
        damage3_attack = 3
        damage3_armor = 0
        return damage3_cost, damage3_attack, damage3_armor

    elif item_name == 'Defence1':
        defence1_cost = 20
        defence1_attack = 0
        defence1_armor = 1
        return defence1_cost, defence1_attack, defence1_armor

    elif item_name == 'Defence2':
        defence2_cost = 40
        defence2_armor_attack = 0
        defence2_armor = 2
        return defence2_cost, defence2_armor_attack, defence2_armor

    elif item_name == 'Defence3':
        defence3_cost = 80
        defence3_attack = 0
        defence3_armor = 3
        return defence3_cost, defence3_attack, defence3_armor

