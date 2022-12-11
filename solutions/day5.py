from collections import deque
stacks = [
    ['B', 'V', 'S', 'N', 'T', 'C', 'H', 'Q'],
    ['W', 'D', 'B','G'],
    ['F', 'W', 'R', 'T', 'S', 'Q', 'B'],
    ['L', 'G', 'W', 'S', 'Z', 'J', 'D', 'N'],
    ['M', 'P', 'D', 'V', 'F'],
    ['F', 'W', 'J'],
    ['L', 'N', 'Q', 'B', 'J', 'V'],
    ['G', 'T', 'R', 'C', 'J', 'Q', 'S', 'N'],
    ['J', 'S', 'Q', 'C', 'W', 'D', 'M']
]
f = open("./data/day5.txt", "r")
for i in f:
    count, source, destination = [int(s) for s in i.split() if s.isdigit()]
    for i in range(0, count):
        last = stacks[source-1].pop()
        stacks[destination-1].append(last)
    temp = deque()
    for i in range(0, count):
        last = stacks[source-1].pop()
        temp.appendleft(last)
    stacks[destination - 1].extend(temp)


print([j for i in stacks for j in i[-1]])





