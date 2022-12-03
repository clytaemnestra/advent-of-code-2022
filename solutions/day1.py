def get_data():
    file = open("./data/day1.txt", "r")
    data = file.readlines()
    return data


def first_part():
    data = get_data()
    max = 0
    curr = 0
    for i in data:
        if i != "\n":
            curr += int(i)
        else:
            if curr > max:
                max = curr
                curr = 0
            curr = 0
    return print(max)


def second_part():
    data = get_data()
    max = 0
    list_of_max = []
    curr = 0
    for i in data:
        if i != "\n":
            curr += int(i)
        else:
            if curr > max:
                max = curr
                list_of_max.append(curr)
                curr = 0
            curr = 0
    s = sorted(list_of_max, reverse=True)
    return print(sum(s[:3]))


first_part()
second_part()
