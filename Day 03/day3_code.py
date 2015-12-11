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

    #TODO Use tuple to move through houses
    current_position = (0,0)  # Used to track whether we've been to a house already or not
    unique_houses_visited = 1  # starts at 1 since he gives a present to his starting location
    total_gifts_given = 1  # starts at 1 since he gives a present to his starting location
    visited_house_before = False

    for direction in instructions:

        if direction == '^':
            current_position += 1
            print "Current current_position (^) is: " + str(current_position)

            if current_position == 0:  # aka back to a house we've been to?
                visited_house_before = True

            if not visited_house_before:
                unique_houses_visited += 1
                total_gifts_given += 1
            else:
                total_gifts_given += 1

        elif direction == 'v':
            current_position -= 1
            print "Current current_position (v) is: " + str(current_position)

            if current_position == 0:  # aka back to a house we've been to?
                visited_house_before = True

            if not visited_house_before:
                unique_houses_visited += 1
                total_gifts_given += 1
            else:
                total_gifts_given += 1

        elif direction == '>':
            current_position += 1
            print "Current current_position (>) is: " + str(current_position)

            if current_position == 0:  # aka back to a house we've been to?
                visited_house_before = True

            if not visited_house_before:
                unique_houses_visited += 1
                total_gifts_given += 1
            else:
                total_gifts_given += 1

        elif direction == '<':
            current_position -= 1
            print "Current current_position (<) is: " + str(current_position)

            if current_position == 0:  # aka back to a house we've been to?
                visited_house_before = True

            if not visited_house_before:
                unique_houses_visited += 1
                total_gifts_given += 1
            else:
                total_gifts_given += 1

    print "unique_houses_visited is: " + str(unique_houses_visited)
    print "total_gifts_given is: " + str(total_gifts_given)
    return unique_houses_visited
