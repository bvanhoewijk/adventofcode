import re
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

def parse_inputfile(inputfile):
    # position=< 9,  1> velocity=< 0,  2>
    x_pos = []
    y_pos = []
    vx = []
    vy = []
    for line in open(inputfile):
        m = re.search(r"position=<(.*\d+),(.*\d+)> velocity=<(.*\d+),(.*\d+)>", line)
        x_pos.append(int(m.group(1)))
        y_pos.append(int(m.group(2)))
        vx.append(int(m.group(3)))
        vy.append(int(m.group(4)))

    return x_pos, y_pos, vx, vy

if __name__ == "__main__":

    input_file = "input.txt"
    x_pos, y_pos, vx, vy = parse_inputfile(input_file)

    boxsizes = []
    for i in range(30000):
        # x_pos, y_pos = updateposition(x_pos, y_pos, vx, vy)
        for j in range(len(x_pos)):
            x_pos[j] += vx[j]
            y_pos[j] += vy[j]
        boxsizes.append(
            max(x_pos) - min(x_pos) + max(y_pos) - min(y_pos)
        )

    imin = np.argmin(boxsizes)

    print("Have to wait %s seconds" % (imin + 1))
    x_pos, y_pos, vx, vy = parse_inputfile(input_file)

    for i in range(len(x_pos)):
        x_pos[i] = x_pos[i] + ((imin + 1) * vx[i])
        y_pos[i] = (
            y_pos[i] + ((imin + 1) * vy[i])
        ) * -1  # Flip the image

    plt.plot(x_pos, y_pos, "bo")
    plt.show()


# RPNNXFZR
# 10946
