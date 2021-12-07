def part_one(file_path: str) -> int:
    """
    runs laternfish simulation for 80 days


    Args:
        file_path (str): [description]

    Returns:
        int: fish population
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    return sum(lanternfish_simulation(lines, 80))


def part_two(file_path: str) -> int:
    """
    runs laternfish simulation for 256 days

    Args:
        file_path (str):

    Returns:
        int: fish population
    """
    with open(file_path) as f:
        lines = f.readlines()

    return sum(lanternfish_simulation(lines, 256))


def get_initial_state(lines: list, initial_time: int) -> list:
    """
    returns a list where each indice is the number of fish with that
    amount of time before breeding for the initial state.

    i.e. the number at position 3 is the number of lanternfish who will
    give birth in 3 days.

    Args:
        lines (list): input text
        initial_time (int): time for lantern fish to breed after being born

    Returns:
        list: timer on each fish population after 0 days
    """

    state = [int(i) for i in lines[0].split(",")]

    time_count = [0 for i in range(initial_time + 1)]

    for time in state:
        time_count[time] += 1

    return time_count


def lanternfish_simulation(lines: list, n: int) -> list:
    """
    runs lanternfish simulation for n days

    Args:
        lines (list): input text
        n (int): n days

    Returns:
        list: timer on each fish population after n days
    """
    initial_time = 8
    normal_time = 6

    time_count = get_initial_state(lines, initial_time)

    for i in range(n):
        # get the number of fish that breed
        n_breeders = time_count.pop(0)
        # append the number of babies with a longer time
        time_count.append(n_breeders)
        # reset the timer on the normal breeders
        time_count[normal_time] += n_breeders

    return time_count


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_06.txt"))
    print(part_two("aoc/inputs/day_06.txt"))
