import math
from textwrap import wrap


def to_binary_string(bitboard: int, n: int) -> str:
    """
    Transforms a bitboard from int to a binary string. The format
    is given by the bitboards width.
    :param bitboard: bitboard to transform
    :param n: board width
    :return: bitboard as binary string
    """
    binary_repr = f'{{:0{n**2}b}}'
    return binary_repr.format(bitboard)


def rank_idx(square: int, n: int):
    """
    Calculates the square's rank (row) of any given board size.
    :param square: int that represents the square
    :param n: board width
    :return: rank/row of the square
    """
    return square // n


def file_idx(square: int, n: int):
    """
    Calculates the square's file (column) of any given board size.
    :param square: int that represents the square
    :param n: board width
    :return: file/column of the square
    """
    return square % n


def display(bitboard: str) -> None:
    """
    Prints the bitboard by separating the lines. 1 stands for a possible attack
    or a piece, 0 stands for an empty square
    :param bitboard: any given bitboard
    :return: None
    """
    line_width = int(math.sqrt(len(bitboard)))
    print('\n'.join([' '.join(wrap(line[::-1], 1)) for line in wrap(bitboard, line_width)]), '\n')
