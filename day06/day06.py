#!/usr/bin/env python3
import numpy as np
import string
from pprint import pprint


def parse_input(input):
    alist = [line.rstrip() for line in open(input)]
    x = [(int(x.split(",")[0])) for x in alist]
    y = [(int(x.split(",")[1])) for x in alist]
    return x, y


def closest(coordinate, x, y):
    current_min = 1000000
    closest_spot = None
    for i in range(len(x)):
        dist = abs(coordinate[0] - x[i]) + abs(coordinate[1] - y[i])
        if dist == 0:
            current_min = dist
            closest_spot = i
        elif dist < current_min:
            current_min = dist
            closest_spot = i
        elif dist == current_min:
            closest_spot = None

    return closest_spot


def part2(coordinate, x, y):
    dist = 0
    for i in range(len(x)):
        dist += abs(coordinate[0] - x[i]) + abs(coordinate[1] - y[i])
    return dist


if __name__ == "__main__":
    x, y = parse_input("input.txt")
    xmax = max(x)
    ymax = max(y)

    surface = dict()
    ignored = set()
    ignored.add(None)
    for i in range(ymax + 1):
        for j in range(xmax + 1):
            location = closest((j, i), x, y)
            if i == 0 or j == 0 or i == ymax + 1 or j == xmax + 1:
                ignored.add(location)

            if location in surface:
                surface[location] += 1
            else:
                surface[location] = 1

    for item in ignored:
        del surface[item]

    print("Max surface without infinites: %s" % surface[max(surface, key=surface.get)])

    area = 0
    for i in range(ymax + 1):
        for j in range(xmax + 1):
            dist = part2((j, i), x, y)
            if dist < 10000:
                area += 1
    print("Part2 area: ", area)
