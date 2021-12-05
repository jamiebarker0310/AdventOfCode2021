import numpy as np


def part_one(file_path):

    with open(file_path) as f:
        lines = f.readlines()

    X = np.round(
        np.array([[int(x) for x in list(row.strip())] for row in lines]).mean(axis=0)
    )

    gamma = int("".join([str(int(i)) for i in X]), 2)
    epsilon = int("".join([str(int(not bool(i))) for i in X]), 2)

    return gamma * epsilon


def part_two(file_path):

    with open(file_path) as f:
        lines = f.readlines()

    X = np.array([[int(x) for x in list(row.strip())] for row in lines])
    og = oxygen_generator(X)

    X = np.array([[int(x) for x in list(row.strip())] for row in lines])
    sr = scrubber_rating(X)

    return og * sr


def oxygen_generator(X):

    i = 0
    while len(X) > 1:
        if X[:, i].mean() >= 0.5:
            X = X[X[:, i] == 1]
        else:
            X = X[X[:, i] == 0]
        i += 1
        i %= X.shape[1]

    return int("".join([str(int(i)) for i in X[0]]), 2)


def scrubber_rating(X):
    i = 0
    while len(X) > 1:
        if X[:, i].mean() >= 0.5:
            X = X[X[:, i] == 0]
        else:
            X = X[X[:, i] == 1]
        i += 1
        i %= X.shape[1]

    return int("".join([str(int(i)) for i in X[0]]), 2)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_03.txt"))
    print(part_two("aoc/inputs/day_03.txt"))
