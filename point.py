# standard imports
import re


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        return

    @classmethod
    def from_string(cls, string):
        match = re.search(r"\((-?\d+),\s*(-?\d+)\)", string)

        x = int(match.group(1))
        y = int(match.group(2))

        point = cls(x, y)
        return point

    @classmethod
    def from_coords(cls, x, y):
        point = cls(x, y)
        return point

    def __str__(self):
        string = "(%s, %s)" % (self.x, self.y)
        return string
