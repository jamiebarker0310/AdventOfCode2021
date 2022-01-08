from typing import List


def part_one(file_path: str):
    """
    Calculates the highest point during a velocity that
    goes through the selected range

    Args:
        file_path (str):

    Returns:
        int: highest position
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # read line
    line = lines[0]

    # get max y bounds
    line = line[line.index("y=") + 2 :]

    # get ymin and ymax
    ymin, ymax = [int(x) for x in line.split("..")]

    # because we know ymin and ymax are both negative
    if ymin < 0:
        ymin = abs(ymin) - 1
    if ymax < 0:
        ymax = abs(ymax) - 1

    # maximum y position is when t = v0
    return get_y_position(max(ymin, ymax), max(ymin, ymax))


def part_two(file_path: str):
    """
    gets the number of possible initial velocities with a
    subsequent trajectory that passes through the range

    Args:
        file_path (str):

    Returns:
        int: number of trajectories
    """
    # get all initial velocities
    pairs = get_pairs(file_path)

    return len(pairs)


def get_pairs(file_path: str) -> List:
    """
    get all possible initial velocities with a
    subsequent trajectory that passes through the range

    Args:
        file_path (str):

    Returns:
        List: list of initial velocities
    """
    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # read line
    line = lines[0]
    # parse bounds
    xmin, xmax = [
        int(x) for x in line[line.index("x=") + 2 : line.index(", ")].split("..")
    ]
    ymin, ymax = [int(x) for x in line[line.index("y=") + 2 :].split("..")]
    # initialise set of pairs
    pairs = set()
    # for initial x velocity in the range 1, x max
    for vx0 in range(1, abs(xmax) + 1):
        # for initial y velocity in range going up or down
        for vy0 in range(-abs(ymin) - 1, abs(ymin) + 1):
            # initialse velocity
            vx = vx0
            vy = vy0
            # initialise position
            px = 0
            py = 0
            # while position is left of xmax and above ymin
            while px <= xmax and py >= ymin:
                # move the position
                px += vx
                py += vy
                # adjust velocity
                vx = max(vx - 1, 0)
                vy -= 1
                # if inside range
                if px in range(xmin, xmax + 1) and py in range(ymin, ymax + 1):
                    # add to pairs
                    pairs.add((vx0, vy0))
                    # break loop
                    break
    return list(pairs)


def get_x_position(initial_velocity: int, t: int) -> int:
    """
    calculate x position for a given initial velocity and time

    Args:
        initial_velocity (int): intiail x velocity
        t (int): time

    Returns:
        int: x position
    """

    if t > initial_velocity:
        return (initial_velocity * (initial_velocity + 1)) / 2
    else:
        return t * (2 * initial_velocity - (t - 1)) / 2


def get_y_position(initial_velocity: int, t: int) -> int:
    """
    calculate y position for a given initial velocity and time

    Args:
        initial_velocity (int): intiail y velocity
        t (int): time

    Returns:
        int: x position
    """
    return t * (2 * initial_velocity - (t - 1)) / 2


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_17.txt"))
    print(part_two("aoc/inputs/day_17.txt"))
