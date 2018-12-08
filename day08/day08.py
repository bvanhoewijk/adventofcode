from pprint import pprint

# Op deze ben ik wel een beetje trots :D
def part1(dataset):
    count = dataset.pop(0)
    meta = dataset.pop(0)

    result = 0
    for _ in range(count):
        result += part1(dataset)

    for _ in range(meta):
        result += dataset.pop(0)

    return result


# Toch maar even anders door heen...
def part2(i, dataset):
    count = dataset[i]
    meta = dataset[i + 1]
    nodes = []
    i += 2
    result = 0
    for _ in range(count):
        tmp, tmp2 = part2(i, dataset)
        i = tmp
        nodes.append(tmp2)
        
    for _ in range(meta):
        if count == 0:
            result += dataset[i]
        elif len(nodes) > (dataset[i] - 1) and (dataset[1] - 1) >= 0:
            result += nodes[dataset[i] - 1]
        i += 1

    return (i, result)


if __name__ == "__main__":
    dataset = [int(x) for x in open("input.txt").read().split(" ")]
    print(part1(dataset))
    dataset = [int(x) for x in open("input.txt").read().split(" ")]
    print(part2(0, dataset))

