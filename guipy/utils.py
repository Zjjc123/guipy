WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREY = (230, 230, 230)
DARK_GREY = (100, 100, 100)
ORANGE = (255, 100, 0)


def sub_coords(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])


# maps a value from one range to another
def translate(value, min1, max1, min2, max2):
    span1 = max1 - min1
    span2 = max2 - min2
    if span1 == 0:
        return 0
    valueScaled = float(value - min1) / float(span1)
    return min2 + (valueScaled * span2)
