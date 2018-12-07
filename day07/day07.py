import re
from pprint import pprint
from collections import defaultdict


def parseline(line):
    m = re.search(r"Step (.) must be finished before step (.) can begin.", line)
    return (m.group(1), m.group(2))

if __name__ == "__main__":
    data = [parseline(line.rstrip()) for line in open("input.txt")]
    # HashSet only adds one
    # Discovered default dict 
    requirements = defaultdict(set)

    # Add requirements to set
    nodes = set()
    for item in data:
        requirements[item[1]].add(item[0])
        nodes.add(item[0])
        nodes.add(item[1])

    # print(nodes)
    sorted_nodes = sorted(nodes)
    done = set()
    result = []
    # While I have not positioned all the nodes
    while sorted_nodes:
        for node in sorted_nodes:
            deps = requirements[node]
            # If no requirements:
            if len(deps - done) == 0:
                result.append(node)
                sorted_nodes.remove(node)
                done.add(node)
                break

    print("Part1: %s" % "".join(result))
    sorted_nodes = sorted(nodes)
    print(sorted_nodes)