#!/usr/bin/env python3


def first_part():
    alist = [line.rstrip() for line in open("input.txt")]
    freq = 0

    firstround = True
    seen = {0}
    while True:
        for item in alist:
            op = item[0]
            inc = item[1:]
            if op == "+":
                freq += int(inc)
            elif op == "-":
                freq -= int(inc)

            if freq in seen:
                print("Twice: ", freq)
                return
            seen.add(freq)
        if firstround:
            print("Sum of list: ", freq)
            firstround = False

    print("final frequency: ", freq)


if __name__ == "__main__":
    first_part()
