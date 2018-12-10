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
    velocityx = []
    velocityy = []
    for line in open(inputfile):
        m = re.search(r"position=<(.*\d+),(.*\d+)> velocity=<(.*\d+),(.*\d+)>", line)
        xposition.append(int(m.group(1)))
        yposition.append(int(m.group(2)))
        velocityx.append(int(m.group(3)))
        velocityy.append(int(m.group(4)))


    return xposition, yposition, velocityx, velocityy


def updateposition(xposition, yposition, velocityx, velocityy):
    for i in range(len(xposition)):
        xposition[i] += velocityx[i]
        yposition[i] += velocityy[i]
    return xposition, yposition


if __name__ == "__main__":

    input_file = "input.txt"
    xposition, yposition, velocityx, velocityy = parse_inputfile(input_file)

    boxsizes = []
    for i in range(30000):
        xposition, yposition = updateposition(xposition, yposition, velocityx, velocityy)
        boxsizes.append(max(xposition) - min(xposition) + max(yposition) - min(yposition))

    imin = np.argmin(boxsizes)

    print("Have to wait %s seconds" % (imin + 1))
    xposition, yposition, velocityx, velocityy = parse_inputfile(input_file)

    for i in range(len(xposition)):
        xposition[i] = xposition[i] + ((imin+1) * velocityx[i])
        yposition[i] = (yposition[i] + ((imin+1) * velocityy[i])) *-1 # Flip the image

    # for i in range(len(xposition)):
    #     xposition[i] = xposition[i] 
    #     yposition[i] = yposition[i] * -1 
    plt.plot(xposition, yposition, "bo")
    plt.show()


# RPNNXFZR
# 10946
