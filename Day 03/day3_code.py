__author__ = 'smelnyk'

from itertools import chain


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
    x_position = 0
    y_position = 0

    all_places_visited = [(0,0)]

    unique_houses_visited = 1  # starts at 1 since he gives a present to his starting location
    total_houses_visited = 1  # starts at 1 since he gives a present to his starting location
    visited_house_before = False


    for direction in instructions:

        if direction == '^':
            x_position += 1
            print "Current x_position (^) is: " + str(x_position)

            current_house_coordinates = (x_position, y_position)
            print "current_house_coordinates: " + str(current_house_coordinates)

            all_places_visited.append(current_house_coordinates)
            print "all_places_visited: " + str(all_places_visited)

            # Need to check whether the house coord is already in the full list
            # if not, add to unique houses as well as total gifts

            # if any(current_house_coordinates in all_places_visited for position in current_position):
            # if current_house_coordinates not in chain.from_iterable(all_places_visited):
            if current_house_coordinates not in all_places_visited:
                # print "current_house_coordinates (any): " + str(current_house_coordinates)
                unique_houses_visited += 1
                total_houses_visited += 1
            # else add to total houses list only
            else:
                total_houses_visited += 1


            # if current_position == 0:  # aka back to a house we've been to?
            #     visited_house_before = True
            #
            # if not visited_house_before:
            #     unique_houses_visited += 1
            #     total_houses_visited += 1
            # else:
            #     total_houses_visited += 1

        elif direction == 'v':
            x_position -= 1
            print "Current x_position (v) is: " + str(x_position)

            current_house_coordinates = (x_position, y_position)
            print "current_house_coordinates: " + str(current_house_coordinates)

            all_places_visited.append(current_house_coordinates)
            print "all_places_visited: " + str(all_places_visited)

            # Need to check whether the house coord is already in the full list
            # if not, add to unique houses as well as total gifts

            # if any(current_house_coordinates in all_places_visited for position in current_position):
            # if current_house_coordinates not in chain.from_iterable(all_places_visited):
            if current_house_coordinates not in all_places_visited:
                # print "current_house_coordinates (any): " + str(current_house_coordinates)
                unique_houses_visited += 1
                total_houses_visited += 1
            # else add to total houses list only
            else:
                total_houses_visited += 1


            # if current_position == 0:  # aka back to a house we've been to?
            #     visited_house_before = True
            #
            # if not visited_house_before:
            #     unique_houses_visited += 1
            #     total_houses_visited += 1
            # else:
            #     total_houses_visited += 1

        elif direction == '>':
            y_position += 1
            print "Current y_position (>) is: " + str(y_position)

            current_house_coordinates = (x_position, y_position)
            print "current_house_coordinates: " + str(current_house_coordinates)

            all_places_visited.append(current_house_coordinates)
            print "all_places_visited: " + str(all_places_visited)

            # Need to check whether the house coord is already in the full list
            # if not, add to unique houses as well as total gifts

            # if any(current_house_coordinates in all_places_visited for position in current_position):
            # if current_house_coordinates not in chain.from_iterable(all_places_visited):
            if current_house_coordinates not in all_places_visited:
                # print "current_house_coordinates (any): " + str(current_house_coordinates)
                unique_houses_visited += 1
                total_houses_visited += 1
            # else add to total houses list only
            else:
                total_houses_visited += 1

            # if current_position == 0:  # aka back to a house we've been to?
            #     visited_house_before = True
            #
            # if not visited_house_before:
            #     unique_houses_visited += 1
            #     total_houses_visited += 1
            # else:
            #     total_houses_visited += 1

        elif direction == '<':
            y_position -= 1
            print "Current y_position (<) is: " + str(y_position)

            current_house_coordinates = (x_position, y_position)
            print "current_house_coordinates: " + str(current_house_coordinates)

            all_places_visited.append(current_house_coordinates)
            print "all_places_visited: " + str(all_places_visited)

            # Need to check whether the house coord is already in the full list
            # if not, add to unique houses as well as total gifts

            # if any(current_house_coordinates in all_places_visited for position in current_position):
            # if current_house_coordinates not in chain.from_iterable(all_places_visited):
            if current_house_coordinates not in all_places_visited:
                # print "current_house_coordinates (any): " + str(current_house_coordinates)
                unique_houses_visited += 1
                total_houses_visited += 1
            # else add to total houses list only
            else:
                total_houses_visited += 1


            # if current_position == 0:  # aka back to a house we've been to?
            #     visited_house_before = True
            #
            # if not visited_house_before:
            #     unique_houses_visited += 1
            #     total_houses_visited += 1
            # else:
            #     total_houses_visited += 1

        #for place_visited in current_position:
        #     all_places_visited.append(place_visited)
        #
        # print "all_places_visited is: " + str(all_places_visited)

    print "unique_houses_visited is: " + str(unique_houses_visited)
    print "total_houses_visited is: " + str(total_houses_visited)
    return unique_houses_visited
