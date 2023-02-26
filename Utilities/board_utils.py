import math
from textwrap import wrap

from Utilities.bit_masks import ZERO, BIT


def rank_idx(_square: int, n: int):
    """
    Calculates the square's rank (row) of any given board size.
    :param _square: int that represents the square
    :param n: board width
    :return: rank/row of the square
    """
    return _square // n


def file_idx(_square: int, n: int):
    """
    Calculates the square's file (column) of any given board size.
    :param _square: int that represents the square
    :param n: board width
    :return: file/column of the square
    """
    return _square % n


def count_bits_set(bitboard: int) -> int:
    return bin(bitboard).count("1")


def board_without_square(_square: int, bb: int) -> int:
    return bb ^ (BIT << _square)


def square(file: int, n: int) -> int:
    _file_idx = file_idx(file, n)
    _rank_idx = rank_idx(file, n)
    return 0


def bit_scan_forward(bitboard: int) -> list:
    """
    Computes the pieces' positions by counting
    the distance of the least significant bit.
    :param bitboard: given board state
    :return: list of squares (Positions of the pieces)
    """
    squares = []
    bit_idx = 0
    while bitboard:
        if bitboard & 1:
            squares.append(bit_idx)
        bitboard >>= 1
        bit_idx += 1
    return squares


def rotate_90_deg_clockwise(bitboard: int, n: int) -> int:
    """
    Rotates a given bitboard by 90 degrees.
    :param bitboard: given bitboard
    :param n: board width
    :return: rotated bitboard
    """
    squares = bit_scan_forward(bitboard)
    bb = ZERO
    for _, square in enumerate(squares):
        _file_idx = square // n
        _rank_idx = (n-1) - (square % n)
        bb |= 1 << ((n * _rank_idx) + _file_idx)
    return bb


def display(bitboard: str) -> None:
    """
    Prints the bitboard by separating the lines. 1 stands for a possible attack
    or a piece, 0 stands for an empty square
    :param bitboard: any given bitboard
    :return: None
    """
    line_width = int(math.sqrt(len(bitboard)))
    print('\n'.join([' '.join(wrap(line[::-1], 1)) for line in wrap(bitboard, line_width)]), '\n')


def to_binary_string(bitboard: int, n: int) -> str:
    """
    Transforms a bitboard from int to a binary string. The format
    is given by the bitboard's number of fields (n * n).
    :param bitboard: bitboard to transform
    :param n: board width
    :return: bitboard as binary string
    """
    binary_repr = f'{{:0{n**2}b}}'
    return binary_repr.format(bitboard)


def bitboard_repr(bitboard: int, n: int) -> str:
    """
    Transforms a bitboard from int to a binary string. The format
    is given by the bitboard's number of fields (n * n).
    :param bitboard: bitboard to transform
    :param n: board width
    :return: bitboard as binary string
    """
    binary_repr = f'{{:0{n**2}b}}'
    return binary_repr.format(bitboard).replace('0', '_').replace('1', 'Q')
