# standard imports
import random
import sys


def create_point():
    """ Creates a point entry.

    Parameters:
        None

    Returns:
        point (str): point in the format (x, y).
    """

    x = random.randint(-100, 100)
    y = random.randint(-100, 100)

    point = "(%s, %s)" % (x, y)

    return point


def main():
    """ Main method.

    Parameters:
        None

    Returns:
        None
    """

    number = int(sys.argv[1])

    points = [create_point() for _ in xrange(number)]
    points = "\n".join(points)

    with open("../neighbors.txt", "w") as f:
        f.writelines(points)

    return


if __name__ == "__main__":

    main()
