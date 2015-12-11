__author__ = 'smelnyk'


def calculate_footage_of_ribbon_needed(wrapping_paper_order_list):

    total_ribbon_needed = 0

    # wrapping_paper_order_list = [int(i) for i in wrapping_paper_order_list]

    for order in wrapping_paper_order_list:
        print "Ribbon order being looked at: " + str(order.strip())
        order = order.strip('\n')
        current_order = order.split('x')
        print "current_order being looked at: " + str(current_order)

        current_order = [int(i) for i in current_order]

        total_ribbon_needed += order_more_ribbon(current_order)
        print "total_ribbon_needed is: " + str(total_ribbon_needed)

    print "calculate_footage_of_ribbon_needed - total_ribbon_footage_needed is: " \
          "" + str(total_ribbon_needed)
    print  # Print a blank line after each full order
    return total_ribbon_needed


def calculate_footage_of_wrapping_paper_needed(wrapping_paper_order_list):
    """
    This is a method to help calculate the amount of wrapping paper is needed.
    Soon will also be calculating the amount of ribbon needed and adding it to that total
    """
    total_square_feet_needed = 0
    current_order = []

    # print "Current wrapping_paper_order_list is: " + str(wrapping_paper_order_list)

    for order in wrapping_paper_order_list:
        # print "order being looked at: " + str(order)

        current_order = order.split('x')
        # print "current_order being looked at: " + str(current_order)

        total_square_feet_needed += order_more_wrapping_paper(current_order)

    print "calculate_square_footage_needed - total_square_feet_needed is: " + str(total_square_feet_needed)
    print  # Print a blank line after each full order
    return total_square_feet_needed


def order_more_wrapping_paper(set_of_dimensions):
    """ This is a helper method to help complete the above function """
    # print "Current set_of_dimensions is: " + str(set_of_dimensions)

    length = 0
    width = 0
    height = 0
    square_footage_needed = 0
    slack = 0

    length = int(set_of_dimensions[0])
    # print "length is: " + str(length)
    width = int(set_of_dimensions[1])
    # print "width is: " + str(width)
    height = int(set_of_dimensions[2])
    # print "height is: " + str(height)

    area_1 = (length * width)
    area_2 = (width * height)
    area_3 = (height * length)

    # print "area_1 is (length): " + str(area_1)
    # print "area_2 is (width): " + str(area_2)
    # print "area_3 is (height): " + str(area_3)

    # The elves also need a little extra paper for each present: the area of the smallest side.
    if area_1 <= area_2 and area_1 <= area_3:
        slack = area_1
        # print "Slack is (length): " + str(slack)
    elif area_2 <= area_1 and area_2 <= area_3:
        slack = area_2
        # print "Slack is (width): " + str(slack)
    elif area_3 <= area_1 and area_3 <= area_2:
        slack = area_3
        # print "Slack is (height): " + str(slack)

    # To calculate square feet needed: 2*l*w + 2*w*h + 2*h*l + slack
    square_footage_needed = (2 * length * width) + (2 * width * height) + (2 * height * length) + slack
    print "order_more_wrapping_paper - square_footage_needed is: " + str(square_footage_needed)
    print
    return square_footage_needed


def order_more_ribbon(set_of_dimensions):
    """
    This is a helper method to calculate the needed ribbon footage for a present.
    Includes calculating the Ribbon needed for the Bow and then adds the two together.
    Returns an int of the total footage of ribbon needed.

    """

    length = 0
    width = 0
    height = 0
    ribbon_footage_needed = 0
    bow_footage_needed = 0
    total_ribbon_footage_needed = 0
    slack_1 = 0
    slack_2 = 0
    update_order_list = []

    # This format works the same as the length, width, height assignments below
    length, width, height = int(set_of_dimensions[0]), int(set_of_dimensions[1]), int(set_of_dimensions[2])

    # The above format is an alternate way of doing the following assignments
    # length = int(set_of_dimensions[0])
    # print "length is: " + str(length)
    # width = int(set_of_dimensions[1])
    # print "width is: " + str(width)
    # height = int(set_of_dimensions[2])
    # print "height is: " + str(height)

    # Ribbon Feet needed: 2+2+3+3 = 10
    slack_1 = min(set_of_dimensions)
    print "slack_1 is: " + str(slack_1)

    # if length <= width and length <= height:
    #     slack_1 = length
    # elif width <= length and width <= height:
    #     slack_1 = width
    # elif height <= length and height <= width:
    #     slack_1 = height
    # print "slack_1 is: " + str(slack_1)

    # Create a list with the original dimensions in it, minus the smallest value and then compare
    # the remaining two
    update_order_list = [i for i in set_of_dimensions]
    print "update_order_list is: " + str(update_order_list)

    update_order_list.remove(slack_1)
    print "update_order_list 2 is: " + str(update_order_list)

    if update_order_list[0] <= update_order_list[1]:
        slack_2 = update_order_list[0]
    elif update_order_list[1] <= update_order_list[0]:
        slack_2 = update_order_list[1]

    print "slack_2 is: " + str(slack_2)

    # if width >= slack_1 and height >= slack_1 and length <= slack_1:
    #     slack_2 = width
    # elif height >= slack_1 and length >= slack_1 and width <= slack_1:
    #     slack_2 = height
    # elif length >= slack_1 and width >= slack_1 and height <= slack_1:
    #     slack_2 = length
    # print "slack_2 is: " + str(slack_2)

    ribbon_footage_needed = slack_1 + slack_1 + slack_2 + slack_2
    # print "ribbon_footage_needed is: " + str(ribbon_footage_needed)

    # Bow Feet needed: 2*3*4 = 24
    bow_footage_needed = length * width * height
    # print "bow_footage_needed is: " + str(bow_footage_needed)

    total_ribbon_footage_needed = ribbon_footage_needed + bow_footage_needed
    print "order_more_ribbon - total_ribbon_footage_needed is: " + str(total_ribbon_footage_needed)
    return total_ribbon_footage_needed