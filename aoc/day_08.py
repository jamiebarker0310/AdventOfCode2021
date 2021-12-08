import json
from os import P_NOWAITO, remove

letter_length_to_number = {
    2:[1],
    3:[7],
    4:[4],
    5:[2,3,5],
    6:[0,6,9],
    7:[8]
}

number_to_position = {
    0:"abcefg",
    1:"cf",
    2:"acdeg",
    3:"acdfg",
    4:"bcdf",
    5:"abdfg",
    6:"abdefg",
    7:"acf",
    8:"abcdefg",
    9:"abcdfg"
}

position_to_number = {value: key for key, value in number_to_position.items()}

number_to_position = {key: set(value) for key, value in number_to_position.items()}

number_to_antiposition = {key: set("abcdefg") - value for key, value in number_to_position.items()}


def part_one(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """
    # read file
    with open(file_path) as f:
        lines = f.readlines()

    count = 0

    for line in lines:
        patterns, output = tuple(map(lambda x: x.split(" ") ,line.strip().split(" | ")))

        for character in output:

            if len(character) in [2,3,4,7]:

                count += 1

    return count


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """


    # read file
    with open(file_path) as f:
        lines = f.readlines()

    sum1 = 0
    for line in lines:
        patterns, outputs = tuple(map(lambda x: x.split(" ") ,line.strip().split(" | ")))

        # initially every letter can map to every other letter
        letters_dict = {letter: set("abcdefg") for letter in "abcdefg"}

        # for each pattern
        mapping = get_mapping(patterns)

        rev_mapping = {value: key for key, value in mapping.items()}

        init_str = ""
        for output in outputs:

            init_str += str(position_to_number["".join(sorted([rev_mapping[letter] for letter in output]))])

        sum1 += int(init_str)

    return sum1

def get_mapping(patterns):

    # initially every letter can map to every other letter
    letters_dict = {letter: set("abcdefg") for letter in "abcdefg"}

    # for each pattern
    for pattern in patterns:
        # get the length to work out which possible numbers the pattern could be
        letter_length = len(pattern)
        pattern = set(pattern)

        must_positions = set("abcdefg")
        must_not_positions = set("abcdefg")
        for number in letter_length_to_number[letter_length]:
            must_positions = must_positions.intersection(number_to_position[number])
            must_not_positions = must_not_positions.intersection(number_to_antiposition[number])

        for letter in must_positions:
            letters_dict[letter] = letters_dict[letter].intersection(pattern)

        for letter in must_not_positions:
            letters_dict[letter] = letters_dict[letter] - pattern

    for key1, value1 in letters_dict.items():

        if len(value1) == 1:

            value1 = value1.pop()
            letters_dict[key1] = set(value1)

            for key2, value2 in letters_dict.items():

                if key1!=key2 and value1 in value2:

                    value2.remove(value1)

    
    return {key: value.pop()  for key, value in letters_dict.items()}


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_08.txt"))
    print(part_two("aoc/inputs/day_08.txt"))
