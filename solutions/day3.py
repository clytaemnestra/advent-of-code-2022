import string


def data():
    with open("./data/day3.txt", "r") as f:
        lines = [i.strip() for i in f]
    return lines


def get_diff():
    backpacks = data()
    diff = []
    for i in backpacks:
        first_half, second_half = i[: len(i) // 2], i[len(i) // 2 :]
        diff.append(set(first_half).intersection(set(second_half)))
    return diff


def priority():
    priority_mapping = dict(zip(string.ascii_lowercase, range(1, 27)))
    priority_mapping.update(zip(string.ascii_uppercase, range(27, 53)))
    return priority_mapping


def evaluate():
    items = get_diff()
    priority_mapping = priority()
    counter = 0
    for k, v in priority_mapping.items():
        for j in items:
            if k in j:
                counter += v
    return print(counter)


evaluate()


def get_diff2():
    backpacks = data()
    priority_mapping = priority()
    intersections = []
    for i in range(0, len(backpacks), 3):
        intersections.append(
            set(backpacks[i])
            .intersection(backpacks[i + 1])
            .intersection(backpacks[i + 2])
        )
    counter = 0
    for k, v in priority_mapping.items():
        for j in intersections:
            if k in j:
                counter += v
    return print(counter)


get_diff2()
