#!/usr/bin/env python3
import re
from pprint import pprint

# 1 @ 1,3: 4x4
# 2 @ 3,1: 4x4
# 3 @ 5,5: 2x2
def parse_input(line):
    fabric = dict()
    m = re.search(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)
    fabric["id"] = int(m.group(1))
    fabric["xpos"] = int(m.group(2))
    fabric["ypos"] = int(m.group(3))
    fabric["width"] = int(m.group(4))
    fabric["height"] = int(m.group(5))

    return fabric


def allocate_suit(list_of_fabrics):
    rowmax = 0
    colmax = 0
    santa_suit = {}
    for one_piece in list_of_fabrics:
        xend = one_piece["xpos"] + one_piece["width"]
        yend = one_piece["ypos"] + one_piece["height"]
        rowmax = xend if xend > rowmax else rowmax
        colmax = yend if yend > colmax else colmax

        for i in range(one_piece["xpos"], xend):
            for j in range(one_piece["ypos"], yend):
                if (j, i) in santa_suit:
                    santa_suit[j, i] += 1
                else:
                    santa_suit[j, i] = 1

    return {"suit": santa_suit, "rowmax": rowmax, "colmax": colmax}


def no_overlap(list_of_fabrics, suit_info):
    santa_suit = suit_info["suit"]
    for one_piece in list_of_fabrics:
        overlap = False
        for i in range(one_piece["xpos"], one_piece["xpos"] + one_piece["width"]):
            for j in range(one_piece["ypos"], one_piece["ypos"] + one_piece["height"]):
                if (j, i) in santa_suit and santa_suit[j, i] > 1:
                    overlap = True
        if not overlap:
            print("No overlap ID: #%s" % one_piece["id"])


def more_than_two_claims(suit_info):
    two_or_more = 0
    santa_suit = suit_info["suit"]
    for x in range(suit_info["rowmax"]):
        for y in range(suit_info["colmax"]):
            if (x, y) in santa_suit and santa_suit[x, y] > 1:
                two_or_more += 1

    print("Two or more claims: ", two_or_more)


if __name__ == "__main__":
    list_of_fabrics = [parse_input(line.rstrip()) for line in open("input.txt")]
    suit_info = allocate_suit(list_of_fabrics)
    print("Colmax: ", suit_info["colmax"])
    print("Rowmax: ", suit_info["rowmax"])
    more_than_two_claims(suit_info)

    no_overlap(list_of_fabrics, suit_info)

