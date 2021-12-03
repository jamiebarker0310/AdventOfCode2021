def part_one(file_path):

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # convert data to int
    lines = [int(i.strip()) for i in lines]

    # if the next term is
    return sum([a < b for a, b in zip(lines[:-1], lines[1:])])


def part_two(file_path):

    with open(file_path) as f:
        lines = f.readlines()

    # convert data to int
    lines = [int(i.strip()) for i in lines]

    # get rolling windows of size 3
    windows = zip(lines[:-2], lines[1:-1], lines[2:])

    # sum each window
    windows = list(map(sum, windows))

    # get count of increasing amount
    return sum([a < b for a, b in zip(windows[:-1], windows[1:])])


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_01.txt"))
    print(part_two("aoc/inputs/day_01.txt"))
