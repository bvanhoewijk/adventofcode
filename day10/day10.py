import re
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm
import numpy as np
from celluloid import Camera
import pylab


def parse_inputfile(inputfile):
    # position=< 9,  1> velocity=< 0,  2>
    xposition = []
    yposition = []
    velocity = []
    for line in open(inputfile):
        m = re.search(r"position=<(.*\d+),(.*\d+)> velocity=<(.*\d+),(.*\d+)>", line)
        xposition.append(int(m.group(1)))
        yposition.append(int(m.group(2)))
        velocity.append([int(m.group(3)), int(m.group(4))])

    return xposition, yposition, velocity


def updateposition(xposition, yposition, velocity):
    for i in range(len(xposition)):
        xposition[i] += velocity[i][0]
        yposition[i] += velocity[i][1]
    return xposition, yposition


if __name__ == "__main__":

    input_file = "small.txt"
    xposition, yposition, velocity = parse_inputfile(input_file)

    boxsizes = []
    for i in range(30000):
        xposition, yposition = updateposition(xposition, yposition, velocity)
        boxsizes.append(max(xposition) - min(xposition) + max(yposition) - min(yposition))

    imin = np.argmin(boxsizes)

    print("Have to wait %s seconds" % (imin + 1))
    xposition, yposition, velocity = parse_inputfile(input_file)
    # for _ in range(imin + 1):
    #     xposition, yposition = updateposition(xposition, yposition, velocity)

    for i in range(len(xposition)):
        xposition[i] = xposition[i] + ((imin+1) * velocity[i][0])
        yposition[i] = yposition[i] + ((imin+1) * velocity[i][1])

    for i in range(len(xposition)):
        xposition[i] = xposition[i] 
        yposition[i] = yposition[i] * -1 # Flip the image
    plt.plot(xposition, yposition, "bo")
    plt.show()


# RPNNXFZR
# 10946
