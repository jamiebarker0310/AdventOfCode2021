from collections import Counter


def part_one(file_path: str) -> int:
    """
    Parses all lines, and returns the number of points where at least two
    lines horizontal or vertical overlap

    Args:
        file_path (str):

    Returns:
        int: the number of points where at least two lines overlap
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # return number of points that appear twice
    return day_05(lines, diagonal=False)


def part_two(file_path: str) -> int:
    """
    Parses all lines, and returns the number of points where at least two
    lines horizontal, vertical or diagonal overlap

    Args:
        file_path (str):

    Returns:
        int: the number of points where at least two lines overlap
    """

    with open(file_path) as f:
        lines = f.readlines()

    return day_05(lines, diagonal=True)


def day_05(lines: list, diagonal: bool = False) -> int:
    """
    Parses all lines, and returns the number of points where at least two
    lines horizontal, vertical or (optional) diagonal overlap

    Args:
        lines (list):
        diagonal (bool, optional): whether to include diagonals. Defaults to False.

    Returns:
        int: the number of points where at least two lines overlap
    """
    # for each line, split by " -> " to get start and end,
    # then split each of those by "," map to an integer.
    # This returns list of list of 2 tuples of 2 integers.
    pairs = [
        [tuple(map(int, pair.strip().split(","))) for pair in line.split(" -> ")]
        for line in lines
    ]

    # initialise line list
    line_list = []
    # for each line
    for line in pairs:
        # initialise end points
        x1, y1 = line[0]
        x2, y2 = line[1]
        # if line is vertical
        if x1 == x2:
            # append each y coordinate
            for y in range(min(y1, y2), max(y1, y2) + 1):
                line_list.append((x1, y))
        # if line is horizontal
        elif y1 == y2:
            # append each x coordinate
            for x in range(min(x1, x2), max(x1, x2) + 1):
                line_list.append((x, y1))

        elif diagonal:
            # get ordered x coordinates
            if x1 < x2:
                x_coords = range(x1, x2 + 1)
            else:
                x_coords = reversed(range(x2, x1 + 1))
            # get ordered y coordinates
            if y1 < y2:
                y_coords = range(y1, y2 + 1)
            else:
                y_coords = reversed(range(y2, y1 + 1))

            # append each x,y pair
            for x, y in zip(x_coords, y_coords):
                line_list.append((x, y))

    # return number of points that appear twice
    return len(list(filter(lambda x: x > 1, Counter(line_list).values())))


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_05.txt"))
    print(part_two("aoc/inputs/day_05.txt"))
