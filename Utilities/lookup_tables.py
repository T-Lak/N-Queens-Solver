from Utilities.bit_masks import *
from Utilities.board_utils import file_idx, bit_scan_forward

ATTACK_LUT        = []
FILE_MASK_LUT     = []
CLEAR_FILE_LUT    = []
RANK_MASK_LUT     = []
CLEAR_RANK_LUT    = []
FILE_SQUARE_LUT   = {}
ALL_SOLUTIONS_LUT = {
    1: 1,
    2: 0,
    3: 0,
    4: 2,
    5: 10,
    6: 4,
    7: 40,
    8: 92,
    9: 352,
    10: 724,
    11: 2680,
    12: 14200,
    13: 73712,
}


def create_attack_lut(n: int) -> None:
    """
    Creates a lookup table containing all attacks a queen can perform from any given square.
    :param n: board width
    :return: None
    """
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


def create_file_masks(n: int) -> None:
    """
    Creates file masks for a given board size and stores them
    in a lookup table.
    :param n: board width
    :return: None
    """
    mask = create_north_mask(n) | 0x1
    FILE_MASK_LUT.append(mask)
    CLEAR_FILE_LUT.append(invert(mask, n))
    for i in range(1, n):
        FILE_MASK_LUT.append(mask << i)
        CLEAR_FILE_LUT.append(invert(mask << i, n))


def create_rank_masks(n: int) -> None:
    """
    Creates rank masks for a given board size and stores them
    in a lookup table.
    :param n: board width
    :return: None
    """
    mask = create_east_mask(n) | 0x1
    RANK_MASK_LUT.append(mask)
    for i in range(1, n):
        RANK_MASK_LUT.append(mask << n * i)


def create_file_square_lut(n: int) -> None:
    """
    Creates a lookup table that maps all square numbers to each
    file of a given board
    :param n: board width
    :return: None
    """
    for i, file in enumerate(FILE_MASK_LUT):
        FILE_SQUARE_LUT[i] = bit_scan_forward(file)


def mirror_horizontally(bitboard: int, n: int) -> int:
    """
    Mirrors a given bitboard horizontally
    :param bitboard: given bitboard
    :param n: board width
    :return: horizontally mirrored bitboard
    """
    bb = ZERO
    lo = n // 2
    for _file_idx in range(lo):
        new_square = (n-1) - _file_idx
        bb |= (bitboard & FILE_MASK_LUT[_file_idx]) << (new_square - _file_idx)
    for _file_idx in range(lo, n):
        new_square = (n - 1) - _file_idx
        bb |= (bitboard & FILE_MASK_LUT[_file_idx]) >> (_file_idx - new_square)
    return bb


def mirror_vertically(bitboard: int, n: int) -> int:
    """
    Mirrors a given bitboard vertically
    :param bitboard: given bitboard
    :param n: board width
    :return: vertically mirrored bitboard
    """
    bb = ZERO
    lo = n // 2
    for _rank_idx in range(lo):
        new_square = (n-1) - _rank_idx
        bb |= (bitboard & RANK_MASK_LUT[_rank_idx]) << (n * (new_square - _rank_idx))
    for _rank_idx in range(lo, n):
        new_square = (n - 1) - _rank_idx
        bb |= (bitboard & RANK_MASK_LUT[_rank_idx]) >> (n * (_rank_idx - new_square))
    return bb
