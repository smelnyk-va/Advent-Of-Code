__author__ = 'smelnyk'


def get_target_floor(instructions):
    """
    Given a set of brackets, navigate an imaginary apartment building is that is very tall,
    and the basement is very deep.  The instructions given are in a form of open and closed brackets
    where '(' goes up a floor and ')' goes down a floor.
    E.g. '((()' should equal floor 2

    Return the floor trying to be reached based on instructions given.

    My not so clean attempt to solve: http://adventofcode.com/day/1
    """
    current_floor = 0
    floor_instructions = []

    # print "instructions is " + instructions

    for string_bracket in instructions:
        floor_instructions.append(string_bracket)
        # print "floor_instructions is " + str(floor_instructions)

    # print "floor_instructions is " + str(floor_instructions)

    for list_bracket in floor_instructions:

        if list_bracket == '(':
            current_floor += 1

        elif list_bracket == ')':
            current_floor -= 1

    # print "current_floor is " + str(current_floor)

    return current_floor

def find_when_basement_reached(instructions):
    """
    Given a set of instructions in the form of open and closed brackets,
    where '(' goes up a floor and ')' goes down a floor, find the position of the first character that causes him
    to enter the basement (floor -1).

    The first character in the instructions has position 1, the second character has position 2, and so on
    """

    move_number = 0
    current_floor = 0
    floor_instructions = []

    print "instructions are: " + str(instructions)

    len_of_instructions = len(instructions)
    # print "len_of_instructions is: " + str(len_of_instructions)

    for string_bracket in instructions:
        floor_instructions.append(string_bracket)

        # print "current string_bracket is: " + str(string_bracket)
        # print "floor_instructions currently is: " + str(floor_instructions)

        if string_bracket == '(':
            move_number += 1
            current_floor += 1

            if current_floor == -1:
                # print "current_floor is: " + str(current_floor)
                # print "Number of moves taken to reach basement: " + str(move_number)
                return move_number

        elif string_bracket == ')':
            move_number += 1
            current_floor -= 1

            if current_floor == -1:
                # print "current_floor is: " + str(current_floor)
                # print "Number of moves taken to reach basement: " + str(move_number)
                return move_number


    # print "floor_instructions filled is: " + str(floor_instructions)
    print "Total number of moves taken: " + str(move_number)
    print "current_floor landed on is: " + str(current_floor)
    print
    # return current_floor