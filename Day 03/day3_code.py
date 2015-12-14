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
    # print "Current instructions are: " + str(instructions)  # Print current instructions passed in

    current_house_coordinates = (0, 0)  # Used to track whether we've been to a house already or not, starting at 0,0

    x_position = 0
    y_position = 0

    all_places_visited = [(0, 0)]

    unique_houses_visited = 1  # starts at 1 since he gives a present to his starting location
    total_houses_visited = 1  # starts at 1 since he gives a present to his starting location

    for direction in instructions:

        if direction == '^':
            x_position += 1
            current_house_coordinates = (x_position, y_position)
            # print "current_house_coordinates: " + str(current_house_coordinates)

        elif direction == 'v':
            x_position -= 1
            current_house_coordinates = (x_position, y_position)
            # print "current_house_coordinates: " + str(current_house_coordinates)

        elif direction == '>':
            y_position += 1
            current_house_coordinates = (x_position, y_position)
            # print "current_house_coordinates: " + str(current_house_coordinates)

        elif direction == '<':
            y_position -= 1
            current_house_coordinates = (x_position, y_position)
            # print "current_house_coordinates: " + str(current_house_coordinates)

        # Need to check whether the house coord is already in the full list of houses
        # if not, add 1 to unique houses as well as 1 to total gifts
        if current_house_coordinates not in all_places_visited:
            unique_houses_visited += 1
            total_houses_visited += 1
            all_places_visited.append(current_house_coordinates)
            # print "all_places_visited: " + str(all_places_visited)
        # else add to total houses list only
        else:
            total_houses_visited += 1
            all_places_visited.append(current_house_coordinates)
            # print "all_places_visited: " + str(all_places_visited)

    print "unique_houses_visited is: " + str(unique_houses_visited)
    print "total_houses_visited is: " + str(total_houses_visited)
    print
    return unique_houses_visited


def calculate_unique_num_houses_santa_and_robo_visited(instructions):
    """
    Santa and Robo-Santa start at the same location (delivering two presents to the
    same starting house), then take turns moving based on instructions from the elf,
    who is eggnoggedly reading from the same script as the previous year.

    This year, how many houses receive at least one present?
    """

    # Split out the instructions for each person
    santa_instructions = instructions[::2]
    robo_instructions = instructions[1::2]
    # print "santa_instructions: " + str(santa_instructions)
    # print "robo_instructions: " + str(robo_instructions)

    santa_current_house_coordinates = (0, 0)  # Used to track whether we've been to a house already or not, starting at 0,0
    robo_current_house_coordinates = (0, 0)  # Used to track whether we've been to a house already or not, starting at 0,0

    santa_x_position = 0
    santa_y_position = 0

    robo_x_position = 0
    robo_y_position = 0

    all_places_visited = [(0, 0)]

    unique_houses_visited = 1  # starts at 1 since they both give a gift to their starting position
    total_houses_visited = 1  # starts at 1 since both gives a present to their starting position

    # TODO: Pass split up instructions into the first method written above (Should be able to replace the below code)

    for direction in santa_instructions:

        if direction == '^':
            santa_x_position += 1
            santa_current_house_coordinates = (santa_x_position, santa_y_position)
            # print "santa_current_house_coordinates: " + str(santa_current_house_coordinates)

        elif direction == 'v':
            santa_x_position -= 1
            santa_current_house_coordinates = (santa_x_position, santa_y_position)
            # print "santa_current_house_coordinates: " + str(santa_current_house_coordinates)

        elif direction == '>':
            santa_y_position += 1
            santa_current_house_coordinates = (santa_x_position, santa_y_position)
            # print "santa_current_house_coordinates: " + str(santa_current_house_coordinates)

        elif direction == '<':
            santa_y_position -= 1
            santa_current_house_coordinates = (santa_x_position, santa_y_position)
            # print "santa_current_house_coordinates: " + str(santa_current_house_coordinates)

        # Need to check whether the house coord is already in the full list of houses
        # if not, add 1 to unique houses as well as 1 to total gifts
        if santa_current_house_coordinates not in all_places_visited:
            unique_houses_visited += 1
            total_houses_visited += 1
            all_places_visited.append(santa_current_house_coordinates)
        # else add to total houses list only
        else:
            total_houses_visited += 1
            all_places_visited.append(santa_current_house_coordinates)

    for direction in robo_instructions:

        if direction == '^':
            robo_x_position += 1
            robo_current_house_coordinates = (robo_x_position, robo_y_position)
            # print "robo_current_house_coordinates: " + str(robo_current_house_coordinates)

        elif direction == 'v':
            robo_x_position -= 1
            robo_current_house_coordinates = (robo_x_position, robo_y_position)
            # print "robo_current_house_coordinates: " + str(robo_current_house_coordinates)

        elif direction == '>':
            robo_y_position += 1
            robo_current_house_coordinates = (robo_x_position, robo_y_position)
            # print "robo_current_house_coordinates: " + str(robo_current_house_coordinates)

        elif direction == '<':
            robo_y_position -= 1
            robo_current_house_coordinates = (robo_x_position, robo_y_position)
            # print "robo_current_house_coordinates: " + str(robo_current_house_coordinates)

        # Need to check whether the house coord is already in the full list of houses
        # if not, add 1 to unique houses as well as 1 to total gifts
        if robo_current_house_coordinates not in all_places_visited:
            unique_houses_visited += 1
            total_houses_visited += 1
            all_places_visited.append(robo_current_house_coordinates)
            # print "all_places_visited: " + str(all_places_visited)
        # else add to total houses list only
        else:
            total_houses_visited += 1
            all_places_visited.append(robo_current_house_coordinates)
            # print "all_places_visited: " + str(all_places_visited)

    print "unique_houses_visited is: " + str(unique_houses_visited)
    print "total_houses_visited is: " + str(total_houses_visited)
    print

    return unique_houses_visited
