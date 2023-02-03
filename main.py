from textwrap import wrap

from Utilities.bit_operations import *

NORTH_RAY = []
SOUTH_RAY = []
EAST_RAY  = []
WEST_RAY  = []

NORTH_CUT = []
EAST_CUTb = []
SOUTH_CUT = []
WEST_CUT  = []

NORTH_EAST_RAY = []
SOUTH_WEST_RAY = []
NORTH_WEST_RAY = []
SOUTH_EAST_RAY = []

CLEAR_RANK = [
    0xFFFFFFFFFFFFFF00, 0xFFFFFFFFFFFF00FF, 0xFFFFFFFFFF00FFFF, 0xFFFFFFFF00FFFFFF,
    0xFFFFFF00FFFFFFFF, 0xFFFF00FFFFFFFFFF, 0xFF00FFFFFFFFFFFF, 0x00FFFFFFFFFFFFFF,
]

CLEAR_FILE = [
    0xFEFEFEFEFEFEFEFE, 0xFDFDFDFDFDFDFDFD, 0xFBFBFBFBFBFBFBFB, 0xF7F7F7F7F7F7F7F7,
    0xEFEFEFEFEFEFEFEF, 0xDFDFDFDFDFDFDFDF, 0xBFBFBFBFBFBFBFBF, 0x7F7F7F7F7F7F7F7F,
]

MASK_RANK = [
    0x00000000000000FF, 0x000000000000FF00, 0x0000000000FF0000, 0x00000000FF000000,
    0x000000FF00000000, 0x0000FF0000000000, 0x00FF000000000000, 0xFF00000000000000,
]

MASK_FILE = [
    0x0101010101010101, 0x0202020202020202, 0x0404040404040404, 0x0808080808080808,
    0x1010101010101010, 0x2020202020202020, 0x4040404040404040, 0x8080808080808080,
]


def display(bitboard: str) -> None:
    print('\n'.join([' '.join(wrap(line[::-1], 1)) for line in wrap(bitboard, 8)]))


def create_lookup_tables() -> None:
    mask            = 0xFFFFFFFFFFFFFFFF
    north_mask      = 0x0101010101010100
    south_mask      = 0x0080808080808080
    north_east_mask = 0x8040201008040200
    north_west_mask = 0x0102040810204000

    for sq in range(64):
        north_east = (north_east_mask & (mask >> 8 * (sq % 8))) << sq
        north_west = (north_west_mask >> 7) << sq & rotate_90_clockwise((mask >> 8 * (7 - (sq & 7))))

        north = north_mask << sq
        east  = 2 * ((1 << (sq | 7)) - (1 << sq))
        south = south_mask >> (63 - sq)
        west  = (1 << sq) - (1 << (sq & 56))

        NORTH_RAY.append(to_binary_string(north)[-64:])
        EAST_RAY.append(to_binary_string(east)[-64:])
        SOUTH_RAY.append(to_binary_string(south)[:64])
        WEST_RAY.append(to_binary_string(west)[-64])

        NORTH_WEST_RAY.append(to_binary_string(north_west)[-64:])
        NORTH_EAST_RAY.append(to_binary_string(north_east)[-64:])
        SOUTH_EAST_RAY.insert(0, to_binary_string(rotate_180(north_west))[-64:])
        SOUTH_WEST_RAY.insert(0, to_binary_string(rotate_180(north_east))[-64:])


if __name__ == '__main__':
    create_lookup_tables()
    for i in range(64):
        display(NORTH_RAY[i])
        print()
