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


# Note:
# Perhaps do something like the santa/robo santa and check each possible combination
# of equipment that way by adding it to the list and then checking if it's
# there already or not


def my_rpg_game(b_health, b_attack, b_defence, weapon, armor,
                accessories1, accessories2):

    if weapon == None:
        has_weapon = False
    else:
        has_weapon = True

    if armor == None:
        has_armor = False
    else:
        has_armor = True

    if accessories1 == None:
        has_accessory_one = False
    else:
        has_accessory_one = True

    if accessories2 == None:
        has_accessory_two = False
    else:
        has_accessory_two = True


    player_health = 100
    player_damage = 0
    player_defense = 0
    player_gold_spent = 0
    num_of_turns_taken = 0
    boss_health = b_health
    boss_damage = b_attack
    boss_defense = b_defence

    # Update player stats based on equipment purchased
    if has_weapon:
        weapon_cost, weapon_damage, weapon_defence = buy_item_from_store(weapon)
        # Update gold spent
        player_gold_spent += weapon_cost
        # Update player stats with the new weapon:
        player_damage += weapon_damage
        player_defense += weapon_defence
        # print "weapon_cost is: %d " % weapon_cost
        # print "weapon_damage is: %d " % weapon_damage
        # print "weapon_defence is: %d " % weapon_defence

    if has_armor:
        armor_cost, armor_damage, armor_defence = buy_item_from_store(armor)
        # Update gold spent
        player_gold_spent += armor_cost
        # Update player stats with the new weapon:
        player_damage += armor_damage
        player_defense += armor_defence
        # print "armor_cost is: %d " % armor_cost
        # print "armor_damage is: %d " % armor_damage
        # print "armor_defence is: %d " % armor_defence

    if has_accessory_one:
        accessories1_cost, accessories1_damage, accessories1_defence = buy_item_from_store(accessories1)
        # Update gold spent
        player_gold_spent += accessories1_cost
        # Update player stats with the new weapon:
        player_damage += accessories1_damage
        player_defense += accessories1_defence
        # print "accessories1_cost is: %d " % accessories1_cost
        # print "accessories1_damage is: %d " % accessories1_damage
        # print "accessories1_defence is: %d " % accessories1_defence

    if has_accessory_two:
        accessories2_cost, accessories2_damage, accessories2_defence = buy_item_from_store(accessories2)
        # Update gold spent
        player_gold_spent += accessories2_cost
        # Update player stats with the new weapon:
        player_damage += accessories2_damage
        player_defense += accessories2_defence
        # print "accessories2_cost is: %d " % accessories2_cost
        # print "accessories2_damage is: %d " % accessories2_damage
        # print "accessories2_defence is: %d " % accessories2_defence

    # Track how much gold has been spent
    # print "player_gold_spent is: %d" % player_gold_spent

    # Print the players stats after purchasing equipment
    # print "player_damage is: %d " % player_damage
    # print "player_defense is: %d " % player_defense
    # Print the bosses stats
    # print "boss_damage is: %d " % boss_damage
    # print "boss_defense is: %d " % boss_defense

    # Calculate the damage dealt for the turn = attacker's damage score minus the defender's armor score
    player_damage_dealt = player_damage - boss_defense
    # print "player_damage_dealt is: %d " % player_damage_dealt

    # An attacker always does at least 1 damage.
    if player_damage_dealt <= 1:
        player_damage_dealt = 1

    # Calculate the boss' damage
    boss_damage_dealt = boss_damage - player_defense
    # print "boss_damage_dealt is: %d " % boss_damage_dealt

    while boss_health > 0:
        # Increment the turn counter to know how many turns have gone by
        num_of_turns_taken += 1
        # print "Turn #: %d" % num_of_turns_taken

        # Hit the Boss
        boss_health = boss_health - player_damage_dealt
        # print "Player dealt %d damage. " \
        #       "Boss Health is at %d" % (player_damage_dealt, boss_health)

        # The Boss's turn - Player hits the boss
        player_health = player_health - boss_damage_dealt
        # print "Boss dealt %d damage. " \
        #       "Player Health is at %d" % (boss_damage_dealt, player_health)

        # If the Player's health goes to 0 or less before the Boss' health
        # hits 0 health, the Boss wins!
        if player_health <= 0 and boss_health > 0:
            print "=== You have died! Please try again. ==="
            # print
            # print "Player stats were as follows: "
            # print "Player Health: %d " % player_health
            # print "Player Damage: %d " % player_damage
            # print "Player Damage Dealt: %d " % player_damage_dealt
            # print "Player Defense: %d " % player_defense
            # print "Player Gold Spent: %d " % player_gold_spent
            # print
            # print "The Bosses Stats were as follows: "
            # print "Boss Health: %d " % boss_health
            # print "Boss Damage: %d " % boss_damage
            # print "Boss Defense: %d " % boss_defense
            # print
            # print "Number of Turns taken: %d " % num_of_turns_taken
            # print
            print "DEAD! Player died in %d turns with %d health left. Boss has %d health " \
                  "remaining. Player does %d damage, boss does %d damage. " \
                  "Gold spent %d. " % \
                  (num_of_turns_taken, player_health, boss_health,
                   player_damage_dealt, boss_damage, player_gold_spent)
            print
            return player_gold_spent

        # If the player and boss die on the same turn, the player is considered the
        # winner since the player attacks first
        elif player_health < 0 and boss_health < 0:
            print "=== You have won! Woot! ==="
            print "!WINS! Player wins in %d turns with %d health left. Boss has %d health " \
                  "remaining. Player does %d damage, boss does %d damage. " \
                  "Gold spent %d. " % \
                  (num_of_turns_taken, player_health, boss_health,
                   player_damage_dealt, boss_damage, player_gold_spent)
            print
            return player_gold_spent

        # If the Boss's health goes to 0 or less before the Player's health
        # hits 0 health, the Player wins!
        elif player_health > 0 and boss_health <= 0:
            print "=== You have won! Woot! ==="
            # print
            # print "Player stats were as follows: "
            # print "Player Health: %d " % player_health
            # print "Player Damage: %d " % player_damage
            # print "Player Damage Dealt: %d " % player_damage_dealt
            # print "Player Defense: %d " % player_defense
            # print "Player Gold Spent: %d " % player_gold_spent
            # print
            # print "The Bosses Stats were as follows: "
            # print "Boss Health: %d " % boss_health
            # print "Boss Damage: %d " % boss_damage
            # print "Boss Defense: %d " % boss_defense
            # print
            # print "Number of Turns taken: %d " % num_of_turns_taken
            # print
            # print "Weapon used: %s. Armor used: %s. Accessory 1 used: %s. Accessory 2 used: %s." %
            print "!WINS! Player wins in %d turns with %d health left. Boss has %d health " \
                  "remaining. Player does %d damage, boss does %d damage. " \
                  "Gold spent %d. " % \
                  (num_of_turns_taken, player_health, boss_health,
                   player_damage_dealt, boss_damage, player_gold_spent)
            print
            return player_gold_spent


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
        greataxe_cost = 74
        greataxe_attack = 8
        greataxe_armor = 0
        return greataxe_cost, greataxe_attack, greataxe_armor

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

    elif item_name == 'Defense1':
        defense1_cost = 20
        defense1_attack = 0
        defense1_armor = 1
        return defense1_cost, defense1_attack, defense1_armor

    elif item_name == 'Defense2':
        defense2_cost = 40
        defense2_armor_attack = 0
        defense2_armor = 2
        return defense2_cost, defense2_armor_attack, defense2_armor

    elif item_name == 'Defense3':
        defense3_cost = 80
        defense3_attack = 0
        defense3_armor = 3
        return defense3_cost, defense3_attack, defense3_armor

