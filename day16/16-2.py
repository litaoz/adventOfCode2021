'''
--- Part Two ---
Now that you have the structure of your transmission decoded, you can calculate the value of the expression it represents.

Literal values (type ID 4) represent a single number as described above. The remaining type IDs are more interesting:

Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
Using these rules, you can now work out the value of the outermost packet in your BITS transmission.

For example:

C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
04005AC33890 finds the product of 6 and 9, resulting in the value 54.
880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
D8005AC2A8F0 produces 1, because 5 is less than 15.
F600BC2D8F produces 0, because 5 is not greater than 15.
9C005AC2F8F0 produces 0, because 5 is not equal to 15.
9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.
What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?
'''

from typing import Tuple
import math

input_filename = 'input16-2.txt'


class Packet:
    def __init__(self, message, index):

        # version, type_id, literal=None, length_type=None,
        version_len = 3
        type_id_len = 3
        literal_len = 5
        length_type_len = 1
        subpackets_bits_len = 15
        subpackets_num_len = 11

        self.subpackets = None

        self.version = int(message[index: index + version_len], 2)
        index += version_len

        self.type_id = int(message[index: index + type_id_len], 2)
        index += type_id_len

        if self.type_id == 4:
            literals = []
            safety = 0
            while safety < 1000:
                safety += 1
                literal_group = message[index: index + literal_len]
                index += literal_len

                control = literal_group[0]
                literal = literal_group[1:]
                literals.append(literal)

                if control == '0':
                    break

            assert safety < 1000
            literals_str = ''.join(literals)
            self.literal = int(literals_str, 2)
            self.last_index = index
            return

        # Operation packet (Not packet type 4)
        # Length_type
        self.length_type = int(message[index: index + length_type_len], 2)
        index += length_type_len
        if self.length_type == 0:
            self.subpackets_bits = int(
                message[index: index + subpackets_bits_len], 2)
            index += subpackets_bits_len

            end_bit = index + self.subpackets_bits
            self.subpackets = []
            safety = 0
            while index < end_bit and safety < 1000:
                subpacket = Packet(message, index)
                self.subpackets.append(subpacket)
                index = subpacket.last_index
                safety += 1

            assert safety < 1000
            self.last_index = index

        else:
            self.subpackets_num = int(
                message[index: index + subpackets_num_len], 2)
            index += subpackets_num_len

            self.subpackets = []
            for _ in range(self.subpackets_num):
                subpacket = Packet(message, index)
                self.subpackets.append(subpacket)
                index = subpacket.last_index
                # check if that is correct

        self.last_index = index

    def get_value(self):
        if self.type_id == 0:
            return sum([packet.get_value() for packet in self.subpackets])
        elif self.type_id == 1:
            return math.prod([packet.get_value() for packet in self.subpackets])
        elif self.type_id == 2:
            return min([packet.get_value() for packet in self.subpackets])
        elif self.type_id == 3:
            return max([packet.get_value() for packet in self.subpackets])
        elif self.type_id == 4:
            return self.literal
        elif self.type_id == 5:
            return int(self.subpackets[0].get_value() > self.subpackets[1].get_value())
        elif self.type_id == 6:
            return int(self.subpackets[0].get_value() < self.subpackets[1].get_value())
        elif self.type_id == 7:
            return int(self.subpackets[0].get_value() == self.subpackets[1].get_value())

    def get_total_version(self):
        if self.subpackets is None:
            return self.version
        return self.version + sum([subpacket.get_total_version() for subpacket in self.subpackets])


def convert_to_binary(hex):
    str_len = len(hex)
    num_of_bits = str_len * 4
    return bin(int(hex, 16))[2:].zfill(num_of_bits)


def parse_input(input_filename) -> Tuple[str, dict]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()

    hex_string = input_data_raw[0]
    binary_string = convert_to_binary(hex_string)
    return Packet(binary_string, 0)


def main():
    packet = parse_input(input_filename)
    return packet.get_value()


if __name__ == "__main__":
    result = main()
    print(result)  # 2223947372407
