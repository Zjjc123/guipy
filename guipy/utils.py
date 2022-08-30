def sub_coords(offset, coord):
    """
    Finds the relative coordinate of one point in another point

    :param coord: the coordinate
    :param offset: the coordinate relative to

    """
    return (coord[0] - offset[0], coord[1] - offset[1])


def translate(value, min1, max1, min2, max2):
    """
    Maps one value from one range to another range

    :param value: Value to be mapped
    :param min1: Min of range 1
    :param max1: Max of range 1
    :param min2: Min of range 2
    :param max2: Max of range 2
    """
    span1 = max1 - min1
    span2 = max2 - min2
    if span1 == 0:
        return 0
    valueScaled = float(value - min1) / float(span1)
    return min2 + (valueScaled * span2)


WHITE = (255, 255, 255)
"""
Preset for the color White
"""
RED = (255, 0, 0)
"""
Preset for the color Red
"""
GREEN = (0, 255, 0)
"""
Preset for the color Green
"""
BLUE = (0, 0, 255)
"""
Preset for the color Blue
"""
BLACK = (0, 0, 0)
"""
Preset for the color Black
"""
GREY = (230, 230, 230)
"""
Preset for the color Grey
"""
DARK_GREY = (100, 100, 100)
"""
Preset for the color Dark Grey
"""
ORANGE = (255, 100, 0)
"""
Preset for the color Orange
"""
