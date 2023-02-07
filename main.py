import math
from textwrap import wrap

from Utilities.bit_masks import *
from Utilities.bit_operations import *


ATTACK_LUT = []


def display(bitboard: str) -> None:
    line_width = int(math.sqrt(len(bitboard)))
    print('\n'.join([' '.join(wrap(line[::-1], 1)) for line in wrap(bitboard, line_width)]), '\n')


def create_lookup_table(n: int) -> None:
    n_x_n_mask = 2**(n * n) - 1  # to truncate bits added by left-shift

    north_mask = create_north_mask(n)
    south_mask = create_south_mask(n)
    east_mask  = create_east_mask(n)
    west_mask  = create_west_mask(n)

    north_east_mask = create_north_east_mask(n)
    north_west_mask = create_north_west_mask(n) >> (n - 1)
    south_east_mask = create_south_east_mask(n) << (n - 1)
    south_west_mask = create_south_west_mask(n)

    for square in range(n ** 2):
        _file_idx = file_idx(square, n)

        north_ray = north_mask << square
        south_ray = south_mask >> ((n ** 2 - 1) - square)
        east_ray  = (east_mask << square) & ~masked_west_files(_file_idx, n)
        west_ray  = (west_mask >> ((n ** 2 - 1) - square)) & masked_west_files(_file_idx, n)

        north_east_ray = north_east_mask  << square & ~masked_west_files(_file_idx, n)
        north_west_ray = north_west_mask  << square & masked_west_files(_file_idx, n)
        south_east_ray = (south_east_mask >> (n ** 2 - 1 - square)) & ~masked_west_files(_file_idx, n)
        south_west_ray = south_west_mask >> (n ** 2 - 1 - square) & masked_west_files(_file_idx, n)

        attack_bitboard = (north_ray & n_x_n_mask) | \
                          (north_east_ray & n_x_n_mask) | \
                          (east_ray & n_x_n_mask) | \
                          (south_east_ray & n_x_n_mask) | \
                          (south_ray & n_x_n_mask) | \
                          (south_west_ray & n_x_n_mask) | \
                          (west_ray & n_x_n_mask) | \
                          (north_west_ray & n_x_n_mask)

        ATTACK_LUT.append(attack_bitboard)


if __name__ == '__main__':
    size = 17
    create_lookup_table(size)
    for i in range(size**2):
        display(to_binary_string(size, ATTACK_LUT[i]))
