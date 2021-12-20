from collections import Counter


def part_one(file_path: str):
    """
    for the optimal polymer after 10 iterations, returns the difference
    between the counts of the most and least common element

    Args:
        file_path (str):

    Returns:
        int: difference between the counts of the most and least common element
    """

    return optimal_polymer(file_path, 10)


def part_two(file_path: str) -> int:
    """
    for the optimal polymer after 40 iterations, returns the difference
    between the most and least common element

    Args:
        file_path (str):

    Returns:
        int: difference between the counts of the most and least common element
    """

    return optimal_polymer(file_path, 40)


def optimal_polymer(file_path: str, n: int) -> int:
    """
    runs the optimal polymer simulation for n iterations

    Args:
        file_path (str): str
        n (int): number of interations

    Returns:
        int: difference between the counts of the most and least common element
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # get the original polymer
    polymer = lines[0].strip()

    # get the count of each neighbouring pair of chars in polymer
    # e.g abcab -> {(a,b):2, (b,c):1, (c,a):1}
    pair_count = dict(Counter(zip(polymer[:-1], polymer[1:])))

    # counts of characters in polymers
    char_count = dict(Counter(polymer))

    # get which neighbouring pairs produce which two neighbouring pairs
    pair_mapping = {
        tuple(line[:2]): [(line[0], line.strip()[-1]), (line.strip()[-1], line[1])]
        for line in lines[2:]
    }

    # get which neighbouring pair produces an extra character
    char_mapping = {tuple(line[:2]): line.strip()[-1] for line in lines[2:]}

    # for n iterations
    for _ in range(n):

        # get the old pair count because everything happens simulataneously
        old_pair_count = pair_count.copy()

        # for each pair in the last polymer
        for pair in old_pair_count.keys():

            # get the number of occurences
            val = old_pair_count[pair]

            # get the added character
            char2 = char_mapping[pair]

            # if in dictionary then add
            if char2 in char_count.keys():
                char_count[char2] += val
            # else set value
            else:
                char_count[char2] = val
            # for the both created pairs
            for pair2 in pair_mapping[pair]:
                # if in dictionary then add
                if pair2 in pair_count.keys():
                    pair_count[pair2] += val
                # else set valu
                else:
                    pair_count[pair2] = val
            # subtract value from existing pair
            pair_count[pair] -= val
    # difference between the counts of the most and least common element
    return max(char_count.values()) - min(char_count.values())


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_14.txt"))
    print(part_two("aoc/inputs/day_14.txt"))
