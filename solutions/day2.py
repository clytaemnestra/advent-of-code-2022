def data():
    with open("./data/day2.txt", "r") as f:
        lines = [i.strip() for i in f]
        a, b = zip(*(s.split(" ") for s in lines))
        return a, b


def calculate_strategy():
    a, b = data()
    y_counter = 0
    z_counter = 0
    x_counter = 0

    for i in b:
        match i:
            case 'Y':
                y_counter += 2
            case 'Z':
                z_counter += 3
            case 'X':
                x_counter += 1
    sum_of_choices = y_counter + z_counter + x_counter

    match_counter = 0
    for i, j in zip(a, b):
        match i, j:
            case ('A', 'Y') | ('B', 'Z') | ('C', 'X'):
                match_counter += 6
            case ('A', 'X') | ('B', 'Y') | ('C', 'Z'):
                match_counter += 3
    return print(match_counter + sum_of_choices)


calculate_strategy()


def change_strategy():
    a, b = data()
    score = 0
    for i, j in zip(a, b):
        match i, j:
            case ('A', 'Y'):
                score += 4
            case ('A', 'X'):
                score += 3
            case ('A', 'Z'):
                score += 8
            case ('B', 'X'):
                score += 1
            case ('B', 'Y'):
                score += 5
            case ('B', 'Z'):
                score += 9
            case ('C', 'X'):
                score += 2
            case ('C', 'Y'):
                score += 6
            case ('C', 'Z'):
                score += 7
    return print(score)


change_strategy()
