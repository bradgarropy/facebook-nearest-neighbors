# standard imports
import logging
import math
import re

# custom imports
from point import Point
import logger
import cli


def calculate_distance(p1, p2):
    """ Calculates the distance between two Points.

    Parameters:
        p1 (Point): first point.
        p2 (Point): second point.

    Returns:
        distance (float): distance between the two points.
    """

    x = p2.x - p1.x
    y = p2.y - p1.y

    distance = math.hypot(x, y)

    return distance


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

        distance = calculate_distance(origin, neighbor)
        farthest = max(nearest_neighbors)

        if distance < farthest:
            logging.info(
                "distance (%s) is closer than farthest (%s)!", distance, farthest)
            index = nearest_neighbors.index(farthest)
            nearest_neighbors[index] = distance

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

    # parse origin
    origin = Point.from_string(args.origin)

    # parse neighbors
    neighbors = parse_neighbors(args.neighbors)

    # determine nearest
    nearest(origin, args.number, neighbors)

    return


if __name__ == "__main__":

    main()
