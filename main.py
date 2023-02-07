import math
from textwrap import wrap

from Utilities.bit_masks import *
from Utilities.bit_operations import *


ATTACK_LUT = []


def display(bitboard: str) -> None:
    line_width = int(math.sqrt(len(bitboard)))
    print('\n'.join([' '.join(wrap(line[::-1], 1)) for line in wrap(bitboard, line_width)]), '\n')


def create_lookup_table(_size: int) -> None:
    n_bits = 2**(_size*_size) - 1  # to truncate bits added by left shift

    north_mask = create_north_mask(_size)
    south_mask = create_south_mask(_size)
    east_mask  = create_east_mask(_size)
    west_mask  = create_west_mask(_size)

    north_east_mask = create_north_east_mask(_size)
    north_west_mask = create_north_west_mask(_size) >> (_size - 1)
    south_east_mask = create_south_east_mask(_size) << (_size - 1)
    south_west_mask = create_south_west_mask(_size)

    for square in range(_size ** 2):
        _file_idx = file_idx(square, _size)

        north = (north_mask << square) & n_bits
        south = (south_mask >> ((_size ** 2 - 1) - square)) & n_bits
        east  = ((east_mask << square) & ~masked_west_files(_file_idx, _size)) & n_bits
        west  = ((west_mask >> ((_size ** 2 - 1) - square)) & masked_west_files(_file_idx, _size)) & n_bits

        north_east = (north_east_mask  << square & ~masked_west_files(_file_idx, _size)) & n_bits
        north_west = (north_west_mask  << square & masked_west_files(_file_idx, _size)) & n_bits
        south_east = ((south_east_mask >> (_size**2 - 1 - square)) & ~masked_west_files(_file_idx, _size)) & n_bits
        south_west = (south_west_mask  >> (size**2 - 1 - square) & masked_west_files(_file_idx, _size)) & n_bits

        attack_bitboard = north | north_east | east | south_east | south | south_west | west | north_west

        ATTACK_LUT.append(attack_bitboard)


if __name__ == '__main__':
    size = 7
    create_lookup_table(size)
    for i in range(size**2):
        display(to_binary_string(size, ATTACK_LUT[i]))
