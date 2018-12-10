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
    
    input_file = "input.txt"
    xposition, yposition, velocity = parse_inputfile(input_file)

    boxsizes = []
    for i in range(30000):
        xposition, yposition = updateposition(xposition, yposition, velocity)
        xmax = max(xposition)
        xmin = min(xposition) 
        ymax = max(yposition)
        ymin = min(yposition) 
        if xmin < 0:
            xmax += abs(xmin)
            xmin += abs(xmin)
        if ymin < 0:
            ymin += abs(ymin)
            ymin += abs(ymin)

        boxsizes.append(xmax*ymax)

    imin = np.argmin(boxsizes)
    print("imin: ", imin+1)
    xposition, yposition, velocity = parse_inputfile(input_file)
    for _ in range(imin+1):
        xposition, yposition = updateposition(xposition, yposition, velocity)
    
    plt.plot(xposition, yposition, "bo")
    plt.show()

    

# RPNNXFZR
# 10946
