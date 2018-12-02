#!/usr/bin/env python3

def get_occurence_dict(barcode):
    occurence_dict = {}
    for char in barcode:
        if char in occurence_dict:
            occurence_dict[char] = occurence_dict[char] + 1
        else:
            occurence_dict[char] = 1
    return occurence_dict

def distance(string1, string2):
    dist = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            dist += 1
    return dist

def part1(alist):
    twos = 0
    threes = 0

    

    for barcode in alist:
        thedict = get_occurence_dict(barcode)
        found_two = False
        found_three = False
        for item in thedict:
            if(thedict[item] == 2):
                found_two = True
            elif(thedict[item] == 3):
                found_three = True
        if found_two:
            twos += 1
        if found_three:
            threes += 1
        
    print("Twos    : ", twos)
    print("Threes  : ", threes)
    print("Checksum: ", (twos * threes))

def common(string1, string2):
    final_string = ""
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            final_string += string1[i]
    return final_string

if __name__ == "__main__":
    alist = [line.rstrip() for line in open("input.txt")]
    part1(alist)
    
    # Imagine the data as a matrix we have to fill in:
    for i in range(0, len(alist)):
        for j in range(i + 1, len(alist)):
            d = distance(alist[i], alist[j])
            if d == 1:
                print(alist[i], alist[j])
                print(common(alist[i], alist[j]))
