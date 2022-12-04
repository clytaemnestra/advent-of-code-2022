import re


def map_data():
    file = open("./data/day4.txt", "r")
    pattern = r"(\d+)-(\d+),(\d+)-(\d+)"
    nums = [
        list(map(lambda i: int(i), re.findall(pattern, line)[0]))
        for line in file.read().strip().split("\n")
    ]
    nums1 = [j for i in nums for j in i]
    return nums1


def count():
    data = map_data()
    counter = 0
    counter1 = 0
    ff = iter(data)
    while True:
        try:
            a, b, c, d = next(ff), next(ff), next(ff), next(ff)
            if (a >= c or b >= d) and (a <= c or b <= d):
                counter += 1
            if (
                (a <= c and c <= b)
                or (a <= d and d <= b)
                or (c <= a and a <= d)
                or (c <= b and b <= d)
            ):
                counter1 += 1
        except StopIteration:
            return print(counter, counter1)


count()
