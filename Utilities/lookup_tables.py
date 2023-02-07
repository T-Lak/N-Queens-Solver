from Utilities.bit_masks import *
from Utilities.bit_operations import file_idx

ATTACK_LUT = []


def create_attack_lut(n: int) -> None:
    nxn_mask = 2**(n * n) - 1  # to truncate bits added by left-shift

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
        south_west_ray = south_west_mask  >> (n ** 2 - 1 - square) & masked_west_files(_file_idx, n)

        attack_bitboard = north_ray | \
                          north_east_ray | \
                          east_ray | \
                          south_east_ray | \
                          south_ray | \
                          south_west_ray | \
                          west_ray | \
                          north_west_ray

        ATTACK_LUT.append(attack_bitboard & nxn_mask)