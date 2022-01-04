from typing import List
import numpy as np


class Packet:
    """
    A class to represent and parse a packet

    """

    def __init__(self, bin_str: str) -> None:
        """
        initialise array

        Args:
            bin_str (str): binary string that is parsed
        """
        # initialise bin string
        self.bin_str = bin_str
        # the first three bits encode the packet version
        self.version = int(bin_str[:3], 2)
        # the next three bits encode the packet type ID
        self.type_id = int(bin_str[3:6], 2)
        # Packets with type ID 4 represent a literal value
        self.literal = self.type_id == 4
        # initialise empty subpackets
        self.subpackets = []

        # if literal
        if self.literal:
            # set bits
            self.bits = bin_str[6:]
            # calculate value
            self.calculate_literal_value()
        else:
            # the bit immediately after the packet header is called the length type ID
            self.length_type_id = int(bin_str[6])
            # If the length type ID is 0
            if self.length_type_id == 0:
                # then the next 15 bits are a number that represents the total length in
                # bits of the sub-packets contained by this packet.
                self.total_bit_length = int(bin_str[7 : 7 + 15], 2)
                self.bits = bin_str[7 + 15 :]
            # If the length type ID is 1
            elif self.length_type_id == 1:
                # then the next 11 bits are a number that represents the number
                # of sub-packets immediately contained by this packet.
                self.n_subpackets = int(bin_str[7 : 7 + 11], 2)
                self.bits = bin_str[7 + 11 :]
            # calculate subpackets
            self.calculate_subpackets()

    def calculate_literal_value(self) -> int:
        """
        calculates literal value of Packet

        Returns:
            int: literal value
        """
        # initialise empty binary string
        value_str = ""
        for i in range(0, len(self.bits), 5):
            # add the last 4 of groups of 5
            value_str += self.bits[i + 1 : i + 5]
            # if the initial bit is a 0
            if self.bits[i] == "0":
                # then calculate literal value
                self.literal_value = int(value_str, 2)
                # output remaining bits
                self.remaining_bits = self.bits[i + 5 :]
                # return literal value
                return self.literal_value

    def calculate_subpackets(self) -> List:
        """
        calculates the subpackets of packet

        Returns:
            List[Packet]:
        """
        # if length type id is 0
        if self.length_type_id == 0:
            # calculate how many bits will be remaining
            remaining_bits = self.bits
            initial_length = len(self.bits)
            final_remain_length = initial_length - self.total_bit_length
            # while the remaining bits are longer than the final length
            while len(remaining_bits) > final_remain_length:
                # create new packet
                packet = Packet(remaining_bits)
                # append packet to subpackets
                self.subpackets.append(packet)
                # updates remaining bits
                remaining_bits = packet.remaining_bits
        # if length type id is 1
        elif self.length_type_id == 1:
            # initialise remaining bits
            remaining_bits = self.bits
            # while there are not enough subpackets
            while len(self.subpackets) < self.n_subpackets:
                # create new packet
                packet = Packet(remaining_bits)
                # append packet to subpackets
                self.subpackets.append(packet)
                # updates remaining bits
                remaining_bits = packet.remaining_bits
        # set remaining bits for this packet
        self.remaining_bits = remaining_bits
        # return subpackets
        return self.subpackets

    def calculate_version_sum(self) -> int:
        """
        calculate sum of versions of packet and subsequent subpackets

        Returns:
            int: version sum
        """
        # add version to sum of versions in subpacket
        return self.version + sum(
            [packet.calculate_version_sum() for packet in self.subpackets]
        )

    def calculate_value(self):
        """
        calculate value of packet

        Returns:
            int:
        """

        if self.type_id == 0:
            return sum([packet.calculate_value() for packet in self.subpackets])
        elif self.type_id == 1:
            return np.product([packet.calculate_value() for packet in self.subpackets])
        elif self.type_id == 2:
            return min([packet.calculate_value() for packet in self.subpackets])
        elif self.type_id == 3:
            return max([packet.calculate_value() for packet in self.subpackets])
        elif self.type_id == 4:
            return self.literal_value
        elif self.type_id == 5:
            assert len(self.subpackets) == 2
            s0 = self.subpackets[0].calculate_value()
            s1 = self.subpackets[1].calculate_value()
            cond = s0 > s1
            return int(cond)
        elif self.type_id == 6:
            assert len(self.subpackets) == 2
            s0 = self.subpackets[0].calculate_value()
            s1 = self.subpackets[1].calculate_value()
            cond = s0 < s1
            return int(cond)
        elif self.type_id == 7:
            assert len(self.subpackets) == 2
            s0 = self.subpackets[0].calculate_value()
            s1 = self.subpackets[1].calculate_value()
            cond = s0 == s1
            return int(cond)


def part_one(file_path: str) -> int:
    """
    calculates version sum of packet

    Args:
        file_path (str):

    Returns:
        int: [description]
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # convert to binary
    bin_str = hex_to_bin(lines[0])
    # initialise packet
    packet = Packet(bin_str)
    # calculate version sum
    return packet.calculate_version_sum()


def part_two(file_path: str) -> int:
    """
    calculate value of packet

    Args:
        file_path (str): [description]

    Returns:
        int: packet value
    """
    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # convert to binary
    bin_str = hex_to_bin(lines[0])
    # initialise packet
    packet = Packet(bin_str)
    # calculate version sum
    return packet.calculate_value()


def hex_to_bin(hex_str: str) -> str:
    """
    converts hex string to padded binary

    Args:
        hex_str (str): hex string to convert to binary

    Returns:
        str: padded binary string
    """
    # map of hex code to binary code
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
    # convert hex list to string
    return "".join(hex_to_bin[a] for a in hex_str)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_16.txt"))
    print(part_two("aoc/inputs/day_16.txt"))
