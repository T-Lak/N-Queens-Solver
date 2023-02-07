import math
from textwrap import wrap

from Utilities.bit_operations import *
from Utilities.lookup_tables import create_attack_lut, ATTACK_LUT


def display(bitboard: str) -> None:
    line_width = int(math.sqrt(len(bitboard)))
    print('\n'.join([' '.join(wrap(line[::-1], 1)) for line in wrap(bitboard, line_width)]), '\n')


if __name__ == '__main__':
    size = 7
    create_attack_lut(size)
    for i in range(size**2):
        display(to_binary_string(size, ATTACK_LUT[i]))
