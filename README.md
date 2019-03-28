# 🏘 Facebook Nearest Neighbors

## Problem

Write a program that finds the n closest points to a given point p.

## Solution
Where n is the number and p is the origin.

```
def closest(points, number, origin)
```

* Maintain a list of the closest n points.
* For every point in points:
    * Find it's distance from the origin.
    * Find the point farthest away in the list.
    * Insert the current point into the list of points only if the current point is closer than the farthest point in the list.
