__author__ = 'smelnyk'

import re

"""
Because your neighbors keep defeating you in the holiday house decorating contest year
after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you
instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each
corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on,
turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair
represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through
2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the
instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.

toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones
that were on, and turning on the ones that were off.

turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?
"""


def toggle_lights(instructions):

    # Need a 1000x1000 grid/matrix
    light_grid = []
    num_of_lights_on = 0

    for x_axis in xrange(1000):
        for y_axis in xrange(1000):
            # I don't know if this works this way or not
            light_grid.append((x_axis, y_axis))

    print "Grid is: " + str(light_grid)


    # The lights all start turned off.
    light_on = False

    # Corner Lights are numbered as follows:
    # top-left: 0,0
    #    top-right: 999,0
    #    bottom left: 0,999
    #    bottom right: 999,999
    # corners = [(0, 0), (999, 0), (0, 999), (999, 999)]

    # Will need some bool checks to check whether a light is on (true) or off (false)

    # The instructions include whether to turn on, turn off, or
    # toggle various inclusive ranges given as coordinate pairs
    # Each coordinate pair represents opposite corners of a rectangle,
    # inclusive; a coordinate pair
    # like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.

    # Will need to parse the ranges from the string passed in:
    print "instructions is: " + str(instructions.read())

    updated_instructions = instructions.read()

    for line in updated_instructions:
        line = line.strip()
        print "line is: " + str(line)
        ranges = re.findall(r'([0-9]+,[0-9]+)', line)
        print "ranges is: " + str(ranges)

        # To see whether the lights to be to turned on:
        # if re.findall(r'^turn on', line):

        # To see whether the lights to be to turned off:
        # if re.findall(r'^turn off', line):

        # To see if we're toggling multiple lights
        # if re.findall(r'^toggle', line):


    return num_of_lights_on
