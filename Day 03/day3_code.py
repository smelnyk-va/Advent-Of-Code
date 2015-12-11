__author__ = 'smelnyk'


def calculate_num_houses_receiving_presents(instructions):
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

    print "Current instructions are: " + str(instructions)

    # Maybe do something like the following
    # starting_position = 0
    # make a variable for each direction
    # increment or decrement based on directions going?
    # (west and south = -1, east and north = +1)
    # then have a check to make sure we didn't make it back to zero?

    unique_gifts_given = 1
    total_gifts_given = 1  # starts at 1 since he gives a present to his starting location
    visited_house_before = False

    for direction in instructions:

        if direction == '<':
            if not visited_house_before:
                unique_gifts_given += 1
                total_gifts_given += 1
                visited_house_before = True
            else:
                total_gifts_given += 1

        elif direction == '>':
            if not visited_house_before:
                unique_gifts_given += 1
                total_gifts_given += 1
                visited_house_before = True
            else:
                total_gifts_given += 1

        elif direction == '^':
            if not visited_house_before:
                unique_gifts_given += 1
                total_gifts_given += 1
                visited_house_before = True
            else:
                total_gifts_given += 1

        elif direction == 'v':
            if not visited_house_before:
                unique_gifts_given += 1
                total_gifts_given += 1
                visited_house_before = True
            else:
                total_gifts_given += 1

    return total_gifts_given
