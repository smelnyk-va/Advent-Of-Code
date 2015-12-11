__author__ = 'smelnyk'


def calculate_num_houses_receiving_presents(directions):
    """
    Santa is delivering presents to an infinite two-dimensional grid of
    houses. Starting location - north pole.

    Moves are always exactly one house to the:
    north (^), south (v), east (>), or west (<).

    After each move, he delivers another present to the house at
    his new location.

    However, the elf back at the north pole has had a little too much
    eggnog, and so his directions are a little off, and Santa ends up
    visiting some houses more than once.

    How many houses receive at least one present?
    """

    print "Current directions are: " + str(directions)

    num_moves_west = 0
    num_moves_east = 0
    num_moves_south = 0
    num_moves_north = 0
    total_moves = 0
    gifts_given = 1 # starts at 1 since he gives a present to his starting location

    if directions == '<':
        num_moves_west = 1
        total_moves = 1


    elif directions == '>':
        num_moves_east = 1
        total_moves = 1

    elif directions == '^':
        num_moves_north = 1
        total_moves = 1

    elif directions == 'v':
        num_moves_south = 1
        total_moves = 1

    return total_moves
