f = open("./data/day8.txt", "r").read().splitlines()
counter = 0
for rowindex, i in enumerate(f):
    for columnindex, currenttree in enumerate(i):
        counter += (
                all(f[rowindex][m] < currenttree for m in range(0, columnindex))
                or all(f[rowindex][m] < currenttree for m in range(columnindex + 1, len(i)))
                or all(f[n][columnindex] < currenttree for n in range(0, rowindex))
                or all(f[n][columnindex] < currenttree for n in range(rowindex + 1, len(f)))
        )
print(counter)
