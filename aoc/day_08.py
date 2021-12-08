from collections import Counter

letter_length_to_number = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}

position_to_number = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def part_one(file_path: str) -> int:
    """
    counts the number of patterns in the output that
    have 2,3,4 or 7 liens

    Args:
        file_path (str):

    Returns:
        int: the number of patterns in the output that have 2,3,4 or 7 liens
    """
    # read file
    with open(file_path) as f:
        lines = f.readlines()

    count = 0

    for line in lines:
        _, output = tuple(map(lambda x: x.split(" "), line.strip().split(" | ")))

        for character in output:

            if len(character) in [2, 3, 4, 7]:

                count += 1

    return count


def part_two(file_path: str) -> int:
    """
    calculates sum of decrypted output

    Args:
        file_path (str):

    Returns:
        int: sum of decrypted output
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    sum1 = 0
    for line in lines:
        patterns, outputs = tuple(
            map(lambda x: x.split(" "), line.strip().split(" | "))
        )
        # for each pattern
        mapping = get_mapping(patterns)

        init_str = ""
        for output in outputs:

            init_str += str(
                position_to_number[
                    "".join(sorted([mapping[letter] for letter in output]))
                ]
            )

        sum1 += int(init_str)

    return sum1


def get_mapping(patterns: list) -> dict:
    """
    decrypts patterns using following logic
    we know if there are 4 of any character then it represents e
    we know if there are 6 of any character then it represents b
    we know if there are 9 of any character then it represents f

    we know that the difference between pattern of length 2 and
    length 3, represents a

    then we can deduce the other is c

    for the last pair, we now know abce and f so we can find the pattern
    with 6 lines with only one extra uncoded element. This is from the
    pattern representing 0 and hence that uncoded element is g

    that leaves only d remaining for the final element

    Args:
        patterns (list): list of patterns

    Returns:
        dict: mapping of code to position
    """

    count_map = {4: set("e"), 6: set("b"), 7: set("dg"), 8: set("ac"), 9: set("f")}

    # maps code to position
    map_dict = {
        key: count_map[value] for key, value in Counter("".join(patterns)).items()
    }

    p2, p3, p6s = get_length_splits(patterns)

    # difference between 2 and 3 maps to a
    map_dict[(p3 - p2).pop()] = set("a")

    # the other option with "a" can remove that option
    for key, value in map_dict.items():
        if len(value) == 2 and "a" in value:
            value.remove("a")
            map_dict[key] = value
            break

    # get list of ones with length 6
    # 0 will have one of the unconfirmed elements which corresponds to g
    # the remaining will correspond to d
    confirmed = set(
        [next(iter(key)) for key, value in map_dict.items() if len(value) == 1]
    )
    
    for p6 in p6s:
        diff = p6 - confirmed
        if len(diff) == 1:
            map_dict[diff.pop()] = set("g")
            break

    for key, value in map_dict.items():
        if len(value) == 2:
            map_dict[key] = "d"
        else:
            map_dict[key] = value.pop()

    return map_dict


def get_length_splits(patterns):
    p6s = []
    for p in patterns:
        if len(p) == 2:
            p2 = set(p)
        elif len(p) == 3:
            p3 = set(p)
        elif len(p) == 6:
            p6s += [set(p)]

    return p2, p3, p6s


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_08.txt"))
    print(part_two("aoc/inputs/day_08.txt"))
