# standard imports
import logging

# custom imports
import logger
import point
import cli


def parse_neighbors():
    """ Parses neighbors file.

    Parameters:
        path (str): path to neighbors file.

    Returns:
        neighbors (list): list of neighbor Points.
    """

    neighbors = []

    with open("neighbors.txt", "r") as f:
        points = f.readlines()

    print points

    return neighbors


def nearest(origin=point.Point(0, 0), number=3, neighbors=[]):
    """ Finds nearest neighbors.

    Parameters:
        origin (Point):   origin point from which to find nearest neighbors.
        number (int):     number of nearest neighbors to find.
        neighbors (list): list of other Points on the graph.

    Returns:
        nearest_neighbors (list): list of nearest Points.
    """

    nearest_neighbors = []

    return nearest_neighbors


def main():
    """ Main method.

    Parameters:
        None

    Returns:
        None
    """

    # configure logging
    logger.configure()

    # cli arguments
    args = cli.cli()

    # run migration monitor
    nearest(args.origin, args.number, args.points)

    return


if __name__ == "__main__":

    main()
