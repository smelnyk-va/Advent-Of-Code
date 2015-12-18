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

    # The lights all start turned off
    light_on = False
    num_of_lights_on = 0

    # Need a 1000x1000 grid/matrix
    gridsize = 1000
    light_grid = []

    # Tried the following but it just makes a grid with a bunch of zeros?
    # Unless this is fine and I need to append the lights that are either on
    # I think this is the GRID format I'll need to use
    # Will just need to append the values in later and not at creation
    # for x_axis in range(gridsize):
    #     light_grid.append([])
    #     for y_axis in range(gridsize):
    #         light_grid[x_axis].append(0)

    # This is giving me a populated grid... not sure if that's what I actually want...
    for x_axis in xrange(gridsize):
        for y_axis in xrange(gridsize):
            # I don't know if this works this way or not
            light_grid.append((x_axis, y_axis))
    print "light_grid is: " + str(light_grid)

    # Loop through all the instructions from the input file
    for line in instructions:
        # Clean up any extra whitespace from the current instructions line
        line = line.strip()
        print "line is: " + str(line)
        # Get the starting range and end range, both stored in ranges
        # Should maybe store into two separate variables instead of just 1?
        ranges = re.findall(r'([0-9]+,[0-9]+)', line)
        print "ranges is: " + str(ranges)

        # Will need to check whether a light is on, off, or being toggled
        # To see whether the lights to be to turned on:
        # if re.findall(r'^turn on', line):
            # light_on = True
            # Loop through and turn on all the specified lights

        # To see whether the lights to be to turned off:
        # if re.findall(r'^turn off', line):
            # light_on = False
            # Loop through and turn off all the specified lights

        # To see if we're toggling multiple lights
        # if re.findall(r'^toggle', line):
            # Loop through and toggle on/off all the specified lights

    print "num_of_lights_on is: " + str(num_of_lights_on)
    return num_of_lights_on
