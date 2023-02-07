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

    for square in range(_size**2):
        _file_idx = file_idx(square, _size)

        north_ray = north_mask << square
        south_ray = south_mask >> ((_size ** 2 - 1) - square)
        east_ray  = (east_mask << square) & ~masked_west_files(_file_idx, _size)
        west_ray  = (west_mask >> ((_size ** 2 - 1) - square)) & masked_west_files(_file_idx, _size)

        north_east_ray = north_east_mask  << square & ~masked_west_files(_file_idx, _size)
        north_west_ray = north_west_mask  << square & masked_west_files(_file_idx, _size)
        south_east_ray = (south_east_mask >> (_size**2 - 1 - square)) & ~masked_west_files(_file_idx, _size)
        south_west_ray = south_west_mask  >> (_size**2 - 1 - square) & masked_west_files(_file_idx, _size)

        attack_bitboard = (north_ray & n_bits) | \
                          (north_east_ray & n_bits) | \
                          (east_ray & n_bits) | \
                          (south_east_ray & n_bits) | \
                          (south_ray & n_bits) | \
                          (south_west_ray & n_bits) | \
                          (west_ray & n_bits) | \
                          (north_west_ray & n_bits)

        ATTACK_LUT.append(attack_bitboard)


if __name__ == '__main__':
    size = 17
    create_lookup_table(size)
    for i in range(size**2):
        display(to_binary_string(size, ATTACK_LUT[i]))
