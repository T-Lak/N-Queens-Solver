from textwrap import wrap

from Utilities.bit_masks import *
from Utilities.bit_operations import *


ATTACK_LUT = []


def display(_size: int, bitboard: str) -> None:
    print('\n'.join([' '.join(wrap(line[::-1], 1)) for line in wrap(bitboard, _size)]), '\n')


def create_lookup_table(_size: int) -> None:
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

        north = north_mask << square
        south = south_mask >> ((_size ** 2 - 1) - square)
        east  = (east_mask << square) & ~masked_west_files(_file_idx, _size)
        west  = (west_mask >> ((_size ** 2 - 1) - square)) & masked_west_files(_file_idx, _size)

        north_east = north_east_mask << square & ~masked_west_files(_file_idx, _size)
        north_west = north_west_mask << square & masked_west_files(_file_idx, _size)
        south_east = (south_east_mask >> (_size**2 - 1 - square)) & ~masked_west_files(_file_idx, _size)
        south_west = south_west_mask >> (size**2 - 1 - square) & masked_west_files(_file_idx, _size)

        # formatting
        formatted_north_mask = to_binary_string(_size, north)[-_size**2:]
        formatted_south_mask = to_binary_string(_size, south)[:_size**2]
        formatted_east_mask  = to_binary_string(_size, east)[-_size**2:]
        formatted_west_mask  = to_binary_string(_size, west)[-_size**2:]

        formatted_nw_mask = to_binary_string(_size, north_west)[-_size**2:]
        formatted_ne_mask = to_binary_string(_size, north_east)[-_size**2:]
        formatted_sw_mask = to_binary_string(_size, south_west)[-_size**2:]
        formatted_se_mask = to_binary_string(_size, south_east)[-_size**2:]

        attack_bitboard = int(formatted_north_mask, 2) | \
                          int(formatted_south_mask, 2) | \
                          int(formatted_east_mask, 2)  | \
                          int(formatted_west_mask, 2)  | \
                          int(formatted_nw_mask, 2)    | \
                          int(formatted_ne_mask, 2)    | \
                          int(formatted_sw_mask, 2)    | \
                          int(formatted_se_mask, 2)

        ATTACK_LUT.append(attack_bitboard)


if __name__ == '__main__':
    size = 7
    create_lookup_table(size)
    for i in range(size**2):
        display(size, to_binary_string(size, ATTACK_LUT[i]))
