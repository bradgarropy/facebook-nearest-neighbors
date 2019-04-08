# standard imports
import logging
import math
import re

# custom imports
from point import Point
import logger
import cli


def parse_neighbors(path):
    """ Parses neighbors file.

    Parameters:
        path (str): path to neighbors file.

    Returns:
        neighbors (list): list of neighbor Points.
    """

    neighbors = []

    with open(path, "r") as f:
        lines = f.readlines()

    for line in lines:
        neighbor = Point.from_string(line)
        neighbors.append(neighbor)

    return neighbors


def nearest(origin=Point.from_coords(0, 0), number=3, neighbors=[]):
    """ Finds nearest neighbors.

    Parameters:
        origin (Point):   origin point from which to find nearest neighbors.
        number (int):     number of nearest neighbors to find.
        neighbors (list): list of other Points on the graph.

    Returns:
        nearest_neighbors (list): list of nearest Points.
    """

    nearest_neighbors = []

    for neighbor in neighbors:

        if len(nearest_neighbors) < number:
            nearest_neighbors.append(neighbor)
            continue

        farthest = max(nearest_neighbors, key=lambda n: origin.distance(n))

        if origin.distance(neighbor) < origin.distance(farthest):
            index = nearest_neighbors.index(farthest)
            nearest_neighbors[index] = neighbor

    return nearest_neighbors


def summary(origin, neighbors):
    """ Logs summary of nearest neighbors.

    Parameters:
        origin (Point):   origin point from which to find nearest neighbors.
        neighbors (list): list of nearest Points.

    Returns:
        None
    """

    for neighbor in neighbors:
        logging.info("%s, %s", origin.distance(neighbor), neighbor)

    return


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

    # parse origin
    origin = Point.from_string(args.origin)

    # parse neighbors
    neighbors = parse_neighbors(args.neighbors)

    # determine nearest
    nearest_neighbors = nearest(origin, args.number, neighbors)

    # log summary
    summary(nearest_neighbors)

    return


if __name__ == "__main__":

    main()
