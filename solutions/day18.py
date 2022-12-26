f = open("./data/day18.txt", "r").read().splitlines()

cubes = [
    tuple(int(c) for c in line.split(','))
    for line in f
]


def cubes_share_edge(cubes):
    counter = 0
    for i in range(len(cubes)):
        for j in range(i + 1, len(cubes)):
            x1, y1, z1 = cubes[i]
            x2, y2, z2 = cubes[j]

            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

            if distance == 1:
                counter += 2
    print((len(cubes) * 6) - counter)


cubes_share_edge(cubes=cubes)
