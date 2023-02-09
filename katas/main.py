# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Geometry Basics: Distance between points in 2D.
# This series of katas will introduce you to basics of doing geometry with computers.
# Point objects have attributes x and y.
# Write a function calculating distance between Point a and Point b.
# Tests compare expected result and actual answer with tolerance of 1e-6.

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance_between_points(a, b):
    return math.sqrt(((b.x - a.x) * (b.x - a.x)) + ((b.y - a.y) * (b.y - a.y)))

res = distance_between_points(Point(1, 6), Point(4, 2))
print(res)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
