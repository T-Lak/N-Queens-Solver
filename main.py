import math
from textwrap import wrap

from Utilities.bit_operations import *
from Utilities.lookup_tables import create_attack_lut, ATTACK_LUT, create_file_masks, FILE_MASK_LUT, RANK_MASK_LUT, \
    create_rank_masks


def display(bitboard: str) -> None:
    line_width = int(math.sqrt(len(bitboard)))
    print('\n'.join([' '.join(wrap(line[::-1], 1)) for line in wrap(bitboard, line_width)]), '\n')


if __name__ == '__main__':
    size = 8
    create_attack_lut(size)
    create_file_masks(size)
    display(to_binary_string((ATTACK_LUT[0] | ATTACK_LUT[23]) & FILE_MASK_LUT[1], size))
    display(to_binary_string(ATTACK_LUT[0], size))
    display(to_binary_string(ATTACK_LUT[23], size))
    # for square in range(size**2):
    #     display(to_binary_string(size, ATTACK_LUT[square]))
