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
