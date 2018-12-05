#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"

def react(line):
    oldline = ""
    while line != oldline:
        oldline = line
        for letter in alphabet:
            line = line.replace(letter.upper() + letter, "")
            line = line.replace(letter + letter.upper(), "")
    return line

if __name__ == "__main__":
    # Part1
    dataset = open("input.txt").read().strip()
    line = react(dataset)
    print("After all reactions:", len(line))

    # Part2
    shortest = len(dataset)
    for letter in alphabet:
        line = dataset
        line = line.replace(letter.upper(), "")
        line = line.replace(letter, "")
        size = len(react(line))
        shortest = size if size < shortest else shortest

    print("Shortest polymer: ", shortest)

