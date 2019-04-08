# standard imports
import math
import re


class Point:

    def __init__(self, x, y):
        """ Initialize a Point.

        Parameters:
            x (float): x coordinate.
            y (float): y coordinate.

        Return:
            point (Point): Point object.
        """

        self.x = x
        self.y = y

        return

    @classmethod
    def from_string(cls, string):
        """ Initialize a Point from a string.

        Parameters:
            string (str): string coordinate.

        Return:
            point (Point): Point object.
        """

        match = re.search(r"\((-?\d+),\s*(-?\d+)\)", string)

        x = int(match.group(1))
        y = int(match.group(2))

        point = cls(x, y)
        return point

    @classmethod
    def from_coords(cls, x, y):
        """ Initialize a Point from coordinates.

        Parameters:
            x (float): x coordinate.
            y (float): y coordinate.

        Return:
            point (Point): Point object.
        """

        point = cls(x, y)
        return point

    def __str__(self):
        """ String representation of a Point.

        Parameters:
            None

        Returns:
            string (str): string representation.
        """

        string = "(%s, %s)" % (self.x, self.y)
        return string

    def distance(self, point):
        """ Calculate distance to another Point.

        Parameters:
            point (Point): another Point object.

        Returns:
            distance (float): distance between Points.
        """

        x = point.x - self.x
        y = point.y - self.y

        distance = math.hypot(x, y)

        return distance
