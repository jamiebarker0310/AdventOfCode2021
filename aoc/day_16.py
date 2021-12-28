import numpy as np

class Packet:

    def __init__(self, bits):
        self.version = int(bits[:3], 2)
        self.type_id = int(bits[3:6], 2)
        self.literal = self.type_id == 4

        self.value = None
        self.subpackets = []
        self.remaining_bits = None


        if self.literal:
            self.bits = bits[6:]
            self.calculate_literal_value()
        
        else:
            self.length_id = bits[6]
            self.bits = bits[7:]
            self.calculate_subpackets()
    
    def calculate_literal_value(self):

        bin_str = ""
        for i in range(0, len(self.bits), 5):
            bin_str += self.bits[i + 1 : i + 5]

            if self.bits[i] == "0":
                self.value = int(bin_str, 2)
                self.remaining_bits = self.bits[i+5:]
                return self.value
    
    def calculate_subpackets(self):

        if self.length_id == 0:
            length = int(self.bits[:15], 2)
            self.bits = self.bits[15:]
        
        else:
            n_subpackets = int(self.bits[:11], 2)
            self.bits = self.bits[11:]
            
        subpacket = Packet(self.bits)
        self.subpackets.append(subpacket)

        remaining_bits = subpacket.remaining_bits
        while remaining_bits != "0" * len(remaining_bits):
            subpacket = Packet(remaining_bits)
            self.subpackets.append(subpacket)
            remaining_bits = subpacket.remaining_bits




        if length_id == 1:
            


        




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
    total = 0
    for line in lines:
        # convert to binary
        bin_line = convert_to_binary(line.strip())

        version_sum = parse_packets_1(bin_line)

        total += version_sum

    return total


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
    total = 0
    for line in lines:
        # convert to binary
        bin_line = convert_to_binary(line.strip())

        total += parse_packets_2(bin_line)

    return total


def parse_packets_1(bin_line) -> str:

    if bin_line == "0" * len(bin_line):
        return 0

    version = int(bin_line[:3], 2)
    type_id = int(bin_line[3:6], 2)
    total = 0

    if type_id == 4:
        subpackets = bin_line[6:]
        bin_str = ""
        for i in range(0, len(subpackets), 5):
            bin_str += subpackets[i + 1 : i + 5]
            if subpackets[i] == "0":
                return version + parse_packets_1(subpackets[i + 5 :])

    else:
        length_id = int(bin_line[6])
        subpackets = bin_line[7:]
        if length_id == 0:
            length = int(subpackets[:15], 2)
            subpackets = subpackets[15:]
            return version + parse_packets_1(subpackets)

        if length_id == 1:
            n_subpackets = int(subpackets[:11], 2)
            subpackets = subpackets[11:]
            return version + parse_packets_1(subpackets)

    return total


def parse_packets_2(bin_line) -> str:

    if bin_line == "0" * len(bin_line):
        return []

    version = int(bin_line[:3], 2)
    type_id = int(bin_line[3:6], 2)
    total = 0

    print(bin_line)
    print(version, type_id)

    if type_id == 4:
        subpackets = bin_line[6:]
        bin_str = ""
        for i in range(0, len(subpackets), 5):
            bin_str += subpackets[i + 1 : i + 5]
            if subpackets[i] == "0":
                other_subpackets = parse_packets_2(subpackets[i + 5 :])
                print("OTHER_SUBPACKETS :", other_subpackets)
                return [int(bin_str, 2)] + other_subpackets

    else:
        length_id = int(bin_line[6])
        subpackets = bin_line[7:]
        if length_id == 0:
            length = int(subpackets[:15], 2)
            subpackets = subpackets[15:]
            return_subpackets(subpackets, type_id)

        if length_id == 1:
            n_subpackets = int(subpackets[:11], 2)
            subpackets = subpackets[11:]
            return_subpackets(subpackets, type_id)

    return total


def return_subpackets(subpackets, type_id):

    if type_id == 0:
        return sum(parse_packets_2(subpackets))
    if type_id == 1:
        return np.prod(parse_packets_2(subpackets))
    if type_id == 2:
        return min(parse_packets_2(subpackets))
    if type_id == 3:
        return max(parse_packets_2(subpackets))
    if type_id == 5:
        subpackets = parse_packets_2(subpackets)
        return int(subpackets[0] > subpackets[1])
    if type_id == 6:
        subpackets = parse_packets_2(subpackets)
        return int(subpackets[0] < subpackets[1])
    if type_id == 7:
        subpackets = parse_packets_2(subpackets)
        return int(subpackets[0] == subpackets[1])


def convert_to_binary(hex_str: str) -> str:

    hex_to_bin = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }

    return "".join(map(lambda x: hex_to_bin[x], hex_str))


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_16.txt"))
    print(part_two("aoc/inputs/day_16.txt"))
