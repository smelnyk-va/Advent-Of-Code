""" Day 1 Advent of Code 2016 - Python Solution Attempt """

FACTORS = (
    (0, 1),  # turning right, N
    (1, 0),  # E
    (0, -1),  # S
    (-1, 0)  # W
)

DIRF = {
    'R': lambda x: (x + 1) % 4,
    'L': lambda x: (x - 1) % 4
}


class DirectionCalculator():

    directions_given = ['R4', 'R5', 'L5', 'L5', 'L3', 'R2', 'R1', 'R1', 'L5', 'R5', 'R2', 'L1', 'L3', 'L4', 'R3', 'L1',
                        'L1', 'R2', 'R3', 'R3', 'R1', 'L3', 'L5', 'R3', 'R1', 'L1', 'R1', 'R2', 'L1', 'L4', 'L5', 'R4',
                        'R2', 'L192', 'R5', 'L2', 'R53', 'R1', 'L5', 'R73', 'R5', 'L5', 'R186', 'L3', 'L2', 'R1', 'R3',
                        'L3', 'L3', 'R1', 'L4', 'L2', 'R3', 'L5', 'R4', 'R3', 'R1', 'L1', 'R5', 'R2', 'R1', 'R1', 'R1',
                        'R3', 'R2', 'L1', 'R5', 'R1', 'L5', 'R2', 'L2', 'L4', 'R3', 'L1', 'R4', 'L5', 'R4', 'R3', 'L5',
                        'L3', 'R4', 'R2', 'L5', 'L5', 'R2', 'R3', 'R5', 'R4', 'R2', 'R1', 'L1', 'L5', 'L2', 'L3', 'L4',
                        'L5', 'L4', 'L5', 'L1', 'R3', 'R4', 'R5', 'R3', 'L5', 'L4', 'L3', 'L1', 'L4', 'R2', 'R5', 'R5',
                        'R4', 'L2', 'L4', 'R3', 'R1', 'L2', 'R5', 'L5', 'R1', 'R1', 'L1', 'L5', 'L5', 'L2', 'L1', 'R5',
                        'R2', 'L4', 'L1', 'R4', 'R3', 'L3', 'R1', 'R5', 'L1', 'L4', 'R2', 'L3', 'R5', 'R3', 'R1', 'L3']

    @staticmethod
    def direction_calculator(directions_given):
        current_dir = 0  # facing north
        loc = (0, 0)
        for line in directions_given:
            for turn in [x.strip() for x in line.split(',')]:
                d, c = turn[0], int(turn[1:])
                current_dir = DIRF[d](current_dir)
                loc = (loc[0] + FACTORS[current_dir][0] * c,
                       loc[1] + FACTORS[current_dir][1] * c)

        end_result = 'DIST: %d' % (abs(loc[0]) + abs(loc[1]))
        print end_result
        return end_result

    # take 1
        # # north, east, south, west
        # position = (0, 0, 0, 0)
        # north = 0
        # east = 0
        # south = 0
        # west = 0
        # rights_encountered = 0
        # lefts_encountered = 0
        #
        # if len(directions_given) == 0:
        #     return position
        #
        # for direction in directions_given:
        #     if direction.startswith('R'):
        #         rights_encountered+=1
        #         if rights_encountered
        #
        #     elif direction.startswith('L'):
        #
        # return position


        # # loop through all the directions given
        # for direction in directions_given:
        #     # figure out the direction we're going
        #     # if we're going right
        #     if direction.startswith('R'):
        #         # get the number next to the direction
        #         move = int(direction[1])
        #         print "Current Move is: " + str(move)
        #         position = (0, move, 0, 0)
        #
        #     # if we're going left
        #     elif direction.startswith('L'):
        #         # get the number next to the direction
        #         move = int(direction[1])
        #         print "Current Move is: " + str(move)
        #         position = (0, 0, 0, move)
        #
        # return position
